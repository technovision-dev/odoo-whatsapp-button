# -*- coding: utf-8 -*-
# Copyright 2026 TechnoVision
# License LGPL-3 (see LICENSE file for full licensing details).
"""A wa.me link for a contact.

Everything here is one small problem done properly: turning what is in an
address book into what WhatsApp will accept.

The module makes no outbound connection. The link is built in Python and
followed by the browser, so Odoo never talks to WhatsApp and nothing about the
contact leaves the instance until a person clicks.
"""
import re

from odoo import api, fields, models

#: Anything that is not a digit or a leading plus.
_NOT_NUMBER = re.compile(r"[^\d+]")

#: wa.me wants digits only - no plus, no spaces, no punctuation.
WA_ME = "https://wa.me/%s"


class ResPartner(models.Model):
    _inherit = "res.partner"

    whatsapp_link = fields.Char(
        compute="_compute_whatsapp_link",
        help="Opens WhatsApp with this contact's number. Empty when the "
             "number is not usable, which is why the button disappears "
             "rather than opening the wrong chat.",
    )

    @api.depends("mobile", "phone", "country_id")
    def _compute_whatsapp_link(self):
        for partner in self:
            number = self._whatsapp_e164(
                partner.mobile or partner.phone, partner.country_id
            )
            partner.whatsapp_link = (
                WA_ME % number.lstrip("+") if self._whatsapp_valid(number) else False
            )

    # ------------------------------------------------------------------
    @api.model
    def _whatsapp_e164(self, raw, country=None):
        """Best-effort international form.

        Conservative on purpose. It strips formatting, converts a `00` prefix,
        and applies the contact's dialling code to a number written
        nationally. Where it cannot tell, it leaves the number alone and the
        validity check rejects it - a button that does nothing is better than
        a button that opens a conversation with a stranger.
        """
        if not raw:
            return ""
        number = _NOT_NUMBER.sub("", raw.strip())
        if not number:
            return ""
        if number.startswith("+"):
            return "+" + number[1:].replace("+", "")
        if number.startswith("00"):
            return "+" + number[2:]
        code = country and country.phone_code
        if code:
            return "+%s%s" % (code, number.lstrip("0"))
        return number

    @api.model
    def _whatsapp_valid(self, number):
        """E.164: a plus and between 8 and 15 digits."""
        return bool(number) and bool(re.fullmatch(r"\+\d{8,15}", number))

    # ------------------------------------------------------------------
    def action_open_whatsapp(self):
        self.ensure_one()
        if not self.whatsapp_link:
            return False
        return {
            "type": "ir.actions.act_url",
            "url": self.whatsapp_link,
            "target": "new",
        }
