import keyboard
import pyautogui as pag

# Основные переменные

letters_down = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letters_up =   ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numerals = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*","(",")","_","-","=","+",".",","]
list_of_lists = []
lists_count = 0
focus_count = 0
password = []
focus_list = []
focus_letter = []
lists_default = 0
list_of_lists_default = []
key_list = []



# Вводимые параметры базы символов

include_letters_down = 1
include_letters_up = 1
include_numerals = 1
include_symbols = 1
password_lenth = 16

# добавления списков
if include_letters_down == 1:
    list_of_lists_default.append(letters_down)
    lists_default = lists_default + 1
if include_letters_up == 1:
    list_of_lists_default.append(letters_up)
    lists_default = lists_default + 1
if include_numerals == 1:
    list_of_lists_default.append(numerals)
    lists_default = lists_default + 1
if include_symbols == 1:
    list_of_lists_default.append(symbols)
    lists_default = lists_default + 1


#ввод ключей
print("input key:")
key = []
key_proto = "kotsac"
key_input = (input())
key_list = list(key_proto) + letters_up + letters_down + numerals + symbols

for i in list(str(key_input)):
    key.append(str(key_list.index(i)))
key = int("".join(key))


# алгоритм программы

lists_count = lists_default
list_of_lists = list(list_of_lists_default)


for i in range (password_lenth):
    focus_list = list_of_lists[(len(str(key)) + password_lenth + key + focus_count) % lists_count]
    focus_letter = focus_list[(password_lenth + key + focus_count) % len(focus_list)]
    focus_count = focus_count + (focus_list.index(focus_letter))
    password.append (focus_letter)
    list_of_lists.remove (focus_list)
    lists_count = lists_count - 1


    if (lists_count == 0):
        lists_count = lists_default
        list_of_lists = list(list_of_lists_default)




password=("".join(password))
if (key_proto != ""):
    key_proto_print = [key_proto[0],"****",key_proto[-1]]
    key_proto_print = ("".join(key_proto_print))
    print("protokey:",key_proto_print)
print()
print()
print()
print("          ",password)
print()
print()
print()
print("To insert password press Del")
def foo():

    pag.typewrite(password)

keyboard.add_hotkey('Del', foo)
keyboard.wait('Del')
password=[]

