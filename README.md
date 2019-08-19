# Facebook粉絲專頁人數追蹤器

使用Python去抓取特定紛絲專頁的按讚數。

### 程式語言

Python

### 套件使用

selenium, codecs, tkinter, os, time, datetime, random

## 使用說明
### 抓取資料
1.將檔案全部下載下來，有fans.py、main.py、gif.py三個檔案。  
2.下載與電腦所使用的chrome瀏覽器有所對應的chromedriver，並放入同一個資料夾。
下載網址:https://chromedriver.chromium.org/
版本資訊可於chrome設定中，關於chrome中得知，如圖所示。  
![image](https://github.com/korigami1005/FacebookFans/blob/master/images/chorme%20version.png)
3.開啟終端機使用python執行fans.py。  
```
python fans.py
```
4.依據各欄位說明，填入對應內容，如圖所示。  
![image](https://github.com/korigami1005/FacebookFans/blob/master/images/fans.png)
5.按下「產生」，會自動生成對應檔案，如圖所示，即可關閉此頁面。  
![image](https://github.com/korigami1005/FacebookFans/blob/master/images/new%20file.png)
6.如原先python沒有安裝selenium套件，請先安裝。
7.開啟終端機使用python執行你所產生的檔案，即可開始抓取資料，程式會自動將資料存成data.txt。  
```
python ???_0830.py
```
每一筆資料包含三個欄位，分別為預設的編號、抓取的按讚人數、抓取的當下時間。  
  
### 簡易資料視覺化  
#### 執行 main.py  
畫面會如同直播，會更新畫面至最新檔案狀況。  
#### 執行 gif.py  
畫面會從所收集資料第一筆開始繪製，繪製至最後一筆。    
可參考此影片：https://youtu.be/CybGg1Dkc5w  
如要儲存成影片檔(.mp4)，請開啟gif.py，修改最後兩行內容如下(fps值為每秒畫面所跑的資料量)。  
```
ani.save('sample.mp4', writer='ffmpeg',fps = 20)
#plt.show()
```
# 如有疑問，請寄信至 korigami1005@gmail.com
