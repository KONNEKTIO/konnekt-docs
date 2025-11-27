# Windows File Explorer

KONNEKT is fully integrated in Windows File Explorer. When you open File Explorer you'll find  KONNEKT in the navigation pane.

![](<../.gitbook/assets/2022-07-21 13_45_30-Windows Sandbox.png>)

{% hint style="info" %}
KONNEKT may take 1 to 3 minutes to discover your SharePoint sites, depending on the number of site collections. Please allow sufficient time for the discovery process.
{% endhint %}

{% hint style="success" %}
KONNEKT does NOT download your documents to the client. it is a synchronized view of your SharePoint library.
{% endhint %}

**General** contains four sections:&#x20;

* Upload
* History
* Offline Files
* Accounts

![](<../.gitbook/assets/2022-07-21 13_42_21-Windows Sandbox (1).png>)

## **Uploads**

The place where the data queue is located, which you're uploading to the SPS. Here you can find all your data if something goes wrong during the upload process (Internet connection lost..). The files will be automatically deleted as long as they are successfully uploaded to the SP.

Once your data is successfully uploaded to the SharePoint Online (SPO), the files in the data queue will be automatically deleted. If there's an issue, such as an internet or wifi disruption, you can find all your data here for troubleshooting.

If there is an issue, you can download stuck files or try to re-upload them by right-clicking on the specific file.

## **History**

The files which you have changed or opened in your sites.

## **Offline Files**

To make **files** available offline from **OneDrive**, right-click on a file, then select Konnekt -> Offline available

![](<../.gitbook/assets/2021-05-21 17_03_26-OneDrive.png>)

{% hint style="info" %}
The Offline Files feature is only available for files stored on OneDrive
{% endhint %}

## **Accounts**

This feature supports multi-tenancy, allowing you to add multiple Microsoft 365 accounts. You'll find here the accounts you've used to log into your tenant(s).

To add another Microsoft 365 account via right-click and "Add an O365 account."&#x20;

<figure><img src="../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

### Existing accounts

If you right-click on an existing user account, the following options will appear:

* Re-authenticate account
*   Add share:&#x20;

    * To map Document Libraries as shares manually.

    <figure><img src="../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>
* Pause account:&#x20;
  * To stop the synchronization for this account temporarily.
* Delete account

![](<../.gitbook/assets/2022-07-21 13_29_24-Windows.png>)
