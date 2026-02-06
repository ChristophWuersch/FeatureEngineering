#!/usr/bin/env python3
"""
Script to generate README.md with all images from the ./images directory
"""
import os
from pathlib import Path

def generate_readme():
    # Define image extensions to look for
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.bmp', '.webp'}
    
    # Get all image files from ./images directory
    images_dir = Path('./images')
    image_files = []
    
    if images_dir.exists() and images_dir.is_dir():
        for file in sorted(images_dir.iterdir()):
            if file.is_file() and file.suffix.lower() in image_extensions:
                image_files.append(file)
    
    # Generate README content
    readme_content = """# FeatureEngineering

Repository for data and images for colab

## Images

This section displays all images stored in the `./images` directory.

"""
    
    if image_files:
        for img_file in image_files:
            # Get relative path from repository root
            rel_path = img_file.relative_to('.')
            # Create markdown image entry
            img_name = img_file.stem.replace('_', ' ').replace('-', ' ').title()
            readme_content += f"### {img_name}\n\n"
            readme_content += f"![{img_name}]({rel_path})\n\n"
    else:
        readme_content += "*No images found. Add images to the `./images` directory and run `python3 generate_readme.py` to update this README.*\n"
    
    # Write README file
    with open('README.md', 'w') as f:
        f.write(readme_content)
    
    print(f"✅ README.md generated successfully!")
    print(f"   Found {len(image_files)} image(s)")
    if image_files:
        for img in image_files:
            print(f"   - {img.name}")

if __name__ == '__main__':
    generate_readme()
