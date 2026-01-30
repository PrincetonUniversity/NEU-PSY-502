import yaml
import os
from pathlib import Path

def check_toc_files(toc_path="website/_toc.yml", base_dir="website"):
    """Check if all files referenced in _toc.yml exist."""
    
    with open(toc_path, 'r') as f:
        toc = yaml.safe_load(f)
    
    missing_files = []
    found_files = []
    
    def check_file(file_path):
        """Check if a file exists with .md or .ipynb extension."""
        full_path_md = os.path.join(base_dir, f"{file_path}.md")
        full_path_ipynb = os.path.join(base_dir, f"{file_path}.ipynb")
        
        if os.path.exists(full_path_md):
            found_files.append(f"{file_path}.md")
            return True
        elif os.path.exists(full_path_ipynb):
            found_files.append(f"{file_path}.ipynb")
            return True
        else:
            missing_files.append(file_path)
            return False
    
    def process_items(items):
        """Recursively process TOC items."""
        if not items:
            return
        
        for item in items:
            if isinstance(item, dict):
                # Check if this item has a 'file' key
                if 'file' in item:
                    check_file(item['file'])
                
                # Check for chapters/sections recursively
                if 'chapters' in item:
                    process_items(item['chapters'])
                if 'sections' in item:
                    process_items(item['sections'])
    
    # Check root file
    if 'root' in toc:
        check_file(toc['root'])
    
    # Process parts
    if 'parts' in toc:
        for part in toc['parts']:
            if 'chapters' in part:
                process_items(part['chapters'])
    
    # Process chapters (if not in parts)
    if 'chapters' in toc:
        process_items(toc['chapters'])
    
    # Print results
    print(f"{'='*60}")
    print(f"TOC File Check Results")
    print(f"{'='*60}")
    
    if found_files:
        print(f"\n✓ Found {len(found_files)} files:")
        for f in found_files:
            print(f"  ✓ {f}")
    
    if missing_files:
        print(f"\n✗ Missing {len(missing_files)} files:")
        for f in missing_files:
            print(f"  ✗ {f}")

if __name__ == "__main__":
    print("Starting TOC file check...")
    all_exist = check_toc_files()
    exit(0 if all_exist else 1)