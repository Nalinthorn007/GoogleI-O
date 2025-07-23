# 🚀 UV Package Setup Guide

Follow these step-by-step instructions to set up the UV package manager and get your project running.

## Prerequisites

### 1. Install Git
Download and install Git from the official website: https://git-scm.com/downloads

### 2. Verify Git Installation
After successful installation, verify Git is working by running:
```bash
git --version
```

### 3. Clone the Repository
Navigate to your desired folder and clone the repository:
```bash
git clone https://github.com/Nalinthorn007/GoogleI-O.git
```
The files will be downloaded automatically to your current directory.

## UV Installation

### 4. Check UV Installation Status
First, check if UV is already installed:
```bash
uv --version
```
**Run this command in PowerShell (Windows) or Terminal (macOS/Linux)**

### 5. Install UV (if not already installed)
If UV is not installed, follow the installation guide at: https://docs.astral.sh/uv/

#### 5.1 Windows Installation
**Run in PowerShell:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### 5.2 macOS/Linux Installation
**Run in Terminal:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 6. Verify UV Installation
After installation, verify UV is working correctly:
```bash
uv --version
```
**Run this command in PowerShell (Windows) or Terminal (macOS/Linux)**

### 7. Sync Dependencies
Once UV is successfully installed, synchronize all project dependencies:
```bash
uv sync
```
This will create a `.venv` virtual environment and install all required libraries.

## Final Steps

### 8. Install Required Models
Run the provided Jupyter notebook to download the necessary models:
```bash
download-model.ipynb
```

> **⚠️ IMPORTANT:** The models and configurations are already set up for you! 
> 
> **DO NOT change anything in the notebook except for the file paths** that need to be adapted to your system location. Everything else should remain exactly as provided.

---

## 🎉 Congratulations!

You've successfully completed the setup guide! Your development environment is now ready. 

**Time to launch your project to the moon! 🌙**

---

### Troubleshooting
- If you encounter permission issues on Windows, make sure to run PowerShell as Administrator
- On macOS/Linux, you may need to restart your terminal after UV installation
- Ensure you have sufficient disk space for the model downloads

### Support
If you encounter any issues, please check the official UV documentation or create an issue in the repository.