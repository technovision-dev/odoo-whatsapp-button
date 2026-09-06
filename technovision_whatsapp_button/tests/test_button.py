# -*- coding: utf-8 -*-
# Copyright 2026 TechnoVision
# License LGPL-3 (see LICENSE file for full licensing details).
"""The number handling, which is the whole module.

A free module is the first thing a prospective buyer installs, so it is the
first evidence they have about how the paid ones are written. These tests are
here for that reason as much as for the code.
"""
from odoo.tests import tagged
from odoo.tests.common import TransactionCase


@tagged("post_install", "-at_install")
class TestWhatsAppButton(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.Partner = cls.env["res.partner"]
        cls.egypt = cls.env.ref("base.eg")

    def partner(self, **values):
        return self.Partner.create(dict({"name": "Test"}, **values))

    # ------------------------------------------------------------- the link
    def test_an_international_mobile_gives_a_link(self):
        partner = self.partner(mobile="+201234567890")
        self.assertEqual(partner.whatsapp_link, "https://wa.me/201234567890")

    def test_formatting_is_removed(self):
        partner = self.partner(mobile="+20 (123) 456-7890")
        self.assertEqual(partner.whatsapp_link, "https://wa.me/201234567890")

    def test_a_double_zero_prefix_is_converted(self):
        partner = self.partner(mobile="00201234567890")
        self.assertEqual(partner.whatsapp_link, "https://wa.me/201234567890")

    def test_a_national_number_uses_the_country_code(self):
        partner = self.partner(mobile="01234567890", country_id=self.egypt.id)
        self.assertEqual(partner.whatsapp_link, "https://wa.me/201234567890")

    def test_mobile_wins_over_phone(self):
        partner = self.partner(mobile="+201111111111", phone="+202222222222")
        self.assertEqual(partner.whatsapp_link, "https://wa.me/201111111111")

    def test_phone_is_used_when_there_is_no_mobile(self):
        partner = self.partner(phone="+202222222222")
        self.assertEqual(partner.whatsapp_link, "https://wa.me/202222222222")

    # ------------------------------------------------------- no false links
    def test_no_number_means_no_link(self):
        self.assertFalse(self.partner().whatsapp_link)

    def test_a_national_number_without_a_country_gives_no_link(self):
        # Guessing the country here is how a chat opens with a stranger.
        partner = self.partner(mobile="01234567890")
        self.assertFalse(partner.whatsapp_link)

    def test_too_short_is_not_a_number(self):
        self.assertFalse(self.partner(mobile="+2012").whatsapp_link)

    def test_too_long_is_not_a_number(self):
        self.assertFalse(self.partner(mobile="+20123456789012345").whatsapp_link)

    def test_letters_give_no_link(self):
        self.assertFalse(self.partner(mobile="call the office").whatsapp_link)

    def test_an_extension_is_not_silently_dialled(self):
        # "+20 123 456 7890 ext 12" must not become +201234567890 12.
        partner = self.partner(mobile="+20 123 456 7890 ext 12")
        self.assertNotEqual(partner.whatsapp_link, "https://wa.me/201234567890")

    # ---------------------------------------------------------- the action
    def test_the_action_opens_the_link(self):
        partner = self.partner(mobile="+201234567890")
        action = partner.action_open_whatsapp()
        self.assertEqual(action["type"], "ir.actions.act_url")
        self.assertEqual(action["url"], "https://wa.me/201234567890")
        self.assertEqual(action["target"], "new")

    def test_the_action_does_nothing_without_a_number(self):
        self.assertFalse(self.partner().action_open_whatsapp())

    # -------------------------------------------------------------- recompute
    def test_the_link_follows_the_number(self):
        partner = self.partner(mobile="+201111111111")
        partner.mobile = "+202222222222"
        self.assertEqual(partner.whatsapp_link, "https://wa.me/202222222222")

    def test_the_link_follows_the_country(self):
        partner = self.partner(mobile="01234567890")
        self.assertFalse(partner.whatsapp_link)
        partner.country_id = self.egypt
        self.assertEqual(partner.whatsapp_link, "https://wa.me/201234567890")
