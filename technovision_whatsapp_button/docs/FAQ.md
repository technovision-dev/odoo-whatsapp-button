# FAQ

**Do I need a WhatsApp Business account?**
No. Nothing here talks to WhatsApp at all.

**Does it cost anything to run?**
No. There is no API, no message fee and no account.

**Why is the button missing on some contacts?**
The number is not usable. Most often it is a national number on a contact with
no country set, so there is no way to tell which country code to apply.
Setting the country makes the button appear.

**Can it send a message automatically?**
No, and it never will. Opening a chat is a person clicking a link. Sending
from Odoo needs the WhatsApp Business API and is a different module.

**Does it work on mobile?**
Yes. `wa.me` is WhatsApp's own link format and it resolves to the app on a
phone, the desktop client where one is installed, and WhatsApp Web otherwise.

**Does anything leave my Odoo?**
No. The link is built in Python and followed by the browser when somebody
clicks. Odoo makes no outbound connection.

**Is it really free, or is it a trial?**
Free, LGPL-3, and the source is readable. It is the smallest end of a larger
suite; it is not a demo of one.

**Why LGPL-3 when your other modules are OPL-1?**
Because a free module under a proprietary licence is a free module nobody can
read, fork or trust.
