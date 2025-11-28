def func(code, hack, script=0, app=0):
    return code, hack, script, app

func = lambda code, hack, script=0, app=0:(code, hack, script, app)

print(func(1, 3))


l = ["Mon", 'tue', "Wed", "Thu", "Fri", "sat", "Sun"]

def change_words(words, func):
    for word in words:
        print(func(word))

sample_func = lambda word: word.capitalize()

change_words(l, sample_func)