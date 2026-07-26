# Playwright set up
1. Make sure python is installed:
    - python --version

2. Create a folder for the project

3. Create a virtual environment in that folder:
    - python3 -m venv .venv

4. Activate the virtual environment
    - source .venv/bin/activate

5. Install playwright
    - pip install playwright

6. Download Playwright browser binaries
   - playwright install

7. Install browser dependencies
    - python -m playwright install-deps

8. Verify installation:
    - playwright --version

9. Install Pytest
    - pip install pytest pytest-playwright