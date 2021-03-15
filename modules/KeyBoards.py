from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import modules.LanguagePack as lp

def keyboard_render(schema):
    keyboards = {}
    for lang in lp.used_languages:
        keyboards[lang] = InlineKeyboardMarkup()
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
            [('accept', 'disclaimer accept')],
        ]
    ),
    'select language': keyboard_render(
        [
            [('russian', 'language ru')],
            [('english', 'language en')]
        ]
    ),
    'select currency': keyboard_render(
        [
            [('ruble', 'currency RUB')],
            [('dollar', 'currency USD')],
            [('euro', 'currency EUR')],
            # [('C.U.', 'currency C.U.' )],
        ]
    ),
}

