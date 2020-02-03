

# wb为二进制写入
with open("文件名", "wb") as f:
    f.write("二进制文件")
# 追加
with open("文件名", "a+") as f:
    f.write("str文件")

# 清空写入
with open("文件名", "w") as f:
    f.write("str文件")
