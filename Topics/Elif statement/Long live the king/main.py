edge = [1, 8]

col_num = int(input())
row_num = int(input())

if col_num in edge and row_num in edge:
    print("3")
elif col_num in edge or row_num in edge:
    print("5")
else:
    print("8")
