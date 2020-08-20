from tkinter import *
from tkinter.messagebox import *
import requests, json, os
from TikTokAPI import TikTokAPI
import sys
#start of CLI
if len(sys.argv) > 1:
    user_name = str(sys.argv[1])
    if len(sys.argv) > 2:
        c = int(sys.argv[2])
    else:
        c = 50
    print('username: {} | amount: {}'.format(user_name, c))
    api = TikTokAPI()
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r'{}'.format(user_name))
    if not os.path.exists(final_directory):
       os.makedirs(final_directory)
    user_obj = api.getVideosByUserName(user_name)
    jsons = json.dumps(user_obj)
    var = json.loads(jsons)
    for i in range(c):
        #print(var)
        out = '{}-{}-{}'.format(i, var['items'][i]['id'], var['items'][i]['video']['downloadAddr'])
        print(out)
        url = var['items'][i]['video']['downloadAddr']
        r = requests.get(url, allow_redirects=True)
        name = '{}\\{}-{}.mp4'.format(user_name, user_name, i)
        open(name, 'wb').write(r.content)
    print("Task completed")
else:
    #start of GUI
    def show_answer():
        blank.delete(0,"end")
        if uname.get() == "":
            out = uname.get()
            #blank.insert(0, out)
        else:
            user_name = str(uname.get())
        if amount.get() != "":
            c = int(amount.get())
        else:
            c = 50
        print('username: {} | amount: {}'.format(user_name, c))
        api = TikTokAPI()
        current_directory = os.getcwd()
        final_directory = os.path.join(current_directory, r'{}'.format(user_name))
        if not os.path.exists(final_directory):
            os.makedirs(final_directory)
        user_obj = api.getVideosByUserName(user_name)
        jsons = json.dumps(user_obj)
        var = json.loads(jsons)
        print(len(var))
        if len(var) > 4:
            out = "working on downloading"
            blank.insert(0, out)
            for i in range(c):
                blank.delete(0, "end")
                out = '{}-{}-{}'.format(i, var['items'][i]['id'], var['items'][i]['video']['downloadAddr'])
                print(out)
                url = var['items'][i]['video']['downloadAddr']
                r = requests.get(url, allow_redirects=True)
                name = '{}\\{}-{}.mp4'.format(user_name, user_name, i)
                open(name, 'wb').write(r.content)
                blank.insert(0, out)
        else: 
            out = "invalid username"
            print(out)
            blank.insert(0, out)
        blank.delete(0, "end")
        print("completed task")
        blank.insert(0, "completed task")

    main = Tk()
    Label(main, text = "username:").grid(row=0)
    Label(main, text = "amount:").grid(row=1)
    Label(main, text = "output").grid(row=2)

    uname = Entry(main)
    amount = Entry(main)
    blank = Entry(main)

    uname.grid(row=0, column=1)
    amount.grid(row=1, column=1)
    blank.grid(row=2, column=1)

    Button(main, text='Quit', command=main.destroy).grid(row=4, column=0, sticky=W, pady=4)
    Button(main, text='Run', command=show_answer).grid(row=4, column=1, sticky=W, pady=4)

    mainloop()
