# BRTrains3 usage and door assignments

This note records the vehicle-level assignments made on 2026-10-18. Profiles and liveries were deliberately not split: `doors` and `usage` are authored at vehicle scope, with BRBuild still allowing later livery/profile overrides.

## Rules

- `usage` was assigned for every known vehicle so the builder does not rely on generic fallbacks. Broad tags such as `PASSENGER`, `FREIGHT`, and `MAIL` are combined with service-role tags where useful.
- Door values were assigned only where the stock family or documented arrangement was clear. An omitted door value is intentional; loading speed will be inferred from usage until a more specific door assignment is established.
- Medium/low-confidence usage entries are best-supported classifications, not claims of a single exclusive historical use.
- Loading-speed behaviour was not changed.

## Sources consulted

- https://en.wikipedia.org/wiki/List_of_British_Rail_classes
- https://en.wikipedia.org/wiki/British_Rail_Mark_1
- https://en.wikipedia.org/wiki/British_Railways_Mark_2
- https://en.wikipedia.org/wiki/British_Railways_Mark_3
- https://en.wikipedia.org/wiki/British_Railways_Mark_4
- https://en.wikipedia.org/wiki/British_Railways_Mark_5A
- https://en.wikipedia.org/wiki/Travelling_Post_Office
- https://en.wikipedia.org/wiki/LNER_coaching_stock
- https://en.wikipedia.org/wiki/GWR_coaching_stock
- https://en.wikipedia.org/wiki/LMS_coaching_stock
- https://en.wikipedia.org/wiki/British_Rail_Class_345
- https://en.wikipedia.org/wiki/British_Rail_Class_700
- https://en.wikipedia.org/wiki/British_Rail_Class_717
- https://en.wikipedia.org/wiki/British_Rail_Class_390
- https://en.wikipedia.org/wiki/British_Rail_Class_800
- https://en.wikipedia.org/wiki/British_Rail_Class_101
- https://en.wikipedia.org/wiki/British_Rail_Class_483
- https://en.wikipedia.org/wiki/Advanced_Passenger_Train

## Per-vehicle record

