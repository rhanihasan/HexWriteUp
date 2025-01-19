# OPEN REDIRECT AND XML ENTERY



Open Redirection

* Redirect from one website to another&#x20;

example

Seen a URL like abc.com/?url=xyz.com&#x20;

* there is redirection happing from abc.com to xyz.com we is happen to change the url of xyz to attacker.com == abc/?url=atttacker.com then its redirect to attacker website which is called open redirect
* Open redirect comes from the facts that it allows to redirect to any website on the planet&#x20;
* Why its need redirection?
  * Web application required this redirection for login, register, checkout, create, password reset.
* there are server side and client-side redirection.
* client side&#x20;
  * using JavaScript which is windows.location object
  * using html which is meta tags

> Open redirect are very common its find many in Facebook and google. so open redirect is a security threads ? it depends.
>
> the simple security threads is phishing&#x20;
>
> * https://www.google.com/serach?aiubaeif=//attacker.com&#x20;
>   * to obverse right
> * https://www.google.com/search?akjabsd://%61%75%234%7623E%8723
>   * URL Encoded&#x20;
>   * Now you have to decode every time to see where you are been redirected.
> * The point here is people are easy to trick which has no knowledge about this thing.
> * I am sick on this social engineering stuff and i know its not hacking..

* &#x20;there are many framework of open redirctoer which developer used without knowing that this can redirect into anywhere in the worlds , wrost they used as a part of password reset links.which could lead into account takeover in some cases.
* localhost/password\_reset?token=12873712876ajwdaiwuey81726\&next=/login
  * There are two parameters first is the token and second is the next
  * if change the localhost/password\_reset?token=12873712876ajwdaiwuey81726\&next=/attacker.com
  * then the token get leaks in the reference header when request is made.





HTTP Parameter Pollutions

* Send the same http parameter mulitply times.
  * deltails/?user=hasan\&user=rhani&#x20;
  * which one gonna be accept ?
  * well its depends on the backlend server.
    * some server retuens 1 value and some server return last value and some retuen everything.
      * JSP + Tomcat will return 1 value.
      * PHP + Apache will return last value
      * ASP + IIS will return everything concatenate.
    * Why are they different implementation ?
      * there is no standard way to accept http parameters so now  its a mess.
* shares.php?u=\[link]\&quote=cats\&dogs
  * the & >> is not encoded which means that can inject own parameters&#x20;
  * shares.php?u=\[link]\&quote=cats\&dogs=test\&u=attavker.com
  * so its just share the attacker website instead of the share post.
* Assume the bank which  transhfer money. appon inpection there are two parameters amount=20\&to=hasan.
  * After the requesst hits the server the server will make another request from the backend to the payment gateway , payment gateway  is respponsible for handling the actual money transfer request to the payment gateway is http://payment-gatewaay.com:8080/?fromattacker\&tohasan\&amount=10&#x20;
  * from parameter is extra paramter which is not diretcly coming from the website itself  because the attacker could modify and steal all the moeny so to prevent this server uses your cookie to get name and then add it at the backend requesst so that you have no way of changing the value now&#x20;

<img src="../../.gitbook/assets/file.excalidraw (3).svg" alt="The Bank HPP" class="gitbook-drawing">

HPP + Other BUGs >> Bypass Web Application Firewall.

<img src="../../.gitbook/assets/file.excalidraw (4).svg" alt="Bypass WAF using HPP" class="gitbook-drawing">



Insecure Direct Object Reference (IDOR)

```
website.com/accounts?user_id=10
```

* What will happened if the number 10 is modify to some any number?
  * it will show error. OR it will show any another user details&#x20;
* IDOR means that the application directly exposes a reference to an object like user details, Files etc.  which can be directly accessed regardless of the authorization



XML External Entities

E<mark style="color:blue;">**x**</mark>tensible <mark style="color:blue;">**M**</mark>arkup <mark style="color:blue;">**L**</mark>anguage

* XML is similar to HTML , HTML is data representation however XML ismore about the data transportation and strograde
* XML is human-readable and used in place like  API , UI  Layout & Styles, application files RSS and more.

Example

```
<?xml version = "1.0"?>  # its used for meta dara
<persion>
    <name>Hasan</name>
    <age>22</age>
</person>
```

* The person tag is the root  elements of the docunment
* inside the root elements there are two more nested tags name and age with some values.
  * tags name are case sensitive.
  * certain characters like quotes , brackets are not allowed.
* Entities are like variable for XML,  this entites are define in the seprate part of XMLdocment called document type defination or DTD

Example

<img src="../../.gitbook/assets/file.excalidraw (5).svg" alt="XML Entities Example" class="gitbook-drawing">

* there are three types of Entities&#x20;
  * General,
  * Parameter,
  * Predefined
* General Entites are some value which is refered somewhere else.

<img src="../../.gitbook/assets/file.excalidraw (6).svg" alt="Types of XML Entity" class="gitbook-drawing">



* External Entities
  * are just like variable which stored value and used later on. but XML is much more then that.\\
  * Entities can also pull value from the local files  or fetch the remote data over the network and stored them as a Entitles.

<pre><code>&#x3C;?xml version="1.0">
&#x3C;!DOCTYPE XXE[
    &#x3C;!ENTITY Hasan <a data-footnote-ref href="#user-content-fn-1">SYSTEM </a>"<a data-footnote-ref href="#user-content-fn-2">robot.txt</a>"?
]>
&#x3C;person>$hasan&#x3C;?person>
</code></pre>

* This called as XXE (XML External Entity)
* Types of XXE&#x20;
  * in band.: Where the XML will parse the output will be shown redirect on screen.
  * error based.: Its a blind XEE, mostly error is visible.
  * Out of Band.: true Blind. No Output

[^1]: Keyword which used by XML to know that Entity types is external,  Telling the XML fetch the external recourse and store inside the entity \
    if it similar to XML TAG then it will output the error as XML Parsering Fail.

[^2]: File Content, it not a file name\
    XML Accept any valid URI : file,http,ftp etc
