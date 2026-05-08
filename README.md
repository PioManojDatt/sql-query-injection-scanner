# SQL Injection Scanner

[![PyPI version](https://badge.fury.io/py/sql-injection-scanner.svg)](https://badge.fury.io/py/sql-injection-scanner)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive Python tool to scan your codebase for potential SQL injection vulnerabilities, with a focus on detecting unsafe f-strings and string formatting in database queries.

## Overview

The SQL Injection Scanner analyzes Python source code to identify potentially dangerous SQL query construction patterns. It detects multiple vulnerability patterns and generates detailed, color-coded Excel reports with risk level classifications.

### Key Features

- **🎯 Multi-Pattern Detection**
  - F-strings in SQL queries (HIGH RISK)
  - String concatenation in SQL queries (HIGH RISK)
  - `.format()` method usage (MEDIUM RISK)
  - `%` formatting in SQL queries (MEDIUM RISK)

- **📊 Risk Level Classification**
  - HIGH: Immediate action required
  - MEDIUM: Should be reviewed and fixed
  - LOW: Monitor for patterns

- **📈 Excel Report Generation**
  - Formatted Excel workbook with detailed findings
  - Summary sheet with statistics
  - Color-coded rows by risk level
  - Sortable and filterable data

- **🚀 Easy Integration**
  - Command-line interface
  - Python API for programmatic use
  - Configurable scanning patterns
  - Smart filtering for safe parameterized queries

## Installation

### From PyPI

```bash
pip install sql-injection-scanner
```

### From Source

```bash
git clone https://github.com/PioManojDatt/sql-query-injection-scanner.git
cd sql-query-injection-scanner
pip install -e .
```

### Requirements

- Python 3.6+
- openpyxl (automatically installed as a dependency)

## Usage

### Command Line

Run the scanner on the current directory:

```bash
sql-injection-scanner
```

Scan a specific directory:

```bash
sql-injection-scanner /path/to/your/project
```

Specify output file:

```bash
sql-injection-scanner /path/to/project -o custom_report.xlsx
```

View help:

```bash
sql-injection-scanner --help
```

### Python API

```python
from sql_injection_scanner import SQLInjectionScanner

# Create scanner instance
scanner = SQLInjectionScanner('/path/to/your/project')

# Run scan
findings = scanner.scan()

# Generate Excel report
scanner.generate_excel_report('vulnerability_report.xlsx')

# Access findings programmatically
for finding in findings:
    print(f"{finding['file_path']}:{finding['line_number']} - {finding['risk_level']}")
```

## Output

### Excel Report

The scanner generates `sql_injection_report.xlsx` with two sheets:

#### Sheet 1: "SQL Injection Findings"

| Column | Description |
|--------|-------------|
| **File Path** | Relative path to the vulnerable file |
| **Module Name** | Python module name (filename without extension) |
| **Line Number** | Line number where issue was detected |
| **Pattern** | Type of vulnerability detected |
| **Risk Level** | HIGH, MEDIUM, or LOW |
| **Code Snippet** | The actual problematic code |

Rows are color-coded:
- 🔴 **RED (HIGH)**: Immediate action required
- 🟠 **ORANGE (MEDIUM)**: Should be reviewed and fixed
- 🟡 **YELLOW (LOW)**: Monitor for patterns

#### Sheet 2: "Summary"

Summary statistics including:
- Total number of findings
- Breakdown by risk level (HIGH, MEDIUM, LOW)
- Scan location

## Vulnerability Patterns Detected

### HIGH RISK: F-String SQL Construction

```python
# ❌ VULNERABLE
user_id = request.args.get('id')
query = f"SELECT * FROM users WHERE id = {user_id}"
```

**Fix:** Use parameterized queries

```python
# ✅ SAFE
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
```

### HIGH RISK: String Concatenation

```python
# ❌ VULNERABLE
query = "SELECT * FROM users WHERE name = '" + username + "'"
```

**Fix:** Use parameterized queries

```python
# ✅ SAFE
cursor.execute("SELECT * FROM users WHERE name = %s", (username,))
```

### MEDIUM RISK: .format() Method

```python
# ❌ POTENTIALLY VULNERABLE
query = "SELECT * FROM users WHERE email = '{}'".format(email)
```

**Fix:** Use parameterized queries

```python
# ✅ SAFE
cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
```

### MEDIUM RISK: % Formatting

```python
# ❌ POTENTIALLY VULNERABLE
query = "SELECT * FROM users WHERE id = %s" % (user_id)
```

**Fix:** Use parameterized queries with proper libraries

```python
# ✅ SAFE
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
```

## Configuration

### Python API Options

```python
scanner = SQLInjectionScanner(
    root_dir='/path/to/project'  # Directory to scan
)

# Customize output
scanner.generate_excel_report(
    output_file='my_report.xlsx'
)
```

## Best Practices

### Using Parameterized Queries

**psycopg2:**
```python
import psycopg2

conn = psycopg2.connect("dbname=test user=postgres")
cursor = conn.cursor()

# Safe: Use parameterized queries
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
results = cursor.fetchall()
```

**SQLAlchemy (ORM - Recommended):**
```python
from sqlalchemy import create_engine, text

engine = create_engine('postgresql://user:password@localhost/dbname')

with engine.connect() as conn:
    result = conn.execute(
        text("SELECT * FROM users WHERE id = :user_id"),
        {"user_id": user_id}
    )
```

**Django ORM (Recommended):**
```python
from django.db import connection

# Safe: Use ORM
users = User.objects.filter(id=user_id)

# Or use parameterized raw SQL
with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM users WHERE id = %s", [user_id])
    row = cursor.fetchone()
```

## Understanding Results

### False Positives

The scanner may flag safe code patterns if they:
- Contain SQL keywords in comments or documentation strings
- Use variables that happen to match keyword patterns

### Handling False Positives

1. **Review findings in context** - Check the actual code and risk level
2. **Use parameterized queries** - Even if flagged as LOW risk
3. **Report issues** - If you find consistent false positives

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Bug Reports

Found a bug? Please report it on [GitHub Issues](https://github.com/PioManojDatt/sql-query-injection-scanner/issues).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool provides automated scanning for common SQL injection patterns. It is not a substitute for professional security audits and code reviews. Always conduct thorough security testing before deploying applications to production.

## Support

For questions, issues, or suggestions:
- Open an issue on [GitHub](https://github.com/PioManojDatt/sql-query-injection-scanner/issues)
- Email: contact@PioManojDatt.com

## Related Resources

- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [CWE-89: SQL Injection](https://cwe.mitre.org/data/definitions/89.html)
- [PostgreSQL Prepared Statements](https://www.postgresql.org/docs/current/sql-prepare.html)
- [SQLAlchemy Best Practices](https://docs.sqlalchemy.org/)

---

**Version:** 1.0.0  
**Last Updated:** 2024
