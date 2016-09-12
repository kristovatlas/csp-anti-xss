## Description

This repo contains some rules for creating a CSP header that is effective at mitigating CSP, as well as some standalone sample web servers that show how bad headers can fail to mitigate.

Keep in mind that Content-Security-Policy is **not** a thorough security control, but is rather a partial mitigation that kicks in when developers fail to validate input and/or encode output.

## Rules

1. The policy must define both the `script-src` and `object-src` directives. You can use `default-src` as a fallback in their absence. A good idea is to begin your CSP header with `default-src 'none'`. <sup>1</sup>
2. The `script-src` directive cannot contain `unsafe-inline`. <sup>1</sup> See [example-001](example-001) for a reflected XSS that is blocked by the lack of `unsafe-inline` and [example-002](example-002) for a reflected XSS that is allowed because of `unsafe-inline`.

## References:
<sup>1</sup>: [CSP Is Dead, Long Live CSP! On the Insecurity of Whitelists and the Future of Content Security Policy](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45542.pdf)
