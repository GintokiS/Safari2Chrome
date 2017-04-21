# Safari2Chrome 
# v0.1
Get URLs from Safari read list, then create Chrome bookmark html file.

## Enviroment
- Pyhton 3.6.1 (install by brew, default)

## How to use
1. In Finder, press CMD + Shift + G, copy the path `/Users/yourusername/Library/Safari`，*yourusername* must use your Mac's username and press enter.
2. copy `Bookmarks.plist` to a folder.
3. Open Terminal, `cd` to the folder in Step2. Input `python3 safari2chrome.py`, press enter
4. In the folder, there is a new html file, open Chrome and import it.
