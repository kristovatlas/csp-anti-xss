#!/usr/bin/env python
"""A damn-vulnerable web page."""

import cgi


DEFAULT_SRC = "'none'"
OBJECT_SRC = "'none'"
SCRIPT_SRC = "'self'" #allow self-hosted scripts but not inline

def build_csp():
    """Returns CSP string using globals"""
    csp_str = 'Content-Security-Policy: '
    if DEFAULT_SRC is not None and DEFAULT_SRC:
        csp_str += 'default-src %s ;' % DEFAULT_SRC

    if OBJECT_SRC is not None and OBJECT_SRC:
        csp_str += 'object-src %s ;' % OBJECT_SRC

    if SCRIPT_SRC is not None and SCRIPT_SRC:
        csp_str += 'script-src %s ;' % SCRIPT_SRC

    return "%s" % csp_str

def print_headers(csp_str):
    """Prints HTTP response headers."""
    print "Content-type: text/html"
    print "%s" % csp_str
    print "\n" #terminate headers

def _main():
    """Main function"""
    csp_str = build_csp()
    print_headers(csp_str)

    print "<HTML><HEAD><TITLE>XSSMAKER</TITLE></HEAD><BODY>"
    args = cgi.FieldStorage()
    keys = args.keys()

    if len(keys) == 0:
        print "<DIV>No paramters specified.</DIV>"
    else:
        print "<DIV>"
        for key in keys:
            print "%s=%s\n" % (key, args[key].value)
        print "</DIV>"

    print "</BODY></HTML>"

if __name__ == '__main__':
    _main()
