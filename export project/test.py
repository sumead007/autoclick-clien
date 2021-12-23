##current only command has not a try catch
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


def task():
    while True:
            
        response2 = requests.get(f"{domain}api/config", headers={
                                    "Content-Type": "application/json", "Authorization": authorization_token})
            
        data_json2 = response2.json()
        print('config')
        print(data_json2)
        requests.put(f"{domain}api/config/1", json=({"action":0}), headers={"Content-Type": "application/json","Authorization":authorization_token})
            
        if(data_json2['data']['status'] == 1):
            print('Status: Service is opened')
                
                #กันล็อกอินซั้า
#                 email
#                 password
            position_textbox_password = pyautogui.locateOnScreen(
                    'pic/textbox_password.PNG')
            pyautogui.moveTo(position_textbox_password)         
            if position_textbox_password != None:
                pyautogui.click(position_textbox_password)
                time.sleep(1)
    #               pyautogui.write(data_json2['data']['password'])
                pyperclip.copy(data_json2['data']['password'])
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(1)
                    
                pyautogui.hotkey('tab')
                time.sleep(1)
    #                 pyautogui.write(data_json2['data']['user_login'])
                pyperclip.copy(data_json2['data']['user_login'])
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(1)
            position_textbox_btnlogin = pyautogui.locateOnScreen(
                        'pic/btnlogin.PNG')
            if(position_textbox_btnlogin != None):
                pyautogui.moveTo(position_textbox_btnlogin)
                pyautogui.click(position_textbox_btnlogin)
                    
                    #ถ้าให้ยืนยันตัวตน (ลบคอมเม้น)
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
                chk_turn_off = True;
                    
                while position_otp != None and chk_turn_off:
                    position_otp = pyautogui.locateOnScreen('pic/otp.PNG')
                    requests.put(f"{domain}api/config/1", json=({"action":1}), headers={"Content-Type": "application/json","Authorization":authorization_token})
                        
                    print("Waiting OTP")
                        
                    response2 = requests.get(f"{domain}api/config", headers={
                                    "Content-Type": "application/json", "Authorization": authorization_token})
                    data_json2 = response2.json()
                    if(data_json2['data']['status'] != 1):
                        chk_turn_off = False;
                        print("Trun Off")
                            
                    time.sleep(2)
                    # time.sleep(180)
            else:
                print("Waiting a second")
                time.sleep(2)
                        
            #เช็คล็อกอิน (ลบคอมเม้น)
            position_more = pyautogui.locateOnScreen('pic/more.PNG')
            position_more2 = pyautogui.locateOnScreen('pic/more2.PNG')
            lambda_click = lambda x: position_more2 if position_more == None else position_more
            more_2click = lambda_click(position_more)
            if(more_2click == None):
                print("Login failed")
                requests.put(f"{domain}api/config/1", json=({"action":4}), headers={"Content-Type": "application/json","Authorization":authorization_token})
                continue;

                # เรียกข้อมูล
            response = requests.get(f"{domain}api/addline", headers={
                                        "Content-Type": "application/json", "Authorization": authorization_token})
            response.encoding = 'ISO-8859-1'
            data_json = response.json()
                
            response = requests.get(f"{domain}api/message", headers={
                                        "Content-Type": "application/json", "Authorization": authorization_token})
            response.encoding = 'ISO-8859-1'
            data_message_json = response.json()
                
                
            data_arr = []
            print('Process Start....')
            requests.put(f"{domain}api/config/1", json=({"action":2}), headers={"Content-Type": "application/json","Authorization":authorization_token})
                
            for i in data_json['data']:
                print('userID: ')
                print(i['user_id'])

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
                    
    #เลือกว่าเป็นเบอร์ หรือid
                if(i['type'] == '1'):
                    position_radio_line_phone = pyautogui.locateOnScreen(
                            'pic/radio line phone.PNG')
                    pyautogui.moveTo(position_radio_line_phone)
                    pyautogui.click(position_radio_line_phone)
                else:
                    position_radio_line_id = pyautogui.locateOnScreen(
                            'pic/radio line id.PNG')
                    pyautogui.moveTo(position_radio_line_id)
                    pyautogui.click(position_radio_line_id)
                        
                    #กดปุ่มค้นหาเล็กๆ
                position_s = pyautogui.locateOnScreen('pic/s.PNG')
                pyautogui.moveTo(position_s)
                pyautogui.click(position_s)
                time.sleep(1)

                pyautogui.hotkey('ctrl', 'a')
                time.sleep(1)
                    
    #               pyautogui.write(i['user_id'])
                pyperclip.copy(i['user_id'])
                pyautogui.hotkey('ctrl', 'v')
                    
                pyautogui.hotkey('enter')
                time.sleep(1)
                #    data_arr.append(i['id'])
                position_lineaddbtn = pyautogui.locateOnScreen('pic/addbtn.PNG')
                position_linebtnchat = pyautogui.locateOnScreen('pic/btnchat.PNG')
                position_lineaccpt = pyautogui.locateOnScreen('pic/accpt.PNG')

                    # เจอ
                if position_lineaddbtn != None or position_linebtnchat != None:
                        
                    if position_lineaddbtn != None:
                            #แอตสำเร็จ
                        pyautogui.moveTo(position_lineaddbtn)
                        pyautogui.click(position_lineaddbtn)    
                        time.sleep(1)
                            
                            #กลิกปุ้มแอต
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
                            
                        pyperclip.copy(i['user_id'])
                        pyautogui.hotkey('ctrl', 'v')
                    
                        pyautogui.hotkey('enter')
                        time.sleep(1)
                            
                            
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
                                pyautogui.move(100, 0)
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
                        time.sleep(1)
                else:
                        # ไม่เจอ
                    pyautogui.moveTo(position_lineaccpt)
                    pyautogui.click(position_lineaccpt)
                requests.put(f'{domain}api/addline/' +
                                str(i['id']), headers={"Content-Type": "application/json", "Authorization": authorization_token})
                
                #เช็คว่าปิดยัง
                response2 = requests.get(f"{domain}api/config", headers={
                                    "Content-Type": "application/json", "Authorization": authorization_token})
                data_json2 = response2.json()
                if(data_json2['data']['status'] == 0):
                    data_json['data'] = [];
                    break;
                time.sleep(2)
                #จบการทำงาน
                
                
            requests.put(f"{domain}api/config/1", json=({"action":3}), headers={"Content-Type": "application/json","Authorization":authorization_token})
                # print(data_arr)
        else:    
                # print('ปิด')
            print('Status: Service is closed')
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
        #     root.after(2000, task)  # reschedule event in 2 seconds
        time.sleep(1)
      
    
# config
global domain;
global path_pic;
domain = "https://bot.eventmoney.site/"
path_pic = f"{pathlib.Path().absolute()}\pic_chat"
    
email = "test"
password = "12345678"
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
task();
    
    
      