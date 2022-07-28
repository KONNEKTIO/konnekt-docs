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

For more information about the policy, see **** [Map all document libraries](../../mappings/auto-mapping.md#map-all-document-libraries)

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
<enabled/> <data id="DriveSelect" value=""/>
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

**OMA-URI**

User context:

```
./User/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~Mappings/SharepointSites
```

Device context:

```
./Device/Vendor/MSFT/Policy/Config/Konnekt~Policy~Konnekt~Mappings/SharepointSites
```

**Data type:** String

**Value options**

```
<enabled/>
<data id="SharepointSites_List" value="URL1&#xF000;URL1&#xF000;URL2&#xF000;URL2" />
```

```
<disabled/>
```

**Note**

For more information about the policy and how to set the URL with examples, see [Managed mappings](../../mappings/administrative-mappings.md)
