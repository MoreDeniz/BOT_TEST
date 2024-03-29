from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.callback import menu_main, select_event, menu_search
from loader import db


def create_kb_navigation(data: dict):
    target_list = []
    current_menu = data.get('menu')
    current_id = data.get('current_id', 0)
    current_city = data.get('city', '')
    current_location = data.get('location', '')
    current_org_id = data.get('org_id', 0)
    current_date = data.get('date', '')

    match current_menu:
        case 'city':
            all_events = {event[4] for event in db.all_events()}
            target_list = [db.get_city_by_id(location_id) for location_id in all_events]
            current_city = ''
        case 'date':
            target_list = db.all_dates()
        case 'org':
            target_list = db.all_orgs()
        case 'event':
            all_list = [db.get_name_and_city_location(id_loc) for id_loc in {event[4] for event in db.all_events()}]
            target_list = [location[0] for location in all_list if location[0][1] == current_city]
    menu_list = create_select_list(target_list)

    next_id = int(current_id) + 1
    prev_id = int(current_id) - 1
    if current_id == 0:
        prev_id = len(menu_list) - 1
    elif current_id == len(menu_list) - 1:
        next_id = 0

    buttons_list = []

    for button_item in menu_list[current_id]:
        button_menu = ''
        match current_menu:
            case 'city':
                current_city = button_item
                button_menu = 'event'
            case 'event':
                current_location = button_item
                button_menu = 'select'
            case 'date':
                current_date = button_item
                button_menu = 'select'
            case 'org':
                current_org_id = button_item
                button_item = db.get_user_name(button_item)[0]
                button_menu = 'select'

        button = InlineKeyboardButton(text=button_item,
                                      callback_data=select_event.new(menu=button_menu, location=current_location,
                                                                     city=current_city, org_id=current_org_id,
                                                                     date=current_date, current_id=0))

        buttons_list.append(button)
    if data.get('city') and not data.get('location'):
        btn_back = InlineKeyboardButton(text='Назад',
                                        callback_data=menu_search.new(menu='search',
                                                                      button='city'))
    else:
        btn_back = InlineKeyboardButton(text='Назад', callback_data=menu_main.new(menu='main',
                                                                                  button='search'))

    btn_prev = InlineKeyboardButton(text='<<<', callback_data=select_event.new(menu=current_menu,
                                                                               location=current_location,
                                                                               city=current_city,
                                                                               org_id=current_org_id,
                                                                               date=current_date,
                                                                               current_id=prev_id))
    btn_next = InlineKeyboardButton(text='>>>', callback_data=select_event.new(menu=current_menu,
                                                                               location=current_location,
                                                                               city=current_city,
                                                                               org_id=current_org_id,
                                                                               date=current_date,
                                                                               current_id=next_id))
    kb_navigation = InlineKeyboardMarkup(row_width=2)
    kb_navigation.row(*buttons_list[:3])
    kb_navigation.row(*buttons_list[3:])
    if len(target_list) > 6:
        kb_navigation.row(btn_prev, btn_back, btn_next)
    else:
        kb_navigation.row(btn_back)

    return kb_navigation

def create_select_list(target_list: list) -> list:
    menu_list = []
    target_list = list(map(lambda x: x[0], target_list))
    for item in target_list:
        menu_list.append(item)
    sorted_item_list = sorted(menu_list)
    menu_list.clear()
    count = 0
    row = []
    for item in sorted_item_list:
        if count < 6:
            row.append(item)
        else:
            count = 0
            menu_list.append(row)
            row = [item]
        count += 1
    else:
        if row:
            menu_list.append(row)
    return menu_list