# Managed Mappings

{% hint style="info" %}
This policy is applicable to version 2.0 and above
{% endhint %}

## Policy description

By using the feature Managed Mappings (policy name `"Sharepoint Sites"`), you can map specific SharePoint sites and libraries to your KONNEKT. You can additionally define drive letters to those mappings.

![](<../../.gitbook/assets/2021-08-18 09\_44\_27-192.168.2.50 - Remote Desktop Connection.png>)

To add mappings click on **Show**

![](<../../.gitbook/assets/2021-08-19 09\_59\_16-192.168.2.50 - Remote Desktop Connection.png>)

## **Policy definition**

**Policy name:** `Sharepoint Sites`&#x20;

**Key name:** `SharepointSites`\
**Key type:** REG\_DWORD, Key and one REG-SZ per Mapping under Key

**Format of site definitions:** `sharepoint-url|Name|DriveLetter|TenantName`

`sharepoint-url:` Your sharepoint site/library URL\
`Name:` Name you choose for the mapped site\
`DriveLetter:` for drive mapping\
`TenantName:` Microsoft365 tenant-name for the corresponding account that must be used to access this site. (\<TenantName>.onmicrosoft.com).

{% hint style="info" %}
Adding `Name, DriveLetter or TenantName` is optional. \
**For example:** the SharePoint site can be configured without drive mapping.
{% endhint %}

**Site mapping result:**

![](<../../.gitbook/assets/2021-08-19 10\_10\_40-192.168.2.50 - Remote Desktop Connection (2).png>)

**Drive mapping result:**

![](<../../.gitbook/assets/2021-08-19 10\_20\_06-192.168.2.50 - Remote Desktop Connection.png>)

## **Examples**

#### All libraries of a site

`https://mytenant.sharepoint.com/sites/mysite`

This will add all document libraries of the site "mysite". The Drive will be labeled "mysite".

#### Dedicated library of a site

`https://mytenant.sharepoint.com/sites/mysite/Shared Documents|MySite Docs`

This will add the "shared documents" library of the site "mysite". The Drive will be labeled "MySite Docs".

#### Assign a drive letter

`https://mytenant.sharepoint.com/sites/mysite/Shared Documents|MySite Docs|M:`&#x20;

This will add the "shared documents" library of the site "mysite". The Drive will be labeled "MySite Docs". The network path will be mapped to drive M.

#### Map foreign tenant

`https://foreignTenant.sharepoint.com/sites/mysite||X:|ForeignTenant`

This will add all document libraries of the site "mysite", from the tenant "ForeignTenant.onmicrosoft.com". The network path will be mapped to drive X.&#x20;

The user must have an account configured in KONNEKT, that belongs to the Azure AD in the tenant "ForeignTenant".

## **There are several ways to apply the policy:**

* manually by adding the key in the registry under machine or user registry settings
* via GPO, see [settings via GPO](../management-options/settings-via-gpo.md)
* pushing policies via Intune, see [settings for Intune Managed Devices](../management-options/setting-for-intune-managed-devices.md)

**Policies** stored in:

`HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`

`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`
