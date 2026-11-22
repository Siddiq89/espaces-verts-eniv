def K(n): return f"<!--code:{n}-->"
def Q(question, choix, explication): return dict(question=question, choix=choix, explication=explication)
def L(titre, objectifs, contenu, exercice): return dict(titre=titre, objectifs=objectifs, contenu=contenu, exercice=exercice)

EN = {}
EN["ev"] = dict(nom="Green spaces", accroche="Green spaces, from the tree to the urban project",
  lead="A step-by-step course to understand, design and manage urban green spaces: types and services, a plant palette suited to the Tlemcen climate, tree inventory and assessment, designing a neighbourhood square, planting and water-saving irrigation, maintenance and differentiated management, mapping with QGIS, cost estimate and management plan. Each lesson offers a practical exercise, videos and an end-of-level quiz.")

# ---------------- Level 1 ----------------
EN["v1"] = dict(titre="Understanding urban green spaces",
  resume="Define and classify green spaces, know their roles for the city and its inhabitants, and understand the regulatory framework and stakeholders in Algeria.",
  quiz=[
    Q("Under Law 07-06, a row of trees along a boulevard belongs to which category?", ["Tree alignments", "Specialised gardens", "Urban parks", "Private gardens"], "Trees planted along streets and roads form the tree-alignment category."),
    Q("A district of 20,000 inhabitants has 12 ha of public green space. How many m² per inhabitant?", ["0.6 m²/inh.", "6 m²/inh.", "60 m²/inh.", "16 m²/inh."], "12 ha = 120,000 m²; 120,000 ÷ 20,000 = 6 m²/inh."),
    Q("What does the “300” in the 3-30-300 rule mean?", ["300 trees per district", "No more than 300 m to a green space", "300 m² of lawn per school", "300 litres of water per tree"], "Every resident should live less than 300 m from a green space."),
    Q("How do trees reduce urban heat islands?", ["Through shade and evapotranspiration", "By absorbing noise", "By increasing runoff", "By reflecting street-light"], "Shade and water evaporated by leaves cool the air."),
    Q("Which planning document sets land-use rules sector by sector?", ["The PDAU", "The POS", "The maintenance specifications", "The tree inventory"], "The POS details, at sector level, what the PDAU sets at municipal level."),
  ])
EN["v1-l1"] = L("What is a green space? Definitions and types",
  ["Define an urban green space and its components", "Distinguish the main categories of green spaces", "Recognise these categories in a city such as Tlemcen"],
  """
<p>A <b>green space</b> is a public or private area largely covered with vegetation (trees, shrubs, lawns, flowers), landscaped or not, located in the city or on its outskirts. It can be large (a park, an urban forest) or very small (a planter, a row of trees along a boulevard).</p>
<p>A green space is always a <b>living system</b>: soil, water, plants, wildlife (birds, insects, hedgehogs), facilities (paths, benches, play equipment, lighting) and <b>users</b>. Managing it means taking care of all of these at once.</p>
<h4>The main categories</h4>
<p>The 2007 Algerian law on green spaces (see lesson 3) distinguishes several categories. They are useful to organise an inventory:</p>
<ul>
  <li><b>Urban and peri-urban parks</b>: large areas (often more than a few hectares) with walks, playgrounds, water features, visitor facilities.</li>
  <li><b>Public gardens</b>: smaller neighbourhood spaces: squares, planted plazas, estate gardens.</li>
  <li><b>Specialised gardens</b>: botanical garden, rose garden, exhibition garden, arboretum.</li>
  <li><b>Collective or residential gardens</b>: green spaces at the foot of apartment blocks, schools, hospitals.</li>
  <li><b>Private gardens</b>: gardens of houses.</li>
  <li><b>Urban forests</b>: woodland in or next to the city, open for walks.</li>
  <li><b>Tree alignments</b>: trees planted along streets, boulevards and roads.</li>
</ul>
<p>We often add <b>accompanying green spaces</b> (embankments, roundabouts, central reservations) and <b>natural areas</b> (wadi banks, wasteland, hillsides), which also play a major ecological role.</p>
<h4>Examples around Tlemcen</h4>
<p>The Lalla Setti plateau (forest and leisure area overlooking the city), the public gardens of the city centre, the hackberry and plane-tree alignments of the main boulevards, the peri-urban olive groves and orchards: each type requires different management.</p>
<div class="astuce"><b>Key point:</b> classifying green spaces by category is the first step of any assessment. Without a typology, you can neither count, compare nor plan maintenance.</div>""",
  """<ol>
  <li>On a map of your city (or in Google Earth), find at least one example of each category.</li>
  <li>For each example, note: name, category, approximate area, district.</li>
  <li>Open the <code>espaces_verts.geojson</code> layer from the practical data in QGIS and look at the <code>categorie</code> field: which categories are present in the fictional study area?</li>
</ol>""")
EN["v1-l2"] = L("The roles of green spaces: ecosystem services",
  ["List the services provided by green spaces", "Explain how trees counter heat islands", "Know the main indicators (m² per inhabitant, 3-30-300 rule)"],
  """
<p>Green spaces are not mere “decoration”. They provide the city with <b>ecosystem services</b>, i.e. free benefits supplied by nature.</p>
<h4>Regulating services</h4>
<ul>
  <li><b>Local climate</b>: tree shade and leaf evapotranspiration cool the air. Under a large tree, the felt temperature in summer can drop by several degrees. Green spaces reduce <b>urban heat islands</b> (mineral districts much hotter than their surroundings).</li>
  <li><b>Water</b>: vegetated soil infiltrates rain, reduces runoff and flooding, recharges aquifers.</li>
  <li><b>Air and noise</b>: foliage traps part of the dust; thick hedges slightly reduce noise and break the wind.</li>
  <li><b>Soil</b>: roots hold the soil on embankments and hillsides (erosion control).</li>
</ul>
<h4>Supporting services and biodiversity</h4>
<p>Trees, hedges and meadows offer shelter and food to birds, pollinating insects and small wildlife. Connected together (alignments, wadi banks), they form a <b>green network</b> that lets species move around.</p>
<h4>Cultural and social services</h4>
<p>Relaxation, sport, children's play, meeting people, physical and mental health, environmental education, property value, identity and landscape of the city.</p>
<h4>Some indicators</h4>
<ul>
  <li><b>Green space per inhabitant</b> (m²/inh.): total public green space ÷ population. A frequently quoted value (attributed to the WHO) is at least <b>9 m² per inhabitant</b>; many cities aim for 10 to 15 m².</li>
  <li><b>Canopy cover</b>: share of the area covered by tree crowns, seen from above.</li>
  <li><b>3-30-300 rule</b>: every resident should see at least <b>3 trees</b> from home, live in a district with <b>30%</b> canopy cover, and live less than <b>300 m</b> from a green space.</li>
</ul>
<div class="astuce"><b>Quick calculation:</b> a district of 12,000 inhabitants with 7.2 ha of public green space has 72,000 ÷ 12,000 = <b>6 m²/inh.</b>, below the 9 m²/inh. benchmark.</div>""",
  """<ol>
  <li>Choose a green space you know and sort its benefits into the three families (regulation, biodiversity, social).</li>
  <li>Using the <code>quartiers_population.csv</code> file, compute the green space per inhabitant of each district (field <code>surface_ev_m2</code>).</li>
  <li>Does the district reach 9 m²/inh.? How many m² would have to be created to reach it?</li>
</ol>""")
EN["v1-l3"] = L("Regulatory framework and stakeholders in Algeria",
  ["Know Law No. 07-06 of 13 May 2007 on green spaces", "Identify who creates and manages green spaces", "Know where to find official texts"],
  """
<p>In Algeria, the reference text is <b>Law No. 07-06 of 13 May 2007 on the management, protection and development of green spaces</b>, published in the Official Journal (JORADP). Its main objectives are:</p>
<ul>
  <li>to improve the urban living environment and develop green spaces in every city;</li>
  <li>to <b>classify</b> green spaces into categories (those seen in lesson 1);</li>
  <li>to <b>protect</b> classified green spaces against changes of use and damage;</li>
  <li>to require green spaces to be taken into account in <b>planning instruments</b> (PDAU, POS) and building projects.</li>
</ul>
<p>Implementing texts specify the procedures (classification, management, specifications). They change over time: always check the version in force on the Official Journal website.</p>
<h4>The stakeholders</h4>
<ul>
  <li><b>The municipality (APC)</b>: management and maintenance of most public green spaces, often through a green-space department or a municipal company.</li>
  <li><b>The wilaya</b>: environment directorate, planning directorate, project funding.</li>
  <li><b>The forest conservation service</b>: peri-urban and recreational forests.</li>
  <li><b>Companies and design offices</b>: design, planting works, contracted maintenance.</li>
  <li><b>Associations and residents</b>: planting, awareness-raising, community gardens, reporting damage.</li>
</ul>
<h4>Planning documents</h4>
<p>The <b>PDAU</b> (master plan for development and urban planning) sets the main orientations at municipal level; the <b>POS</b> (land-use plan) specifies the rules by sector. These documents reserve land for future parks and set the required amount of greenery.</p>
<div class="astuce"><b>Good habit:</b> before any project, ask for the sector's POS and identify existing or planned green spaces. A classified green space cannot become a car park or a building plot.</div>""",
  """<ol>
  <li>Find Law No. 07-06 of 13 May 2007 on the Official Journal website (joradp.dz) and write down the exact list of green-space categories.</li>
  <li>Draw a diagram of the stakeholders in your municipality: who designs, who funds, who maintains, who controls?</li>
  <li>In half a page, explain to an elected official why a classified green space must be protected.</li>
</ol>""")

