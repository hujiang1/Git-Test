import urllib
import os
import random
def save_url_content(url,folder_path=None):
	try:
		d = urllib.urlopen(url)
	except Exception as e:
		print(e)
		raise u'该网页无法打开'	
	else:
		content = d.read()
		if not os.path.isdir(folder_path):
			return u'folder_path非文件夹'
		rand_filename = random.randint(1,1000)
		# file_path = '%s/%s'%(folder_path,rand_filename)
		file_path = os.path.join(folder_path,rand_filename)
		d = open(file_path,'w')
		d.write(content)
		d.close()
		return file_path


save_url_content('https://www.baidu.com,'tmp')