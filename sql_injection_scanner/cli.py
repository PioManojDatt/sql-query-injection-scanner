#!/usr/bin/env python3
"""
Command-line interface for SQL Injection Scanner.

Provides the main entry point for running the scanner from the command line.
"""

import sys
import argparse
from pathlib import Path

from .scanner import SQLInjectionScanner


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description='SQL Injection Vulnerability Scanner',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  sql-injection-scanner                    # Scan current directory
  sql-injection-scanner /path/to/project   # Scan specific directory
  sql-injection-scanner . -o report.xlsx   # Custom output file
        '''
    )
    
    parser.add_argument(
        'directory',
        nargs='?',
        default='.',
        help='Directory to scan (default: current directory)'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='sql_injection_report.xlsx',
        help='Output Excel file path (default: sql_injection_report.xlsx)'
    )
    
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s 1.0.1'
    )
    
    parser.add_argument(
        '-q', '--quiet',
        action='store_true',
        help='Suppress output (only generate report)'
    )
    
    args = parser.parse_args()
    
    # Verify directory exists
    target_dir = Path(args.directory)
    if not target_dir.exists():
        print(f"Error: Directory '{args.directory}' does not exist", file=sys.stderr)
        sys.exit(1)
    
    if not target_dir.is_dir():
        print(f"Error: '{args.directory}' is not a directory", file=sys.stderr)
        sys.exit(1)
    
    try:
        # Create scanner and run scan
        scanner = SQLInjectionScanner(str(target_dir))
        findings = scanner.scan()
        
        # Generate report
        report_file = scanner.generate_excel_report(args.output)
        
        if not args.quiet:
            # Print summary
            print(f"\n{'='*60}")
            print(f"Scan Complete!")
            print(f"{'='*60}")
            print(f"Total Vulnerabilities Found: {len(findings)}")
            print(f"High Risk: {sum(1 for f in findings if f['risk_level'] == 'HIGH')}")
            print(f"Medium Risk: {sum(1 for f in findings if f['risk_level'] == 'MEDIUM')}")
            print(f"Low Risk: {sum(1 for f in findings if f['risk_level'] == 'LOW')}")
            print(f"\nReport saved to: {report_file}")
            print(f"{'='*60}\n")
            
            # Print first few findings
            if findings:
                print("Top findings:")
                risk_order = {'HIGH': 0, 'MEDIUM': 1, 'LOW': 2}
                sorted_findings = sorted(
                    findings,
                    key=lambda x: (risk_order.get(x['risk_level'], 3), x['file_path'], x['line_number'])
                )
                for finding in sorted_findings[:10]:
                    print(f"  [{finding['risk_level']}] {finding['file_path']}:{finding['line_number']} - {finding['pattern']}")
        
        return 0
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
