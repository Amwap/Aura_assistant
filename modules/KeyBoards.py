from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import modules.LanguagePack as lp

def keyboard_render(schema):
    keyboards = {'ru': InlineKeyboardMarkup(), 'en': InlineKeyboardMarkup()}
    for lang in keyboards.keys():
        keyboard = keyboards[lang]
        for button in schema:
            columns = []
            for column in button:
                columns.append(InlineKeyboardButton(
                    lp.buttons[column[0]][lang],
                    callback_data=column[1]))
            keyboard.row(*columns)
    return keyboards



common = {
    'disclaimer': keyboard_render(
        [
            [('accept', 'none')],
        ],

    'select language': keyboard_render(
        [
            [('russian', 'none')],
            [('english', 'none')]
        ]
    )
}

