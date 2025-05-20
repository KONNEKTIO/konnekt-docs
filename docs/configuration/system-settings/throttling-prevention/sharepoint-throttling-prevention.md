# SharePoint throttling prevention

{% hint style="info" %}
This feature is available in KONNEKT 2.2 or newer
{% endhint %}

This "[update frequency control](sharepoint-throttling-prevention.md)" policy limits fka as "SharePoint throttling prevention" requests by enhanced refresh cycles e.g. updating the users Site Collections.

## Policy

You can load this policy in Policy Editor or Intune with our [ADMX](../../management-options/settings-via-gpo.md#admx-file).

Policy Name (GPO & Intune): `Sharepoint Throttling Prevention`

Available settings:

* `Enabled`
  * `Autodetect` (default)\
    KONNEKT will decide on active measures.
  * `Low`\
    Throttling prevention takes place in case of throttling events, only.
  * `Medium`\
    More data is cached than in Low to prevent unnecessary requests to SharePoint Online.
  * `High`\
    Throttling prevention has the highest priority. Some changes from other clients (e.g. new libraries or new files/folders) may be updated late (up to 24 hours).
* `Disabled`\
  Default Throttling Prevention takes place

{% hint style="warning" %}
SharePoint Online monitors throttling on several levels. From our experience the tenant level is the most important one for KONNEKT.

Because of that, throttling prevention becomes effective, if **ALL** KONNEKT clients in your tenant use the same prevention level. For example: Just setting this policy to "high" on some clients may have no effect at all. Please set all to "high", if you experience throttling while using KONNEKT.
{% endhint %}

## Manual setting in the registry

{% hint style="info" %}
You do not need this, if you use GPO or Intune management.
{% endhint %}

* **Value name:** `SharepointThrottling`
* **Value type:** `REG_DWORD`
* **Value data**
  * `0` => Autodetect (default)
  * `1` => Low
  * `2` => Medium
  * `3` => High
* Value **stored** in:
  * `HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`\
    or
  * `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`
