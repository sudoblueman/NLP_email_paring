from cnsenti import Emotion
from cnsenti import Sentiment
import json
import re
import jieba
import spacy
from opencc import OpenCC
import sys
from os import path
import time

#email 套件
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.mime.image import MIMEImage
from pathlib import Path

import smtplib


from string import Template


#if __name__ == "__main__":


def send_match_email(match_email_send,username,matcher_mail_2,username_2,text_in_a,text_in_b,sim,pic_a,pic_b):

    #template = Template(Path('/success_template.html').read_text())
    #body = template.substitute({ 
        #"user": username,
        #"user_2":username_2,
        #"send_to_matched_email":matcher_mail_2
    
    #})

    content = MIMEMultipart('alternative')  #建立MIMEMultipart物件
    content["subject"] = "一網情深 click and love"  #郵件標題
    content["from"] = "r@gmail.com"  #寄件者
    content["to"] = match_email_send  #收件者
    #content.attach(MIMEText(body, "html"))  # HTML郵件內容
    content.attach(MIMEText("恭喜 【 "+str(username)+ " 】 配對成功 !!! 您的配對對象是 【 "  + str(username_2) +" 】 ，配對分數達到 "+ str(round(sim*100,1))+" 分!!!" +" \n歡迎進一步email到他/她的信箱 "+str(matcher_mail_2)+" 做聯繫喔\n\n"+"="*10+"以下是對方的自我介紹"+"="*10+"\n\n"+text_in_b))  #郵件內容
    
    
    #content.attach(MIMEImage(Path("/home/tibamelala/ai_project_web/uploadPHP/savepath/"+str(pic_b)+".png").read_bytes()))  # 郵件圖片內容
  
    
    #print("/home/tibamelala/ai_project_web/uploadPHP/savepath/"+pic_b+".png")

    #更換測試圖片  
    attachment="/home/tibamelala/ai_project_web/uploadPHP/savepath/"+pic_b+".png"
    #attachment="/home/tibamelala/ai_project_web/tibame_group_project-main/NLP/test_NLP.png"

    part = MIMEImage(open(attachment, 'rb').read())
    content.attach(part)




    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("email", "password")  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("已寄出Complete!")
        except Exception as e:
            print("Error message: ", e)

#def pri_send_match_email(match_email_send,username,matcher_mail_2,username_2,text_in_a,text_in_b,sim):
    #print("恭喜 [ "+str(username)+ " [ 配對成功 !!! 您的配對對象是 [ "  + str(username_2) +" ] ，配對分數達到 "+ str(round(sim*100,1))+" 分!!!" +" \n歡迎進一步email到他/她的信箱 "+str(matcher_mail_2)+" 做聯繫喔\n\n"+"="*10+"以下是對方的自我介紹"+"="*10+"\n\n"+text_in_b)) 


#input 路徑 "/home/tibamelala/ai_project_web/uploadPHP/NLP_input_ready_for_test/"

#file_path = path.relpath("/home/tibamelala/ai_project_web/uploadPHP/NLP_input_ready_for_test/20211224100411.json")
#with open(file_path) as f:
    #print("open 成功")

all={}
index=[]
index_pic=[]
import os

#比較整齊是統一輸出在一個資料夾
#Path = "/home/tibamelala/ai_project_web/uploadPHP/NLP_input_ready/"

Path = "/home/tibamelala/ai_project_web/uploadPHP/"
filelist = os.listdir(Path)
for i in filelist:
    if i.endswith(".json"):  # You could also add "and i.startswith('f')
        with open(Path + i, 'r') as f:
            all[(str(i).split(".")[0])] = json.loads(f.read()) 
            #print(str(i)+"存檔成功") 
            #存 key
            index.append(str(i).split(".")[0])      
            #for line in f:
                # Here you can check (with regex, if, or whatever if the keyword is in the document.)
#存成大字典                
#print(all)  


#json 排序，最新到最舊
index= sorted(index,reverse=True)
#print(index)              



#抓圖片目錄

Path_pic="/home/tibamelala/ai_project_web/uploadPHP/savepath/"
filelist_pic = os.listdir(Path_pic)
for i in filelist_pic:
    if i.endswith(".png"):  # You could also add "and i.startswith('f')
        with open(Path_pic + i, 'r') as f:
            #print(str(i)+"圖片目錄讀取成功") 
            #存 key
            index_pic.append(str(i).split(".")[0])      

