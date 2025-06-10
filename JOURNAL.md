---
title: "TABLE TENIS ROBOT"
author: "Advay Roongta"
description: "Robot that moves paddle along 1 axis to return table tennis ball"
created_at: "June 7 2025"
---
# June 9th: Just researching and finalized a rough design

[So heres what I figured out so far about how it will work:
Nema stepper motor with a keyed belt attachement for the timing belt. The motor will be stationary and the belt will go around the vslot with an idler (wheel) on the other side. Then theres gonna be a gantry (plate) with wheels that gets attched to the belt just by feeding it through the holes on the side and securing it with tape or bands. For ball tracking perhaps an ESP-EYE from Visioneer that goes on top of the gantry plate. Then it could work by recognizing the ball by color and making sure it is in a certain range of x values that will be in the middle, and if the ball is not in that ideal range it will move depending on how out of the range it is.
The stuff I would have to do:
Firmware
CAD: [
Mount for paddle to gantry
Mounts for table to v-slot
Mount for gantry to mcu
]


[https://www.google.com/imgres?q=timing%20belt&imgurl=https%3A%2F%2Fwww.fecconsulting.dk%2Fimages%2Fstories%2Fvirtuemart%2Fproduct%2Fhtd_tandrem_i_gummi_timing_belt.webp&imgrefurl=https%3A%2F%2Fwww.fecconsulting.dk%2Fen%2Frubber-timing-belts%2Fhtd-timing-belts%2Ftiming-belts-htd-8m-optibel%2Ftiming-belt-htd-8m-1128-optibelt.html&docid=30Yg8dCHzwHhMM&tbnid=9UG149nHgJ8Y-M&vet=12ahUKEwiGusnew-WNAxUjGDQIHUFVOycQM3oFCIABEAA..i&w=1000&h=1000&hcb=2&ved=2ahUKEwiGusnew-WNAxUjGDQIHUFVOycQM3oFCIABEAA![image](https://github.com/user-attachments/assets/43aade89-3383-4b64-9eb4-b5b0ed51188b)
https://www.google.com/url?sa=i&url=https%3A%2F%2Fus.openbuilds.com%2Fidler-pulley-plate%2F&psig=AOvVaw2_WKV3VcRRSVFtPpaur4NS&ust=1749615590022000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJCGwZCA5o0DFQAAAAAdAAAAABAE![image](https://github.com/user-attachments/assets/129a4095-d922-4f57-8fa5-1c147d9728be)
https://www.google.com/url?sa=i&url=https%3A%2F%2Fyuyongindustry.com%2Fproduct%2Fv-slot-nema-17-linear-actuator-bundle%2F&psig=AOvVaw2D7c59vgqqqjgoWHlPNaUr&ust=1749582330572000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJCgr56E5Y0DFQAAAAAdAAAAABAE![image](https://github.com/user-attachments/assets/2f00e190-52de-4b49-8df1-410c21da1532)

]

**Total time spent: 2h**
