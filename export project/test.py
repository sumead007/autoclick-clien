##current only command has not a try catch2
from json import dumps
import json
from urllib.request import urlopen
import pyautogui
import time
import requests
import subprocess
import pyperclip
from base64 import b64encode
import pathlib
import os
from datetime import datetime
import random

fail_login = 0
fail_otp = 0;

def set_globvar_to_one():
    global fail_login    # Needed to modify global copy of globvar
    fail_login += 1
    
def set_globvar_to_zero():
    global fail_login    # Needed to modify global copy of globvar
    fail_login = 0
    #otp
def set_glob_fail_otp_to_one():
    global fail_otp    # Needed to modify global copy of globvar
    fail_otp += 1
    
def set_glob_fail_otp_to_zero():
    global fail_otp    # Needed to modify global copy of globvar
    fail_otp = 0
    
def task():
    while True:
            
        response2 = requests.get(f"{domain}api/config", headers={
                                    "Content-Type": "application/json", "Authorization": authorization_token})
        time.sleep(1)
        data_json2 = response2.json()
        print('config')
        print(data_json2)

        response3 = requests.get(f"{domain}api/line_login", headers={
                                    "Content-Type": "application/json", "Authorization": authorization_token})
        time.sleep(2)
        data_json3 = response3.json()
        print('line_login')
        print(data_json3)
        
        
        # เรียกข้อมูล
        response = requests.get(f"{domain}api/addline", headers={
                                            "Content-Type": "application/json", "Authorization": authorization_token})
        time.sleep(2)
        response.encoding = 'ISO-8859-1'
        data_json = response.json()

        response = requests.get(f"{domain}api/message", headers={
                                            "Content-Type": "application/json", "Authorization": authorization_token})
        time.sleep(2)
        response.encoding = 'ISO-8859-1'
        data_message_json = response.json()
                
        
        requests.put(f"{domain}api/config/1", json=({"action":0}), headers={"Content-Type": "application/json","Authorization":authorization_token})
            
        if(data_json2['data']['status'] == 1 and len(data_json3['data']) > 0 and len(data_json['data']) > 0):
            print('Status: Service is started')
            lengh_data_user = len(data_json3['data']);
            #วนตามจำนวนคนล็อกอิน
            num_row = 0;
            while num_row < lengh_data_user :
                position_textbox_btnlogin = pyautogui.locateOnScreen('pic/btnlogin.PNG')
                if(position_textbox_btnlogin != None ):
                    pyautogui.moveTo(position_textbox_btnlogin)
                    pyautogui.move(0, -50)
                    time.sleep(1)
                    pyautogui.click()
                    pyautogui.hotkey('ctrl', 'a')
                    pyautogui.hotkey('backspace')
                    pyautogui.move(0, -50)
                    time.sleep(1)
                    pyautogui.click()
                    pyautogui.hotkey('ctrl', 'a')
                    time.sleep(0.5)
                    pyautogui.hotkey('backspace')
                                
                print(f"num_row = {num_row}")
