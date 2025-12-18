# Enhanced Authentication

Enhanced Authentication enables KONNEKT to use improved [OAuth 2.0 authorization](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-auth-code-flow#protocol-details).

{% hint style="danger" %}
By enabling this setting:

* **A new** [**Azure app registration**](../../installation/security/grant-admin-consent-in-enterprise-applications.md) **is required**
* Users need to reauthenticate!
* Namespaces are built from [default domain](https://learn.microsoft.com/en-us/microsoft-365/admin/setup/domains-faq?view=o365-worldwide#how-do-i-set-or-change-the-default-domain-in-microsoft-365) (\\\onedrive-\<DefaultDomainName>\\...), no longer from [initial domain](https://learn.microsoft.com/en-us/microsoft-365/admin/setup/domains-faq?view=o365-worldwide#how-do-i-set-or-change-the-default-domain-in-microsoft-365) (\\\onedrive-\<InitialDomainName>\\...).
  * Possible side effects include:
    * Pinned KONNEKT folders in Quick Access won't work
    * KONNEKT UNC paths in Office apps might still refer to previous names
{% endhint %}

{% hint style="info" %}
This policy is applicable to KONNEKT version 2.10 and above.
{% endhint %}

To enable this setting, configure it tenant-wide. Enabling this will prompt Azure to register a new app with fewer permissions.

With more detailed permissions, users have to reauthenticate. Additionally, the UNC path and displayed tenant name will switch to the default tenant name rather than the initial tenant name.

This feature enables the use of conditional access policies with excluded apps in Azure/EntraID.

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Policy

Policy Name: Enhanced OAuth

Possible values: Can be enabled or disabled.&#x20;

The default value is disabled.

{% hint style="info" %}
We recommend to use our latest [ADMX template](../management-options/settings-via-gpo.md#admx-file) to configure this setting. You will find the policy in "System settings" in GPO editor.
{% endhint %}

{% hint style="info" %}
After the new Azure app registration is set up, the old one should be deleted.
{% endhint %}



### Registry

Key name: EnhancedOAuth

Type: REG\_DWORD 32 bit

| Function |           Value          | Behavior                                               |
| :------: | :----------------------: | ------------------------------------------------------ |
|  Disable | <p>0</p><p>(default)</p> | KONNEKT will use the traditional OAuth 2.0 procedures. |
|  Enable  |             1            | KONNEKT will use an improved OAuth 2.0 code with.      |

The default value is 0 (disable).
