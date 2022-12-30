# Logging

KONNEKT writes the log to `%localappdata%\KONNEKT`. The log consists of up to 6 files, that are rotated, if full:

* client.txt
* client.1.txt
* client.2.txt
* client.3.txt
* client.4.txt
* client.5.txt

`Client.txt` holds the newest and `client.5.txt` the oldest log lines.&#x20;

The [Log Level](logging.md#log-level) setting determines what information is written to to log.

The files will be rotated, if the newest file has reached the [Log Rotation](logging.md#log-rotation) size.

## Log Level

{% hint style="info" %}
Available for KONNEKT 2.1 or newer
{% endhint %}

User can change this setting in the preference menu of the UI. If you do the setting by policy, users can not change it anymore.

The default log level is `info`.

**Policy name:** `Logging Level`

![](<../../.gitbook/assets/2022-02-25 Log Level.png>)

|                |           |                                       |
| -------------- | --------- | ------------------------------------- |
| **Option**     | **Value** | **Behavior**                          |
| No logging     | 0         | No logging                            |
| Error          | 1         | Only error records will be stored     |
| Info (default) | 2         | Info and error records will be stored |
| Debug          | 3         | All log records will be stored        |

### **There are several ways to apply the policy**

1. Via GPO, see [settings via GPO](../management-options/settings-via-gpo.md)
2. Pushing policies via Intune, see [settings for Intune Managed Devices](../management-options/setting-for-intune-managed-devices-1/)
3. Manually by adding the key in the registry

### Manual setting in the registry

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

## Log Rotation

{% hint style="warning" %}
Please do not use this setting unless requested by our support team.
{% endhint %}

The Log Rotation setting determines the maximum size of one log file. The **default** is 1 MB (1024 \* 1024 = 1.048.576 bits), so that the maximum total size of all 6 log files is 6 MB.

* **Value name:** `LogRotation`
* **Value type:** `REG_DWORD`
* **Value data:** Maximum files size; unit is bits
* **Value stored in:**
  * `HKEY_CURRENT_USER\SOFTWARE\GlueckKanja\Konnekt`

