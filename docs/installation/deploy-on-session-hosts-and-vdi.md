# Deploy on session hosts and VDI

How to run KONNEKT on Azure Virtual Desktop (AVD), Citrix Virtual Apps and Desktops, Remote Desktop Services and Windows 365 Cloud PC. Most VDI problems come from three causes: policies that don't reach multi-session hosts, user state that doesn't roam, and a cache that fills the profile container.

## Install on the image

1. Install KONNEKT on the gold image with the silent install command from [Deployment](README.md#step-2-install-the-msi).
2. Restart the image before you seal it, so the driver is loaded.
3. Set the license key under `HKEY_LOCAL_MACHINE`, so it doesn't depend on the user profile.

{% hint style="warning" %}
Keep the KONNEKT version the same on every host in a pool. A user who roams between hosts with different versions can see errors after logon.
{% endhint %}

## Deliver policies

Put every setting you can under `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\GlueckKanja\Konnekt`. Machine policies win over user policies and survive whatever the profile solution does.

On Windows multi-session hosts, Microsoft Intune can't ingest the KONNEKT ADMX template. Use Group Policy, or an Intune remediation script that writes the registry values. For example:

```powershell
$key = 'HKLM:\SOFTWARE\Policies\GlueckKanja\Konnekt'
New-Item -Path $key -Force | Out-Null
Set-ItemProperty -Path $key -Name 'CachePolicy' -Value 1 -Type DWord
Set-ItemProperty -Path $key -Name 'CacheTTL' -Value 30 -Type DWord
Set-ItemProperty -Path $key -Name 'CacheSize' -Value 1000 -Type DWord
Set-ItemProperty -Path $key -Name 'UpdateInterval' -Value 0 -Type DWord
```

For values that must differ per user, run a logon task that writes to `HKEY_CURRENT_USER\SOFTWARE\Policies\GlueckKanja\Konnekt`. This works with FSLogix profiles too. For every value name, see [Management options](../configuration/management-options/README.md).

## Size the cache

The cache lives in each user profile, so its size multiplies by the number of sessions on a host. Set a fixed cache size and a short TTL. The recommended values are on [Cache settings](../configuration/system-settings/cache-setting.md#recommendations-for-vdi-environments).

## Persist the right user state

KONNEKT keeps per-user state in the registry and in the local app data folder. Your profile solution (FSLogix, Citrix Profile Management, profile disks) must carry the state between sessions, but not the cache.

{% hint style="warning" %}
If the cache is part of the profile container, a single large file can fill the container and break the user's session. Always exclude `%LOCALAPPDATA%\konnekt\cache`.
{% endhint %}

If the account state doesn't persist, users have to sign in again in every session, and auto-mapping runs again from scratch.

## Verify

1. Sign in to a session host as a test user.
2. Check that the drives appear.
3. Sign out.
4. Sign in to a different host in the same pool.
5. Check that KONNEKT doesn't ask for sign-in again and the drives appear.

## Related pages

- [Cache settings](../configuration/system-settings/cache-setting.md)
- [Management options](../configuration/management-options/README.md)
- [Set license key](../configuration/other/license-key-on-multi-user-environments.md)
- [System requirements](system-requirements.md)
