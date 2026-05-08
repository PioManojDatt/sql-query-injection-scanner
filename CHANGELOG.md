# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-01-XX

### Added
- Initial release of SQL Injection Scanner
- Command-line interface with argparse
- Python API for programmatic scanning
- Multi-pattern detection for SQL injection vulnerabilities:
  - F-string detection (HIGH RISK)
  - String concatenation detection (HIGH RISK)
  - `.format()` method detection (MEDIUM RISK)
  - `%` formatting detection (MEDIUM RISK)
- Excel report generation with color-coded findings
- Summary sheet with vulnerability statistics
- Smart filtering for safe parameterized queries
- Support for Python 3.6+
- Comprehensive documentation and examples

### Features
- Recursive directory scanning with configurable skip patterns
- Risk level classification (HIGH, MEDIUM, LOW)
- Detailed code snippet extraction
- Line number reporting
- Module name extraction
- Sorted findings by risk level and file path

## Future Releases

### [Planned]
- Additional database framework support detection (SQLAlchemy, Django ORM)
- JSON output format support
- Custom pattern configuration
- Performance optimizations for large codebases
- Additional test coverage
- Integration with CI/CD pipelines
- Web-based report viewer
