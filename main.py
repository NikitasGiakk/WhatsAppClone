import tkinter as tk
from tkinter import ttk


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

    try:
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
    except Exception as e:
        print(e)
    return data_to_return


def convert_msg_to_list(file_name):
    data_list = []

    for line in load_data(file_name):
        data_list.append(extract_data(line, file_name))
    return data_list

if __name__ == '__main__':
    root = tk.Tk()
    root.title('WhatsApp')
    root.geometry("990x1600")
    frame = tk.Frame(root)
    frame.pack()
    canvas = tk.Canvas(frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH)
    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)
    interior = tk.Frame(canvas)
    interior_id = canvas.create_window(0, 0, window=interior, anchor=tk.NW)


    def configure_interior(event):
        canvas.configure(scrollregion=canvas.bbox("all"))


    def on_mousewheel(event):
        canvas.yview_scroll()


    def resize_canvas(event):
        canvas.config(scrollregion=canvas.bbox("all"), width=960, height= 1500)


    canvas.bind("<Configure>", resize_canvas)
    try:
        for item in convert_msg_to_list(6):
            if item['sender'] == 'Nikitas':
                button = tk.Button(interior, text=item['content'], fg='blue', wraplength=930)
                button.pack( side=tk.TOP, anchor='e')
            else:
                button = tk.Button(interior, text=item['content'], fg='green', wraplength=930)
                button.pack( side=tk.TOP, anchor='w')
    except Exception as e:
        print(e)

root.mainloop()
