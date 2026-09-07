# -*- coding: utf-8 -*-
{
    "name": "Free WhatsApp Button for Contacts",
    "version": "18.0.1.0.1",
    "category": "Productivity",
    "summary": "Free WhatsApp button for Odoo contacts: open a WhatsApp chat "
               "from any contact or customer with the number already formatted. "
               "No API key, no account.",
    "description": """
The smallest useful thing.

A button on every contact that opens WhatsApp with that person's number
already filled in - on wa.me, so it works in the desktop app, in WhatsApp Web
and on a phone, with no configuration and no account of any kind.

Why this is not trivial
-----------------------

The number is the problem. WhatsApp needs it in international form with no
spaces, brackets, dashes or leading zeros, and almost no address book stores
it that way. This module reads Mobile, falls back to Phone, applies the
contact's country dialling code when the number is written nationally, and
refuses to show the button at all when the result would not be a valid
number - because a button that opens a chat with the wrong person is worse
than no button.

Free, and built like a paid one
-------------------------------

No account, no API key, no outbound connection, nothing recorded. The number
is turned into a link in the browser; Odoo never contacts WhatsApp.

It is free because it is the smallest end of something larger, not because it
is a demo. It ships the same documentation and the same tests as the paid
modules in the suite.

If you need to send a message from Odoo rather than open a chat - templates,
delivery status, retries, a log of what was sent - that is
TechnoVision WhatsApp Core, and this module is deliberately not a cut-down
version of it.
    """,
    "author": "TechnoVision",
    "maintainer": "TechnoVision",
    "website": "https://technovision.dev",
    "support": "info@technovision.dev",
    # LGPL-3 rather than OPL-1: this is the free tier, it is published on
    # GitHub, and a free module under a proprietary licence is a free module
    # nobody can read, fork or trust.
    "license": "LGPL-3",
    "images": ["static/description/banner.png"],
    "icon": "static/description/icon.png",
    "depends": ["base"],
    "data": [
        "views/res_partner_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
