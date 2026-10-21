# Generates legal + trade pages into ../public. Run: python3 tools/gen.py
import os,json,re
ROOT=os.path.join(os.path.dirname(__file__),'..','public')
SITE='https://crewwear-site.imransidd-co.workers.dev'   # change when the real domain is live
BRAND='CrewWear Custom'

HEAD='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{site}/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0E1B2C">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Lora:ital,wght@1,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
{ld}
</head>
<body>
'''
NAV='''<header class="nav"><div class="wrap">
<a href="/" class="logo"><i>CW</i>CrewWear Custom</a>
<nav><a href="/#trades">Trades</a><a href="/#products">Products</a><a href="/#bundles">Bundles</a><a href="/#how">How it works</a><a href="/#faq">FAQ</a></nav>
<a href="#design" class="btn btn-p">Get free design</a>
</div></header>
'''
FOOT='''<footer><div class="wrap">
<div><b>CrewWear Custom</b>Full-print custom uniforms for US trade businesses.</div>
<div><b>Trades</b><a href="/hvac">HVAC</a><a href="/plumbing">Plumbing</a><a href="/roofing">Roofing</a><a href="/landscaping">Landscaping</a><a href="/pressure-washing">Pressure washing</a></div>
<div><b>Company</b><a href="/#products">Products</a><a href="/#bundles">Bundles</a><a href="/#faq">FAQ</a><a href="/returns">Returns &amp; shipping</a><a href="/terms">Terms</a><a href="/privacy">Privacy</a></div>
</div></footer>
<script src="/config.js"></script><script src="/app.js"></script>
</body></html>
'''
STICKY='<div class="sticky"><a href="#design" class="btn btn-p">Get free design</a><a href="#" data-book class="btn btn-o" hidden>Book a call</a></div>\n'

def form(idp='lead'):
    return ('''<section id="design"><div class="wrap" style="max-width:720px">
