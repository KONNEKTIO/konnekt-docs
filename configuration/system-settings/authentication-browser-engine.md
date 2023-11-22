# Authentication browser engine

{% hint style="info" %}
This policy is applicable to version 2.9 and above
{% endhint %}

This policy controls whether KONNEKT uses the Edge (Chromium) web browser component WebView2.

### Definition

**Policy name:** Disable Edge Browser Component (WebView2)

**Policy group:** KONNEKT / System Settings

| Policy setting     | Behavior                                                                                   |
| ------------------ | ------------------------------------------------------------------------------------------ |
| Not configured     | The default is used (disabled).                                                            |
| Enabled            | KONNEKT will not use WebView2, instead Internet Explorer based control is used.            |
| Disabled (default) | KONNEKT will try to use WebView2. If it fails it will use Internet Explorer based control. |

{% hint style="warning" %}
To apply the policy you have to restart **KONNEKT**
{% endhint %}

**Policies** are stored in:&#x20;

`HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`

`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`



To set it up for a single user, create this **Registry** key:

Computer\HKEY\_CURRENT\_USER\Software\GlueckKanja\Konnekt&#x20;

**Value name** (DWORD 32 bit): DisableWebView2&#x20;

**Value data:** 1

### **Apply the policy**

1. Manually by adding the key in the registry under machine or user registry settings
2. Via GPO, see [settings via GPO](../management-options/settings-via-gpo.md)
3. Pushing policies via Intune, see [settings for Intune Managed Devices](../management-options/setting-for-intune-managed-devices-1/)
