import tkinter as tk
from main_function import Encrypt, Decrypt

# 定义双重加密和解密的函数
def double_encrypt(plain_text, key1, key2):
    cipher_text1 = Encrypt(plain_text, key1)
    cipher_text2 = Decrypt(cipher_text1, key2)
    return cipher_text2

def double_decrypt(cipher_text, key1, key2):
    plain_text1 = Encrypt(cipher_text, key2)
    plain_text2 = Decrypt(plain_text1, key1)
    return plain_text2

# 定义三重加密和解密的函数
def triple_encrypt(plain_text, key1, key2):
    cipher_text1 = Encrypt(plain_text, key1)
    cipher_text2 = Decrypt(cipher_text1, key2)
    cipher_text3 = Encrypt(cipher_text2, key1)
    return cipher_text3

def triple_decrypt(cipher_text, key1, key2):
    plain_text1 = Decrypt(cipher_text, key1)
    plain_text2 = Encrypt(plain_text1, key2)
    plain_text3 = Decrypt(plain_text2, key1)
    return plain_text3

# 双重加密的处理函数
def handle_double_encrypt():
    plain_text = plain_text_entry.get()
    key1 = key1_entry.get()
    key2 = key2_entry.get()
    result = double_encrypt(plain_text, key1, key2)
    result_label.config(text="加密结果: " + result)

# 双重解密的处理函数
def handle_double_decrypt():
    cipher_text = cipher_text_entry.get()
    key1 = key1_entry.get()
    key2 = key2_entry.get()
    result = double_decrypt(cipher_text, key1, key2)
    result_label.config(text="解密结果: " + result)

# 三重加密的处理函数
def handle_triple_encrypt():
    plain_text = plain_text_entry.get()
    key1 = key1_entry.get()
    key2 = key2_entry.get()
    result = triple_encrypt(plain_text, key1, key2)
    result_label.config(text="加密结果: " + result)

# 三重解密的处理函数
def handle_triple_decrypt():
    cipher_text = cipher_text_entry.get()
    key1 = key1_entry.get()
    key2 = key2_entry.get()
    result = triple_decrypt(cipher_text, key1, key2)
    result_label.config(text="解密结果: " + result)

# 创建主窗口
root = tk.Tk()
root.title("加密和解密界面")

# 输入框和标签
tk.Label(root, text="明文:").grid(row=0, column=0, sticky="w")
plain_text_entry = tk.Entry(root, width=30)
plain_text_entry.grid(row=0, column=1)

tk.Label(root, text="密文:").grid(row=1, column=0, sticky="w")
cipher_text_entry = tk.Entry(root, width=30)
cipher_text_entry.grid(row=1, column=1)

tk.Label(root, text="密钥1:").grid(row=2, column=0, sticky="w")
key1_entry = tk.Entry(root, width=30)
key1_entry.grid(row=2, column=1)

tk.Label(root, text="密钥2:").grid(row=3, column=0, sticky="w")
key2_entry = tk.Entry(root, width=30)
key2_entry.grid(row=3, column=1)

# 加密和解密按钮
tk.Button(root, text="双重加密", command=handle_double_encrypt).grid(row=4, column=0)
tk.Button(root, text="双重解密", command=handle_double_decrypt).grid(row=4, column=1)

tk.Button(root, text="三重加密", command=handle_triple_encrypt).grid(row=5, column=0)
tk.Button(root, text="三重解密", command=handle_triple_decrypt).grid(row=5, column=1)

# 结果显示标签
result_label = tk.Label(root, text="结果将在这里显示")
result_label.grid(row=6, column=0, columnspan=2)

# 运行主循环
root.mainloop()
