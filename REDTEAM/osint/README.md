---
description: Open Source Intelligences
---

# OSINT

Defination

> Internet GIves us RAW DATA Harverst IT.
>
> Open Souce Intelligence is the collection of information grather from public avaiable resouces.

* Data: A set of values about a particular subject.&#x20;
* Information: Processed and organised data which has relevance in terms of a particular context.
* Intelligence: Evaluated and analysed information for a particular objective.

Type of Intelligence

* HUMINT : HUMAN Intelligence which gatherd information from person on ground.
* GOEINT : GEOSPATIAL  Intelligence which gatherd information form satellite, photos, mapping etc
* MASINT - Measurement and signature intelligence.
* OSINT - Gathered from open sources.
* SIGINT - Signals intelligence which gathered from interception of signals.
* TECHINT - Technical intelligence which gathered from analysis of weapons and equipment used by the armed forces of foreign nations, or environmental conditions.
* CYBINT/DNINT - Cyber Intelligence/Digital Network Intelligence which gathered from cyberspace.&#x20;
* FinINT - Financial intelligence which gathered from analysis of monetary transactions.



OSINT Source&#x20;

* Search Engines&#x20;
* Social Media Platforms&#x20;
* File Sharing Websites&#x20;
* Blogs &#x20;
* APIs&#x20;
* Domain Discovery Tools&#x20;
* Public/Government Data Sites&#x20;
* News Websites&#x20;
* MetaData in Files&#x20;
* Many More...

Possible Output&#x20;

* Domains/Sub-Domains&#x20;
* IP Addresses&#x20;
* &#x20;Open Ports and Services&#x20;
* Emails&#x20;
* Leaked Credentials/Keys/Tokens&#x20;
* Technology Stack&#x20;
* Usernames&#x20;
* Known Vulnerabilities&#x20;
* &#x20;Exposed Cloud Storage&#x20;
* &#x20;Compromised Organization&#x20;
* Much More...

Digital Assests

* Many companies has digital assets which are exposed to internet, cloud S3 buckets are not involve in this. Such assests are Domains/Subdomains,IP Ranges,DNS Records,Cloud Storage.

Digital Assests Scoping

* WHOIS and ASN IDs
* Reverse WHOIS, NSLOOKUP , DIG with A name and C name like dig hexrinx.com cname and MXTOOL
* DIG Options

```
dig redhat.com
dig redhat.com MX +noall +answer
dig redhat.com +nocomments +noquestion
+noauthority +noadditional +nostats

dig -x 209.132.183.81
dig @ns1.redhat.com redhat.com
dig -f names.txt +noall +answer
dig redhat.com -t axfr
```



ASN ID And LOOKUP

```
dig uber.com
whois PUBLICIP | grep AS
whois
```



### REFERENCE

{% file src="../.gitbook/assets/Tactical OSINT.pdf" %}
OSINT
{% endfile %}

OSINT Resources



&#x20;OSINT Resources:&#x20;

