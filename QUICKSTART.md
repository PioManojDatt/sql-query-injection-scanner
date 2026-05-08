#!/usr/bin/env python3
"""
Quick start guide for SQL Injection Scanner

This script demonstrates the basic usage patterns.
"""

print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    SQL Injection Scanner - Quick Start                       ║
╚══════════════════════════════════════════════════════════════════════════════╝

INSTALLATION
============
    pip install sql-injection-scanner

COMMAND LINE USAGE
==================

Scan current directory:
    $ sql-injection-scanner

Scan specific directory:
    $ sql-injection-scanner /path/to/project

Custom output file:
    $ sql-injection-scanner /path/to/project -o my_report.xlsx

View help:
    $ sql-injection-scanner --help

PYTHON API USAGE
================

Basic usage:
    
    from sql_injection_scanner import SQLInjectionScanner
    
    # Create scanner
    scanner = SQLInjectionScanner('/path/to/project')
    
    # Run scan
    findings = scanner.scan()
    
    # Generate report
    scanner.generate_excel_report('report.xlsx')
    
    # Access findings
    for finding in findings:
        print(f"{finding['file_path']}:{finding['line_number']}")

Working with results:

    # Filter by risk level
    high_risk = [f for f in findings if f['risk_level'] == 'HIGH']
    
    # Group by file
    by_file = {}
    for finding in findings:
        if finding['file_path'] not in by_file:
            by_file[finding['file_path']] = []
        by_file[finding['file_path']].append(finding)
    
    # Generate statistics
    total = len(findings)
    high = sum(1 for f in findings if f['risk_level'] == 'HIGH')
    medium = sum(1 for f in findings if f['risk_level'] == 'MEDIUM')
    low = sum(1 for f in findings if f['risk_level'] == 'LOW')

VULNERABILITY PATTERNS
======================

F-String (HIGH RISK)
    ❌ query = f"SELECT * FROM users WHERE id = {user_id}"
    ✅ cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

String Concatenation (HIGH RISK)
    ❌ query = "SELECT * FROM users WHERE name = '" + username + "'"
    ✅ cursor.execute("SELECT * FROM users WHERE name = %s", (username,))

.format() Method (MEDIUM RISK)
    ❌ query = "SELECT * FROM users WHERE email = '{}'".format(email)
    ✅ cursor.execute("SELECT * FROM users WHERE email = %s", (email,))

Percent Formatting (MEDIUM RISK)
    ❌ query = "SELECT * FROM users WHERE id = '%s'" % (user_id)
    ✅ cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

COMMON FRAMEWORKS
=================

psycopg2:
    import psycopg2
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))

SQLAlchemy:
    from sqlalchemy import text
    result = engine.execute(text("SELECT * FROM users WHERE id = :id"), id=user_id)

Django ORM:
    User.objects.filter(id=user_id)  # Automatically parameterized

OUTPUT FILES
============

The scanner generates:
    - sql_injection_report.xlsx  Main Excel report with all findings
    - Summary sheet with statistics
    - Color-coded by risk level (RED=HIGH, ORANGE=MEDIUM, YELLOW=LOW)

MORE INFORMATION
================

Full documentation: See README.md
Deployment guide: See DEPLOYMENT.md
Examples: Run example_usage.py

For issues or questions:
    Email: contact@PioManojDatt.com
    GitHub: https://github.com/PioManojDatt/sql-query-injection-scanner

╔══════════════════════════════════════════════════════════════════════════════╗
║                          Happy Scanning! 🛡️                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝
""")
