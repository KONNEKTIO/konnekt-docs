# Site Collections are not displayed for some users

## Situation

Currently, some customers are experiencing issues where specific users cannot view any Site Collections within KONNEKT. KONNEKT uses the RestAPI connected to SharePoint Online to identify the Site Collections a user can access. The query responsible for this can be located in the KONNEKT logs preceding this line:

```
Sharepoint query returned the folloing sites 
```

The structure is similar to this:

```
https://<TenantName>.sharepoint.com/_api/search/query?QueryText=%27%28webtemplate%3ASTS%20OR%20webtemplate%3AGROUP%20OR%20webtemplate%3ASITEPAGEPUBLISHING%29%20AND%20%28contentclass%3DSTS_Site%20OR%20contentclass%3DSTS_Web%29%20AND%20path%3Ahttps%3A%2F%2F%27&SelectProperties=%27SiteId%2CSiteLogo%2CPath%2CTitle%2CDescription%27&Properties=%27EnableMultiGeoSearch%3Atrue%2C%20EnableDynamicGroups%3Atrue%27&ClientType=%27KONNEKT%27&StartRow=0&RowLimit=500&BypassResultTypes=true&EnableQueryRules=false&ProcessBestBets=false&ProcessPersonalFavorites=false&TrimDuplicates=false
```

When using Edge, the XML should display all Site Collections that a user can access. At the end, the "InternalRequestId" will be provided, which can assist Microsoft in identifying the issue's root cause.\
We are unable to determine what changes

\
**Temporary workaround to add shares**:\
\- ​Manually- Right click on Accounts / Add Share

![](https://eucattachment.freshdesk.com/inline/attachment?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjA0MDA2MTY3MTUzLCJkb21haW4iOiJjNGE4LmZyZXNoZGVzay5jb20iLCJhY2NvdW50X2lkIjozNDEwODY3fQ.EwKt8cWoK0Xa0306p3SGU4SYjphP1T-lB3LReg8fZG0)

\
or use\
\- Managed Mappings\
[https://docs.konnekt.io/configuration/mappings/administrative-mappings](https://docs.konnekt.io/configuration/mappings/administrative-mappings)\
\
Please help to raise the awareness by opening a Microsoft for th affected M365 tenant.

```
"The following RestAPI query returns site collections for some users and no site collections for others. Nothing has been changed in the corresponding authorizations. This is the corresponding request:"
```
