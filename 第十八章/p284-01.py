import re
my_str = """<img alt="⼩浅⽉o的直播" data-original="https://rpic.douyucdn.cn/livecover/appCovers/2018/03/25/3544712_20180325111300_big.jpg"
src="https://rpic.douyucdn.cn/livecover/appCovers/2018/03/25/3544712_20180325111300_big.jpg"
width="283"
height="163" class="JS_listthumb" style="display: block;">"""
# python⾥⾯正则表达式默认是贪婪的， 尽量根据正则表达式多匹配数据
# 设置成为⾮贪婪， ⾮贪婪就是根据正则表达式尽量少匹配数据
# ⾮贪婪的样式: *? +? ??
# ⾮贪婪的含义:?后⾯的数据不要前⾯去匹配，让?后⾯匹配
match_obj = re.search(r"https?://.*?\.jpg", my_str)
if match_obj:
 # 获取匹配结果数据
 print(match_obj.group())
else:
 print("匹配失败")