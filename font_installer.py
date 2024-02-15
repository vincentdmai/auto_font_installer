import os
import shutil
import subprocess

from fontTools.ttLib import TTFont

def install_font(font_path):
    try:
        font = TTFont(font_path)
        font_name = font['name'].getName(4, 3, 1, 1033).toUnicode()
        shutil.copy(font_path, os.path.join(font_dir, font_name + os.path.splitext(font_path)[1]))
        print(f"Installed font: {font_name}")
    except Exception as e:
        print(f"Failed to install font '{font_path}': {e}")

def install_fonts_from_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.otf', '.ttf')):
                font_path = os.path.join(root, file)
                install_font(font_path)

if __name__ == "__main__":
    font_dir = input("Enter the directory path containing font files: ").strip()
    if not os.path.isdir(font_dir):
        print("Invalid directory.")
        exit(1)

    install_fonts_from_directory(font_dir)
    # Update font cache
    try:
        subprocess.run(['fc-cache', '-f', '-v'], check=True)
        print("Font cache updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error updating font cache: {e}")
    
    print("Font installation complete.")
