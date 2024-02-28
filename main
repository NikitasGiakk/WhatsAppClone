import tkinter
import tkinter as tk
from tkinter import ttk
import re
import random


# current_month = data[1:3]
# current_year = data[7:11]
current_month = 11
current_year = 2020
x= 960
conv_index = 1

def random_color():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f'#{r:02x}{g:02x}{b:02x}'

couleur = random_color()

def switch_right():
    global current_month, current_year
    if current_month == '12':
        current_year += 1
        current_month = '01'
    else:
        current_month = str(int(current_month) + 1).zfill(2)  # Ajoute 1 au mois et assure un format avec zfill
    reload_messages()
    update_month_button()
    scrollbar.set(0,0)

def switch_left():
    global current_month, current_year
    if current_month == '01':
        current_year -= 1
        current_month = '12'
    else:
        current_month = str(int(current_month) - 1).zfill(2)  # Soustrait 1 au mois et assure un format avec zfill
    reload_messages()
    update_month_button()
    scrollbar.set(0, 0)

def load_data(data_index):
    with open(fr'./data/{str(data_index)}.txt', 'r') as current_file:
        data = current_file.readlines()
        current_file.close()
        return data


def extract_data(data, encoding_method: int):
    data = data
    data_to_return = {'date': None,
                      'time': None,
                      'sender': None,
                      'content': None}

    if encoding_method == 1:
        data_to_return['date'] = data[1:11]
        data_to_return['time'] = data[12:20]
        data_to_return['sender'] = str(data.split(' ')[2])[:-1]
        data_to_return['content'] = data.split(' ')[3:]
        data_to_return['content'] = ' '.join(data_to_return['content'])

    else:
        data_to_return['date'] = data[:10]
        data_to_return['time'] = data[13:18]
        data_to_return['sender'] = str(data.split(' ')[4])[:-1]
        data_to_return['content'] = data.split(' ')[5:]
        data_to_return['content'] = ' '.join(data_to_return['content'])[:-1]
    return data_to_return


def convert_msg_to_list(file_name):
    msg_list = []
    data_list = []

    for line in load_data(file_name):
        if  re.search("\d{2}/\d{2}/\d{4}",line) :
            msg_list.append(line)
        else :
            msg_list[-1] += line

#    print(msg_list)

    for line in msg_list:
        data_list.append(extract_data(line, file_name))
    return data_list


def update_month_button():
    month_button.config(text=f"{current_month}/{current_year}")

def change_conv(event=None):
    global conv_index
    if conv_index == 6:
        conv_index = 1
    else:
        conv_index += 1
    reload_messages()
    root.title('WhatsApp ' + str(conv_index))



if __name__ == '__main__':
    root = tk.Tk()
    root.title('WhatsApp '+ str(conv_index))
    root.geometry("990x1600")
    frame = tk.Frame(root)
    canvas = tk.Canvas(frame)
    frame2 = tk.Frame(canvas)
    tk.Button(frame2, text="<<<", command=switch_left).pack(side=tk.LEFT)
    tk.Button(frame2, text=">>>", command=switch_right).pack(side=tk.RIGHT)
    month_button = tk.Button(frame2, text=f"{current_month}/{current_year}", command=change_conv)
    month_button.pack(side=tk.LEFT)
    frame2.pack(expand=tk.YES)
    canvas.pack(side=tkinter.TOP)
    canvas.pack(side=tkinter.TOP)
    frame.pack(expand=tkinter.YES)
    canvas = tk.Canvas(frame)
    canvas.pack(side=tk.LEFT)
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)
    interior = tk.Frame(canvas, bg=couleur)
    interior_id = canvas.create_window(0, 0, window=interior, anchor=tk.NW, width=x)


    def configure_interior(event):
        canvas.configure(scrollregion=canvas.bbox("all"))



    def on_mousewheel(event):
        canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def resize_canvas(event):
        canvas.config(scrollregion=canvas.bbox("all"), width=x, height= 1300)


    def on_arrow_key(event):
        if event.keysym == "Up":
            canvas.yview_scroll(-1, "units")
        elif event.keysym == "Down":
            canvas.yview_scroll(1, "units")

    canvas.bind("<Configure>", resize_canvas)
    canvas.bind("<Up>", on_arrow_key)
    canvas.bind("<Down>", on_arrow_key)
    canvas.focus_set()

    def reload_messages():
        global current_month, current_year, interior, interior_id
        try:
            interior.destroy()
            couleur = random_color()
            interior = tk.Frame(canvas, bg=couleur)
            interior_id = canvas.create_window(0, 0, window=interior, anchor=tk.NW, width=x)



            for item in convert_msg_to_list(conv_index):
                if item['date'][3:] == f'{current_month}/{current_year}':
                    if item['sender'] == 'Nikitas':
                        button = tk.Button(interior, text=item['content'], fg='blue', wraplength=x-200)
                        button.pack(side=tk.TOP, anchor='e')
                    else:
                        button = tk.Button(interior, text=item["sender"] + " " + item['content'], fg='green',wraplength=x-200)
                        button.pack(side=tk.TOP, anchor='w')

        except Exception as e:
            print(e)


    reload_messages()

root.mainloop()
