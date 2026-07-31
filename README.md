# Playwright set up
1. Make sure python is installed:
    - python3 --version

2. Create a folder for the project

3. Create a virtual environment in that folder:
    - python3 -m venv .venv
    - apt install python3.14-venv

5. Activate the virtual environment
    - source .venv/bin/activate

6. Install playwright
    - pip install playwright

7. Download Playwright browser binaries
   - playwright install

8. Install browser dependencies
    - python -m playwright install-deps

9. Verify installation:
    - playwright --version

10. Install Pytest
    - pip install pytest pytest-playwright

11. Check all the installed packages
- pip list
