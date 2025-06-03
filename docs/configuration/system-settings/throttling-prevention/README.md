# Throttling Prevention

**KONNEKT’s throttling prevention** includes two policies an "[update frequency control](sharepoint-throttling-prevention.md)" policy and a "[request rate limiting](throttling-prevention-client-side.md)" policy designed to manage and control the rate at which requests are made to the Microsoft’s GraphAPI, ensuring that the connections to SharePoint Online (SPO) remain stable and perform optimally. These policies are particularly useful in preventing an excessive resource usage and maintaining a smooth user experience.

The usage of Microsoft 365 APIs is subject to limitations in terms of the amount of requests per time, that an application may send. If an application uses more resources, it will be throttled. You can find more on this in the [Microsoft docs](https://learn.microsoft.com/en-us/sharepoint/dev/general-development/how-to-avoid-getting-throttled-or-blocked-in-sharepoint-online).

Since KONNEKT is using Microsoft SharePoint Online REST API and Microsoft Graph API, it may happen, that Microsoft APIs will throttle your KONNEKT usage. If an application is throttled, the corresponding API (e.g. SPO REST API) tells KONNEKT, that it has to wait for a defined amount of time. This starts from some seconds and can grow up to minutes, depending on the usage. Impacts for KONNEKT may be slow browsing through or loading/writing of files. If the throttling grows up to minutes, it will result in error messages that the drive is currently not available.

KONNEKT has several mechanisms to reduce the occurrence of throttling, which are applied automatically.&#x20;

## Common Scenarios for Throttling Prevention

### **Scenario 1: High Volume Data Uploads or Data Migration**

When a user attempts to upload a large number of files to / or a data migration within SPO within a short period, the device may reach the specified limit.

### **Scenario 2: Intensive Read Operations**

If a user performs intensive read operations, such as querying or searching a large directory (> 1000 items), the device may reach the specified limit.

&#x20;Examples:

* Using the File Explorer Search in large folders
* Scrolling through folders with numerous graphic or PDF files&#x20;

### **Scenario 3: Permission Queries**&#x20;

Since version 2.10 KONNEKT additionally checks permissions per folder and files since these queries consume a higher number of resource units compared to the other operations. The system may reach the specified limit much faster, which can trigger throttling prevention. Permission queries won't be triggered if "[SharePoint Throttling Prevention](sharepoint-throttling-prevention.md)" is set to 'High'.



{% hint style="warning" %}
In heavy load environments, all measures may not be enough to prevent throttling.

KONNEKT was made for regular office work. If you use high volume files (e.g. video editing, graphics design, CAD) or read/write gigabytes of data, KONNEKT (& SPO) may not be the proper tool of choice.

Please also check our [use-cases](../../../#use-cases).
{% endhint %}

## **Resource Units**

Each type of GraphAPI request consumes different amounts of resource units:

* Single-item reads: 1 resource unit each
* Write operations and directory queries: 2 resource units each
* Permission queries: 5

For details see:\
[https://learn.microsoft.com/en-us/sharepoint/dev/general-development/how-to-avoid-getting-throttled-or-blocked-in-sharepoint-online](https://learn.microsoft.com/en-us/sharepoint/dev/general-development/how-to-avoid-getting-throttled-or-blocked-in-sharepoint-online)

## How can I prevent throttling?

#### The following circumstances promote throttling:

* Usage of 3rd party tools for SPO backup - especially during working hours
* Use of tools that crawl your whole filesystem (like preview renderer etc.)
* Use of very big folders with >1000 files on the first level of the folder
* Excessive use of File Explorer Search in large Site Collections or Document Libraries

{% hint style="info" %}
Consider the following settings and actions for all users of an M365 tenant without exceptions.
{% endhint %}

#### To avoid throttling:

* Do not run SPO backups during business hours.
* If the File Explorer Search is inevitable: Optimize File Explorer searches, focus on specific folders or sub-folders to limit GraphAPI requests
* Regular Maintenance: Archive or remove outdated files, folders, Document Libraries, and Site Collections.
* Avoid excessive use of File Explorer Search in large Site Collections or Document Libraries
* Do not use any preview renderer for KONNEKT resources. See also [here](../offline-attribute.md). You can additionally set the [Offline Filter](../offline-attribute.md#exclude-dedicated-file-types-from-offline-attribute-filter) to the file extension "YYY" (which does not exist), to prevent Windows File Explorer from rendering previews for PDF files.
* Segment your data (not too many files in the first level of a folder).
* Set "[SharePoint Throttling Prevention](sharepoint-throttling-prevention.md)" Policy to "High" - only recommended until KONNEKT version 2.10.2
* As of version 2.11.0, we recommend enabling "[Client side throttling](throttling-prevention-client-side.md)" and setting the "[SharePoint Throttling Prevention](sharepoint-throttling-prevention.md)" policy to "Auto".

When you turn the [KONNEKT logging to "debug"](../logging.md#log-level), you will see log entries with "`ThrottlingHook: Need to wait Xs before start`" (where X stands for the amount of seconds SPO wants us to wait).

Log entries that contain "`[Sharepoint] UpdateDrives: Skipping volume due to throttling prevention.`" are NOT caused by SharePoint throttling. Those indicate regular operations to prevent throttling - nothing to worry about. ;-)

## **How It Works**

The "[update frequency control](sharepoint-throttling-prevention.md)" policy limits requests by enhanced refresh cycles e.g. updating the users Site Collections.

The "[request rate limiting](throttling-prevention-client-side.md)" policy operates by monitoring the number of requests and there corresponding resource units made within a specified time window and applying limits to these requests. This policy, “[Client side throttling](throttling-prevention-client-side.md)”, includes **soft** and **hard** limits:

* **Soft Limit**:\
  When the soft limit is reached, the system will begin to throttle requests. This means that most operations will be delayed for a short period (e.g., 2 seconds), and the throttling prevention level will switch to HIGH. Some operations, such as opportunistic upload jobs and read-ahead operations, will be postponed until the request amount falls below the soft limit.
* **Hard Limit**:\
  When the hard limit is reached, the system will stop sending any requests. The application will display an error message until the end of the time window is reached.

{% hint style="warning" %}
Use "Hard Limit" only when necessary, as it prevents KONNEKT from accessing communicating to Microsoft's endpoints.
{% endhint %}
