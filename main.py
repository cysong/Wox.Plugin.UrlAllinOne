# -*- coding: utf-8 -*-

import urllib.parse
import requests
import json
import qrcode
import io
import os
import tempfile
from wox import Wox
from bs4 import BeautifulSoup


class UrlTools(Wox):

    def __init__(self):
        super().__init__()
        self.commands = {
            "en": {"func": self.encode_url, "help": "Encode URL"},
            "de": {"func": self.decode_url, "help": "Decode URL"},
            "s": {"func": self.shorten_url, "help": "Get short URL"},
            "o": {"func": self.get_original_url, "help": "Get original URL from short URL"},
            "qr": {"func": self.generate_qr, "help": "Generate QR code"},
            "re": {"func": self.get_redirect_chain, "help": "Get redirect chain"},
            "json": {"func": self.parse_to_json, "help": "Parse URL parameters to JSON format"},
            "og": {"func": self.extract_open_graph, "help": "Extract Open Graph information"},
            "tc": {"func": self.extract_twitter_card, "help": "Extract Twitter Card information"}
        }

    def query(self, query):
        parts = query.strip().split(maxsplit=1)
        if len(parts) == 0 or parts[0] not in self.commands:
            return self.show_help()
        elif len(parts) == 1:
            return self.show_command_help(parts[0])
        else:
            return self.commands[parts[0]]["func"](parts[1])

    def show_help(self):
        return [
            {"Title": f"{cmd}: {info['help']}", "IcoPath": "help.png"} for cmd, info in self.commands.items()
        ]

    def show_command_help(self, cmd):
        return [{
            "Title": f"Usage: {cmd} <url>",
            "SubTitle": self.commands[cmd]["help"],
            "IcoPath": "Images/help.png"
        }]

    def is_valid_url(self, url):
        try:
            result = urllib.parse.urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

    def encode_url(self, url):
        encoded = urllib.parse.quote(url)
        return [self.create_result("Encoded URL", encoded, "app")]

    def decode_url(self, url):
        decoded = urllib.parse.unquote(url)
        return [self.create_result("Decoded URL", decoded, "app")]

    def shorten_url(self, url):
        if not self.is_valid_url(url):
            return [self.create_result("Error", "Invalid URL", "app")]
        try:
            response = requests.post(
                'https://tinyurl.com/api-create.php', data={'url': url})
            short_url = response.text
            return [self.create_result("Shortened URL", short_url, "app")]
        except:
            return [self.create_result("Error", "Failed to shorten URL", "app")]

    def get_original_url(self, url):
        if not self.is_valid_url(url):
            return [self.create_result("Error", "Invalid URL", "app")]
        try:
            response = requests.head(url, allow_redirects=True)
            original_url = response.url
            return [self.create_result("Original URL", original_url, "app")]
        except:
            return [self.create_result("Error", "Failed to get original URL", "app")]

    def generate_qr(self, url):
        if not self.is_valid_url(url):
            return [self.create_result("Error", "Invalid URL", "app")]
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img_path = self.save_qr(img)
        return [{
            "Title": "QR Code generated",
            "SubTitle": "Click to open",
            "IcoPath": "Images/app.png",
            "JsonRPCAction": {
                "method": "open_file",
                "parameters": [img_path],
                "dontHideAfterAction": False
            }
        }]

    def get_redirect_chain(self, url):
        if not self.is_valid_url(url):
            return [self.create_result("Error", "Invalid URL", "app")]
        try:
            response = requests.get(url, allow_redirects=True)
            chain = [r.url for r in response.history] + [response.url]
            return [self.create_result(f"Redirect {i+1}", url, "app") for i, url in enumerate(chain)]
        except:
            return [self.create_result("Error", "Failed to get redirect chain", "app")]

    def parse_to_json(self, url):
        if not self.is_valid_url(url):
            return [self.create_result("Error", "Invalid URL", "app")]
        parsed = urllib.parse.urlparse(url)
        params = urllib.parse.parse_qs(parsed.query)
        json_str = json.dumps(params, indent=2)
        return [self.create_result("JSON Format", json_str, "app")]

    def extract_open_graph(self, url):
        if not self.is_valid_url(url):
            return [self.create_result("Error", "Invalid URL", "app")]
        try:
            response = requests.get(url)
            og_tags = self.extract_meta_tags(response.text, "og:")
            json_str = json.dumps(og_tags, indent=2)
            return [self.create_result("Open Graph Data", json_str, "open-graph")]
        except:
            return [self.create_result("Error", "Failed to extract Open Graph info", "app")]

    def extract_twitter_card(self, url):
        if not self.is_valid_url(url):
            return [self.create_result("Error", "Invalid URL", "app")]
        try:
            response = requests.get(url)
            tc_tags = self.extract_meta_tags(response.text, "twitter:")
            json_str = json.dumps(tc_tags, indent=2)
            return [self.create_result("Twitter Card Data", json_str, "twitter")]
        except:
            return [self.create_result("Error", "Failed to extract Twitter Card info", "app")]

    def extract_meta_tags(self, html, prefix):
        soup = BeautifulSoup(html, 'html.parser')
        tags = {}
        for tag in soup.find_all("meta"):
            if tag.get("property", "").startswith(prefix):
                tags[tag["property"][len(prefix):]] = tag["content"]
        return tags

    def create_result(self, title, subtitle, icon):
        return {
            "Title": title,
            "SubTitle": subtitle,
            "IcoPath": f"Images/{icon}.png",
            "JsonRPCAction": {
                "method": "copy_to_clipboard",
                "parameters": [subtitle],
                "dontHideAfterAction": False
            }
        }

    def save_qr(self, img):
        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
            img.save(temp_file, format='PNG')
            return temp_file.name

    def copy_to_clipboard(self, text):
        command = f'echo {text.strip()}| clip'
        self.shell_run(command)

    def open_file(self, path):
        os.startfile(path)


if __name__ == "__main__":
    UrlTools()
