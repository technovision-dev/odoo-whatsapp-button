# Simple WhatsApp Button for Odoo

A WhatsApp button on the contact form that opens the chat with the number
already correct.

**Free. No account, no API key, no configuration, and no outbound connection
from Odoo.**

| | |
|---|---|
| **Technical name** | `technovision_whatsapp_button` |
| **Odoo** | 18.0, Community or Enterprise |
| **Depends on** | `base` only |
| **Licence** | LGPL-3 |
| **Tests** | 18, all passing on Odoo 18 |
| **Maintainer** | [TechnoVision](https://technovision.dev) |

---

## What it does

Adds a **WhatsApp** button next to the number on every contact. Clicking it
opens WhatsApp — the desktop app, WhatsApp Web or the phone, whichever the
browser hands it to — with that person's number already filled in.

## Why it is not trivial

The number is the problem. WhatsApp needs it in international form with no
spaces, brackets, dashes or leading zeros, and almost no address book stores it
that way.

This module reads **Mobile**, falls back to **Phone**, strips formatting,
converts a `00` prefix, and applies the contact's **country** dialling code
when the number is written nationally.

And when the result would not be a valid number, **the button does not appear
at all**:

| On the contact | Button | Why |
|---|---|---|
| `+20 123 456 7890` | ✅ | already international |
| `00201234567890` | ✅ | `00` is the international prefix |
| `01234567890` **with a country set** | ✅ | the dialling code is applied, the leading zero dropped |
| `01234567890` with **no country** | ❌ | no way to know which country. Guessing opens a chat with a stranger. |
| `+2012` | ❌ | too short to be a number |
| `+20 123 456 7890 ext 12` | ❌ | an extension is not part of the number |
| `call the office` | ❌ | not a number |

**A button that does nothing is better than a button that opens the wrong
conversation.** That single decision is most of what this module is.

## Install

```bash
cp -r technovision_whatsapp_button /opt/odoo/custom/
sudo systemctl restart odoo
```

Then **Apps → Update Apps List**, search for *Simple WhatsApp Button*, install.
There is nothing to configure.

## Tests

```bash
odoo-bin -d <database> -i technovision_whatsapp_button \
    --test-enable --test-tags /technovision_whatsapp_button --stop-after-init
```

18 tests. Most of them are about the cases where **no** link should be
produced, because that is where this kind of module actually goes wrong.

## Privacy

Nothing leaves your Odoo. The link is built in Python and rendered into the
page; the browser only goes to `wa.me` when a person clicks. No account, no
API, no telemetry, and nothing recorded.

## Documentation

In [`technovision_whatsapp_button/docs/`](technovision_whatsapp_button/docs) —
installation, configuration, user guide, FAQ, troubleshooting, security model,
test report and changelog. The same set the paid modules ship, because a free
module is the first evidence anyone has about how the paid ones are written.

## If you need to *send* from Odoo

Templates, delivery status, retries and a log of what was sent are
**TechnoVision WhatsApp Core**, a paid module. This one is deliberately **not**
a cut-down version of it — it is a different thing that happens to share a
name. See [technovision.dev/products](https://technovision.dev/products).

## Contributing

Issues and pull requests welcome. A bug here is evidence about the whole
catalogue, so it is treated the same as one in a paid module.

## Licence

LGPL-3. Full text in [LICENSE](LICENSE); the GPL-3 text it incorporates is in
[COPYING](COPYING).

Copyright 2026 TechnoVision.
