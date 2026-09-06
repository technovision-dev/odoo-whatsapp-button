# Test report

* **Module:** `technovision_whatsapp_button` 18.0.1.0.0
* **Tests:** 18 in 1 file
* **Result:** 0 failed, 0 errors
* **Run on:** Odoo 18.0, PostgreSQL, with demo data

```bash
odoo-bin -d <database> -i technovision_whatsapp_button \
    --test-enable --test-tags /technovision_whatsapp_button --stop-after-init
```

## What is covered

Number handling, which is the whole module:

* international numbers, formatting stripped, `00` prefixes converted
* national numbers with the contact's country applied
* Mobile preferred over Phone, Phone used when there is no Mobile
* the link recomputing when the number or the country changes
* the action returning the right URL and target

And, at least as important, every case where it **refuses** to produce a link:
no number, a national number with no country, too short, too long, letters,
and a number with an extension appended.

## Why a free module has a test report

Because a free module is the first thing a prospective buyer installs, and it
is therefore the first evidence they have about how the paid ones are written.
