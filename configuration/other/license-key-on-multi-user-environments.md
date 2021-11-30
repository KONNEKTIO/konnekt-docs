# Set license key

## License Key Storage

KONNEKT searches for license keys in two registry keys:

`HKEY_CURRENT_USER\SOFTWARE\GlueckKanja\Konnekt\License` (REG SZ)

`HKEY_LOCAL_MACHINE\SOFTWARE\GlueckKanja\Konnekt\License` (REG SZ)

{% hint style="info" %}
If a license key is set at machine level (HKLM), it will supersede a license key at user level (HKCU).&#x20;
{% endhint %}

## License Key Configuration

There are several options how you can configure the license key:

|         Option        |                                                                 Description                                                                |                                                                                               Use Case                                                                                              | Lic Key Storage Location |
| :-------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: |
| **Interactive Setup** |                                                 Enter the key during the interactive setup                                                 |                                                                       This option may be a good choice for a singular system.                                                                       |           HKLM           |
|       **Policy**      |                                                Set the license key via GPO or Intune policy.                                               | <p>This is the recommended approach for managed environments. <br>See <a href="license-key-on-multi-user-environments.md#set-license-key-via-registry-gpo-mdm">Set License Key</a> for details.</p> |       HKLM or HKCU       |
|   **MSI Parameter**   | <p>Sets the license key as a MSI-parameter <br>(e.g. with silent <a href="../../installation/setup.md#silent-installation">Setup</a>).</p> |                                                         This option may be a good choice for environments with a software deployment system.                                                        |           HKLM           |
|  **Preferences Menu** |                                               Enter the license key in the preferences menu.                                               |                                                                        This option may be used for single user systems, only.                                                                       |           HKCU           |

Entering the license key in the preferences menu:

![](<../../.gitbook/assets/image (16).png>)

{% hint style="danger" %}
The preference menu sets the license for the current user (HKCU), only. Other users logging in the same machine would also have to set the license.

If a license key is configured at HKLM, settings via preferences menu are not effective. (see [Set License Key](license-key-on-multi-user-environments.md#license-key-storage) for details).&#x20;
{% endhint %}

## Set License Key via Registry/GPO/MDM

Key name: **License**\
Type: REG\_SZ (String Value).

Sets the license key.

We recommend to use our [ADMX template](../management-options/settings-via-gpo.md#admx-file) to configure this setting.

## **There are several ways to apply the policy:**

* manually by adding the key in the registry under machine or user registry settings
* via GPO, see [settings via GPO](../management-options/settings-via-gpo.md)
* pushing policies via Intune, see [settings for Intune Managed Devices](../management-options/setting-for-intune-managed-devices.md)

**Policies** stored in:

`HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`

`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`