# ---------------- Level 2 ----------------
EN["v2"] = dict(titre="Plants in the urban environment",
  resume="Name and recognise plants, know layers and growth habits, choose a plant palette suited to the Tlemcen climate.",
  quiz=[
    Q("How is the scientific name of the Aleppo pine written correctly?", ["<i>Pinus halepensis</i>", "<i>pinus Halepensis</i>", "PINUS HALEPENSIS", "<i>Pinus Halepensis</i>"], "Genus capitalised, species in lower case, all in italics."),
    Q("A tree that keeps its leaves in winter has … foliage.", ["deciduous", "evergreen", "compound", "columnar"], "Evergreen: it keeps its leaves all year round."),
    Q("Why avoid more than 10% of a single species in a tree population?", ["To reduce the risk that a disease or pest destroys a large share of the trees", "Because the law forbids it", "To simplify watering", "Because nurseries do not have enough"], "Diversity limits losses when a species-specific pest strikes."),
    Q("Which species is invasive and must not be planted?", ["<i>Quercus ilex</i>", "<i>Celtis australis</i>", "<i>Ailanthus altissima</i>", "<i>Myrtus communis</i>"], "Tree of heaven suckers everywhere and smothers native vegetation."),
    Q("The ash tree produces as fruit…", ["cones", "winged samaras", "pods", "drupes"], "Ash fruits are samaras with a wing."),
  ])
EN["v2-l1"] = L("Naming plants: applied botany basics",
  ["Write a scientific name correctly", "Distinguish vegetation layers", "Describe a plant: foliage, habit, mature size"],
  """
<p>The same tree may have several common names depending on the region (in French, Arabic, Tamazight). To avoid errors in an inventory or a nursery order, we use the <b>scientific name</b>, in Latin, valid worldwide.</p>
<h4>The scientific name</h4>
<ul>
  <li>It has two words: the <b>genus</b> (capital letter) and the <b>species</b> (lower case), written in <i>italics</i>: <i>Pinus halepensis</i> (Aleppo pine), <i>Olea europaea</i> (olive).</li>
  <li>A <b>cultivar</b> can be added in quotes: <i>Nerium oleander</i> 'Album' (white-flowered oleander).</li>
  <li>The <b>family</b> groups related genera: Pinaceae, Oleaceae, Fabaceae…</li>
</ul>
<h4>Layers</h4>
<ul>
  <li><b>Tree layer</b>: trees, more than 7 to 8 m when mature.</li>
  <li><b>Shrub layer</b>: shrubs and subshrubs, 1 to 7 m (hedges, borders).</li>
  <li><b>Herbaceous layer</b>: lawn, meadow, perennials, annual flowers.</li>
  <li><b>Ground covers and climbers</b>: creeping plants covering the soil, plants climbing walls and pergolas.</li>
</ul>
<p>A pleasant, biodiversity-rich green space combines several layers.</p>
<h4>Describing a plant</h4>
<ul>
  <li><b>Foliage</b>: evergreen (keeps its leaves in winter) or deciduous (loses them).</li>
  <li><b>Habit</b>: overall shape: upright, spreading, weeping, columnar, rounded.</li>
  <li><b>Mature size</b>: height and width after 20 to 30 years. This decides the planting distance from façades and utility networks.</li>
  <li><b>Requirements</b>: sun or shade, water, soil type, resistance to cold and wind.</li>
</ul>
<div class="astuce"><b>Common mistake:</b> planting a tree according to its size when bought. A 2 m Aleppo pine in the nursery will exceed 15 m: it must not be planted 2 m from a façade.</div>""",
  """<ol>
  <li>Choose 5 trees in your neighbourhood or school. For each, record the common name, the scientific name (use the Pl@ntNet app), the foliage (evergreen or deciduous) and the habit.</li>
  <li>Write the scientific names correctly (capitalised genus, italics).</li>
  <li>Sort them by layer and estimate their mature size.</li>
</ol>""")
EN["v2-l2"] = L("Choosing a plant palette suited to Tlemcen",
  ["Link plant choice to Tlemcen's Mediterranean climate", "Use a palette of water-saving trees, shrubs and ground covers", "Avoid invasive and highly allergenic species"],
  """
<p>Tlemcen has a <b>Mediterranean climate</b>: rain concentrated from October to April, hot dry summer, possible frost in winter (the city lies at about 800 m altitude). Good plants must therefore <b>tolerate summer drought AND winter cold</b>.</p>
<h4>Selection principles</h4>
<ul>
  <li><b>The right plant in the right place</b>: mature size compatible with the available space, exposure, soil.</li>
  <li><b>Prefer native or well-adapted species</b>: they need less water and maintenance and feed local wildlife.</li>
  <li><b>Diversify</b>: avoid more than 10% of a single species in a tree population, to limit disease or pest risks.</li>
  <li><b>Think about water</b>: group plants by their needs (hydrozones).</li>
</ul>
<h4>Example palette (file <code>palette_vegetale.csv</code>)</h4>
<div class="tab-wrap"><table class="tab"><thead><tr><th>Layer</th><th>Species</th><th>Strengths</th></tr></thead><tbody>
<tr><td>Tree</td><td><i>Pinus halepensis</i> (Aleppo pine)</td><td>Native, very drought-tolerant; watch out for the processionary moth.</td></tr>
<tr><td>Tree</td><td><i>Celtis australis</i> (European hackberry)</td><td>Excellent street tree, dense shade, hardy.</td></tr>
<tr><td>Tree</td><td><i>Fraxinus angustifolia</i> (narrow-leaved ash)</td><td>Native, fast-growing, likes moist soils (banks).</td></tr>
<tr><td>Tree</td><td><i>Olea europaea</i> (olive)</td><td>Mediterranean symbol, very water-sparing.</td></tr>
<tr><td>Tree</td><td><i>Ceratonia siliqua</i> (carob)</td><td>Evergreen, sparing; sensitive to hard frost.</td></tr>
<tr><td>Tree</td><td><i>Quercus ilex</i> (holm oak)</td><td>Native, long-lived, tolerates cold and drought.</td></tr>
<tr><td>Shrub</td><td><i>Pistacia lentiscus</i> (mastic tree)</td><td>Native, informal hedges, very sparing.</td></tr>
<tr><td>Shrub</td><td><i>Nerium oleander</i> (oleander)</td><td>Summer flowering; toxic plant, avoid near playgrounds.</td></tr>
<tr><td>Shrub</td><td><i>Myrtus communis</i> (myrtle)</td><td>Native, fragrant, tolerates pruning.</td></tr>
<tr><td>Ground cover</td><td><i>Rosmarinus officinalis</i> (prostrate rosemary)</td><td>Attracts bees, no watering once established.</td></tr>
</tbody></table></div>
<h4>Species to avoid or watch</h4>
<ul>
  <li><b>Invasive</b>: tree of heaven (<i>Ailanthus altissima</i>) suckers everywhere and smothers native vegetation. Do not plant it; remove it gradually.</li>
  <li><b>Highly allergenic</b>: cypress, plane, birch: do not plant them in large numbers near schools and hospitals.</li>
  <li><b>Water-hungry</b>: large fine-turf lawns in full sun, to be kept for areas actually used.</li>
</ul>""",
  """<ol>
  <li>Open <code>palette_vegetale.csv</code> (in a spreadsheet or QGIS) and sort the species by water needs.</li>
  <li>Propose a palette for a 2,000 m² neighbourhood square: 3 trees, 4 shrubs, 2 ground covers, justifying each choice.</li>
  <li>Check that no species exceeds 10% of the trees proposed for all the squares in the area.</li>
</ol>""")
EN["v2-l3"] = L("Recognising plants in the field",
  ["Use simple identification criteria", "Use an identification app and check its result", "Build a small herbarium or identification sheet"],
  """
<p>In the field, a plant is identified by observing several <b>criteria</b>, from the most general to the most precise:</p>
<ol>
  <li><b>Habit and bark</b>: silhouette, smooth, furrowed bark, or bark peeling in plates (plane).</li>
  <li><b>Leaves</b>: simple or compound (several leaflets), alternate or opposite on the twig, margin shape (entire, toothed, lobed), needles (conifers) in bundles of 2, 3 or 5.</li>
  <li><b>Flowers and fruits</b>: cones (pines), pods (carob, pagoda tree), drupes (olive, hackberry), winged samaras (ash).</li>
</ol>
<h4>Identification apps</h4>
<p><b>Pl@ntNet</b> (free) recognises a plant from a photo of a leaf, flower or fruit. It suggests several names with a confidence percentage. <b>Always check</b> with a second criterion (fruit, bark) or a guide: apps are often wrong about ornamental plants and young plants.</p>
<h4>The identification sheet</h4>
<p>For each species found, prepare a sheet: scientific name, family, common name in French and Arabic, photos of habit, leaf, bark and fruit, mature size, uses in green spaces. Together, these sheets form a <b>digital herbarium</b>, very useful for inventories.</p>
<div class="astuce"><b>Field tip:</b> always photograph a leaf placed on your notebook next to a ruler: real size helps identification a lot.</div>""",
  """<ol>
  <li>30-minute outing in the school grounds or a nearby garden: identify 8 species with Pl@ntNet.</li>
  <li>For each one, check the result with a second criterion (fruit, bark, leaf arrangement).</li>
  <li>Produce 3 complete identification sheets and share them with the class.</li>
</ol>""")

