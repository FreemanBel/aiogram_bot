from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

pagination_call = CallbackData("paginator", "key", "page")
show_item = CallbackData("show_item", "item_id")


def get_page_keyboard(max_pages: int, key="book", page: int = 1):
    # Клавиатура будет выглядеть вот так:
    # |<< | <5> | >>|

    previous_page = page - 1
    previous_page_text = "<< "

    current_page_text = f"<{page}>"

    next_page = page + 1
    next_page_text = " >>"

    markup = InlineKeyboardMarkup()
    if previous_page > 0:
        markup.insert(
                InlineKeyboardButton(
                        text=previous_page_text,
                        callback_data=pagination_call.new(key=key, page=previous_page)
                )
        )

    markup.insert(
            InlineKeyboardButton(
                    text=current_page_text,
                    callback_data=pagination_call.new(key=key, page="current_page")
            )
    )

    if next_page < max_pages:
        markup.insert(
                InlineKeyboardButton(
                        text=next_page_text,
                        callback_data=pagination_call.new(key=key, page=next_page)
                )
        )

    return markup


def get_better_pages_keyboard(array, page: int = 1):
    key = "items"
    markup = InlineKeyboardMarkup(row_width=3)
    MAX_ITEMS_PER_PAGE = 7
    first_item_index = (page - 1) * MAX_ITEMS_PER_PAGE
    last_item_index = page * MAX_ITEMS_PER_PAGE

    sliced_array = array[first_item_index:last_item_index]
    items_buttons = list()

    for item in sliced_array:
        items_buttons.append(
                InlineKeyboardButton(
                        text=f'{item.name} - ${item.price}',
                        callback_data=show_item.new(item_id=item.id)
                )
        )
    pages_buttons = list()
    first_page = 1
    first_page_text = "« 1"

    if len(array) % MAX_ITEMS_PER_PAGE == 0:
        max_page = len(array) // MAX_ITEMS_PER_PAGE
    else:
        max_page = len(array) // MAX_ITEMS_PER_PAGE + 1

    max_page_text = f"» {max_page}"

    pages_buttons.append(
            InlineKeyboardButton(
                    text=first_page_text,
                    callback_data=pagination_call.new(key=key,
                                                      page=first_page)
            )
    )

    previous_page = page - 1
    previous_page_text = f"< {previous_page}"

    if previous_page >= first_page:
        pages_buttons.append(
                InlineKeyboardButton(
                        text=previous_page_text,
                        callback_data=pagination_call.new(key=key,
                                                          page=previous_page)
                )
        )
    else:
        pages_buttons.append(
                InlineKeyboardButton(
                        text=" . ",
                        callback_data=pagination_call.new(key=key,
                                                          page="current_page")
                )
        )

    pages_buttons.append(
            InlineKeyboardButton(
                    text=f"- {page} -",
                    callback_data=pagination_call.new(key=key,
                                                      page="current_page")
            )
    )

    next_page = page + 1
    next_page_text = f"{next_page} >"

    if next_page <= max_page:
        pages_buttons.append(
                InlineKeyboardButton(
                        text=next_page_text,
                        callback_data=pagination_call.new(key=key,
                                                          page=next_page)))
    else:
        pages_buttons.append(
                InlineKeyboardButton(
                        text=" . ",
                        callback_data=pagination_call.new(key=key,
                                                          page="current_page")
                )
        )

    pages_buttons.append(
            InlineKeyboardButton(
                    text=max_page_text,
                    callback_data=pagination_call.new(key=key,
                                                      page=max_page)
            )
    )
    for button in items_buttons:
        markup.insert(button)

    markup.row(*pages_buttons)
    return markup
