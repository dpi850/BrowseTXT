import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from colorama import init, Fore, Style
import random
import subprocess
import time
from datetime import datetime
from pathlib import Path
import sys
import textwrap
import shutil

init(autoreset=True)

class TextBrowser:
    COLORS = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    CACHE_TTL = 300  # 5 minutes
    MAX_CACHE_SIZE = 10

    def __init__(self):
        self.history = []
        self.current_url = None
        self.last_links = []
        self.cache = {}  # url: (timestamp, html)

    def random_color(self):
        return random.choice(self.COLORS)

    def print_header(self):
        color = self.random_color()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(color + r"""
  ____                          _________   _________
 |  _ \                        |__   __\ \ / /__   __|
 | |_) |_ __ _____      _____  ___| |   \ V /   | |
 |  _ <| '__/ _ \ \ /\ / / __|/ _ \ |    > <    | |
 | |_) | | | (_) \ V  V /\__ \  __/ |   / . \   | |
 |____/|_|  \___/ \_/\_/ |___/\___|_|  /_/ \_\  |_|2025
""")
        print(self.random_color() + f" Welcome to BrowseTXT — Local Time: {current_time}")
        print(" Commands: open <url>, link <number>, back, download <url>, exit\n")

    def fetch_page(self, url):
        now = time.time()
        if url in self.cache:
            timestamp, html = self.cache[url]
            if now - timestamp < self.CACHE_TTL:
                return html

        HEADERS = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 11.0; Win64; x64; rv:139.0) "
                "Gecko/20100101 Firefox/139.0"
            )
        }
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            html = response.text
            self.cache[url] = (now, html)
            if len(self.cache) > self.MAX_CACHE_SIZE:
                oldest = sorted(self.cache.items(), key=lambda x: x[1][0])[0][0]
                del self.cache[oldest]
            return html
        except requests.RequestException as e:
            print(Fore.RED + f"[Error] Unable to fetch the page: {e}")
            return None

    def display_page(self, html, base_url):
        soup = BeautifulSoup(html, "html.parser")

        for tag in soup(["script", "style", "header", "footer", "nav", "aside", "form"]):
            tag.decompose()

        title = soup.title.string.strip() if soup.title and soup.title.string else "No Title"
        print(Fore.CYAN + Style.BRIGHT + f"\n=== {title} ===\n")

        article = soup.find("article")
        if article:
            text = article.get_text(separator="\n", strip=True)
        else:
            main_div = soup.find(
                lambda tag: tag.name == "div" and (
                    (tag.get("id") and "content" in tag.get("id").lower()) or
                    (tag.get("class") and any(
                        "content" in c.lower() or "article" in c.lower() or "main" in c.lower()
                        for c in tag.get("class")
                    ))
                )
            )
            if main_div:
                text = main_div.get_text(separator="\n", strip=True)
            else:
                paragraphs = soup.find_all("p")
                texts = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]
                text = "\n\n".join(texts)

        # Get terminal width
        terminal_width = shutil.get_terminal_size().columns
        # Calculate 70% of the terminal width for wrapping
        wrap_width = int(terminal_width * 0.70)

        # Apply word wrapping and print
        wrapped_text = textwrap.fill(text, width=wrap_width)
        print(Style.NORMAL + wrapped_text + "\n")

        self.last_links = []
        links = soup.find_all("a", href=True)
        if links:
            print(Fore.YELLOW + "--- Links ---")
            for i, link in enumerate(links, 1):
                href = urljoin(base_url, link['href'])
                text_link = link.get_text(strip=True) or href
                print(self.random_color() + f"[{i}] {text_link} - {href}")
                self.last_links.append(href)
        else:
            print(Fore.YELLOW + "(No links found on this page)")

    def open_url(self, url):
        if not url.startswith("http"):
            url = "http://" + url

        html = self.fetch_page(url)
        if html:
            if self.current_url:
                self.history.append(self.current_url)
            self.current_url = url
            self.print_header()
            self.display_page(html, url)

    def follow_link(self, index):
        try:
            href = self.last_links[index - 1]
            self.open_url(href)
        except (IndexError, ValueError):
            print(Fore.RED + "Invalid link number.")

    def go_back(self):
        if not self.history:
            print(Fore.RED + "No previous page.")
            return
        self.current_url = self.history.pop()
        html = self.fetch_page(self.current_url)
        if html:
            self.print_header()
            self.display_page(html, self.current_url)

    def download_file(self, url):
        try:
            download_dir = Path.home() / "Downloads"
            filename = url.split("/")[-1] or "downloaded_file"
            filepath = download_dir / filename

            with requests.get(url, stream=True, timeout=15) as r:
                r.raise_for_status()
                total = int(r.headers.get("content-length", 0))
                downloaded = 0
                start = time.time()
                with open(filepath, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)
                            percent = downloaded * 100 // total if total else 0
                            elapsed = time.time() - start
                            speed = downloaded / elapsed if elapsed > 0 else 0
                            eta = (total - downloaded) / speed if speed > 0 else 0
                            sys.stdout.write(
                                f"\r{Fore.GREEN}Downloading {filename}... {percent}% "
                                f"[{downloaded // 1024} KB / {total // 1024} KB] "
                                f"ETA: {eta:.1f}s"
                            )
                            sys.stdout.flush()
            print(f"\n{Fore.CYAN}Download complete: {filepath}")
        except Exception as e:
            print(Fore.RED + f"[Download Error] {e}")

    def run(self):
        self.print_header()
        while True:
            try:
                command = input(Fore.WHITE + "\n>> ").strip()
            except (KeyboardInterrupt, EOFError):
                print(Fore.GREEN + "\nGoodbye!")
                break

            if command == "exit":
                print(Fore.GREEN + "Goodbye!")
                break
            elif command.startswith("open "):
                url = command.split(" ", 1)[1]
                self.open_url(url)
            elif command == "back":
                self.go_back()
            elif command.startswith("link "):
                try:
                    index = int(command.split(" ", 1)[1])
                    self.follow_link(index)
                except ValueError:
                    print(Fore.RED + "Please enter a valid number after 'link'.")
            elif command.startswith("download "):
                url = command.split(" ", 1)[1]
                self.download_file(url)
            else:
                print(Fore.RED + "Invalid command. Use: open <url>, link <number>, back, download <url>, exit")

if __name__ == "__main__":
    TextBrowser().run()