import tkinter as tk
from main_function import Encrypt, Decrypt, XOR

# 实现 CBC 加密模式
def CBC_encrypt(plain_text, key, IV):
    # 将明文分组
    plain_text_list = [plain_text[i:i + 16] for i in range(0, len(plain_text), 16)]
    # 存储密文
    cipher_text_list = []
    # 对每个分组进行加密
    for block in plain_text_list:
        cipher_block = Encrypt(XOR(block, IV), key)
        IV = cipher_block  # 更新 IV
        cipher_text_list.append(cipher_block)
    return ''.join(cipher_text_list)

# 实现 CBC 解密模式
def CBC_decrypt(cipher_text, key, IV):
    # 将密文分组
    cipher_text_list = [cipher_text[i:i + 16] for i in range(0, len(cipher_text), 16)]
    # 存储明文
    plain_text_list = []
    # 对每个分组进行解密
    for block in cipher_text_list:
        plain_block = XOR(Decrypt(block, key), IV)
        IV = block  # 更新 IV
        plain_text_list.append(plain_block)
    return ''.join(plain_text_list)

# 处理加密的函数
def handle_encrypt():
    plain_text = plain_text_entry.get()
    key = key_entry.get()
    IV = iv_entry.get()
    cipher_text = CBC_encrypt(plain_text, key, IV)
    result_label.config(text="加密密文: " + cipher_text)
    decrypted_text = CBC_decrypt(cipher_text, key, IV)
    if decrypted_text == plain_text:
        verify_label.config(text="解密验证成功: " + decrypted_text)
    else:
        verify_label.config(text="解密验证失败")

# 处理解密的函数
def handle_decrypt():
    cipher_text = cipher_text_entry.get()
    key = key_entry.get()
    IV = iv_entry.get()
    plain_text = CBC_decrypt(cipher_text, key, IV)
    result_label.config(text="解密明文: " + plain_text)

# 创建主窗口
root = tk.Tk()
root.title("CBC 加密/解密模式")

# 明文输入框
tk.Label(root, text="明文:").grid(row=0, column=0, sticky="w")
plain_text_entry = tk.Entry(root, width=30)
plain_text_entry.grid(row=0, column=1)

# 密钥输入框
tk.Label(root, text="密钥:").grid(row=1, column=0, sticky="w")
key_entry = tk.Entry(root, width=30)
key_entry.grid(row=1, column=1)

# 初始向量输入框
tk.Label(root, text="初始向量 (IV):").grid(row=2, column=0, sticky="w")
iv_entry = tk.Entry(root, width=30)
iv_entry.grid(row=2, column=1)

# 密文输入框
tk.Label(root, text="密文:").grid(row=3, column=0, sticky="w")
cipher_text_entry = tk.Entry(root, width=30)
cipher_text_entry.grid(row=3, column=1)

# 加密和解密按钮
tk.Button(root, text="加密", command=handle_encrypt).grid(row=4, column=0)
tk.Button(root, text="解密", command=handle_decrypt).grid(row=4, column=1)

# 结果显示标签
result_label = tk.Label(root, text="结果将在这里显示")
result_label.grid(row=5, column=0, columnspan=2)

# 验证显示标签
verify_label = tk.Label(root, text="")
verify_label.grid(row=6, column=0, columnspan=2)

# 运行主循环
root.mainloop()
