# Adobe Acrobat Compatibility Mode

## Description

In several environments, users may experience crashes of Adobe Acrobat applications when attempting to open PDF files from a UNC-based file volume, such as KONNEKT with versions before 2.10. In the past, we mitigated that issue by adjusting the compatibility settings of the Adobe Acrobat executables.

KONNEKT versions older than 2.10 by default configure the compatibility mode for Adobe Acrobat applications to ensure smooth operation and prevent potential crashes.

<figure><img src="../../../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

KONNEKT 2.10 and newer has a change in the files system driver that circumvents Adobe Acrobat apps to crash. Therefore, it is not necessary to set compatibility mode for Acrobat applications. KONNEKT 2.10 automatically removes the compatibility mode setting for Adobe Acrobat applications. This policy allows you to keep compatibility mode if needed.

## Definition

### **Configuration by policy**

{% hint style="info" %}
This policy is available in KONNEKT 2.10 or newer
{% endhint %}

**Policy name:** AcrobatPatch

**Policy group:** KONNEKT / System Settings

| Policy setting | Behavior                                                       |
| -------------- | -------------------------------------------------------------- |
| Not configured | KONNEKT removes the compatibility mode for Adobe Acrobat apps. |
| Enabled        | KONNEKT sets compatibility modes for Adobe Acrobat apps        |
| Disabled       | KONNEKT removes the compatibility mode for Adobe Acrobat apps  |

{% hint style="warning" %}
To apply the policy you have to restart **KONNEKT**
{% endhint %}

### Manual Configuration

**Policies** are stored in:&#x20;

`HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`

`HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`



To set it up for a single user, create this **Registry** key:

Computer\HKEY\_CURRENT\_USER\Software\GlueckKanja\Konnekt&#x20;

**Value name** (DWORD 32 bit): AcrobatPatch

**Value data:**

* Enabled = 1
* Disabled = 2
