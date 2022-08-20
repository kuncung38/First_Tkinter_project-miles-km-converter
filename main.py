from tkinter import *
from tkinter.font import Font


wd = Tk()
wd.minsize(width=150, height=150)
wd.title("Miles-KM Converter")
wd.config(padx=20, pady=20)

MY_FONT = ('Ink Free', '18', 'bold')
INK_FREE = Font(family= 'Ink Free', size= 18, weight='bold')

#Let input can only accept numerical / decimal value
'''------------------------------------------------------------------------------'''
def float_validation(P):
    #  if str.isdigit(P) or P == "" or '.' in P:
    if P == "":
        return True
    else:
        try:
            float(P)
        except:
            return False
        return True

vcmd = wd.register(float_validation)

input = Entry(text= "0", validate="all", validatecommand=(vcmd, '%P'), 
                    width= 10, font=MY_FONT)
input.insert(0, "0")
input.focus()
input.grid(column= 1, row= 0)
'''------------------------------------------------------------------------------'''

#Conversion menu
'''------------------------------------------------------------------------------'''
conversion_list = ["Miles", "Km"]
value_inside = StringVar(wd)
value_inside.set(conversion_list[0])

conversion_menu = OptionMenu(wd, value_inside, *conversion_list)


conversion_menu.config(padx= 10, font= INK_FREE)
conversion_menu.grid(column= 2, row= 0)
'''------------------------------------------------------------------------------'''


is_equal_label = Label(text="is equal to:", font=INK_FREE)
is_equal_label.config(padx= 10)
is_equal_label.grid(column= 0, row= 1)


#result
'''------------------------------------------------------------------------------'''
result_value = Entry(text = 0, font=INK_FREE, justify="center")
result_value.config(state='readonly')
result_value.grid(column= 1, row= 1)
'''------------------------------------------------------------------------------'''

unit_label = Label(text="Km", font=INK_FREE)
unit_label.config(padx= 10)
unit_label.grid(column= 2, row= 1)

def change():
    if input.get() == '':
        raw_result = 0
    else: 
        raw_result = float(input.get())

    if value_inside.get() == 'Miles':
        final_result = raw_result * 0.1609344
        unit_label.config(text="Km", font=INK_FREE)
    else:
        final_result = raw_result / 0.1609344
        unit_label.config(text="Miles", font=INK_FREE)
    
    result_str_var = StringVar(wd)
    result_str_var.set(final_result)
    result_value.config(textvariable=result_str_var)
    #update the text on the label

    wd.after(5,change) #repeat the function each 5 ms

change()
wd.mainloop()