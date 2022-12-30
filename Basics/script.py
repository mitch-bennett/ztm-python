from translate import Translator

with open("test.txt", "r") as my_file:
    text = my_file.read()

print(text)
translator = Translator(to_lang="ja")
translation = translator.translate(text)
print(translation)

with open("test-ja.txt", "w") as my_file2:
    my_file2.write(translation)
