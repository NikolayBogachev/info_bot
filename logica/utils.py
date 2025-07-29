import os
from pathlib import Path
from typing import Optional, Union

from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, InlineKeyboardMarkup, CallbackQuery, Message
import logging


async def edit_message_handler(
        callback: types.CallbackQuery,
        state: FSMContext,
        keyboard: types.InlineKeyboardMarkup,
        text: str = "Выберите действие:",
        new_state: Optional[object] = None
):
    try:
        await callback.message.edit_text(
            text=text,
            reply_markup=keyboard
        )
        await callback.answer()
        if new_state is not None:
            await state.set_state(new_state)
    except Exception as e:
        await callback.answer(f"Ошибка: {str(e)}", show_alert=True)


async def replace_message_handler(
    callback: types.CallbackQuery,
    state: FSMContext,
    keyboard: types.InlineKeyboardMarkup,
    text: str = "Выберите действие:",
    new_state: Optional[object] = None
):
    try:
        await callback.message.delete()
        await callback.message.answer(
            text=text,
            reply_markup=keyboard
        )
        await callback.answer()
        if new_state is not None:
            await state.set_state(new_state)
    except Exception as e:
        await callback.answer(f"Ошибка: {str(e)}", show_alert=True)


async def send_document_handler(
        callback: CallbackQuery,
        state: FSMContext,
        file_path: str,
        keyboard: InlineKeyboardMarkup,
        caption: Optional[str] = None,
        new_state: Optional[object] = None,
        delete_previous: bool = True,
        parse_mode: str = "HTML"
):
    """
    Универсальный обработчик для отправки документов

    :param callback: CallbackQuery объект
    :param state: FSMContext
    :param file_path: Путь к файлу
    :param caption: Подпись к документу
    :param keyboard: Клавиатура
    :param new_state: Новое состояние (опционально)
    :param delete_previous: Удалять ли предыдущее сообщение
    :param parse_mode: Режим парсинга текста
    """
    try:
        # Получаем абсолютный путь к корню проекта (info_bot/)
        project_root = Path(__file__).parent.parent.parent # Предполагаем, что handlers/ внутри info_bot/
        # Нормализуем путь (заменяем / на \ для Windows)
        normalized_path = os.path.normpath(file_path)

        full_file_path = project_root / normalized_path

        print(full_file_path)
        # Проверка существования файла
        if not os.path.exists(full_file_path):
            await callback.answer("❌ Файл не найден!", show_alert=True)
            return

        # Удаление предыдущего сообщения (если нужно)
        if delete_previous:
            await callback.message.delete()

        # Отправка документа
        await callback.message.answer_document(
            document=FSInputFile(full_file_path),
            caption=caption,
            reply_markup=keyboard,
            parse_mode=parse_mode
        )

        # Установка нового состояния (если указано)
        if new_state is not None:
            await state.set_state(new_state)

    except Exception as e:
        await callback.answer(f"⚠️ Ошибка: {str(e)}", show_alert=True)
    finally:
        await callback.answer()




# Настройка логгирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def send_html_template_callback(
        callback: CallbackQuery,
        state: FSMContext,
        html_path: str,
        keyboard: Optional[InlineKeyboardMarkup] = None,
        new_state: Optional[str] = None,
        delete_previous: bool = True,
        **template_vars
) -> bool:
    """
    Улучшенный обработчик HTML-шаблонов для CallbackQuery

    Возвращает:
        True - если сообщение успешно отправлено
        False - если произошла ошибка
    """
    try:
        # Получаем абсолютный путь к корню проекта (info_bot/)
        project_root = Path(__file__).parent.parent.parent # Предполагаем, что handlers/ внутри info_bot/
        normalized_html_path = os.path.normpath(html_path)
        full_html_path = project_root / normalized_html_path

        # 1. Проверка существования файла
        resolved_path = Path(full_html_path).absolute()
        if not resolved_path.exists():
            error_msg = f"Файл не найден: {resolved_path}"
            logger.error(error_msg)
            await callback.answer("❌ Ошибка: файл шаблона не найден", show_alert=True)
            return False

        # 2. Чтение файла
        try:
            html_content = resolved_path.read_text(encoding='utf-8-sig')  # utf-8-sig для файлов с BOM
        except UnicodeDecodeError:
            logger.error(f"Ошибка кодировки файла: {resolved_path}")
            await callback.answer("❌ Ошибка: неправильная кодировка файла", show_alert=True)
            return False

        # 3. Подстановка переменных
        if template_vars:
            try:
                html_content = html_content.format(**template_vars)
            except KeyError as e:
                logger.error(f"Недостающие переменные в шаблоне: {e}")
                await callback.answer("❌ Ошибка в шаблоне", show_alert=True)
                return False

        # 4. Удаление предыдущего сообщения
        if delete_previous:
            try:
                await callback.message.delete()
                logger.info("Предыдущее сообщение удалено")
            except Exception as e:
                logger.warning(f"Не удалось удалить сообщение: {e}")

        # 5. Отправка сообщения
        try:
            await callback.message.answer(
                text=html_content,
                reply_markup=keyboard,
                parse_mode="HTML",
                disable_web_page_preview=True
            )
            logger.info("Сообщение успешно отправлено")
        except Exception as e:
            logger.error(f"Ошибка отправки сообщения: {e}")
            await callback.answer("❌ Ошибка отправки сообщения", show_alert=True)
            return False

        # 6. Обновление состояния
        if new_state is not None:
            await state.set_state(new_state)
            logger.info(f"Установлено новое состояние: {new_state}")

        # 7. Подтверждение callback
        await callback.answer()
        return True

    except Exception as e:
        logger.exception("Критическая ошибка в send_html_template_callback")
        await callback.answer(f"⚠️ Критическая ошибка: {str(e)}", show_alert=True)
        return False


async def handle_error(target: Union[Message, CallbackQuery], text: str):
    """Обработчик ошибок"""
    if isinstance(target, CallbackQuery):
        await target.answer(text, show_alert=True)
    else:
        await target.answer(text)