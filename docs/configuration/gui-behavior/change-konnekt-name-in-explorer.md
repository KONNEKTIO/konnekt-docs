# Change KONNEKT name in explorer

By editing the following registry key, you can change the name of KONNEKT in Windows Explorer to a preferred name e.g. File Server, SharePoint files, company name, etc.

### **Key paths**

You have to change the "(Default)" values in the following two registry keys:

Key for 64 bit apps:

```
Computer\HKEY_CLASSES_ROOT\CLSID\{6E619E0D-21EB-4471-A40B-040815C884EF}
```

Key for 32 bit apps:

```
Computer\HKEY_CLASSES_ROOT\WOW6432Node\CLSID\{6E619E0D-21EB-4471-A40B-040815C884EF}
```

Change the value of the "(Default)" REG\_SZ to whatever name you would like. By default it is `KONNEKT`.

In the following example, we changed it to `SharePoint Data`

![](<../../.gitbook/assets/2021-10-22 12_50_06-Window.png>)

### **Result**

![](<../../.gitbook/assets/2021-10-25 11_07_36-Windows Sandbox.png>)
