import os, shutil
from pathlib import Path

p = Path(r'C:/Users/obasi/Downloads')
# (p / 'trialshi').mkdir(exist_ok=True)
# (p / 'trialpee').mkdir(exist_ok=True)
# (p / 'trialfail').mkdir(exist_ok=True)
video = ('.MOV', '.MP4')

for folder, subfolders, filenames in os.walk(p / 'obasiFiles'):
    
    # for files in filenames:
    #     if files.endswith(video):
    #         try:
    #             print(shutil.move(p / f"{folder}/{files}", p / 'trialshi'))
    #         except Exception:
    #             print('File already exists in destination')
    #             response = input('Enter D~(delete) or S~(skip)>')
    #             if response == 'D':
    #                 os.unlink(f"{folder}//{files}")
    #                 print(f'Deleting {files}')
    #             else:
    #                 print(f'Ok...skipping {files} ')
    #                 continue

    #     if files.endswith('.AAE'):
    #         try:
    #             print(shutil.move(p / f"{folder}/{files}", p / 'trialfail'))
    #         except Exception:
    #             print('File already exists in destination')
    #             response = input('Enter D~(delete) or S~(skip)')
    #             if response == 'D':
    #                 os.unlink(f"{folder}//{files}")
    #                 print(f'Deleting {files}')
    #             else:
    #                 print(f'Ok...skipping {files} ')
    #                 continue
    #     else:
    #         try:
    #             print(shutil.move(p / f"{folder}/{files}", p / 'trialpee'))
    #         except Exception:
    #             print('File already exists in destination')
    #             response = input('Enter D~(delete) or S~(skip)')
    #             if response == 'D':
    #                 os.unlink(f"{folder}//{files}")
    #                 print(f'Deleting {files}')
    #             else:
    #                 print(f'Ok...skipping {files} ')
    #                 continue

        for subfolder in subfolders:
            try:
                print((p / f'{subfolder}').rmdir(exist_ok=True))
            except Exception:
                print(f"Folder: {subfolder} is not empty")



                
print('')
print('File sorting complete!!')