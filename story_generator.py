import random

TOPICS = [
    "friendly dinosaurs",
    "space adventure",
    "ocean animals",
    "magical forest",
    "cute robots",
    "farm animals",
    "jungle safari",
    "butterfly garden",
    "snow adventure",
    "underwater world",
    "dragon friends",
    "silly monsters",
    "famous vehicles",
    "world travel adventure",
    "funny animal moments",
    "life hacks for kids",
    "dance party animals",
    "nature and plants",
    "sports day fun",
    "art class rainbow",
    "music band animals",
    "food around the world",
    "building a treehouse",
    "world cultures celebration",
]

# Story templates per topic
_STORIES = {
    "friendly dinosaurs": {
        "title": "Dino and the Rainbow Egg",
        "scenes": [
            {"scene_number": 1, "title_text": "A Sunny Morning", "narration": "Dino the little dinosaur woke up and found a shiny rainbow egg near his home!", "image_prompt": "children's book illustration, cute friendly baby dinosaur waking up near a colorful rainbow egg in a lush green prehistoric jungle, bright sunny day, cartoon style, digital art"},
            {"scene_number": 2, "title_text": "Who Does It Belong To?", "narration": "Dino asked his friends if the egg belonged to them, but nobody knew whose egg it was.", "image_prompt": "children's book illustration, group of cute friendly cartoon dinosaurs of different colors gathered around a glowing rainbow egg, bright colors, curious expressions, digital art"},
            {"scene_number": 3, "title_text": "Keeping It Warm", "narration": "Kind-hearted Dino decided to sit by the egg and keep it warm until its mama came.", "image_prompt": "children's book illustration, small cute dinosaur sitting beside a big colorful egg, warm golden sunlight, cozy prehistoric setting, caring expression, digital art"},
            {"scene_number": 4, "title_text": "Crack! Crack! Crack!", "narration": "The egg began to wiggle and crack — and out popped the tiniest, cutest baby dragon!", "image_prompt": "children's book illustration, adorable tiny baby dragon hatching from a rainbow egg, sparkles and stars around, excited dinosaur watching, bright joyful colors, digital art"},
            {"scene_number": 5, "title_text": "New Best Friends!", "narration": "The baby dragon smiled at Dino, and from that day on they were the very best of friends!", "image_prompt": "children's book illustration, cute dinosaur and tiny baby dragon hugging, colorful flowers and rainbow in background, happy cheerful scene, digital art"},
        ],
    },
    "space adventure": {
        "title": "Ziggy's Trip to the Stars",
        "scenes": [
            {"scene_number": 1, "title_text": "Blast Off!", "narration": "Ziggy the astronaut jumped into her little rocket and blasted off into the sparkling night sky!", "image_prompt": "children's book illustration, cute little girl astronaut in colorful spacesuit launching in a tiny rocket ship, bright stars and colorful planets, cartoon style, digital art"},
            {"scene_number": 2, "title_text": "Hello, Moon!", "narration": "Ziggy landed on the Moon and bounced around, because everything is so bouncy up there!", "image_prompt": "children's book illustration, adorable child astronaut bouncing happily on the Moon surface, Earth visible in background, stars everywhere, bright fun colors, digital art"},
            {"scene_number": 3, "title_text": "Alien Friends", "narration": "Three funny little aliens with green skin and big eyes waved hello and invited Ziggy to play!", "image_prompt": "children's book illustration, three cute friendly cartoon aliens waving at a child astronaut, colorful alien planet with purple sky and two moons, digital art"},
            {"scene_number": 4, "title_text": "Dancing in Space", "narration": "They all floated and danced together among the stars, laughing and spinning around!", "image_prompt": "children's book illustration, child astronaut and cute aliens floating and dancing together in space, colorful stars and galaxies, joyful expressions, digital art"},
            {"scene_number": 5, "title_text": "Safe Back Home", "narration": "Ziggy waved goodbye and zoomed home, full of wonderful stories to tell!", "image_prompt": "children's book illustration, cute child astronaut in rocket waving goodbye to alien friends, Earth getting closer, sunset colors in space, happy warm scene, digital art"},
        ],
    },
    "ocean animals": {
        "title": "Finn's Big Ocean Day",
        "scenes": [
            {"scene_number": 1, "title_text": "Good Morning Ocean!", "narration": "Little Finn the fish swam out of his coral home and said good morning to the whole ocean!", "image_prompt": "children's book illustration, cute small fish swimming out of a colorful coral reef home, surrounded by colorful sea creatures, bright underwater scene, digital art"},
            {"scene_number": 2, "title_text": "Meeting the Jellyfish", "narration": "Finn found a group of glowing pink jellyfish doing a wiggly underwater dance!", "image_prompt": "children's book illustration, cute fish watching happy glowing jellyfish dancing underwater, soft pink and blue lights, magical underwater atmosphere, digital art"},
            {"scene_number": 3, "title_text": "A Big Whale Hello", "narration": "A huge friendly whale swooped by, smiled, and gently blew bubbles all around Finn!", "image_prompt": "children's book illustration, giant friendly blue whale smiling at a tiny fish, huge stream of bubbles, deep blue ocean, warm cheerful scene, digital art"},
            {"scene_number": 4, "title_text": "The Treasure Chest", "narration": "Finn discovered an old treasure chest filled with shiny colourful sea shells — what a find!", "image_prompt": "children's book illustration, cute fish opening a treasure chest full of glowing shells and gems on the ocean floor, bright colors, excited expression, digital art"},
            {"scene_number": 5, "title_text": "Home for Dinner", "narration": "As the sun went down, Finn swam back home happy, ready to share his wonderful adventures!", "image_prompt": "children's book illustration, small fish swimming back to colorful coral reef home as warm sunlight filters through the water, peaceful happy underwater scene, digital art"},
        ],
    },
    "magical forest": {
        "title": "Lily and the Talking Trees",
        "scenes": [
            {"scene_number": 1, "title_text": "Into the Forest", "narration": "Little Lily skipped into the magical forest where flowers sparkled and fireflies danced!", "image_prompt": "children's book illustration, cute small girl with pigtails entering a magical glowing forest, sparkling flowers, friendly fireflies, fairy tale setting, digital art"},
            {"scene_number": 2, "title_text": "A Tree That Talks!", "narration": "A big friendly oak tree blinked its eyes and said 'Hello there, little one!' and Lily giggled.", "image_prompt": "children's book illustration, giant friendly talking tree with a warm smiling face, surprised and delighted little girl looking up, magical forest, digital art"},
            {"scene_number": 3, "title_text": "Fairy Friends", "narration": "Tiny fairies with butterfly wings flew down and sprinkled glittery pink dust all around Lily.", "image_prompt": "children's book illustration, tiny colourful fairies with butterfly wings sprinkling glitter on a happy child, magical forest clearing, dreamy soft colours, digital art"},
            {"scene_number": 4, "title_text": "The Magic Pond", "narration": "They showed Lily a shimmering magic pond where she could see rainbows dancing in the water!", "image_prompt": "children's book illustration, child and fairies looking at a glowing rainbow pond in a magical forest, colourful reflections, peaceful magical scene, digital art"},
            {"scene_number": 5, "title_text": "Promise to Return", "narration": "Lily promised her new forest friends she would come back to play, and she skipped home with a big smile!", "image_prompt": "children's book illustration, happy girl waving goodbye to fairies and friendly trees, golden light, warm magical forest farewell scene, digital art"},
        ],
    },
    "cute robots": {
        "title": "Bolt's Big Day Out",
        "scenes": [
            {"scene_number": 1, "title_text": "Bolt Wakes Up!", "narration": "Bolt the little robot opened his big bright eyes and beeped happily — today was going to be a great day!", "image_prompt": "children's book illustration, adorable round little robot with big glowing eyes waking up in a colourful robot bedroom, cheerful morning, digital art"},
            {"scene_number": 2, "title_text": "Making Breakfast", "narration": "Bolt whirred and buzzed as he made towers of pancakes with his tiny robot arms — yum!", "image_prompt": "children's book illustration, cute small robot with tiny arms carefully stacking a tall tower of fluffy pancakes, kitchen setting, bright cheerful colours, digital art"},
            {"scene_number": 3, "title_text": "Playing in the Park", "narration": "At the park, Bolt chased butterflies and spun around until he got dizzy and fell over giggling!", "image_prompt": "children's book illustration, small cute robot happily chasing colourful butterflies in a sunny park, spinning and laughing, flowers everywhere, digital art"},
            {"scene_number": 4, "title_text": "Helping a Friend", "narration": "Bolt noticed a puppy stuck in a bush and carefully helped it get free with his little robot hands!", "image_prompt": "children's book illustration, sweet little robot gently helping a small fluffy puppy out of a bush, kind caring expression, bright sunny park, digital art"},
            {"scene_number": 5, "title_text": "Stars and Sleeptime", "narration": "At night, Bolt looked up at the stars and beeped softly — it had been the best day ever!", "image_prompt": "children's book illustration, tiny cute robot sitting on a hill gazing at a sky full of stars, peaceful night, soft glowing lights, dreamy cozy scene, digital art"},
        ],
    },
    "farm animals": {
        "title": "A Day on Sunny Farm",
        "scenes": [
            {"scene_number": 1, "title_text": "Rise and Shine!", "narration": "The rooster crowed and all the animals on Sunny Farm woke up for a brand new day!", "image_prompt": "children's book illustration, colourful rooster crowing on a fence post at sunrise, cute farm animals peeking out of their pens, bright warm morning, digital art"},
            {"scene_number": 2, "title_text": "Muddy Fun", "narration": "The little pink pigs ran outside and splashed into the biggest, muddiest puddle with a huge SPLASH!", "image_prompt": "children's book illustration, three cheerful piglets jumping into a big muddy puddle, mud splashing everywhere, sunny farm background, joyful expressions, digital art"},
            {"scene_number": 3, "title_text": "The Woolly Sheep", "narration": "The fluffy sheep tried to count clouds but kept losing track and starting all over again!", "image_prompt": "children's book illustration, adorable fluffy white sheep lying in grass staring up at puffy clouds, counting on tiny hooves, cute confused expression, sunny farm, digital art"},
            {"scene_number": 4, "title_text": "Lunch Together", "narration": "All the animals gathered under the big apple tree to share a yummy lunch together!", "image_prompt": "children's book illustration, all cute farm animals gathered under a big apple tree sharing food, cow, sheep, pig, chicken together, friendly warm picnic scene, digital art"},
            {"scene_number": 5, "title_text": "Goodnight Farm!", "narration": "As the sun set orange and pink, all the animals snuggled up and drifted off to sleep.", "image_prompt": "children's book illustration, cute farm animals snuggled up in a cosy barn, warm golden sunset outside the barn door, stars beginning to appear, peaceful happy scene, digital art"},
        ],
    },
    "jungle safari": {
        "title": "Maya's Jungle Journey",
        "scenes": [
            {"scene_number": 1, "title_text": "Into the Jungle!", "narration": "Maya put on her safari hat and walked bravely into the big green jungle — adventure awaited!", "image_prompt": "children's book illustration, brave little girl in safari hat and backpack stepping into a lush bright jungle, colourful birds and flowers, digital art"},
            {"scene_number": 2, "title_text": "Hello, Monkey!", "narration": "A cheeky little monkey swung down from a tree and stole Maya's hat, then gave it back with a grin!", "image_prompt": "children's book illustration, funny cartoon monkey wearing a safari hat on its head and grinning at a laughing little girl below, bright jungle trees, digital art"},
            {"scene_number": 3, "title_text": "The Elephant Parade", "narration": "Three big elephants marched past, and the smallest one blew a tiny honk right at Maya!", "image_prompt": "children's book illustration, three friendly elephants walking in a line through the jungle, smallest elephant trumpeting at a giggling child, bright colorful scene, digital art"},
            {"scene_number": 4, "title_text": "Colourful Parrots", "narration": "A rainbow of parrots landed on Maya's arms and sang the silliest song she had ever heard!", "image_prompt": "children's book illustration, brightly coloured parrots of all colours perched on a delighted child's arms and shoulders, jungle clearing, rainbow feathers everywhere, digital art"},
            {"scene_number": 5, "title_text": "Journey Home", "narration": "Maya waved goodbye to her jungle friends and skipped home, already dreaming of her next adventure!", "image_prompt": "children's book illustration, happy girl waving to jungle animals including monkey, elephants and parrots, golden afternoon light through jungle trees, warm farewell scene, digital art"},
        ],
    },
    "butterfly garden": {
        "title": "Bella the Butterfly's Big Day",
        "scenes": [
            {"scene_number": 1, "title_text": "From Cocoon to Wings", "narration": "Bella pushed out of her cosy cocoon and spread her brand new bright yellow wings for the very first time!", "image_prompt": "children's book illustration, beautiful butterfly emerging from a cocoon on a branch, spreading bright colourful wings, garden flowers and sunlight, magical moment, digital art"},
            {"scene_number": 2, "title_text": "First Flight!", "narration": "Bella took a deep breath and flew for the first time — up, up and over the flowers she soared!", "image_prompt": "children's book illustration, cute butterfly flying for first time above a field of colourful flowers, joyful expression, sunshine and blue sky, digital art"},
            {"scene_number": 3, "title_text": "Flower Friends", "narration": "Every flower she landed on smiled and shared a little sweet nectar — what a delicious treat!", "image_prompt": "children's book illustration, colourful butterfly landing on a smiling flower, other flowers watching happily, bright vibrant garden, cheerful and whimsical, digital art"},
            {"scene_number": 4, "title_text": "Butterfly Dance", "narration": "Bella and her butterfly friends danced together in circles, making rainbow patterns in the sky!", "image_prompt": "children's book illustration, group of colourful butterflies dancing in circular patterns in the sky, rainbow trail behind them, garden below, magical joyful scene, digital art"},
            {"scene_number": 5, "title_text": "Resting at Sunset", "narration": "As the sun went to sleep, Bella folded her wings and hummed a happy little butterfly song.", "image_prompt": "children's book illustration, beautiful butterfly resting on a flower petal at sunset, warm orange and pink sky, peaceful garden, soft glowing colours, digital art"},
        ],
    },
    "snow adventure": {
        "title": "Ollie's Snowday Magic",
        "scenes": [
            {"scene_number": 1, "title_text": "It Snowed!", "narration": "Ollie woke up and saw fluffy white snow covering everything — it was a perfect snowday!", "image_prompt": "children's book illustration, excited child at window seeing heavy snowfall, cosy house, everything covered in sparkly white snow, warm winter morning, digital art"},
            {"scene_number": 2, "title_text": "Building a Snowman", "narration": "Ollie rolled three big snowballs and built the funniest, most lopsided snowman you ever saw!", "image_prompt": "children's book illustration, happy child building a silly lopsided snowman with a wonky carrot nose, snowy garden, colourful scarf and hat, bright winter day, digital art"},
            {"scene_number": 3, "title_text": "Sledding Down!", "narration": "Ollie climbed to the top of the big hill and whooshed down on his red sled — wheee!", "image_prompt": "children's book illustration, joyful child on a bright red sled speeding down a snowy hill, snowy trees, big smile and arms out, winter fun scene, digital art"},
            {"scene_number": 4, "title_text": "Snowball Fight!", "narration": "Ollie and his friends had the biggest snowball fight ever, laughing and ducking in the snow!", "image_prompt": "children's book illustration, group of children having a fun snowball fight, snow flying everywhere, big laughing smiles, colourful winter coats and scarves, digital art"},
            {"scene_number": 5, "title_text": "Hot Cocoa Time", "narration": "Back inside, Ollie wrapped up in a warm blanket and sipped a big mug of yummy hot cocoa.", "image_prompt": "children's book illustration, cosy child wrapped in a warm blanket by a fireplace holding a big mug of hot cocoa with marshmallows, snowy window outside, warm and peaceful, digital art"},
        ],
    },
    "underwater world": {
        "title": "Pearl's Ocean Discovery",
        "scenes": [
            {"scene_number": 1, "title_text": "Diving Deep!", "narration": "Pearl the little mermaid dived under the waves and found a whole new underwater world to explore!", "image_prompt": "children's book illustration, cute little mermaid with colourful tail diving into bright blue ocean, coral reefs and colourful fish below, magical underwater entrance, digital art"},
            {"scene_number": 2, "title_text": "The Coral Castle", "narration": "She discovered a beautiful castle made entirely of pink and orange coral with starfish for windows!", "image_prompt": "children's book illustration, beautiful underwater castle made of pink coral and starfish, glowing windows, little mermaid looking amazed, ocean floor, digital art"},
            {"scene_number": 3, "title_text": "Seahorse Race!", "narration": "Pearl joined in a seahorse race and came second — she got a shiny pearl necklace as a prize!", "image_prompt": "children's book illustration, cute mermaid riding a seahorse in an underwater race, colourful seahorses, cheering sea creatures, bright underwater setting, digital art"},
            {"scene_number": 4, "title_text": "The Singing Clams", "narration": "Pearl found a choir of clams singing beautiful songs — she joined in and they all sang together!", "image_prompt": "children's book illustration, group of happy clams with mouths open singing, little mermaid singing along, musical notes floating through water, joyful underwater scene, digital art"},
            {"scene_number": 5, "title_text": "Swimming Home", "narration": "As the ocean turned golden, Pearl waved to all her friends and swam back home, heart full of joy!", "image_prompt": "children's book illustration, happy little mermaid swimming upward toward golden sunlit surface, waving to sea creatures below, warm glowing underwater scene, digital art"},
        ],
    },
    "dragon friends": {
        "title": "Sparky's First Flame",
        "scenes": [
            {"scene_number": 1, "title_text": "Little Sparky", "narration": "Sparky was the smallest dragon in the whole mountain, and he really really wanted to breathe fire!", "image_prompt": "children's book illustration, tiny adorable baby dragon with big eyes sitting on a mountain, looking up at bigger dragons blowing fire, hopeful expression, bright sky, digital art"},
            {"scene_number": 2, "title_text": "Trying and Trying", "narration": "Sparky huffed and puffed and tried to breathe fire, but only tiny smoke rings came out — puff puff puff!", "image_prompt": "children's book illustration, cute tiny dragon puffing hard making small smoke rings instead of fire, trying very hard, funny determined expression, mountain setting, digital art"},
            {"scene_number": 3, "title_text": "Kind Advice", "narration": "Old wise dragon Ember told Sparky: take a deep breath, close your eyes, and believe in yourself!", "image_prompt": "children's book illustration, old friendly dragon kindly speaking to a small young dragon, wise warm expression, mountain cave setting, magical golden light, digital art"},
            {"scene_number": 4, "title_text": "The Big Moment!", "narration": "Sparky took the biggest breath of his whole life — and out shot the most beautiful rainbow flame!", "image_prompt": "children's book illustration, tiny dragon breathing out a beautiful rainbow coloured flame for first time, surprised and delighted expression, all the other dragons cheering, digital art"},
            {"scene_number": 5, "title_text": "Sparky the Brave!", "narration": "All the dragons cheered for Sparky — and from that day on he shared his special rainbow fire with everyone!", "image_prompt": "children's book illustration, small dragon breathing rainbow fire while surrounded by cheering happy dragons of all sizes, celebration scene, colourful fireworks and confetti, digital art"},
        ],
    },
    "silly monsters": {
        "title": "The Monster Dance Party",
        "scenes": [
            {"scene_number": 1, "title_text": "Monsters Are Nice!", "narration": "The monsters under the bed were not scary at all — they were just very very silly and loved to dance!", "image_prompt": "children's book illustration, cute funny colourful monsters under a bed waving hello, big goofy smiles, funny shapes and silly faces, bright bedroom, digital art"},
            {"scene_number": 2, "title_text": "The Invitation", "narration": "Wobbly the three-eyed monster sent out sparkly invitations for the biggest monster dance party ever!", "image_prompt": "children's book illustration, cute three-eyed monster handing out sparkly invitations to other funny monsters, excited expressions, colourful party decorations, digital art"},
            {"scene_number": 3, "title_text": "Everyone Arrives!", "narration": "Monsters of all shapes, colours and sizes arrived — some had ten legs, some had no legs at all!", "image_prompt": "children's book illustration, wildly varied and funny cute monsters arriving at a party, some with many legs, some floating, some tiny, some huge, all colourful, digital art"},
            {"scene_number": 4, "title_text": "The Silly Dance!", "narration": "They danced the silliest dances ever — the wobbly wiggle, the tentacle twist, and the one-eyed bounce!", "image_prompt": "children's book illustration, colourful funny monsters dancing wildly in silly poses, disco lights, big happy expressions, confetti everywhere, joyful party scene, digital art"},
            {"scene_number": 5, "title_text": "Best Friends Forever!", "narration": "The little child peeked and saw the fun — and the monsters invited them to join the party too!", "image_prompt": "children's book illustration, happy child joining a group of friendly silly monsters dancing together, everyone laughing, colourful party decorations, warm and joyful scene, digital art"},
        ],
    },
    "famous vehicles": {
        "title": "The World's Most Famous Vehicles!",
        "scenes": [
            {
                "scene_number": 1,
                "title_text": "Ferrari — The Red Rocket!",
                "narration": "The Ferrari is a super-fast red race car from Italy! It zooms so fast it looks like a rocket on wheels!",
                "image_prompt": "children's book illustration, shiny bright red Ferrari sports car racing down a road with speed lines, Italian flag and checkered race flags, big cartoon wheels, cheerful sunny day, colourful digital art for kids",
            },
            {
                "scene_number": 2,
                "title_text": "Lamborghini — The Bull Car!",
                "narration": "The Lamborghini is a bright yellow supercar shaped like a lightning bolt! Its doors open upward like wings — how cool is that!",
                "image_prompt": "children's book illustration, bright yellow Lamborghini supercar with scissor doors opening upward like wings, lightning bolt design, excited cartoon children watching, city road, vibrant colourful digital art for kids",
            },
            {
                "scene_number": 3,
                "title_text": "Monster Truck — Mighty Wheels!",
                "narration": "A Monster Truck has the biggest wheels you have ever seen! It can crush other cars and jump really really high!",
                "image_prompt": "children's book illustration, giant colourful monster truck with enormous wheels jumping over a row of small cars, crowd of cheering cartoon children, stadium setting, action-packed bright digital art for kids",
            },
            {
                "scene_number": 4,
                "title_text": "Formula 1 — Speed Champion!",
                "narration": "A Formula 1 racing car is the fastest car in the whole world! Drivers wear special helmets and go faster than an aeroplane!",
                "image_prompt": "children's book illustration, colourful Formula 1 race car speeding around a race track, motion blur behind it, waving flags, cartoon racing driver waving, exciting race atmosphere, bright digital art for kids",
            },
            {
                "scene_number": 5,
                "title_text": "Fire Truck — Hero on Wheels!",
                "narration": "The big red Fire Truck is the hero of the road! It has long ladders, a loud siren, and brave firefighters ready to help!",
                "image_prompt": "children's book illustration, big shiny red fire truck with extended ladder, friendly cartoon firefighters waving, bright flashing lights, children waving from the pavement, cheerful heroic scene, digital art for kids",
            },
        ],
    },
    "world travel adventure": {
        "title": "Around the World in One Day!",
        "scenes": [
            {"scene_number": 1, "title_text": "Packing Our Bags!", "narration": "Mia and her family packed their bags and jumped on a big aeroplane to visit amazing places around the world!", "image_prompt": "children's book illustration, excited family with colourful suitcases boarding a big cheerful aeroplane, airport setting, bright colours, cartoon style, digital art for kids"},
            {"scene_number": 2, "title_text": "Hello, Paris!", "narration": "First stop — Paris, France! They saw the tall sparkly Eiffel Tower and ate the yummiest croissants ever!", "image_prompt": "children's book illustration, happy cartoon children in front of the Eiffel Tower, eating croissants, Paris street with flower stalls, bright cheerful colours, digital art for kids"},
            {"scene_number": 3, "title_text": "Wild Safari!", "narration": "Next they went to Africa for a safari and saw giraffes, elephants, and a cheeky little lion cub!", "image_prompt": "children's book illustration, excited children in safari jeep watching cute cartoon giraffes and elephants on the African savannah, golden sunshine, digital art for kids"},
            {"scene_number": 4, "title_text": "Great Wall of China!", "narration": "Then they climbed the Great Wall of China — it was so long it went all the way to the clouds!", "image_prompt": "children's book illustration, smiling children walking along the Great Wall of China stretching into puffy clouds, colourful kites in the sky, bright digital art for kids"},
            {"scene_number": 5, "title_text": "Home Sweet Home!", "narration": "After the most amazing adventure ever, the family flew back home full of wonderful memories and new friends!", "image_prompt": "children's book illustration, happy family arriving home with souvenirs, world map on the wall with pins, warm cosy home, big smiles, digital art for kids"},
        ],
    },
    "funny animal moments": {
        "title": "When Animals Do Silly Things!",
        "scenes": [
            {"scene_number": 1, "title_text": "The Clumsy Giraffe", "narration": "Gerald the giraffe tried to drink water and his long neck got all tangled up — what a silly giraffe!", "image_prompt": "children's book illustration, cartoon giraffe with its long neck comically tangled trying to drink from a pond, surprised expression, other animals laughing kindly, bright savannah, digital art for kids"},
            {"scene_number": 2, "title_text": "Penguin Slip!", "narration": "Percy the penguin tried to dance on the ice but slipped and slid all the way across the frozen lake!", "image_prompt": "children's book illustration, funny cartoon penguin sliding across ice on its tummy with a big grin, other penguins clapping and cheering, snowy Arctic scene, bright digital art for kids"},
            {"scene_number": 3, "title_text": "Monkey Mix-Up!", "narration": "Momo the monkey grabbed a bunch of bananas but tripped and juggled them all by accident — what talent!", "image_prompt": "children's book illustration, surprised cartoon monkey accidentally juggling bananas, other jungle animals amazed and laughing, colourful jungle setting, digital art for kids"},
            {"scene_number": 4, "title_text": "Elephant's Big Sneeze!", "narration": "Ellie the elephant sniffed a flower and let out the biggest sneeze ever — it blew everyone's hats off!", "image_prompt": "children's book illustration, elephant sneezing enormously near flowers, hats flying off cartoon animals all around, everybody laughing together, sunny safari park, digital art for kids"},
            {"scene_number": 5, "title_text": "Best Silly Friends!", "narration": "All the animals laughed together because being silly with your friends is the best thing in the whole world!", "image_prompt": "children's book illustration, group of happy cartoon animals laughing together, giraffe, penguin, monkey and elephant side by side, sunny cheerful scene, digital art for kids"},
        ],
    },
    "life hacks for kids": {
        "title": "Super Smart Kids Tricks!",
        "scenes": [
            {"scene_number": 1, "title_text": "Tidy Room in 1 Minute!", "narration": "Tommy learned a super trick — put a big box in the middle of your room and toss everything in! Tidy in one minute!", "image_prompt": "children's book illustration, happy child tossing toys into a big colourful box, messy room becoming tidy, funny action pose, bright bedroom, digital art for kids"},
            {"scene_number": 2, "title_text": "Never Lose Your Socks!", "narration": "Clip your socks together before putting them in the wash and they will always come out as a pair — like magic!", "image_prompt": "children's book illustration, clever child clipping colourful socks together with a clothes peg, socks looking happy together, laundry basket, bright cheerful illustration, digital art for kids"},
            {"scene_number": 3, "title_text": "Homework Superpower!", "narration": "Do the hardest homework first — then the easy stuff feels like a party! Your brain will thank you!", "image_prompt": "children's book illustration, determined child doing homework at a desk, big book shrinking smaller as child works through it, star and sparkle effects, bright study room, digital art for kids"},
            {"scene_number": 4, "title_text": "Morning Ready Fast!", "narration": "Pack your school bag the night before! Morning-you will think night-you was a total genius!", "image_prompt": "children's book illustration, child happily packing school bag the evening before, next morning child sleeping peacefully while packed bag waits by the door, split panel, bright digital art for kids"},
            {"scene_number": 5, "title_text": "You Are Super Smart!", "narration": "With these clever tricks you can be the smartest, most organised kid in the whole wide world!", "image_prompt": "children's book illustration, confident smiling child wearing a superhero cape with a star on it, surrounded by school items, trophies and gold stars, colourful empowering scene, digital art for kids"},
        ],
    },
    "dance party animals": {
        "title": "The Animal Dance-Off!",
        "scenes": [
            {"scene_number": 1, "title_text": "The Party Begins!", "narration": "All the jungle animals got an invitation to the biggest dance party in the whole forest — tonight!", "image_prompt": "children's book illustration, excited cartoon animals reading sparkly party invitations, jungle setting decorated with colourful lights and balloons, festive and fun, digital art for kids"},
            {"scene_number": 2, "title_text": "Lion's Cool Moves!", "narration": "Leo the lion showed off his best moonwalk move and everyone went wild with cheers!", "image_prompt": "children's book illustration, cool cartoon lion moonwalking on a dance floor, spotlight on him, crowd of animals cheering and clapping, disco lights, digital art for kids"},
            {"scene_number": 3, "title_text": "Elephant's Twirl!", "narration": "Ellie the elephant tried to spin around and caused a tiny earthquake — but everyone laughed and loved it!", "image_prompt": "children's book illustration, large elephant twirling on a dance floor creating funny vibrations, animals bouncing around laughing, colourful party setting, digital art for kids"},
            {"scene_number": 4, "title_text": "Everyone Joins In!", "narration": "Soon every single animal was dancing — fast ones, slow ones, big ones and tiny ones — all moving together!", "image_prompt": "children's book illustration, huge crowd of different jungle animals all dancing joyfully together, disco ball, colourful lights, confetti, every animal with a big smile, digital art for kids"},
            {"scene_number": 5, "title_text": "Dance Champions!", "narration": "At the end every animal got a golden trophy because when everyone dances together, everybody wins!", "image_prompt": "children's book illustration, all cartoon animals holding golden trophies and celebrating together, confetti raining down, big group hug, joyful party finale, digital art for kids"},
        ],
    },
    "nature and plants": {
        "title": "The Secret Life of Plants!",
        "scenes": [
            {"scene_number": 1, "title_text": "A Tiny Seed", "narration": "Maya planted a tiny seed in the soil, watered it carefully, and whispered 'Grow, little seed, grow!'", "image_prompt": "children's book illustration, small child carefully planting a tiny seed in dark rich soil in a sunny garden, watering can nearby, hopeful expression, bright warm colours, digital art for kids"},
            {"scene_number": 2, "title_text": "The First Sprout!", "narration": "One morning Maya woke up and saw a tiny green sprout poking out of the soil — it was alive!", "image_prompt": "children's book illustration, excited child discovering a tiny green sprout in a flower pot on a windowsill, morning sunlight, big delighted eyes, digital art for kids"},
            {"scene_number": 3, "title_text": "Bugs Are Friends!", "narration": "A friendly ladybird and a tiny earthworm came to help — bugs are a plant's best garden helpers!", "image_prompt": "children's book illustration, cute smiling ladybird and friendly earthworm helping a growing plant in a garden, cartoon style, friendly bug faces, bright garden colours, digital art for kids"},
            {"scene_number": 4, "title_text": "Flower Power!", "narration": "After days of sunshine and rain, the seed had grown into the most beautiful, colourful flower you ever saw!", "image_prompt": "children's book illustration, magnificent bright rainbow-coloured flower in full bloom in a garden, child amazed and delighted, butterflies and bees visiting, sunny beautiful scene, digital art for kids"},
            {"scene_number": 5, "title_text": "Grow Your Own!", "narration": "Now Maya grows flowers, tomatoes and herbs — because with love and water anything can grow!", "image_prompt": "children's book illustration, proud child standing in a lush colourful garden full of flowers and vegetables they grew, garden tools, sunshine, rainbow in the background, digital art for kids"},
        ],
    },
    "sports day fun": {
        "title": "The Big Sports Day!",
        "scenes": [
            {"scene_number": 1, "title_text": "Ready, Set, Go!", "narration": "It was Sports Day and everyone was excited! Children stretched, jumped, and got ready to have the best day ever!", "image_prompt": "children's book illustration, excited children in colourful sports kit stretching and warming up on a bright grassy field, sports day banner, sunshine, digital art for kids"},
            {"scene_number": 2, "title_text": "The Big Race!", "narration": "The whistle blew and everyone ran as fast as their legs could carry them — the crowd went wild!", "image_prompt": "children's book illustration, group of cheerful children racing on a track, colourful running lanes, cheering crowd, motion lines showing speed, bright sunny sports day, digital art for kids"},
            {"scene_number": 3, "title_text": "Jump So High!", "narration": "Sam jumped so high in the long jump that he almost touched the clouds — everyone gasped!", "image_prompt": "children's book illustration, cartoon child jumping extremely high in a long jump pit, amazed spectators watching, gold medals dangling above, bright blue sky, digital art for kids"},
            {"scene_number": 4, "title_text": "Team Spirit!", "narration": "In the tug-of-war both teams pulled so hard they all fell down together — and everyone burst out laughing!", "image_prompt": "children's book illustration, two teams of children in colourful tug-of-war all tumbling over laughing, rope in the middle, muddy grass, huge happy smiles, digital art for kids"},
            {"scene_number": 5, "title_text": "Everyone's a Winner!", "narration": "At the end every child got a shiny medal because trying your best makes you a winner every single time!", "image_prompt": "children's book illustration, all children receiving colourful medals at a podium, big group celebration, teachers clapping, rainbow and confetti, warm joyful sports day finale, digital art for kids"},
        ],
    },
    "art class rainbow": {
        "title": "Let's Paint the Rainbow!",
        "scenes": [
            {"scene_number": 1, "title_text": "A Blank Canvas!", "narration": "Zara looked at her big blank white canvas and smiled — she was about to make the most colourful painting ever!", "image_prompt": "children's book illustration, enthusiastic child in a paint-splattered apron facing a big blank white canvas, colourful paints and brushes all around, bright art studio, digital art for kids"},
            {"scene_number": 2, "title_text": "Mixing Magic Colours!", "narration": "She mixed red and yellow to make orange, and blue and yellow to make green — colours are like magic!", "image_prompt": "children's book illustration, amazed child mixing paint colours in a palette and watching new colours appear, red plus yellow equals orange shown visually, bright cheerful art lesson, digital art for kids"},
            {"scene_number": 3, "title_text": "Painting the Sky!", "narration": "Zara painted a big bright blue sky with fluffy white clouds and a golden shining sun in the corner!", "image_prompt": "children's book illustration, child happily painting a sky scene on canvas with big brush strokes, painting the sun and clouds, colourful splashes of paint, joyful art session, digital art for kids"},
            {"scene_number": 4, "title_text": "The Rainbow Appears!", "narration": "She added a huge rainbow with all seven colours — red, orange, yellow, green, blue, indigo and violet!", "image_prompt": "children's book illustration, child painting a big beautiful rainbow on canvas, each colour arc labelled, rainbow glowing with magic, child's face lit up with joy, digital art for kids"},
            {"scene_number": 5, "title_text": "A Masterpiece!", "narration": "Everyone admired Zara's painting — she had made something truly beautiful all by herself!", "image_prompt": "children's book illustration, proud child standing next to completed rainbow painting in a frame, family and friends admiring it, gold star stickers, bright warm art gallery scene, digital art for kids"},
        ],
    },
    "music band animals": {
        "title": "The Jungle Music Band!",
        "scenes": [
            {"scene_number": 1, "title_text": "Forming the Band!", "narration": "Five animals in the jungle decided to form the world's very first jungle music band — the Jungle Jammers!", "image_prompt": "children's book illustration, five cartoon animals forming a music band, lion, elephant, parrot, monkey and zebra holding instruments, band name banner, excited expressions, digital art for kids"},
            {"scene_number": 2, "title_text": "Choosing Instruments!", "narration": "The lion played drums, the parrot played guitar, and the elephant tried to play the tiny flute — very funny!", "image_prompt": "children's book illustration, large elephant trying to play a tiny flute with a comical expression, lion at drum kit, parrot with guitar, hilarious and fun music scene, digital art for kids"},
            {"scene_number": 3, "title_text": "First Practice!", "narration": "Their first practice was very noisy — they all played different songs at once! But they laughed and kept going!", "image_prompt": "children's book illustration, cartoon animals playing instruments all at once with funny sound waves clashing, messy chaotic music practice, musical notes everywhere, animals laughing, digital art for kids"},
            {"scene_number": 4, "title_text": "Concert Night!", "narration": "On the big night, the Jungle Jammers played together perfectly and the whole jungle danced along!", "image_prompt": "children's book illustration, animal band performing on a jungle stage with spotlights, whole audience of animals dancing and cheering, colourful concert atmosphere, musical notes in the air, digital art for kids"},
            {"scene_number": 5, "title_text": "Rock Stars!", "narration": "The crowd roared and cheered — the Jungle Jammers were the greatest band the jungle had ever heard!", "image_prompt": "children's book illustration, five cartoon animal band members taking a bow on stage, huge cheering animal crowd, gold confetti, trophies and flowers, triumphant joyful concert finale, digital art for kids"},
        ],
    },
    "food around the world": {
        "title": "Yummy Foods from Every Land!",
        "scenes": [
            {"scene_number": 1, "title_text": "Pizza from Italy!", "narration": "In Italy people make pizza with stretchy dough, tangy tomato sauce and lots of gooey melted cheese — yum!", "image_prompt": "children's book illustration, Italian chef cartoon tossing pizza dough in the air, cheerful pizza with colourful toppings, Italian flag and leaning tower of Pisa in background, bright digital art for kids"},
            {"scene_number": 2, "title_text": "Sushi from Japan!", "narration": "In Japan they roll rice and fish into tiny delicious sushi bites — they eat them with chopsticks!", "image_prompt": "children's book illustration, excited child using chopsticks to pick up colourful sushi rolls, Japanese style setting with cherry blossoms, friendly sushi with cute faces, digital art for kids"},
            {"scene_number": 3, "title_text": "Tacos from Mexico!", "narration": "In Mexico they fill crunchy taco shells with beans, cheese and vegetables — so colourful and tasty!", "image_prompt": "children's book illustration, colourful crunchy tacos with all the toppings overflowing, Mexican decorations and flags, happy cartoon child eating a taco, bright fiesta colours, digital art for kids"},
            {"scene_number": 4, "title_text": "Dumplings from China!", "narration": "In China they make little dumplings filled with vegetables and meat — steamed until soft and perfectly delicious!", "image_prompt": "children's book illustration, bamboo steamer basket full of cute cartoon dumplings with happy faces, Chinese lanterns and decorations, child eating with chopsticks, warm cosy food scene, digital art for kids"},
            {"scene_number": 5, "title_text": "Food Brings Us Together!", "narration": "Food from every country is different and delicious — trying new food is like tasting a little bit of the whole world!", "image_prompt": "children's book illustration, children from different countries sharing food around a big round table, pizza, sushi, tacos and dumplings all together, flags of the world, happy sharing scene, digital art for kids"},
        ],
    },
    "building a treehouse": {
        "title": "Our Amazing Treehouse!",
        "scenes": [
            {"scene_number": 1, "title_text": "The Big Idea!", "narration": "Jake and his friends had the most brilliant idea — they were going to build a treehouse in the big oak tree!", "image_prompt": "children's book illustration, excited group of children gathered around a drawing of a treehouse, big oak tree visible behind them, pencils and paper, big ideas lightbulb above their heads, digital art for kids"},
            {"scene_number": 2, "title_text": "Gathering Wood!", "narration": "They collected planks of wood, nails, and a hammer — building day had finally arrived!", "image_prompt": "children's book illustration, children in hard hats carrying planks of wood and tools toward a big tree, construction day excitement, tool belt and safety goggles, bright sunny day, digital art for kids"},
            {"scene_number": 3, "title_text": "Hammering Away!", "narration": "Bang bang bang went the hammers! Every plank they nailed made the treehouse grow bigger and stronger!", "image_prompt": "children's book illustration, children happily hammering planks onto a growing treehouse structure in a big tree, wood shavings flying, focused and proud expressions, bright outdoors, digital art for kids"},
            {"scene_number": 4, "title_text": "Adding the Extras!", "narration": "They added a rope ladder, a little window, and a flag on top — their treehouse was totally perfect!", "image_prompt": "children's book illustration, children adding finishing touches to a completed treehouse, hanging a flag, painting walls, adding a rope ladder, proud happy faces, colourful treehouse in a big tree, digital art for kids"},
            {"scene_number": 5, "title_text": "Our Secret Hideout!", "narration": "That evening they sat in their treehouse watching the stars and knew it was the best thing they had ever built!", "image_prompt": "children's book illustration, happy children sitting inside their cosy treehouse at night, looking out the window at stars, fairy lights inside, warm golden glow, magical peaceful scene, digital art for kids"},
        ],
    },
    "world cultures celebration": {
        "title": "Celebrate the World!",
        "scenes": [
            {"scene_number": 1, "title_text": "Diwali — Festival of Lights!", "narration": "In India, Diwali is a festival where everyone lights thousands of tiny lamps to celebrate light over darkness!", "image_prompt": "children's book illustration, children in colourful Indian clothes lighting beautiful clay oil lamps called diyas, fireworks in the night sky, warm glowing lights everywhere, joyful celebration, digital art for kids"},
            {"scene_number": 2, "title_text": "Chinese New Year!", "narration": "In China, the New Year is celebrated with a huge red dragon parade, fireworks and lucky red envelopes!", "image_prompt": "children's book illustration, colourful dragon parade through a street with Chinese lanterns, children waving red envelopes, fireworks, festive red and gold decorations, bright digital art for kids"},
            {"scene_number": 3, "title_text": "Carnival in Brazil!", "narration": "In Brazil the Carnival is the biggest party on earth — with samba dancing, bright costumes and giant floats!", "image_prompt": "children's book illustration, children in spectacular colourful carnival costumes dancing samba, huge decorated float, confetti and feathers everywhere, joyful Brazilian carnival scene, digital art for kids"},
            {"scene_number": 4, "title_text": "Holi — Colour Festival!", "narration": "In India at Holi, everyone throws bright coloured powder at each other — you end up looking like a rainbow!", "image_prompt": "children's book illustration, happy children throwing clouds of bright coloured powder at each other at Holi festival, everyone laughing and covered in colours, joyful outdoor celebration, digital art for kids"},
            {"scene_number": 5, "title_text": "One World, One Family!", "narration": "Every country has its own special celebrations — and every one of them reminds us that the whole world is one big family!", "image_prompt": "children's book illustration, children from all around the world holding hands in a circle around a globe, each wearing their cultural clothes, flags and symbols, warm unified celebration, digital art for kids"},
        ],
    },
}


def get_random_topic() -> str:
    return random.choice(TOPICS)


def generate_story(topic: str) -> dict:
    # Normalize topic to match a known key
    key = topic.lower().strip()
    if key not in _STORIES:
        # Pick the closest match or random
        for k in _STORIES:
            if any(word in k for word in key.split()):
                key = k
                break
        else:
            key = random.choice(list(_STORIES.keys()))

    story = _STORIES[key].copy()
    story["scenes"] = [s.copy() for s in story["scenes"]]
    print(f"  Using built-in story template for: {key}")
    return story
