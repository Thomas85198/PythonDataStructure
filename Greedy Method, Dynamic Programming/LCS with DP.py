x = "ATTTGGCTA"
y = "TTAGCCAT"
table1 = None
table2 = None
result = ""


def LCS(str1, str2):
    global table1, table2
    m = len(str1)
    n = len(str2)
    table1 = []
    table2 = []

    # 初始化 table1
    for i in range(m + 1):
        table1.append([])
        table1[i].append(0)  # 設置第一列為 0
        for k in range(1, n + 1):
            table1[i].append(None)

    # 設置第一行為 0
    for j in range(1, n + 1):
        table1[0][j] = 0

    # 初始化 table2
    for i in range(m + 1):
        table2.append([])
        for k in range(n + 1):
            table2[i].append(None)

    # 計算最長公共子序列
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                table1[i][j] = 1 + table1[i - 1][j - 1]
                table2[i][j] = "↖"
            elif table1[i - 1][j] >= table1[i][j - 1]:
                table1[i][j] = table1[i - 1][j]
                table2[i][j] = "↑"
            else:
                table1[i][j] = table1[i][j - 1]
                table2[i][j] = "←"


def printLCS(i, j):
    global result
    if i == 0 or j == 0:
        return

    if table2[i][j] == "↖":
        printLCS(i - 1, j - 1)
        result += x[i - 1]
    elif table2[i][j] == "↑":
        printLCS(i - 1, j)
    else:
        printLCS(i, j - 1)


# 執行 LCS 算法
LCS(x, y)
printLCS(len(x), len(y))
print(result)
