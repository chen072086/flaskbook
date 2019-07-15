#@project:checkDomain
#@author:chenliangfu
#@file:myfile.py
#@time:2018-7-6  15:00:00
#@Description:XX

# 导入 base64模块
# import base64
# # 给定需要转换的字符串
# str1 = ""
#
# # 需要转成2进制格式才可以转换，所以我们这里再手动转换一下
# result = base64.b64encode(str(str1))
# # # 打印转换后的结果
# print(result)
# 再把加密后的结果解码
# temp = base64.b64decode(str1.encode())
# print(temp)
# 同样的，解码后的结0果是二进制，我们再转换一下
#print('解密后的结果 --> '+temp.decode())

#
#
# x = b"ShJ9s7QWHJCVYhPPz5ijfQ=="  # bytes object
# s = "ShJ9s7QWHJCVYhPPz5ijfQ=="   # str object
#
# print('str --> bytes')
# print(bytes(s, encoding="gbk"))
# print(str.encode(s))   # 默认 encoding="utf-8"
# print(s.encode())      # 默认 encoding="utf-8"
# print(bytearray(x.encode('utf-8')))
#
# print('\nbytes --> str')
# print(str(b, encoding="utf-8"))
# print(bytes.decode(x))  # 默认 encoding="utf-8"
# print(b.decode())       # 默认 encoding="utf-8"


#import binascii

# 一个字符串
x = "ShJ9s7QWHJCVYhPPz5ijfQ=="
# 字符串变字符型字节流
#bin(int(s,16))
# oct(int(x, 10))
print(bytearray(x.encode('utf-8')))
import  base64
s1 = base64.encodestring(b'4A-12-7D-B3-B4-16-1C-90-95-62-13-CF-CF-98-A3-7D')
s2 = base64.decodestring(s1)
print (s1)