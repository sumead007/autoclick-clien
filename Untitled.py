#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install pyautogui


# In[66]:


# pip install opencv-python


# In[50]:


# pip install requests


# In[2]:


import pyautogui
import time 
import requests
domain ="http://127.0.0.1:8000/";
from urllib.request import urlopen
import json



# In[3]:



# import urllib library
  
# import json
# store the URL in url as 
# parameter for urlopen

# print(response.json())
  
# storing the JSON response 
# from url in data
# response = requests.get(f"{domain}api/addline")
# data_json = response.json()
  
# print the json response
# print(data_json)


# In[4]:


# response = requests.get(f"{domain}api/message")
# data_message_json = response.json()
# data_message_json


# In[86]:


# #โหลดรูป (ไม่ต้องรัน)
# url = f'{domain}service/images/1.jpg'
# filename = url.split('/')[-1]
# r = requests.get(url, allow_redirects=True)
# open('pic_chat/'+filename, 'wb').write(r.content)
# # path


# In[31]:


#เข้าระบบครั้งแรกต้องล็อกอินก่อน
# response2 = requests.get(f"{domain}api/config")
# data_json2 = response2.json()
# print(data_json2['data'])
# if(data_json2['data']['status']==0):
#     print('ปิด')
#     position_more = pyautogui.locateOnScreen('pic/more.PNG')
#     pyautogui.moveTo(position_more)
#     pyautogui.click(position_more)
#     time.sleep(1)
#     position_logout = pyautogui.locateOnScreen('pic/logout.PNG')
#     pyautogui.moveTo(position_logout)
#     pyautogui.click(position_logout)
# #     continue;
# else:
#     position_textbox_password = pyautogui.locateOnScreen('pic/textbox_password.PNG')
#     pyautogui.moveTo(position_textbox_password)
#     pyautogui.click(position_textbox_password)
#     time.sleep(1)
#     pyautogui.write(data_json2['data']['password'])
#     pyautogui.hotkey('tab')
#     time.sleep(1)
#     pyautogui.write(data_json2['data']['user_login'])
#     time.sleep(1)
#     position_textbox_btnlogin = pyautogui.locateOnScreen('pic/btnlogin.PNG')
#     pyautogui.moveTo(position_textbox_btnlogin)
#     pyautogui.click(position_textbox_btnlogin)
    
    


# In[50]:


# import os
# os.startfile("C:\\Users\\sumead007\\Documents\\flow_model")


# In[45]:



# pyautogui.write('hello world')
response2 = requests.get(f"{domain}api/config")
data_json2 = response2.json()
print(data_json2)

if(data_json2['data']['status']==1):
    position_textbox_password = pyautogui.locateOnScreen('pic/textbox_password.PNG')
    pyautogui.moveTo(position_textbox_password)
    pyautogui.click(position_textbox_password)
    time.sleep(1)
    if position_textbox_password != None:
        pyautogui.write(data_json2['data']['password'])
        pyautogui.hotkey('tab')
        time.sleep(1)
        pyautogui.write(data_json2['data']['user_login'])
        time.sleep(1)
        position_textbox_btnlogin = pyautogui.locateOnScreen('pic/btnlogin.PNG')
        pyautogui.moveTo(position_textbox_btnlogin)
        pyautogui.click(position_textbox_btnlogin)
        time.sleep(30)
    
    

    #เรียกข้อมูล
    response = requests.get(f"{domain}api/addline")
    data_json = response.json()
    response = requests.get(f"{domain}api/message")
    data_message_json = response.json()

    data_arr = [];
    for i in data_json['data']:
    #     print(i['user_id'])
        position_add = pyautogui.locateOnScreen('pic/add.PNG')
        pyautogui.moveTo(position_add)
        pyautogui.click(position_add)
        time.sleep(1)
        position_serach_friend = pyautogui.locateOnScreen('pic/serach friend.PNG')
        pyautogui.moveTo(position_serach_friend)
        pyautogui.click(position_serach_friend)
        time.sleep(1)

        if(i['type'] == '1'):
            position_radio_line_phone = pyautogui.locateOnScreen('pic/radio line phone.PNG')
            pyautogui.moveTo(position_radio_line_phone)
            pyautogui.click(position_radio_line_phone)
        else:
            position_radio_line_id = pyautogui.locateOnScreen('pic/radio line id.PNG')
            pyautogui.moveTo(position_radio_line_id)
            pyautogui.click(position_radio_line_id)
        #กดปุ่มค้นหาก่อนพิม
        position_s = pyautogui.locateOnScreen('pic/s.PNG')
        pyautogui.moveTo(position_s)
        pyautogui.click(position_s)
        time.sleep(1)

        pyautogui.hotkey('ctrl','a')

        time.sleep(1)
        pyautogui.write(i['user_id'])
        pyautogui.hotkey('enter')
        time.sleep(1)
    #     data_arr.append(i['id'])
        position_lineaddbtn = pyautogui.locateOnScreen('pic/addbtn.PNG')
        position_linebtnchat = pyautogui.locateOnScreen('pic/btnchat.PNG')
        position_lineaccpt = pyautogui.locateOnScreen('pic/accpt.PNG')

        #เจอ
        if position_lineaddbtn != None or position_linebtnchat != None:        
            pyautogui.moveTo(position_lineaddbtn)
            pyautogui.click(position_lineaddbtn)
            time.sleep(1) 
            #กดปุ้มแชท
            position_linebtnchat = pyautogui.locateOnScreen('pic/btnchat.PNG')
            pyautogui.moveTo(position_linebtnchat)
            pyautogui.click(position_linebtnchat)
            time.sleep(1) 
            #ส่งแชท
            if position_linebtnchat != None:
                for j in data_message_json['data']:
                    #รูป
                    if (j['type']==0):
                        #โหลดรูป
                        url = f'{domain}'+j['data'];
                        filename = url.split('/')[-1]
                        r = requests.get(url, allow_redirects=True)
                        open('pic_chat/'+filename, 'wb').write(r.content)

                        #กดปุ่มอัพโหลด
                        position_lineupload = pyautogui.locateOnScreen('pic/upload.PNG')
                        pyautogui.moveTo(position_lineupload)
                        pyautogui.click(position_lineupload)
                        time.sleep(1) 

                        position_linefolder = pyautogui.locateOnScreen('pic/folder.PNG')
                        pyautogui.moveTo(position_linefolder)
                        pyautogui.click(position_linefolder)
                        path = "C:\\Users\\sumead007\\Desktop\\autoclick\\pic_chat" #แก้ไข: เป็นpathรูปที่จะส่ง
                        pyautogui.write(path)
                        pyautogui.hotkey('enter')
                        time.sleep(1) 

                        position_linefile_name = pyautogui.locateOnScreen('pic/file_name.PNG')
                        pyautogui.moveTo(position_linefile_name)
                        time.sleep(1) 

                        #เลื่อนไปทางซ้ายนิดหน่อย
                        pyautogui.move(100, 0)
                        pyautogui.click()
                        time.sleep(1)     

                        pyautogui.write(filename)

                        #กดopen
        #                 position_lineopen = pyautogui.locateOnScreen('pic/open.PNG')
        #                 pyautogui.moveTo(position_lineopen)
        #                 pyautogui.click(position_lineopen)
                        pyautogui.hotkey('enter')
                        time.sleep(1) 

                    else:
                        #ส่งแชท
                        position_linetextbox = pyautogui.locateOnScreen('pic/textbox.PNG')
                        pyautogui.moveTo(position_linetextbox)
                        time.sleep(1)     
                        pyautogui.click(position_linetextbox)
                        pyautogui.write(j['data'])
                        time.sleep(1)     
                        pyautogui.hotkey('enter')
                        time.sleep(1)     
                pyautogui.hotkey('esc')
                time.sleep(1) 
        else:  
        #ไม่เจอ
            pyautogui.moveTo(position_lineaccpt)
            pyautogui.click(position_lineaccpt)
        requests.put(f'{domain}api/addline/'+str(i['id']),headers = {"Content-Type":"application/json"})
        time.sleep(5)

    # print(data_arr)
