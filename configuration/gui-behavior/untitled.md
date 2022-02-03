# Account re-authentication

{% hint style="info" %}
This policy is applicable to version 2.0 and above
{% endhint %}

This policy controls if the login dialog pops up immediately if an account needs to be re-authenticated.

If the policy is enabled, the login dialog is shown. If the policy is disabled, only an error is indicated in the tray and explorer.

{% hint style="warning" %}
To apply the policy you have to restart **KONNEKT**
{% endhint %}

### **There are several ways to apply the policy:**

* manually by adding the key in the registry under machine or user registry settings
* via GPO, [check settings via GPO](../management-options/settings-via-gpo.md)
* pushing policies via Intune, see [setting for Intune Managed Devices](../management-options/setting-for-intune-managed-devices/intune-gui-settings.md#account-re-authentication-ui)

**Policies** stored in:

`HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`

`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`
