from aiogram.fsm.state import StatesGroup, State


class MainStates(StatesGroup):
    C1_state = State()
    Complaints = State()
    DataBase = State()
    Nesting = State()
    Stub = State()


class NestingStates(StatesGroup):
    First = State()
    FirstFirst = State()
    End = State()
    Second = State()
    Third = State()


class DataBase(StatesGroup):
    Bar_inventory = State()
    Topping = State()
    Equipment = State()


class C1_States(StatesGroup):
    Create_order = State()
    Create_invoice = State()
    Return = State()
    Create_contractor = State()
    Create_item = State()


class ComplaintsStates(StatesGroup):
    Klen = State()
    Restint = State()
    Masterclass = State()
    Region_50 = State()
    Ru_project = State()
