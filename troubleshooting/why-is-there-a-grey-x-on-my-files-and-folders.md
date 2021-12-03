# Why is there a grey "X" on my files and folders?

KONNEKT users may see a grey "X" on file and folder icons in Windows File Explorer.

![](<../.gitbook/assets/image (22).png>)

**This is not an Error or a Problem.** You can still work with your files without any restrictions.

This is a visualization in Windows Files Explorer of a setting that KONNEKT folders and files have, to save bandwidth.

**Background:**

The setting is called "FILE\_ATTRIBUTE\_OFFLINE". It indicates to the operating system, that this file or folder is not available immediately. As a result, the Windows File Explorer does not generate previews for the files.

**We use this setting with KONNEKT files & folders to save bandwidth between the client and SharePoint Online.**

The visualization is not visible to every client.

See also: [offline-attribute.md](../configuration/performance/offline-attribute.md "mention")
