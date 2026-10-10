# Edició visual dels continguts (Pages CMS)

Aquesta versió incorpora un editor visual de textos i fotografies. **No cal editar HTML** per canviar els camps disponibles al panell.

## Primera configuració (una vegada)

1. Crea un repositori **privat** a GitHub i puja-hi el **contingut de la carpeta `nexweb-cms`** (el fitxer `.pages.yml` ha de quedar a l'arrel). Si publiques el repositori, els fitxers seran visibles públicament.
2. Entra a https://app.pagescms.org, identifica't amb GitHub i autoritza l'aplicació per al repositori. Selecciona el repositori i la branca principal.
3. Obre **Textos i fotografies de Nexweb**. Modifica els textos o selecciona **Fotografies** per carregar i canviar imatges. Desa els canvis; es registren al repositori.
4. A Netlify, fes **Add new project > Import an existing project > GitHub**, selecciona aquest repositori i deixa el directori de publicació com `.` (carpeta arrel). Sense comanda de compilació.
5. Publica i obre la URL de Netlify: els canvis desats al CMS es desplegaran automàticament quan Netlify els detecti.

**Important:** Arrossegar una carpeta a Netlify Drop no crea la connexió contínua amb GitHub; cal fer el pas 4 per publicar automàticament els canvis del panell. Pages CMS utilitza l'inici de sessió amb GitHub, i no constitueix un administrador natiu dins la web de Nexweb.

## Comprovar el lloc abans de publicar

Al directori del projecte, executa `python -m http.server 8000` i obre `http://localhost:8000`. No obris `index.html` amb file:// per provar modificacions del CMS: per seguretat, els navegadors bloquegen la lectura de JSON local.

## Abast de l'editor

El panell cobreix textos principals, serveis, beneficis, procés, plans, respostes freqüents i fotografies. Textos estructurals i legals, preguntes de FAQ, etiquetes de formulari i menú continuen dins del codi. Es poden afegir com a camps editables en una ampliació.

# Nexweb · lloc web responsive

## Provar la web
Obriu `index.html` o executeu `python -m http.server 8000` dins aquesta carpeta i visiteu http://localhost:8000.

## Pàgines
Inici, Serveis, Com treballem, Plans, Contacte, Avís legal, Privacitat i Cookies. Navegació amb enllaços `.html` aptes per a allotjament estàtic.

## Abans de publicar (imprescindible)
1. Substituïu o verifiqueu els drets d'ús de les fotos provisionals extretes del wireframe proporcionat.
2. Completeu la identitat, NIF/CIF, domicili, contacte i reviseu els textos legals amb assessorament competent.
3. Configureu un servei segur de formularis/API a `assets/config.js`, assignant `window.NEXWEB_FORM_ENDPOINT` a una URL HTTPS que rebi POST JSON, apliqui validació servidor, límits de peticions, mesures antispam i gestioni les dades conforme a la política de privacitat. Sense endpoint, la web NO simula cap enviament.
4. Confirmeu un municipi i una comarca i, si escau, actualitzeu contingut i metadades.
5. Quan tingueu un domini, genereu el sitemap amb URLs absolutes i afegiu-ne la referència a `robots.txt`; configureu URLs canòniques i `og:url`.
6. Per producció, preferiu fonts allotjades localment si les descarregueu sota les llicències corresponents. Les fonts de Google estan carregades mitjançant @import.
7. Comproveu consentiment de cookies si introduïu serveis de seguiment o tercers que ho requereixin.

## Arquitectura
`assets/app.js` conté components reutilitzables en funcions, contingut de pàgines i formulari; `assets/style.css` inclou les variables del sistema de disseny. `assets/config.js` separa la configuració d'enviament. No inclou testimonis o dades inventades.
