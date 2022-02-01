# Open File Size Limitations

By default, KONNEKT limits the size of files, that you open on SharePoint or read from SharePoint:

* KONNEKT **will not open** files, that are bigger than 1 GB
* KONNEKT **will open** files in **read-only**, if they are bigger than 500 MB

{% hint style="success" %}
We recommend, to keep these defaults.&#x20;
{% endhint %}

## Changing the open file size defaults

You can change the thresholds for "open file size" via registry keys. This may be a good idea, if you are restricting the [cache size](../system-settings/cache-setting.md).

{% hint style="info" %}
Please be aware, that this is about the file sizes, that KONNEKT is opening/reading **from** SharePoint Online.&#x20;

It is **not** about the size of files, that you are writing **to** SharePoint Online.
{% endhint %}

{% hint style="danger" %}
Our support team will offer limited support for environments with thresholds, that are larger than the defaults.
{% endhint %}

### **Read-only threshold**

**Value name:** `OneDriveOpenFilesLargerThanReadOnly`\
``**Value storage location:** `HKCU\SOFTWARE\GlueckKanja\Konnekt`\
**Value type:** `DWORD`\
``**Value unit:** `bytes`

Files which are larger than this size are opened read-only on OneDrive and O365 accounts.

**Default: 512 \* 1024 \* 1024 bytes = 500 MB**

### **Block opening threshold**

**Value name:** `OneDriveOpenFilesLargerThanReadOnly`\
**Value storage location:** `HKCU\SOFTWARE\GlueckKanja\Konnekt`\
**Value type:** `DWORD`\
``**Value unit:** `bytes`

Do not open files which are larger than this size on OneDrive and O365 accounts.

**Default: 1024 \* 1024 \* 1024 bytes = 1 GB**
