# Explorer UI

{% hint style="info" %}
This policy is applicable to version 2.0 and above
{% endhint %}

This policy defines which components of the Konnekt explorer node are shown and which are not.

Konnekt has 4 components shown in the Explorer window: **Uploads**, **History**, **Offline Files,** and **Accounts**

![](<../../../.gitbook/assets/2022-07-20 18_13_04-Window.png>)

**Example:** Show Uploads, History, Offline Files and hide Accounts (to prevent users adding new M365 accounts)&#x20;

![](<../../../.gitbook/assets/2021-10-27 10_13_30-Windows Sandbox.png>)

{% hint style="warning" %}
To apply the policy you have to restart the **Windows Explorer** process, no need to restart **KONNEKT**
{% endhint %}

**Result:**

![](<../../../.gitbook/assets/2022-07-20 18_10_09-Window.png>)

### **Policy information**

**Policy name:** Konnekt Explorer UI

### Registry

**Key names:** `ShellAccounts, ShellHistory, ShellOfflineFiles, ShellRestricted, ShellUploads`\
**Key type:** REG\_DWORD (32-Bit Value)

## **There are several ways to apply the policy:**

* manually by adding the key in the registry under machine or user registry settings
* via GPO, see [settings via GPO](../management-options/settings-via-gpo.md)
* pushing policies via Intune, see [settings for Intune Managed Devices](../management-options/setting-for-intune-managed-devices-1/intune-gui-settings.md#konnekt-explorer-ui)

**Policies** stored in:

`HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`

`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`
