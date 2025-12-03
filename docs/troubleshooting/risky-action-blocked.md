# Risky action blocked

## Situation

Working with Attack Surface Reduction (ASR) rules can cause Windows to block KONNEKT performing some of it's main actions.

{% embed url="https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference" %}

## Problem

Without exclusion KONNEKT crashes when trying to open or preview an Office file e.g. Word, Excel or PowerPoint.

In this case check for entries under Windows Security / Protection History:

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

## Solution

Exclude KONNEKT from the ASR rule "Office Child Process":

"C:\Program Files\Konnekt\Konnekt.exe"

"C:\Program Files\Konnekt\KonnektStarter.exe"

{% embed url="https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference#block-all-office-applications-from-creating-child-processes" %}