# ---------------- Level 3 ----------------
EN["v3"] = dict(titre="Tree inventory and assessment",
  resume="Organise an inventory, measure trees (girth, height, crown) and assess their health and risk.",
  quiz=[
    Q("At what height is a tree's girth measured?", ["At ground level", "At 1.30 m", "At 2 m", "Below the first branch"], "The standard measurement is taken at 1.30 m, breast height."),
    Q("A trunk has a girth of 157 cm. Its diameter is about…", ["25 cm", "50 cm", "78 cm", "157 cm"], "157 ÷ 3.14 ≈ 50 cm."),
    Q("Distance 20 m, angle 30° (tan = 0.577), eyes at 1.5 m. Tree height?", ["≈ 10 m", "≈ 13 m", "≈ 20 m", "≈ 31.5 m"], "20 × 0.577 + 1.5 ≈ 13 m."),
    Q("Which defect is a frequent failure point?", ["A V-shaped fork with included bark", "Evergreen leaves", "Smooth bark", "Abundant flowering"], "Included bark prevents the two stems of the fork from bonding."),
    Q("Why is the same defect more serious above a playground?", ["Because the tree grows worse there", "Because the target (children) is very present", "Because the law forbids trees near play areas", "It is not more serious"], "Risk combines the probability of failure and the presence of targets."),
  ])
EN["v3-l1"] = L("Organising a tree inventory",
  ["Understand what a tree inventory is for", "Fill in a complete tree record", "Prepare GPS survey and coding"],
  """
<p>The <b>tree inventory</b> is the located list of all trees managed by a municipality, with their characteristics. It is the basic tool to plan maintenance, estimate budgets, monitor the tree population and justify decisions (felling, replanting).</p>
<h4>The tree record</h4>
<div class="tab-wrap"><table class="tab"><thead><tr><th>Field</th><th>Example</th><th>Note</th></tr></thead><tbody>
<tr><td>Identifier</td><td>ARB-0042</td><td>Unique, never reused</td></tr>
<tr><td>Species</td><td><i>Celtis australis</i></td><td>Scientific + common name</td></tr>
<tr><td>Coordinates</td><td>X = 653,812; Y = 3,860,455</td><td>UTM 30N (EPSG 32630), GPS or map</td></tr>
<tr><td>Girth at 1.30 m</td><td>142 cm</td><td>Tape measure</td></tr>
<tr><td>Height</td><td>11 m</td><td>Clinometer or hypsometer</td></tr>
<tr><td>Crown diameter</td><td>8 m</td><td>Mean of two perpendicular measurements</td></tr>
<tr><td>Stage</td><td>Adult</td><td>Young, adult, mature, senescent</td></tr>
<tr><td>Health</td><td>Fair</td><td>Good, fair, poor, dead</td></tr>
<tr><td>Defects</td><td>Dead branch</td><td>Coded list (lesson 3)</td></tr>
<tr><td>Proposed action</td><td>Safety pruning</td><td>With a deadline</td></tr>
</tbody></table></div>
<h4>Preparing the survey</h4>
<ul>
  <li><b>Divide</b> the city into sectors (districts, streets) and give each sector a code.</li>
  <li><b>Code</b> values in advance (pick lists) to avoid typing errors: “Fair”, “fair”, “FR” must become a single value.</li>
  <li><b>Tools</b>: paper sheet or digital form (QField, ODK Collect, KoboToolbox), GPS or smartphone, tape measure, clinometer, camera.</li>
  <li><b>Photograph</b> each tree and name the photo with its identifier.</li>
</ul>
<div class="astuce"><b>Good habit:</b> test the record on 10 trees before launching the survey. You always discover a missing field or an incomplete pick list.</div>
<p><i>Note: in the practical data files, field values remain in French (e.g. état = Bon, Moyen, Mauvais, Mort).</i></p>""",
  """<ol>
  <li>Open <code>inventaire_arbres.csv</code> in a spreadsheet. Identify the fields and compare them with the record in the lesson.</li>
  <li>How many trees are in the inventory? How many different species? What is the most frequent species, and does it exceed 10%?</li>
  <li>Inventory 10 trees at your school with <code>fiche_inventaire_arbre.csv</code> (empty template).</li>
</ol>""")
EN["v3-l2"] = L("Measuring a tree: girth, height, crown",
  ["Measure girth at 1.30 m and derive the diameter", "Compute a tree's height from an angle and a distance", "Estimate crown area"],
  """
<h4>Girth and diameter</h4>
<p>Measure the trunk <b>girth</b> (C) with a tape at <b>1.30 m</b> above ground (breast height), on the uphill side on a slope. The diameter is:</p>
<p class="formule">D = C ÷ π &nbsp;&nbsp; (example: 142 cm ÷ 3.1416 ≈ 45 cm)</p>
<p>The <b>basal area</b> (trunk cross-section) is g = π × D² ÷ 4. For D = 0.45 m: g ≈ 0.16 m².</p>
<h4>Height with a clinometer</h4>
<p>Stand at a known distance <b>d</b> from the trunk (e.g. 15 m, taped), aim at the top and read the angle <b>α</b>. Then:</p>
<p class="formule">h = d × tan(α) + eye height</p>
<p>Example: d = 15 m, α = 32°, eyes at 1.60 m: h = 15 × 0.625 + 1.60 ≈ <b>11 m</b>. A smartphone with a clinometer app is enough for practical work.</p>
<h4>Stick method (no instrument)</h4>
<p>Hold a stick vertically at arm's length, as long as the eye-to-hand distance. Step back until the bottom and top of the stick line up with the foot and the top of the tree: your distance to the trunk is roughly equal to the tree's height.</p>
<h4>Crown</h4>
<p>Measure the crown diameter on the ground in two perpendicular directions (north-south and east-west) and average them. Crown area ≈ π × (mean diameter ÷ 2)². For 8 m: ≈ 50 m² of shade on the ground.</p>
<div class="astuce"><b>In QGIS:</b> once the inventory is imported, the field calculator gives the diameter with the expression <code>"circonference_cm" / pi()</code>.</div>""",
  """<ol>
  <li>Measure 3 trees: girth at 1.30 m, height (clinometer and stick method), crown diameter.</li>
  <li>Compute the diameter, basal area and crown area of each.</li>
  <li>Compare the two height methods: what difference do you find?</li>
  <li>In the spreadsheet, add a computed <code>diametre_cm</code> column to <code>inventaire_arbres.csv</code>.</li>
</ol>""")
EN["v3-l3"] = L("Health assessment and risk evaluation",
  ["Recognise the main tree defects", "Apply the logic of Visual Tree Assessment (VTA)", "Classify a tree and propose an action with a deadline"],
  """
<p>An unhealthy tree may drop a branch or fall. In the city, <b>user safety</b> is the priority. Assessment is first visual, following the <b>Visual Tree Assessment</b> (VTA) method, then, if needed, with instruments (resistograph, tomograph) by a specialist.</p>
<h4>What to look at, from the base to the top</h4>
<ul>
  <li><b>Root collar and roots</b>: fungi at the base, roots cut by works, lifted soil (sign of tilting).</li>
  <li><b>Trunk</b>: cavities, cracks, loose bark, seepage, impact wounds (cars, strimmers), recent leaning.</li>
  <li><b>Main limbs</b>: V-shaped forks with included bark (frequent failure point), stubs from bad pruning.</li>
  <li><b>Crown</b>: dead branches, sparse or yellowing foliage, pest attacks.</li>
</ul>
<h4>Classify and decide</h4>
<div class="tab-wrap"><table class="tab"><thead><tr><th>Condition</th><th>Signs</th><th>Typical action</th></tr></thead><tbody>
<tr><td>Good</td><td>No significant defect</td><td>Normal monitoring (every 3 to 5 years)</td></tr>
<tr><td>Fair</td><td>Limited defects: deadwood, small wound</td><td>Maintenance pruning, new visit in 1 to 2 years</td></tr>
<tr><td>Poor</td><td>Serious defect: large cavity, crack, fungus at the base</td><td>Detailed assessment, quick make-safe</td></tr>
<tr><td>Dead / dangerous</td><td>Dead tree or imminent failure</td><td>Safety perimeter, urgent felling, replanting</td></tr>
</tbody></table></div>
<p><b>Risk</b> also depends on the <b>target</b>: a weak tree above a playground is far more urgent than the same tree in a little-visited wood.</p>
<div class="astuce"><b>Golden rule:</b> never fell a tree without a written, photographed assessment. And every felled tree should be replaced (if possible by two).</div>""",
  """<ol>
  <li>In <code>inventaire_arbres.csv</code>, filter trees whose <code>etat</code> is “Mauvais” (poor) or “Mort” (dead). How many are there? In which spaces?</li>
  <li>Cross with the <code>cible</code> field (use intensity): list the 5 highest-priority trees.</li>
  <li>For each, propose an action and a deadline (immediate, 3 months, 1 year).</li>
</ol>""")

