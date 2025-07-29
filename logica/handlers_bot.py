from aiogram import F
from aiogram.filters import CommandStart, StateFilter

from bot import dp
from logica.funcs_tg import *


# Функция для регистрации обработчиков
def register_handlers():

    dp.message.register(command_start_handler, CommandStart())

    dp.callback_query.register(return_to_main_menu, F.data == "main_menu")
    dp.callback_query.register(stub, F.data.in_(["service", "support", "company"]))

    dp.callback_query.register(handle_1c_menu, F.data == '1C')
    dp.callback_query.register(create_order, StateFilter(MainStates.C1_state), F.data == "create_order")
    dp.callback_query.register(create_invoice, StateFilter(MainStates.C1_state), F.data == "create_invoice")
    dp.callback_query.register(create_contractor, StateFilter(MainStates.C1_state), F.data == "create_contractor")
    dp.callback_query.register(buyer_return, StateFilter(MainStates.C1_state), F.data == "return")
    dp.callback_query.register(crate_nomenclature, StateFilter(MainStates.C1_state), F.data == "create_item")

    dp.callback_query.register(handle_complaints_menu, F.data == "reclam")
    dp.callback_query.register(klen, StateFilter(MainStates.Complaints), F.data == "klen")
    dp.callback_query.register(restint, StateFilter(MainStates.Complaints), F.data == "restint")
    dp.callback_query.register(masterclass, StateFilter(MainStates.Complaints), F.data == "masterclass")
    dp.callback_query.register(region_50, StateFilter(MainStates.Complaints), F.data == "region_50")
    dp.callback_query.register(ru_project, StateFilter(MainStates.Complaints), F.data == "ru_project")

    dp.callback_query.register(db_menu, F.data == "db")
    dp.callback_query.register(inventory, StateFilter(MainStates.DataBase), F.data == "bar_inventory")
    dp.callback_query.register(topping, StateFilter(MainStates.DataBase), F.data == "topping")
    dp.callback_query.register(equipment, StateFilter(MainStates.DataBase), F.data.in_(["equipment"]))

    dp.callback_query.register(nesting, F.data == "level")
    dp.callback_query.register(nesting_lvl2, StateFilter(MainStates.Nesting), F.data == "first")
    dp.callback_query.register(nesting_lvl3, StateFilter(NestingStates.First), F.data == "first_first")
    dp.callback_query.register(second, StateFilter(MainStates.Nesting), F.data.in_(["second"]))
    dp.callback_query.register(second_second, StateFilter(NestingStates.First), F.data == "second_second")
    dp.callback_query.register(first_3, StateFilter(NestingStates.FirstFirst), F.data == "first_3")
    dp.callback_query.register(third, StateFilter(MainStates.Nesting), F.data == "third")

    dp.callback_query.register(handle_back, F.data == "back")




