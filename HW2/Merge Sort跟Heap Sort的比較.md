## heap sort 
 
* 不一樣的地方
 
Heap Sort可以分為Min Heap與Max Heap兩種。兩者用在排序上，Min Heap是「由大到小」而Max Heap則是「由小到大」。

最小堆積樹(Min Heap)：樹根(二元樹的最頂端)一定是最小值
將樹根(最小值)與最後一個節點調換，將最小值取出，並加入已排序數列，重複步驟，將整棵樹重新調整為最小堆積樹

最大堆積樹(Max Heap)：樹根(二元樹的最頂端)一定是最大值
將樹根(最大值)與最後一個節點調換，將最大值取出，並加入已排序數列，重複步驟，將整棵樹重新調整為最大堆積樹

額外空間:只需一額外記錄空間。

----------------------------------------

* 一樣的地方

最佳狀況時間複雜度：n log n

平均狀況時間複雜度：n log n

最差狀況時間複雜度：n log n



## merge sort
 
* 不一樣的地方

把問題先拆解成子問題，逐一處理子問題後，將子問題的結果合併。

1.將陣列分割直到只有一個元素。

2.開始兩兩合併，合併時同時進行排序。

3.重複2的動作直到全部合併完成。

額外空間:需n個額外記錄空間。

----------------------------------------

* 一樣的地方

最佳狀況時間複雜度：n log n

平均狀況時間複雜度：n log n

最差狀況時間複雜度：n log n
