# Intune mappings

## Add SharePoint libraries

**Name:** Konnekt-Automatically-Add-All-SharePoint-Libraries

**OMA-URI**

User context:

```
./User/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~Mappings/AddAllSharepointLibraries
```

Device context:

```
./Device/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~Mappings/AddAllSharepointLibraries
```

**Data type:** String

**Value options**

```
<enabled/>
```

```
<disabled/>
```

**Note**

For more information about the policy, see [Map all document libraries](../../mappings/auto-mapping.md#map-all-document-libraries)

## Connect Drive

**Name:** Konnekt-Connect-Drive

**OMA-URI**

User context:

```
./User/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~Mappings/ConnectDrive
```

Device context:

```
./Device/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~Mappings/ConnectDrive
```

**Data type:** String

**Value options**

```
<enabled/> <data id="DriveSelect" value="F:"/>
```

Disable connect drive mapping

```
<enabled/> <data id="DriveSelect" value="disabled"/>
```

**Note**

Choose value from `F:` to `Z:` For more information about the policy, see [Assign drive letter](../../mappings/assign-drive-letters.md)

## SharePoint site query

**Name:** Konnekt-SharePoint-Site-Query

**OMA-URI**

User context:

```
./User/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~Mappings/SharepointSiteQuery
```

Device context:

```
./Device/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~Mappings/SharepointSiteQuery
```

**Data type:** String

**Value**&#x20;

```
<enabled/>
<data id="SharepointSiteQuery" value="your query"/>
```

**Note**

For more information about the policy and the query, see [Auto mapping](../../mappings/auto-mapping.md#1.-site-scope)

## SharePoint Usage

**Name:** Konnekt-SharePoint-Usage

**OMA-URI**

User context:

```
./User/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~Mappings/O365SharepointUsage
```

Device context:

```
./Device/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~Mappings/O365SharepointUsage
```

**Data type:** String

**Value options**

```
<enabled/>
```

```
<disabled/>
```

**Note**

For more information about the policy, see [Map default document site libraries](../../mappings/auto-mapping.md#map-default-document-site-libraries)

## Multi-Geo

{% hint style="info" %}
Available for KONNEKT 2.1 or newer
{% endhint %}

**Name:** Konnekt-Multi-Geo

**OMA-URI**

User context:

```
./User/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~Mappings/SharepointMultiGeo
```

Device context:

```
./Device/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~Mappings/SharepointMultiGeo
```

**Data type:** String

**Value options**

```
<enabled/>
```

```
<disabled/>
```

**Note**

For more information about the policy, see [Multi-Geo](../../mappings/multi-geo.md)

## Sharepoint Sites

{% hint style="info" %}
Available for KONNEKT 2.1 or newer
{% endhint %}

**Name:** Konnekt-SharePoint-Sites

### **OMA-URI**

User context:

```
./User/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~Mappings/SharepointSites
```

Device context:

```
./Device/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~Mappings/SharepointSites
```

**Data type:** String

### **Value options**

To map one site, use the following syntax and replace <mark style="color:blue;">\<URL1></mark> with your site/library URL (<mark style="color:blue;">\<URL1></mark> must be added twice as in the following syntax and be separated by "<mark style="color:green;">\&#xF000;</mark>"):

_\<enabled/>_\
_<<mark style="color:red;">data id</mark>="<mark style="color:green;">SharepointSites\_List</mark>" <mark style="color:red;">value</mark>="<mark style="color:blue;">\<URL1></mark><mark style="color:green;">\&#xF000;</mark><mark style="color:blue;">\<URL1></mark>" />_

To map multiple sites, use the following syntax and replace <mark style="color:blue;">\<URL1></mark> with your first site/library URL and <mark style="color:orange;">\<URL2></mark> with your second site/library URL, and so on (each URL should be added twice as in the following syntax):

_\<enabled/>_\
_<<mark style="color:red;">data id</mark>="<mark style="color:green;">SharepointSites\_List</mark>" <mark style="color:red;">value</mark>="<mark style="color:blue;">\<URL1></mark><mark style="color:green;">\&#xF000;</mark><mark style="color:blue;">\<URL1></mark><mark style="color:green;">\&#xF000;</mark><mark style="color:orange;">\<URL2></mark><mark style="color:green;">\&#xF000;</mark><mark style="color:orange;">\<URL2></mark>" />_

To disable the policy

```
<disabled/>
```

### **Example**

#### **Site 1**

* Site URI = [`https://konnektdemo.sharepoint.com/sites/TestSite1`](https://c4a8.sharepoint.com/sites/GKGABSlides/Shared%20Documents/Forms/AllItems.aspx)
* Assigned Name = `TestSite1Name`
* Assigned drive letter = `k:`

KONNEKT URL for this site mapping would be:

_<mark style="color:blue;">https://konnektdemo.sharepoint.com/sites/TestSite1|TestSite1Name|k:</mark>_

#### **Site 2**

* Site URI = [`https://konnektdemo.sharepoint.com/sites/TestSite2`](https://c4a8.sharepoint.com/sites/GKGABSlides/Shared%20Documents/Forms/AllItems.aspx)
* Assigned Name = `TestSite2Name`
* Assigned drive letter = `m:`

KONNEKT URL for this site mapping would be:

_<mark style="color:orange;">https://konnektdemo.sharepoint.com/sites/TestSite2|TestSite2Name|m:</mark>_

#### **Resulting Intune Policy String Value**

_\<enabled/>_\
_<<mark style="color:red;">data id</mark>="<mark style="color:green;">SharepointSites\_List</mark>" <mark style="color:red;">value</mark>="<mark style="color:blue;">https://konnektdemo.sharepoint.com/sites/TestSite1|TestSite1Name|k:</mark><mark style="color:green;">\&#xF000;</mark><mark style="color:blue;">https://konnektdemo.sharepoint.com/sites/TestSite1|TestSite1Name|k:</mark><mark style="color:green;">\&#xF000;</mark><mark style="color:orange;">https://konnektdemo.sharepoint.com/sites/TestSite2|TestSite2Name|m:</mark><mark style="color:green;">\&#xF000;</mark><mark style="color:orange;">https://konnektdemo.sharepoint.com/sites/TestSite2|TestSite2Name|m:</mark>" />_

### **Note**

For more information about the policy and how to set the URL with examples, see [Managed mappings](../../mappings/administrative-mappings.md)
