# -*- coding: utf-8 -*-
{
    "name": "WhatsApp Button for Contacts",
    "version": "18.0.1.0.6",
    "category": "Productivity",
    "summary": "WhatsApp button for Odoo contacts: open a WhatsApp chat "
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

Built properly
--------------

No account, no API key, no outbound connection, nothing recorded. The number
is turned into a link in the browser; Odoo never contacts WhatsApp.

It is the smallest end of something larger, not a demo. It ships the same
documentation and the same tests as the other modules in the suite.

If you want Odoo to send and answer WhatsApp messages rather than open a
chat by hand - two-way messaging on the official Meta Cloud API, order and
invoice lookups, payment links and human handover - that is TechnoVision
WhatsApp Sales and Payment Automation. This module is complete
on its own; it is not a trial of that one.
    """,
    "author": "TechnoVision",
    "maintainer": "TechnoVision",
    "website": "https://technovision.dev",
    "support": "info@technovision.dev",
    # OPL-1 from 9 Oct 2026, when the module became paid. Versions published
    # before that stay LGPL-3 for whoever already has them.
    "price": 20.00,
    "currency": "USD",
    "license": "OPL-1",
    "images": ["static/description/banner.png"],
    "icon": "static/description/icon.png",
    # base_setup provides res_config_settings_view_form, which the About
    # panel extends. It is part of every standard Odoo installation, and the
    # panel is the only thing that needs it.
    "depends": ["base", "base_setup"],
    "data": [
        "views/res_partner_views.xml",
        "views/res_config_settings_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
