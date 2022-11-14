# Subscribe a subset of users

It is allowed to subscribe KONNEKT for a subset of the SharePoint Online users in a tenant. Please see our [licensing guide](../licensing/) for details on licensing.

However, there are some things, you should care about, to ensure proper usage:

* Assign license key to subscribe users, only
* Install KONNEKT on machines with subscribed users, only

## Assign licenses

You must make sure, that only those users, who are subscribed to KONNEKT have a license key. To achieve this, please assign the license key on a user-basis, only:

* Disabled the license key on the machine level for ALL users/machines.
* Set the license key on user level for all users that are subscribed to KONNEKT.

Details on how to set license keys can be found [here](../configuration/other/license-key-on-multi-user-environments.md).

## Disable KONNEKT on machines

You should install KONNEKT machines with subscribed users, only.

In case of VDI, there may be machines, where both types of users (subscribed/non-subscribed) are working. In those cases you should prevent, that KONNEKT is generating an account for non-subscribed users. You can do this by disabling the Account Setup Wizard for the non-subscribed users. You can find details on this [here](subscribe-a-subset-of-users.md).

{% hint style="warning" %}
Disabling the account setup wizard must be set prior the first login of the user after the setup of KONNEKT to be effective.
{% endhint %}

