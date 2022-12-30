# Office365 Co-Authoring

[Microsoft Office 365 Co-Authoring](https://support.microsoft.com/en-us/office/document-collaboration-and-co-authoring-ee1509b4-1f6e-401e-b04a-782d26f564a4) is a technology, that allows you advanced collaboration with Microsoft Office files. One of the benefits is, that multiple users can work on an office file simultaneously.

## Setting in KONNEKT

KONNEKT can leverage Microsoft Office 365 Co-Authoring, when opening files from Windows File Explorer. In this case, KONNEKT just hands of the SharePoint URL of a file to the corresponding Microsoft 365 App (e.g. Microsoft Word). The App will then load the file directly from SharePoint.

{% hint style="info" %}
This setting will affect files, that are opened from Windows File Explorer, only.&#x20;

Other use-cases (e.g. KONNEKT file is opened from Office App) are not covered and Co-Authoring & Auto-Save will not work.
{% endhint %}

We recommend using Microsoft Office 365 Co-Authoring, since it has valuable benefits. This is why Co-Authoring is activated by default in KONNEKT.

However, if you do not want to use Co-Authoring and want to load office files through KONNEKT instead, you can use this setting and deactivate it.

Here are the possible settings:

|     Function     | Value | Behavior                                                                                                                                                                                                                      |
| :--------------: | :---: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      Disable     |   0   | <p>KONNEKT handles up- and downloads to SharePoint Online for Microsoft Offices files.</p><p>Files are opened exclusively - Office 365 Co-Authoring is <strong>not</strong> working.</p>                                      |
| Enable (default) |   1   | <p>KONNEKT will delegate the file-handling to the Microsoft Office apps for KONNEKT files that are opened from Windows File Explorer.</p><p>Microsoft Office 365 Co-Authoring and Auto-Save is available for those files.</p> |

### GUI

You can find this setting in the preferences menu:

![](<../../.gitbook/assets/2022-08-02 16\_30\_24-Window.png>)

### Policy

Policy Name: **Co-Authoring**

Possible values: can be enabled or disabled.

The default value is enabled.

We recommend to use our [ADMX template](../management-options/settings-via-gpo.md#admx-file) to configure this setting. You will find the policy in "System settings" in GPO editor.

#### **Usage**

There are several ways to apply the policy:

* via GPO, see [settings via GPO](../management-options/settings-via-gpo.md)
* pushing policies via Intune, see [settings for Intune Managed Devices](../management-options/setting-for-intune-managed-devices-1/intune-system-settings.md#co-authoring)

**Policies** stored in:

`HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`

`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`
