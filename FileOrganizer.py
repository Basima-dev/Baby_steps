import os, shutil
from pathlib import Path
h = Path(r'C:/Users/obasi/Downloads')
# (h / 'fails').mkdir(exist_ok=True)
# (h / 'obasiVideos').mkdir(exist_ok=True)
# (h / 'obasiPhotos').mkdir(exist_ok=True)
for folderName, subfolders, filenames in os.walk(h / 'obasiFiles'):
    # for subfolder in subfolders:
    # for subfolder in subfolders:

    for files in filenames:
        if files.endswith('.MP4'):
            try:
                print(shutil.move(h / f'{folderName}/{files}', h / 'obasiVideos'))
            except Exception:
                print(f"Skipped: {files} already exists in destination.")
                

        elif files.endswith('.MOV'):
            try:
                print(shutil.move(h / f'{folderName}/{files}', h / 'obasiVideos'))
            except Exception:
                print(f"Skipped: {files} already exists in destination.")
                
            
        else:
            try:
                print(shutil.move(h / f'{folderName}/{files}', h / 'obasiPhotos'))
            except Exception:
                print(f"Skipped: {files} already exists in destination.")
print(' ')
print(' ')                
print("Files Sorting Complete!")
        