#                 print(f"lengh_data_user = {data_json3['data']}")
                #เช็คว่าปิดยัง
                response2 = requests.get(f"{domain}api/config", headers={
                                        "Content-Type": "application/json", "Authorization": authorization_token})
                time.sleep(1)
                data_json2 = response2.json()
                if(data_json2['data']['status'] == 0):
                    break;
                        
                    #กันล็อกอินซั้า
    #                 email
    #                 password
                data_user = data_json3['data'][num_row];
                num_add = data_json3['data'][num_row]['num_add'];
                num_chat = data_json3['data'][num_row]['num_chat'];
                print(f"login by {data_user['user_login']}")
                position_textbox_password = pyautogui.locateOnScreen(
                        'pic/textbox_password.PNG')
                pyautogui.moveTo(position_textbox_password)         
                if position_textbox_password != None:
                    pyautogui.click(position_textbox_password)
                    time.sleep(1)
        #               pyautogui.write(data_json2['data']['password'])
                    pyperclip.copy(data_user['password'])
                    pyautogui.hotkey('ctrl', 'v')
                    time.sleep(1)

                    pyautogui.hotkey('tab')
                    time.sleep(1)
        #                 pyautogui.write(data_json2['data']['user_login'])
                    pyperclip.copy(data_user['user_login'])
                    pyautogui.hotkey('ctrl', 'v')
                    time.sleep(1)
                position_textbox_btnlogin = pyautogui.locateOnScreen(
                            'pic/btnlogin.PNG')
                if(position_textbox_btnlogin != None):
                    pyautogui.moveTo(position_textbox_btnlogin)
                    pyautogui.click(position_textbox_btnlogin)

                        #ถ้าให้ยืนยันตัวตน (ลบคอมเม้น)
                time.sleep(3)
                position_otp = pyautogui.locateOnScreen('pic/otp.PNG')
                if(position_otp != None ):
                        #รอotp
                        #saveรูปที่แคป
                    now = datetime.now()
                    timestamp = datetime.timestamp(now)
                    name = str(int(timestamp));
                    position_otp = pyautogui.locateOnScreen('pic/otp.PNG')
                    [left, top, width, height] = position_otp
                    try:
                        os.remove(data_json2['data']['image_screen_shot'])
                    except Exception:
                        pass
                    myScreenshot = pyautogui.screenshot(region=(left, top, width, height+80));
                    myScreenshot.save(r'service/screen_shot/'+name+'.png');
                    time.sleep(0.5)


                            #นำภาพไปเข้าเป็นbase64 แล้วอัพขึ้นเซิฟ
                    ENCODING = 'utf-8';
                    IMAGE_NAME = f'service/screen_shot/{name}.png';
                    with open(IMAGE_NAME, 'rb') as open_file:
                        byte_content = open_file.read()
                    base64_bytes = b64encode(byte_content)
                    base64_string = base64_bytes.decode(ENCODING)                  
                    raw_data = base64_string                 
                    json_data = dumps(raw_data, indent=2)
                    requests.put(f"{domain}api/config/1", json=({"base64": json_data,"name":f"{name}.png"}), headers={"Content-Type": "application/json","Authorization":authorization_token})
                    
                    #line notify
                    message_line = f"กำลังรอ OTP ของไอดี {data_user['user_login']}"
                    line_response = requests.post(f"{domain}api/line_notify", headers={
                                            "Content-Type": "application/json", "Authorization": authorization_token}, 
                                                          json=({"message":message_line}))
                    time.sleep(1)
                    data_json_line = line_response.json()
                    print(f"line notify status: {data_json_line}")
                    time.sleep(3)
                    position_otp = pyautogui.locateOnScreen('pic/otp.PNG')

                    while position_otp != None:
                        position_otp = pyautogui.locateOnScreen('pic/otp.PNG')
                        requests.put(f"{domain}api/config/1", json=({"action":1}), headers={"Content-Type": "application/json","Authorization":authorization_token})

                        print("Waiting OTP")

                        response2 = requests.get(f"{domain}api/config", headers={
                                        "Content-Type": "application/json", "Authorization": authorization_token})
                        time.sleep(1)
                        data_json2 = response2.json()


                        if(data_json2['data']['status'] != 1):
                            print("Trun Off")
                            break
                        time.sleep(3)
                        # time.sleep(180)
                else:
                    print("Waiting a second")
                    time.sleep(3)

                #เช็คล็อกอิน (ลบคอมเม้น)
                time.sleep(3)
                position_more = pyautogui.locateOnScreen('pic/more.PNG')
                position_more2 = pyautogui.locateOnScreen('pic/more2.PNG')
                lambda_click = lambda x: position_more2 if position_more == None else position_more
                more_2click = lambda_click(position_more)
                if(more_2click == None):  
                    #line notify
                    message_line = f"ไอดีนี้ {data_user['user_login']} ล็อกอินล้มเหลว"
                    line_response = requests.post(f"{domain}api/line_notify", headers={
                                            "Content-Type": "application/json", "Authorization": authorization_token}, 
                                                          json=({"message":message_line}))
                    data_json_line = line_response.json()
                    print(f"line notify status: {data_json_line}")
                    
                    print("Login failed")
                    requests.put(f"{domain}api/config/1", json=({"action":4}), headers={"Content-Type": "application/json","Authorization":authorization_token})
                    time.sleep(3) 
                    if(fail_login >= 2):
                        print("2 per login")
                        set_globvar_to_zero()
