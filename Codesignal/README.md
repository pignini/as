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
- [第一題](#1)
- [第二題](#2)
- [第三題](#3)
- [第四題](#4)
- [第五題](#5)
- [第六題](#6)

# 第一部分 Python Meet Python

## 01
![](/image/01.png)

### 解答：
res = [False]*2 會變成 res = [False, False]，而 if xs是如果xs是存在的(因為xs是空的，沒東西可以是False)，res[0]會變成True。

第二個 if xs[0]，xs是空的所以是False，res[1]不變。

#### 答案：[True, False]

## 02

![](/image/02.png)

### 解答：
題目是問哪個效率最高，選項1的函式最為精簡

#### 答案：1

## 03

![](/image/03.png)

### 解答：
在python語法中，會先處理==，所以應為a == (not b)，只有a == not b跟其他的意思不同

#### 答案：a == not b

## 04

![](/image/04.png)

### 解答：
Python中的(//)將取到的商的小數位無條件取『小』一位整數(也就是往負的方向進位)，

15/-4=-3，15//-4=-4

#### 答案：x=15,y=-4

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

---------------------------

# 第二部分 Python Intro

## 1
![](/image/1.png)

### 解答：
題目給我param1 = 1，param2 = 2和add(param1,param2)，他要我們把這兩個變數加起來並且顯示出來

def是定義一個函數，return可以把我要的答案丟出來

#### 答案：def add(param1, param2): return param1+param2

## 2

![](/image/2.png)

### 解答：
題目要判斷西元幾年會是幾世紀，對於year = 1905，輸出應為CenturyFromYear（year）= 20;year = 1700，輸出應為CenturyFromYear（年）= 17

#### 答案：int((year-1)/100)+1

## 3

![](/image/3.png)

### 解答：
題目是判斷假如整個字串相反是否跟原本一樣

[::-1]是顺序相反的意思，假如a=[1,2,3,4,5] b=a[::-1]，b就會是[5, 4, 3, 2, 1]

#### 答案：if(inputString==inputString[::-1])：

## 4

![](/image/4.png)

### 解答：
題目是乘旁邊的數值比出最大的數，字串 = [3，6，-2，-5，7，3]，輸出應為neighborElementsProduct（inputArray）= 21，7乘以3產生最大的數值。

#### 答案：    a=inputArray[0]b=a*inputArray[1] for i in inputArray[1::]: if a*i>b: b=a*ia=i else: return b

## 5

![](/image/5.png)

### 解答：
題目是若n = 2，輸出應為shapeArea（n）= 5;n = 3，輸出應為shapeArea（n）= 13

計算是應為n*n+(n-1)*(n-1)

#### 答案：return (n*n+(n-1)*(n-1))

## 6

![](/image/6.png)

### 解答：
題目是要找出缺得值，數列= [6，2，3，8]，輸出應為makeArrayConsecutive2（statues）= 3，缺少4、5和7，三個值。

所以是最大值減最小值再減掉字串長度再加1

#### 答案： return max(statues)-min(statues)-len(statues)+1

