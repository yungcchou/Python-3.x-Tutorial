# 4 Loop

使用迴圈操作的主要原因是為了自動化、**提高效率**和**靈活性**，從而減少手動操作的重複性工作。它讓程式能夠輕鬆處理大型資料集、動態控制流程，並且可以更快速地完成重複性任務。在 Python 程式設計中，**迴圈操作（疊代）** 是非常重要的，原因如下：
### 1. **自動化重複任務**：
迴圈允許程式自動執行重複性操作，而無需手動撰寫多次相同的程式碼。如果你需要執行某段程式碼 100 次，使用迴圈可以大幅減少程式碼量並提高程式的可維護性。

**範例**：
```python
for i in range(100):
    print("這是第", i + 1, "次執行")
```
這段程式碼會自動列印 100 次訊息，而不需要撰寫 100 行相同的程式碼。

### 2. **處理大量數據**：
迴圈操作非常適合處理大型資料集或序列，例如列表、元組、字典等。在 Python 中，你可以使用迴圈來逐個處理每個元素，並根據需求進行操作。

**範例**：
```python
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print("總和是:", total)
```
此程式碼將逐個處理列表中的每個數字，並計算它們的總和。

### 3. **動態控制流程**：
有些情境下，你無法預知需要重複操作多少次，這時 `while` 迴圈會很有用，它會根據動態變化的條件決定是否繼續執行。

**範例**：
```python
count = 1
while count <= 5:
    print("這是第", count, "次執行")
    count += 1
```
在這裡，迴圈會持續運行，直到 `count` 達到 5 為止。

### 4. **提升程式效率**：
迴圈使得 Python 程式更具彈性和高效，特別是在需要重複操作的情況下。它能夠自動處理大批資料並且進行複雜的計算，這對於資料分析、網頁爬蟲和機器學習等領域來說尤為重要。

### 5. **結合其他功能**：
迴圈可以與條件判斷 (`if` 條件) 結合使用，來對特定條件進行操作，這使得程式能夠靈活應對不同的情況。

**範例**：
```python
for i in range(10):
    if i % 2 == 0:
        print(i, "是偶數")
    else:
        print(i, "是奇數")
```
這段程式碼會檢查每個數字是奇數還是偶數，並根據條件輸出不同的結果。

---
在 Python 程式設計中，**迴圈疊代**（loop iteration）是指在特定條件為真時，反覆執行一段程式碼，直到滿足結束條件為止。Python 提供了兩種主要的迴圈方式來進行疊代：

## **`for` 迴圈**

`for` 迴圈用來對一個序列（如列表、元組、字典、集合或字串）進行疊代，並對序列中的每個元素執行程式碼。當序列中的所有項目都被處理後，`for` 迴圈會自動結束。

   **範例**：
   ```python
   fruits = ["apple", "banana", "cherry"]
   for fruit in fruits:
       print(fruit)
   ```
   輸出：
   ```
   apple
   banana
   cherry
   ```
### opportunity for using `for` loop

`for` 迴圈非常適合用來處理已知大小的序列或集合、執行固定次數的操作、遍歷字典、處理資料集、生成數字範圍，或者是進行多層疊代。它簡潔且易於使用，是 Python 程式設計中非常常用的工具。在 Python 中，**`for` 迴圈** 適合用於以下幾種情境，特別是當你需要對一個已知範圍或序列中的元素進行操作時：

### 1. **遍歷固定的序列或集合**
當你需要對一個已知的序列（例如列表、元組、字典、集合或字串）中的每個元素進行操作時，`for` 迴圈是最佳選擇。

**範例**：依次列印 list 的水果名稱
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### 2. **需要重複執行固定次數的操作**
如果你知道需要重複執行的次數，可以使用 `for` 迴圈搭配 `range()` 函數。

**範例**：執行 5 次，並輸出對應次數的訊息
```python
for i in range(5):
    print("這是第", i + 1, "次執行")
```

