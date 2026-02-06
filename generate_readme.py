#!/usr/bin/env python3
"""
Script to generate README.md with all images from the ./images directory
"""
import os
import sys
import argparse
from pathlib import Path

def generate_readme(images_dir='./images', preserve_header=True):
    # Define image extensions to look for
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.bmp', '.webp'}
    
    # Get all image files from images directory
    images_path = Path(images_dir)
    image_files = []
    
    if images_path.exists() and images_path.is_dir():
        for file in sorted(images_path.iterdir()):
            if file.is_file() and file.suffix.lower() in image_extensions:
                image_files.append(file)
    
    # Try to preserve existing README header if requested
    readme_header = """# FeatureEngineering

Repository for data and images for colab"""
    
    if preserve_header and Path('README.md').exists():
        try:
            with open('README.md', 'r') as f:
                content = f.read()
                # Extract content before ## Images section
                if '## Images' in content:
                    readme_header = content.split('## Images')[0].rstrip()
        except Exception:
            pass  # Use default header if reading fails
    
    # Generate README content
    readme_content = f"""{readme_header}

## Images

This section displays all images stored in the `{images_dir}` directory.

> **Note**: To update this README with new images, run: `python3 generate_readme.py`

"""
    
    if image_files:
        for img_file in image_files:
            # Get relative path from repository root
            rel_path = img_file
            # Create markdown image entry
            img_name = img_file.stem.replace('_', ' ').replace('-', ' ').title()
            readme_content += f"### {img_name}\n\n"
            readme_content += f"![{img_name}]({rel_path})\n\n"
    else:
        readme_content += f"*No images found. Add images to the `{images_dir}` directory and run `python3 generate_readme.py` to update this README.*\n"
    
    # Write README file
    with open('README.md', 'w') as f:
        f.write(readme_content)
    
    print(f"✅ README.md generated successfully!")
    print(f"   Found {len(image_files)} image(s)")
    if image_files:
        for img in image_files:
            print(f"   - {img.name}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate README.md with images from a directory')
    parser.add_argument('--images-dir', default='./images', help='Directory containing images (default: ./images)')
    parser.add_argument('--no-preserve-header', action='store_true', help='Do not preserve existing README header')
    
    args = parser.parse_args()
    generate_readme(images_dir=args.images_dir, preserve_header=not args.no_preserve_header)
