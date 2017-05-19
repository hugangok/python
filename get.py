import cgi, cgitb 

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 

# 获取数据
site_name = form.getvalue('name')
site_url  = form.getvalue('url')
print ("")
print (site_name, site_url)
print ("</body>")
print ("</html>")
