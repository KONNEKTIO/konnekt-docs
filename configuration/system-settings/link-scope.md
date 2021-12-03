# Link scope

### Default SharePoint link scope policy

Select the default link scope for links created on SharePoint files, value can be:

* **0:** Default company setting
* **1:** Anonymous
* **2:** Organisation
* **3:** Disabled

![](<../../.gitbook/assets/2021-10-27 10\_01\_39-Windows Sandbox.png>)

For more information see [https://github.com/OneDrive/onedrive-api-docs/blob/live/docs/rest-api/api/driveitem\_createlink.md#scope-types](https://github.com/OneDrive/onedrive-api-docs/blob/live/docs/rest-api/api/driveitem\_createlink.md#scope-types)

## **There are several ways to apply the policy:**

* manually by adding the key in the registry under machine or user registry settings
* via GPO, see [settings via GPO](../management-options/settings-via-gpo.md)
* pushing policies via Intune, see [settings for Intune Managed Devices](../management-options/setting-for-intune-managed-devices.md)

**Policies** stored in:

`HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`

`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`
