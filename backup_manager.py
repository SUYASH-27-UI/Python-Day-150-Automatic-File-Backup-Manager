import shutil
import zipfile
from pathlib import Path
from datetime import datetime

SOURCE = Path("source_files")
BACKUP = Path("backups")


def create_backup():

    if not SOURCE.exists():
        print("Source folder not found!")
        return

    files = [f for f in SOURCE.rglob("*") if f.is_file()]

    if not files:
        print("No files available for backup!")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_folder = BACKUP / f"backup_{timestamp}"
    backup_folder.mkdir(parents=True)

    zip_path = BACKUP / f"backup_{timestamp}.zip"

    try:
        # Copy files into backup folder
        for file in files:
            relative_path = file.relative_to(SOURCE)
            destination = backup_folder / relative_path

            destination.parent.mkdir(
                parents=True, exist_ok=True
            )

            shutil.copy2(file, destination)

        # Create ZIP backup
        with zipfile.ZipFile(
            zip_path, "w", zipfile.ZIP_DEFLATED
        ) as zip_file:

            for file in backup_folder.rglob("*"):
                if file.is_file():
                    zip_file.write(
                        file,
                        file.relative_to(backup_folder)
                    )

        print("\n===== BACKUP REPORT =====")
        print("Files Backed Up:", len(files))
        print("Backup Folder:", backup_folder)
        print("ZIP File:", zip_path)
        print("Backup completed successfully!")

    except OSError as error:
        print("Backup failed:", error)


create_backup()
