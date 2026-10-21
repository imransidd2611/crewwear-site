(function(){
var C=window.CW_CONFIG||{};
// analytics
if(C.ga4){var s=document.createElement("script");s.async=true;s.src="https://www.googletagmanager.com/gtag/js?id="+C.ga4;document.head.appendChild(s);window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};gtag("js",new Date());gtag("config",C.ga4)}
if(C.metaPixel){!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version="2.0";n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");fbq("init",C.metaPixel);fbq("track","PageView")}
// booking buttons
document.querySelectorAll("[data-book]").forEach(function(a){if(C.bookingUrl){a.href=C.bookingUrl;a.hidden=false}else a.hidden=true});
// forms
document.querySelectorAll("form.lead-form").forEach(function(form){
form.addEventListener("submit",function(e){
e.preventDefault();
var btn=form.querySelector("button[type=submit]"),msg=form.querySelector(".fmsg");
msg.textContent="";msg.className="fmsg";
var d=new FormData(form);
if(d.get("botcheck")){return}
if(!C.web3formsKey){msg.textContent="Our form is being connected. Please try again shortly.";msg.className="fmsg err";return}
var p={access_key:C.web3formsKey,subject:"New CrewWear lead: "+d.get("business"),from_name:"CrewWear Custom website",name:d.get("name"),business:d.get("business"),email:d.get("email"),phone:d.get("phone"),trade:d.get("trade"),bundle:d.get("bundle")||"(none chosen)",message:d.get("message")||"",page:location.pathname,botcheck:""};
btn.disabled=true;var old=btn.textContent;btn.textContent="Sending…";
fetch("https://api.web3forms.com/submit",{method:"POST",headers:{"Content-Type":"application/json",Accept:"application/json"},body:JSON.stringify(p)})
.then(function(r){return r.json()}).then(function(j){
if(!j.success)throw new Error(j.message||"failed");
if(window.gtag)gtag("event","generate_lead");if(window.fbq)fbq("track","Lead");
var box=form.closest(".formbox")||form.parentNode;
box.innerHTML='<div class="thanks"><h3>Thanks, '+(String(d.get("name")).split(" ")[0]||"")+'! You\'re in.</h3><p>We\'ll email your free design to <b></b> within 24 hours. To speed things up, reply to our email with your logo and brand colours.</p>'+(C.bookingUrl?'<p>Want to talk it through sooner?</p><a class="btn btn-p" href="'+C.bookingUrl+'">Book a quick call</a>':'')+'</div>';
box.querySelector("b").textContent=d.get("email");
}).catch(function(){btn.disabled=false;btn.textContent=old;msg.textContent="Something went wrong sending that. Please try again.";msg.className="fmsg err"});
})});
})();
