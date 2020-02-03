from selenium import webdriver

# 使用Chrome驱动
browser = webdriver.Chrome()

url = 'https:www.baidu.com'
browser.get(url)    # 打开浏览器预设网址
print(browser.page_source)  # 打印网页源代码
browser.close()  # 关闭浏览器

# 界面下滑
browser.execute_script('window.scrollBy(0,1000)')
# scrollBy(x,y)中，x表示向右滚动的像素值；y表示向下滚动的像素值

# 跳界面
browser.execute_script('window.scrollTo(0,1000)')
# scrollTo(x,y) 中，x表示要在窗口文档显示区左上角显示的文档的x坐标；y表示要在窗口文档显示区左上角显示的文档的y坐标

# 一拉到底（适合到底端才加载的界面）
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")