else:
    print('ปิด')
    position_more = pyautogui.locateOnScreen('pic/more.PNG')
    pyautogui.moveTo(position_more)
    pyautogui.click(position_more)
    time.sleep(1)
    position_logout = pyautogui.locateOnScreen('pic/logout.PNG')
    pyautogui.moveTo(position_logout)
    pyautogui.click(position_logout)


# In[95]:





# In[104]:



# #กดปุ่มอัพโหลด
# for i in data_message_json['data']:
#     #รูป
#     if (i['type']==0):
#         #โหลดรูป
#         url = f'{domain}'+i['data'];
#         filename = url.split('/')[-1]
#         r = requests.get(url, allow_redirects=True)
#         open('pic_chat/'+filename, 'wb').write(r.content)
        
#         #กดปุ่มอัพโหลด
#         position_lineupload = pyautogui.locateOnScreen('pic/upload.PNG')
#         pyautogui.moveTo(position_lineupload)
#         pyautogui.click(position_lineupload)
#         time.sleep(1) 

#         position_linefolder = pyautogui.locateOnScreen('pic/folder.PNG')
#         pyautogui.moveTo(position_linefolder)
#         pyautogui.click(position_linefolder)
#         path = "C:\\Users\\sumead007\\Desktop\\autoclick\\pic_chat" #แก้ไข: เป็นpathรูปที่จะส่ง
#         pyautogui.write(path)
#         pyautogui.hotkey('enter')
#         time.sleep(1) 

#         position_linefile_name = pyautogui.locateOnScreen('pic/file_name.PNG')
#         pyautogui.moveTo(position_linefile_name)
#         time.sleep(1) 

#         #เลื่อนไปทางซ้ายนิดหน่อย
#         pyautogui.move(100, 0)
#         pyautogui.click()
#         pyautogui.write(filename)

#         #กดopen
#         position_lineopen = pyautogui.locateOnScreen('pic/open.PNG')
#         pyautogui.moveTo(position_lineopen)
#         pyautogui.click(position_lineopen)
        
#     else:
#         #ส่งแชท
#         position_linetextbox = pyautogui.locateOnScreen('pic/textbox.PNG')
#         pyautogui.moveTo(position_linetextbox)
#         pyautogui.click(position_linetextbox)
#         time.sleep(1)     
#         pyautogui.write(i['data'])
#         pyautogui.hotkey('enter')
        
#     time.sleep(1) 
        


# import requests
# import json
# response_API = requests.get('https://api.covid19india.org/state_district_wise.json')
# #print(response_API.status_code)
# data = response_API.text
# parse_json = json.loads(data)
# active_case = parse_json['Andaman and Nicobar Islands']
# print("Active cases in South Andaman:", active_case)
# 
