def get_content(fileName):
    '''根据文件名获取文件内容'''
    extend_name=fileName.split('.')[-1]
    if extend_name=='html' or extend_name=='htm':
        return r'text/html'
    elif extend_name=='jpg' or extend_name=='gif':
        return r'image/jpeg'
    elif extend_name=='png':
        return r'image/png'
    else:
        raise exception('Unknown Error')
    


print('test begin...')
files=['a.html','b.gif']
for item in files:
    print(get_content(item))
    
print('test end')