# Clicking a share does nothing

This is most likely caused by the missing registration of the **KONNEKT** network provider. Please verify of you can open **OneDrive.** If you cannot open the folder add the following registry entry to your system:

```
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\NetworkProvider\Order
"ProviderOrder"="konnekt,RDPNP,LanmanWorkstation,webclient"
```

You may also want to have a look at this: [libraries-are-empty.md](libraries-are-empty.md "mention")
