from PIL import Image, ImageEnhance
im=Image.open('/mnt/data/Nexweb_ webs amb sentit per a negocis locals.png').convert('RGB')
crops={'hero':(396,46,687,345),'shop':(87,632,296,755),'salon':(319,632,527,755),'restaurant':(551,632,758,755),'craft':(30,855,325,1111),'cafe':(30,1415,260,1535)}
for name,area in crops.items():
 a=im.crop(area)
 a.save(f'/mnt/data/nexweb/assets/{name}.webp','WEBP',quality=89,method=6)
