/* Traduction en du parcours Espaces verts (générée par generateur/gen_trad.py). Les blocs de code restent ceux de la version française (<!--code:N-->). */
window.TRAD = window.TRAD || {};
window.TRAD.en = Object.assign(window.TRAD.en || {}, {
 "ev": {
  "nom": "Green spaces",
  "accroche": "Green spaces, from the tree to the urban project",
  "lead": "A step-by-step course to understand, design and manage urban green spaces: types and services, a plant palette suited to the Tlemcen climate, tree inventory and assessment, designing a neighbourhood square, planting and water-saving irrigation, maintenance and differentiated management, mapping with QGIS, cost estimate and management plan. Each lesson offers a practical exercise, videos and an end-of-level quiz."
 },
 "v1": {
  "titre": "Understanding urban green spaces",
  "resume": "Define and classify green spaces, know their roles for the city and its inhabitants, and understand the regulatory framework and stakeholders in Algeria.",
  "quiz": [
   {
    "question": "Under Law 07-06, a row of trees along a boulevard belongs to which category?",
    "choix": [
     "Specialised gardens",
     "Private gardens",
     "Tree alignments",
     "Urban parks"
    ],
    "explication": "Trees planted along streets and roads form the tree-alignment category."
   },
   {
    "question": "A district of 20,000 inhabitants has 12 ha of public green space. How many m² per inhabitant?",
    "choix": [
     "0.6 m²/inh.",
     "16 m²/inh.",
     "6 m²/inh.",
     "60 m²/inh."
    ],
    "explication": "12 ha = 120,000 m²; 120,000 ÷ 20,000 = 6 m²/inh."
   },
   {
    "question": "What does the “300” in the 3-30-300 rule mean?",
    "choix": [
     "300 m² of lawn per school",
     "300 trees per district",
     "300 litres of water per tree",
     "No more than 300 m to a green space"
    ],
    "explication": "Every resident should live less than 300 m from a green space."
   },
   {
    "question": "How do trees reduce urban heat islands?",
    "choix": [
     "By absorbing noise",
     "By increasing runoff",
     "By reflecting street-light",
     "Through shade and evapotranspiration"
    ],
    "explication": "Shade and water evaporated by leaves cool the air."
   },
   {
    "question": "Which planning document sets land-use rules sector by sector?",
    "choix": [
     "The POS",
     "The PDAU",
     "The tree inventory",
     "The maintenance specifications"
    ],
    "explication": "The POS details, at sector level, what the PDAU sets at municipal level."
   }
  ]
 },
 "v1-l1": {
  "titre": "What is a green space? Definitions and types",
  "objectifs": [
   "Define an urban green space and its components",
   "Distinguish the main categories of green spaces",
   "Recognise these categories in a city such as Tlemcen"
  ],
  "contenu": "\n<p>A <b>green space</b> is a public or private area largely covered with vegetation (trees, shrubs, lawns, flowers), landscaped or not, located in the city or on its outskirts. It can be large (a park, an urban forest) or very small (a planter, a row of trees along a boulevard).</p>\n<p>A green space is always a <b>living system</b>: soil, water, plants, wildlife (birds, insects, hedgehogs), facilities (paths, benches, play equipment, lighting) and <b>users</b>. Managing it means taking care of all of these at once.</p>\n<h4>The main categories</h4>\n<p>The 2007 Algerian law on green spaces (see lesson 3) distinguishes several categories. They are useful to organise an inventory:</p>\n<ul>\n  <li><b>Urban and peri-urban parks</b>: large areas (often more than a few hectares) with walks, playgrounds, water features, visitor facilities.</li>\n  <li><b>Public gardens</b>: smaller neighbourhood spaces: squares, planted plazas, estate gardens.</li>\n  <li><b>Specialised gardens</b>: botanical garden, rose garden, exhibition garden, arboretum.</li>\n  <li><b>Collective or residential gardens</b>: green spaces at the foot of apartment blocks, schools, hospitals.</li>\n  <li><b>Private gardens</b>: gardens of houses.</li>\n  <li><b>Urban forests</b>: woodland in or next to the city, open for walks.</li>\n  <li><b>Tree alignments</b>: trees planted along streets, boulevards and roads.</li>\n</ul>\n<p>We often add <b>accompanying green spaces</b> (embankments, roundabouts, central reservations) and <b>natural areas</b> (wadi banks, wasteland, hillsides), which also play a major ecological role.</p>\n<h4>Examples around Tlemcen</h4>\n<p>The Lalla Setti plateau (forest and leisure area overlooking the city), the public gardens of the city centre, the hackberry and plane-tree alignments of the main boulevards, the peri-urban olive groves and orchards: each type requires different management.</p>\n<div class=\"astuce\"><b>Key point:</b> classifying green spaces by category is the first step of any assessment. Without a typology, you can neither count, compare nor plan maintenance.</div>",
  "exercice": "<ol>\n  <li>On a map of your city (or in Google Earth), find at least one example of each category.</li>\n  <li>For each example, note: name, category, approximate area, district.</li>\n  <li>Open the <code>espaces_verts.geojson</code> layer from the practical data in QGIS and look at the <code>categorie</code> field: which categories are present in the fictional study area?</li>\n</ol>"
 },
 "v1-l2": {
  "titre": "The roles of green spaces: ecosystem services",
  "objectifs": [
   "List the services provided by green spaces",
   "Explain how trees counter heat islands",
   "Know the main indicators (m² per inhabitant, 3-30-300 rule)"
  ],
  "contenu": "\n<p>Green spaces are not mere “decoration”. They provide the city with <b>ecosystem services</b>, i.e. free benefits supplied by nature.</p>\n<h4>Regulating services</h4>\n<ul>\n  <li><b>Local climate</b>: tree shade and leaf evapotranspiration cool the air. Under a large tree, the felt temperature in summer can drop by several degrees. Green spaces reduce <b>urban heat islands</b> (mineral districts much hotter than their surroundings).</li>\n  <li><b>Water</b>: vegetated soil infiltrates rain, reduces runoff and flooding, recharges aquifers.</li>\n  <li><b>Air and noise</b>: foliage traps part of the dust; thick hedges slightly reduce noise and break the wind.</li>\n  <li><b>Soil</b>: roots hold the soil on embankments and hillsides (erosion control).</li>\n</ul>\n<h4>Supporting services and biodiversity</h4>\n<p>Trees, hedges and meadows offer shelter and food to birds, pollinating insects and small wildlife. Connected together (alignments, wadi banks), they form a <b>green network</b> that lets species move around.</p>\n<h4>Cultural and social services</h4>\n<p>Relaxation, sport, children's play, meeting people, physical and mental health, environmental education, property value, identity and landscape of the city.</p>\n<h4>Some indicators</h4>\n<ul>\n  <li><b>Green space per inhabitant</b> (m²/inh.): total public green space ÷ population. A frequently quoted value (attributed to the WHO) is at least <b>9 m² per inhabitant</b>; many cities aim for 10 to 15 m².</li>\n  <li><b>Canopy cover</b>: share of the area covered by tree crowns, seen from above.</li>\n  <li><b>3-30-300 rule</b>: every resident should see at least <b>3 trees</b> from home, live in a district with <b>30%</b> canopy cover, and live less than <b>300 m</b> from a green space.</li>\n</ul>\n<div class=\"astuce\"><b>Quick calculation:</b> a district of 12,000 inhabitants with 7.2 ha of public green space has 72,000 ÷ 12,000 = <b>6 m²/inh.</b>, below the 9 m²/inh. benchmark.</div>",
  "exercice": "<ol>\n  <li>Choose a green space you know and sort its benefits into the three families (regulation, biodiversity, social).</li>\n  <li>Using the <code>quartiers_population.csv</code> file, compute the green space per inhabitant of each district (field <code>surface_ev_m2</code>).</li>\n  <li>Does the district reach 9 m²/inh.? How many m² would have to be created to reach it?</li>\n</ol>"
 },
 "v1-l3": {
  "titre": "Regulatory framework and stakeholders in Algeria",
  "objectifs": [
   "Know Law No. 07-06 of 13 May 2007 on green spaces",
   "Identify who creates and manages green spaces",
   "Know where to find official texts"
  ],
  "contenu": "\n<p>In Algeria, the reference text is <b>Law No. 07-06 of 13 May 2007 on the management, protection and development of green spaces</b>, published in the Official Journal (JORADP). Its main objectives are:</p>\n<ul>\n  <li>to improve the urban living environment and develop green spaces in every city;</li>\n  <li>to <b>classify</b> green spaces into categories (those seen in lesson 1);</li>\n  <li>to <b>protect</b> classified green spaces against changes of use and damage;</li>\n  <li>to require green spaces to be taken into account in <b>planning instruments</b> (PDAU, POS) and building projects.</li>\n</ul>\n<p>Implementing texts specify the procedures (classification, management, specifications). They change over time: always check the version in force on the Official Journal website.</p>\n<h4>The stakeholders</h4>\n<ul>\n  <li><b>The municipality (APC)</b>: management and maintenance of most public green spaces, often through a green-space department or a municipal company.</li>\n  <li><b>The wilaya</b>: environment directorate, planning directorate, project funding.</li>\n  <li><b>The forest conservation service</b>: peri-urban and recreational forests.</li>\n  <li><b>Companies and design offices</b>: design, planting works, contracted maintenance.</li>\n  <li><b>Associations and residents</b>: planting, awareness-raising, community gardens, reporting damage.</li>\n</ul>\n<h4>Planning documents</h4>\n<p>The <b>PDAU</b> (master plan for development and urban planning) sets the main orientations at municipal level; the <b>POS</b> (land-use plan) specifies the rules by sector. These documents reserve land for future parks and set the required amount of greenery.</p>\n<div class=\"astuce\"><b>Good habit:</b> before any project, ask for the sector's POS and identify existing or planned green spaces. A classified green space cannot become a car park or a building plot.</div>",
  "exercice": "<ol>\n  <li>Find Law No. 07-06 of 13 May 2007 on the Official Journal website (joradp.dz) and write down the exact list of green-space categories.</li>\n  <li>Draw a diagram of the stakeholders in your municipality: who designs, who funds, who maintains, who controls?</li>\n  <li>In half a page, explain to an elected official why a classified green space must be protected.</li>\n</ol>"
 },
 "v2": {
  "titre": "Plants in the urban environment",
  "resume": "Name and recognise plants, know layers and growth habits, choose a plant palette suited to the Tlemcen climate.",
  "quiz": [
   {
    "question": "How is the scientific name of the Aleppo pine written correctly?",
    "choix": [
     "<i>Pinus Halepensis</i>",
     "<i>Pinus halepensis</i>",
     "<i>pinus Halepensis</i>",
     "PINUS HALEPENSIS"
    ],
    "explication": "Genus capitalised, species in lower case, all in italics."
   },
   {
    "question": "A tree that keeps its leaves in winter has … foliage.",
    "choix": [
     "compound",
     "deciduous",
     "columnar",
     "evergreen"
    ],
    "explication": "Evergreen: it keeps its leaves all year round."
   },
   {
    "question": "Why avoid more than 10% of a single species in a tree population?",
    "choix": [
     "To simplify watering",
     "Because nurseries do not have enough",
     "To reduce the risk that a disease or pest destroys a large share of the trees",
     "Because the law forbids it"
    ],
    "explication": "Diversity limits losses when a species-specific pest strikes."
   },
   {
    "question": "Which species is invasive and must not be planted?",
    "choix": [
     "<i>Quercus ilex</i>",
     "<i>Celtis australis</i>",
     "<i>Myrtus communis</i>",
     "<i>Ailanthus altissima</i>"
    ],
    "explication": "Tree of heaven suckers everywhere and smothers native vegetation."
   },
   {
    "question": "The ash tree produces as fruit…",
    "choix": [
     "pods",
     "drupes",
     "winged samaras",
     "cones"
    ],
    "explication": "Ash fruits are samaras with a wing."
   }
  ]
 },
 "v2-l1": {
  "titre": "Naming plants: applied botany basics",
  "objectifs": [
   "Write a scientific name correctly",
   "Distinguish vegetation layers",
   "Describe a plant: foliage, habit, mature size"
  ],
  "contenu": "\n<p>The same tree may have several common names depending on the region (in French, Arabic, Tamazight). To avoid errors in an inventory or a nursery order, we use the <b>scientific name</b>, in Latin, valid worldwide.</p>\n<h4>The scientific name</h4>\n<ul>\n  <li>It has two words: the <b>genus</b> (capital letter) and the <b>species</b> (lower case), written in <i>italics</i>: <i>Pinus halepensis</i> (Aleppo pine), <i>Olea europaea</i> (olive).</li>\n  <li>A <b>cultivar</b> can be added in quotes: <i>Nerium oleander</i> 'Album' (white-flowered oleander).</li>\n  <li>The <b>family</b> groups related genera: Pinaceae, Oleaceae, Fabaceae…</li>\n</ul>\n<h4>Layers</h4>\n<ul>\n  <li><b>Tree layer</b>: trees, more than 7 to 8 m when mature.</li>\n  <li><b>Shrub layer</b>: shrubs and subshrubs, 1 to 7 m (hedges, borders).</li>\n  <li><b>Herbaceous layer</b>: lawn, meadow, perennials, annual flowers.</li>\n  <li><b>Ground covers and climbers</b>: creeping plants covering the soil, plants climbing walls and pergolas.</li>\n</ul>\n<p>A pleasant, biodiversity-rich green space combines several layers.</p>\n<h4>Describing a plant</h4>\n<ul>\n  <li><b>Foliage</b>: evergreen (keeps its leaves in winter) or deciduous (loses them).</li>\n  <li><b>Habit</b>: overall shape: upright, spreading, weeping, columnar, rounded.</li>\n  <li><b>Mature size</b>: height and width after 20 to 30 years. This decides the planting distance from façades and utility networks.</li>\n  <li><b>Requirements</b>: sun or shade, water, soil type, resistance to cold and wind.</li>\n</ul>\n<div class=\"astuce\"><b>Common mistake:</b> planting a tree according to its size when bought. A 2 m Aleppo pine in the nursery will exceed 15 m: it must not be planted 2 m from a façade.</div>",
  "exercice": "<ol>\n  <li>Choose 5 trees in your neighbourhood or school. For each, record the common name, the scientific name (use the Pl@ntNet app), the foliage (evergreen or deciduous) and the habit.</li>\n  <li>Write the scientific names correctly (capitalised genus, italics).</li>\n  <li>Sort them by layer and estimate their mature size.</li>\n</ol>"
 },
 "v2-l2": {
  "titre": "Choosing a plant palette suited to Tlemcen",
  "objectifs": [
   "Link plant choice to Tlemcen's Mediterranean climate",
   "Use a palette of water-saving trees, shrubs and ground covers",
   "Avoid invasive and highly allergenic species"
  ],
  "contenu": "\n<p>Tlemcen has a <b>Mediterranean climate</b>: rain concentrated from October to April, hot dry summer, possible frost in winter (the city lies at about 800 m altitude). Good plants must therefore <b>tolerate summer drought AND winter cold</b>.</p>\n<h4>Selection principles</h4>\n<ul>\n  <li><b>The right plant in the right place</b>: mature size compatible with the available space, exposure, soil.</li>\n  <li><b>Prefer native or well-adapted species</b>: they need less water and maintenance and feed local wildlife.</li>\n  <li><b>Diversify</b>: avoid more than 10% of a single species in a tree population, to limit disease or pest risks.</li>\n  <li><b>Think about water</b>: group plants by their needs (hydrozones).</li>\n</ul>\n<h4>Example palette (file <code>palette_vegetale.csv</code>)</h4>\n<div class=\"tab-wrap\"><table class=\"tab\"><thead><tr><th>Layer</th><th>Species</th><th>Strengths</th></tr></thead><tbody>\n<tr><td>Tree</td><td><i>Pinus halepensis</i> (Aleppo pine)</td><td>Native, very drought-tolerant; watch out for the processionary moth.</td></tr>\n<tr><td>Tree</td><td><i>Celtis australis</i> (European hackberry)</td><td>Excellent street tree, dense shade, hardy.</td></tr>\n<tr><td>Tree</td><td><i>Fraxinus angustifolia</i> (narrow-leaved ash)</td><td>Native, fast-growing, likes moist soils (banks).</td></tr>\n<tr><td>Tree</td><td><i>Olea europaea</i> (olive)</td><td>Mediterranean symbol, very water-sparing.</td></tr>\n<tr><td>Tree</td><td><i>Ceratonia siliqua</i> (carob)</td><td>Evergreen, sparing; sensitive to hard frost.</td></tr>\n<tr><td>Tree</td><td><i>Quercus ilex</i> (holm oak)</td><td>Native, long-lived, tolerates cold and drought.</td></tr>\n<tr><td>Shrub</td><td><i>Pistacia lentiscus</i> (mastic tree)</td><td>Native, informal hedges, very sparing.</td></tr>\n<tr><td>Shrub</td><td><i>Nerium oleander</i> (oleander)</td><td>Summer flowering; toxic plant, avoid near playgrounds.</td></tr>\n<tr><td>Shrub</td><td><i>Myrtus communis</i> (myrtle)</td><td>Native, fragrant, tolerates pruning.</td></tr>\n<tr><td>Ground cover</td><td><i>Rosmarinus officinalis</i> (prostrate rosemary)</td><td>Attracts bees, no watering once established.</td></tr>\n</tbody></table></div>\n<h4>Species to avoid or watch</h4>\n<ul>\n  <li><b>Invasive</b>: tree of heaven (<i>Ailanthus altissima</i>) suckers everywhere and smothers native vegetation. Do not plant it; remove it gradually.</li>\n  <li><b>Highly allergenic</b>: cypress, plane, birch: do not plant them in large numbers near schools and hospitals.</li>\n  <li><b>Water-hungry</b>: large fine-turf lawns in full sun, to be kept for areas actually used.</li>\n</ul>",
  "exercice": "<ol>\n  <li>Open <code>palette_vegetale.csv</code> (in a spreadsheet or QGIS) and sort the species by water needs.</li>\n  <li>Propose a palette for a 2,000 m² neighbourhood square: 3 trees, 4 shrubs, 2 ground covers, justifying each choice.</li>\n  <li>Check that no species exceeds 10% of the trees proposed for all the squares in the area.</li>\n</ol>"
 },
 "v2-l3": {
  "titre": "Recognising plants in the field",
  "objectifs": [
   "Use simple identification criteria",
   "Use an identification app and check its result",
   "Build a small herbarium or identification sheet"
  ],
  "contenu": "\n<p>In the field, a plant is identified by observing several <b>criteria</b>, from the most general to the most precise:</p>\n<ol>\n  <li><b>Habit and bark</b>: silhouette, smooth, furrowed bark, or bark peeling in plates (plane).</li>\n  <li><b>Leaves</b>: simple or compound (several leaflets), alternate or opposite on the twig, margin shape (entire, toothed, lobed), needles (conifers) in bundles of 2, 3 or 5.</li>\n  <li><b>Flowers and fruits</b>: cones (pines), pods (carob, pagoda tree), drupes (olive, hackberry), winged samaras (ash).</li>\n</ol>\n<h4>Identification apps</h4>\n<p><b>Pl@ntNet</b> (free) recognises a plant from a photo of a leaf, flower or fruit. It suggests several names with a confidence percentage. <b>Always check</b> with a second criterion (fruit, bark) or a guide: apps are often wrong about ornamental plants and young plants.</p>\n<h4>The identification sheet</h4>\n<p>For each species found, prepare a sheet: scientific name, family, common name in French and Arabic, photos of habit, leaf, bark and fruit, mature size, uses in green spaces. Together, these sheets form a <b>digital herbarium</b>, very useful for inventories.</p>\n<div class=\"astuce\"><b>Field tip:</b> always photograph a leaf placed on your notebook next to a ruler: real size helps identification a lot.</div>",
  "exercice": "<ol>\n  <li>30-minute outing in the school grounds or a nearby garden: identify 8 species with Pl@ntNet.</li>\n  <li>For each one, check the result with a second criterion (fruit, bark, leaf arrangement).</li>\n  <li>Produce 3 complete identification sheets and share them with the class.</li>\n</ol>"
 },
 "v3": {
  "titre": "Tree inventory and assessment",
  "resume": "Organise an inventory, measure trees (girth, height, crown) and assess their health and risk.",
  "quiz": [
   {
    "question": "At what height is a tree's girth measured?",
    "choix": [
     "At ground level",
     "Below the first branch",
     "At 2 m",
     "At 1.30 m"
    ],
    "explication": "The standard measurement is taken at 1.30 m, breast height."
   },
   {
    "question": "A trunk has a girth of 157 cm. Its diameter is about…",
    "choix": [
     "50 cm",
     "25 cm",
     "157 cm",
     "78 cm"
    ],
    "explication": "157 ÷ 3.14 ≈ 50 cm."
   },
   {
    "question": "Distance 20 m, angle 30° (tan = 0.577), eyes at 1.5 m. Tree height?",
    "choix": [
     "≈ 31.5 m",
     "≈ 20 m",
     "≈ 10 m",
     "≈ 13 m"
    ],
    "explication": "20 × 0.577 + 1.5 ≈ 13 m."
   },
   {
    "question": "Which defect is a frequent failure point?",
    "choix": [
     "Smooth bark",
     "Abundant flowering",
     "A V-shaped fork with included bark",
     "Evergreen leaves"
    ],
    "explication": "Included bark prevents the two stems of the fork from bonding."
   },
   {
    "question": "Why is the same defect more serious above a playground?",
    "choix": [
     "Because the target (children) is very present",
     "Because the tree grows worse there",
     "It is not more serious",
     "Because the law forbids trees near play areas"
    ],
    "explication": "Risk combines the probability of failure and the presence of targets."
   }
  ]
 },
 "v3-l1": {
  "titre": "Organising a tree inventory",
  "objectifs": [
   "Understand what a tree inventory is for",
   "Fill in a complete tree record",
   "Prepare GPS survey and coding"
  ],
  "contenu": "\n<p>The <b>tree inventory</b> is the located list of all trees managed by a municipality, with their characteristics. It is the basic tool to plan maintenance, estimate budgets, monitor the tree population and justify decisions (felling, replanting).</p>\n<h4>The tree record</h4>\n<div class=\"tab-wrap\"><table class=\"tab\"><thead><tr><th>Field</th><th>Example</th><th>Note</th></tr></thead><tbody>\n<tr><td>Identifier</td><td>ARB-0042</td><td>Unique, never reused</td></tr>\n<tr><td>Species</td><td><i>Celtis australis</i></td><td>Scientific + common name</td></tr>\n<tr><td>Coordinates</td><td>X = 653,812; Y = 3,860,455</td><td>UTM 30N (EPSG 32630), GPS or map</td></tr>\n<tr><td>Girth at 1.30 m</td><td>142 cm</td><td>Tape measure</td></tr>\n<tr><td>Height</td><td>11 m</td><td>Clinometer or hypsometer</td></tr>\n<tr><td>Crown diameter</td><td>8 m</td><td>Mean of two perpendicular measurements</td></tr>\n<tr><td>Stage</td><td>Adult</td><td>Young, adult, mature, senescent</td></tr>\n<tr><td>Health</td><td>Fair</td><td>Good, fair, poor, dead</td></tr>\n<tr><td>Defects</td><td>Dead branch</td><td>Coded list (lesson 3)</td></tr>\n<tr><td>Proposed action</td><td>Safety pruning</td><td>With a deadline</td></tr>\n</tbody></table></div>\n<h4>Preparing the survey</h4>\n<ul>\n  <li><b>Divide</b> the city into sectors (districts, streets) and give each sector a code.</li>\n  <li><b>Code</b> values in advance (pick lists) to avoid typing errors: “Fair”, “fair”, “FR” must become a single value.</li>\n  <li><b>Tools</b>: paper sheet or digital form (QField, ODK Collect, KoboToolbox), GPS or smartphone, tape measure, clinometer, camera.</li>\n  <li><b>Photograph</b> each tree and name the photo with its identifier.</li>\n</ul>\n<div class=\"astuce\"><b>Good habit:</b> test the record on 10 trees before launching the survey. You always discover a missing field or an incomplete pick list.</div>\n<p><i>Note: in the practical data files, field values remain in French (e.g. état = Bon, Moyen, Mauvais, Mort).</i></p>",
  "exercice": "<ol>\n  <li>Open <code>inventaire_arbres.csv</code> in a spreadsheet. Identify the fields and compare them with the record in the lesson.</li>\n  <li>How many trees are in the inventory? How many different species? What is the most frequent species, and does it exceed 10%?</li>\n  <li>Inventory 10 trees at your school with <code>fiche_inventaire_arbre.csv</code> (empty template).</li>\n</ol>"
 },
 "v3-l2": {
  "titre": "Measuring a tree: girth, height, crown",
  "objectifs": [
   "Measure girth at 1.30 m and derive the diameter",
   "Compute a tree's height from an angle and a distance",
   "Estimate crown area"
  ],
  "contenu": "\n<h4>Girth and diameter</h4>\n<p>Measure the trunk <b>girth</b> (C) with a tape at <b>1.30 m</b> above ground (breast height), on the uphill side on a slope. The diameter is:</p>\n<p class=\"formule\">D = C ÷ π &nbsp;&nbsp; (example: 142 cm ÷ 3.1416 ≈ 45 cm)</p>\n<p>The <b>basal area</b> (trunk cross-section) is g = π × D² ÷ 4. For D = 0.45 m: g ≈ 0.16 m².</p>\n<h4>Height with a clinometer</h4>\n<p>Stand at a known distance <b>d</b> from the trunk (e.g. 15 m, taped), aim at the top and read the angle <b>α</b>. Then:</p>\n<p class=\"formule\">h = d × tan(α) + eye height</p>\n<p>Example: d = 15 m, α = 32°, eyes at 1.60 m: h = 15 × 0.625 + 1.60 ≈ <b>11 m</b>. A smartphone with a clinometer app is enough for practical work.</p>\n<h4>Stick method (no instrument)</h4>\n<p>Hold a stick vertically at arm's length, as long as the eye-to-hand distance. Step back until the bottom and top of the stick line up with the foot and the top of the tree: your distance to the trunk is roughly equal to the tree's height.</p>\n<h4>Crown</h4>\n<p>Measure the crown diameter on the ground in two perpendicular directions (north-south and east-west) and average them. Crown area ≈ π × (mean diameter ÷ 2)². For 8 m: ≈ 50 m² of shade on the ground.</p>\n<div class=\"astuce\"><b>In QGIS:</b> once the inventory is imported, the field calculator gives the diameter with the expression <code>\"circonference_cm\" / pi()</code>.</div>",
  "exercice": "<ol>\n  <li>Measure 3 trees: girth at 1.30 m, height (clinometer and stick method), crown diameter.</li>\n  <li>Compute the diameter, basal area and crown area of each.</li>\n  <li>Compare the two height methods: what difference do you find?</li>\n  <li>In the spreadsheet, add a computed <code>diametre_cm</code> column to <code>inventaire_arbres.csv</code>.</li>\n</ol>"
 },
 "v3-l3": {
  "titre": "Health assessment and risk evaluation",
  "objectifs": [
   "Recognise the main tree defects",
   "Apply the logic of Visual Tree Assessment (VTA)",
   "Classify a tree and propose an action with a deadline"
  ],
  "contenu": "\n<p>An unhealthy tree may drop a branch or fall. In the city, <b>user safety</b> is the priority. Assessment is first visual, following the <b>Visual Tree Assessment</b> (VTA) method, then, if needed, with instruments (resistograph, tomograph) by a specialist.</p>\n<h4>What to look at, from the base to the top</h4>\n<ul>\n  <li><b>Root collar and roots</b>: fungi at the base, roots cut by works, lifted soil (sign of tilting).</li>\n  <li><b>Trunk</b>: cavities, cracks, loose bark, seepage, impact wounds (cars, strimmers), recent leaning.</li>\n  <li><b>Main limbs</b>: V-shaped forks with included bark (frequent failure point), stubs from bad pruning.</li>\n  <li><b>Crown</b>: dead branches, sparse or yellowing foliage, pest attacks.</li>\n</ul>\n<h4>Classify and decide</h4>\n<div class=\"tab-wrap\"><table class=\"tab\"><thead><tr><th>Condition</th><th>Signs</th><th>Typical action</th></tr></thead><tbody>\n<tr><td>Good</td><td>No significant defect</td><td>Normal monitoring (every 3 to 5 years)</td></tr>\n<tr><td>Fair</td><td>Limited defects: deadwood, small wound</td><td>Maintenance pruning, new visit in 1 to 2 years</td></tr>\n<tr><td>Poor</td><td>Serious defect: large cavity, crack, fungus at the base</td><td>Detailed assessment, quick make-safe</td></tr>\n<tr><td>Dead / dangerous</td><td>Dead tree or imminent failure</td><td>Safety perimeter, urgent felling, replanting</td></tr>\n</tbody></table></div>\n<p><b>Risk</b> also depends on the <b>target</b>: a weak tree above a playground is far more urgent than the same tree in a little-visited wood.</p>\n<div class=\"astuce\"><b>Golden rule:</b> never fell a tree without a written, photographed assessment. And every felled tree should be replaced (if possible by two).</div>",
  "exercice": "<ol>\n  <li>In <code>inventaire_arbres.csv</code>, filter trees whose <code>etat</code> is “Mauvais” (poor) or “Mort” (dead). How many are there? In which spaces?</li>\n  <li>Cross with the <code>cible</code> field (use intensity): list the 5 highest-priority trees.</li>\n  <li>For each, propose an action and a deadline (immediate, 3 months, 1 year).</li>\n</ol>"
 },
 "v4": {
  "titre": "Designing a green space",
  "resume": "Analyse a site, write a brief, compose a master plan and choose accessible, safe facilities.",
  "quiz": [
   {
    "question": "What do “desire lines” worn into the grass show?",
    "choix": [
     "Areas to fence",
     "Pedestrians' real routes, where to put paths",
     "Buried networks",
     "Frost pockets"
    ],
    "explication": "They reveal the routes users actually take."
   },
   {
    "question": "Where should trees be placed to shade a bench in the afternoon?",
    "choix": [
     "South and west of the bench",
     "It does not matter",
     "North of the bench",
     "East only"
    ],
    "explication": "Afternoon sun comes from the south-west."
   },
   {
    "question": "What minimum width is commonly used for an accessible path?",
    "choix": [
     "1.40 m",
     "3.00 m",
     "1.00 m",
     "0.80 m"
    ],
    "explication": "1.40 m lets a wheelchair and a pedestrian pass."
   },
   {
    "question": "What is standard EN 1177 about?",
    "choix": [
     "Tree pruning",
     "Street lighting",
     "Irrigation",
     "Impact-absorbing surfaces of playgrounds"
    ],
    "explication": "EN 1177 covers impact-absorbing surfaces; EN 1176 covers equipment."
   },
   {
    "question": "How is a tree shown on a master plan?",
    "choix": [
     "By its name only",
     "It is not shown",
     "As a 1 mm dot",
     "As a circle the size of its mature crown"
    ],
    "explication": "Mature size lets you check distances and future shade."
   }
  ]
 },
 "v4-l1": {
  "titre": "Analysing the site and writing the brief",
  "objectifs": [
   "Carry out a site analysis before drawing",
   "Identify users and their needs",
   "Write a design brief"
  ],
  "contenu": "\n<p>A good project starts <b>on site</b>, not on paper. Site analysis lists everything that will constrain or enrich the project.</p>\n<h4>Site analysis grid</h4>\n<ul>\n  <li><b>Location</b>: district, access, roads, bus stops, nearby schools and facilities.</li>\n  <li><b>Topography</b>: slopes, high and low points (where does rainwater go?).</li>\n  <li><b>Local climate</b>: sunlight (where is the shade at 3 pm in July?), prevailing winds, frost areas in winter.</li>\n  <li><b>Soil</b>: topsoil, fill, rock, compaction.</li>\n  <li><b>Existing features</b>: trees to keep, walls, networks (water, electricity, gas, sewerage), overhead and buried.</li>\n  <li><b>Current uses</b>: paths worn by pedestrians, improvised football pitches, fly-tipping.</li>\n  <li><b>Landscape</b>: views to keep (mountain, minaret, medina), views to screen.</li>\n</ul>\n<h4>Users</h4>\n<p>Who will come? Children, teenagers, families, elderly people, wheelchair users, sportspeople, workers on a break. A <b>quick survey</b> (10-question questionnaire, observation at different times) avoids building a park that suits nobody.</p>\n<h4>The brief</h4>\n<p>The brief is the written list of what the project must contain, with areas: e.g. “2-6 years playground (150 m²), 6-12 years playground (250 m²), open lawn (800 m²), accessible main path, 20 benches of which 10 in the shade, drinking fountain, toilets, 30 shade trees”. It also sets the <b>budget</b> and the acceptable level of maintenance.</p>\n<div class=\"astuce\"><b>Tip:</b> paths worn into the grass by pedestrians (“desire lines”) show where paths should go.</div>",
  "exercice": "<ol>\n  <li>In QGIS, open the <code>site_projet.geojson</code> layer (fictional 1.2 ha plot) with an OpenStreetMap basemap.</li>\n  <li>Produce an analysis map: access, nearby schools, orientation, prevailing winds (north-west in winter), networks (<code>reseaux.geojson</code> layer).</li>\n  <li>Write a one-page brief with the area of each element.</li>\n</ol>"
 },
 "v4-l2": {
  "titre": "Composing the plan: sketch and master plan",
  "objectifs": [
   "Move from the brief to a zoning sketch",
   "Draw a readable master plan at the right scale",
   "Apply accessibility and comfort rules"
  ],
  "contenu": "\n<h4>1. Zoning (sketch)</h4>\n<p>First draw “bubbles”: quiet area, play area, sports area, main entrance, shaded area. Put noisy areas away from homes and children's play near parents' benches. Test several options.</p>\n<h4>2. Circulation</h4>\n<ul>\n  <li>A <b>main path</b> linking the entrances and following desire lines.</li>\n  <li><b>Secondary paths</b> to each area, a walking loop if space allows.</li>\n  <li><b>Accessibility</b>: commonly used benchmarks: width of at least 1.40 m, gradient preferably 5% or less, firm surface, benches with armrests about every 50 m.</li>\n</ul>\n<h4>3. Plants as structure</h4>\n<p>Trees form the framework: rows to guide, groves for shade, single trees to mark a place. Put shade trees <b>south and west</b> of benches and play areas (afternoon shade). A windbreak hedge to the north-west protects from the winter wind.</p>\n<h4>4. The master plan</h4>\n<p>The master plan shows the project from above, to scale (often 1:200 or 1:500), with: north arrow, scale bar, legend, trees (circles of mature crown size), paths, facilities, main dimensions and a title block (title, author, date). It can be drawn by hand, with CAD software or in QGIS (print layout).</p>\n<div class=\"astuce\"><b>Check:</b> draw crowns at their mature size. If they overlap a lot or touch façades, move them or change species.</div>",
  "exercice": "<ol>\n  <li>From your brief (lesson 1), draw two zoning options for the project site.</li>\n  <li>Choose one and draw the master plan at 1:500 (paper or QGIS) with north arrow, scale, legend and title block.</li>\n  <li>Check the width and gradient of the main paths with the contours in <code>courbes_site.geojson</code> (field <code>altitude</code>).</li>\n</ol>"
 },
 "v4-l3": {
  "titre": "Facilities, furniture and safety",
  "objectifs": [
   "Choose the furniture of a green space",
   "Know the safety principles of playgrounds",
   "Plan lighting, water and cleanliness"
  ],
  "contenu": "\n<h4>Furniture</h4>\n<ul>\n  <li><b>Benches</b>: in the shade, facing a view or an activity, with a backrest; provide benches for elderly people near entrances.</li>\n  <li><b>Litter bins</b>: near entrances, benches and play areas; a clean space stays respected.</li>\n  <li><b>Drinking fountains</b>, toilets in large parks.</li>\n  <li><b>Signage</b>: entrance map, rules, names of notable trees (education).</li>\n  <li><b>Fence and gates</b> if the park closes at night.</li>\n</ul>\n<h4>Playgrounds</h4>\n<p>The European references often used are standards <b>EN 1176</b> (play equipment) and <b>EN 1177</b> (impact-absorbing surfaces). Key principles:</p>\n<ul>\n  <li>Separate play for small children (2-6 years) and older children (6-12 years).</li>\n  <li>Under each item, an <b>impact-absorbing surface</b> (wood chips, sand, suitable artificial turf, tiles) over a safety zone around the equipment.</li>\n  <li>No toxic or thorny plants nearby (oleander, for example).</li>\n  <li>Shade is essential: metal slides in full sun burn in summer.</li>\n  <li>Regular inspection: frequent visual checks, annual in-depth inspection.</li>\n</ul>\n<h4>Lighting and safety</h4>\n<p>Light the main paths without lighting the whole park (nocturnal wildlife needs darkness); keep clear sightlines so users feel safe (no dense 1.5 m shrub masses along paths).</p>",
  "exercice": "<ol>\n  <li>Place the furniture on your master plan: benches (half in the shade), bins, drinking fountain, signage.</li>\n  <li>Draw the playground with its safety zones and type of impact-absorbing surface.</li>\n  <li>List the quantities of furniture: they will be used for the cost estimate in level 8.</li>\n</ol>"
 },
 "v5": {
  "titre": "Soil, planting and irrigation",
  "resume": "Prepare the soil, plant a tree properly, compute water needs and design water-saving irrigation.",
  "quiz": [
   {
    "question": "When are bare-root trees planted?",
    "choix": [
     "Only in April",
     "During dormancy, from November to March, avoiding frost",
     "In midsummer",
     "Any time"
    ],
    "explication": "Bare roots only tolerate planting during dormancy."
   },
   {
    "question": "Where should the root collar be after planting?",
    "choix": [
     "Buried 20 cm deep",
     "50 cm above the soil",
     "In the gravel layer",
     "At finished ground level"
    ],
    "explication": "A buried collar leads to bark rot."
   },
   {
    "question": "ET0 = 5 mm/day, KL = 0.3, area 100 m², drip (0.9). Daily need?",
    "choix": [
     "≈ 1,500 L",
     "≈ 150 L",
     "≈ 167 L",
     "≈ 15 L"
    ],
    "explication": "5 × 0.3 × 100 ÷ 0.9 ≈ 167 litres per day."
   },
   {
    "question": "Why are plants grouped into hydrozones?",
    "choix": [
     "To water each group according to its real needs",
     "To make nice colours",
     "To avoid pruning",
     "To reduce the number of trees"
    ],
    "explication": "Each irrigation sector receives the dose suited to its plants."
   },
   {
    "question": "What soil volume is often targeted for a large street tree?",
    "choix": [
     "10 m³ or more",
     "1 m³",
     "No soil, gravel is enough",
     "0.5 m³"
    ],
    "explication": "A large soil volume lets the tree develop its roots and live long."
   }
  ]
 },
 "v5-l1": {
  "titre": "Soil and the planting pit",
  "objectifs": [
   "Describe the qualities of good topsoil",
   "Size a planting pit in the city",
   "Prevent soil compaction"
  ],
  "contenu": "\n<p>Roots live in the soil: a tree in poor soil will remain stunted all its life, whatever the care. In the city, soil is often <b>fill</b>, rubble, compacted by machines and cars.</p>\n<h4>Good topsoil</h4>\n<ul>\n  <li>Balanced <b>texture</b> (sand, silt, clay): neither too sticky nor too free-draining. Simple test: a handful of moist soil forms a ball that breaks under light pressure.</li>\n  <li><b>Organic matter</b>: 2 to 5%; improve it with mature compost.</li>\n  <li>Airy <b>structure</b>: air and water must circulate. Compacted soil suffocates roots.</li>\n  <li><b>pH</b>: soils around Tlemcen are often calcareous (pH 7.5 to 8.5); choose species that tolerate it.</li>\n</ul>\n<h4>The planting pit</h4>\n<ul>\n  <li>Volume: <b>as large as possible</b>. For a large street tree, 10 m³ of soil or more is often targeted; a small 1 m³ pit condemns the tree to stay small and die young.</li>\n  <li>When the pavement is narrow, pits are linked (<b>continuous trench</b>) or load-bearing <b>structural soils</b> (soil-stone mixes) let roots grow under pavements.</li>\n  <li>Loosen the bottom and sides; do not put a gravel layer at the bottom.</li>\n</ul>\n<h4>Protecting the soil</h4>\n<p>During works, fence the area under the crown of existing trees (no machines, no storage). In green spaces, prevent cars from parking on lawns and at tree bases. <b>Mulch</b> (wood chips, shredded material) protects the soil from the sun, keeps moisture and feeds soil life.</p>",
  "exercice": "<ol>\n  <li>Take some soil from two places (lawn, street tree base): do the ball test and observe the colour, stones, roots.</li>\n  <li>A fictional 300 m street must receive hackberries every 8 m on one side. How many trees? What total soil volume at 10 m³ per tree?</li>\n  <li>Propose a solution if the pavement is only 2 m wide.</li>\n</ol>"
 },
 "v5-l2": {
  "titre": "Planting a tree properly",
  "objectifs": [
   "Choose the season and the plant",
   "Plant step by step",
   "Ensure watering and follow-up in the first years"
  ],
  "contenu": "\n<h4>The season</h4>\n<p>Plant during <b>dormancy</b>, from November to March, avoiding frost or waterlogged soil. <b>Bare-root</b> plants must be planted in this period; <b>container</b> or <b>root-balled</b> plants tolerate a slightly longer period, but never in midsummer in Tlemcen.</p>\n<h4>Choosing the plant</h4>\n<p>Straight trunk, intact leader (top shoot), roots not circling in the pot, no wounds. A young plant (girth 10-14 cm) often establishes better than a large specimen.</p>\n<h4>Steps</h4>\n<ol>\n  <li>Dig the pit and loosen the bottom.</li>\n  <li>Set the <b>stake(s)</b> before the tree (on the prevailing-wind side), without damaging roots.</li>\n  <li>Untangle circling roots, cut damaged roots.</li>\n  <li>Position the tree: the <b>root collar</b> (trunk-root junction) at finished ground level, never buried.</li>\n  <li>Backfill with topsoil (improved with compost), firm lightly at the base.</li>\n  <li>Form a <b>watering basin</b> and water generously (at least 50 litres) even if it rains.</li>\n  <li>Tie the tree to the stake with a soft tie that does not hurt the bark; mulch the basin.</li>\n</ol>\n<h4>Follow-up</h4>\n<p>During the <b>first 2 to 3 summers</b>, water regularly (e.g. 50 litres once a week, adjusted to weather and soil). Loosen ties every year, remove stakes after 2 to 3 years. Replace dead trees the following winter.</p>\n<div class=\"astuce\"><b>Common mistake:</b> burying the root collar. The trunk bark rots and the tree slowly declines. The collar must stay visible.</div>",
  "exercice": "<ol>\n  <li>Write an illustrated work sheet (diagram of pit, stake, basin) for planting an ash tree.</li>\n  <li>If possible, take part in planting a tree at school and photograph each step.</li>\n  <li>Plan the watering schedule for the first 3 summers and the total amount of water.</li>\n</ol>"
 },
 "v5-l3": {
  "titre": "Computing water needs and designing irrigation",
  "objectifs": [
   "Understand reference evapotranspiration (ET0)",
   "Compute the water need of a planted area",
   "Choose a water-saving irrigation system"
  ],
  "contenu": "\n<p>Water is scarce in Tlemcen in summer: a green space must be designed to <b>use little</b>. Needs are computed from <b>reference evapotranspiration</b> (ET0): the amount of water, in mm per day, lost by a well-watered reference lawn. 1 mm on 1 m² = 1 litre.</p>\n<h4>The calculation</h4>\n<p class=\"formule\">Need (L/day) = ET0 (mm/day) × KL × Area (m²) ÷ Efficiency</p>\n<ul>\n  <li><b>KL</b>, landscape coefficient: about 0.2 to 0.3 for sparing plants (olive, rosemary, mastic); 0.4 to 0.6 for average beds; 0.7 to 0.8 for lawn.</li>\n  <li>System <b>efficiency</b>: drip ≈ 0.9; sprinkler ≈ 0.7 (some water evaporates or blows away).</li>\n  <li>Useful rainfall is subtracted when it rains (rarely in summer).</li>\n</ul>\n<h4>Example (July, ET0 = 6 mm/day, values from <code>et0_tlemcen.csv</code>)</h4>\n<div class=\"tab-wrap\"><table class=\"tab\"><thead><tr><th>Zone</th><th>Area</th><th>KL</th><th>System</th><th>Need</th></tr></thead><tbody>\n<tr><td>Lawn</td><td>800 m²</td><td>0.8</td><td>Sprinkler (0.7)</td><td>6 × 0.8 × 800 ÷ 0.7 ≈ 5,490 L/day</td></tr>\n<tr><td>Mediterranean beds</td><td>800 m²</td><td>0.3</td><td>Drip (0.9)</td><td>6 × 0.3 × 800 ÷ 0.9 = 1,600 L/day</td></tr>\n</tbody></table></div>\n<p>For the same area, sparing beds on drip use <b>3.4 times less</b> water than sprinkled lawn.</p>\n<h4>Good practice</h4>\n<ul>\n  <li><b>Hydrozones</b>: group plants by needs and water them in separate sectors.</li>\n  <li>Water <b>early in the morning or at night</b>, less often but longer (deep roots).</li>\n  <li><b>Mulch</b>: greatly reduces evaporation.</li>\n  <li>Use <b>non-conventional water</b> where permitted: stored rainwater, treated wastewater according to regulations.</li>\n  <li><b>Xeriscaping</b> (dry garden): adapted plants, little lawn, mineral or organic mulch.</li>\n</ul>",
  "exercice": "<ol>\n  <li>Open <code>et0_tlemcen.csv</code> and compute the monthly water need (m³) of the 2,000 m² square from your palette (level 2): state the area of each zone.</li>\n  <li>Compare two options: 50% lawn or 10% lawn. What annual water saving?</li>\n  <li>The workbook <code>calcul_irrigation.xlsx</code> contains the calculation model: check your results.</li>\n</ol>"
 },
 "v6": {
  "titre": "Maintenance and sustainable management",
  "resume": "Plan maintenance over the year, apply differentiated management, prune correctly and protect plants without pesticides.",
  "quiz": [
   {
    "question": "Which differentiated-management class covers banks and meadows mown once or twice a year?",
    "choix": [
     "Class 1, horticultural",
     "Class 3, rustic",
     "Class 4, natural",
     "Class 2, gardened"
    ],
    "explication": "The natural class keeps interventions to a minimum."
   },
   {
    "question": "Where should a branch be cut?",
    "choix": [
     "Just outside the collar, without a stub",
     "30 cm from the trunk",
     "Flush with the trunk, removing the collar",
     "In the middle of the branch"
    ],
    "explication": "The collar contains the tissues that close the wound."
   },
   {
    "question": "Why is topping a bad practice?",
    "choix": [
     "It is compulsory every year",
     "It gives too much shade",
     "It costs too little",
     "It produces weak shoots and large wounds that rot"
    ],
    "explication": "A topped tree becomes weak and dangerous."
   },
   {
    "question": "When are trunk collar traps used against the processionary moth?",
    "choix": [
     "In autumn",
     "In late winter, when caterpillars come down",
     "In summer",
     "Never"
    ],
    "explication": "The collars catch the caterpillars coming down the trunk."
   },
   {
    "question": "In integrated pest management, a treatment product is used…",
    "choix": [
     "first, as prevention",
     "every month",
     "only on lawns",
     "as a last resort"
    ],
    "explication": "Prevention, mechanical and biological control come first."
   }
  ]
 },
 "v6-l1": {
  "titre": "Maintenance calendar and differentiated management",
  "objectifs": [
   "Draw up the annual maintenance calendar",
   "Apply differentiated management by maintenance classes",
   "Make use of green waste"
  ],
  "contenu": "\n<h4>Annual calendar (Tlemcen climate)</h4>\n<div class=\"tab-wrap\"><table class=\"tab\"><thead><tr><th>Period</th><th>Main tasks</th></tr></thead><tbody>\n<tr><td>November to March</td><td>Planting, pruning deciduous trees, removing processionary nests, furniture maintenance, mulching.</td></tr>\n<tr><td>March to May</td><td>Mowing, hand weeding, starting and checking irrigation, spring flowers. No heavy pruning while birds nest.</td></tr>\n<tr><td>June to September</td><td>Irrigation (the main task), watching young trees, litter collection, fire prevention (clearing undergrowth in wooded areas).</td></tr>\n<tr><td>October</td><td>Summer review, preparing plantings, sowing meadows, collecting leaves for compost.</td></tr>\n</tbody></table></div>\n<h4>Differentiated management</h4>\n<p>Not all spaces need the same maintenance. <b>Differentiated management</b> gives each space a <b>maintenance class</b>:</p>\n<ul>\n  <li><b>Class 1, horticultural</b>: prestige squares and entrances, flower beds, short-mown lawn. Intensive maintenance.</li>\n  <li><b>Class 2, gardened</b>: squares and neighbourhood gardens, regular maintenance.</li>\n  <li><b>Class 3, rustic</b>: large lawns mown less often, free-growing shrubs.</li>\n  <li><b>Class 4, natural</b>: banks, hillsides, meadows mown once or twice a year, deadwood left for wildlife (if safe).</li>\n</ul>\n<p>Benefits: less water, fewer working hours, more biodiversity, and resources concentrated where they are visible and useful. It must be <b>explained to residents</b> (signs): an unmown meadow is not an abandoned space.</p>\n<h4>Green waste</h4>\n<p>Grass clippings, leaves and shredded branches become <b>compost</b> or <b>mulch</b>: the cycle is closed and purchases of fertiliser and mulch are reduced.</p>",
  "exercice": "<ol>\n  <li>In QGIS, open <code>espaces_verts.geojson</code> and add a <code>classe_entretien</code> field (1 to 4).</li>\n  <li>Give each space a class, with a justification (use, function, ecological interest).</li>\n  <li>Map differentiated management with one colour per class and compute the area of each class.</li>\n</ol>"
 },
 "v6-l2": {
  "titre": "Tree pruning",
  "objectifs": [
   "Distinguish types of pruning and their aims",
   "Make a correct cut just outside the branch collar",
   "Reject topping and know safety rules"
  ],
  "contenu": "\n<p>A well-planted tree in the right place <b>needs little pruning</b>. Pruning meets a precise aim; it is never routine.</p>\n<h4>Types of pruning</h4>\n<ul>\n  <li><b>Formative pruning</b> (young trees): keep a single leader, remove V-shaped forks, gradually raise low branches above paths.</li>\n  <li><b>Maintenance pruning</b>: remove deadwood and broken, diseased or crossing branches.</li>\n  <li><b>Safety pruning</b>: remove a dangerous branch above a path or playground.</li>\n  <li><b>Architectural pruning</b> (pleaching, pollarding, espaliers): only on trees trained this way from a young age, and repeated regularly.</li>\n</ul>\n<h4>The correct cut</h4>\n<p>Cut just outside the <b>branch collar</b> (the swelling at its base), without damaging it and without leaving a <b>stub</b>. The collar contains the tissues that close the wound. For a large branch, use three cuts (undercut, top cut further out, then final cut) to avoid tearing the bark.</p>\n<h4>What not to do</h4>\n<ul>\n  <li><b>Topping</b> (cutting all large branches): the tree reacts with weak shoots, rots through the large wounds and becomes dangerous. It is still a common bad practice.</li>\n  <li>Removing more than about a quarter of the foliage at once.</li>\n  <li>Using climbing spikes on a tree that is not going to be felled.</li>\n</ul>\n<h4>Safety</h4>\n<p>Work at height is for trained, equipped staff only: helmet, goggles, gloves, chainsaw-protective trousers, harness and ropes or aerial platform. The site is marked out and traffic protected.</p>",
  "exercice": "<ol>\n  <li>On photos of trees in your city, find examples of topping, stubs and correct cuts.</li>\n  <li>Draw the three cuts needed to remove a large branch, showing the collar.</li>\n  <li>In <code>inventaire_arbres.csv</code>, list the trees for which pruning is proposed and specify the type of pruning.</li>\n</ol>"
 },
 "v6-l3": {
  "titre": "Protecting plants without pesticides: integrated pest management",
  "objectifs": [
   "Recognise the pine processionary moth and its dangers",
   "Combine integrated pest management methods",
   "Organise health monitoring of the tree population"
  ],
  "contenu": "\n<p><b>Integrated pest management</b> combines several methods and uses a product only as a last resort. In public places, chemical pesticides, which are dangerous for users, staff and beneficial wildlife, are avoided as far as possible.</p>\n<h4>Example: the pine processionary moth</h4>\n<p>The caterpillar of <i>Thaumetopoea pityocampa</i> lives in colonies in <b>white silky nests</b> at the tips of pine and cedar branches. It eats the needles and its <b>stinging hairs</b> cause serious reactions in humans and animals (eyes, skin, airways). At the end of winter, caterpillars come down in single file to bury themselves.</p>\n<ul>\n  <li><b>Winter</b>: nest removal, i.e. cutting and destroying nests, by equipped staff (suit, mask, goggles).</li>\n  <li><b>Late winter</b>: <b>collar traps</b> around trunks that catch caterpillars on their way down.</li>\n  <li><b>Summer</b>: <b>pheromone traps</b> catching male moths.</li>\n  <li><b>Autumn</b>: biological treatment with <i>Bacillus thuringiensis</i> on young caterpillars if infestation is heavy.</li>\n  <li><b>All year</b>: nest boxes for tits, which eat many caterpillars; diversify tree species.</li>\n</ul>\n<h4>Other methods</h4>\n<ul>\n  <li><b>Prevention</b>: right species in the right place, living soil, suitable watering: a healthy plant resists better.</li>\n  <li><b>Mechanical control</b>: hand or thermal weeding, pruning affected parts.</li>\n  <li><b>Biological control</b>: beneficial insects (ladybirds against aphids), nest boxes, refuge hedges.</li>\n</ul>\n<h4>Health monitoring</h4>\n<p>Record every observation (date, place, tree, pest, intensity) in the inventory: hot spots are identified, actions evaluated and next year's campaigns planned.</p>",
  "exercice": "<ol>\n  <li>In <code>inventaire_arbres.csv</code>, count the pines reported with processionary nests (field <code>defaut</code> = “Nids processionnaire”).</li>\n  <li>Map them in QGIS: are they near schools and playgrounds?</li>\n  <li>Write the annual integrated pest management plan for these trees, month by month.</li>\n</ol>"
 },
 "v7": {
  "titre": "Mapping green spaces with QGIS",
  "resume": "Digitise and measure green spaces, compute indicators per district, analyse accessibility and use the tree inventory and NDVI.",
  "quiz": [
   {
    "question": "Which QGIS expression computes a polygon's area in the project CRS?",
    "choix": [
     "area_m()",
     "$length",
     "$area",
     "$x"
    ],
    "explication": "$area returns the area in CRS units (m² in UTM)."
   },
   {
    "question": "Why is the practical data in UTM zone 30N?",
    "choix": [
     "To have distances and areas in metres",
     "Because QGIS only accepts UTM",
     "To display colours",
     "To reduce file size"
    ],
    "explication": "A projected metric system allows direct measurement in metres."
   },
   {
    "question": "Which tool creates the 300 m zone around green spaces?",
    "choix": [
     "Raster calculator",
     "Buffer",
     "Union",
     "Georeferencer"
    ],
    "explication": "A buffer draws a zone at a fixed distance around features."
   },
   {
    "question": "With Sentinel-2, NDVI is computed with bands…",
    "choix": [
     "B11 and B12",
     "B1 and B9",
     "B2 and B3",
     "B8 (NIR) and B4 (red)"
    ],
    "explication": "NDVI = (B8 − B4) ÷ (B8 + B4)."
   },
   {
    "question": "An NDVI of 0.7 indicates…",
    "choix": [
     "dense, vigorous vegetation",
     "water",
     "built-up area",
     "bare soil"
    ],
    "explication": "Above 0.5, vegetation is dense and active."
   }
  ]
 },
 "v7-l1": {
  "titre": "Mapping green spaces and computing areas",
  "objectifs": [
   "Open the practical layers in QGIS with the right coordinate system",
   "Digitise a new green space",
   "Compute areas and the m² per inhabitant ratio by district"
  ],
  "contenu": "\n<p>QGIS is a free, open-source GIS (qgis.org, LTR version recommended). The practical layers are in <b>WGS 84 / UTM zone 30N (EPSG 32630)</b>: distances and areas are in metres. Menu names below are those of the English interface.</p>\n<h4>1. Open the data</h4>\n<ol>\n  <li><i>Project &gt; Properties &gt; CRS</i>: choose EPSG:32630.</li>\n  <li>Drag and drop <code>quartiers.geojson</code> and <code>espaces_verts.geojson</code> into QGIS.</li>\n  <li>Add an OpenStreetMap basemap: <i>Browser panel &gt; XYZ Tiles &gt; OpenStreetMap</i>.</li>\n</ol>\n<h4>2. Digitise a green space</h4>\n<p>Select the <code>espaces_verts</code> layer, click <i>Toggle Editing</i> (pencil), then <i>Add Polygon Feature</i>. Click the vertices, right-click to finish, fill in the attributes (name, category), save.</p>\n<h4>3. Compute areas</h4>\n<p>Open the <i>Field Calculator</i> and create a decimal field <code>surface_m2</code> with the expression:</p>\n<!--code:0-->\n<h4>4. Green space per district</h4>\n<p>Tool <i>Processing &gt; Toolbox &gt; Join attributes by location (summary)</i>: target layer <code>quartiers</code>, join layer <code>espaces_verts</code>, predicate “intersects”, field <code>surface_m2</code>, summary “sum”. (To be exact, first cut green spaces by districts with the <i>Intersection</i> tool.) Then, in the new layer, compute the ratio:</p>\n<!--code:1-->\n<p>Display this field with <i>Symbology &gt; Graduated</i>: you get the map of deficient districts (less than 9 m²/inh.).</p>",
  "exercice": "<ol>\n  <li>Carry out the lesson's steps with the practical data.</li>\n  <li>Which districts are below 9 m²/inh.? How much area would have to be created in each?</li>\n  <li>Make a print layout (title, legend, scale, north arrow, source “fictional ENIV data”) and export it as PDF.</li>\n</ol>"
 },
 "v7-l2": {
  "titre": "Analysing access to green spaces",
  "objectifs": [
   "Create a 300 m buffer around green spaces",
   "Estimate the share of the population within 300 m",
   "Propose the location of a new green space"
  ],
  "contenu": "\n<p>Having enough green space is not enough: it must be <b>close</b> to residents. Under the 3-30-300 rule (level 1), everyone should live less than <b>300 m</b> from a green space.</p>\n<h4>1. Buffer</h4>\n<p><i>Vector &gt; Geoprocessing Tools &gt; Buffer</i>: layer <code>espaces_verts</code>, distance <b>300</b> metres, tick <i>Dissolve result</i>. You can first filter out small spaces (e.g. keep only those over 5,000 m²) with the expression:</p>\n<!--code:0-->\n<h4>2. Population served</h4>\n<p>The <code>batiments_habitat.geojson</code> layer contains housing points with a number of residents (field <code>habitants</code>). Use <i>Select by Location</i>: select points that “intersect” the buffer. The sum of selected residents (<i>Statistics</i> panel) divided by the total population gives the <b>share of the population served</b>.</p>\n<h4>3. Gaps and proposal</h4>\n<p>Invert the selection: the remaining points are residents <b>not served</b>. With a <i>Heatmap</i> (symbology) on these points, find the area where a new green space would be most useful. Then check that a vacant plot exists there (<code>terrains_libres.geojson</code> layer).</p>\n<div class=\"astuce\"><b>Going further:</b> straight-line distance overestimates access. With the <i>Service area</i> tool (network analysis) and OpenStreetMap streets, you compute the real walking distance.</div>",
  "exercice": "<ol>\n  <li>Compute the share of the population within 300 m of a green space larger than 5,000 m².</li>\n  <li>Map unserved residents and propose a plot for a new square.</li>\n  <li>Recompute the share served with this new square: what is the gain?</li>\n</ol>"
 },
 "v7-l3": {
  "titre": "Mapping the tree inventory and vegetation (NDVI)",
  "objectifs": [
   "Import the tree inventory from X/Y coordinates",
   "Symbolise trees by health and species",
   "Compute and interpret NDVI from Sentinel-2 imagery"
  ],
  "contenu": "\n<h4>1. Import the inventory</h4>\n<p><i>Layer &gt; Add Layer &gt; Add Delimited Text Layer</i>: file <code>inventaire_arbres.csv</code>, comma separator, geometry “point”, X field = <code>x</code>, Y field = <code>y</code>, CRS = EPSG:32630. Then export the layer to GeoPackage so that you can edit it.</p>\n<h4>2. Symbology and labels</h4>\n<ul>\n  <li><i>Categorized</i> on <code>etat</code>: green (Bon = good), yellow (Moyen = fair), orange (Mauvais = poor), red (Mort = dead).</li>\n  <li>Size proportional to crown diameter: in the symbol size, use an expression such as:</li>\n</ul>\n<!--code:0-->\n<p>(Unit: <b>map units / metres at scale</b>, so the circle has the real size of the crown.)</p>\n<h4>3. NDVI</h4>\n<p><b>NDVI</b> (Normalized Difference Vegetation Index) measures vegetation vigour from satellite images: vegetation strongly reflects near infrared (NIR) and absorbs red (R).</p>\n<p class=\"formule\">NDVI = (NIR − R) ÷ (NIR + R) &nbsp; ; &nbsp; Sentinel-2: NIR = band B8, R = band B4 (10 m)</p>\n<p>Values: close to 0 or negative for buildings, water and bare soil; 0.2 to 0.4 for sparse or dry vegetation; above 0.5 for dense, vigorous vegetation.</p>\n<p>Download bands B4 and B8 of a Sentinel-2 image over Tlemcen free of charge from the <b>Copernicus Browser</b> (free registration), then <i>Raster &gt; Raster Calculator</i>:</p>\n<!--code:1-->\n<p>Compare a May image and an August image: unirrigated lawns and meadows dry out, trees stay green.</p>",
  "exercice": "<ol>\n  <li>Import the inventory and map tree health with circles at the real crown size.</li>\n  <li>Compute the canopy cover of each green space: sum of crown areas ÷ area of the space (hint: <i>Join attributes by location (summary)</i>).</li>\n  <li>With a real Sentinel-2 image, compute the NDVI of Tlemcen and compare districts.</li>\n</ol>"
 },
 "v8": {
  "titre": "Project, budget and participation",
  "resume": "Cost a project (quantities and estimate), write a management plan, involve residents and evaluate results.",
  "quiz": [
   {
    "question": "What does the bill of quantities of a project contain?",
    "choix": [
     "Quantities measured on the plan",
     "The list of users",
     "Unit prices",
     "The maintenance schedule"
    ],
    "explication": "The bill of quantities measures quantities; costing multiplies them by unit prices."
   },
   {
    "question": "30 trees at 9,000 DA each cost…",
    "choix": [
     "2,700,000 DA",
     "39,000 DA",
     "27,000 DA",
     "270,000 DA"
    ],
    "explication": "30 × 9,000 = 270,000 DA."
   },
   {
    "question": "Why present maintenance costs with the construction estimate?",
    "choix": [
     "Because the law forbids maintenance",
     "Because a green space costs mostly after it is built",
     "To inflate the budget",
     "It is not useful"
    ],
    "explication": "Water, labour and replacements weigh every year."
   },
   {
    "question": "Which is a monitoring indicator of a management plan?",
    "choix": [
     "Canopy cover",
     "The architect's name",
     "The brand of mowers",
     "The colour of the benches"
    ],
    "explication": "Canopy cover measures change in tree cover."
   },
   {
    "question": "What is a main benefit of resident participation?",
    "choix": [
     "Skipping the assessment",
     "Reducing the number of trees",
     "Removing maintenance",
     "A space that is better used and better respected"
    ],
    "explication": "Residents who took part take ownership of the space."
   }
  ]
 },
 "v8-l1": {
  "titre": "Bill of quantities and cost estimate",
  "objectifs": [
   "Draw up the bill of quantities of a project",
   "Build a cost estimate with unit prices",
   "Estimate the annual maintenance cost"
  ],
  "contenu": "\n<p>The <b>cost estimate</b> gives the forecast cost of the project. It is built in two steps: the <b>bill of quantities</b> (measured on the master plan) then the <b>costing</b> (quantity × unit price).</p>\n<h4>Structure of an estimate</h4>\n<div class=\"tab-wrap\"><table class=\"tab\"><thead><tr><th>No.</th><th>Item</th><th>Unit</th><th>Quantity</th><th>Unit price (DA)</th><th>Amount (DA)</th></tr></thead><tbody>\n<tr><td>1</td><td>Earthworks and topsoil supply</td><td>m³</td><td>300</td><td>2,500</td><td>750,000</td></tr>\n<tr><td>2</td><td>Supply and planting of trees (girth 12-14 cm)</td><td>u</td><td>30</td><td>9,000</td><td>270,000</td></tr>\n<tr><td>3</td><td>Supply and planting of shrubs</td><td>u</td><td>400</td><td>600</td><td>240,000</td></tr>\n<tr><td>4</td><td>Drip network</td><td>lm</td><td>900</td><td>350</td><td>315,000</td></tr>\n<tr><td>5</td><td>Benches</td><td>u</td><td>20</td><td>35,000</td><td>700,000</td></tr>\n<tr><td colspan=\"5\"><b>Total excluding tax</b></td><td><b>2,275,000</b></td></tr>\n</tbody></table></div>\n<p><b>Note:</b> these prices are <b>fictional</b>, for the exercise. In real situations, use prices from the municipality's recent contracts or from contractor quotes. Then add VAT and a contingency margin (often 5 to 10%).</p>\n<h4>Management cost</h4>\n<p>A green space costs mostly <b>after</b> it is built: water, labour, replacements, repairs. Estimate it per m² by maintenance class (level 6) and present it with the estimate, so the client knows whether they can afford to maintain it.</p>\n<div class=\"astuce\"><b>Spreadsheet:</b> the workbook <code>devis_estimatif.xlsx</code> contains the formulas (Amount = Quantity × UP, subtotals, VAT, contingencies). Change the quantities and everything recalculates.</div>",
  "exercice": "<ol>\n  <li>From your master plan (level 4) and furniture list, draw up the bill of quantities.</li>\n  <li>Fill in <code>devis_estimatif.xlsx</code> with your quantities. What is the total cost including tax with 10% contingency?</li>\n  <li>Estimate the project's annual water cost with your level 5 calculations (fictional water price: 40 DA/m³).</li>\n</ol>"
 },
 "v8-l2": {
  "titre": "The management plan of a green space",
  "objectifs": [
   "Know the content of a management plan",
   "Write management sheets for each space",
   "Choose monitoring indicators"
  ],
  "contenu": "\n<p>The <b>management plan</b> organises the maintenance of a green space (or all those of a municipality) over several years. It is the roadmap for teams and the basis for contractors' specifications.</p>\n<h4>Typical content</h4>\n<ol>\n  <li><b>Assessment</b>: inventory, health, uses, problems (levels 1 to 3).</li>\n  <li><b>Objectives</b>: e.g. “raise canopy cover from 20% to 25% in 10 years”, “cut water use by 30%”, “zero pesticides”.</li>\n  <li><b>Maintenance classes</b> and differentiated-management map (level 6).</li>\n  <li><b>Management sheets</b>: for each space, operations, frequency, period and resources (staff, equipment).</li>\n  <li><b>Multi-year programme</b>: planting, replacements, renovations, with a yearly budget.</li>\n  <li><b>Monitoring indicators</b>: trees planted and dead, canopy cover, m³ of water used, m²/inh., user satisfaction.</li>\n</ol>\n<h4>Example management sheet</h4>\n<div class=\"tab-wrap\"><table class=\"tab\"><thead><tr><th>Operation</th><th>Frequency</th><th>Period</th></tr></thead><tbody>\n<tr><td>Mowing the central lawn</td><td>Twice a month</td><td>March to June, October</td></tr>\n<tr><td>Cutting the meadow</td><td>Twice a year</td><td>June and October</td></tr>\n<tr><td>Checking irrigation</td><td>Every week</td><td>May to September</td></tr>\n<tr><td>Tree health inspection</td><td>Once a year</td><td>Winter</td></tr>\n<tr><td>Playground inspection</td><td>Visual every week, in-depth every year</td><td>All year</td></tr>\n</tbody></table></div>",
  "exercice": "<ol>\n  <li>Write the management plan (4 pages maximum) of your project's square with the lesson's structure.</li>\n  <li>Fill in a management sheet for each zone (lawn, beds, trees, play).</li>\n  <li>Choose 5 indicators and their target value in 5 years.</li>\n</ol>"
 },
 "v8-l3": {
  "titre": "Involving residents and evaluating the project",
  "objectifs": [
   "Organise resident participation",
   "Prepare and analyse a user survey",
   "Present a project clearly"
  ],
  "contenu": "\n<p>A green space designed <b>with</b> residents is better respected and better used. Participation can take place at every stage.</p>\n<h4>Forms of participation</h4>\n<ul>\n  <li><b>Before the project</b>: questionnaire, neighbourhood meeting, assessment walk with residents, workshops with children from the nearby school.</li>\n  <li><b>During</b>: presentation of sketches, choice between two options, community planting day.</li>\n  <li><b>After</b>: community gardens, tree sponsorship by families or classes, user committees, reporting problems.</li>\n</ul>\n<h4>The user survey</h4>\n<p>Short questions, closed if possible: frequency of visits, access time, activities, satisfaction (1 to 5) with shade, cleanliness, safety, play, and one open question “what should be improved?”. The file <code>enquete_usagers.csv</code> contains 120 fictional answers to analyse.</p>\n<h4>Presenting the project</h4>\n<p>For a jury or a municipal council: a poster or slide show with the assessment (maps), the master plan, two or three mood views, the plant palette, the estimate and the management plan. A clear message: “what the project brings to the district”.</p>\n<div class=\"astuce\"><b>Key point:</b> evaluation closes the loop. Indicators (canopy, m²/inh., water, satisfaction) measured before and after show whether objectives are met and feed the next project.</div>",
  "exercice": "<ol>\n  <li>Analyse <code>enquete_usagers.csv</code> in a spreadsheet: average score per criterion, share of users coming on foot, three most requested improvements.</li>\n  <li>Propose three participation actions for your square project.</li>\n  <li>Final project: present your square (assessment, master plan, palette, irrigation, estimate, management plan) in 10 slides.</li>\n</ol>"
 }
});
