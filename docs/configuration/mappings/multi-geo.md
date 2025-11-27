# Multi-Geo

{% hint style="info" %}
Available for KONNEKT version 2.1 or later
{% endhint %}

{% hint style="success" %}
For machines with KONNEKT 2.3 or later, the policy is ignored as Multi-Geo support is always enabled.
{% endhint %}

Using this policy, you can activate support for [OneDrive and SharePoint Online Multi-Geo](https://learn.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-capabilities-in-onedrive-and-sharepoint-online-in-microsoft-365?view=o365-worldwide) in KONNEKT.

**Policy name:** `Multi-Geo Sharepoint support`

![](<../../.gitbook/assets/2022-05-18 16_42_33MultiGeo.png>)

<table><thead><tr><th width="232.33333333333331"></th><th></th><th></th></tr></thead><tbody><tr><td>Function</td><td>Value</td><td>Behavior</td></tr><tr><td>not set</td><td>N/A</td><td>Multi-Geo is de-activated</td></tr><tr><td>enabled</td><td>1</td><td>Multi-Geo is  activated</td></tr><tr><td>disabled</td><td>0</td><td>Multi-Geo is  de-activated</td></tr></tbody></table>

You can find more details on OneDrive and SharePoint Online Multi-Geo [here](https://docs.microsoft.com/en-us/microsoft-365/enterprise/multi-geo-capabilities-in-onedrive-and-sharepoint-online-in-microsoft-365?view=o365-worldwide).

## **There are several ways to apply the policy**

1. Via GPO, see [settings via GPO](../management-options/settings-via-gpo.md)
2. Pushing policies via Intune, see [settings for Intune Managed Devices](../management-options/setting-for-intune-managed-devices-1/)
3. Manually by adding the key in the registry

### Manual setting in the registry

{% hint style="info" %}
You do not need this if you use GPO or Intune management
{% endhint %}

* **Value name:** `SharepointMultiGeo`
* **Value type:** `REG_DWORD`
* **Value data:** `1` (to activate the feature), `0` to disable it
* **Value stored** **in**:
  * `HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`\
    or
  * `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`
