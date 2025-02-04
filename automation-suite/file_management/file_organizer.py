import os
import shutil
from pathlib import Path
from datetime import datetime

def organize_files(source_dir: str, organize_by: str = 'type') -> None:
    """
    Organize files by type (extension) or date
    """
    source = Path(source_dir)
    if not source.exists():
        raise FileNotFoundError(f"Directory {source_dir} not found")

    for item in source.iterdir():
        if item.is_file():
            if organize_by == 'type':
                dest_dir = source / (item.suffix[1:] if item.suffix else 'Other')
            elif organize_by == 'date':
                mtime = item.stat().st_mtime
                date_str = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
                dest_dir = source / date_str
            else:
                raise ValueError("Invalid organization type. Use 'type' or 'date'")
            
            dest_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(dest_dir / item.name))

def organize_files_by_date(path: str):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            timestamp = os.path.getmtime(os.path.join(path, file))
            date = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
            # ... rest of the code ...

if __name__ == "__main__":
    import sys
    organize_files(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else 'type') 