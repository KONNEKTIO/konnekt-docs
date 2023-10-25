# SharePoint throttling prevention

{% hint style="info" %}
This feature is available in KONNEKT 2.2 or newer
{% endhint %}

The usage of Microsoft 365 APIs is subject to limitations in terms of the amount of requests per time, that an application may send. If an application uses more resources, it will be throttled. You can find more on this in the [Microsoft docs](https://learn.microsoft.com/en-us/sharepoint/dev/general-development/how-to-avoid-getting-throttled-or-blocked-in-sharepoint-online).

Since KONNEKT is using Microsoft SharePoint Online REST API and Microsoft Graph API, it may happen, that Microsoft APIs will throttle your KONNEKT usage. If an application is throttled, the corresponding API (e.g. SharePoint Online REST API) tells KONNEKT, that it has to wait for a defined amount of time. This starts from some seconds and can grow up to minutes, depending on the usage. Impacts for KONNEKT may be slow browsing through or loading/writing of files. If the throttling grows up to minutes, it will result in error messages that the drive is currently not available.

KONNEKT has several mechanisms to reduce the occurrence of throttling, which are applied automatically. There are other settings, that you can decide on, since this will affect the timeliness e.g. of new libraries or files being available in KONNEKT. Please take a look at the following policy to learn about the available options.

{% hint style="warning" %}
In heavy load environments, all measures may not be enough to prevent throttling.

KONNEKT was made for regular office work. If you use high volume files (e.g. video editing, graphics design, CAD) or read/write gigabytes of data, KONNEKT (& SharePoint Online) may not be the proper tool of choice.

Please also check our [use-cases](../../#use-cases).
{% endhint %}

## How can I prevent throttling?

The following circumstances promote throttling:

* Usage of 3rd party tools for SharePoint Online backup - especially during working hours
* Use of tools that crawl your whole filesystem (like preview renderer etc.)
* Use of very big folders with >1000 files on the first level of the folder

To avoid this, please

* Do not run backups of SharePoint online during working hours.
* Do not use any preview renderer for KONNEKT resources. See also [here](offline-attribute.md). You can additionally set the [Offline Filter](offline-attribute.md#exclude-dedicated-file-types-from-offline-attribute-filter) to the file extension "YYY" (which does not exist), to prevent Windows File Explorer from rendering previews for PDF files.
* Segment your data (not too many files in the first level of a folder).
* Set KONNEKT SharePoint Throttling Prevention Policy (see below) to "High"

## How can I detect throttling?

When you turn the [KONNEKT logging to "debug"](logging.md#log-level), you will see log entries with "ThrottlingHook: Need to wait `X`s before start" (where X stands for the amount of seconds SharePoint Online wants us to wait).

Log entries that contain "`ThrottledRequest:`" are NOT caused by SharePoint throttling. Those indicate regular operations - nothing to worry about. ;-)

## Policy

You can load this policy in Policy Editor or Intune with our [ADMX](../management-options/settings-via-gpo.md#admx-file).

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
