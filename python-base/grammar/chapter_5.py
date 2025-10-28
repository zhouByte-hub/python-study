## File 文件
import os

##  始代码使用相对路径 "files/text.txt" ，这依赖于当前工作目录
##  工作目录不一致 ：如果你在不同的目录下运行脚本，相对路径就会失效
try:
    # 使用绝对路径，避免工作目录问题
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "files", "text.txt")
    
    # 使用with语句自动管理文件资源，更安全
    # r: 只读模式，默认值
    # w: 写入模式，会覆盖文件内容
    # a: 追加模式，不会覆盖文件内容
    # r+: 读写模式，文件指针在开头
    # w+: 读写模式，文件指针在开头，会覆盖文件内容
    # a+: 读写模式，文件指针在末尾，不会覆盖文件内容
    with open(file_path, "r", encoding="utf-8") as file: 
        print(file.read())
except Exception as e:
    print("文件打开失败", e)
