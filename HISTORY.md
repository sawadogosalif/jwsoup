# Changelog

## [0.0.1] - 2024-11-23
### Added
- Initial release of `jw_scraper`.
- Supports scraping of text-based Bible verses from JW.org.
- Extracts individual verses and saves them to parquet files using `pyarrow`.
- Includes basic error handling and logging with `loguru`.

### Known Limitations
- Only supports scraping textual data.
- Does not handle multimedia content (audio/video).
- Limited testing for edge cases (e.g., malformed HTML or network interruptions).
