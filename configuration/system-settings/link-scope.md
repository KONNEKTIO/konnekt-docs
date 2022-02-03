# Link scope

### Default SharePoint link scope policy

Select the default link scope for links created on SharePoint files, value can be:

* **0:** Default company setting (Default)
* **1:** Anonymous
* **2:** Organisation
* **3:** Disabled

![](<../../.gitbook/assets/2021-10-27 10\_01\_39-Windows Sandbox.png>)

For more information see [https://github.com/OneDrive/onedrive-api-docs/blob/live/docs/rest-api/api/driveitem\_createlink.md#scope-types](https://github.com/OneDrive/onedrive-api-docs/blob/live/docs/rest-api/api/driveitem\_createlink.md#scope-types)

{% hint style="warning" %}
#### Links for "specific people" not supported

Please check your "[Default SharePoint link scope policy](https://docs.microsoft.com/en-us/sharepoint/change-default-sharing-link)" setting in SharePoint Online.&#x20;

![](<../../.gitbook/assets/image (24).png>)

_Copy Link To Clipboard_ in KONNEKT will not work, if the _Default sharing link type_ of a SharePoint Site is set to _Specific people_ and the KONNEKT _Default SharePoint link scope policy_ is not set.

If you have sites with the default sharing link type _Specific people_, we therefore recommend to set this policy in KONNEKT to _Anonymous_, _Organization,_ or _Disabled_. The _default company setting_ will not work.
{% endhint %}

## **There are several ways to apply the policy:**

* manually by adding the key in the registry under machine or user registry settings
* via GPO, see [settings via GPO](../management-options/settings-via-gpo.md)
* pushing policies via Intune, see [settings for Intune Managed Devices](../management-options/setting-for-intune-managed-devices/intune-system-settings.md#link-scope)

**Policies** stored in:

`HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`

`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`
