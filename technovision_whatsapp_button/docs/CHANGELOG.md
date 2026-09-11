# Changelog

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and
the version numbering is Odoo's own.

## [18.0.1.0.2] - 2026-09-11

### Added

* **An About panel under Settings**, and nothing anywhere else. It says what
  this module does and does not do, and compares it with the paid two-way
  module for anyone who needs receiving, automatic replies, order lookups or
  payment links.

  Where it lives is the whole design. It is a section of Settings, reached only
  by deliberately opening Settings. There is no banner on the contact form, no
  dialog on install, no notification, and nothing that appears while somebody
  is doing their job. A free module that advertises at you during work is a
  free module people uninstall.

  **Nothing is transmitted.** No ping, no version check, no install count, no
  identifier, no outbound request of any kind. The only attribution is a
  `utm_source` on the links themselves, which the destination sees if — and
  only if — a person chooses to click one. That is a link, not telemetry.

  The button itself is unchanged and still free. Nothing here gates a feature
  or degrades one.

### Changed

* Depends on `base_setup` as well as `base`. It is part of every standard Odoo
  installation, and the About panel is the only thing that needs it.

## [18.0.1.0.1] - 2026-09-06

### Changed

* **The Odoo Apps Store listing now has a face.** Banner, icon and a
  description page in the same house style as the paid modules, with three
  screenshots — a number already international, a national number with the
  country set, and one that is not usable, where the button correctly is not
  there. A listing with no image beside nine that have one reads as abandoned.

---

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
