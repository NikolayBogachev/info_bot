from TG.keyboards.InlineKeyboard import *
from TG.StatesGroup import *
from TG.logica.utils import *


async def command_start_handler(message: Message):

    await message.answer(f"Здравствуйте {message.from_user.full_name}, что бы вы хотели узнать?",
                         reply_markup=get_start_menu_keyboard())


async def return_to_main_menu(callback: CallbackQuery, state: FSMContext):

    await state.clear()
    await replace_message_handler(callback, state,
                                  text=f"Здравствуйте, {callback.from_user.full_name}, что бы вы хотели узнать?",
                                  keyboard=get_start_menu_keyboard())
    await callback.answer()


async def handle_1c_menu(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(
        text="Выберите подкатегорию:",
        reply_markup=get_1c_menu_keyboard(),
        parse_mode="HTML"
    )
    await state.set_state(MainStates.C1_state)
    await callback.answer()


async def create_order(callback: CallbackQuery, state: FSMContext):

    await send_document_handler(callback, state,
                                file_path="C:/Users/bogac/PycharmProjects/info_bot/TG/documents/Создание_Заказа_Покупателя_и_выставление_счёта.pdf",
                                caption="Вот документ для изучения Создание Заказа Покупателя и выставление счёта.",
                                keyboard=back_keyboard(),
                                new_state=C1_States.Create_order)


async def create_invoice(callback: CallbackQuery, state: FSMContext):

    await send_document_handler(callback, state,
                                file_path="C:/Users/bogac/PycharmProjects/info_bot/TG/documents/Создание отгрузочной накладной.pdf",
                                caption="Вот документ для изучения Создание отгрузочной накладной",
                                keyboard=back_keyboard(),
                                new_state=C1_States.Create_invoice)


async def create_contractor(callback: CallbackQuery, state: FSMContext):
    await send_document_handler(callback, state,
                                file_path="C:/Users/bogac/PycharmProjects/info_bot/TG/documents/Создание контрагента.pdf",
                                caption="Вот документ для изучения Создание контрагента",
                                keyboard=back_keyboard(),
                                new_state=C1_States.Create_contractor)


async def buyer_return(callback: CallbackQuery, state: FSMContext):
    await send_document_handler(callback, state,
                                file_path="C:/Users/bogac/PycharmProjects/info_bot/TG/documents/Возврат от покупателя.pdf",
                                caption="Вот документ для изучения Возврат от покупателя",
                                keyboard=back_keyboard(),
                                new_state=C1_States.Return)


async def crate_nomenclature(callback: CallbackQuery, state: FSMContext):
    await send_document_handler(callback, state,
                                file_path="C:/Users/bogac/PycharmProjects/info_bot/TG/documents/Создание номенклатуры.pdf",
                                caption="Вот документ для изучения Создание номенклатуры",
                                keyboard=back_keyboard(),
                                new_state=C1_States.Create_item)


async def handle_complaints_menu(callback: CallbackQuery, state: FSMContext):
    await edit_message_handler(callback, state, get_complaints_keyboard(), text="Выберите подкатегорию:",
                               new_state=MainStates.Complaints)


async def klen(callback: CallbackQuery, state: FSMContext):
    await send_html_template_callback(callback,  state,
                                      html_path="C:/Users/bogac/PycharmProjects/info_bot/TG/documents/texts/klen.html",
                                      keyboard=back_keyboard(),
                                      new_state=ComplaintsStates.Klen)


async def restint(callback: CallbackQuery, state: FSMContext):
    await send_html_template_callback(callback,  state,
                                      html_path="C:/Users/bogac/PycharmProjects/info_bot/TG/documents/texts/intras.html",
                                      keyboard=back_keyboard(),
                                      new_state=ComplaintsStates.Restint)


async def masterclass(callback: CallbackQuery, state: FSMContext):
    await send_html_template_callback(callback,  state,
                                      html_path="C:/Users/bogac/PycharmProjects/info_bot/TG/documents/texts/masterclass.html",
                                      keyboard=back_keyboard(),
                                      new_state=ComplaintsStates.Masterclass)


async def region_50(callback: CallbackQuery, state: FSMContext):
    await send_html_template_callback(callback,  state,
                                      html_path="C:/Users/bogac/PycharmProjects/info_bot/TG/documents/texts/reg_50.html",
                                      keyboard=back_keyboard(),
                                      new_state=ComplaintsStates.Region_50)


async def ru_project(callback: CallbackQuery, state: FSMContext):
    await send_html_template_callback(callback,  state,
                                      html_path="C:/Users/bogac/PycharmProjects/info_bot/TG/documents/texts/ru_project.html",
                                      keyboard=back_keyboard(),
                                      new_state=ComplaintsStates.Ru_project)


async def db_menu(callback: CallbackQuery, state: FSMContext):
    await edit_message_handler(callback, state, get_db_keyboard(), text="Выберите подкатегорию:",
                               new_state=MainStates.DataBase)


async def inventory(callback: CallbackQuery, state: FSMContext):
    await send_document_handler(callback, state,
                                file_path="C:/Users/bogac/PycharmProjects/info_bot/TG/documents/Барный инвентарь.pdf",
                                caption="Вот документ для изучения Барный инвентарь",
                                keyboard=back_keyboard(),
                                new_state=DataBase.Bar_inventory)


async def topping(callback: CallbackQuery, state: FSMContext):
    await send_document_handler(callback, state,
                                file_path="C:/Users/bogac/PycharmProjects/info_bot/TG/documents/Сиропы, топинги, пюре.pdf",
                                caption="Вот документ для изучения Сиропы, топинги, пюре",
                                keyboard=back_keyboard(),
                                new_state=DataBase.Topping)


async def equipment(callback: CallbackQuery, state: FSMContext):
    await edit_message_handler(callback, state, back_keyboard(), text="Ожидайте... 😊",
                               new_state=DataBase.Equipment)


async def stub(callback: CallbackQuery, state: FSMContext):
    await edit_message_handler(callback, state, back_keyboard(), text="Выберите категорию",
                               new_state=MainStates.Stub)


async def nesting(callback: CallbackQuery, state: FSMContext):
    await edit_message_handler(callback, state, get_level_keyboard(), text="Выберите подкатегорию",
                               new_state=MainStates.Nesting)


async def nesting_lvl2(callback: CallbackQuery, state: FSMContext):
    await edit_message_handler(callback, state, get_level2_keyboard(), text="Выберите подподкатегорию",
                               new_state=NestingStates.First)


async def nesting_lvl3(callback: CallbackQuery, state: FSMContext):
    await edit_message_handler(callback, state, get_level3_keyboard(), text="Выберите подподкатегорию",
                               new_state=NestingStates.FirstFirst)


async def third(callback: CallbackQuery, state: FSMContext):
    await edit_message_handler(callback, state, back_keyboard(), text="Ожидайте... 😊",
                               new_state=MainStates.Nesting)


async def second(callback: CallbackQuery, state: FSMContext):
    await edit_message_handler(callback, state, back_keyboard(), text="Просто проверка, ничего важного",
                               new_state=NestingStates.Second)


async def second_second(callback: CallbackQuery, state: FSMContext):
    await edit_message_handler(callback, state, back_keyboard(), text="Просто проверка, ничего важного",
                               new_state=NestingStates.First)


async def first_3(callback: CallbackQuery, state: FSMContext):
    await edit_message_handler(callback, state, back_keyboard(), text="Просто проверка, ничего важного",
                               new_state=NestingStates.FirstFirst)


async def handle_back(callback: CallbackQuery, state: FSMContext):

    current_state = await state.get_state()
    match  current_state:
        case (MainStates.C1_state.state |
              MainStates.Complaints.state |
              MainStates.DataBase.state |
              MainStates.Stub.state |
              MainStates.Nesting.state):
            #Возвращаемся в главное меню
            await return_to_main_menu(callback, state)

        case (C1_States.Create_order.state |
              C1_States.Create_invoice.state |
              C1_States.Create_contractor.state |
              C1_States.Return |
              C1_States.Create_item):
            # Возвращаемся в меню 1C
            await replace_message_handler(callback, state, text="Выберите подкатегорию:",
                                          keyboard=get_1c_menu_keyboard(),
                                          new_state=MainStates.C1_state)

        case (ComplaintsStates.Klen.state |
              ComplaintsStates.Restint.state |
              ComplaintsStates.Masterclass.state |
              ComplaintsStates.Region_50.state |
              ComplaintsStates.Ru_project.state):
            # Возвращаемся в меню Complaints
            await edit_message_handler(callback, state, text="Выберите подкатегорию:",
                                       keyboard=get_complaints_keyboard(),
                                       new_state=MainStates.Complaints)

        case (DataBase.Bar_inventory.state |
              DataBase.Topping.state |
              DataBase.Equipment.state):
            # Возвращаемся в меню 1C
            await replace_message_handler(callback, state, text="Выберите подкатегорию:",
                                          keyboard=get_db_keyboard(),
                                          new_state=MainStates.DataBase)

        case (NestingStates.First.state |
              NestingStates.Second.state):
            # Возвращаемся в меню Complaints
            await edit_message_handler(callback, state, text="Выберите подкатегорию:",
                                       keyboard=get_level_keyboard(),
                                       new_state=MainStates.Nesting)
        case NestingStates.FirstFirst.state:
            # Возвращаемся в меню Complaints
            await edit_message_handler(callback, state, text="Выберите подподкатегорию:",
                                       keyboard=get_level2_keyboard(),
                                       new_state=NestingStates.First)