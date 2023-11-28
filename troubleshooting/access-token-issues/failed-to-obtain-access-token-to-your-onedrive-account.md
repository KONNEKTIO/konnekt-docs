# Failed to obtain access token to your OneDrive account

{% hint style="info" %}
Can appear in KONNEKT 2.9.0 and higher.
{% endhint %}

### Problem

When trying to log in to KONNEKT, the error message "Failed to obtain an access token to your OneDrive account" appears.

<figure><img src="../../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

### Cause

If you see this error, please check the Sign-in logs in Azure/EntraID to see if there are any failed sign- ins.

Take a look at the active and interactive Sign-ins.

<figure><img src="../../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>

Check the "Device info" under Activity Details: Sign-ins

<figure><img src="../../.gitbook/assets/image (32).png" alt=""><figcaption></figcaption></figure>

### Solution

This issue can be solved by changing the [browser engine](../../configuration/system-settings/authentication-browser-engine.md) to authenticate the user.

