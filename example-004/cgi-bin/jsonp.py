#!/usr/bin/env python
"""A damn-vulnerable JSONP endpoint.
It simply feeds the string 'bob' to the specified callback function.
http://stackoverflow.com/questions/2067472/what-is-jsonp-all-about

This will be accessible via:
http://myvulnerablethirdpartydomain.com/cgi-bin/jsonp.py?callback=foo
"""

import cgi


DEFAULT_SRC = "'none'"
OBJECT_SRC = "'none'"
SCRIPT_SRC = "'none'"

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
    print "Content-type: application/javascript"
    print "%s" % csp_str
    print "\n" #terminate headers

def _main():
    """Main function"""
    csp_str = build_csp()
    print_headers(csp_str)

    args = cgi.FieldStorage()
    keys = args.keys()

    if len(keys) == 0 or 'callback' not in keys:
        print "console.log('No callback provided to jsonp.py.');"
    else:
        print "%s('bob');" % args['callback'].value

if __name__ == '__main__':
    _main()
