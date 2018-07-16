#
# https://py.checkio.org/en/mission/text-editor/
#

class Text(object):

    def __init__(self):
        self._text = ""
        self._font_name = None

    def write(self, text):
        self._text += text

    def set_font(self, font_name):
        self._font_name = font_name

    def show(self):
        if self._font_name:
            format = "[{font_name}]{text}[{font_name}]"
            return format.format(font_name=self._font_name, text=self._text)
        else:
            return self._text

    def restore(self, dumped_text):
        self._text = dumped_text["text"]
        self._font_name = dumped_text["font_name"]

    def dump(self):
        return {"text": self._text, "font_name": self._font_name}

class SavedText(object):

    def __init__(self):
        self._histories = []

    def save_text(self, text):
        self._histories.append(text.dump())

    def get_version(self, version):
        return self._histories[version]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()
    
    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"
    
    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")

