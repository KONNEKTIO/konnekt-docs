# Adobe Acrobat Compatibility Mode

## Description

In several environments, users may experience crashes of Adobe Acrobat applications when attempting to open PDF files from a UNC-based file volume, such as KONNEKT. This issue can be mitigated by adjusting the compatibility settings of the Adobe Acrobat executables.

To prevent these crashes, it is recommended to set the Adobe Acrobat applications to operate in Windows 7 compatibility mode. By default, KONNEKT configures the compatibility mode for Adobe Acrobat applications to ensure smooth operation and prevent potential crashes.

<figure><img src="../../../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

While setting Adobe Acrobat applications to operate in Windows 7 compatibility mode can prevent crashes, it’s important to note that this setting may limit the functionality of some features in newer Acrobat applications.

If you find that this is the case in your environment, KONNEKT provides the following policy that allows you to prevent the automatic configuration of the compatibility mode for Adobe Acrobat applications.&#x20;

However, if you choose to use this policy and subsequently experience crashes with Adobe Acrobat applications, we recommend contacting Adobe support.

## Definition

### **Configuration by policy**

{% hint style="info" %}
This policy is available in KONNEKT 2.10 or newer
{% endhint %}

**Policy name:** AcrobatPatch

**Policy group:** KONNEKT / System Settings

| Policy setting    | Behavior                                                        |
| ----------------- | --------------------------------------------------------------- |
| Not configured    | The default is used (enabled).                                  |
| Enabled (default) | KONNEKT sets compatibility modes for Adobe Acrobat apps         |
| Disabled          | KONNEKT does not set compatibility modes for Adobe Acrobat apps |

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
