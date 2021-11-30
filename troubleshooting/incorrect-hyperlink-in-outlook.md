# Incorrect hyperlink in Outlook

## Problem description

When you copy a path of file or folder from a mapped drive and paste it as a hyperlink in Outlook (Ctrl+k), Outlook sets automatically the drive letter twice at the beginning, this leads to an error **"The system cannot find the file specified"**

![](<../.gitbook/assets/2021-11-04 16\_20\_40-Untitled - Message (HTML).png>)

## Workaround

* right- drag the file/folder from windows explorer into the outlook e-mail body
* click on **Create Hyperlink Here**
* a UNC path of the file will be copied to the message body

{% hint style="info" %}
The recommended way to internally share files is by using the UNC path!
{% endhint %}

