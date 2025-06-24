# Throttling prevention (client side)

{% hint style="info" %}
This feature is available in KONNEKT 2.11 or later
{% endhint %}

In addition to the policy "[SharePoint throttling prevention](sharepoint-throttling-prevention.md)", a KONNEKT client can be actively throttled. This setting applies to folders and files.&#x20;

## **Soft Limit**

When the soft limit is reached, the client will limit GraphAPI requests by initiating throttling:

* Most operations will be throttled for 2 seconds.
* Throttling prevention level will switch to HIGH

Some operations will be postponed until the request amount falls below the soft limit.&#x20;

## **Hard Limit**

When the hard limit is reached, the client will stop to send any GraphAPI requests. The KONNEKT app will display an error until the end of the time window is reached.

## **How to Use It**

Administrators can configure this policy by enabling it and set the following parameters:

<table><thead><tr><th width="272">Name</th><th>Default Value</th><th>Description</th></tr></thead><tbody><tr><td>ClientThrottlingTimeWindow</td><td>300</td><td>Duration, in seconds, over which throttling and resource units are measured. (0 disables client side throttling)</td></tr><tr><td>ClientThrottlingSoftLimit</td><td>250</td><td>Number of resource units that trigger the client side soft limit. (0 disables soft limit)</td></tr><tr><td>ClientThrottlingHardLimit</td><td>0</td><td>Number of resource units that trigger the hard limit. (0 disables hard limit)</td></tr></tbody></table>

## Manual setting in the registry

{% hint style="info" %}
You do not need this, if you use GPO or Intune management.
{% endhint %}

The policy consists of two components in the registry:

1. **Value** (activate the feature)
2. **Key with value per mapping** (describe every single mapping)



1. **Value**

* **Value name:** `ClientThrottling`
* **Value type:** `REG_DWORD`
* **Value data:** `1` (to activate the feature)
* Value **stored** in:
  * `HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`\
    or
  * `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`



2. **Key with value per setting -** e.g. `ClientThrottlingTimeWindow`

* **Value name:** `ClientThrottlingTimeWindow`
* **Value type:** `REG_DWORD`
* **Value data:** `300` (duration in seconds)
* Key **stored** in:
  * `HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`\
    or
  * `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`
