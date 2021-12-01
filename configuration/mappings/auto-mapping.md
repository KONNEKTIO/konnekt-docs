# Auto Mapping

Auto Mapping is the feature of KONNEKT, that automatically maps all SharePoint Online sites & document libraries into the users Windows File Explorer (and other file dialogues). Only sites & libraries, the user has access to, are mapped.

Administrators can control this feature on two levels:

1. Site level
2. Library level

KONNEKT updates the mappings every 60 minutes.

## 1. Site scope

{% hint style="info" %}
This policy is applicable to version 2.0 and above
{% endhint %}

{% hint style="info" %}
By default KONNEKT will map all team and communication sites, the user has access to. Private channels of Teams are not in the default site scope.

**If you are fine with that, you do not need to use this policy.**
{% endhint %}

This policy enables you to define the query string used to find SharePoint sites.

The site query needs to be expressed in KQL. You can find general KQL documentation here: [https://docs.microsoft.com/en-us/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference](https://docs.microsoft.com/en-us/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference)

A list of query properties for SharePoint can be found here: [https://docs.microsoft.com/en-us/sharepoint/technical-reference/crawled-and-managed-properties-overview](https://docs.microsoft.com/en-us/sharepoint/technical-reference/crawled-and-managed-properties-overview)

## **Example 1**

### **C**ontrol which sites should be available under KONNEKT&#x20;

**Query String to map only the sites "Give" and "Contoso"**

```
(webtemplate:STS OR webtemplate:GROUP OR webtemplate:SITEPAGEPUBLISHING) AND (contentclass=STS_Site OR contentclass=STS_Web) AND (Title="Give" OR Title="Contoso")
```

![](<../../.gitbook/assets/2021-07-16 14\_40\_28-192.168.2.50 - Remote Desktop Connection.png>)

{% hint style="warning" %}
To apply the policy you have to restart **KONNEKT**
{% endhint %}

**Result**

![](<../../.gitbook/assets/2021-07-16 14\_41\_22-192.168.2.50 - Remote Desktop Connection.png>)

## **Example 2**

### **A**dd teams private channels automatically to KONNEKT&#x20;

**Query String**

```
(webtemplate:STS OR webtemplate:GROUP OR webtemplate:SITEPAGEPUBLISHING OR webtemplate:TEAMCHANNEL) AND (contentclass=STS_Site OR contentclass=STS_Web)
```

{% hint style="warning" %}
Do not forget to restart **KONNEKT** to apply the policy
{% endhint %}

**Result**

![](<../../.gitbook/assets/2021-08-13 08\_29\_21-192.168.2.50 - Remote Desktop Connection.png>)

## Example 3

### Map SharePoint sites and subsites under KONNEKT

**Query string**

```
(webtemplate:STS OR webtemplate:GROUP OR webtemplate:SITEPAGEPUBLISHING) AND (contentclass=STS_Site OR contentclass=STS_Web)
```

{% hint style="warning" %}
Do not forget to restart **KONNEKT** to apply the policy
{% endhint %}

****

**Result**

![](<../../.gitbook/assets/2021-11-04 17\_39\_56-Win10\_RJoin\_Scepman on LAPTOP-2BEFN6TS - Virtual Machine Connection.png>)

{% hint style="info" %}
you can change the site query string to fit your requirements to show:

* all subsites
* only specific subsites
* all sites and specific subsites
* specific sites and specific subsites
* and so on
{% endhint %}

## Example 4

Map all sites and libraries except specific sites (and their libraries), in the following example we will exclude Site01 and Site02 and all libraries under them.

```
(webtemplate:STS OR webtemplate:GROUP OR webtemplate:SITEPAGEPUBLISHING) AND (NOT (SiteTitle="Site01" OR SiteTitle="Site02"))
```

{% hint style="warning" %}
Do not forget to restart **KONNEKT** to apply the policy
{% endhint %}

****

## **There are several ways to apply the policy:**

* manually by adding the key in the registry under machine or user registry settings
* via GPO, [check settings via GPO](../management-options/settings-via-gpo.md)
* pushing policies via Intune, see [settings for Intune Managed Devices](../management-options/setting-for-intune-managed-devices.md)

**Policies** stored in:

`HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`

`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`

## 2. Library scope

### Map default document site libraries

You can find this setting in the preferences menu:

![](<../../.gitbook/assets/image (17).png>)

You can also configure this setting via registry/GPO/MDM:

Key name: **O365SharepointUsage**\
Key type: REG\_DWORD

Enable or disable access to SharePoint Online sites.

| Function |           Value          | Behavior                                                                                                                          |
| :------: | :----------------------: | --------------------------------------------------------------------------------------------------------------------------------- |
|  Disable |             0            | KONNEKT maps the OneDrive for Business library, only.                                                                             |
|  Enable  | <p>1</p><p>(default)</p> | KONNEKT maps the OneDrive for Business and all default document libraries of the SharePoint Online sites, the user has access to. |

The default value is 1 (enable).

We recommend using our [ADMX template](../management-options/settings-via-gpo.md#admx-file) to configure this setting.

### Map all document libraries

You can find this setting in the preferences menu:

![](<../../.gitbook/assets/image (18).png>)

{% hint style="info" %}
Please make sure to reboot **KONNEKT** after changing this setting.
{% endhint %}

You can also configure this setting via registry/GPO/MDM:

Key name: **AddAllSharepointLibraries**\
Type: REG\_DWORD

| Function |           Value          | Behavior                                                                                                                                                                                                     |
| :------: | :----------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|  Disable | <p>0</p><p>(default)</p> | <p>KONNEKT will map the default document library of the SharePoint Online sites, only.</p><p>Format of the UNC addressing is: <br><code>\\OneDrive-&#x3C;tenant-name>\&#x3C;site-name>\...</code></p>        |
|  Enable  |             1            | <p>KONNEKT will map all document libraries of the SharePoint Online site.</p><p>Format of the UNC addressing is: <br><code>\\OneDrive-&#x3C;tenant-name>\&#x3C;site-name>\&#x3C;library-name>\...</code></p> |

The default value is 0 (disable)

{% hint style="danger" %}
If users in your company are using different values of this setting, their UNC paths will not be compatible with each other (e.g. when they exchange UNC links).

To prevent this, make sure, that all users use the same value for this setting.
{% endhint %}

We recommend using our [ADMX template](../management-options/settings-via-gpo.md#admx-file) to configure this setting.
