from collections import defaultdict
import shutil
from pathlib import Path
import argparse


def copy_file(root_address, dist='dist'):
    extensions = defaultdict(list)
    dist = Path(dist)

    try:
        for file in root_address.iterdir():
            if file.is_dir():
                copy_file(file, dist)
                continue

            extensions[file.suffix].append(file)

        for ext, files in extensions.items():
            directory = dist / ext
            directory.mkdir(parents=True, exist_ok=True)
            for file in files:
                shutil.copy(file, directory / file.name)
    except FileNotFoundError as e:
        print(f"Error: {e}. File or directory not found: {root_address}")
    except PermissionError as e:
        print(f"Error: {e}. Permission denied: {root_address}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Copy files to a destination directory, organized by file extension.")
    parser.add_argument("source", type=str, help="Path to the source directory")
    parser.add_argument("destination", type=str, nargs='?', default='dist', help="Path to the destination directory (default: 'dist')")
    
    args = parser.parse_args()
    
    source_path = Path(args.source)
    destination_path = Path(args.destination)
    
    copy_file(source_path, destination_path)
