# Troubleshooting

## The button is not there

The number is not usable. Check, in order:

1. Is there a number in **Mobile** or **Phone**?
2. Is it in international form (`+20...`)?
3. If it is national (`0123...`), is the contact's **Country** set?
4. Does it contain an extension, a second number, or a note? Those are not
   numbers, and the module will not try to extract one.

## The button opens WhatsApp with the wrong number

Look at the contact. The module uses Mobile first, then Phone, and shows the
number it built in the link itself - hover the button. If the number on the
contact is right and the link is wrong, that is a bug: send both to
info@technovision.dev.

## WhatsApp says the number is not registered

The number is valid but the person is not on WhatsApp, or the number in your
address book is out of date. Nothing in Odoo can tell you that in advance -
only WhatsApp knows.

## It opens WhatsApp Web instead of the app

That is the browser's choice, not Odoo's. `wa.me` hands off to whichever
WhatsApp client the machine is set up to use.

## The button appears but nothing happens

A pop-up blocker. The button opens a new tab.
