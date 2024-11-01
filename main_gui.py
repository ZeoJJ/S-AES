import tkinter as tk
from ascii_function import *
from main_function import *

window = tk.Tk()
window.title('S-AES')

# 设置窗口尺寸
window.geometry('800x200')

# 二进制加解密部分
binary_frame = tk.LabelFrame(window, text='二进制加解密')
binary_frame.pack(pady=10)

# 明文(密文)输入
binary_input_label = tk.Label(binary_frame, text='明文(密文)')
binary_input_label.pack(side=tk.LEFT)
binary_input_entry = tk.Entry(binary_frame)
binary_input_entry.pack(side=tk.LEFT)

# 密钥输入
binary_key_label = tk.Label(binary_frame, text='密钥')
binary_key_label.pack(side=tk.LEFT)
binary_key_entry = tk.Entry(binary_frame)
binary_key_entry.pack(side=tk.LEFT)

# 输出部分
binary_output_label = tk.Label(binary_frame, text='输出')
binary_output_label.pack(side=tk.LEFT)

binary_output_entry = tk.Entry(binary_frame)
binary_output_entry.pack(side=tk.LEFT)

# 加密解密按钮
binary_button_frame = tk.Frame(binary_frame)
binary_button_frame.pack(side=tk.TOP)

# 加密功能
def binary_encrypt():
    binary_output_entry.delete(0, tk.END)
    binary_output_entry.insert(0, Encrypt(binary_input_entry.get(), binary_key_entry.get()))

# 解密功能
def binary_decrypt():
    binary_output_entry.delete(0, tk.END)
    binary_output_entry.insert(0, Decrypt(binary_input_entry.get(), binary_key_entry.get()))

binary_encrypt_button = tk.Button(binary_button_frame, text='加密', command=binary_encrypt)
binary_encrypt_button.pack(side=tk.LEFT)

binary_decrypt_button = tk.Button(binary_button_frame, text='解密', command=binary_decrypt)
binary_decrypt_button.pack(side=tk.LEFT)


# 字符加解密部分
text_frame = tk.LabelFrame(window, text='字符加解密')
text_frame.pack(pady=10)

# 明文(密文)输入
text_input_label = tk.Label(text_frame, text='明文(密文)')
text_input_label.pack(side=tk.LEFT)
text_input_entry = tk.Entry(text_frame)
text_input_entry.pack(side=tk.LEFT)

# 密钥输入
text_key_label = tk.Label(text_frame, text='密钥')
text_key_label.pack(side=tk.LEFT)
text_key_entry = tk.Entry(text_frame)
text_key_entry.pack(side=tk.LEFT)

# 输出部分
text_output_label = tk.Label(text_frame, text='输出')
text_output_label.pack(side=tk.LEFT)

text_output_entry = tk.Entry(text_frame)
text_output_entry.pack(side=tk.LEFT)

# 加密解密按钮
text_button_frame = tk.Frame(text_frame)
text_button_frame.pack(side=tk.TOP)

# 加密功能
def text_encrypt():
    text_output_entry.delete(0, tk.END)
    cipher_text = ascii_encrypt(text_input_entry.get(), text_key_entry.get())
    text_output_entry.insert(0, cipher_text)

# 解密功能
def text_decrypt():
    text_output_entry.delete(0, tk.END)
    decrypted_text = ascii_decrypt(text_input_entry.get(), text_key_entry.get())
    text_output_entry.insert(0, decrypted_text)

text_encrypt_button = tk.Button(text_button_frame, text='加密', command=text_encrypt)
text_encrypt_button.pack(side=tk.LEFT)

text_decrypt_button = tk.Button(text_button_frame, text='解密', command=text_decrypt)
text_decrypt_button.pack(side=tk.LEFT)



# 运行界面
window.mainloop()