# ---------------- Level 4 ----------------
EN["v4"] = dict(titre="Designing a green space",
  resume="Analyse a site, write a brief, compose a master plan and choose accessible, safe facilities.",
  quiz=[
    Q("What do “desire lines” worn into the grass show?", ["Areas to fence", "Pedestrians' real routes, where to put paths", "Buried networks", "Frost pockets"], "They reveal the routes users actually take."),
    Q("Where should trees be placed to shade a bench in the afternoon?", ["North of the bench", "South and west of the bench", "East only", "It does not matter"], "Afternoon sun comes from the south-west."),
    Q("What minimum width is commonly used for an accessible path?", ["0.80 m", "1.00 m", "1.40 m", "3.00 m"], "1.40 m lets a wheelchair and a pedestrian pass."),
    Q("What is standard EN 1177 about?", ["Impact-absorbing surfaces of playgrounds", "Street lighting", "Irrigation", "Tree pruning"], "EN 1177 covers impact-absorbing surfaces; EN 1176 covers equipment."),
    Q("How is a tree shown on a master plan?", ["As a 1 mm dot", "As a circle the size of its mature crown", "By its name only", "It is not shown"], "Mature size lets you check distances and future shade."),
  ])
EN["v4-l1"] = L("Analysing the site and writing the brief",
  ["Carry out a site analysis before drawing", "Identify users and their needs", "Write a design brief"],
  """
<p>A good project starts <b>on site</b>, not on paper. Site analysis lists everything that will constrain or enrich the project.</p>
<h4>Site analysis grid</h4>
<ul>
  <li><b>Location</b>: district, access, roads, bus stops, nearby schools and facilities.</li>
  <li><b>Topography</b>: slopes, high and low points (where does rainwater go?).</li>
  <li><b>Local climate</b>: sunlight (where is the shade at 3 pm in July?), prevailing winds, frost areas in winter.</li>
  <li><b>Soil</b>: topsoil, fill, rock, compaction.</li>
  <li><b>Existing features</b>: trees to keep, walls, networks (water, electricity, gas, sewerage), overhead and buried.</li>
  <li><b>Current uses</b>: paths worn by pedestrians, improvised football pitches, fly-tipping.</li>
  <li><b>Landscape</b>: views to keep (mountain, minaret, medina), views to screen.</li>
</ul>
<h4>Users</h4>
<p>Who will come? Children, teenagers, families, elderly people, wheelchair users, sportspeople, workers on a break. A <b>quick survey</b> (10-question questionnaire, observation at different times) avoids building a park that suits nobody.</p>
<h4>The brief</h4>
<p>The brief is the written list of what the project must contain, with areas: e.g. “2-6 years playground (150 m²), 6-12 years playground (250 m²), open lawn (800 m²), accessible main path, 20 benches of which 10 in the shade, drinking fountain, toilets, 30 shade trees”. It also sets the <b>budget</b> and the acceptable level of maintenance.</p>
<div class="astuce"><b>Tip:</b> paths worn into the grass by pedestrians (“desire lines”) show where paths should go.</div>""",
  """<ol>
  <li>In QGIS, open the <code>site_projet.geojson</code> layer (fictional 1.2 ha plot) with an OpenStreetMap basemap.</li>
  <li>Produce an analysis map: access, nearby schools, orientation, prevailing winds (north-west in winter), networks (<code>reseaux.geojson</code> layer).</li>
  <li>Write a one-page brief with the area of each element.</li>
</ol>""")
EN["v4-l2"] = L("Composing the plan: sketch and master plan",
  ["Move from the brief to a zoning sketch", "Draw a readable master plan at the right scale", "Apply accessibility and comfort rules"],
  """
<h4>1. Zoning (sketch)</h4>
<p>First draw “bubbles”: quiet area, play area, sports area, main entrance, shaded area. Put noisy areas away from homes and children's play near parents' benches. Test several options.</p>
<h4>2. Circulation</h4>
<ul>
  <li>A <b>main path</b> linking the entrances and following desire lines.</li>
  <li><b>Secondary paths</b> to each area, a walking loop if space allows.</li>
  <li><b>Accessibility</b>: commonly used benchmarks: width of at least 1.40 m, gradient preferably 5% or less, firm surface, benches with armrests about every 50 m.</li>
</ul>
<h4>3. Plants as structure</h4>
<p>Trees form the framework: rows to guide, groves for shade, single trees to mark a place. Put shade trees <b>south and west</b> of benches and play areas (afternoon shade). A windbreak hedge to the north-west protects from the winter wind.</p>
<h4>4. The master plan</h4>
<p>The master plan shows the project from above, to scale (often 1:200 or 1:500), with: north arrow, scale bar, legend, trees (circles of mature crown size), paths, facilities, main dimensions and a title block (title, author, date). It can be drawn by hand, with CAD software or in QGIS (print layout).</p>
<div class="astuce"><b>Check:</b> draw crowns at their mature size. If they overlap a lot or touch façades, move them or change species.</div>""",
  """<ol>
  <li>From your brief (lesson 1), draw two zoning options for the project site.</li>
  <li>Choose one and draw the master plan at 1:500 (paper or QGIS) with north arrow, scale, legend and title block.</li>
  <li>Check the width and gradient of the main paths with the contours in <code>courbes_site.geojson</code> (field <code>altitude</code>).</li>
</ol>""")
EN["v4-l3"] = L("Facilities, furniture and safety",
  ["Choose the furniture of a green space", "Know the safety principles of playgrounds", "Plan lighting, water and cleanliness"],
  """
<h4>Furniture</h4>
<ul>
  <li><b>Benches</b>: in the shade, facing a view or an activity, with a backrest; provide benches for elderly people near entrances.</li>
  <li><b>Litter bins</b>: near entrances, benches and play areas; a clean space stays respected.</li>
  <li><b>Drinking fountains</b>, toilets in large parks.</li>
  <li><b>Signage</b>: entrance map, rules, names of notable trees (education).</li>
  <li><b>Fence and gates</b> if the park closes at night.</li>
</ul>
<h4>Playgrounds</h4>
<p>The European references often used are standards <b>EN 1176</b> (play equipment) and <b>EN 1177</b> (impact-absorbing surfaces). Key principles:</p>
<ul>
  <li>Separate play for small children (2-6 years) and older children (6-12 years).</li>
  <li>Under each item, an <b>impact-absorbing surface</b> (wood chips, sand, suitable artificial turf, tiles) over a safety zone around the equipment.</li>
  <li>No toxic or thorny plants nearby (oleander, for example).</li>
  <li>Shade is essential: metal slides in full sun burn in summer.</li>
  <li>Regular inspection: frequent visual checks, annual in-depth inspection.</li>
</ul>
<h4>Lighting and safety</h4>
<p>Light the main paths without lighting the whole park (nocturnal wildlife needs darkness); keep clear sightlines so users feel safe (no dense 1.5 m shrub masses along paths).</p>""",
  """<ol>
  <li>Place the furniture on your master plan: benches (half in the shade), bins, drinking fountain, signage.</li>
  <li>Draw the playground with its safety zones and type of impact-absorbing surface.</li>
  <li>List the quantities of furniture: they will be used for the cost estimate in level 8.</li>
</ol>""")

