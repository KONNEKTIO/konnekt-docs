# Hide tray icon

{% hint style="info" %}
This policy is applicable to version 2.0 and above
{% endhint %}

This policy controls if KONNEKT shows an icon in the window's start bar tray area.

If the policy is enabled, the tray icon is shown. If the policy is disabled, no tray icon is visible. Users can restart KONNEKT with the `/ui` option to have a tray icon.

![](<../../.gitbook/assets/2021-10-27 10_11_42-Windows Sandbox.png>)

{% hint style="warning" %}
To apply the policy you have to restart **KONNEKT**
{% endhint %}

### **Policy information:**

**Policy Name:** Tray Icon

### Registry

**Key names:** `ShowTrayIcon`\
**Key type:** REG\_DWORD (32-Bit Value)<br>

## **There are several ways to apply the policy:**

* manually by adding the key in the registry under machine or user registry settings
* via GPO, see [settings via GPO](../management-options/settings-via-gpo.md)
* pushing policies via Intune, see [settings for Intune Managed Devices](../management-options/setting-for-intune-managed-devices-1/intune-gui-settings.md#tray-icon)

**Policies** stored in:

`HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`

`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`
