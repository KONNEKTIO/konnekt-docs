# Skip Account Wizard

{% hint style="info" %}
Available in KONNEKT 2.2.0 or newer
{% endhint %}

When KONNEKT starts, it automatically deploys KONNEKT for the current user including the setup of an account. With this policy, you can prevent this.

**Policy name:** `SkipAccountWizard`

| Policy Setting     | Behavior                                             |
| ------------------ | ---------------------------------------------------- |
| Disabled (Default) | KONNEKT shall be configured for the current user     |
| Enabled            | KONNEKT shall NOT be configured for the current user |

{% hint style="warning" %}
It is very important to populate this policy **prior** the first start of KONNEKT to be effective.
{% endhint %}

Please see also [here](../../troubleshooting/subscribe-a-subset-of-users.md) for related information on this topic.

### **There are several ways to apply the policy**

1. Via GPO, see [settings via GPO](../management-options/settings-via-gpo.md)
2. Pushing policies via Intune, see [settings for Intune Managed Devices](../management-options/setting-for-intune-managed-devices-1/)
3. Manually by adding the key in the registry

### Manual setting in the registry

{% hint style="info" %}
You do not need this if you use GPO or Intune management
{% endhint %}

* **Value name:** `SkipAccountWizard`
* **Value type:** `REG_DWORD`
* **Value data:** `0` or `1`
  * `0` = disabled
  * `1` = enabled
* **Value stored in:**
  * `HKEY_CURRENT_USER\SOFTWARE\GlueckKanja\Konnekt`
