import os
import zipfile

path_to = r'C:\projects\hac2\test_tar.py'
def inf_obj(self, path_to, path_review_to):
    dict = {}
    try:
        dict['ext'] = path_to.split('.')[1]
    except:
        dict['ext'] = 'It is a dir'
    dict['size'] = os.path.getsize(path_to)
    path1 = path_to.split('\\')
    try:
        dict['name'] = path1[-1].split('.')[0]
    except:
        dict['name'] = path1[-1]
    dict['preview'] = get_preview_path(path_review_to)
    dict['user'] = path_to.split('\\')[1]
    dict1 = dict
    dict.clear()
    return dict1
print(dict)