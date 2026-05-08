# SQL Injection Scanner - PyPI Deployment Guide

This guide provides step-by-step instructions for deploying the SQL Injection Scanner package to PyPI (Python Package Index).

## Prerequisites

Before deploying to PyPI, ensure you have:

1. **PyPI Account**: Register at [https://pypi.org/account/register/](https://pypi.org/account/register/)
2. **TestPyPI Account** (Optional but recommended): Register at [https://test.pypi.org/account/register/](https://test.pypi.org/account/register/)
3. **Required Tools**:
   ```bash
   pip install --upgrade pip
   pip install build twine
   ```

## Step 1: Prepare the Package

### 1.1 Verify Package Structure

Ensure your project structure matches this:

```
sql-injection-scanner/
├── sql_injection_scanner/
│   ├── __init__.py
│   ├── scanner.py
│   └── cli.py
├── tests/
│   └── __init__.py
├── setup.py
├── pyproject.toml
├── setup.cfg
├── README.md
├── LICENSE
├── CHANGELOG.md
├── MANIFEST.in
└── .gitignore
```

### 1.2 Update Version Numbers

Update the version in these files (currently 1.0.0):
- `sql_injection_scanner/__init__.py`
- `setup.py`
- `pyproject.toml`
- `setup.cfg`

## Step 2: Build the Package

### 2.1 Build Distribution Files

```bash
# Clean previous builds
rm -rf build dist *.egg-info

# Build the package (creates wheel and source distribution)
python -m build
```

This creates:
- `dist/sql-injection-scanner-1.0.0.tar.gz` (source distribution)
- `dist/sql-injection-scanner-1.0.0-py3-none-any.whl` (wheel)

### 2.2 Verify Build

```bash
# Check the distribution files
ls -la dist/

# Verify the wheel contents
python -m zipfile -l dist/sql-injection-scanner-1.0.0-py3-none-any.whl
```

## Step 3: Test on TestPyPI (Recommended)

### 3.1 Create PyPI Credentials

Option A: Use API Token (Recommended)
1. Go to [https://test.pypi.org/manage/account/token/](https://test.pypi.org/manage/account/token/)
2. Create a new API token
3. Save it somewhere secure (you'll need it in Step 3.2)

Option B: Use Username/Password
1. Use your TestPyPI username and password directly

### 3.2 Configure Credentials

Create or edit `~/.pypirc` file:

```ini
[distutils]
index-servers =
    testpypi
    pypi

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-AgEIcHlwaS5vcmc... (your token here)

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = pypi-AgEIcHlwaS5vcmc... (your actual PyPI token)
```

### 3.3 Upload to TestPyPI

```bash
python -m twine upload --repository testpypi dist/*
```

### 3.4 Test Installation from TestPyPI

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ sql-injection-scanner
```

Test the CLI:
```bash
sql-injection-scanner --help
```

## Step 4: Deploy to PyPI

### 4.1 Upload to Production PyPI

Once you've tested on TestPyPI and everything works:

```bash
python -m twine upload dist/*
```

When prompted, enter your PyPI credentials (API token).

### 4.2 Verify Publication

1. Visit [https://pypi.org/project/sql-injection-scanner/](https://pypi.org/project/sql-injection-scanner/)
2. Verify all files and metadata are correct

## Step 5: Post-Deployment

### 5.1 Install from PyPI

```bash
pip install sql-injection-scanner
```

### 5.2 Test Installation

```bash
sql-injection-scanner --version
sql-injection-scanner --help
```

### 5.3 Create Release Tag (Git)

```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

### 5.4 Create GitHub Release

1. Go to [https://github.com/PioManojDatt/sql-query-injection-scanner/releases](https://github.com/PioManojDatt/sql-query-injection-scanner/releases)
2. Click "Create a new release"
3. Tag version: `v1.0.0`
4. Title: `Release 1.0.0`
5. Add release notes and upload `dist/` files
6. Publish

## Version Management Strategy

For future releases, follow this workflow:

### Example: Releasing Version 1.1.0

1. Update version in all files:
   ```bash
   # Files to update:
   # - sql_injection_scanner/__init__.py
   # - setup.py
   # - pyproject.toml
   # - setup.cfg
   ```

2. Update CHANGELOG.md with new changes

3. Rebuild:
   ```bash
   rm -rf build dist *.egg-info
   python -m build
   ```

4. Test on TestPyPI:
   ```bash
   python -m twine upload --repository testpypi dist/*
   ```

5. Deploy to PyPI:
   ```bash
   python -m twine upload dist/*
   ```

6. Tag and release on GitHub

## Troubleshooting

### "Filename already exists" Error

If you get an error that the filename already exists, it means that exact version/file combination was already uploaded. You must use a new version number.

### "Invalid Distribution" Error

Check that:
- All required files are included (setup.py, README.md, LICENSE)
- README.md is valid Markdown
- No syntax errors in Python files

Use: `python -m twine check dist/*`

### Failed Upload

Common causes:
1. Invalid PyPI token - regenerate and update `.pypirc`
2. Network issues - try again
3. Package already exists - use new version number

## Useful Commands

```bash
# Check distribution files
python -m twine check dist/*

# Upload only source distribution
python -m twine upload dist/*.tar.gz

# Upload only wheel
python -m twine upload dist/*.whl

# Upload with verbose output
python -m twine upload --verbose dist/*

# Upload to TestPyPI with explicit repository
python -m twine upload --repository testpypi dist/*
```

## Additional Resources

- [PyPI Help](https://pypi.org/help/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Python Packaging Guide](https://packaging.python.org/)
- [PEP 427 - Wheel Binary Package Format](https://www.python.org/dev/peps/pep-0427/)
- [PEP 517 - A build-backend interface for Python source distributions](https://www.python.org/dev/peps/pep-0517/)

## Support

For issues or questions about deployment:
- Check PyPI documentation
- Review package structure
- Test locally before uploading
- Contact: contact@PioManojDatt.com