### 3. **對字典進行疊代**
當你想要遍歷字典中的鍵或鍵值對時，`for` 迴圈可以輕鬆實現。

**範例**：列出字典中所有的鍵和值
```python
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(key, ":", value)
```

### 4. **使用 `for` 迴圈處理數據集合**
當你有一組資料，並需要對每個資料項目進行處理或運算時，`for` 迴圈非常適合。

**範例**：計算列表中所有數字的總和
```python
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print("總和是:", total)
```

### 5. **生成有規律的序列或範圍**
當你需要生成或遍歷一個範圍內的數字時，`for` 迴圈搭配 `range()` 是很方便的選擇。例如，生成偶數、奇數、或是等差序列。

**範例**：輸出 0、2、4、6、8，即從 0 開始，每次增加 2 的數字序列
```python
for i in range(0, 10, 2):
    print(i)
```

### 6. **使用 `for` 迴圈與列表生成式**
當你需要對一個列表進行轉換或過濾時，可以使用 `for` 迴圈搭配列表生成式來快速產生新列表。

**範例**：生成 [0, 1, 4, 9, 16]，即 0 到 4 的平方值列表
```python
squares = [x**2 for x in range(5)]
print(squares)
```

### 7. **處理文件或輸入數據**
當你需要逐行讀取文件內容或輸入數據時，`for` 迴圈可以簡化操作，尤其是處理大型文件時。

**範例**：逐行讀取文件並列印出內容
```python
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())
```

### 8. **嵌套迴圈進行多層疊代**
當你有多維結構（如二維列表）需要進行疊代時，可以使用嵌套的 `for` 迴圈。

**範例**：輸出 Matrix 中的每個元素
```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()
```


---
## **`while` 迴圈**

- `while` 迴圈的主要原因在於它的靈活性，適合在條件不確定的情況下使用。
- 無論是等待條件變化、處理動態事件，還是持續監控，`while` 迴圈都能夠根據實際需要進行控制。
- <span style="color: #ff22dd; font-size:1.5em">它適合用於那些無法預測確切執行次數的情況。</span>
- 在 Python 中，**`while` 迴圈** 是另一種常見的迴圈形式，用於在某個條件為 `True` 時持續執行一段程式碼，直到條件變為 `False`。`

while` 迴圈在以下幾種情況下特別有用：

### 1. **處理不確定的重複次數**
當你無法確定操作需要執行多少次，但可以根據條件判斷是否繼續執行時，`while` 迴圈非常適合。例如，當你需要等候用戶輸入正確資料時，就可以使用 `while` 迴圈。

**範例**：重複要求輸入密碼，直到輸入正確的密碼為止
```python
password = ""
while password != "1234":
    password = input("請輸入密碼: ")
print("密碼正確，登入成功！")
```

### 2. **監測動態條件**
如果你需要根據程式運行中的動態條件來決定是否繼續操作，`while` 迴圈是一個非常靈活的選擇。例如，當感測器數據不符合要求時，持續檢查感測器的輸入。

**範例**：持續模擬溫度下降，直到溫度低於 20 為止
```python
temperature = 30
while temperature > 20:
    print("溫度太高，等待降溫中...")
    temperature -= 1  # 模擬溫度下降
print("溫度已經降到安全範圍")
```

### 3. **條件控制的持續監控**
當你需要在某個條件下持續執行任務，並且直到條件不滿足時才停止，`while` 迴圈是最有效的工具。例如，網頁伺服器需要持續等待客戶端的請求，這時可以使用 `while` 迴圈來保持伺服器運行。

**範例**：一直執行程式，直到用戶輸入 `quit` 才會結束
```python
running = True
while running:
    command = input("請輸入命令 (輸入 'quit' 來結束): ")
    if command == "quit":
        running = False
    else:
        print(f"執行命令: {command}")
```

### 4. **等待某個事件的發生**
`while` 迴圈可以用來等待某個事件或條件的發生，比如等待資料庫中的數據更新，或者等待網絡連接的建立。

