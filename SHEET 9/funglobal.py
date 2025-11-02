name = "Suyash"
print(name)

def fun():
    global name
    print(name)
    name = "Chaudhary"
    lang = "Python"
    print(lang)

fun()
print(name)
