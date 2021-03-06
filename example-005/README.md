## Description

A web application vulnerable to reflected XSS via the use of DOM-reading scripts that fail to validate DOM contents.

## Requirements

* Python 2
* [CGIHTTPServer](https://docs.python.org/2.7/library/cgihttpserver.html)


## Usage

### Starting the server

```
$ chmod -R +x *.py #make the Python web pages executable
$ python -m CGIHTTPServer 8000
```

### Configuring your browser

You will need to bypass or disable the XSS filtering features in your browser. Disabling is easier. (Don't forget to enable it when you're done.)

Firefox:
1. Go to the location `about:config` in the URL.
2. Find the attribute `browser.urlbarfilter.javascript` and set it to `false`.

### Viewing in your browser

Visit http://127.0.0.1:8000/

This will redirect you automatically to http://127.0.0.1:8000/cgi-bin/xssmaker.py

You can add GET parameters in the URL to reflect XSS. For example:

    http://127.0.0.1:8000/cgi-bin/xssmaker.py?a=%3CINPUT%20id=%22cmd%22%20value=%22alert,1337%22%3E

### Output

In Firefox 48: An alert box is displayed showing '1337'.
