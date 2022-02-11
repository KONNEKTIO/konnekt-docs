# Multi-Geo

{% hint style="info" %}
Available for KONNEKT 2.1 or newer
{% endhint %}

You can activate support for OneDrive an SharePoint Online Multi-Geo in KONNEKT.

Policy name: `Multi-Geo Sharepoint support`

|          |       |                            |
| -------- | ----- | -------------------------- |
| Function | Value | Behavior                   |
| not set  | N/A   | Multi-Geo is de-activated  |
| enabled  | 1     | Multi-Geo is  activated    |
| disabled | 0     | Multi-Geo is  de-activated |

You can find more details on OneDrive and SharePoint Online Multi-Geo [here](https://docs.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-capabilities-in-onedrive-and-sharepoint-online-in-microsoft-365?view=o365-worldwide).

## **There are several ways to apply the policy**

1. Via GPO, see [settings via GPO](../management-options/settings-via-gpo.md)
2. Pushing policies via Intune, see [settings for Intune Managed Devices](../management-options/setting-for-intune-managed-devices/)
3. Manually by adding the key in the registry

### Manual setting in registry

{% hint style="info" %}
You do not need this, if you use GPO or Intune management
{% endhint %}

* **Value name:** `SharepointMultiGeo`
* **Value type:** `REG_DWORD`
* **Value data:** `1` (to activate the feature)
* Value **stored** in:
  * `HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`\
    ``or
  * `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`
