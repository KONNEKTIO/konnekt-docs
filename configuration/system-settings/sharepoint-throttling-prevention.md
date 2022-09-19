# SharePoint Throttling Prevention

{% hint style="info" %}
This feature is available in KONNEKT 2.2 or newer
{% endhint %}

The usage of SharePoint Online API is subject to limitations in terms of the amount of requests per time, that an application may use. If an application uses more resources, it will be throttled by SharePoint Online. You can find more on this in the [Microsoft docs](https://learn.microsoft.com/en-us/sharepoint/dev/general-development/how-to-avoid-getting-throttled-or-blocked-in-sharepoint-online).

Since KONNEKT is using Microsoft SharePoint Online and Microsoft Graph APIs, it may happen, that SharePoint Online will throttle your KONNEKT usage. If an application is throttled, SharePoint Online will not respond for a defined amount of time. This starts from some seconds and can grow up to minutes, depending on the usage. Impacts for KONNEKT may be slow browsing through or loading/writing of files. If the throttling grows up to minutes, it will result in error messages that the drive is currently not available.

KONNEKT has several mechanisms to reduce the occurrence of throttling, which are applied automatically. There are other settings, that you can decide on, since this will affect the timeliness e.g. of new libraries or files being available in KONNEKT. Please take a look at the following policy to learn about the available options.

{% hint style="warning" %}
In heavy load environments, all measures may not be enough to prevent throttling.

KONNEKT was made for regular office work. If you use high volume files (e.g. video editing, graphics design, CAD) or read/write gigabytes of data, KONNEKT (& SharePoint Online) may not be the proper tool of choice.
{% endhint %}

## Policy

You can load this policy in Policy Editor or Intune with our ADMX.

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
    ``or
  * `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`
