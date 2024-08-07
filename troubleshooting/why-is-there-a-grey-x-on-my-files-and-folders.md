# Why is there a grey "X" or "brown suitcase" on my files and folders?

KONNEKT users (Windows 10 or earlier) may see a grey "X" on file and folder icons in Windows File Explorer.

![](<../.gitbook/assets/image (43).png>)

In Windows 11 it looks like&#x20;

<figure><img src="../.gitbook/assets/2022-11-09 16_55_14-EyadWin11.png" alt=""><figcaption></figcaption></figure>

**This is not an Error or a Problem.** You can still work with your files without any restrictions.

This is a visualization in Windows Files Explorer of a setting that KONNEKT folders and files have, to save bandwidth.

**Background:**

The setting is called "FILE\_ATTRIBUTE\_OFFLINE". It indicates to the operating system, that this file or folder is not available immediately. As a result, Windows File Explorer does not generate previews for the files.

**Workaround:**

This symbol comes usually after a new installation, as a workaround, you can restart the Windows file explorer to remove it.

**We use this setting with KONNEKT files & folders to save bandwidth between the client and SharePoint Online.**

The visualization is not visible to every client.

See also: [offline-attribute.md](../configuration/system-settings/offline-attribute.md "mention")
