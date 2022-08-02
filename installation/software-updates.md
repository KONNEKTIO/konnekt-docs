# Software updates

## How do I know?

If a software update is available, KONNEKT informs the user with a toast, if the user has local admin priviledges.&#x20;

You may alternatively observe the context menu of the KONNEKT tray icon (right click), if there is a new version available.

![](<../.gitbook/assets/2022-08-02 15\_34\_16-Window.png>)

## Manual download of current setup files

You can get the latest version of KONNEKT [here](https://trial.konnekt.io/).

## Executing the update

{% hint style="warning" %}
Local admin permissions are required to execute an update of KONNEKT.&#x20;
{% endhint %}

Please follow the following steps to update KONNEKT:

1. Uninstall the previous version of KONNEKT
2. Reboot the machine.
3. Install the current version of KONNEKT (see [Setup](setup.md) for details)

{% hint style="info" %}
Why do I have to reboot the machine?

An important module of KONNEKT is a kernel driver. This kind of drivers must be unloaded before being updated. If you update KONNEKT without unloading the driver (= reboot the system after uninstallation), bluescreens may occur.
{% endhint %}

## Recommended update procedure

Managed FAT clients should be updated by the client management system (e.g. MEM/Intune)

VDI servers should be updated by admins only.
