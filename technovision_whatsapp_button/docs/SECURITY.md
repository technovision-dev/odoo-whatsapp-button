# Security model

## What it reads

`res.partner`: **Mobile**, **Phone** and **Country**. Nothing else.

## What it writes

Nothing. The link is a non-stored computed field.

## What leaves your instance

**Nothing.** The module makes no outbound connection of any kind. The link is
built in Python and rendered into the page; it is followed by the browser only
when a person clicks it, and at that point the browser goes to `wa.me` - which
is a normal outbound link, the same as any other on a web page.

## Access control

None of its own. Anyone who can see a contact can see the button, because
anyone who can see the contact can already see the phone number the button is
built from.

## Personal data

No new personal data is stored, and no processing happens on it. The number is
already in your database; the module reformats it for display.
