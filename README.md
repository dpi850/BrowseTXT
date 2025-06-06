BrowseTXT: A Command-Line Text Browser

A minimalist, yet powerful, command-line text browser for efficient web content consumption directly from your terminal.

Built With

BrowseTXT leverages the power of Python and a few robust libraries:

    Python 3.x

    Requests - For making HTTP requests.

    Beautiful Soup 4 - For parsing HTML and XML documents.

    Colorama - For cross-platform colored terminal output.

Getting Started

Commands:

    open <url>: Opens the specified URL. BrowseTXT will attempt to add http:// if no scheme is provided.

        Example: open example.com

        Example: open https://www.google.com/search?q=text+browser

    link <number>: Follows the link corresponding to the given number, as listed at the bottom of each page.

        Example: link 3

    back: Navigates back to the previously visited page in your browsing history.

    download <url>: Downloads the file from the specified URL to your system's default Downloads directory.

        Example: download https://www.iana.org/_downloads/iana-domains-examples-1.pdf

    exit: Exits the browser application.


Screenshots

![Capture444](https://github.com/user-attachments/assets/5c15e2de-0576-4e8e-9e44-8039c8215a88)

![Capture444333](https://github.com/user-attachments/assets/9031c934-d754-4341-ac2f-e5a37ea953ed)

![Capture44444444](https://github.com/user-attachments/assets/5d970671-d3e0-4271-9cc2-5fe4bbe814d3)

![Capture444444446666666666](https://github.com/user-attachments/assets/54bf075e-fb09-4e8e-91f2-c66de526f3a5)
