# Change KONNEKT name in explorer

By editing the following registry key, you can change the name of KONNEKT in Windows Explorer to a preferred name e.g. File Server, SharePoint files, company name, etc.

### **Key path**

```
Computer\HKEY_CLASSES_ROOT\CLSID{6E619E0D-21EB-4471-A40B-040815C884EF}
```

Therefore, you have to change the value of the default REG\_SZ to whatever name you would like, by default it is KONNEKT.

In the following example, we changed it to `SharePoint Data`

![](<../../.gitbook/assets/2021-10-22 12\_50\_06-Window.png>)

### **Result**

![](<../../.gitbook/assets/2021-10-25 11\_07\_36-Windows Sandbox.png>)