**範例**：`while` 迴圈模擬等待網絡連接的過程，直到連接成功才退出迴圈
```python
connected = False
while not connected:
    print("等待網絡連接...")
    # 模擬網絡連接成功
    connected = True
print("已連接到網絡")
```

### 5. **無限迴圈與手動控制退出**
有時候你可能會需要一個無限迴圈，例如持續運行的伺服器程式或遊戲主迴圈，這時可以使用 `while True`，並根據條件來手動退出迴圈。

**範例**：程式會無限運行，直到用戶輸入 `exit` 來手動退出
```python
while True:
    command = input("請輸入命令 (輸入 'exit' 來結束): ")
    if command == "exit":
        break
    print(f"你輸入了: {command}")
```

### 6. **動態修改條件的情境**
當你需要根據某個值的變化來決定迴圈是否繼續時，`while` 迴圈可以根據變量的動態更新來控制流程。例如，在遊戲中玩家的生命值持續減少，直到歸零結束遊戲。

**範例**：隨著玩家的生命值變動來控制遊戲狀態，直到生命值為 0 才結束
```python
health = 100
while health > 0:
    damage = 10
    health -= damage
    print(f"玩家受到了 {damage} 點傷害，剩餘生命值: {health}")
print("遊戲結束，玩家死亡")
```

### 7. **與外部事件交互**
當程式需要持續等待外部設備或用戶輸入時，`while` 迴圈可以保持程式處於運行狀態，並根據外部的回饋做出相應處理。

**範例**：持續等待用戶的輸入，直到用戶按下 'q' 為止
```python
while True:
    user_input = input("按下 'q' 退出，或繼續輸入: ")
    if user_input == 'q':
        break
```
---
## continue and break

在 Python 的迴圈控制中，`continue` 和 `break` 是兩個非常重要的控制指令，用來控制迴圈的執行流程。這兩個指令可以讓你在特定情況下改變迴圈的正常執行順序：

### 1. **`break` 指令**
`break` 用於**立即結束整個迴圈**，無論迴圈的條件是否已經達成。一旦程式執行到 `break`，它會立刻跳出當前的迴圈，迴圈後的程式碼會繼續執行。

#### **使用情境**：
- 需要在特定條件滿足時提前終止迴圈。
- 在搜尋一個目標值時，一旦找到就停止迴圈。

**範例**：當 `i` 等於 5 時，`break` 會終止迴圈，所以不會輸出 5 之後的數字
```python
for i in range(1, 11):
    if i == 5:
        print("找到了，結束迴圈")
        break
    print(i)
```
輸出：
```
1
2
3
4
找到了，結束迴圈
```


### 2. **`continue` 指令**
`continue` 用於**跳過當前的這次迴圈**，並進入下一次的迴圈。當程式執行到 `continue`，它不會結束整個迴圈，而是立即跳過當前這次的後續程式碼，並回到迴圈的起點進行下一次的判斷或操作。

#### **使用情境**：
- 當不希望執行某些條件下的操作，但仍然希望保持迴圈運行。
- 跳過特定條件下的迴圈內容。

**範例**：當 `i` 等於 3 時，`continue` 會跳過當前的這次迴圈，因此 3 沒有被列印出來，但後續的迴圈還會繼續執行
```python
for i in range(1, 6):
    if i == 3:
        print("跳過 3")
        continue
    print(i)
```
輸出：
```
1
2
跳過 3
4
5
```

### `break` 和 `continue` 的比較：

- **`break`**：完全退出迴圈，不再執行剩餘的迴圈步驟。
- **`continue`**：跳過當前這次的迴圈步驟，直接進入下一次迴圈。

### 結合範例：
以下範例同時展示了 `break` 和 `continue` 的使用：

