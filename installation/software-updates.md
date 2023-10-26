# Software updates

## How do I know?

If a software update is available, KONNEKT informs the user with a toast, if the user has local admin privileges.&#x20;

You may alternatively observe the context menu of the KONNEKT tray icon (right click), if there is a new version available.

![](<../.gitbook/assets/2022-08-02 15\_34\_16-Window.png>)

## Manual download of current setup files

You can get the latest version of KONNEKT [here](https://trial.konnekt.io/).

## Preview Releases

Sometimes we publish KONNEKT Preview Releases. We do this, when we are working on a new version of KONNEKT, to give customers the opportunity to try new features before those are finally released. We are happy, when we get feedback on those versions, to find bugs and improve release quality.

{% hint style="info" %}
Preview Releases are still in development and therefore bugs may occur.
{% endhint %}

KONNEKT Preview Releases are not published via the built-in update-checker in KONNEKT. You have to manually download it. If a preview release is available, you can find it in the [changelog](../changelog.md).

## Executing the update

Please follow the following steps to update KONNEKT:

1. Run the MSI of [the most current KONNEKT version](../changelog.md)
2. Reboot the machine if needed

{% hint style="warning" %}
**Local admin permissions** are required to execute an update of KONNEKT.&#x20;
{% endhint %}

{% hint style="info" %}
Why do I have to reboot the machine?

An important module of KONNEKT is a kernel driver. This kind of drivers can be updated during a reboot, only.
{% endhint %}

{% hint style="warning" %}
**Restart vs. Shutdown**

If KONNEKT setup requests a restart, please do so. Please be aware that shutting down a Windows machine and start it up again may not be equal to a restart. Many modern Windows machines use hibernation for shutdown by default. In this case driver updates may fail.
{% endhint %}

## Recommended update procedure

Managed FAT clients should be updated by the client management system (e.g. MEM/Intune)

Multiuser VDI servers should be updated manually by admins.
