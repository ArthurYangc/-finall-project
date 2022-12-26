# -finall-project

## 前言
有時我們會覺得特地去做一件事情很麻煩，這時如果有個line bot，讓你在回訊息時順便做一些日常會做到的事，感覺還滿方便的。

## 構想
先進到主頁面，之後分別選擇想要做的事，這裡有天氣查詢、吃飯查詢以及貓咪影片(大家都喜歡看貓咪影片)，之後便按照想做的事給你對應的幫助。

## 環境
- python 3.11.1

## 技術
ButtonsTemplate 按鈕樣板

## 使用教學
```shell
pip3 install pipenv

pipenv --three

pipenv install

pipenv shell
```
將 LINE_CHANNEL_SECRET
   LINE_CHANNEL_ACCESS_TOKEN
   輸入`.env`檔
   
install `ngrok`

```shell
sudo snap install ngrok
```
run `ngrok` to deploy Line Chat Bot locally
```shell
ngrok http 8000
```
execute app.py
```shell
python3 app.py
```

## 使用說明
- 基本操作
    - 以下指令皆可隨時輸入
        - `start`
            - 回到初始頁
       
- 架構圖
    1. 輸入`start`開始使用生活小助手
    2. 輸入功能 -> `天氣` `貓咪` `吃飯`
   
- `天氣` 
    - 輸出天氣的網址
       
- `貓咪`
    - 輸出貓咪的網址

- `吃飯`
    - 選擇類型
        - `飯`
            - 輸出附近飯店的網址
        - `麵`
            - 輸出附近麵店的網址
        - `水餃`
            - 輸出附近水餃店的網址
           

## 使用示範


## FSM
![](C:\Users\user\Desktop\fsm.png)
### state說明
- user: 輸入fitness開始使用健身小幫手
- input_gender: 輸入男生或女生
- input_age: 輸入年齡(整數)
- input_height: 輸入身高(整數)
- input_weight: 輸入體重(整數)
- input_days: 輸入一周運動天數(整數)
- choose: 顯示個人資訊，並選擇要增肌還是減脂
- muscle: 選擇要看增肌所需的熱量或是進入搜尋健身影片模式
- show_video: 輸入想訓練的部位
- get_video: 秀出youtube推薦的健身影片
- thin: 選擇要低醣飲食還是生酮飲食
- thin_type1: 說明何謂低醣飲食
- thin_type2: 說明何謂生酮飲食
- show_cal: 顯示使用者的BMR與TDEE
- show_food: 根據使用者要增肌或低醣飲食或生酮飲食，顯示使用者一天三大營養素應該各吃多少
- show_img: 根據使用者要增肌或低醣飲食或生酮飲食，回傳三大營養素比例的圓餅圖
- query: 作者事先整理過衛生署公布的各食物營養素，使用者可輸入他想要查詢的食物，會回傳所有相關該關鍵字的食物三大營養素提供給作者參考
- 