#                         print(f"fail login : {fail_login}")
                        time.sleep(5)
                        num_row +=1
                        continue;
                    set_globvar_to_one();
                    print(f"fail login : {fail_login}")
                    time.sleep(5)
                    continue;
                    
                         # เรียกข้อมูล
                response = requests.get(f"{domain}api/addline", headers={
                                                    "Content-Type": "application/json", "Authorization": authorization_token})
                time.sleep(2)
                response.encoding = 'ISO-8859-1'
                data_json = response.json()

                response = requests.get(f"{domain}api/message", headers={
                                                    "Content-Type": "application/json", "Authorization": authorization_token})
                time.sleep(2)
                response.encoding = 'ISO-8859-1'
                data_message_json = response.json()

                data_arr = []
                print('Process Start....')
                requests.put(f"{domain}api/config/1", json=({"action":2}), headers={"Content-Type": "application/json","Authorization":authorization_token})
                
                if (len(data_json['data'])<=0):
                    print("addline: 0")
                    break;
                #เริ่มแอต
                count_num = 0
                for i in data_json['data']:
#                     user_seard = ""
#                     if i['type'] == '1': 
#                         user_seard = i['user_tel']
#                     else:
#                         user_seard = i['user_id']
    
#                     print(f'userID: {user_seard}')
#                     print(f"userseard: {i}")

                        #กลิกปุ้มแอต
                    position_add = pyautogui.locateOnScreen('pic/add.PNG')
                    position_add2 = pyautogui.locateOnScreen('pic/add2.PNG')
                    lambda_click = lambda x: position_add2 if position_add == None else position_add
                    position_2click = lambda_click(position_add)
                    pyautogui.moveTo(position_2click)
                    pyautogui.click(position_2click)
                    time.sleep(1)

                        # กดปุ่มค้นหาก่อนพิม
                    position_serach_friend = pyautogui.locateOnScreen(
                            'pic/serach friend.PNG')
                    pyautogui.moveTo(position_serach_friend)
                    pyautogui.click(position_serach_friend)
                    time.sleep(1)
                    
                    
                    #แอตไปกลับ
                    row_id = i['id']#ใส่
                    user_id = i['user_id'] #ใส่
                    user_tel = i['user_tel'] #ใส่
                    type_id_or_tel = i['type'] #ใส่
                    # user_datas = [];
                    # user_datas.append(user_tel);
                    # user_datas.append(user_id);
                    count_radio= 0
                    while count_radio < 2:
                    #     print(type_id_or_tel)
                        #แอตเบอร์
                        if type_id_or_tel == '1':
                            user_data = user_tel

                            if user_data.isnumeric():
                                position_radio_line_id = pyautogui.locateOnScreen(
                                                                        'pic/radio line phone.PNG')
                                pyautogui.moveTo(position_radio_line_id)
                                time.sleep(1)
                                pyautogui.click(position_radio_line_id)
                                position_s = pyautogui.locateOnScreen('pic/s.PNG') 
                                pyautogui.moveTo(position_s)
                                time.sleep(1)
                                pyautogui.click(position_s)
                                pyautogui.hotkey('ctrl', 'a')
                                time.sleep(1)
                                pyperclip.copy(user_data)
                                pyautogui.hotkey('ctrl', 'v')
                                pyautogui.hotkey('enter')
                                time.sleep(1)
                                position_lineaddbtn = pyautogui.locateOnScreen('pic/addbtn.PNG')
                                position_linebtnchat = pyautogui.locateOnScreen('pic/btnchat.PNG')
                                if position_lineaddbtn != None or position_linebtnchat != None:
                                    print(f'found this: {user_data}')
                                    line_response = requests.post(f"{domain}api/addline", headers={
                                     "Content-Type": "application/json", "Authorization": authorization_token}, 
                                         json=({"id": row_id,"type":type_id_or_tel,"user_data":user_data}))
                                    time.sleep(1)
                                    requests.post(f"{domain}api/line_status", headers={
                                     "Content-Type": "application/json", "Authorization": authorization_token}, 
                                         json=({"id": row_id,"status":1}))
                                    time.sleep(1)
                                    break

                            if user_data != None and user_data != "":
                                position_radio_line_phone = pyautogui.locateOnScreen(
                                                                'pic/radio line id.PNG')
                                pyautogui.moveTo(position_radio_line_phone)
                                pyautogui.click(position_radio_line_phone)
                                time.sleep(1)   
                                position_s = pyautogui.locateOnScreen('pic/s.PNG')   
                                pyautogui.moveTo(position_s)
                                time.sleep(1)
                                pyautogui.click(position_s)
                                pyautogui.hotkey('ctrl', 'a')
                                time.sleep(1)
                                pyperclip.copy(user_data)
                                pyautogui.hotkey('ctrl', 'v')
                                pyautogui.hotkey('enter')
                                time.sleep(1)
                                position_lineaddbtn = pyautogui.locateOnScreen('pic/addbtn.PNG')
                                position_linebtnchat = pyautogui.locateOnScreen('pic/btnchat.PNG')
                                if position_lineaddbtn != None or position_linebtnchat != None:
                                    print(f'found this: {user_data}')
                                    line_response = requests.post(f"{domain}api/addline", headers={
                                     "Content-Type": "application/json", "Authorization": authorization_token}, 
                                         json=({"id": row_id,"type":type_id_or_tel,"user_data":user_data}))
                                    time.sleep(1)
                                    requests.post(f"{domain}api/line_status", headers={
                                     "Content-Type": "application/json", "Authorization": authorization_token}, 
                                         json=({"id": row_id,"status":1}))
                                    time.sleep(1)
                                    break
                            type_id_or_tel ='0'
                            time.sleep(5)
                        #แอตไอดี
                        else:

                            user_data = user_id
                            if user_data != None and user_data != "":
                                position_radio_line_id = pyautogui.locateOnScreen(
                                                                        'pic/radio line id.PNG')
                                pyautogui.moveTo(position_radio_line_id)
                                time.sleep(1)
                                pyautogui.click(position_radio_line_id)
                                position_s = pyautogui.locateOnScreen('pic/s.PNG') 
                                pyautogui.moveTo(position_s)
                                time.sleep(1)
                                pyautogui.click(position_s)
                                pyautogui.hotkey('ctrl', 'a')
                                time.sleep(1)
                                pyperclip.copy(user_data)
                                pyautogui.hotkey('ctrl', 'v')
                                pyautogui.hotkey('enter')
                                time.sleep(1)
                                position_lineaddbtn = pyautogui.locateOnScreen('pic/addbtn.PNG')
                                position_linebtnchat = pyautogui.locateOnScreen('pic/btnchat.PNG')
                                if position_lineaddbtn != None or position_linebtnchat != None:
                                    print(f'found this: {user_data}')
                                    line_response = requests.post(f"{domain}api/addline", headers={
                                     "Content-Type": "application/json", "Authorization": authorization_token}, 
                                         json=({"id": row_id,"type":type_id_or_tel,"user_data":user_data}))
                                    time.sleep(1)
                                    requests.post(f"{domain}api/line_status", headers={
                                     "Content-Type": "application/json", "Authorization": authorization_token}, 
                                         json=({"id": row_id,"status":1}))
                                    time.sleep(1)
                                    break

                            if user_data.isnumeric():
                                position_radio_line_phone = pyautogui.locateOnScreen(
                                                                'pic/radio line phone.PNG')
                                pyautogui.moveTo(position_radio_line_phone)
                                pyautogui.click(position_radio_line_phone)
                                time.sleep(1)   
                                position_s = pyautogui.locateOnScreen('pic/s.PNG')  
                                pyautogui.moveTo(position_s)
                                time.sleep(1)
                                pyautogui.click(position_s)
                                pyautogui.hotkey('ctrl', 'a')
                                time.sleep(1)
                                pyperclip.copy(user_data)
                                pyautogui.hotkey('ctrl', 'v')
                                pyautogui.hotkey('enter')
                                time.sleep(1)
                                position_lineaddbtn = pyautogui.locateOnScreen('pic/addbtn.PNG')
                                position_linebtnchat = pyautogui.locateOnScreen('pic/btnchat.PNG')
                                if position_lineaddbtn != None or position_linebtnchat != None:
                                    print(f'found this: {user_data}')
                                    line_response = requests.post(f"{domain}api/addline", headers={
                                     "Content-Type": "application/json", "Authorization": authorization_token}, 
                                         json=({"id": row_id,"type":type_id_or_tel,"user_data":user_data}))
                                    time.sleep(1)
                                    requests.post(f"{domain}api/line_status", headers={
                                     "Content-Type": "application/json", "Authorization": authorization_token}, 
                                         json=({"id": row_id,"status":1}))
                                    time.sleep(1)
                                    break
                            type_id_or_tel ='1'
                            time.sleep(5)
                        count_radio+=1
                        if count_radio == 2:   
                            requests.post(f"{domain}api/line_status", headers={
                                     "Content-Type": "application/json", "Authorization": authorization_token}, 
                                         json=({"id": row_id,"status":2}))
                    
                    #    data_arr.append(i['id'])
                    position_lineaddbtn = pyautogui.locateOnScreen('pic/addbtn.PNG')
                    position_linebtnchat = pyautogui.locateOnScreen('pic/btnchat.PNG')
                    position_lineaccpt = pyautogui.locateOnScreen('pic/accpt.PNG')
                    time.sleep(1)

                        # เจอ
                    if position_lineaddbtn != None or position_linebtnchat != None:

                        if position_lineaddbtn != None:
                                #แอตสำเร็จ
                            pyautogui.moveTo(position_lineaddbtn)
                            pyautogui.click(position_lineaddbtn)    
                            time.sleep(1)
                            num_add += 1;
                            print(f"num_add: {num_add}")
                            requests.post(f"{domain}api/line_login_otp", 
                                          json=(
                                              {
                                                "id":data_json3['data'][num_row]['id'],
                                                "num_add":num_add,
                                                "num_chat":num_chat
                                              }
                                          ), headers={"Content-Type": "application/json","Authorization":authorization_token})
                            time.sleep(1)

                                #กลิกปุ้มแอต
                            position_add = pyautogui.locateOnScreen('pic/add.PNG')
                            position_add2 = pyautogui.locateOnScreen('pic/add2.PNG')
                            lambda_click = lambda x: position_add2 if position_add == None else position_add
                            position_2click = lambda_click(position_add)
                            pyautogui.moveTo(position_2click)
                            pyautogui.click(position_2click)
                            time.sleep(1)

                                # กดปุ่มค้นหาก่อนพิม
                            pyautogui.moveTo(position_serach_friend)
                            pyautogui.click(position_serach_friend)
                            time.sleep(1)

                                #เลือกว่าเป็นเบอร์ หรือid
                            if(i['type'] == '1'):
                                pyautogui.moveTo(position_radio_line_phone)
                                pyautogui.click(position_radio_line_phone)
                            else:
                                pyautogui.moveTo(position_radio_line_id)
                                pyautogui.click(position_radio_line_id)
                                #กดปุ่มค้นหาเล็กๆ
                            pyautogui.moveTo(position_s)
                            pyautogui.click(position_s)
                            time.sleep(1)

                            pyautogui.hotkey('ctrl', 'a')
                            time.sleep(1)

                            
                            pyperclip.copy(user_seard)
                            pyautogui.hotkey('ctrl', 'v')
                            pyautogui.hotkey('enter')
                            time.sleep(1)
                        #จบแอตไปกลับ


                            # กดปุ้มแชท
                        position_linebtnchat = pyautogui.locateOnScreen('pic/btnchat.PNG')
                        pyautogui.moveTo(position_linebtnchat)
                        pyautogui.click(position_linebtnchat)
                        time.sleep(1)
                            # ส่งแชท
                        if position_linebtnchat != None:
                            for j in data_message_json['data']:
                                    # รูป
                                if (j['type'] == 0):
                                        # โหลดรูป
                                    url = f'{domain}'+j['data']
                                    filename = url.split('/')[-1]
                                    r = requests.get(url, allow_redirects=True, headers={
                                                        "Content-Type": "application/json", "Authorization": authorization_token})
                                    open('pic_chat/'+filename, 'wb').write(r.content)

                                        # กดปุ่มอัพโหลด
                                    position_lineupload = pyautogui.locateOnScreen(
                                            'pic/upload.PNG')
                                    pyautogui.moveTo(position_lineupload)
                                    pyautogui.click(position_lineupload)
                                    time.sleep(1)

                                    position_linefolder = pyautogui.locateOnScreen(
                                            'pic/folder.PNG')
                                    pyautogui.moveTo(position_linefolder)
                                    pyautogui.click(position_linefolder)
                                        # แก้ไข: เป็นpathรูปที่จะส่ง
                                    path = path_pic
        #                                 pyautogui.write(path)
                                    pyperclip.copy(path)
                                    pyautogui.hotkey('ctrl', 'v')

                                    pyautogui.hotkey('enter')
                                    time.sleep(1)

                                    position_linefile_name = pyautogui.locateOnScreen(
                                            'pic/file_name.PNG')
                                    pyautogui.moveTo(position_linefile_name)
                                    time.sleep(1)

                                        # เลื่อนไปทางซ้ายนิดหน่อย
                                    pyautogui.move(120, 0)
                                    pyautogui.click()
                                    time.sleep(1)

        #                                 pyautogui.write(filename)
                                    pyperclip.copy(filename)
                                    pyautogui.hotkey('ctrl', 'v')

                                        # กดopen
                        #                 position_lineopen = pyautogui.locateOnScreen('pic/open.PNG')
                        #                 pyautogui.moveTo(position_lineopen)
                        #                 pyautogui.click(position_lineopen)
                                    pyautogui.hotkey('enter')
                                    time.sleep(1)

                                else:
                                        # ส่งแชท
                                    position_linetextbox = pyautogui.locateOnScreen(
                                            'pic/textbox.PNG')
                                    pyautogui.moveTo(position_linetextbox)
                                    time.sleep(1)
                                    pyautogui.click(position_linetextbox)
        #                                 pyautogui.write(j['data'])
                                    pyperclip.copy(j['data'])
                                    pyautogui.hotkey('ctrl', 'v')

                                    time.sleep(1)
                                    pyautogui.hotkey('enter')
                                    time.sleep(1)
                            pyautogui.hotkey('esc')
                            num_chat += 1;
                            requests.post(f"{domain}api/line_login_otp", 
                                          json=(
                                              {
                                                "id":data_json3['data'][num_row]['id'],
                                                "num_add":num_add,
                                                "num_chat":num_chat,
                                              } 
                                          ), headers={"Content-Type": "application/json","Authorization":authorization_token})
                            time.sleep(1)
                            requests.put(f"{domain}api/line_status/{i['id']}", json=({"status":1}), headers={"Content-Type": "application/json","Authorization":authorization_token})
                            time.sleep(1)
                    else:
                            # ไม่เจอ
    #                     time_cant_find = random.randint(20, 30)
                        time_cant_find = 60
                        print(f"Not found. waiting time: {time_cant_find} s")
                        time.sleep(time_cant_find)

                        position_error_seach = pyautogui.locateOnScreen(
                                            'pic/error_seach.PNG')
                        pyautogui.moveTo(position_lineaccpt)
                        pyautogui.click(position_lineaccpt)
                        if(position_error_seach != None):  
                            print("Can't not add continue")
                            position_more = pyautogui.locateOnScreen('pic/more.PNG')
                            position_more2 = pyautogui.locateOnScreen('pic/more2.PNG')
                            lambda_click = lambda x: position_more2 if position_more == None else position_more
                            more_2click = lambda_click(position_more)
                            if(more_2click):
                                pyautogui.moveTo(more_2click)
                                pyautogui.click(more_2click)
                                time.sleep(1)
                                position_logout = pyautogui.locateOnScreen('pic/logout.PNG')
                                pyautogui.moveTo(position_logout)
                                pyautogui.click(position_logout)
                                            #เคลีย text box
                            position_textbox_btnlogin = pyautogui.locateOnScreen('pic/btnlogin.PNG')
                            if(position_textbox_btnlogin != None ):
                                pyautogui.moveTo(position_textbox_btnlogin)
                                pyautogui.move(0, -50)
                                time.sleep(1)
                                pyautogui.click()
                                pyautogui.hotkey('ctrl', 'a')
                                pyautogui.hotkey('backspace')
                                pyautogui.move(0, -50)
                                time.sleep(1)
                                pyautogui.click()
                                pyautogui.hotkey('ctrl', 'a')
                                time.sleep(0.5)
                                pyautogui.hotkey('backspace')
