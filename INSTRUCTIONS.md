# SQL Injection Scanner - Package Build & Deployment Instructions

Complete guide for building, testing, and deploying the SQL Injection Scanner package to PyPI.

## Table of Contents

1. [Quick Start](#quick-start)
2. [Local Testing](#local-testing)
3. [Building for Distribution](#building-for-distribution)
4. [Testing on PyPI](#testing-on-testpypi)
5. [Production Deployment](#production-deployment)
6. [Post-Deployment Verification](#post-deployment-verification)

## Quick Start

### One-Time Setup

```bash
# Clone or navigate to the package directory
cd sql-query-injection-scanner

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install development dependencies
pip install --upgrade pip
pip install -e ".[dev]"
```

### Verify Local Installation Works

```bash
# Test the CLI
sql-injection-scanner --help
sql-injection-scanner --version

# Test Python API
python -c "from sql_injection_scanner import SQLInjectionScanner; print('Import successful!')"
```

## Local Testing

### Run Unit Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=sql_injection_scanner --cov-report=html

# Run specific test file
pytest tests/test_scanner.py -v
```

### Code Quality Checks

```bash
# Check code formatting
black --check sql_injection_scanner tests

# Fix formatting
black sql_injection_scanner tests

# Lint code
flake8 sql_injection_scanner tests

# Type checking
mypy sql_injection_scanner

# All checks together
tox
```

### Test Installation in Clean Environment

```bash
# Create temporary virtual environment
python -m venv test_env
source test_env/bin/activate  # or test_env\Scripts\activate on Windows

# Install from local directory
pip install -e /path/to/sql-query-injection-scanner

# Test it works
sql-injection-scanner --help

# Cleanup
deactivate
rm -rf test_env
```

## Building for Distribution

### Prerequisites

Ensure you're in the package directory with your virtual environment activated:

```bash
# Upgrade build tools
pip install --upgrade pip build twine
```

### Create Distribution Files

```bash
# Clean previous builds
rm -rf build dist *.egg-info

# Build both source and wheel distributions
python -m build

# Verify built files
ls -la dist/
```

This creates:
- `dist/sql-injection-scanner-1.0.0.tar.gz` (source distribution)
- `dist/sql-injection-scanner-1.0.0-py3-none-any.whl` (wheel)

### Validate Distribution Files

```bash
# Check for common issues
python -m twine check dist/*

# Inspect wheel contents
python -m zipfile -l dist/sql-injection-scanner-1.0.0-py3-none-any.whl

# Inspect source distribution
tar -tzf dist/sql-injection-scanner-1.0.0.tar.gz | head -20
```

## Testing on TestPyPI

### Get TestPyPI API Token

1. Create account at https://test.pypi.org/account/register/
2. Go to https://test.pypi.org/manage/account/tokens/
3. Create a new token with scope "Entire account"
4. Copy and save the token securely

### Configure Local Credentials

Create `~/.pypirc` file (or update if exists):

```ini
[distutils]
index-servers =
    testpypi
    pypi

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-AgEIcHlwaS5vcmc...  # Your TestPyPI token

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = pypi-AgEIcHlwaS5vcmc...  # Your PyPI token (get later)
```

**Security Note**: Keep `~/.pypirc` private (permissions 600 on Unix)

### Upload to TestPyPI

```bash
# Upload the distributions
python -m twine upload --repository testpypi dist/*

# When prompted, enter credentials or use token
# Username: __token__
# Password: pypi-AgEIcHlwaS5vcmc...
```

### Test Installation from TestPyPI

```bash
# Create test environment
python -m venv testpypi_env
source testpypi_env/bin/activate

# Install from TestPyPI (use explicit index)
pip install --index-url https://test.pypi.org/simple/ sql-injection-scanner

# Verify installation
sql-injection-scanner --version
sql-injection-scanner --help

# Test it scans correctly
sql-injection-scanner .

# Clean up
deactivate
rm -rf testpypi_env
```

### Verify on TestPyPI Website

1. Visit: https://test.pypi.org/project/sql-injection-scanner/
2. Verify:
   - Version number is correct
   - All metadata displays properly
   - Description renders correctly
   - Files are listed

## Production Deployment

### Get PyPI API Token

1. Create account at https://pypi.org/account/register/
2. Go to https://pypi.org/manage/account/tokens/
3. Create a new token with scope "Entire account" (or project-specific)
4. Copy and save the token securely

### Update PyPI Credentials

Update your `~/.pypirc`:

```ini
[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = pypi-AgEIcHlwaS5vcmc...  # Your PyPI token
```

### Deploy to Production PyPI

```bash
# Verify everything is ready
python -m twine check dist/*

# Upload to production PyPI
python -m twine upload dist/*
```

## Post-Deployment Verification

### Verify on PyPI

1. Visit: https://pypi.org/project/sql-injection-scanner/
2. Check:
   - Version number
   - Description and README
   - Download files (wheel and tarball)
   - Project links
   - Classifiers

### Test Production Installation

```bash
# Create test environment
python -m venv prod_test_env
source prod_test_env/bin/activate

# Install from production PyPI
pip install sql-injection-scanner

# Verify
sql-injection-scanner --version

# Test on a directory
sql-injection-scanner /path/to/test/project

# Clean up
deactivate
rm -rf prod_test_env
```

### Create Git Tag and Release

```bash
# Tag the release
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0

# Or create directly on GitHub:
# 1. Go to https://github.com/PioManojDatt/sql-query-injection-scanner/releases
# 2. Click "Create a new release"
# 3. Tag: v1.0.0
# 4. Title: Release 1.0.0
# 5. Add release notes
# 6. Upload dist/* files
# 7. Publish
```

### Announce Release

- Update project website
- Send announcement email
- Post on social media
- Notify relevant communities

## Version Bump Workflow

For future releases:

### 1. Update Version Numbers

Edit these files and change version:
- `sql_injection_scanner/__init__.py`
- `setup.py`
- `pyproject.toml`
- `setup.cfg`

```python
__version__ = "1.1.0"
```

### 2. Update Changelog

Edit `CHANGELOG.md`:

```markdown
## [1.1.0] - 2024-01-XX

### Added
- New feature description

### Fixed
- Bug fix description

### Changed
- Change description
```

### 3. Commit and Tag

```bash
git add -A
git commit -m "Bump version to 1.1.0"
git tag -a v1.1.0 -m "Release version 1.1.0"
git push
git push origin v1.1.0
```

### 4. Build and Deploy

```bash
# Clean old builds
rm -rf build dist *.egg-info

# Build
python -m build

# Test on TestPyPI
python -m twine upload --repository testpypi dist/*

# Deploy to production
python -m twine upload dist/*
```

## Troubleshooting

### Issue: "Filename already exists on index"

**Cause**: Package with same version was already uploaded
**Solution**: Increment version number in all files and rebuild

### Issue: "Invalid classifier"

**Cause**: Invalid classifier in setup.py/setup.cfg
**Solution**: Check classifiers against [official list](https://pypi.org/classifiers/)

### Issue: "README rendering fails"

**Cause**: README.md has invalid Markdown/RST
**Solution**: 
```bash
# Check rendering
python -m twine check dist/*

# Fix Markdown syntax
```

### Issue: "Upload hangs or times out"

**Cause**: Network or Twine issue
**Solution**: 
```bash
# Try verbose mode
python -m twine upload --verbose dist/*

# Or try again later
```

### Issue: "Authentication failed"

**Cause**: Invalid token or credentials
**Solution**:
```bash
# Regenerate token at PyPI website
# Update ~/.pypirc with new token
# Verify permissions
```

## Best Practices

1. **Always test on TestPyPI first** - Avoid mistakes on production
2. **Use API tokens, not passwords** - More secure
3. **Keep ~/.pypirc private** - Set permissions to 600 on Unix
4. **Test installation in clean environment** - Catch dependency issues
5. **Tag releases in Git** - Maintain version history
6. **Update CHANGELOG** - Document all changes
7. **Run all checks** - Use tox before deploying
8. **Wait after release** - Allow time for CDN propagation before heavy promotion

## Useful Links

- [PyPI Package Management](https://pypi.org/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Python Packaging Guide](https://packaging.python.org/)
- [setuptools Documentation](https://setuptools.pypa.io/)
- [Wheel Documentation](https://wheel.readthedocs.io/)
- [PyPI Classifiers](https://pypi.org/classifiers/)

## Support

For deployment help:
- Review this guide thoroughly
- Check official PyPI and Twine documentation
- Contact: contact@PioManojDatt.com

---

**Last Updated**: 2024
**Package**: sql-injection-scanner v1.0.0