<p class="eyebrow">Free design</p>
<h2>Get your free design <em>today</em></h2>
<p class="lead" style="margin-bottom:22px">Tell us who you are and we'll email your mockup within 24 hours. No obligation.</p>
<div class="formbox">
<form class="lead-form" id="%s" novalidate>
<div id="bsum" class="bsum" hidden></div>
<input type="hidden" name="bundle" id="bundleField">
<div class="hp" aria-hidden="true"><label>Leave empty<input name="botcheck" tabindex="-1" autocomplete="off"></label></div>
<div class="two">
<label>Your name<input name="name" required autocomplete="name" placeholder="Jane Smith"></label>
<label>Business name<input name="business" required autocomplete="organization" placeholder="Smith Heating &amp; Air"></label>
</div>
<div class="two">
<label>Email<input name="email" type="email" required autocomplete="email" placeholder="you@company.com"></label>
<label>Phone<input name="phone" type="tel" required autocomplete="tel" placeholder="(555) 123-4567"></label>
</div>
<label>Your trade<select name="trade"><option>HVAC</option><option>Plumbing</option><option>Roofing</option><option>Landscaping</option><option>Pressure washing</option><option>Other</option></select></label>
<label>Anything we should know? (optional)<textarea name="message" rows="3" placeholder="Colours, logo link, crew size, deadline…"></textarea></label>
<button class="btn btn-p" type="submit">Send me my free design →</button>
<p class="fmsg" role="status"></p>
<p class="note">We only use your details to send your design and quote. See our <a href="/privacy" style="text-decoration:underline">privacy policy</a>.</p>
</form></div>
<p class="callrow">Prefer to talk? <a href="#" data-book hidden>Book a quick call</a></p>
</div></section>
''').replace('%s',idp)

def write(name,html):
    open(os.path.join(ROOT,name+'.html'),'w').write(html)

def legal(slug,title,desc,body):
    url=f'{SITE}/{slug}'
    h=HEAD.format(title=title+' | '+BRAND,desc=desc,url=url,site=SITE,ld='')+NAV.replace('href="#design"','href="/#design"')
    h+=f'<div class="pagehead"><div class="wrap"><h1>{title}</h1><p>Last updated: October 2026</p></div></div>\n<main class="prose">{body}</main>\n'+FOOT
    write(slug,h)

PRIVACY='''
<p>This policy explains what information CrewWear Custom ("we", "us") collects through this website, how we use it, and the choices you have.</p>
<h2>Information we collect</h2>
<ul><li><b>Details you give us:</b> your name, business name, email address, phone number, trade, notes, logo files and order details when you request a design or place an order.</li>
<li><b>Usage data:</b> basic information such as pages viewed, device and browser type, and approximate location, collected through cookies and similar tools such as analytics and advertising pixels.</li></ul>
<h2>How we use it</h2>
<ul><li>To create your free design, send you a quote, and follow up about your order.</li>
<li>To process payments, produce and ship your order, and give you support.</li>
<li>To understand how the site is used and to improve it and our advertising.</li>
<li>To meet legal and tax obligations.</li></ul>
<h2>Who we share it with</h2>
<p>We do not sell your personal information. We share it only with service providers that help us run the business, for example website hosting, form and email delivery, payment processing, manufacturing partners, shipping carriers, and analytics and advertising platforms. They may use it only to provide their service to us.</p>
<h2>Cookies and tracking</h2>
<p>We may use cookies and tools such as Google Analytics and the Meta pixel to measure traffic and the performance of our ads. You can block or delete cookies in your browser settings and can opt out of ad personalisation through your ad settings on those platforms.</p>
<h2>How long we keep it</h2>
<p>We keep your information as long as needed for the purposes above, including to meet legal, tax and accounting requirements, and then delete or anonymise it.</p>
<h2>Your choices and rights</h2>
<p>You can ask us to access, correct or delete the personal information we hold about you, or to stop marketing messages, at any time. Depending on where you live, such as California and other US states, you may have additional rights under local privacy laws. Contact us through the form on our <a href="/#design">homepage</a> and we will respond within a reasonable time.</p>
<h2>Security</h2>
<p>We use reasonable measures to protect your information, but no method of transmission or storage is completely secure.</p>
<h2>Children</h2>
<p>Our services are for businesses and are not directed to children under 16.</p>
<h2>Changes</h2>
<p>We may update this policy from time to time. The date above shows when it was last changed.</p>
'''

TERMS='''
<p>These terms apply to your use of this website and to orders placed with CrewWear Custom ("we", "us"). By requesting a design or placing an order you agree to them.</p>
<h2>Our service</h2>
<p>We make custom, made-to-order work apparel, including fully printed (dye-sublimated) polyester garments and logo-decorated fleece and cotton-blend garments. Every order is produced specifically for you from the design you approve.</p>
<h2>Free design and quotes</h2>
<p>Design mockups are free and come with no obligation. Quotes show the items, quantities, price and delivery details, and are valid for the period stated on the quote. Prices and bundle contents on this website are for guidance and are confirmed on your quote.</p>
<h2>Approving your design</h2>
<p>Production starts only after you approve the final design in writing and pay the deposit. Please check names, spelling, phone numbers, colours and sizes carefully. Because production follows your approved file, we are not responsible for errors that were in the design you approved.</p>
<h2>Your artwork</h2>
<p>You confirm that you own, or have permission to use, the logos and artwork you send us, and that they do not infringe anyone else's rights. We may decline artwork that is unlawful or infringing.</p>
<h2>Payment</h2>
<p>A deposit is due before production, with the balance due as stated on your quote. Payments are taken through a secure payment link.</p>
<h2>Production, delivery and colour</h2>
<p>Production and delivery times are estimates confirmed on your quote and may be affected by factors outside our control such as carrier delays and customs. Printed colours can differ slightly from what you see on a screen, and the same design can look slightly different across fabrics and garment types.</p>
<h2>Returns, replacements and refunds</h2>
<p>See our <a href="/returns">Returns &amp; shipping</a> page.</p>
<h2>Liability</h2>
<p>To the fullest extent allowed by law, our total liability for any claim relating to an order is limited to the amount you paid for that order. We are not liable for indirect or consequential losses such as lost profits. Nothing in these terms limits liability that cannot be limited by law.</p>
<h2>Website use</h2>
<p>This website is provided "as is". Do not misuse it, attempt to disrupt it, or copy its content or images without our permission.</p>
<h2>Changes</h2>
<p>We may update these terms. The version published here when you place an order applies to that order.</p>
<h2>Contact</h2>
<p>Questions about these terms? Reach us through the form on our <a href="/#design">homepage</a>.</p>
'''

RETURNS='''
<p>Every item we make is custom. Here is how returns, replacements and shipping work.</p>
<h2>Made-to-order items</h2>
<p>Because each order is printed or decorated specifically for your business, we cannot accept returns or exchanges for change of mind, wrong size ordered, or errors in a design you approved.</p>
<h2>If something is wrong with your order</h2>
<p>We will reprint or replace, or refund where a replacement is not possible, if your order arrives:</p>
<ul><li>with a manufacturing or print defect,</li><li>damaged in transit, or</li><li>not matching your approved design or the quantities and sizes you ordered.</li></ul>
<p>Tell us within 7 days of delivery through the form on our <a href="/#design">homepage</a>, include your order details and clear photos of the problem, and we will make it right.</p>
<h2>Sizing</h2>
<p>Please check the size guidance before ordering. We are happy to help you choose sizes for your crew when you request your design.</p>
<h2>Shipping</h2>
<ul><li>Orders of $200 or more ship free.</li>
<li>Production and delivery times, and the delivery fee for smaller orders, are shown on your quote before you pay.</li>
<li>Orders are produced and shipped from outside the United States. Any import duties or taxes that apply will be explained on your quote so there are no surprises.</li>
<li>You will receive tracking details once your order ships.</li></ul>
<h2>Cancellations</h2>
<p>You can cancel before you approve your design at no cost. After approval and deposit, production begins, so deposits are not refundable once production has started.</p>
'''

legal('privacy','Privacy Policy','How CrewWear Custom collects, uses and protects your information.',PRIVACY)
legal('terms','Terms of Service','Terms for using the CrewWear Custom website and placing custom apparel orders.',TERMS)
legal('returns','Returns & Shipping','Returns, replacements and shipping for custom orders from CrewWear Custom.',RETURNS)

# ------------- trade pages -------------
IMG={'hvac':[('hoodie-sub-front.webp','Full-print hoodie, front'),('hoodie-sub-back.webp','Hoodie back with phone number'),('fleece-front.webp','Fleece hoodie, logo'),('fleece-back.webp','Fleece hoodie, back logo')],
'plumbing':[('plumbing-hoodie-front.webp','Hoodie, front'),('plumbing-hoodie-back.webp','Hoodie back with services'),('plumbing-long-front.webp','Long sleeve, front'),('plumbing-long-back.webp','Long sleeve back with phone')],
'pressure-washing':[('long-front.webp','Long sleeve, front'),('long-back.webp','Long sleeve back with services'),('tee-front.webp','Short sleeve tee'),('polo-front.webp','Polo shirt')]}
SINGLE={'plumbing':'plumbing-hero.webp'}
PAIR={'hvac':('hoodie-sub-front.webp','fleece-front.webp'),'plumbing':('plumbing-hoodie-front.webp','plumbing-long-back.webp'),'pressure-washing':('long-front.webp','tee-front.webp')}
T={
'hvac':dict(name='HVAC',h1='Custom HVAC uniforms that <em>sell</em> before you speak',
 sub='Full-print hoodies, long sleeves, polos and caps for heating and cooling crews. Your logo, your colours, your phone number, all over the garment.',
 title='Custom HVAC Uniforms & Work Hoodies',desc='Custom full-print HVAC uniforms, hoodies, long sleeves, polos and caps. Free design in 24 hours. Free delivery on orders $200+.',
 why=[('Look like a company','A crew in matching ice-and-flame gear looks established the moment it steps out of the van.'),('Your number on every back','Your phone number and services printed edge to edge turns every job site into a billboard.'),('Built for the attic and the roof','Lightweight polyester that breathes in summer, with hoodies and layers for winter call-outs.')],
 faq=[('Can the design show heating and cooling?','Yes. A frost and flame theme is our most popular HVAC look, and we can match it to your logo colours.'),('Can I put each technician name on the sleeve?','Yes. Names and crew numbers can be added per person.')]),
'plumbing':dict(name='Plumbing',h1='Custom plumbing uniforms your customers <em>remember</em>',
 sub='Full-print hoodies, long sleeves, polos and caps for plumbing crews. Water, steel and copper themes in your own colours.',
 title='Custom Plumbing Uniforms & Work Shirts',desc='Custom full-print plumbing uniforms, hoodies, long sleeves, polos and caps. Free design in 24 hours. Free delivery on orders $200+.',
 why=[('Trust at the door','Matching, clean uniforms tell homeowners they are letting in a professional business.'),('Your brand in every kitchen and basement','Your logo and number printed edge to edge stays visible when crews are bending, kneeling and reaching.'),('Made for wet, messy work','Moisture-wicking polyester dries fast and prints that cannot peel or crack.')],
 faq=[('Can you match my van wrap colours?','Yes. Send your logo and van photo and we will match the colours.'),('Can I get polos for office staff?','Yes. Mix polos, tees, hoodies and caps in one order or in a bundle.')]),
'roofing':dict(name='Roofing',h1='Custom roofing crew gear that handles the <em>heat</em>',
 sub='Full-print long sleeves, hoodies, tees and caps for roofing crews. Light polyester that keeps cooler in the sun, with your brand on every piece.',
 title='Custom Roofing Crew Uniforms & Sun Shirts',desc='Custom full-print roofing uniforms, sun-ready long sleeves, hoodies, tees and caps. Free design in 24 hours. Free delivery on orders $200+.',
 why=[('Sun-ready long sleeves','Lightweight long sleeves cover arms from the sun, and the full-print design keeps your brand visible from the street.'),('Seen from the ground','Big back prints with your name and number work like a moving sign on every roof and every lot.'),('One look for the whole crew','Crews, foremen and estimators in a matching set look like one serious operation.')],
 faq=[('Is the fabric breathable?','Yes. Our polyester garments are lightweight and moisture-wicking. Exact fabric details are confirmed on your quote.'),('Can I get different looks for crew and office?','Yes. Mix garments and designs in one order.')]),
'landscaping':dict(name='Landscaping',h1='Custom landscaping uniforms that <em>grow</em> your brand',
 sub='Full-print polos, tees, long sleeves, hoodies and caps for lawn and landscape crews. Fresh greens or your own colours, with your logo everywhere.',
 title='Custom Landscaping Uniforms & Crew Shirts',desc='Custom full-print landscaping uniforms, polos, tees, long sleeves and caps. Free design in 24 hours. Free delivery on orders $200+.',
 why=[('Every truck, every yard','A matching crew in bold, clean uniforms makes your business stand out on every street you work.'),('Tough, fade-resistant print','Dye-sublimated print is part of the fabric, so it does not crack or peel after washes and long days.'),('Cool and light','Polyester that breathes in heat, with long sleeves for sun and hoodies for the shoulder seasons.')],
 faq=[('Can the design use my green and brand colours?','Yes. We build the design around your logo and brand colours.'),('How many pieces can I order?','Any quantity. See the bundles for set pricing on crews of different sizes.')]),
'pressure-washing':dict(name='Pressure washing',h1='Custom pressure washing uniforms <em>made</em> to be seen',
 sub='Full-print long sleeves, tees, polos and caps for pressure washing and soft washing crews. Water splashes, your logo, your services and phone number all printed edge to edge.',
 title='Custom Pressure Washing Uniforms & Shirts',desc='Custom full-print pressure washing uniforms, long sleeves, tees, polos and caps. Free design in 24 hours. Free delivery on orders $200+.',
 why=[('Your services on your back','List driveways, roofs, fleets and your phone number across the back so every customer can call you.'),('Made for wet work','Moisture-wicking polyester dries fast and the print cannot peel or fade like a patch or sticker.'),('Crew numbers and flag patches','Add crew numbers, a printed flag and contrast panels for a proper team-kit look.')],
 faq=[('Can the back list my services?','Yes. Phone numbers, email, services and a licensed-and-insured line can all be printed on the back.'),('Do you do hooded sun shirts?','Ask us in the form. We can quote hooded long sleeves for sun protection.')]),
}
urls=[SITE+'/']
for slug,t in T.items():
    url=f'{SITE}/{slug}'; urls.append(url)
    faqld={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a.replace("\\'","'")}} for q,a in t['faq']]}
    svc={"@context":"https://schema.org","@type":"Service","name":f"Custom {t['name']} uniforms","provider":{"@type":"Organization","name":BRAND,"url":SITE},"areaServed":"US","description":t['desc']}
    ld='<script type="application/ld+json">'+json.dumps(svc)+'</script>\n<script type="application/ld+json">'+json.dumps(faqld)+'</script>'
    h=HEAD.format(title=t['title']+' | '+BRAND,desc=t['desc'],url=url,site=SITE,ld=ld)+NAV
    nm=t['name'] if t['name']=='HVAC' else t['name'].lower()
    imgs=IMG.get(slug)
    pr=PAIR.get(slug)
    sh=SINGLE.get(slug)
    hero_img=f'<div class="duo"><div class="it m"><img src="/img/{pr[0]}" alt="{t["name"]} custom hoodie or shirt, front" width="900" height="900"></div><div class="it b"><img src="/img/{pr[1]}" alt="{t["name"]} custom shirt, back" width="900" height="900"></div></div>' if pr and not sh else ''
    if sh: hero_img=f'<img class="himg" src="/img/{sh}" alt="Custom {t["name"]} hoodie and long sleeve work shirt" width="{r.size[0] if False else 1100}" height="900" fetchpriority="high">'
    h+=f'''<section class="thero"><div class="wrap"><div>
