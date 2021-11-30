# Libraries are empty

### Problem

Some or all libraries in KONNEKT and mapped drives are empty.

KONNEKT client log shows the following messages: `[Sharepoint] Failed to determine drives of site ... Key not found. Use default drive instead.`

Customers with this issue may also also experience this: [add-share-key-not-found.md](add-share-key-not-found.md "mention")

### Background

Microsoft (temporarily) changed the content of the response of the query for the library discovery for some tenants. Therefore KONNEKT will not map those affected libraries.

This only happens if the feature "Automatically add all SharePoint document libraries" (see [#map-all-document-libraries](../configuration/mappings/auto-mapping.md#map-all-document-libraries "mention")) is used.

### Solution

We implemented a workaround for that behavior starting with KONNNEKT V2 preview 43 (1.20.43.0). You can download it here: [#2.0-currently-in-public-preview](../changelog.md#2.0-currently-in-public-preview "mention").

After starting the new version of KONNEKT, it will still not show the libraries. 60 min after starting, KONNEKT will automatically start a volume update for the current user session. Once this has finished (may take some minutes - depends on how many sites/libraries the user has), the libraries will work again.

### Additional info

If you want to speed up the process of discovering the libraries, you can manually start a volume update in two ways.

{% hint style="warning" %}
Both approaches will be ignored by KONNEKT with in 2 minutes after startup of KONNEKT. So please wait >2 min after startup of KONNEKT.
{% endhint %}

#### 1. Windows Explorer

In Explorer (right click on KONNEKT node and chose "Update volumes"):

![Update volumes in Windows Explorer](<../.gitbook/assets/image (26).png>)

#### 2. Command Line

Run the following command in command line:

`"%programfiles%\KONNEKT\konnektcmd.exe" updateShares:`

``
