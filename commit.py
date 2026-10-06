import sys
import subprocess

# --- AUTOMATIC DEPENDENCY INSTALLATION ---
def install_dependencies():
    try:
        import playwright
    except ImportError:
        print("Required dependencies missing. Installing 'playwright'...")
        subprocess.run([sys.executable, "-m", "pip", "install", "playwright"], check=True)
        print("Installing browser binaries...")
        subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
        print("Setup complete! Running automation...\n")

install_dependencies()
# ----------------------------------------

import asyncio
import os
import shutil
import zipfile
from playwright.async_api import async_playwright

# --- CONFIGURATION ---
PROJECT_URL = "https://onecompiler.com/python/4558rhwnw"
REPO_DIR = os.getcwd()  
SCRIPT_NAME = os.path.basename(__file__)  
COMMIT_MESSAGE = "Auto-update project files from OneCompiler (clean sync)"

# Add any files here that you never want the script to touch
PROTECTED_FILES = {
    ".git", 
    ".gitignore",
    ".gitattributes",
    SCRIPT_NAME, 
    "LICENSE", 
    "README.md"
}
# ---------------------

async def download_onecompiler_zip(project_url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        print(f"Opening project: {project_url}")
        await page.goto(project_url)
        await page.wait_for_selector(".explorer-files, button:has-text('Run')")

        # Open options menu
        await page.click("button:has-text('Run') + div, .three-dots-menu-icon-selector") 
        
        # Trigger and capture download
        async with page.expect_download() as download_info:
            await page.click("text=Download")
            
        download = await download_info.value
        zip_path = os.path.join(REPO_DIR, download.suggested_filename)
        await download.save_as(zip_path)
        await browser.close()
        
        print(f"Downloaded ZIP to: {zip_path}")
        return zip_path

def clear_old_files(target_dir, current_zip_name):
    print("Clearing old local files...")
    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)
        
        # PROTECTION check against our whitelist + the active ZIP download
        if item in PROTECTED_FILES or item == current_zip_name:
            continue
            
        try:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)
        except Exception as e:
            print(f"Warning: Could not delete {item}: {e}")

def extract_and_git_sync(zip_path):
    zip_name = os.path.basename(zip_path)
    
    # 1. Clear out the non-protected workspace files
    clear_old_files(REPO_DIR, zip_name)
    
    # 2. Extract new files
    print("Extracting fresh files...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(REPO_DIR)
    
    # Remove the ZIP archive
    os.remove(zip_path)
    print("Workspace refreshed.")

    # 3. Git sync sequence
    try:
        print("Staging all changes...")
        subprocess.run(["git", "add", "-A"], check=True, cwd=REPO_DIR)
        
        print("Committing changes...")
        subprocess.run(["git", "commit", "-m", COMMIT_MESSAGE], check=True, cwd=REPO_DIR)
        
        print("Pushing to remote repository...")
        subprocess.run(["git", "push"], check=True, cwd=REPO_DIR)
        
        print("Successfully synchronized clean workspace to remote!")
    except subprocess.CalledProcessError as e:
        print(f"Git automation command failed: {e}")

async def main():
    if not os.path.exists(os.path.join(REPO_DIR, ".git")):
        print("Error: This script must be run inside an initialized Git repository.")
        return
        
    zip_file = await download_onecompiler_zip(PROJECT_URL)
    extract_and_git_sync(zip_file)

if __name__ == "__main__":
    asyncio.run(main())