#pic 排序，最新到最舊
index_pic= sorted(index_pic,reverse=True)
#print(index_pic) 



#確定是否偶數個檔案排序跟判斷偶數

#count=3
#while len(index)%2!=0:

    #print("還沒偶數個")
    #print("配對中，正等待另外一個人完成送出，請稍後......") 
    #time.sleep(10)




    #重新抓一次
    #Path = "/home/tibamelala/ai_project_web/uploadPHP/"
    #filelist = os.listdir(Path)    
    #for i in filelist:
        #if i.endswith(".json"):  # You could also add "and i.startswith('f')
            #with open(Path + i, 'r') as f:
                #比對新檔，存 key
                #if str(i).split(".")[0] not in index:
                    #all[(str(i).split(".")[0])] = json.loads(f.read()) 
                    #print(str(i)+"存檔成功") 
                #比對新檔，存 目錄
                #if str(i).split(".")[0] not in index:
                    #index.append(str(i).split(".")[0])      
    #index= sorted(index,reverse=True)


    
    #count-=1
    #if count < 0:
        #print("配對人數不足!!! 請重新輸入!!!")
        #os.remove("/home/tibamelala/ai_project_web/uploadPHP/"+index[0]+".json")
        #TODO 儲存需要重新輸入訊息的 json     
        #sys.exit(0)
#沒有要做即時配對，直接判斷不等待
#if  len(index)%2!=0:
    #print("等待配對中")   
    #sys.exit(0)    
#if len(index)%2==0:

    #print("開始配對......\n\n",index)
#讀完移動json 到已經讀取的資料夾

#讀取json 測試，看是否都讀取到兩個檔案


#try:
  #with open('1_php_input.json') as f:
      #in_a = json.loads(f.read())
  
  #with open('2_php_input.json') as f:
      #in_b = json.loads(f.read())
      
# 沒有讀到其中一個人的檔案，php 要重新呼叫nlp.py
#except:
  #print("配對中，正等待另外一個人完成送出，請稍後......") 
  #sys.exit(0)

#print("配對完成")

#print(data2)

#印出測試
#with open("_inputest_result_dict_sim_o.json", "w") as f:
#    #json.dump(data2, f, indent = 4) 
     #str_=json.dumps(data2, indent = 4)
     #f.write(str(str_))      

#繁轉簡

cc = OpenCC('t2s')



# load  nlp model zh_core_web_md 輕量化模型
nlp = spacy.load("zh_core_web_md")
#model = FastText.load_fasttext_format('cc.zh.300.bin')


# 解析 從 php來的 JSON 字串資料
# in_a = json.loads(in_a_from_php)
# in_b = json.loads(in_b_from_php)
in_a = all[index[0]]


in_b = all[index[1]]

#print("A",in_a)

#print(in_b)
#接收php文字 A的自我介紹跟B的自我介紹


#測試文字輸入讀取請況

#print(in_a)
#print(in_b)

#情緒分析
def w2np(test_text,numf):
  senti = Sentiment()
  emotion = Emotion()
  
  result_emotion = emotion.emotion_count(cc.convert(test_text))
  result_senti  = senti.sentiment_count(cc.convert(test_text))
  # print(result_emotion)
  # print(result_senti)

  print("情緒分析中")

  # ***********輸出情緒分析資料************
  n_dict = {
      "words": str(result_emotion['words']),
      "sentences":str(result_emotion['sentences'] ),
      "like": str(result_emotion['好']),
      "happy":str(result_emotion['乐']),
      "sad" :str(result_emotion['哀']),
      "angry" :str(result_emotion['怒']), 
      "afraid" :str(result_emotion['惧']), 
      "disgust" :str(result_emotion['恶']),
      "shocked":str(result_emotion['惊']),
      "pos":str(result_senti['pos']),
      "neg": str(result_senti ['neg']),
      "input":test_text,
      "person":str(numf)#第幾個人
  }
  print(n_dict)
  #print("情緒分析中2")
  # 列印分析文字情感分析
  # print(n_dict)
  #print("AA",str(numf))
  # 將 Python 資料轉為 JSON 格式，儲存至 n_dict_output.json 檔案
  path_o_p="/home/tibamelala/ai_project_web/uploadPHP/NLP_output_person/"
  with open(path_o_p+str(numf)+"_n_dict_output.json", "w") as f:
      json.dump(n_dict, f, indent = 4)
      #print("情緒分析json 成功")

