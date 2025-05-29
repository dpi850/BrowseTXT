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



    Example Session:

  ____                          _________   _________
 |  _ \                        |__   __\ \ / /__   __|
 | |_) |_ __ _____      _____  ___| |   \ V /   | |
 |  _ <| '__/ _ \\ \\ /\\ / / __|/ _ \\ |    > <    | |
 | |_) | | | (_) \\ V  V /\\__ \\  __/ |   / . \\   | |
 |____/|_|  \\___/ \\_/\_/ |___/\\___|_|  /_/ \\_\\  |_|2025

 Welcome to BrowseTXT — Local Time: 2025-05-29 13:22:41
 Commands: open <url>, link <number>, back, download <url>, exit

>> open example.com

=== Example Domain ===

This domain is for use in illustrative examples in documents. You may use this
domain in examples without prior coordination or asking for permission.

--- Links ---
[1] More information... - https://www.iana.org/domains/example

>> link 1

=== Example Domains ===

Example domains are intended for use in documentation and examples.
These domains are not available for registration.

--- Links ---
[1] Home - https://www.iana.org/
[2] About - https://www.iana.org/about
[3] Contact Us - https://www.iana.org/contact

>> back

=== Example Domain ===

This domain is for use in illustrative examples in documents. You may use this
domain in examples without prior coordination or asking for permission.

--- Links ---
[1] More information... - https://www.iana.org/domains/example

>> exit
Goodbye!


