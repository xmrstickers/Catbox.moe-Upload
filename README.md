# Catbox.moe-Upload
simple file-upload to free file-upload platform Catbox.moe
# Usage: 
assuming _file.txt_ is in the same directory as _catbox.py_

**single-file upload**:
```
catbox.py file.txt 
```
**Successful Output**:

![image](https://user-images.githubusercontent.com/89484281/211171298-2e39f6a3-69b2-477f-a667-875044e2b0b4.png)
# Why? 
I like to share files with strangers on the internet. This website will temporarily host files up to 200 megs and provide a link to your file. 
Using this on my desktop workstation is fast and easy in the browser, but I wanted to be able to share files from CLI or other scripts on the same platform. So I made this tool! 

# What file types aren't allowed?
The following file types are currently not allowed: **.exe, .scr, .cpl, .doc*, .jar**

This a server-side check and completely out of my control (*ahem*, just compress them first)

# Why can't I upload multiple files at once >:(
eagerly awaiting your PR, king :) 
