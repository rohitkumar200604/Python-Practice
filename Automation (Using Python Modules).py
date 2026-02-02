# Copy notes.txt to notes_backup.txt.
import shutil
shutil.copy("notes.txt","notes_backup.txt")

# Rename temp.txt to final.txt.
import os
os.rename("temp.txt","final.txt")

# Ask user for a filename and copy it to a backup folder.
file = input("Enter filename to be copied with extension: ")
import shutil
shutil.copy(file, f"backup_{file}")