# ---------------- Level 5 ----------------
EN["v5"] = dict(titre="Soil, planting and irrigation",
  resume="Prepare the soil, plant a tree properly, compute water needs and design water-saving irrigation.",
  quiz=[
    Q("When are bare-root trees planted?", ["In midsummer", "During dormancy, from November to March, avoiding frost", "Only in April", "Any time"], "Bare roots only tolerate planting during dormancy."),
    Q("Where should the root collar be after planting?", ["Buried 20 cm deep", "At finished ground level", "50 cm above the soil", "In the gravel layer"], "A buried collar leads to bark rot."),
    Q("ET0 = 5 mm/day, KL = 0.3, area 100 m², drip (0.9). Daily need?", ["≈ 167 L", "≈ 150 L", "≈ 1,500 L", "≈ 15 L"], "5 × 0.3 × 100 ÷ 0.9 ≈ 167 litres per day."),
    Q("Why are plants grouped into hydrozones?", ["To water each group according to its real needs", "To make nice colours", "To avoid pruning", "To reduce the number of trees"], "Each irrigation sector receives the dose suited to its plants."),
    Q("What soil volume is often targeted for a large street tree?", ["0.5 m³", "1 m³", "10 m³ or more", "No soil, gravel is enough"], "A large soil volume lets the tree develop its roots and live long."),
  ])
EN["v5-l1"] = L("Soil and the planting pit",
  ["Describe the qualities of good topsoil", "Size a planting pit in the city", "Prevent soil compaction"],
  """
<p>Roots live in the soil: a tree in poor soil will remain stunted all its life, whatever the care. In the city, soil is often <b>fill</b>, rubble, compacted by machines and cars.</p>
<h4>Good topsoil</h4>
<ul>
  <li>Balanced <b>texture</b> (sand, silt, clay): neither too sticky nor too free-draining. Simple test: a handful of moist soil forms a ball that breaks under light pressure.</li>
  <li><b>Organic matter</b>: 2 to 5%; improve it with mature compost.</li>
  <li>Airy <b>structure</b>: air and water must circulate. Compacted soil suffocates roots.</li>
  <li><b>pH</b>: soils around Tlemcen are often calcareous (pH 7.5 to 8.5); choose species that tolerate it.</li>
</ul>
<h4>The planting pit</h4>
<ul>
  <li>Volume: <b>as large as possible</b>. For a large street tree, 10 m³ of soil or more is often targeted; a small 1 m³ pit condemns the tree to stay small and die young.</li>
  <li>When the pavement is narrow, pits are linked (<b>continuous trench</b>) or load-bearing <b>structural soils</b> (soil-stone mixes) let roots grow under pavements.</li>
  <li>Loosen the bottom and sides; do not put a gravel layer at the bottom.</li>
</ul>
<h4>Protecting the soil</h4>
<p>During works, fence the area under the crown of existing trees (no machines, no storage). In green spaces, prevent cars from parking on lawns and at tree bases. <b>Mulch</b> (wood chips, shredded material) protects the soil from the sun, keeps moisture and feeds soil life.</p>""",
  """<ol>
  <li>Take some soil from two places (lawn, street tree base): do the ball test and observe the colour, stones, roots.</li>
  <li>A fictional 300 m street must receive hackberries every 8 m on one side. How many trees? What total soil volume at 10 m³ per tree?</li>
  <li>Propose a solution if the pavement is only 2 m wide.</li>
</ol>""")
EN["v5-l2"] = L("Planting a tree properly",
  ["Choose the season and the plant", "Plant step by step", "Ensure watering and follow-up in the first years"],
  """
<h4>The season</h4>
<p>Plant during <b>dormancy</b>, from November to March, avoiding frost or waterlogged soil. <b>Bare-root</b> plants must be planted in this period; <b>container</b> or <b>root-balled</b> plants tolerate a slightly longer period, but never in midsummer in Tlemcen.</p>
<h4>Choosing the plant</h4>
<p>Straight trunk, intact leader (top shoot), roots not circling in the pot, no wounds. A young plant (girth 10-14 cm) often establishes better than a large specimen.</p>
<h4>Steps</h4>
<ol>
  <li>Dig the pit and loosen the bottom.</li>
  <li>Set the <b>stake(s)</b> before the tree (on the prevailing-wind side), without damaging roots.</li>
  <li>Untangle circling roots, cut damaged roots.</li>
  <li>Position the tree: the <b>root collar</b> (trunk-root junction) at finished ground level, never buried.</li>
  <li>Backfill with topsoil (improved with compost), firm lightly at the base.</li>
  <li>Form a <b>watering basin</b> and water generously (at least 50 litres) even if it rains.</li>
  <li>Tie the tree to the stake with a soft tie that does not hurt the bark; mulch the basin.</li>
</ol>
<h4>Follow-up</h4>
<p>During the <b>first 2 to 3 summers</b>, water regularly (e.g. 50 litres once a week, adjusted to weather and soil). Loosen ties every year, remove stakes after 2 to 3 years. Replace dead trees the following winter.</p>
<div class="astuce"><b>Common mistake:</b> burying the root collar. The trunk bark rots and the tree slowly declines. The collar must stay visible.</div>""",
  """<ol>
  <li>Write an illustrated work sheet (diagram of pit, stake, basin) for planting an ash tree.</li>
  <li>If possible, take part in planting a tree at school and photograph each step.</li>
  <li>Plan the watering schedule for the first 3 summers and the total amount of water.</li>
</ol>""")
EN["v5-l3"] = L("Computing water needs and designing irrigation",
  ["Understand reference evapotranspiration (ET0)", "Compute the water need of a planted area", "Choose a water-saving irrigation system"],
  """
<p>Water is scarce in Tlemcen in summer: a green space must be designed to <b>use little</b>. Needs are computed from <b>reference evapotranspiration</b> (ET0): the amount of water, in mm per day, lost by a well-watered reference lawn. 1 mm on 1 m² = 1 litre.</p>
<h4>The calculation</h4>
<p class="formule">Need (L/day) = ET0 (mm/day) × KL × Area (m²) ÷ Efficiency</p>
<ul>
  <li><b>KL</b>, landscape coefficient: about 0.2 to 0.3 for sparing plants (olive, rosemary, mastic); 0.4 to 0.6 for average beds; 0.7 to 0.8 for lawn.</li>
  <li>System <b>efficiency</b>: drip ≈ 0.9; sprinkler ≈ 0.7 (some water evaporates or blows away).</li>
  <li>Useful rainfall is subtracted when it rains (rarely in summer).</li>
</ul>
<h4>Example (July, ET0 = 6 mm/day, values from <code>et0_tlemcen.csv</code>)</h4>
<div class="tab-wrap"><table class="tab"><thead><tr><th>Zone</th><th>Area</th><th>KL</th><th>System</th><th>Need</th></tr></thead><tbody>
<tr><td>Lawn</td><td>800 m²</td><td>0.8</td><td>Sprinkler (0.7)</td><td>6 × 0.8 × 800 ÷ 0.7 ≈ 5,490 L/day</td></tr>
<tr><td>Mediterranean beds</td><td>800 m²</td><td>0.3</td><td>Drip (0.9)</td><td>6 × 0.3 × 800 ÷ 0.9 = 1,600 L/day</td></tr>
</tbody></table></div>
<p>For the same area, sparing beds on drip use <b>3.4 times less</b> water than sprinkled lawn.</p>
<h4>Good practice</h4>
<ul>
  <li><b>Hydrozones</b>: group plants by needs and water them in separate sectors.</li>
  <li>Water <b>early in the morning or at night</b>, less often but longer (deep roots).</li>
  <li><b>Mulch</b>: greatly reduces evaporation.</li>
  <li>Use <b>non-conventional water</b> where permitted: stored rainwater, treated wastewater according to regulations.</li>
  <li><b>Xeriscaping</b> (dry garden): adapted plants, little lawn, mineral or organic mulch.</li>
</ul>""",
  """<ol>
  <li>Open <code>et0_tlemcen.csv</code> and compute the monthly water need (m³) of the 2,000 m² square from your palette (level 2): state the area of each zone.</li>
  <li>Compare two options: 50% lawn or 10% lawn. What annual water saving?</li>
  <li>The workbook <code>calcul_irrigation.xlsx</code> contains the calculation model: check your results.</li>
</ol>""")