```python
for i in range(1, 11):
    if i == 3:
        print("跳過 3")
        continue
    if i == 7:
        print("找到 7，結束迴圈")
        break
    print(i)
```
輸出：
```
1
2
跳過 3
4
5
6
找到 7，結束迴圈
```
在這裡，當 `i` 為 3 時，`continue` 跳過了當次迴圈，沒有列印出 3。而當 `i` 為 7 時，`break` 結束了迴圈，導致 7 之後的數字不再被列印。

---
## 巢狀迴圈 (Nested loop)
在 Python 中，**巢狀迴圈**（Nested Loop）指的是在一個迴圈內嵌套另一個迴圈。這種結構允許程式在處理多維資料時，對每個層級的資料進行獨立操作。巢狀迴圈常用於處理列表、矩陣（多維列表）、表格或其他需要多層次疊代的情況。

### 巢狀迴圈的工作原理：
1. **外層迴圈**：先執行一遍，然後每當外層迴圈執行一次時，內層迴圈會完整執行一輪。
2. **內層迴圈**：每次外層迴圈進行一次疊代時，內層迴圈會重新開始，並執行多次疊代，直到條件不再滿足。

### 範例 1：巢狀 `for` 迴圈
```python
for i in range(1, 4):  # 外層迴圈
    for j in range(1, 4):  # 內層迴圈
        print(f"i={i}, j={j}")
```
輸出：
```
i=1, j=1
i=1, j=2
i=1, j=3
i=2, j=1
i=2, j=2
i=2, j=3
i=3, j=1
i=3, j=2
i=3, j=3
```
**解釋**：當外層迴圈 `i` 執行一次時，內層迴圈 `j` 會執行三次。這樣的結構在處理多層資料結構時非常有用。

### 什麼時候使用巢狀迴圈？

1. **處理多維資料結構**：當需要對多維資料（例如矩陣、表格）進行操作時，巢狀迴圈是最佳選擇。每一層迴圈可以處理不同的資料維度。
   
   **範例**：遍歷二維列表（矩陣）
   ```python
   matrix = [
       [1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]
   ]
   
   for row in matrix:  # 外層迴圈，處理每一列
       for num in row:  # 內層迴圈，處理每一列中的元素
           print(num, end=" ")
       print()  # 換行
   ```
   輸出：
   ```
   1 2 3 
   4 5 6 
   7 8 9 
   ```

2. **建立嵌套結構**：在建構複雜的多層結構時，巢狀迴圈可以幫助你根據不同條件或數據自動生成這樣的結構。

3. **雙重比對或配對操作**：例如，當你需要比較兩個列表中的每個元素時，巢狀迴圈能夠有效處理這樣的需求。

   **範例**：比對兩個列表中的元素是否相同
   ```python
   list1 = [1, 2, 3]
   list2 = [3, 2, 1]
   
   for a in list1:
       for b in list2:
           if a == b:
               print(f"{a} 和 {b} 相同")
   ```
   輸出：
   ```
   1 和 1 相同
   2 和 2 相同
   3 和 3 相同
   ```

4. **處理巢狀結構或樹狀結構**：在處理需要多層次遞歸的結構（如樹狀結構或巢狀資料結構）時，巢狀迴圈可以逐層深入資料結構進行處理。

### 巢狀迴圈的效能考慮
巢狀迴圈的運行時間隨著層級的增加而顯著增長。舉例來說，當有兩層迴圈時，時間複雜度通常是 O(n^2)，而三層迴圈則是 O(n^3)。因此，使用巢狀迴圈時要注意效能問題，尤其是在處理大量數據時，應謹慎使用過多層的巢狀迴圈。

### 範例 2：巢狀 `while` 迴圈
巢狀迴圈也可以用 `while` 來實現。例如：
```python
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1
```
這個範例的行為與範例 1 中的 `for` 迴圈相同。

### 總結：
巢狀迴圈在處理多維數據、表格、矩陣或進行多重比對時非常有用。它允許在每次外層迴圈執行時，內層迴圈可以進行多次操作，從而實現複雜的流程控制。不過，應避免過度使用過多層巢狀迴圈，以免影響程式效能。