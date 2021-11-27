def test_uppercase():
    name = "antony"
    print(name.upper())

def test_lowercase():
    name = 'ANTONY'
    print(name.lower())

def test_strip():
    name = ' Antony Raj'
    print(name.strip())

def test_replace():
    name = 'Antony Raj'
    print(name.replace("Raj", "Aju"))

def test_split():
    name = 'Antony Raj'
    print(name.split(' '))

def test_stringlength():
    name = 'Antony Raj'
    print(len(name))

def test_liststring():
    name = ["Antony","Aruna","Apu","Aju"]
    print(name)
    w,x,y,z = ["Antony","Aruna","Apu","Aju"]
    print(w)
    print(x)
    print(y)
    print(z)

def test_concat():
    name1 = "Antony"
    name2 = "Raj"
    print(name1 + name2)
    print(name1 + " " + name2)

def test_formatstring():
    Antonyweight = 85
    Arunaweight = 91
    text = "Antony weight is {}, Aruna weight is {}"
    print(text.format(Antonyweight,Arunaweight))
