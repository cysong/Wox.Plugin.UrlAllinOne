# Wox.Plugin.UrlAllinOne

Wox.Plugin.UrlAllinOne is a powerful Wox plugin that provides a variety of URL-related operations, including encoding/decoding, shortening URLs, generating QR codes, and more.

## Features

- URL encoding and decoding
- Shortening URLs
- Retrieving original URLs from shortened ones
- Generating QR codes for URLs
- Getting the redirect chain of a URL
- Parsing URL parameters to JSON format
- Extracting Open Graph information from web pages
- Extracting Twitter Card information from web pages

## Installation

1. Ensure you have [Wox](http://www.wox.one/) installed.
2. Download the zip file of this plugin.
3. Extract the zip file to Wox's plugin directory (typically `%APPDATA%\Wox\Plugins`).

## Usage

In the Wox search box, type `url` followed by a space, then enter the corresponding subcommand and URL. For example:

- `url en https://example.com` - Encode URL
- `url de https%3A%2F%2Fexample.com` - Decode URL
- `url s https://example.com` - Get short URL
- `url o http://tinyurl.com/xxx` - Get original URL
- `url qr https://example.com` - Generate QR code for URL
- `url re https://example.com` - Get URL redirect chain
- `url json https://example.com?param1=value1&param2=value2` - Parse URL parameters to JSON
- `url og https://example.com` - Extract Open Graph information
- `url tc https://example.com` - Extract Twitter Card information

## Dependencies

This plugin depends on the following Python libraries:

- requests
- qrcode
- beautifulsoup4

You can install these dependencies using:

`pip install requests qrcode beautifulsoup4`

## Contributing

Issues and pull requests are welcome.

## License

[MIT License](LICENSE)