[https://www.osintessentials.com/](https://www.youtube.com/redirect?event=video_description\&redir_token=QUFFLUhqbjZma18zaGtRWjRBX1dnalFnSzlDVTdJQ3JnZ3xBQ3Jtc0trVlU3QnNTV2VlZlpSRUphbXBlY2tVRDU4VjlIWE5xTTZYdEZCZGprekg4b3pqb0tEUUJXLWM4U3gyalpSVDA4SGh1MFlUM2pDZVJxNWdnUmZZbjdIODJ5Q185WGVWMFdsWEw4UTFUVThEV0RRVmpVOA\&q=https%3A%2F%2Fwww.osintessentials.com%2F\&v=HORzekIiZZ0)&#x20;

[https://randhome.io/blog/2019/01/05/2...](https://www.youtube.com/redirect?event=video_description\&redir_token=QUFFLUhqbVo3RFVBUUtOUDVZVjhqWWRfM3ZqcDV2MGpPQXxBQ3Jtc0tuLXFDa2JySVRKNEhIZ1pqX2pHbGY0eno0Rm80cm5oMjduZ0tFQlNTRHphWDVoNWh6c3h2ZzBURDNqRnJJeks4c3ktbUF6akdBVjY4VGNRRE9SM3FUellEb0paSjEwcFdiT2lJbUp6ZkJQcEREYmYzRQ\&q=https%3A%2F%2Frandhome.io%2Fblog%2F2019%2F01%2F05%2F2019-osint-guide%2F\&v=HORzekIiZZ0)&#x20;

[https://www.aware-online.com/en/osint...](https://www.youtube.com/redirect?event=video_description\&redir_token=QUFFLUhqbG5uMTVBWUZ0Tlp2Z25mcF9qTDJNREZWM19UZ3xBQ3Jtc0tsWlhhTTRxQ2E3WGlvNEtaTnRPSUM1Zy1aRG11YzZ5c1I5Y2lfTVZjZ2xyLWVZVnZWWjlCYVlBR2l6QkV0QWtXQmNBNWhVTjE1eWN4UVFRaUViUVphaGFXSFZwU2cxQkNFR3FVeHVUTmxya3pxRGdYOA\&q=https%3A%2F%2Fwww.aware-online.com%2Fen%2Fosint-tools%2F\&v=HORzekIiZZ0)&#x20;

[https://osintframework.com/](https://www.youtube.com/redirect?event=video_description\&redir_token=QUFFLUhqbkRBWEZGU3dHSndvN1FqVmJOUDBZTnphV2x6UXxBQ3Jtc0tsQVBNYUloWmVmR1RNTXVDTG4zaW96OXBjWGM1bmluaTl4LWlDelpRWmpGWE5UMmo3dVlGUXlKdnByUUNidUlQZ3JNbWZsSk45cnJ4WVBMa0xPMHR6aDZsdFVDbEpLZGxIZTUxMTEwUVNaVWVkVzk4bw\&q=https%3A%2F%2Fosintframework.com%2F\&v=HORzekIiZZ0)&#x20;

[https://www.osintcurio.us/](https://www.youtube.com/redirect?event=video_description\&redir_token=QUFFLUhqbXlCTjY1UUlfNXBOYnhrdTdXUDd3SGphc2JNUXxBQ3Jtc0trTGZHT3hkMDFsMXdVWWlaTmk5eWlZaFdLMWZwNEpJR1dISUhTTUpHT0RTRnk3RG9hc2YycHNPaUZ5N2VIWDRVeGVqTnFnWFZWWTJnaTl3V3VKdGRZSzE1ajBRNjlpM0xOSllGY2s4NVp3cEFZMzZwZw\&q=https%3A%2F%2Fwww.osintcurio.us%2F\&v=HORzekIiZZ0) &#x20;







#### Face recognition

* facecheckid.com



Collecting Proxy Data

> Data Form Cracked.io[> \
> https://github.com/TheSpeedX/PROXY-List/tree/master> \
> https://proxylist.to/> \
> http://www.proxydb.net/> \
> https://hidemy.name/es/proxy-list](https://github.com/TheSpeedX/PROXY-List/tree/masterhttps://proxylist.to/http://www.proxydb.net/https://hidemy.name/es/proxy-list/)



## SOCK PUPPET

> Online identify that is fake account



## My process for setting up anonymous sockpuppet accounts.

![](https://www.redditstatic.com/desktop2x/img/renderTimingPixel.png)[How-To](https://www.reddit.com/r/OSINT/search?q=flair_name%3A%22How-To%22\&restrict_sr=1)

This is my process for setting up an anonymous sockpuppet account.

1. Come up with a persona for the sockpuppet account.
2.  Use [Fake Name Generator](https://www.fakenamegenerator.com/)

    &#x20;to create a person whom you feel fits your sockpuppet persona.
3.  Use [This Person Does Not Exist](https://www.thispersondoesnotexist.com/)

    &#x20;to generate an image. Make sure you inspect the image closely and get one that doesn't have any obvious flaws, as they often do. It is worth picking up some Photoshop, GIMP, Affinity Photo or Designer, or other basic image manipulation skills to fix them and change the background of the image.
4. Get a burner phone, completely wiped and fresh. Can be any brand that will accept a Mint Mobile SIM card.
5.  Get a burner credit card from [Privacy.com](https://privacy.com/)

    &#x20;to use for on Amazon and possible the Mint Mobile setup. They might need it to set up the account.
6. Set up a burner Amazon account. We're only going to use it once.
7. Buy two Mint Mobile SIM cards. You can find them various places online and in stores near you, but you can get two of them for $5 on Amazon. They also give you 1 week free trial with something like 100 text messages, which we're going to use. This gives you two cards for two sockpuppet accounts for only $5.
8. I like to use Amazon to have the card sent to an Amazon pickup box, which can be anonymous.
9. Get a VPN that you can set to the physical area in which you want your sockpuppet to "exist."
10. Set up the Mint Mobile trial account somewhere away from your home; as far as you're willing to go.
11. Use this Mint Mobile trial phone number to set up all of the websites you need.
12. I recommend at least set up a Google account and Protonmail account. Both will come in handy at different times.
13. Once you've set up all the accounts with your trial Mint SIM, set up 2FA on all of the accounts.
14. After setting up 2FA on all of the accounts, change the phone number to one you have more permanent access to, such as MySudo or Google Voice.
15. Make sure everything works!
16. Destroy the SIM card.
17. Wipe the phone.

A lot of these websites are blocking MySudo, Google Voice, and other VoIP numbers. That's why we go through the Mint phone number first.

They should be less stringent now.



#### Reference Link



[https://www.reddit.com/r/OSINT/comments/dp70jr/my\_process\_for\_setting\_up\_anonymous\_sockpuppet/](https://www.reddit.com/r/OSINT/comments/dp70jr/my_process_for_setting_up_anonymous_sockpuppet/)

{% embed url="https://garrettmickley.com/sockpuppet-account-creation/" %}