<p class="crumb"><a href="/">Home</a> / {t['name']}</p>
<p class="eyebrow">Custom {t['name']} uniforms</p>
<h1>{t['h1']}</h1>
<p class="lead" style="margin:16px 0 22px">{t['sub']}</p>
<div class="cta"><a href="#design" class="btn btn-p">Get my free design →</a><a href="/#bundles" class="btn btn-o">See crew bundles</a></div>
<div class="checks"><span>Free design in 24h</span><span>No setup fees</span><span>Free delivery $200+</span></div>
</div>{hero_img}</div></section>
<section class="stats"><div class="wrap">
<div class="stat"><b>24<small>h</small></b><span>Free design turnaround</span></div>
<div class="stat"><b>$0</b><span>Design &amp; setup fees</span></div>
<div class="stat"><b>100<small>%</small></b><span>Edge-to-edge print</span></div>
<div class="stat"><b>$200<small>+</small></b><span>Ships free</span></div>
</div></section>
<section><div class="wrap"><p class="eyebrow">Why crews choose us</p><h2>Built for {nm} <em>crews</em></h2>
<div class="bullets">'''
    for a,b in t['why']: h+=f'<div class="card"><h3>{a}</h3><p style="color:var(--slate);margin-top:6px;font-size:15px">{b}</p></div>'
    h+='</div></div></section>\n<section class="why"><div class="wrap"><p class="eyebrow">Example designs</p><h2>See what it <em>looks</em> like</h2>'
    if imgs:
        h+='<div class="gal">'+''.join(f'<div class="g"><img src="/img/{f}" alt="{a}" width="900" height="900" loading="lazy"><span>{a}</span></div>' for f,a in imgs)+'</div>'
        h+='<p class="note">Example designs use sample brand names. Yours will carry your logo, colours and phone number.</p>'
    else:
        h+=f'<div class="soon"><b>{t["name"]} example designs are on the way.</b><p style="margin-top:6px">Want to see yours now? Send your logo and we will email a free full-print design within 24 hours.</p><a href="#design" class="btn btn-p" style="margin-top:12px">Get my free design</a></div>'
    h+='</div></section>\n<section><div class="wrap" style="max-width:780px"><p class="eyebrow">FAQ</p><h2>Questions from <em>'+nm+'</em> crews</h2>'
    for q,a in t['faq']+[('How fast do I get my design?','Within 24 hours of your request. Production starts after you approve it.'),('What is the minimum order?','Details are confirmed on your quote. Send your design request and we will advise for your crew size.')]:
        h+=f'<details><summary>{q}</summary><p>{a.replace(chr(92)+chr(39),chr(39))}</p></details>'
    h+='</div></section>\n'+form(f'lead-{slug}')+STICKY+FOOT
    write(slug,h)

for s in ('privacy','terms','returns'): urls.append(f'{SITE}/{s}')
open(os.path.join(ROOT,'sitemap.xml'),'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{u}</loc></url>\n' for u in urls)+'</urlset>\n')
open(os.path.join(ROOT,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')

# ---- patch the homepage ----
p=os.path.join(ROOT,'index.html'); h=open(p).read()
h=re.sub(r'<section id="design">.*?</section>\n',form('lead'),h,count=1,flags=re.S)
for nm,slug in (('HVAC','hvac'),('Plumbing','plumbing'),('Roofing','roofing'),('Landscaping','landscaping'),('Pressure washing','pressure-washing')):
    h=re.sub(r'<a class="trade" href="[^"]*">(<i>[^<]*</i>'+nm+')',r'<a class="trade" href="/'+slug+r'">\1',h)
h=re.sub(r'<footer>.*?</footer>',FOOT.split('<script')[0].replace('href="#design"','href="#design"'),h,count=1,flags=re.S)
if '/app.js' not in h: h=h.replace('</body>','<script src="/config.js"></script><script src="/app.js"></script>\n</body>')
if 'favicon.svg' not in h: h=h.replace('<link rel="stylesheet" href="/style.css">','<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n<link rel="stylesheet" href="/style.css">')
h=h.replace('<meta property="og:image" content="/img/hero.webp">','<meta property="og:image" content="'+SITE+'/img/og.png">\n<meta property="og:url" content="'+SITE+'/">\n<meta name="twitter:card" content="summary_large_image">')
h=h.replace('<div class="sticky"><a href="#design" class="btn btn-p">Get free design</a><a href="#bundles" class="btn btn-o">Bundles</a></div>','<div class="sticky"><a href="#design" class="btn btn-p">Get free design</a><a href="#bundles" class="btn btn-o">Bundles</a></div>')
open(p,'w').write(h)
print('done',len(urls),'urls')