# ---------------- Level 6 ----------------
EN["v6"] = dict(titre="Maintenance and sustainable management",
  resume="Plan maintenance over the year, apply differentiated management, prune correctly and protect plants without pesticides.",
  quiz=[
    Q("Which differentiated-management class covers banks and meadows mown once or twice a year?", ["Class 1, horticultural", "Class 2, gardened", "Class 3, rustic", "Class 4, natural"], "The natural class keeps interventions to a minimum."),
    Q("Where should a branch be cut?", ["Flush with the trunk, removing the collar", "Just outside the collar, without a stub", "30 cm from the trunk", "In the middle of the branch"], "The collar contains the tissues that close the wound."),
    Q("Why is topping a bad practice?", ["It produces weak shoots and large wounds that rot", "It gives too much shade", "It costs too little", "It is compulsory every year"], "A topped tree becomes weak and dangerous."),
    Q("When are trunk collar traps used against the processionary moth?", ["In summer", "In late winter, when caterpillars come down", "In autumn", "Never"], "The collars catch the caterpillars coming down the trunk."),
    Q("In integrated pest management, a treatment product is used…", ["first, as prevention", "as a last resort", "every month", "only on lawns"], "Prevention, mechanical and biological control come first."),
  ])
EN["v6-l1"] = L("Maintenance calendar and differentiated management",
  ["Draw up the annual maintenance calendar", "Apply differentiated management by maintenance classes", "Make use of green waste"],
  """
<h4>Annual calendar (Tlemcen climate)</h4>
<div class="tab-wrap"><table class="tab"><thead><tr><th>Period</th><th>Main tasks</th></tr></thead><tbody>
<tr><td>November to March</td><td>Planting, pruning deciduous trees, removing processionary nests, furniture maintenance, mulching.</td></tr>
<tr><td>March to May</td><td>Mowing, hand weeding, starting and checking irrigation, spring flowers. No heavy pruning while birds nest.</td></tr>
<tr><td>June to September</td><td>Irrigation (the main task), watching young trees, litter collection, fire prevention (clearing undergrowth in wooded areas).</td></tr>
<tr><td>October</td><td>Summer review, preparing plantings, sowing meadows, collecting leaves for compost.</td></tr>
</tbody></table></div>
<h4>Differentiated management</h4>
<p>Not all spaces need the same maintenance. <b>Differentiated management</b> gives each space a <b>maintenance class</b>:</p>
<ul>
  <li><b>Class 1, horticultural</b>: prestige squares and entrances, flower beds, short-mown lawn. Intensive maintenance.</li>
  <li><b>Class 2, gardened</b>: squares and neighbourhood gardens, regular maintenance.</li>
  <li><b>Class 3, rustic</b>: large lawns mown less often, free-growing shrubs.</li>
  <li><b>Class 4, natural</b>: banks, hillsides, meadows mown once or twice a year, deadwood left for wildlife (if safe).</li>
</ul>
<p>Benefits: less water, fewer working hours, more biodiversity, and resources concentrated where they are visible and useful. It must be <b>explained to residents</b> (signs): an unmown meadow is not an abandoned space.</p>
<h4>Green waste</h4>
<p>Grass clippings, leaves and shredded branches become <b>compost</b> or <b>mulch</b>: the cycle is closed and purchases of fertiliser and mulch are reduced.</p>""",
  """<ol>
  <li>In QGIS, open <code>espaces_verts.geojson</code> and add a <code>classe_entretien</code> field (1 to 4).</li>
  <li>Give each space a class, with a justification (use, function, ecological interest).</li>
  <li>Map differentiated management with one colour per class and compute the area of each class.</li>
</ol>""")
EN["v6-l2"] = L("Tree pruning",
  ["Distinguish types of pruning and their aims", "Make a correct cut just outside the branch collar", "Reject topping and know safety rules"],
  """
<p>A well-planted tree in the right place <b>needs little pruning</b>. Pruning meets a precise aim; it is never routine.</p>
<h4>Types of pruning</h4>
<ul>
  <li><b>Formative pruning</b> (young trees): keep a single leader, remove V-shaped forks, gradually raise low branches above paths.</li>
  <li><b>Maintenance pruning</b>: remove deadwood and broken, diseased or crossing branches.</li>
  <li><b>Safety pruning</b>: remove a dangerous branch above a path or playground.</li>
  <li><b>Architectural pruning</b> (pleaching, pollarding, espaliers): only on trees trained this way from a young age, and repeated regularly.</li>
</ul>
<h4>The correct cut</h4>
<p>Cut just outside the <b>branch collar</b> (the swelling at its base), without damaging it and without leaving a <b>stub</b>. The collar contains the tissues that close the wound. For a large branch, use three cuts (undercut, top cut further out, then final cut) to avoid tearing the bark.</p>
<h4>What not to do</h4>
<ul>
  <li><b>Topping</b> (cutting all large branches): the tree reacts with weak shoots, rots through the large wounds and becomes dangerous. It is still a common bad practice.</li>
  <li>Removing more than about a quarter of the foliage at once.</li>
  <li>Using climbing spikes on a tree that is not going to be felled.</li>
</ul>
<h4>Safety</h4>
<p>Work at height is for trained, equipped staff only: helmet, goggles, gloves, chainsaw-protective trousers, harness and ropes or aerial platform. The site is marked out and traffic protected.</p>""",
  """<ol>
  <li>On photos of trees in your city, find examples of topping, stubs and correct cuts.</li>
  <li>Draw the three cuts needed to remove a large branch, showing the collar.</li>
  <li>In <code>inventaire_arbres.csv</code>, list the trees for which pruning is proposed and specify the type of pruning.</li>
</ol>""")
EN["v6-l3"] = L("Protecting plants without pesticides: integrated pest management",
  ["Recognise the pine processionary moth and its dangers", "Combine integrated pest management methods", "Organise health monitoring of the tree population"],
  """
<p><b>Integrated pest management</b> combines several methods and uses a product only as a last resort. In public places, chemical pesticides, which are dangerous for users, staff and beneficial wildlife, are avoided as far as possible.</p>
<h4>Example: the pine processionary moth</h4>
<p>The caterpillar of <i>Thaumetopoea pityocampa</i> lives in colonies in <b>white silky nests</b> at the tips of pine and cedar branches. It eats the needles and its <b>stinging hairs</b> cause serious reactions in humans and animals (eyes, skin, airways). At the end of winter, caterpillars come down in single file to bury themselves.</p>
<ul>
  <li><b>Winter</b>: nest removal, i.e. cutting and destroying nests, by equipped staff (suit, mask, goggles).</li>
  <li><b>Late winter</b>: <b>collar traps</b> around trunks that catch caterpillars on their way down.</li>
  <li><b>Summer</b>: <b>pheromone traps</b> catching male moths.</li>
  <li><b>Autumn</b>: biological treatment with <i>Bacillus thuringiensis</i> on young caterpillars if infestation is heavy.</li>
  <li><b>All year</b>: nest boxes for tits, which eat many caterpillars; diversify tree species.</li>
</ul>
<h4>Other methods</h4>
<ul>
  <li><b>Prevention</b>: right species in the right place, living soil, suitable watering: a healthy plant resists better.</li>
  <li><b>Mechanical control</b>: hand or thermal weeding, pruning affected parts.</li>
  <li><b>Biological control</b>: beneficial insects (ladybirds against aphids), nest boxes, refuge hedges.</li>
</ul>
<h4>Health monitoring</h4>
<p>Record every observation (date, place, tree, pest, intensity) in the inventory: hot spots are identified, actions evaluated and next year's campaigns planned.</p>""",
  """<ol>
  <li>In <code>inventaire_arbres.csv</code>, count the pines reported with processionary nests (field <code>defaut</code> = “Nids processionnaire”).</li>
  <li>Map them in QGIS: are they near schools and playgrounds?</li>
  <li>Write the annual integrated pest management plan for these trees, month by month.</li>
</ol>""")

