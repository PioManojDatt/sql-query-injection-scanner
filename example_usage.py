#!/usr/bin/env python3
"""
Example usage of the SQL Injection Scanner package.

This script demonstrates how to use the SQL Injection Scanner
both as a command-line tool and as a Python library.
"""

from sql_injection_scanner import SQLInjectionScanner
from pathlib import Path


def example_api_usage():
    """Example of using the scanner as a Python API."""
    print("=" * 60)
    print("SQL Injection Scanner - API Usage Example")
    print("=" * 60)
    
    # Create scanner for current directory
    scanner = SQLInjectionScanner('.')
    
    # Run the scan
    print("\nScanning...")
    findings = scanner.scan()
    
    # Process results
    print(f"\nFound {len(findings)} potential vulnerabilities\n")
    
    # Group by risk level
    high_risk = [f for f in findings if f['risk_level'] == 'HIGH']
    medium_risk = [f for f in findings if f['risk_level'] == 'MEDIUM']
    low_risk = [f for f in findings if f['risk_level'] == 'LOW']
    
    print(f"HIGH RISK:   {len(high_risk)} findings")
    print(f"MEDIUM RISK: {len(medium_risk)} findings")
    print(f"LOW RISK:    {len(low_risk)} findings")
    
    # Display findings by risk level
    if high_risk:
        print("\n" + "=" * 60)
        print("HIGH RISK FINDINGS (Immediate Action Required)")
        print("=" * 60)
        for finding in high_risk[:5]:
            print(f"\n  File: {finding['file_path']}:{finding['line_number']}")
            print(f"  Pattern: {finding['pattern']}")
            print(f"  Code: {finding['code']}")
    
    if medium_risk:
        print("\n" + "=" * 60)
        print("MEDIUM RISK FINDINGS (Should Be Reviewed)")
        print("=" * 60)
        for finding in medium_risk[:5]:
            print(f"\n  File: {finding['file_path']}:{finding['line_number']}")
            print(f"  Pattern: {finding['pattern']}")
            print(f"  Code: {finding['code']}")
    
    # Generate Excel report
    print("\n" + "=" * 60)
    print("Generating Excel Report...")
    print("=" * 60)
    report_file = scanner.generate_excel_report('example_report.xlsx')
    print(f"✓ Report saved to: {report_file}\n")


def example_filtering():
    """Example of filtering and analyzing findings programmatically."""
    print("=" * 60)
    print("SQL Injection Scanner - Filtering Example")
    print("=" * 60)
    
    scanner = SQLInjectionScanner('.')
    findings = scanner.scan()
    
    # Find all HIGH RISK findings
    high_risk_findings = [f for f in findings if f['risk_level'] == 'HIGH']
    
    print(f"\nTotal HIGH RISK findings: {len(high_risk_findings)}")
    
    # Group by file
    files_with_issues = {}
    for finding in high_risk_findings:
        file_path = finding['file_path']
        if file_path not in files_with_issues:
            files_with_issues[file_path] = []
        files_with_issues[file_path].append(finding)
    
    print(f"\nFiles with HIGH RISK findings:")
    for file_path, findings_in_file in files_with_issues.items():
        print(f"  {file_path}: {len(findings_in_file)} issues")


def example_custom_output():
    """Example of generating custom output formats."""
    print("=" * 60)
    print("SQL Injection Scanner - Custom Output Example")
    print("=" * 60)
    
    scanner = SQLInjectionScanner('.')
    findings = scanner.scan()
    
    # Generate CSV-style output
    print("\nCSV Output:")
    print("file_path,line_number,risk_level,pattern,code")
    for finding in findings[:10]:
        csv_line = f'"{finding["file_path"]}",{finding["line_number"]},{finding["risk_level"]},"{finding["pattern"]}","{finding["code"]}"'
        print(csv_line)
    
    # Generate JSON output (requires json module)
    import json
    print("\n\nJSON Output (first 3 findings):")
    json_output = json.dumps(findings[:3], indent=2)
    print(json_output)


if __name__ == '__main__':
    # Run examples
    example_api_usage()
    # example_filtering()
    # example_custom_output()
    
    print("\nFor more information, see the README.md file.")
    print("Or run: sql-injection-scanner --help")
