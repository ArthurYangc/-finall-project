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
![](https://github.com/ArthurYangc/-finall-project/blob/main/final%20project/picture/130688.jpg)

![](https://github.com/ArthurYangc/-finall-project/blob/main/final%20project/picture/130689.jpg)

![](https://github.com/ArthurYangc/-finall-project/blob/main/final%20project/picture/130690.jpg)

![](https://github.com/ArthurYangc/-finall-project/blob/main/final%20project/picture/130691.jpg)

![](https://github.com/ArthurYangc/-finall-project/blob/main/final%20project/picture/130692.jpg)

![](https://github.com/ArthurYangc/-finall-project/blob/main/final%20project/picture/130693.jpg)

![](https://github.com/ArthurYangc/-finall-project/blob/main/final%20project/picture/130694.jpg)

## FSM
![](https://github.com/ArthurYangc/-finall-project/blob/main/final%20project/picture/fsm.png)

### state說明
- user: 輸入start開始使用生活小助手
- start: 選擇想要的功能
- weather: 查詢天氣
- cat: 找尋貓咪影片
- eat: 選擇食物類型
- rice: 查詢附近飯店
- noodle: 查詢附近麵店
- dumpling: 查詢附近水餃店
- fsm: 輸出fsm圖

