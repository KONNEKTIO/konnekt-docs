# Update checker

{% hint style="info" %}
Available for KONNEKT 2.1 or newer
{% endhint %}

This policy defines if KONNEKT checks for software updates.

If the policy is enabled, KONNEKT will check for software updates and inform the user via a pop-up window to download the newer version. If the policy is disabled, no update checks take place, which means no pop-up window will show up.

**Policy name:** `Update check`

![](<../../.gitbook/assets/2022-05-18 16\_14\_26 UpdateCheck.png>)

## **There are several ways to apply the policy**

1. Via GPO, see [settings via GPO](../management-options/settings-via-gpo.md)
2. Pushing policies via Intune, see [settings for Intune Managed Devices](../management-options/setting-for-intune-managed-devices-1/)
3. Manually by adding the key in the registry

## Manual setting in the registry

{% hint style="info" %}
You do not need this if you use GPO or Intune management
{% endhint %}

* **Value name:** `UpdateInterval`
* **Value type:** `REG_DWORD`
* **Value data:** `78` (Hexadecimal) for enabled, and `0` for disabled
* **Value stored in:**
  * `HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`\
    or
  * `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`
