#     Stack
* 定義

Heap Sort可以分為Min Heap與Max Heap兩種。兩者用在排序上，Min Heap是「由大到小」而Max Heap則是「由小到大」。

網頁的回到上一頁的功能，「最晚進入Stack」的資料會「最先被取出」，「最早進入Stack」的資料則「最晚被取出」

是一種後進先出(Last-In-First-Out, LIFO)的排程

* Push：把資料放到最上面。

* Pop：把「最上面」的資料移除。

* Top：回傳「最上面」的資料，確認「最上面」的是什麼。

*	IsEmpty：確認Stack裡是否有資料。

*	getSize：回傳Stack裡的資料個數。

-array

堆疊建立時即建立一個陣列，並使用一個索引來記錄目前所指到的位址，新增或移除資料時，同步修改索引位址。優點是不用處理指標鏈結建立與移除，缺點是容量超過陣列大小時需要額外處理。

-linked-list

用指標將資料串起來，將新的東西不斷接在最後面，而取出時則移除最後面的東西即可。優缺點與陣列相反。

* 圖片例子

 ![](/image/Stack1.png)
 
 #     Queue
* 定義

排隊，不能插隊。一次只能執行一個需求，所以需要用 Queue來安排執行順序。（影印機印紙一次印一張）


* Push：把資料放進Queue的最後面，成新的back。

* Pop：把front最前面所指向的資料從Queue中移除，並更新front。

* getFront：回傳front所指向的資料。

* getBack：回傳back所指向的資料。

* IsEmpty：確認Queue裡是否有資料。

* getSize：回傳Queue裡的資料個數。

 
 #     Tree
* 定義
最廣義的樹，樹上的node之child數沒有限制，因此每個node可以有多個child。

## Binary Tree(二元樹)
* 定義

限制node最多有兩個child，子節點有左右之分，稱兩個child pointer為left child和right child。樹的樹根稱為Root，樹的「分支」為Branch。
1和2是0的子節點，6和7是3的子節點，1是3和4的「父節點」(Parent)

* parent：父節點
* left：左子節點。
* right：右子節點。
* addLeft：加入左子節點。
* addRight：加入右子節點。
* remove：移除節點。
* level：節點的階層。
* depth：樹的深度，最大階層數
* size：子樹的節點個數。

-完滿二元樹(Full binary tree)

每個節點有0或2個子節點。

-完全二元樹(Complete binary tree)

除了最後一階層之外的階層都必須填滿，而最後一階層的節點必須由左至右填入。

-完美二元樹(Perfect binary tree)

同時滿足完滿二元樹的條件，並且所有的節點都在同一個階層。

## Binary Search Tree(BST，二元搜尋樹)
* 定義

 是基於二元樹的一種延伸，可以利用在搜索、排序和提供資料集合基本結構，發展其他資料結構。
 
1.小於根節點 ( root )的放左邊節點 ( left node )

2.大於根節點 ( root )的放右邊節點 ( right node ) 

3.任意節點 ( node ) 的左、右子樹也分別符合 BST 的定義

* insert(新增資料)：要在BST中新增node(新增資料)。

* search(搜尋資料)：在處理資料時，時常需要尋找某特定資料是否存在資料結構中。

*  delete(刪除資料):刪除不能直接把節點與其子孫全部移除，要讓樹保持二元搜索樹的定義，基本上有三種情況需要考慮：

 -沒有子節點時，可以直接移除。
 
 -有一個子節點時，將子節點取代被移除的節點的位置。
 
 -有兩個子節點時，可以從左子樹找到最大值或右子樹找到最小值的節點，來取代被移除的節點位置。

新增資料(insert)、刪除資料(delete)本身都必須先執行一次搜尋(search)，而搜尋(search)的時間複雜度取決於BST的height(樹高) ，height為logN

