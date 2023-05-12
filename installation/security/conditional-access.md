# Conditional Access

If you use [Azure AD Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview), you are of course also controlling the access of KONNEKT to your Microsoft 365 resources.

KONNEKT is using different APIs to connect to Microsoft 365. Therefore, it is necessary to configure the corresponding Conditional Access policies to **"All cloud apps"**.&#x20;

It is **not** enough to just select the app "KONNEKT".

<figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Make sure, to [grant tenant-wide admin](grant-admin-consent-in-enterprise-applications.md) consent first. Without this, KONNEKT will not be part of "All cloud apps".
{% endhint %}
