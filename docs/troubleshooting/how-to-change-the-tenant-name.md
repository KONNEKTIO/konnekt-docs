---
description: There is one option to change the tenant name.
---

# How to change the tenant name

With KONNEKT version 2.10 the behavior has changed what KONNEKT refers as tenant name. By enabling "[Enhanced OAuth](../configuration/system-settings/enhanced-authentication.md)" this setting will take affect.

All KONNEKT versions from 2.9.1 and earlier are using the initial tenant name. By enabling the setting "Enhanced OAuth" this behavior will change. Instead it will show the default tenant name that can be set via Microsoft Admin Center.

{% hint style="info" %}
Takes affect with KONNEKT version 2.10 and above
{% endhint %}

Steps that needs to be done by administrators or users are:

* Enabling "Enhanced OAuth" via GPO or Intune policy
* Apply the new App registration in Azure
* delete previous user data from the user registry



{% hint style="warning" %}
The UNC path will change after enabling this setting!

For example, if there are references between files or folders, these links will break!
{% endhint %}

