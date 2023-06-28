# Download Directory

The Download Directory is the path where KONNEKT saves files to, that the user wants to recover.&#x20;

The typical use-case is, that an error happened during the transfer of a file to SharePoint Online. In this case KONNEKT will show an error in Windows File Explorer. One option for users is to "[export file to download folder](../../troubleshooting/how-to-deal-with-error-s.md)".

You can find more about handling errors [here](../../troubleshooting/error-message-about-missing-token.md).

## Default location

The default location for the Download Directory is `%USERPROFILE%\Downloads`.

## Set by user

Users can change the location manually in the preferences dialog, as long as the policy is not set.

<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

## Policy

{% hint style="info" %}
This policy is available in KONNEKT 2.6.0 or newer
{% endhint %}

### **Definition**

**Policy name:** `Download Directory`

**Policy Group:** KONNEKT / System Settings

| Policy Setting | Behavior                                                                                                                                      |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Not configured | The user-setting/default is used.                                                                                                             |
| Enabled        | The Download Directory configured in the policy is used by KONNEKT. The user can not change the Download Directory via the preference dialog. |
| Disabled       | The user-setting/default is used.                                                                                                             |

### **Apply the policy**

1. Via GPO, see [settings via GPO](../management-options/settings-via-gpo.md)
2. Pushing policies via Intune, see [settings for Intune Managed Devices](../management-options/setting-for-intune-managed-devices-1/)

{% hint style="warning" %}
Make sure to use the most current [ADMX file](../management-options/settings-via-gpo.md#admx-file), that matches your KONNEKT version.
{% endhint %}
