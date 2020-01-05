# Codesignal
學習程式有很多方法，像許多網站可以教我們一些技巧。有些網站會建立教育計劃，以便我們可以按主題學習，有效率且能有明確進度的進步，然而許多這類網站都需要收費，而且無法教我們如何應用這些概念。

Python程式設計是資料科學的基本技能。為了熟悉Python的語法以及喚醒之前學習Python的記憶，老師推薦了CodeSignal以及Leetcode。

CodeSignal跟Leetcode都是充滿程式題目的平台，兩者的差別在CodeSignal的題目比較簡單一些，針對初學者使用。

# 總題目整理
- [Python Meet Python](#第一部分-Python-Meet-Python)
- [第一題](#01)
- [第二題](#02)
- [第三題](#03)
- [第四題](#04)
- [第五題](#05)
- [第六題](#06)
- [第七題](#07)
- [第八題](#08)
- [Python Intro](#第二部分-Python-Intro)

# 第一部分 Python Meet Python

## 01
![](/image/01.png)

### 解答：
res = [False]*2 會變成 res = [False, False]，而 if xs是如果xs是存在的(因為xs是空的，沒東西可以是False)，res[0]會變成True。

第二個 if xs[0]，xs是空的所以是False，res[1]不變。

#### 答案為[True, False]

## 02

![](/image/02.png)

### 解答：
題目是問哪個效率最高，選項1的函式最為精簡

#### 答案選1

## 03

![](/image/03.png)

### 解答：
在python語法中，會先處理==，所以應為a == (not b)，只有a == not b跟其他的意思不同

#### 答案選a == not b

## 04

![](/image/04.png)

### 解答：
Python中的(//)將取到的商的小數位無條件取『小』一位整數(也就是往負的方向進位)，

15/-4=-3，15//-4=-4

#### 答案選x=15,y=-4

## 05

![](/image/05.png)

### 解答：
這題是要求二進位，n.bit_length()為python語法求二進位的方式

#### 答案：n.bit_length()

## 06

![](/image/06.png)

### 解答：
題目要分辨n是否為整數，是的話return n除以2的餘數，不是就return -1

n%1==0是為了判斷n是不是整數，n除以1的餘數為0的話就表示n是整數，其餘則不是整數

#### 答案：n%1==0

## 07

![](/image/07.png)

### 解答：
題目要分辨arr中數值的大小，把數值由小排到大，他有設定for迴圈跑n（n為arr數列的長度），也設定停下的狀況，而我多加的那行就是分類，也就是分大小排序

#### 答案：arr=sorted(arr)

## 08

![](/image/08.png)

### 解答：
hex() 函数用在把10進位整數轉換成16進位制，

#### 答案：hex(int(n,x))[2:]

# 第二部分 Python Intro