#相似度分析
def sim(a,b,comb):
    def process(content):

      #要刪除的標點符號
      punct = set(u''':!),.:;?]}¢'"、。〉》」』】〕〗〞︰︱︳﹐､﹒﹔﹕﹖﹗﹚﹜﹞！），．：；？｜｝︴︶︸︺︼︾﹀﹂﹄﹏､～￠々‖•·ˇˉ―--′’”([{£¥'"‵〈《「『【〔〖（［｛￡￥〝︵︷︹︻︽︿﹁﹃﹙﹛﹝（｛“‘-—_…~/ －＊➜■─★☆=@<>◉é''')  
      content = re.sub(r'https?:\/\/.*[\r\n]*', '', content)
      fil = filter(lambda x: x not in punct, jieba.cut(content))
      content = " ".join(fil)
      return content

    #****輸出文句相似度Json 格式 s_dict:*****


    s_dict = {
        "person_a_sentense": a,#第一個人文句
        "person_b_sentense":b ,#第二個人文句
        "similarity":"",#文章風格相似度
        "success_match":"N/A" #是否成功配對
    }

    #情緒分析，篩檢正面情緒要>負面情緒
    senti = Sentiment()

    result_senti_a  = senti.sentiment_count(cc.convert(a)) 
    result_senti_b  = senti.sentiment_count(cc.convert(b))   
     


    a=process(a)
    a_d=nlp(a)
    #print(a_d)
    b=process(b)
    b_d=nlp(b)
    #print(b_d)
    distance=a_d.similarity(b_d)
    
    #print(result_senti_a)
    #print(result_senti_b)
    
    #try:
      #distance = model.wv.n_similarity(a.lower().split(), b.lower().split())
    #except:
      #distance = model.wv.similarity(a, b)
      # print("Q")
    if  int(result_senti_a['pos'])-int(result_senti_a['neg']) >= -3 and int(result_senti_b['pos'])- int(result_senti_b['neg']) >=-3 and distance >=0.85:
        print("配對成功 !!! 文句風格相似度 = \n"+ str(round(distance*100,1))+"分")
        s_dict["success_match"]="success" 
        print("\n 雙方的email 為 "+in_a["email"]+" 跟 "+in_b["email"]+" 歡迎進一步聯繫")
        #pri_send_match_email(in_a["email"],in_a["nickname"],in_b["email"],in_b["nickname"],in_a["NLP_input"],in_b["NLP_input"],distance)
        #暫時關閉
        #send_match_email(in_a["email"],in_a["nickname"],in_b["email"],in_b["nickname"],in_a["NLP_input"],in_b["NLP_input"],distance,index_pic[0],index_pic[1]) 
        #send_match_email(in_b["email"],in_b["nickname"],in_a["email"],in_a["nickname"],in_b["NLP_input"],in_a["NLP_input"],distance,index_pic[1],index_pic[0])                     
    else:
        s_dict["success_match"]="fail"
        print("配對失敗，文句相似度 = "+ str(distance))
    s_dict["similarity"]=str(distance)
    
    print(s_dict)
    #output 路徑 /home/tibamelala/ai_project_web/uploadPHP/NLP_output
    Path_out = "/home/tibamelala/ai_project_web/uploadPHP/NLP_output/"
    #with open(Path_out+comb+"_s_dict_sim_o.json", "w") as f:
    with open(Path_out+"ab_s_dict_sim_o.json", "w") as f:    
        json.dump(s_dict, f, indent = 4)    
        print("相似度json儲存成功")

#輸入欄位  key "input" 文字字串作為 php 文字框字典檔輸入欄位
#相似度分析
sim(in_a["NLP_input"],in_b["NLP_input"],'ab') # 輸出 ab_s_dict_sim_o.json



#情緒分析產生      
w2np(in_a["NLP_input"],1)# 輸出 1_n_dict_output.json
w2np(in_b["NLP_input"],2)# 輸出 2_n_dict_output.json


    
    
    
