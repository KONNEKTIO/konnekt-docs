# Cache settings

{% hint style="info" %}
This policy is applicable to version 2.0 and above
{% endhint %}

All files, that are read from or written to SharePoint Online via KONNEKT are temporarily cached on the local disc.&#x20;

The cache directory is located at: `%localappdata%\konnekt\cache`

This policy defines the caching behavior of KONNEKT.

## **KONNEKT uses the cache for different purposes:**

* Files that are currently opened by the user
* Files that need to be uploaded (write cache)
* Files that are closed (read cache)

#### **Definitions:**&#x20;

* **Cache TTL (Time To Live):** How long (in minutes) closed documents (read cache) will stay in the Cache. This value needs to be filled in the input field if the policy is enabled.
* **Fixed Cache Size:** How big (in Megabytes) is the KONNEKT cache folder. This value needs to be filled in the input field if the policy is enabled.
* **Cache Size:** Main cache size of the machine.&#x20;

## **The cache operates in different pressure states:**

* **Normal pressure:** The cache is utilized below critical values. Closed files will be kept in the read cache up to the TTL value.
* **High read pressure:** The cache is filled up with too many closed files. The read cache will be deleted.
* **High write pressure:** The cache is holding lots of files queued for upload. Further, write operations will be throttled in order to empty the upload queue.
* **Critical write pressure:** The cache is nearly filled up with files queued for upload. Further, write operations will be throttled significantly in order to empty the upload queue.
* **Cache full:** The cache is completely occupied. Requests to open further files will be rejected.

{% hint style="danger" %}
Maximum value of CacheTTL is **2880** (Time in minutes) \
\
Maximum value of CacheSize is **20000** (Size in megabytes), if zero (0), the cache size will be calculated from free disk space (default)
{% endhint %}



![](<../../.gitbook/assets/2021-07-16 12\_27\_25-Cache.png>)

* **Cache size from free disk calculation**\
  &#x20;_sizeMax_ = (_FreeDiskSize_ + _CacheSize_) \* 75%
* **High pressure calculation**\
  &#x20;_pressure_ = _sizeUsed_ / _sizeMax_ >= 80%
* **High write pressure calculation**\
  &#x20;_writePressure_ = _uploadSize_ / _sizeMax_ >= 60%
* **Critical write pressure calculation**\
  &#x20;_writePressure_ = _uploadSize_ / _sizeMax_ >= 80%
* **Cache filled calculation**\
  &#x20;_sizeUsed_ >= _sizeMax_

{% hint style="warning" %}
To apply the policy you have to restart the **Windows Explorer**
{% endhint %}

## **There are several ways to apply the policy:**

* manually by adding the key in the registry under machine or user registry settings
* via GPO, [check settings via GPO](../management-options/settings-via-gpo.md)
* pushing policies via Intune, see [setting for Intune Managed Devices](../management-options/setting-for-intune-managed-devices/)

#### **Policies** stored in:

`HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`

`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`

## Recommendations for VDI environments

We recommend the following settings for VDI environments in general, but please make sure, that this settings fits your use-case of KONNEKT:&#x20;

**Cache TTL**: 10-60 min

**Cache Size**: 500-1000 MB

You may also want to [restrict the file size](../other/open-file-size-limitations.md), that you are reading from SharePoint Online:

**OneDriveOpenFilesLargerThanReadOnly**: 100-500 MB (= 104,857,600 - 524,288,000 bytes)

**OneDriveDoNotOpenFilesLargerThan**: 200-1000 MB (= 209,715,200 - 1,048,576,000 bytes)
