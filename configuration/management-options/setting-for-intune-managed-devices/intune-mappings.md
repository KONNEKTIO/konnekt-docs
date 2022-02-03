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

**Value**&#x20;

```
<enabled/>
or 
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

**Value**&#x20;

```
<enabled/> <data id="DriveSelect" value="F:"/>
or
<disabled/>
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

**Value**&#x20;

```
<enabled/>
or
<disabled/>
```

**Note**

For more information about the policy, see [Map default document site libraries](../../mappings/auto-mapping.md#map-default-document-site-libraries)
