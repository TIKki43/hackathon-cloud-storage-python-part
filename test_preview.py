# from preview_generator.manager import PreviewManager
from PyPreviewGenerator.manager import PreviewManager
import os
import zipfile


fantasy_zip = zipfile.ZipFile('C:\\projects\\hac2\\img\\file.zip', 'w')
for folder, subfolders, files in os.walk('C:\\projects\\hac2\\img'):
    for file in files:
        if True:
            fantasy_zip.write(os.path.join(folder, file),
                              os.path.relpath(os.path.join(folder, file), 'C:\\projects\\hac2\\img'),
                              compress_type=zipfile.ZIP_DEFLATED)

fantasy_zip.close()
