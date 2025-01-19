---
description: >-
  API is not a programming language it's a set of rules that allows different
  software application to communicate with each other.
---

# Application Programming Language Testing

## API TESTING

> API Testing involves finding vulnerabilities like SQL injection which can affect how APIs handle and transmit data.

### API RECON

> Gathers as much information as possible about APIs such as endpoints how they receive and handles request and where they are located on the server.

### Discovering The API

> Some API documentation is machine-readable providing instruction on how to use and integrate the API.

There are API Scanner that can be used:

> Examples are &#x20;
>
> /api&#x20;
>
> /openapi.json&#x20;

> If you find an endpoint with a resource, try to investigate the PATH like /api/servicename/v1/users/123 then try to /api/servicename/v1 or /api/servicename/ or /api

> Automate the process using OPENAPI parser and scanner like BWAP Scanner &#x20;
>
> * link: [https://portswigger.net/bappstore/6bf7574b632847faaaa4eb5e42f1757c](https://portswigger.net/bappstore/6bf7574b632847faaaa4eb5e42f1757c)&#x20;

### Find the API Endpoints

> By browsing the web application there is information on API like /api/ also look for JavaScript and for more heavy wait extraction use JS Link Finder BApp Link: [https://portswigger.net/bappstore/0e61c786db0c4ac787a08c4516d52ccf](https://portswigger.net/bappstore/0e61c786db0c4ac787a08c4516d52ccf)&#x20;

### Interacting The Endpoints

> Onces, you find the endpoint you can interact with using burp repeater and intruder this help to discover attacks surface like changing the HTTP or media type

### Identifying HTTP Methods

> GET > Is get data from the resources.&#x20;
>
> PATCH > Applies partial changes.&#x20;
>
> OPTIONS >>GET information on the type of request method used on the resources.&#x20;

* Endpoints support different HTTP methods therefore it important to check all the HTTP methods and investigate API endpoints

Example:

> api/task/&#x20;
>
> GET /api/tasks >> get the data&#x20;
>
> POST /api/tasks >> create new task&#x20;
>
> DELETE /api/tasks/1 delete task.&#x20;

### Find Supported Content-Type

* API use specific data format, and they have behave differently depending on the content-type of data provided in request, changing the content-type may.&#x20;
  * Trigger error which discloses useful information.&#x20;
  * Use advantage of different in process in logic:  an API is secure handling JSON but susceptible (effected) when dealing with XML.&#x20;
  * &#x20;To do that change the content-type header and use content-type converter BAPP link : [https://portswigger.net/bappstore/db57ecbe2cb7446292a94aa6181c9278](https://portswigger.net/bappstore/db57ecbe2cb7446292a94aa6181c9278)&#x20;

### Testing Mass Assignments

> It finds the hidden parameter in the JSON Data by manually finding object return by API Means you have request GET /api/users/123 where its response is JSON Data

```
{  

"id": 123,  

"name": "John Doe",  

"email": "john@example.com",  

"isAdmin": "false"  

} 
```

> Change the isadmin parameter to something else and see the response its may give error so change to True.

```
{  

"username":  

"wiener",  

"email": "wiener@example.com",  

"isAdmin": true,  

} 
```

> If this request is connected to isAdmin without any security, then the winer user may get admin privileges

### Prevent API Vulnerabilities

* Securely document the API don't publish it.&#x20;
* Apply and Access list of HTTP method to be permitted.&#x20;
* Validate that the content-type is requested in every request.&#x20;
* Use generic error so the attacker can’t user this information.&#x20;
