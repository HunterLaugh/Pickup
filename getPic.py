# coding:utf-8

import requests
import re

# 要下载的图片数
picNumber=30

# 搜索的关键词
key="sex long leg"

# 网址URL
url="http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="+key+"&v=flip"


def getPicUrl():
	# url内容获取
	html=requests.get(url)
	
	# 解悉，正则 获取.jpg url
	htmlTxt=html.text
	pic_url=re.findall('"objURL":"(.*?)",',htmlTxt,re.S)
	#返回 .jpg url
	return pic_url

	
def downloadPic():
	picUrl=getPicUrl()
	
	i=1
	for each in picUrl :
		try:
			pic=requests.get(each,timeout=10)
		except requests.exceptions.ConnectionError:
			print("[错误] can't download this picture")
			continue
		string='girls/'+key+str(i)+'.jpg'
		fp=open(string,'wb')
		fp.write(pic.content)
		fp.close()
		print("Download  picture",i)
		
		i+=1
		
		if i>picNumber:
			break
	

# 开始运行
downloadPic()
