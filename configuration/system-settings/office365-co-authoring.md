# Office365 Co-Authoring

You can find this setting in the preferences menu:

![](<../../.gitbook/assets/image (13).png>)

You can also configure this setting via registry/GPO/MDM:

Key name: **EnableCoAuthoring**\
Key type: REG\_DWORD

Controls how KONNEKT treats Microsoft Office files.

| Function | Value | Behavior                                                                                                                                                                                 |
| :------: | :---: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  Disable |   0   | <p>KONNEKT handles up- and downloads to SharePoint Online for Microsoft Offices files.</p><p>Files are opened exclusively - Office 365 Co-Authoring is <strong>not</strong> working.</p> |
|  Enable  |   1   | <p>KONNEKT will delegate the file-handling to the Microsoft Office apps.</p><p>Microsoft Office 365 Co-Authoring is active.</p>                                                          |

The default value is 1 (enable)

We recommend to use our [ADMX template](../management-options/settings-via-gpo.md#admx-file) to configure this setting.

## **There are several ways to apply the policy:**

* manually by adding the key in the registry under machine or user registry settings
* via GPO, see [settings via GPO](../management-options/settings-via-gpo.md)
* pushing policies via Intune, see [settings for Intune Managed Devices](../management-options/setting-for-intune-managed-devices/)

**Policies** stored in:

`HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`

`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`
