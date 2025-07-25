from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_start_menu_keyboard() -> InlineKeyboardMarkup:
    kb = [
        [InlineKeyboardButton(text="1C", callback_data="1C")],
        [InlineKeyboardButton(text="Рекламации", callback_data="reclam")],
        [InlineKeyboardButton(text="База знаний", callback_data="db")],
        [InlineKeyboardButton(text="Сервисное обслуживание оборудования", callback_data="service")],
        [InlineKeyboardButton(text="О компании", callback_data="company")],
        [InlineKeyboardButton(text="Проверка вложенности", callback_data="level")],
        [InlineKeyboardButton(text="Техническая поддержка", callback_data="support")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


def get_1c_menu_keyboard() -> InlineKeyboardMarkup:
    kb = [
        [InlineKeyboardButton(text="Создание Заказа Покупателя", callback_data="create_order")],
        [InlineKeyboardButton(text="Выставление счёта", callback_data="create_invoice")],
        [InlineKeyboardButton(text="Возврат от покупателя", callback_data="return")],
        [InlineKeyboardButton(text="Создание контрагента", callback_data="create_contractor")],
        [InlineKeyboardButton(text="Создание номенклатуры", callback_data="create_item")],
        [InlineKeyboardButton(text="<< назад", callback_data="back")],
        [InlineKeyboardButton(text="в меню ↩️", callback_data="main_menu")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


def get_complaints_keyboard() -> InlineKeyboardMarkup:
    kb = [
        [InlineKeyboardButton(text="Клён", callback_data="klen")],
        [InlineKeyboardButton(text="Рестинтернешинл", callback_data="restint")],
        [InlineKeyboardButton(text="Мастергласс", callback_data="masterclass")],
        [InlineKeyboardButton(text="Регион 50 (Проект 2015)", callback_data="region_50")],
        [InlineKeyboardButton(text="Русский проект (Метроном)", callback_data="ru_project")],
        [InlineKeyboardButton(text="<< назад", callback_data="back")],
        [InlineKeyboardButton(text="в меню ↩️", callback_data="main_menu")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


def get_db_keyboard() -> InlineKeyboardMarkup:
    kb = [
        [InlineKeyboardButton(text="Барный инвентарь", callback_data="bar_inventory")],
        [InlineKeyboardButton(text="Сиропы, топинги , пюре", callback_data="topping")],
        [InlineKeyboardButton(text="Оборудование", callback_data="equipment")],
        [InlineKeyboardButton(text="<< назад", callback_data="back")],
        [InlineKeyboardButton(text="в меню ↩️", callback_data="main_menu")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


def get_level_keyboard() -> InlineKeyboardMarkup:
    kb = [
        [InlineKeyboardButton(text="Первый", callback_data="first")],
        [InlineKeyboardButton(text="Второй", callback_data="second")],
        [InlineKeyboardButton(text="Третий", callback_data="third")],
        [InlineKeyboardButton(text="<< назад", callback_data="back")],
        [InlineKeyboardButton(text="в меню ↩️", callback_data="main_menu")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


def get_level2_keyboard() -> InlineKeyboardMarkup:
    kb = [
        [InlineKeyboardButton(text="ПодПодКатегория", callback_data="first_first")],
        [InlineKeyboardButton(text="2 ПодПодКатегория", callback_data="second_second")],
        [InlineKeyboardButton(text="<< назад", callback_data="back")],
        [InlineKeyboardButton(text="в меню ↩️", callback_data="main_menu")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


def get_level3_keyboard() -> InlineKeyboardMarkup:
    kb = [
        [InlineKeyboardButton(text="Еще Вложение", callback_data="first_3")],
        [InlineKeyboardButton(text="<< назад", callback_data="back")],
        [InlineKeyboardButton(text="в меню ↩️", callback_data="main_menu")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard


def back_keyboard() -> InlineKeyboardMarkup:
    kb = [
        [InlineKeyboardButton(text="<< назад", callback_data="back")],
        [InlineKeyboardButton(text="в меню ↩️", callback_data="main_menu")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb)

    return keyboard
