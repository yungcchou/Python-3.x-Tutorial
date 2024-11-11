def factorial(n): # 定義階乘函數
    # 基礎情況：當 n 為 0 時，返回 1
    if n == 0:
        return 1
    # 遞迴情況：n 乘以 (n-1) 的階乘
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    print(factorial(5))  # 輸出：120

