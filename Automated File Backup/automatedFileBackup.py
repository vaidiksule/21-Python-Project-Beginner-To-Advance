import os
import shutil
import datetime
import schedule
import time

source_dir = os.path.expanduser('~/Downloads/Images')
destination_dir = os.path.expanduser('~/Downloads/Backup')

def copy_folder_to_directory(sorce, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source_dir, dest_dir)
        print(f"Folder copies to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

# copy_folder_to_directory(source_dir, destination_dir)
schedule.every().day.at("01:01").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)