#                             requests.put(f"{domain}api/line_login/{data_user['id']}", json=({"status":2}), headers={"Content-Type": "application/json","Authorization":authorization_token})
                            num_row +=1;     
                            break;

                    requests.put(f'{domain}api/addline/' +
                                    str(i['id']), headers={"Content-Type": "application/json", "Authorization": authorization_token})

                    #เช็คว่าปิดยัง
                    response2 = requests.get(f"{domain}api/config", headers={
                                        "Content-Type": "application/json", "Authorization": authorization_token})
                    time.sleep(1)   
                    data_json2 = response2.json()
                    if(data_json2['data']['status'] == 0):
                        data_json['data'] = [];
                        break;
                    count_num += 1
                    if count_num >= 10:
                        count_num = 0
                        time_rand = random.randint(50, 60)
                        print(f"group is end. waiting time: {time_rand} s")
                        time.sleep(time_rand)
                        continue;
                    time_sent = random.randint(20, 30)
                    print(f"sent is end. waiting time: {time_sent} s")
                    time.sleep(time_sent)
                print("finish 1 ")
#                 num_row +=1; 
                print(f"Nexe Id: {data_json3['data'][num_row]['user_login']}")
                #เช็คว่าปิดยัง
                response2 = requests.get(f"{domain}api/config", headers={
                                        "Content-Type": "application/json", "Authorization": authorization_token})
                time.sleep(1)
                data_json2 = response2.json()
                if(data_json2['data']['status'] == 0):
                    break;
            print("อีกลูป")
            #จบการทำงาน                 
            requests.put(f"{domain}api/config/1", json=({"action":3}), headers={"Content-Type": "application/json","Authorization":authorization_token})
            # print(data_arr)
        else:
                 
                # print('ปิด')
            print('Status: Service is closed or data login is zero')
    #             position_more = pyautogui.locateOnScreen('pic/more.PNG')
    #             pyautogui.moveTo(position_more)
    #             pyautogui.click(position_more)
    #ถ้าเจอ dialog otp ให้ออก
            position_otp = pyautogui.locateOnScreen('pic/otp.PNG')
            if(position_otp != None ):
                pyautogui.hotkey('esc')
                time.sleep(1)
                pyautogui.hotkey('enter')
                    
    #เคลีย text box
            position_textbox_btnlogin = pyautogui.locateOnScreen('pic/btnlogin.PNG')
            if(position_textbox_btnlogin != None ):
                pyautogui.moveTo(position_textbox_btnlogin)
                pyautogui.move(0, -50)
                time.sleep(1)
                pyautogui.click()
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.hotkey('backspace')
                pyautogui.move(0, -50)
                time.sleep(1)
                pyautogui.click()
                pyautogui.hotkey('ctrl', 'a')
                time.sleep(0.5)
                pyautogui.hotkey('backspace')
                
            position_more = pyautogui.locateOnScreen('pic/more.PNG')
            position_more2 = pyautogui.locateOnScreen('pic/more2.PNG')
            lambda_click = lambda x: position_more2 if position_more == None else position_more
            more_2click = lambda_click(position_more)
            if(more_2click):
                pyautogui.moveTo(more_2click)
                pyautogui.click(more_2click)
                time.sleep(1)
                
                position_logout = pyautogui.locateOnScreen('pic/logout.PNG')
                pyautogui.moveTo(position_logout)
                pyautogui.click(position_logout)
            
            #ยืนยัน OTP
            response4 = requests.get(f"{domain}api/line_login/1", headers={
                                    "Content-Type": "application/json", "Authorization": authorization_token})
            time.sleep(2)
            data_json4 = response4.json()
            if(len(data_json4['data']) > 0):
                data_user = data_json4['data'][0];
                print(f"login otp by: {data_user['user_login']}");
                position_textbox_password = pyautogui.locateOnScreen(
                        'pic/textbox_password.PNG')
                pyautogui.moveTo(position_textbox_password)         
                if position_textbox_password != None:
                    pyautogui.click(position_textbox_password)
                    time.sleep(1)
        #               pyautogui.write(data_json2['data']['password'])
                    pyperclip.copy(data_user['password'])
                    pyautogui.hotkey('ctrl', 'v')
                    time.sleep(1)

                    pyautogui.hotkey('tab')
                    time.sleep(1)
        #                 pyautogui.write(data_json2['data']['user_login'])
                    pyperclip.copy(data_user['user_login'])
                    pyautogui.hotkey('ctrl', 'v')
                    time.sleep(1)
                position_textbox_btnlogin = pyautogui.locateOnScreen(
                            'pic/btnlogin.PNG')
                if(position_textbox_btnlogin != None):
                    pyautogui.moveTo(position_textbox_btnlogin)
                    pyautogui.click(position_textbox_btnlogin)
                 #ถ้าให้ยืนยันตัวตน (ลบคอมเม้น)
                time.sleep(3)
                position_otp = pyautogui.locateOnScreen('pic/otp.PNG')
                if(position_otp != None ):
                        #รอotp
                        #saveรูปที่แคป
                    now = datetime.now()
                    timestamp = datetime.timestamp(now)
                    name = str(int(timestamp));
                    position_otp = pyautogui.locateOnScreen('pic/otp.PNG')
                    [left, top, width, height] = position_otp
                    try:
                        os.remove(data_json2['data']['image_screen_shot'])
                    except Exception:
                        pass
                    myScreenshot = pyautogui.screenshot(region=(left, top, width, height+80));
                    myScreenshot.save(r'service/screen_shot/'+name+'.png');
                    time.sleep(0.5)


                            #นำภาพไปเข้าเป็นbase64 แล้วอัพขึ้นเซิฟ
                    ENCODING = 'utf-8';
                    IMAGE_NAME = f'service/screen_shot/{name}.png';
                    with open(IMAGE_NAME, 'rb') as open_file:
                        byte_content = open_file.read()
                    base64_bytes = b64encode(byte_content)
                    base64_string = base64_bytes.decode(ENCODING)                  
                    raw_data = base64_string                 
                    json_data = dumps(raw_data, indent=2)
                    requests.put(f"{domain}api/config/1", json=({"base64": json_data,"name":f"{name}.png"}), headers={"Content-Type": "application/json","Authorization":authorization_token})
                    
                    #line notify
                    message_line = f"กำลังรอ OTP ของไอดี {data_user['user_login']}"
                    line_response = requests.post(f"{domain}api/line_notify", headers={
                                            "Content-Type": "application/json", "Authorization": authorization_token}, 
                                                          json=({"message":message_line}))
                    time.sleep(1)
                    data_json_line = line_response.json()
                    print(f"line notify status: {data_json_line}")
                    time.sleep(3)
                    position_otp = pyautogui.locateOnScreen('pic/otp.PNG')

                    while position_otp != None:
                        position_otp = pyautogui.locateOnScreen('pic/otp.PNG')
                        requests.put(f"{domain}api/config/1", json=({"action":1}), headers={"Content-Type": "application/json","Authorization":authorization_token})
                        print("Waiting OTP")
                        response4 = requests.get(f"{domain}api/line_login/1", headers={
                                    "Content-Type": "application/json", "Authorization": authorization_token})
                        time.sleep(2)
                        data_json4 = response4.json()     
                        if(len(data_json4['data']) <= 0):
                            break;
                        time.sleep(3)
                        
                    #เช็คล็อกอิน (ลบคอมเม้น)
                time.sleep(3)
                position_more = pyautogui.locateOnScreen('pic/more.PNG')
                position_more2 = pyautogui.locateOnScreen('pic/more2.PNG')
                lambda_click = lambda x: position_more2 if position_more == None else position_more
                more_2click = lambda_click(position_more)
                if(more_2click!=None):
                    print("login otp success")
                    requests.put(f"{domain}api/line_login_otp/{data_user['id']}", json=({"status":2}), headers={"Content-Type": "application/json","Authorization":authorization_token})
                    requests.put(f"{domain}api/config/1", json=({"action":3}), headers={"Content-Type": "application/json","Authorization":authorization_token})
                else:
                    set_glob_fail_otp_to_one();
                    print(f"login otp fail: {fail_otp}")
                    if(fail_otp >= 2):
                        requests.put(f"{domain}api/line_login_otp/{data_user['id']}", json=({"status":0}), headers={"Content-Type": "application/json","Authorization":authorization_token})
                        set_glob_fail_otp_to_zero();
                        
                    requests.put(f"{domain}api/config/1", json=({"action":4}), headers={"Content-Type": "application/json","Authorization":authorization_token})
                    
#                     else:
#                         requests.put(f"{domain}api/line_login_otp/{data_user['id']}", json=({"status":1}), headers={"Content-Type": "application/json","Authorization":authorization_token})                 
#                         print("otp fail")
                        
                    #จบการทำงานของยืนยัน OTP
                    
        time.sleep(1)
      
    
# config
global domain;
global path_pic;

domain = "https://bot.eventmoney.site/"
# domain = "http://127.0.0.1:8000/"
path_pic = f"{pathlib.Path().absolute()}\pic_chat"
    
email = "test"
# email = "sumead007@gmail.com"
password = "aaaa7777"
request_token = requests.post(f'{domain}api/login', headers={
                                          "Content-Type": "application/json"}, json={"email": email, "password": password})
    
try:
    token_object = request_token.json()
except:
    print("รหัสไม่ถูกต้องหรือมีข้อผิดพลาดบางอย่าง")
token_str = token_object['token'].split('|')

global authorization_token 
#        global email
#        global password
authorization_token = "Bearer " + token_str[1];
    
#        while True:
# print(authorization_token)
try:
    task();
except ValueError:
    pass;

    