# Offline attribute

Files provided by KONNEKT are marked with the offline attribute (see also [FILE\_ATTRIBUTE\_OFFLINE](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-fscc/ca28ec38-f155-4768-81d6-4bfeb8586fc9)). This offline attribute signals to other system components like the Windows Explorer that the file is not locally available. This prevents components like preview, search and indexing from accessing the files.&#x20;

Marking files with the offline attribute therefore saves bandwidth between the KONNEKT client and SharePoint Online. The downside of this is, that no thumbnails or previews (e.g. of pictures) are rendered in Windows Explorer. Sometimes Windows Explorer also shows a grey X on files that are marked offline (see also [why-is-there-a-grey-x-on-my-files-and-folders.md](../../troubleshooting/why-is-there-a-grey-x-on-my-files-and-folders.md "mention")).

By default, KONNEKT marks all files (besides PDF) as offline. This policy allows to change this behavior.

{% hint style="warning" %}
Disabling the offline attribute for some file types allows the Windows Explorer to show preview information for the files, at the cost of more network traffic and possible slower response times when browsing through directories. It is also increasing the risk of [SharePoint Throttling](throttling-prevention/sharepoint-throttling-prevention.md).

Therefore, please disable the offline attribute with care and only for environments that have a good connection to Office 365.
{% endhint %}

## Setting the Offline Attribute for all files

This policy controls if all files handeled by KONNEKT will be marked with the offline attribute.

**GPO Policy Name**: "Offline Attribute"

**Key Name**: `EnableOfflineAttribute` (REG\_DWORD)

**Values**

|          GPO-setting          | Value | Behavior                                                                    |
| :---------------------------: | :---: | --------------------------------------------------------------------------- |
|         Not configured        |  N/A  | All file-types (besides PDF) handeled by KONNEKT will be marked as offline. |
| <p>Enable</p><p>(default)</p> |   1   | All file-types (besides PDF) handeled by KONNEKT will be marked as offline. |
|            Disabled           |   0   | All file-types handeled by KONNEKT will be marked as online.                |

## Exclude dedicated file-types from offline attribute (filter)

{% hint style="info" %}
This policy is applicable to version 2.0 and above
{% endhint %}

This policy controls which file types will **not** be marked with an offline attribute.

**GPO Policy Name**: "Offline Attribute Filter"

**Key Name**: `OfflineAttributeFilter` (REG\_SZ)

**Values**

|   GPO-setting  |                Value               | Behavior                                                                              |
| :------------: | :--------------------------------: | ------------------------------------------------------------------------------------- |
| Not configured |                 N/A                | Only PDF files are excluded from offline attribute.                                   |
|     Enable     |            \<filetypes>            | The specified file-extensions (separated by \| ) are excluded from offline attribute. |
|    Disabled    | <p>N/A</p><p>(Key not present)</p> | Only PDF files are excluded from offline attribute.                                   |

**Example** for \<filetypes>: `pdf|png|jpg|jpeg`

## **There are several ways to apply the policies**

* manually by adding the key in the registry under machine or user registry settings
* via GPO, see [settings via GPO](../management-options/settings-via-gpo.md)
* pushing policies via Intune, see [settings for Intune Managed Devices](../management-options/setting-for-intune-managed-devices-1/intune-system-settings.md#offline-attribute)

**Policies** stored in:

`HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`

`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`
