# Account re-authentication

{% hint style="info" %}
This policy is applicable to version 2.0 and above
{% endhint %}

This policy controls if the login dialog pops up immediately if an account needs to be re-authenticated.

### **Definition**

**Policy name:** `Account Reauthentication UI`

**Policy Group:** KONNEKT / GUI Settings

| Policy Setting    | Behavior                                                                                                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Not configured    | The default is used (enabled).                                                                                                                                      |
| Enabled (default) | The login dialogue is shown, if an account needs to be re-authenticated.                                                                                            |
| Disabled          | The login dialogue is **not** shown, if an account needs to be re-authenticated. An error is indicated in the tray and in the KONNEKT node in Windows File Explorer |

{% hint style="warning" %}
To apply the policy you have to restart **KONNEKT**
{% endhint %}

**Policies** are stored in:

`HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`

`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`

### **Apply the policy**

1. Via GPO, see [settings via GPO](../management-options/settings-via-gpo.md)
2. Pushing policies via Intune, see [settings for Intune Managed Devices](../management-options/setting-for-intune-managed-devices-1/)
