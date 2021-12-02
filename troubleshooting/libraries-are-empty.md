# Libraries are empty

### Problem

Some or all libraries in KONNEKT and mapped drives are empty.

KONNEKT client log shows the following messages: `[Sharepoint] Failed to determine drives of site ... Key not found. Use default drive instead.`

Customers with this issue may also also experience this: [add-share-key-not-found.md](add-share-key-not-found.md "mention")

### Background

Microsoft (temporarily) changed the content of the response of the query for the library discovery for some tenants. Therefore KONNEKT will not map those affected libraries.

This only happens if the feature "Automatically add all SharePoint document libraries" (see [#map-all-document-libraries](../configuration/mappings/auto-mapping.md#map-all-document-libraries "mention")) is used.

### Solution

We implemented a workaround for that behavior starting with KONNNEKT V2 preview 44 (1.20.44.0). You can download it here: [#2.0-currently-in-public-preview](../changelog.md#2.0-currently-in-public-preview "mention").

After installing the new version of KONNEKT, please&#x20;

* Reboot the machine,
* Start Windows Explorer and click on KONNEKT node and
* Wait 5-10 minutes.

After this procedure, the libraries should work.
