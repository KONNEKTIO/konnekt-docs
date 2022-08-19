# Managed mappings

{% hint style="info" %}
This policy is applicable to version 2.0 and above
{% endhint %}

## Policy description

By using the feature Managed Mappings (policy name `"Sharepoint Sites"`), you can map specific SharePoint sites and libraries to your KONNEKT. You can additionally define drive letters to those mappings.

To add mappings, go to the policy and click on **Show...**

![](<../../.gitbook/assets/2021-08-18 09\_44\_27-192.168.2.50 - Remote Desktop Connection.png>)

![](<../../.gitbook/assets/2022-08-19 11\_17\_20-LabServer ‎- Remotedesktop.png>)

{% hint style="info" %}
This policy does not support folder mapping, for folder mapping please use **net use**  as described [here](assign-drive-letters.md#assign-drive-letters-to-other-folders-using-net-use)
{% endhint %}

## **Policy definition**

**Policy name:** `Sharepoint Sites`&#x20;

**Format of site definitions:** `sharepoint-url|Name|DriveLetter|TenantName`

`sharepoint-url:` Your sharepoint site/library URL. Must be URL encoded (e.g. Spaces are represented by `%20`).\
`Name:` Name you choose for the mapped site. This name must be unique for each mapping.\
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

`https://mytenant.sharepoint.com/sites/mysite/Shared%20Documents|MySite Docs`

This will add the "shared documents" library of the site "mysite". The Drive will be labeled "MySite Docs".

#### Assign a drive letter

`https://mytenant.sharepoint.com/sites/mysite/Shared%20Documents|MySite Docs|M:`&#x20;

This will add the "shared documents" library of the site "mysite". The Drive will be labeled "MySite Docs". The network path will be mapped to drive M.

#### Map foreign tenant

`https://foreignTenant.sharepoint.com/sites/mysite||X:|ForeignTenant`

This will add all document libraries of the site "mysite", from the tenant "ForeignTenant.onmicrosoft.com". The network path will be mapped to drive X.&#x20;

The user must have an account configured in KONNEKT, that belongs to the Azure AD in the tenant "ForeignTenant".

## **There are several ways to apply the policy**

1. via GPO, see [settings via GPO](../management-options/settings-via-gpo.md)
2. pushing policies via Intune, see [settings for Intune Managed Devices](../management-options/setting-for-intune-managed-devices/)
3. manually by adding the key in the registry under machine or user registry settings

{% hint style="warning" %}
We highly recommend to use 1. or 2., since this policy has several components.
{% endhint %}

## Manual setting in registry

{% hint style="info" %}
You do not need this, if you use GPO or Intune management.
{% endhint %}

The policy consists of two components in the registry:

1. **Value** (activate the feature)
2. **Key with value per mapping** (describe every single mapping)

#### **1. Value**

* **Value name:** `SharepointSites`
* **Value type:** `REG_DWORD`
* **Value data:** `1` (to activate the feature)
* Value **stored** in:
  * `HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`\
    ``or
  * `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`

#### **2. Key with value per mapping**

* **Key name:** `SharepointSites`
* Key **stored** in:
  * `HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`\
    ``or
  * `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`

Under this key, one value/data entry has to be generated per mapping:

* **Value name:** equals Value data
* **Value type:** `REG_SZ`
* **Value data:** see [Policy definition](administrative-mappings.md#policy-definition).
* Value **stored** in:
  * `HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt\SharepointSites`\
    ``or
  * `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt\SharepointSites`
