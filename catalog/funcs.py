BANNED_WORDS = ("казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар", )


def check_banned_words(text, words=BANNED_WORDS):
    text = text.lower()
    for word in words:
        if word in text:
            return word
