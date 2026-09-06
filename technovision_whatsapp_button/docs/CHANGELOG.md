# Changelog

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and
the version numbering is Odoo's own.

## [18.0.1.0.0] - 2026-09-06

First release.

### Added

* A **WhatsApp** button next to the number on the contact form, opening
  `wa.me` with the number in the form WhatsApp accepts.
* Number handling that reads Mobile then Phone, strips formatting, converts a
  `00` prefix, and applies the contact's country dialling code to a number
  written nationally.
* **The button is hidden when the number is not usable**, rather than
  producing a link that opens a chat with the wrong person.
* 18 automated tests, most of them about the cases where no link should be
  produced.
