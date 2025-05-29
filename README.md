# BrowseTXT

A lightweight, command-line web browser designed for efficient text-based Browse and navigation. `BrowseTXT` fetches web pages, strips away distractions, and presents the core textual content and navigable links directly in your terminal. It also includes basic history and file download capabilities.

## Table of Contents

* [About BrowseTXT](#about-browsetxt)
* [Features](#features)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [Usage](#usage)
* [License](#license)
* [Contact](#contact)

## About BrowseTXT

`BrowseTXT` is a terminal-based web browser built for simplicity and efficiency. Instead of rendering complex web pages with images, videos, and scripts, it focuses on delivering the essential text content. This makes it ideal for quickly reading articles, documentation, or navigating through websites without the overhead of a full graphical browser. It intelligently extracts main content, removes extraneous elements like headers, footers, and scripts, and allows you to follow links and download files directly from your command line.

## Features

* **Text-focused Browse:** Strips out non-essential elements (scripts, styles, headers, footers, navigation, forms, asides) to provide a clean text view of web pages.
* **Intelligent Content Extraction:** Prioritizes `article` tags, content-related `div` elements, or `p` tags to find the main body of the text.
* **Terminal Integration:** Displays content directly in your terminal, wrapping text to 70% of your terminal's width for readability.
* **Link Navigation:** Automatically lists all accessible links on a page with numbered indices, allowing easy navigation using the `link <number>` command.
* **Navigation History:** Go back to previously visited pages using the `back` command.
* **File Downloading:** Download files directly to your system's `Downloads` directory with a progress indicator using the `download <url>` command.
* **Page Caching:** Caches recently visited pages for faster re-loading (5-minute TTL, max 10 pages).
* **User-Agent Spoofing:** Uses a common Firefox User-Agent to improve compatibility with websites.
* **Colorized Output:** Enhances readability with random color headers and distinct styling for links and messages using `colorama`.

## Getting Started

Follow these instructions to get `BrowseTXT` up and running on your local machine.

### Prerequisites

* Python 3.x (Tested with Python 3.8+)
* `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/dpi850/BrowseTXT.git](https://github.com/dpi850/BrowseTXT.git)
    cd BrowseTXT
    ```

2.  **Install dependencies:**
    `BrowseTXT` relies on a few Python libraries. You can install them using pip:
    ```bash
    pip install requests beautifulsoup4 colorama
    ```
    (Or, if you create a `requirements.txt` file from the above: `pip install -r requirements.txt`)

### Usage

To start `BrowseTXT`, simply run the Python script:

```bash
python browsetxt.py

Here's the README.md content formatted for GitHub Markdown:
Markdown

# BrowseTXT

![BrowseTXT Banner (Optional - You can add an ASCII art banner or a relevant image here, e.g., a console screenshot)](https://via.placeholder.com/800x200?text=BrowseTXT+-+Terminal+Web+Browser)

A lightweight, command-line web browser designed for efficient text-based Browse and navigation. `BrowseTXT` fetches web pages, strips away distractions, and presents the core textual content and navigable links directly in your terminal. It also includes basic history and file download capabilities.

## Table of Contents

* [About BrowseTXT](#about-browsetxt)
* [Features](#features)
* [Getting Started](#getting-started)
    * [Prerequisites](#prerequisites)
    * [Installation](#installation)
    * [Usage](#usage)
* [Screenshots/Demo](#screenshotsdemo)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)

## About BrowseTXT

`BrowseTXT` is a terminal-based web browser built for simplicity and efficiency. Instead of rendering complex web pages with images, videos, and scripts, it focuses on delivering the essential text content. This makes it ideal for quickly reading articles, documentation, or navigating through websites without the overhead of a full graphical browser. It intelligently extracts main content, removes extraneous elements like headers, footers, and scripts, and allows you to follow links and download files directly from your command line.

## Features

* **Text-focused Browse:** Strips out non-essential elements (scripts, styles, headers, footers, navigation, forms, asides) to provide a clean text view of web pages.
* **Intelligent Content Extraction:** Prioritizes `article` tags, content-related `div` elements, or `p` tags to find the main body of the text.
* **Terminal Integration:** Displays content directly in your terminal, wrapping text to 70% of your terminal's width for readability.
* **Link Navigation:** Automatically lists all accessible links on a page with numbered indices, allowing easy navigation using the `link <number>` command.
* **Navigation History:** Go back to previously visited pages using the `back` command.
* **File Downloading:** Download files directly to your system's `Downloads` directory with a progress indicator using the `download <url>` command.
* **Page Caching:** Caches recently visited pages for faster re-loading (5-minute TTL, max 10 pages).
* **User-Agent Spoofing:** Uses a common Firefox User-Agent to improve compatibility with websites.
* **Colorized Output:** Enhances readability with random color headers and distinct styling for links and messages using `colorama`.

## Getting Started

Follow these instructions to get `BrowseTXT` up and running on your local machine.

### Prerequisites

* Python 3.x (Tested with Python 3.8+)
* `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/dpi850/BrowseTXT.git](https://github.com/dpi850/BrowseTXT.git)
    cd BrowseTXT
    ```

2.  **Install dependencies:**
    `BrowseTXT` relies on a few Python libraries. You can install them using pip:
    ```bash
    pip install requests beautifulsoup4 colorama
    ```
    (Or, if you create a `requirements.txt` file from the above: `pip install -r requirements.txt`)

### Usage

To start `BrowseTXT`, simply run the Python script:

```bash
python browsetxt.py

Once running, you'll see a welcome header and a >> prompt. Here are the available commands:

    open <url>: Opens and displays the content of the specified URL. You can omit http:// or https://.
    Bash

>> open example.com
>> open [https://www.google.com/search?q=github](https://www.google.com/search?q=github)

link <number>: Follows a link displayed on the current page, using its assigned number.
Bash

>> link 5

back: Navigates back to the previously viewed page in your history.
Bash

>> back

download <url>: Downloads a file from the given URL to your system's Downloads directory.
Bash

>> download [https://example.com/some_file.zip](https://example.com/some_file.zip)

exit: Closes BrowseTXT.
Bash

    >> exit

Here's an example of what BrowseTXT output looks like:

  ____                          _________   _________
 |  _ \                        |__   __\ \ / /__   __|
 | |_) |_ __ _____      _____  ___| |   \ V /   | |
 |  _ <| '__/ _ \ \ /\ / / __|/ _ \ |    > <    | |
 | |_) | | | (_) \ V  V /\__ \  __/ |   / . \   | |
 |____/|_|  \___/ \_/\_/ |___/\___|_|  /_/ \_\  |_|2025
 Welcome to BrowseTXT — Local Time: 2025-05-29 12:30:00
 Commands: open <url>, link <number>, back, download <url>, exit

=== Example Domain ===

Example Domain

This domain is for use in illustrative examples in documents.
You may use this domain in examples without prior coordination or asking for permission.

--- Links ---
[1] More information... - [http://www.iana.org/domains/example](http://www.iana.org/domains/example)

>> open google.com
