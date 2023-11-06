# Account re-authentication

{% hint style="info" %}
This policy is applicable to version 2.0 and above
{% endhint %}

This policy controls if the login dialog pops up immediately if an account needs to be re-authenticated.

KONNEKT supports AAD/Entra ID **SSO**. Therefore users do not have to enter credentials for the KONNEKT account in Windows sessions supporting SSO, like on Entra ID/AAD joined (AADJ), Entra ID/AAD hybrid joined (AADHJ) or Entra ID/AAD registered devices. On those machines you would **disable this policy**, since authentication for KONNEKT does not require any user interaction and happens automatically.

If you are running KONNEKT in environments **without SSO**, user have to enter credentials to work with KONNEKT. After successful authentication, KONNEKT receives a [refresh token](https://learn.microsoft.com/en-us/entra/identity-platform/refresh-tokens) from AAD/Entra ID. Users will have to re-authenticate, once the refresh token is expired. In those environments we recommend to **enable this policy**.

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
