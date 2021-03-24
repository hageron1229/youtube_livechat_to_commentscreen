#webdriver短縮
from hg import sel
import time

youtube = "https://www.youtube.com/watch?v="+"QUERY"
commentscreen = "https://commentscreen.com/comments?&id="+"ID"

def send(new_data):
    w.switch_to.window(w.window_handles[1])
    for new in new_data:
        w.find_element_by_class_name("InputArea__TextInput-sc-10cafwy-6").send_keys(new+"\n")
    w.switch_to.window(w.window_handles[0])
    iframe = w.find_element_by_id("chatframe")
    w.switch_to.frame(iframe)

w = sel.init(False)
w.get(youtube)

#commentscreen
w.execute_script("window.open()")
w.switch_to.window(w.window_handles[1])
w.get(commentscreen)
w.switch_to.window(w.window_handles[0])
time.sleep(1)

iframe = w.find_element_by_id("chatframe")
w.switch_to.frame(iframe)

history = []

while 1:
    print("wating...")
    time.sleep(5)
    new = []
    coms = w.find_elements_by_tag_name("yt-live-chat-text-message-renderer")
    l = len(history)
    for i in range(len(coms)-len(history)):
        j = i+l
        mes = coms[j].find_element_by_id("message")
        print("new message :",mes.text)
        history.append(mes.text)
        new.append(mes.text)
    if len(new)!=0:
        send(new)

