# Safari2Chrome 
# v0.1
Get URLs from Safari read list, then create Chrome bookmark html file.

## My Enviroment
- Pyhton 3.6.1 (install by Homebrew, default)
- Mac 10.11.6
- Safari 10.0.1(11602.2.14.0.7)
- Chrome 57.0.2987.133 (64-bit)

## How to use
1. In Finder, press CMD + Shift + G, copy the path `/Users/yourusername/Library/Safari`，*yourusername* must use your Mac's username and press enter.
2. copy `Bookmarks.plist` to a folder.
3. Open Terminal, `cd` to the folder in Step2. Input `python3 safari2chrome.py`, press enter
4. In the folder, there is a new html file, open Chrome and import it. 



# Safari2Chrome 
# v0.1
找到 Safari 的“阅读列表”的 URL 和标题，将 URL 和 标题导入到 Chrome

## 我的环境：
- Mac 10.11.6
- Safari 10.0.1(11602.2.14.0.7)
- Chrome 57.0.2987.133 (64-bit)
- Python 3.6.1 (使用 Homebrew 默认安装)

## 用法：
1. 把 plist 文件复制到一个文件夹
2. 打开终端，cd 到那个文件夹
3. 在终端输入`python3 safari2chrome.py `来运行脚本
4. 脚本运行完会在当前目录生成个 html 文件，导入到 Chrome 齐活
