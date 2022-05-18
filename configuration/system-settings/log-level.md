# Log level

{% hint style="info" %}
Available for KONNEKT 2.1 or newer
{% endhint %}

With this setting, you can set the log level to KONNEKT so that users can not change it anymore, the default log level is info.

**Policy name:** `Logging Level`

![](<../../.gitbook/assets/2022-02-25 Log Level.png>)

|            |           |                                       |
| ---------- | --------- | ------------------------------------- |
| **Option** | **Value** | **Behavior**                          |
| No logging | 0         | No logging                            |
| Error      | 1         | Only error records will be stored     |
| Info       | 2         | Info and error records will be stored |
| Debug      | 3         | All log records will be stored        |

{% hint style="info" %}
Log records will be stored in **client.x.txt** files under `%localappdata%\konnekt`
{% endhint %}

## **There are several ways to apply the policy**

1. Via GPO, see [settings via GPO](../management-options/settings-via-gpo.md)
2. Pushing policies via Intune, see [settings for Intune Managed Devices](../management-options/setting-for-intune-managed-devices/)
3. Manually by adding the key in the registry

## Manual setting in the registry

{% hint style="info" %}
You do not need this if you use GPO or Intune management
{% endhint %}

* **Value name:** `LogLevel`
* **Value type:** `REG_DWORD`
* **Value data:** `0, 1, 2 or 3` (see table above)
* **Value stored in:**
  * `HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`\
    ``or
  * `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`
