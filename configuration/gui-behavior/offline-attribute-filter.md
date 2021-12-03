# Offline Attribute Filter

{% hint style="info" %}
This policy is applicable to version 2.0 and above
{% endhint %}

This policy controls which file types will not be marked with an offline attribute.

The offline attribute signals to other system components like the explorer that the file is not locally available. This prevents components like preview, search, and indexing from accessing the files. Disabling the offline attribute for some file types allows the explorer to show preview information for the files, at the cost of more network traffic and possible slower response times when browsing through directories.

If the policy is enabled, all file extensions mentioned in the filter will not be marked as offline. If the policy is disabled, a default filter is applied which is "pdf".

{% hint style="warning" %}
Enabling this policy causes more network traffic and slower response time browsing directories in Windows Explorer
{% endhint %}

![](<../../.gitbook/assets/2021-12-03 13\_50\_47-Offline Attribute Filter.png>)

{% hint style="warning" %}
To apply the policy you have to restart **KONNEKT**
{% endhint %}

### **Policy information**

**Policy Name:** Offline Attribute Filter

### Registry

**Key names:** `OfflineAttributeFilter`\
**Key type:** REG\_SZ (String Value)

## **There are several ways to apply the policy:**

* manually by adding the key in the registry under machine or user registry settings
* via GPO, see [settings via GPO](../management-options/settings-via-gpo.md)
* pushing policies via Intune, see [settings for Intune Managed Devices](../management-options/setting-for-intune-managed-devices.md)

**Policies** stored in:

`HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`

`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`
