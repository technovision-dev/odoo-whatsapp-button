# Installation

* **Module:** `technovision_whatsapp_button`
* **Odoo:** 18.0, Community or Enterprise
* **Depends on:** `base` only
* **Extra Python:** none

## Install

1. Copy the module into your addons path.

   ```bash
   cp -r technovision_whatsapp_button /opt/odoo/custom/
   ```

2. Restart Odoo.

   ```bash
   sudo systemctl restart odoo
   ```

3. **Apps -> Update Apps List**, search for *Simple WhatsApp Button*, install.

## Check the install worked

Open any contact with a mobile number in international form. A **WhatsApp**
button appears next to the number.

If it does not appear, the number is not usable - see CONFIGURATION for what
counts as usable and why the button hides rather than guessing.

## Configuration

None. There is nothing to configure, which is deliberate.

## Uninstalling

Clean. The module adds one computed field, which is not stored, and one view
inheritance. Nothing is left behind.
