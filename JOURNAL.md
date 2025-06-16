---
title: "TABLE TENIS ROBOT"
author: "Advay Roongta"
description: "Robot that moves paddle along 1 axis to return table tennis ball"
created_at: "June 7 2025"
---
# June 9th: Just researching and finalized a rough design 

[So heres what I figured out so far about how it will work:
Nema stepper motor with a keyed belt attachement for the timing belt. The motor will be stationary and the belt will go around the vslot with an idler (wheel) on the other side. Then theres gonna be a gantry (plate) with wheels that gets attched to the belt just by feeding it through the holes on the side and securing it with tape or bands. For ball tracking perhaps an ESP-EYE from Visioneer that goes on top of the gantry plate. Then it could work by recognizing the ball by color and making sure it is in a certain range of x values that will be in the middle, and if the ball is not in that ideal range it will move depending on how out of the range it is.
The stuff I would have to do:<br>
Firmware
CAD: [
Mount for paddle to gantry<br>
Mounts for table to v-slot<br>
Mount for gantry to mcu<br>
Mount for motor to vslot and idler
]


[https://www.google.com/imgres?q=timing%20belt&imgurl=https%3A%2F%2Fwww.fecconsulting.dk%2Fimages%2Fstories%2Fvirtuemart%2Fproduct%2Fhtd_tandrem_i_gummi_timing_belt.webp&imgrefurl=https%3A%2F%2Fwww.fecconsulting.dk%2Fen%2Frubber-timing-belts%2Fhtd-timing-belts%2Ftiming-belts-htd-8m-optibel%2Ftiming-belt-htd-8m-1128-optibelt.html&docid=30Yg8dCHzwHhMM&tbnid=9UG149nHgJ8Y-M&vet=12ahUKEwiGusnew-WNAxUjGDQIHUFVOycQM3oFCIABEAA..i&w=1000&h=1000&hcb=2&ved=2ahUKEwiGusnew-WNAxUjGDQIHUFVOycQM3oFCIABEAA![image](https://github.com/user-attachments/assets/43aade89-3383-4b64-9eb4-b5b0ed51188b)
https://www.google.com/url?sa=i&url=https%3A%2F%2Fus.openbuilds.com%2Fidler-pulley-plate%2F&psig=AOvVaw2_WKV3VcRRSVFtPpaur4NS&ust=1749615590022000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJCGwZCA5o0DFQAAAAAdAAAAABAE![image](https://github.com/user-attachments/assets/129a4095-d922-4f57-8fa5-1c147d9728be)
https://www.google.com/url?sa=i&url=https%3A%2F%2Fyuyongindustry.com%2Fproduct%2Fv-slot-nema-17-linear-actuator-bundle%2F&psig=AOvVaw2D7c59vgqqqjgoWHlPNaUr&ust=1749582330572000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJCgr56E5Y0DFQAAAAAdAAAAABAE![image](https://github.com/user-attachments/assets/2f00e190-52de-4b49-8df1-410c21da1532)

]

**Total time spent: 2h**

# June 10th: Started code, time spent: 1hr
Its in python and so I just wrote the framework with OPenCV. Its only 20ish lines right now. Since i'm using the HoughCirlces function from OpenCV I had to meausure the minimun and maximun pixel radius of a table tennis ball. I took webcam photos from 7 ft and 1 ft away and measured it using this website called ImageJS.
<br>
![image](https://github.com/user-attachments/assets/73da225f-646e-4443-92a4-b0fe1988a77c)

# June 13th: Implemented color trakcing with code,2.5hr
I made the ball only register if it was white in color, and this works a lot better, and cuts out most other noise. Before it would think that my fingers and nose and eyes were circles. I also messed around with the Hough transform parameters to give me the best results. It works much better at close and moderate distances, but not so much at farther distances. I am exploring other options such as an elliptical transform. I also wrote some code that only chooses the ball if it is moving from its current position, but the color tracking kind of makes that redundant since in the real case (me playing ping pong) there will only be 1 white ball. <br>
![image](https://github.com/user-attachments/assets/b318f491-ce29-400b-8c8c-bed99fbaec25) 
<br>
# June 15th: Ball tracking complete with mask, 2hr:
Since the hough transform wasnt working well for farther distances, I used a color mask to first filter out all colors except orange (which will now be the color of the ball). Then it locates the ball based on the contours and size, and finds the center by using a cv2 function that returns the center coords for the smallest cirlce that fits around the contour. TLDR; It works! ONTO THE CAD PROBABLY NOW<br>
![image](https://github.com/user-attachments/assets/2a7acb81-5e66-4f59-993d-5bbe70aefe5f)
<br>