- `BR08` (Class 08): usage `['DEPARTMENTAL', 'UTILITY']` (medium; departmental/engineering or non-standard support stock). Door type not assigned; infer from usage.
- `BR101` (Class 101): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family); doors `slam` (high confidence from the supplied door-layout classification).
- `BR102` (Class 102): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family); doors `slam` (high confidence from the supplied door-layout classification).
- `BR121` (Class 121): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family); doors `slam` (high confidence from the supplied door-layout classification).
- `BR128` (Class 128): usage `['MAIL']` (high; mail/parcels role from YAML/candidate identity). Door type not assigned; infer from usage.
- `BR13` (Class 13): usage `['DEPARTMENTAL', 'UTILITY']` (medium; departmental/engineering or non-standard support stock). Door type not assigned; infer from usage.
- `BR140` (Class 140): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR141` (Class 141): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR142` (Class 142): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR143` (Class 143): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR150_0` (Class 150/0): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR150_1` (Class 150/1): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR150_2` (Class 150/2): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR151` (Class 151): usage `['PASSENGER', 'REGIONAL', 'PROTOTYPE']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR153` (Class 153): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR155` (Class 155): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR156` (Class 156): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR158` (Class 158): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR159` (Class 159): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR165` (Class 165): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR168` (Class 168/0): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR168_123` (Class 168/1-3): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR170` (Class 170): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR171` (Class 171): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR172` (Class 172/1): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR172_0` (Class 172/0): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR172_23` (Class 172/2/3): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR175` (Class 175): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR180` (Class 180): usage `['PASSENGER', 'INTERCITY']` (high; named high-speed/intercity passenger stock). Door type not assigned; infer from usage.
- `BR18100` (BR 18100 (Gas Turbine Prototype)): usage `['PROTOTYPE']` (high; prototype/experimental identity). Door type not assigned; infer from usage.
- `BR185` (Class 185): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR195Civity` (Class 195): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR196Civity` (Class 196): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR197Civity` (Class 197): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR20` (Class 20): usage `['DEPARTMENTAL', 'UTILITY']` (medium; departmental/engineering or non-standard support stock). Door type not assigned; infer from usage.
- `BR220` (Class 220): usage `['PASSENGER', 'INTERCITY']` (high; named high-speed/intercity passenger stock). Door type not assigned; infer from usage.
- `BR221` (Class 221): usage `['PASSENGER', 'INTERCITY']` (high; named high-speed/intercity passenger stock). Door type not assigned; infer from usage.
- `BR222` (Class 222): usage `['PASSENGER', 'INTERCITY']` (high; named high-speed/intercity passenger stock). Door type not assigned; infer from usage.
- `BR230` (Class 230 'D-Train'): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR231` (Class 231/0): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR252` (Class 41): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `BR28` (Class 28): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `BR302` (Class 302): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR305` (Class 305): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR31` (Class 31): usage `['DEPARTMENTAL', 'UTILITY']` (medium; departmental/engineering or non-standard support stock). Door type not assigned; infer from usage.
- `BR310` (Class 310): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR315` (Class 315): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR319` (Class 319): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR320` (Class 320/3): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR321` (Class 321): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR322` (Class 322): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR323` (Class 323): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR325` (Class 325): usage `['MAIL']` (high; mail/parcels role from YAML/candidate identity). Door type not assigned; infer from usage.
- `BR33` (Class 33): usage `['DEPARTMENTAL', 'UTILITY']` (medium; departmental/engineering or non-standard support stock). Door type not assigned; infer from usage.
- `BR331` (Class 331): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR332` (Class 332): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR333` (Class 333): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR334` (Class 334): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR345` (Class 345): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family); doors `commuter_triple` (high confidence from the supplied door-layout classification).
- `BR350` (Class 350): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR357` (Class 357): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR360` (Class 360/1): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR360_2` (Class 360/2): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR37` (Class 37): usage `['DEPARTMENTAL', 'UTILITY']` (medium; departmental/engineering or non-standard support stock). Door type not assigned; infer from usage.
- `BR373` (Class 373): usage `['PASSENGER', 'INTERCITY', 'HIGH_SPEED']` (high; named high-speed/intercity passenger stock). Door type not assigned; infer from usage.
- `BR374` (Class 374): usage `['PASSENGER', 'INTERCITY', 'HIGH_SPEED']` (high; named high-speed/intercity passenger stock). Door type not assigned; infer from usage.
- `BR375` (Class 375): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR376` (Class 376): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR377` (Class 377): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR378` (Class 378): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR379` (Class 379): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR380` (Class 380): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR387` (Class 387): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR390` (Class 390): usage `['PASSENGER', 'INTERCITY', 'HIGH_SPEED']` (high; named high-speed/intercity passenger stock); doors `intercity` (high confidence from the supplied door-layout classification).
- `BR395` (Class 395): usage `['PASSENGER', 'REGIONAL']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR397` (Class 397): usage `['PASSENGER', 'INTERCITY']` (high; named high-speed/intercity passenger stock). Door type not assigned; infer from usage.
- `BR411` (Class 411): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR412` (Class 412): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR413` (Class 413): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR414` (Class 414): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR415_1` (Class 415/1): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR415_2` (Class 415/2): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR416_1` (Class 416/1): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR416_2` (Class 416/2): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR418_1` (Class 418): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR421` (Class 421): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR422` (Class 422): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR423` (Class 423): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR43` (Class 43): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `BR432` (Class 432): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR438` (Class 438): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR442` (Class 442): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR444` (Class 444): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR450` (Class 450): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR455` (Class 455): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR456` (Class 456): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR458` (Class 458): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR460` (Class 460): usage `['PASSENGER', 'REGIONAL']` (medium; passenger role; service category inferred from available identity). Door type not assigned; infer from usage.
- `BR465` (Class 465): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR466` (Class 466): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR47` (Class 47): usage `['DEPARTMENTAL']` (medium; departmental/engineering or non-standard support stock). Door type not assigned; infer from usage.
- `BR48` (Class 48): usage `['PROTOTYPE']` (high; prototype/experimental identity). Door type not assigned; infer from usage.
- `BR483` (Class 483 (LU 1938 Stock)): usage `['PASSENGER', 'UNDERGROUND', 'METRO', 'LOCAL']` (high; Underground/metro stock); doors `multiple` (high confidence from the supplied door-layout classification).
- `BR484` (Class 484 (LU D Stock)): usage `['PASSENGER', 'UNDERGROUND', 'METRO', 'LOCAL']` (high; Underground/metro stock); doors `multiple` (high confidence from the supplied door-layout classification).
- `BR50` (Class 50): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `BR504` (Class 504): usage `['PASSENGER', 'UNDERGROUND', 'LOCAL']` (high; Underground stock). Door type not assigned; infer from usage.
- `BR507` (Class 507): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR508` (Class 508): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR52` (Class 52): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `BR55` (Class 55): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `BR56` (Class 56): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `BR57` (Class 57): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `BR58` (Class 58): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `BR59` (Class 59): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `BR60` (Class 60): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `BR66` (Class 66): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `BR67` (Class 67): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `BR68` (Class 68): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `BR69` (Class 69): usage `['DEPARTMENTAL', 'UTILITY']` (medium; departmental/engineering or non-standard support stock). Door type not assigned; infer from usage.
- `BR70` (Class 70): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `BR700` (Class 700): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family); doors `commuter_double` (high confidence from the supplied door-layout classification).
- `BR701` (Class 701): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR707` (Class 707): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR70OG` (Class 70 (Southern Railway Class CC)): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `BR71` (Class 71): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `BR710` (Class 710): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR717` (Class 717): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family); doors `commuter_double` (high confidence from the supplied door-layout classification).
- `BR720` (Class 720): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR730` (Class 730): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR73GatEx` (Class 73 "Gatwick Express" set (9 car + locomotive)): usage `['PASSENGER', 'REGIONAL']` (medium; passenger role; service category inferred from available identity). Door type not assigned; infer from usage.
- `BR745` (Class 745/0/1): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR755` (Class 755 FLIRT): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR756` (Class 756): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR76` (Class 76 (LNER Gresley "EM1")): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `BR769` (Class 769/0/3/4/5/9): usage `['PASSENGER', 'COMMUTER', 'LOCAL']` (high; commuter/suburban multiple unit family). Door type not assigned; infer from usage.
- `BR76Prototype` (Class 76 Prototype (LNER Gresley "EM1")): usage `['PROTOTYPE']` (high; prototype/experimental identity). Door type not assigned; infer from usage.
- `BR799` (Class 799 Hydrogen Prototype): usage `['PASSENGER', 'REGIONAL', 'PROTOTYPE']` (high; regional passenger multiple unit or coach family). Door type not assigned; infer from usage.
- `BR80` (Class 80 (25kV Prototype)): usage `['PROTOTYPE']` (high; prototype/experimental identity). Door type not assigned; infer from usage.
- `BR800` (Class 800): usage `['PASSENGER', 'INTERCITY', 'HIGH_SPEED']` (high; named high-speed/intercity passenger stock); doors `intercity` (high confidence from the supplied door-layout classification).
- `BR801` (Class 801): usage `['PASSENGER', 'INTERCITY', 'HIGH_SPEED']` (high; named high-speed/intercity passenger stock); doors `intercity` (high confidence from the supplied door-layout classification).
- `BR802` (Class 802): usage `['PASSENGER', 'INTERCITY', 'HIGH_SPEED']` (high; named high-speed/intercity passenger stock); doors `intercity` (high confidence from the supplied door-layout classification).
- `BR803` (Class 803): usage `['PASSENGER', 'INTERCITY', 'HIGH_SPEED']` (high; named high-speed/intercity passenger stock); doors `intercity` (high confidence from the supplied door-layout classification).
- `BR805` (Class 805): usage `['PASSENGER', 'INTERCITY', 'HIGH_SPEED']` (high; named high-speed/intercity passenger stock); doors `intercity` (high confidence from the supplied door-layout classification).
- `BR807` (Class 807): usage `['PASSENGER', 'INTERCITY', 'HIGH_SPEED']` (high; named high-speed/intercity passenger stock); doors `intercity` (high confidence from the supplied door-layout classification).
- `BR81` (Class 81): usage `['PROTOTYPE']` (high; prototype/experimental identity). Door type not assigned; infer from usage.
- `BR810` (Class 810): usage `['PASSENGER', 'INTERCITY', 'HIGH_SPEED']` (high; named high-speed/intercity passenger stock); doors `intercity` (high confidence from the supplied door-layout classification).
- `BR82` (Class 82): usage `['PROTOTYPE']` (high; prototype/experimental identity). Door type not assigned; infer from usage.
- `BR83` (Class 83): usage `['PROTOTYPE']` (high; prototype/experimental identity). Door type not assigned; infer from usage.
- `BR84` (Class 84): usage `['PROTOTYPE']` (high; prototype/experimental identity). Door type not assigned; infer from usage.
- `BR85` (Class 85): usage `['PROTOTYPE']` (high; prototype/experimental identity). Door type not assigned; infer from usage.
- `BR86` (Class 86): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `BR87` (Class 87): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `BR88` (Class 88): usage `['PROTOTYPE']` (high; prototype/experimental identity). Door type not assigned; infer from usage.
- `BR89` (Class 89): usage `['PASSENGER', 'INTERCITY', 'PROTOTYPE']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `BR90` (Class 90): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `BR901` (Class 901): usage `['PROTOTYPE']` (high; prototype/experimental identity). Door type not assigned; infer from usage.
- `BR91` (Class 91): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `BR92` (Class 92): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `BR93` (Class 93): usage `['PASSENGER', 'INTERCITY', 'PROTOTYPE']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `BR99` (Class 99): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `BRAPTE` (APT-E): usage `['PASSENGER', 'INTERCITY', 'HIGH_SPEED', 'PROTOTYPE']` (high; named high-speed/intercity passenger stock). Door type not assigned; infer from usage.
- `BRAPTP` (Class 370 APT-P): usage `['PASSENGER', 'INTERCITY', 'HIGH_SPEED', 'PROTOTYPE']` (high; named high-speed/intercity passenger stock). Door type not assigned; infer from usage.
- `BRBluePullman` (Blue Pullman): usage `['PASSENGER', 'INTERCITY']` (high; named high-speed/intercity passenger stock). Door type not assigned; infer from usage.
- `BRConflatA` (Conflat A Container Wagon): usage `['FREIGHT']` (high; non-passenger wagon cargo from YAML). Door type not assigned; infer from usage.
- `BRConflatP` (Conflat P Container Wagon): usage `['FREIGHT']` (high; non-passenger wagon cargo from YAML). Door type not assigned; infer from usage.
- `BRContainerFlatbed` (FEA Container Flat Wagon): usage `['FREIGHT']` (high; non-passenger wagon cargo from YAML). Door type not assigned; infer from usage.
- `BREurotunnelClass9` (Eurotunnel Class 9): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `BRFlyingBanana` (Flying Banana): usage `['PASSENGER', 'INTERCITY']` (high; named high-speed/intercity passenger stock). Door type not assigned; infer from usage.
- `BRHHA` (BR HHA Hopper Wagon): usage `['FREIGHT']` (high; non-passenger wagon cargo from YAML). Door type not assigned; infer from usage.
- `BRJIA` (BR JIA Polybulk Wagon): usage `['FREIGHT']` (high; non-passenger wagon cargo from YAML). Door type not assigned; infer from usage.
- `BRKestrel` (Kestrel): usage `['PROTOTYPE']` (high; prototype/experimental identity). Door type not assigned; infer from usage.
- `BRMPVDualFreight` (BR MPV Dual Freight): usage `['DEPARTMENTAL', 'UTILITY', 'FREIGHT']` (medium; departmental/engineering or non-standard support stock). Door type not assigned; infer from usage.
- `BRMPVDualTrack` (British Rail MPV Dual-Track): usage `['DEPARTMENTAL', 'UTILITY']` (medium; departmental/engineering or non-standard support stock). Door type not assigned; infer from usage.
- `BRMk1` (Mk1 Coach): usage `['PASSENGER', 'INTERCITY']` (medium; coach service role inferred from historical/InterCity stock); doors `slam` (high confidence from the supplied door-layout classification).
- `BRMk2` (Mk2 Coach): usage `['PASSENGER', 'INTERCITY']` (medium; coach service role inferred from historical/InterCity stock); doors `slam` (high confidence from the supplied door-layout classification).
- `BRMk3` (Mk3 Coach): usage `['PASSENGER', 'INTERCITY']` (medium; coach service role inferred from historical/InterCity stock); doors `intercity` (high confidence from the supplied door-layout classification).
- `BRMk4` (Mk4 Coach): usage `['PASSENGER', 'INTERCITY']` (medium; coach service role inferred from historical/InterCity stock); doors `intercity` (high confidence from the supplied door-layout classification).
- `BRMk5` (Mk5 Coach): usage `['PASSENGER', 'INTERCITY']` (medium; coach service role inferred from historical/InterCity stock). Door type not assigned; infer from usage.
- `BRMk5a` (Mk5a Coach): usage `['PASSENGER', 'INTERCITY']` (medium; coach service role inferred from historical/InterCity stock). Door type not assigned; infer from usage.
- `BRStandard9F` (Standard Class 9F): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `BRTCovHop` (BRT Covered Hopper): usage `['FREIGHT']` (high; non-passenger wagon cargo from YAML). Door type not assigned; infer from usage.
- `BRTTA` (BR TTA Tank Wagon): usage `['FREIGHT']` (high; non-passenger wagon cargo from YAML). Door type not assigned; infer from usage.
- `BRVGA` (BR VGA Wagon): usage `['FREIGHT']` (high; non-passenger wagon cargo from YAML). Door type not assigned; infer from usage.
- `CaledonianSingle` (Caledonian Single 4-2-2): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `CoronationSet` (LNER Coronation Set): usage `['PASSENGER', 'INTERCITY']` (medium; coach service role inferred from historical/InterCity stock); doors `slam` (high confidence from the supplied door-layout classification).
- `Furness115` (Furness Railway 115 Class): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `Furness20TonHopper` (Furness Railway 20-ton Hopper Wagon): usage `['FREIGHT']` (high; non-passenger wagon cargo from YAML). Door type not assigned; infer from usage.
- `FurnessCoppernob` (Furness A2 Class 0-4-0): usage `['PROTOTYPE']` (high; prototype/experimental identity). Door type not assigned; infer from usage.
- `FurnessD1` (Furness Sharp D1 Class 0-6-0): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `FurnessGoodsVan` (Furness Railway Goods Van): usage `['FREIGHT']` (high; non-passenger wagon cargo from YAML). Door type not assigned; infer from usage.
- `FurnessK2` (Furness K2 Class 4-4-0): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `FurnessLumberWagon` (Furness Railway Lumber Wagon): usage `['FREIGHT']` (high; non-passenger wagon cargo from YAML). Door type not assigned; infer from usage.
- `FurnessTankWagon` (Furness Railway Rectangular Tanker Wagon): usage `['FREIGHT']` (high; non-passenger wagon cargo from YAML). Door type not assigned; infer from usage.
- `GCRRobinson50CLSO` (GCR Robinson 50ft Semi-Corridor Lavatory Composite): usage `['PASSENGER', 'REGIONAL']` (medium; coach service role inferred from historical/InterCity stock); doors `slam` (high confidence from the supplied door-layout classification).
- `GERL77` (GER Class L77 0-6-2T): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `GNRA1` (GNR Gresley Class A1 4-6-2): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `GWR254CompSY` (GWR Dean 25ft 4 Compartment Second Class (SY)): usage `['PASSENGER', 'INTERCITY']` (medium; coach service role inferred from historical/InterCity stock); doors `slam` (high confidence from the supplied door-layout classification).
- `GWR5700` (GWR Collett 5700 Class 0-6-0PT): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `GWR6700` (GWR Collett 6700 Class 0-6-0PT): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `GWRGreatBear` (GWR Churchward 111 4-6-2): usage `['PASSENGER', 'INTERCITY', 'PROTOTYPE']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `GWRHall` (GWR Collett 4900 Class 4-6-0): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `GWRMinkG` (GWR Mink G Goods Van): usage `['FREIGHT']` (high; non-passenger wagon cargo from YAML). Door type not assigned; infer from usage.
- `LMS8F` (LMS Stanier Class 8F 2-8-0): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `LMSBlack5` (LMS Stanier Class 5MT 4-6-0): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `LMSJubilee` (LMS Stanier Jubilee Class 4-6-0): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `LMSStanierP3BG` (LMS Stanier Period III 50ft BG): usage `['PASSENGER', 'INTERCITY']` (medium; coach service role inferred from historical/InterCity stock); doors `slam` (high confidence from the supplied door-layout classification).
- `LNERA3` (LNER Gresley Class A3 4-6-2): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `LNERA4` (LNER Gresley Class A4 4-6-2): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `LNERBCK` (LNER Gresley BCK): usage `['PASSENGER', 'INTERCITY']` (medium; coach service role inferred from historical/InterCity stock); doors `slam` (high confidence from the supplied door-layout classification).
- `LNERBG` (LNER Gresley BG): usage `['PASSENGER', 'INTERCITY']` (medium; coach service role inferred from historical/InterCity stock); doors `slam` (high confidence from the supplied door-layout classification).
- `LNERGresley616BCK` (LNER Gresley 61' 6" BCK): usage `['PASSENGER', 'INTERCITY']` (medium; coach service role inferred from historical/InterCity stock); doors `slam` (high confidence from the supplied door-layout classification).
- `LNERGresley616BG` (LNER Gresley 61' 6" BG): usage `['MAIL']` (high; mail/parcels role from YAML/candidate identity). Door type not assigned; infer from usage.
- `LNERGresley616TK` (LNER Gresley 61' 6" TK): usage `['PASSENGER', 'INTERCITY']` (medium; coach service role inferred from historical/InterCity stock); doors `slam` (high confidence from the supplied door-layout classification).
- `LNERGresley616TPO` (LNER Gresley 61' 6" TPO): usage `['MAIL']` (high; mail/parcels role from YAML/candidate identity). Door type not assigned; infer from usage.
- `LNERJ70` (GER Class C53 0-6-0T): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `LNERP2` (LNER Gresley Class P2 2-8-2): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `LNERPV` (LNER Gresley PV): usage `['MAIL']` (high; mail/parcels role from YAML/candidate identity). Door type not assigned; infer from usage.
- `LNERTK` (LNER Gresley TK): usage `['PASSENGER', 'INTERCITY']` (medium; coach service role inferred from historical/InterCity stock); doors `slam` (high confidence from the supplied door-layout classification).
- `LNERThompson61FK` (LNER Thompson 61' FK): usage `['PASSENGER', 'INTERCITY']` (medium; coach service role inferred from historical/InterCity stock); doors `slam` (high confidence from the supplied door-layout classification).
- `LNERThompson63TK` (LNER Thompson 63' TK): usage `['PASSENGER', 'INTERCITY']` (medium; coach service role inferred from historical/InterCity stock); doors `slam` (high confidence from the supplied door-layout classification).
- `LNERV2` (LNER Gresley Class V2 2-6-2): usage `['PASSENGER', 'INTERCITY']` (medium; passenger express locomotive role). Door type not assigned; infer from usage.
- `LNWRWebb` (LNWR Webb Coal Tank 0-6-2T): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `LSWRAdamsRadial` (LSWR Adams Radial): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `LUAStock` (LU A Stock): usage `['PASSENGER', 'UNDERGROUND', 'METRO', 'LOCAL']` (high; Underground/metro stock); doors `multiple` (high confidence from the supplied door-layout classification).
- `LUCStock` (LU C Stock): usage `['PASSENGER', 'UNDERGROUND', 'METRO', 'LOCAL']` (high; Underground/metro stock); doors `multiple` (high confidence from the supplied door-layout classification).
- `MPVSingle` (BR MPV Single): usage `['DEPARTMENTAL', 'UTILITY']` (medium; departmental/engineering or non-standard support stock). Door type not assigned; infer from usage.
- `RMTPO` (Royal Mail TPO): usage `['MAIL']` (high; mail/parcels role from YAML/candidate identity). Door type not assigned; infer from usage.
- `RS_SWB_Hopper` (LNER Standard Medium Hopper): usage `['FREIGHT']` (high; non-passenger wagon cargo from YAML). Door type not assigned; infer from usage.
- `SRQ1` (SR Bulleid Q1 Class 0-6-0): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `SRZClass` (SR Z Class): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.
- `StephensonPlanet` (L&MR Stephenson 2-2-0): usage `['PROTOTYPE']` (high; prototype/experimental identity). Door type not assigned; infer from usage.
- `TGV` (SNCF TGV): usage `['MAIL']` (high; mail/parcels role from YAML/candidate identity). Door type not assigned; infer from usage.
- `WDAusterityTank` (WD Austerity Tank 0-6-0ST): usage `['FREIGHT']` (medium; locomotive with no passenger role in YAML; freight is best operational fallback). Door type not assigned; infer from usage.


## Follow-up from the slam-door train reference

The Wikipedia slam-door train article explicitly identifies the Class 101–129 DMU family as slam-door stock, the Eastern Region Class 302–312 family as slam-door except Classes 303, 306 and 311, and the Southern 4-CIG/4-CEP/4-VEP families as slam-door. It also identifies the Mark 1/Mark 2 association used by the initial pass. On that basis, these additional vehicle-level assignments were applied: `BR302`, `BR305`, `BR310`, `BR411`, `BR412`, `BR413`, `BR414`, `BR415_1`, `BR415_2`, `BR416_1`, `BR416_2`, `BR418_1`, `BR421`, `BR422`, `BR423`, `BR432`, and `BR438` → `doors: slam`.

`LNERJ70` was corrected to remove an erroneous door assignment: it is a locomotive, not passenger stock.

Source: https://en.wikipedia.org/wiki/Slam-door_train

## Door-layout classification incorporated

The supplied research distinguishes door arrangement from service pattern and was applied at vehicle scope:

- `intercity`: narrow, generally single-leaf doors near carriage ends. Applied to Classes 153, 155, 156, 158, 159, 175, 180, 220, 221, 222, 373, 374, 390, 397, 442, 444, 800, 801, 802, 803, 805, 807 and 810.
- `commuter_double`: wider doors positioned around thirds or quarters. Applied to the listed BRTrains3 classes in the supplied commuter-style grouping, including 141/142/143, 150/151, 165/166, 168/170/171/172, 185, 195/196/197, 303/311, 313/314/315/317/318/319/320/321/322/323, 332/333/334, 350/357/360/365/375/376/377/378/379/380/385/387, 450/455/456/458/460/465/466, 700/701/707/710/717/720/730, 756, 769 and 231.
- `commuter_triple`: Class 345 remains explicitly assigned as the three-doorway commuter case.
- `multiple`: retained for London Underground-derived or otherwise unusual multiple-unit arrangements such as Classes 483 and 484; these are not treated as conventional intercity or commuter layouts.

Classes 395, 745, 755 and 230 are deliberately not forced into an existing door enum because the supplied material identifies them as exceptions or unusual layouts. Classes absent from BRTrains3 were not added.

Reference supplied for this update: UK passenger multiple-unit door-layout classification citing Fandom, Wikipedia, GB Trains and Hitachi Rail material.
