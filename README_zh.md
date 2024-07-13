# Wox.Plugin.UrlAllinOne

Wox.Plugin.UrlAllinOne 是一个强大的 Wox 插件，提供了多种 URL 相关的操作功能，包括编码/解码、缩短 URL、生成二维码等。

## 功能

- URL 编码和解码
- 获取短 URL
- 从短 URL 获取原始 URL
- 生成 URL 的二维码
- 获取 URL 的重定向链
- 将 URL 参数解析为 JSON 格式
- 提取网页的 Open Graph 信息
- 提取网页的 Twitter Card 信息

## 安装

1. 确保你已经安装了 [Wox](http://www.wox.one/)。
2. 下载此插件的 zip 文件。
3. 将 zip 文件解压到 Wox 的插件目录（通常是 `%APPDATA%\Wox\Plugins`）。

## 使用方法

在 Wox 搜索框中输入 `url` 后跟一个空格，然后输入相应的子命令和 URL。例如：

- `url en https://example.com` - 编码 URL
- `url de https%3A%2F%2Fexample.com` - 解码 URL
- `url s https://example.com` - 获取短 URL
- `url o http://tinyurl.com/xxx` - 获取原始 URL
- `url qr https://example.com` - 生成 URL 的二维码
- `url re https://example.com` - 获取 URL 的重定向链
- `url json https://example.com?param1=value1&param2=value2` - 解析 URL 参数为 JSON
- `url og https://example.com` - 提取 Open Graph 信息
- `url tc https://example.com` - 提取 Twitter Card 信息

## 依赖

此插件依赖以下 Python 库：

- requests
- qrcode
- beautifulsoup4

你可以通过以下命令安装这些依赖：

`pip install requests qrcode beautifulsoup4`

## 贡献

欢迎提交 issues 和 pull requests。

## 许可证

[MIT License](LICENSE)