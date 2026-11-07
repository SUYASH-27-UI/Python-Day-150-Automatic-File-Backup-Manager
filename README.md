# Python-Day-150-Automatic-File-Backup-Manager
# Python Day 150 – Automatic File Backup Manager

## Description
A Python application that automatically creates backups of files and generates compressed ZIP archives.

## Features
- Scans source folders.
- Copies files while preserving their metadata.
- Creates timestamped backup folders.
- Generates ZIP backup archives.
- Supports nested directories.

## Files
- `backup_manager.py` – Main Python program.
- `source_files/` – Folder containing original files.
- `backups/` – Generated backup folders and ZIP files.

## How to Run
```bash
python backup_manager.py
```

## Concepts Used
- pathlib
- shutil
- zipfile
- File Handling
- Exception Handling
- Date and Time

## Note
This project is for educational purposes. Keep an additional backup of important real-world data.
