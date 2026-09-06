# Configuration

There is none, and that is the point of the module.

What decides whether the button appears is the number on the contact.

## Which number is used

**Mobile**, and **Phone** when there is no mobile.

## What counts as usable

WhatsApp needs a number in international form: a country code followed by the
national number, with no spaces, brackets, dashes or leading zero.

The module accepts:

| On the contact | Becomes | Why |
|---|---|---|
| `+20 123 456 7890` | `+201234567890` | formatting removed |
| `00201234567890` | `+201234567890` | `00` is the international prefix |
| `01234567890` **with the country set to Egypt** | `+201234567890` | the country's dialling code is applied and the leading zero dropped |

It refuses:

| On the contact | Why |
|---|---|
| `01234567890` with **no country** | there is no way to know which country. Guessing opens a chat with a stranger. |
| `+2012` | too short to be a number |
| `call the office` | not a number |
| `+20 123 456 7890 ext 12` | an extension is not part of the number, and appending it dials the wrong one |

**When the number is not usable the button does not appear.** That is the
design: a button that does nothing is better than a button that opens the
wrong conversation.

## Making the button appear for a national number

Set the contact's **Country**. That is the single piece of information the
module needs, and it is a field you already have.