# ---------------- Level 7 ----------------
EN["v7"] = dict(titre="Mapping green spaces with QGIS",
  resume="Digitise and measure green spaces, compute indicators per district, analyse accessibility and use the tree inventory and NDVI.",
  quiz=[
    Q("Which QGIS expression computes a polygon's area in the project CRS?", ["$length", "$area", "$x", "area_m()"], "$area returns the area in CRS units (m² in UTM)."),
    Q("Why is the practical data in UTM zone 30N?", ["To have distances and areas in metres", "Because QGIS only accepts UTM", "To display colours", "To reduce file size"], "A projected metric system allows direct measurement in metres."),
    Q("Which tool creates the 300 m zone around green spaces?", ["Buffer", "Union", "Raster calculator", "Georeferencer"], "A buffer draws a zone at a fixed distance around features."),
    Q("With Sentinel-2, NDVI is computed with bands…", ["B2 and B3", "B8 (NIR) and B4 (red)", "B11 and B12", "B1 and B9"], "NDVI = (B8 − B4) ÷ (B8 + B4)."),
    Q("An NDVI of 0.7 indicates…", ["water", "built-up area", "dense, vigorous vegetation", "bare soil"], "Above 0.5, vegetation is dense and active."),
  ])
EN["v7-l1"] = L("Mapping green spaces and computing areas",
  ["Open the practical layers in QGIS with the right coordinate system", "Digitise a new green space", "Compute areas and the m² per inhabitant ratio by district"],
  """
<p>QGIS is a free, open-source GIS (qgis.org, LTR version recommended). The practical layers are in <b>WGS 84 / UTM zone 30N (EPSG 32630)</b>: distances and areas are in metres. Menu names below are those of the English interface.</p>
<h4>1. Open the data</h4>
<ol>
  <li><i>Project &gt; Properties &gt; CRS</i>: choose EPSG:32630.</li>
  <li>Drag and drop <code>quartiers.geojson</code> and <code>espaces_verts.geojson</code> into QGIS.</li>
  <li>Add an OpenStreetMap basemap: <i>Browser panel &gt; XYZ Tiles &gt; OpenStreetMap</i>.</li>
</ol>
<h4>2. Digitise a green space</h4>
<p>Select the <code>espaces_verts</code> layer, click <i>Toggle Editing</i> (pencil), then <i>Add Polygon Feature</i>. Click the vertices, right-click to finish, fill in the attributes (name, category), save.</p>
<h4>3. Compute areas</h4>
<p>Open the <i>Field Calculator</i> and create a decimal field <code>surface_m2</code> with the expression:</p>
""" + K(0) + """
<h4>4. Green space per district</h4>
<p>Tool <i>Processing &gt; Toolbox &gt; Join attributes by location (summary)</i>: target layer <code>quartiers</code>, join layer <code>espaces_verts</code>, predicate “intersects”, field <code>surface_m2</code>, summary “sum”. (To be exact, first cut green spaces by districts with the <i>Intersection</i> tool.) Then, in the new layer, compute the ratio:</p>
""" + K(1) + """
<p>Display this field with <i>Symbology &gt; Graduated</i>: you get the map of deficient districts (less than 9 m²/inh.).</p>""",
  """<ol>
  <li>Carry out the lesson's steps with the practical data.</li>
  <li>Which districts are below 9 m²/inh.? How much area would have to be created in each?</li>
  <li>Make a print layout (title, legend, scale, north arrow, source “fictional ENIV data”) and export it as PDF.</li>
</ol>""")
EN["v7-l2"] = L("Analysing access to green spaces",
  ["Create a 300 m buffer around green spaces", "Estimate the share of the population within 300 m", "Propose the location of a new green space"],
  """
<p>Having enough green space is not enough: it must be <b>close</b> to residents. Under the 3-30-300 rule (level 1), everyone should live less than <b>300 m</b> from a green space.</p>
<h4>1. Buffer</h4>
<p><i>Vector &gt; Geoprocessing Tools &gt; Buffer</i>: layer <code>espaces_verts</code>, distance <b>300</b> metres, tick <i>Dissolve result</i>. You can first filter out small spaces (e.g. keep only those over 5,000 m²) with the expression:</p>
""" + K(0) + """
<h4>2. Population served</h4>
<p>The <code>batiments_habitat.geojson</code> layer contains housing points with a number of residents (field <code>habitants</code>). Use <i>Select by Location</i>: select points that “intersect” the buffer. The sum of selected residents (<i>Statistics</i> panel) divided by the total population gives the <b>share of the population served</b>.</p>
<h4>3. Gaps and proposal</h4>
<p>Invert the selection: the remaining points are residents <b>not served</b>. With a <i>Heatmap</i> (symbology) on these points, find the area where a new green space would be most useful. Then check that a vacant plot exists there (<code>terrains_libres.geojson</code> layer).</p>
<div class="astuce"><b>Going further:</b> straight-line distance overestimates access. With the <i>Service area</i> tool (network analysis) and OpenStreetMap streets, you compute the real walking distance.</div>""",
  """<ol>
  <li>Compute the share of the population within 300 m of a green space larger than 5,000 m².</li>
  <li>Map unserved residents and propose a plot for a new square.</li>
  <li>Recompute the share served with this new square: what is the gain?</li>
</ol>""")
EN["v7-l3"] = L("Mapping the tree inventory and vegetation (NDVI)",
  ["Import the tree inventory from X/Y coordinates", "Symbolise trees by health and species", "Compute and interpret NDVI from Sentinel-2 imagery"],
  """
<h4>1. Import the inventory</h4>
<p><i>Layer &gt; Add Layer &gt; Add Delimited Text Layer</i>: file <code>inventaire_arbres.csv</code>, comma separator, geometry “point”, X field = <code>x</code>, Y field = <code>y</code>, CRS = EPSG:32630. Then export the layer to GeoPackage so that you can edit it.</p>
<h4>2. Symbology and labels</h4>
<ul>
  <li><i>Categorized</i> on <code>etat</code>: green (Bon = good), yellow (Moyen = fair), orange (Mauvais = poor), red (Mort = dead).</li>
  <li>Size proportional to crown diameter: in the symbol size, use an expression such as:</li>
</ul>
""" + K(0) + """
<p>(Unit: <b>map units / metres at scale</b>, so the circle has the real size of the crown.)</p>
<h4>3. NDVI</h4>
<p><b>NDVI</b> (Normalized Difference Vegetation Index) measures vegetation vigour from satellite images: vegetation strongly reflects near infrared (NIR) and absorbs red (R).</p>
<p class="formule">NDVI = (NIR − R) ÷ (NIR + R) &nbsp; ; &nbsp; Sentinel-2: NIR = band B8, R = band B4 (10 m)</p>
<p>Values: close to 0 or negative for buildings, water and bare soil; 0.2 to 0.4 for sparse or dry vegetation; above 0.5 for dense, vigorous vegetation.</p>
<p>Download bands B4 and B8 of a Sentinel-2 image over Tlemcen free of charge from the <b>Copernicus Browser</b> (free registration), then <i>Raster &gt; Raster Calculator</i>:</p>
""" + K(1) + """
<p>Compare a May image and an August image: unirrigated lawns and meadows dry out, trees stay green.</p>""",
  """<ol>
  <li>Import the inventory and map tree health with circles at the real crown size.</li>
  <li>Compute the canopy cover of each green space: sum of crown areas ÷ area of the space (hint: <i>Join attributes by location (summary)</i>).</li>
  <li>With a real Sentinel-2 image, compute the NDVI of Tlemcen and compare districts.</li>
</ol>""")

