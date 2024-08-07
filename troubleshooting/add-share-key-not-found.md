# Add Share: "Key not found"

### Problem

When you try to add a SharePoint library manually (see [#add-additional-document-libraries](../configuration/mappings/add-a-document-library.md#add-additional-document-libraries "mention")), you get the the error message "Failed to open site: Key not found".

![Error-Message: "Failed to open site: Key not found"](<../.gitbook/assets/image (19).png>)

Customers with this issue may also also experience this: [libraries-are-empty.md](libraries-are-empty.md "mention")

### Background

Microsoft (temporarily) changed the content of the response of the query for the library discovery for some tenants. Therefore KONNEKT will not map those affected libraries.

### Solution

We implemented a workaround for that behavior starting with KONNNEKT V2.0.0. Please see here, how to get the update: [software-updates.md](../installation/software-updates.md "mention").