# ---------------- Level 8 ----------------
EN["v8"] = dict(titre="Project, budget and participation",
  resume="Cost a project (quantities and estimate), write a management plan, involve residents and evaluate results.",
  quiz=[
    Q("What does the bill of quantities of a project contain?", ["Unit prices", "Quantities measured on the plan", "The maintenance schedule", "The list of users"], "The bill of quantities measures quantities; costing multiplies them by unit prices."),
    Q("30 trees at 9,000 DA each cost…", ["27,000 DA", "270,000 DA", "2,700,000 DA", "39,000 DA"], "30 × 9,000 = 270,000 DA."),
    Q("Why present maintenance costs with the construction estimate?", ["Because a green space costs mostly after it is built", "It is not useful", "To inflate the budget", "Because the law forbids maintenance"], "Water, labour and replacements weigh every year."),
    Q("Which is a monitoring indicator of a management plan?", ["The colour of the benches", "Canopy cover", "The architect's name", "The brand of mowers"], "Canopy cover measures change in tree cover."),
    Q("What is a main benefit of resident participation?", ["A space that is better used and better respected", "Removing maintenance", "Skipping the assessment", "Reducing the number of trees"], "Residents who took part take ownership of the space."),
  ])
EN["v8-l1"] = L("Bill of quantities and cost estimate",
  ["Draw up the bill of quantities of a project", "Build a cost estimate with unit prices", "Estimate the annual maintenance cost"],
  """
<p>The <b>cost estimate</b> gives the forecast cost of the project. It is built in two steps: the <b>bill of quantities</b> (measured on the master plan) then the <b>costing</b> (quantity × unit price).</p>
<h4>Structure of an estimate</h4>
<div class="tab-wrap"><table class="tab"><thead><tr><th>No.</th><th>Item</th><th>Unit</th><th>Quantity</th><th>Unit price (DA)</th><th>Amount (DA)</th></tr></thead><tbody>
<tr><td>1</td><td>Earthworks and topsoil supply</td><td>m³</td><td>300</td><td>2,500</td><td>750,000</td></tr>
<tr><td>2</td><td>Supply and planting of trees (girth 12-14 cm)</td><td>u</td><td>30</td><td>9,000</td><td>270,000</td></tr>
<tr><td>3</td><td>Supply and planting of shrubs</td><td>u</td><td>400</td><td>600</td><td>240,000</td></tr>
<tr><td>4</td><td>Drip network</td><td>lm</td><td>900</td><td>350</td><td>315,000</td></tr>
<tr><td>5</td><td>Benches</td><td>u</td><td>20</td><td>35,000</td><td>700,000</td></tr>
<tr><td colspan="5"><b>Total excluding tax</b></td><td><b>2,275,000</b></td></tr>
</tbody></table></div>
<p><b>Note:</b> these prices are <b>fictional</b>, for the exercise. In real situations, use prices from the municipality's recent contracts or from contractor quotes. Then add VAT and a contingency margin (often 5 to 10%).</p>
<h4>Management cost</h4>
<p>A green space costs mostly <b>after</b> it is built: water, labour, replacements, repairs. Estimate it per m² by maintenance class (level 6) and present it with the estimate, so the client knows whether they can afford to maintain it.</p>
<div class="astuce"><b>Spreadsheet:</b> the workbook <code>devis_estimatif.xlsx</code> contains the formulas (Amount = Quantity × UP, subtotals, VAT, contingencies). Change the quantities and everything recalculates.</div>""",
  """<ol>
  <li>From your master plan (level 4) and furniture list, draw up the bill of quantities.</li>
  <li>Fill in <code>devis_estimatif.xlsx</code> with your quantities. What is the total cost including tax with 10% contingency?</li>
  <li>Estimate the project's annual water cost with your level 5 calculations (fictional water price: 40 DA/m³).</li>
</ol>""")
EN["v8-l2"] = L("The management plan of a green space",
  ["Know the content of a management plan", "Write management sheets for each space", "Choose monitoring indicators"],
  """
<p>The <b>management plan</b> organises the maintenance of a green space (or all those of a municipality) over several years. It is the roadmap for teams and the basis for contractors' specifications.</p>
<h4>Typical content</h4>
<ol>
  <li><b>Assessment</b>: inventory, health, uses, problems (levels 1 to 3).</li>
  <li><b>Objectives</b>: e.g. “raise canopy cover from 20% to 25% in 10 years”, “cut water use by 30%”, “zero pesticides”.</li>
  <li><b>Maintenance classes</b> and differentiated-management map (level 6).</li>
  <li><b>Management sheets</b>: for each space, operations, frequency, period and resources (staff, equipment).</li>
  <li><b>Multi-year programme</b>: planting, replacements, renovations, with a yearly budget.</li>
  <li><b>Monitoring indicators</b>: trees planted and dead, canopy cover, m³ of water used, m²/inh., user satisfaction.</li>
</ol>
<h4>Example management sheet</h4>
<div class="tab-wrap"><table class="tab"><thead><tr><th>Operation</th><th>Frequency</th><th>Period</th></tr></thead><tbody>
<tr><td>Mowing the central lawn</td><td>Twice a month</td><td>March to June, October</td></tr>
<tr><td>Cutting the meadow</td><td>Twice a year</td><td>June and October</td></tr>
<tr><td>Checking irrigation</td><td>Every week</td><td>May to September</td></tr>
<tr><td>Tree health inspection</td><td>Once a year</td><td>Winter</td></tr>
<tr><td>Playground inspection</td><td>Visual every week, in-depth every year</td><td>All year</td></tr>
</tbody></table></div>""",
  """<ol>
  <li>Write the management plan (4 pages maximum) of your project's square with the lesson's structure.</li>
  <li>Fill in a management sheet for each zone (lawn, beds, trees, play).</li>
  <li>Choose 5 indicators and their target value in 5 years.</li>
</ol>""")
EN["v8-l3"] = L("Involving residents and evaluating the project",
  ["Organise resident participation", "Prepare and analyse a user survey", "Present a project clearly"],
  """
<p>A green space designed <b>with</b> residents is better respected and better used. Participation can take place at every stage.</p>
<h4>Forms of participation</h4>
<ul>
  <li><b>Before the project</b>: questionnaire, neighbourhood meeting, assessment walk with residents, workshops with children from the nearby school.</li>
  <li><b>During</b>: presentation of sketches, choice between two options, community planting day.</li>
  <li><b>After</b>: community gardens, tree sponsorship by families or classes, user committees, reporting problems.</li>
</ul>
<h4>The user survey</h4>
<p>Short questions, closed if possible: frequency of visits, access time, activities, satisfaction (1 to 5) with shade, cleanliness, safety, play, and one open question “what should be improved?”. The file <code>enquete_usagers.csv</code> contains 120 fictional answers to analyse.</p>
<h4>Presenting the project</h4>
<p>For a jury or a municipal council: a poster or slide show with the assessment (maps), the master plan, two or three mood views, the plant palette, the estimate and the management plan. A clear message: “what the project brings to the district”.</p>
<div class="astuce"><b>Key point:</b> evaluation closes the loop. Indicators (canopy, m²/inh., water, satisfaction) measured before and after show whether objectives are met and feed the next project.</div>""",
  """<ol>
  <li>Analyse <code>enquete_usagers.csv</code> in a spreadsheet: average score per criterion, share of users coming on foot, three most requested improvements.</li>
  <li>Propose three participation actions for your square project.</li>
  <li>Final project: present your square (assessment, master plan, palette, irrigation, estimate, management plan) in 10 slides.</li>
</ol>""")
