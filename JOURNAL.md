---
title: "TABLE TENIS ROBOT"
author: "Advay Roongta"
description: "Robot that moves paddle along 1 axis to return table tennis ball"
created_at: "June 7 2025"
time_spent: ""
---

# Note:
I haven't been working on this every single day, so for example the gap between July 21 and 23, I didn't do anything on this during the 22nd.

# June 9th: Just researching and finalized a rough design, 2hrs

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

![Timing Belt](https://www.fecconsulting.dk/images/stories/virtuemart/product/htd_tandrem_i_gummi_timing_belt.webp)

![Idler Pulley Plate](https://github.com/user-attachments/assets/129a4095-d922-4f57-8fa5-1c147d9728be)

![V-Slot NEMA 17 Linear Actuator](https://github.com/user-attachments/assets/2f00e190-52de-4b49-8df1-410c21da1532)

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

# June 30: I'm ill
I've been traveling for the past 2 weeks and fell quite sick a few days ago.
<br>
# July 21: Motor mount done, 4 hours (first CAD)
I made a mount from the vslot to the motor by using a threaded tnut that goes inside of the vslot extrusion, and then a screw that goes in there. The mount has a threaded hole for the screw, and a larger one for the motor, connected the two. I ran into a few issues about parts not working together such as the first few tnuts I found being too big. Through this proccess I also did a little bit of part sourcing, like finding the exact vslot I will buy when I get the grant :).
<br>
<img width="1096" height="701" alt="image" src="https://github.com/user-attachments/assets/51c75429-9a64-402e-bad5-4386d5ea958d" />
<br>
<img width="669" height="517" alt="image" src="https://github.com/user-attachments/assets/ba504a15-d5b6-4f6e-8a35-17d1d7bac24b" />
<br>
<img width="344" height="233" alt="image" src="https://github.com/user-attachments/assets/312b30ce-5e21-4a80-a08e-657641b113d1" />

<br>

# July 23: Fixed motor mount, added table mount: 3.5 hrs

So I first realized my motor mount was a bit flawed because it was only connected to the vslot at one point, which it not too stable, so I added another tnut and screw at the bottom. This fixed the issue, but then a few hours later I realized that having it at the bottom would block the belt from going around the vslot, which is vital, so I had to move it to the side. I also realized that the motor was quite high up, so I just lowered it down to make it centered with the vslot. I also today made the table mount to connect the whole thing to the table. I attached it to one side by using the same bottom platform for the motor, I just made a extrusion downwards and then a screw hole, there is also a screw hole on the top of the mount so they can connect with a screw. Tmrw I will do the idler mount and attach the other table mount. 





<img width="694" height="513" alt="image" src="https://github.com/user-attachments/assets/ad7893fd-0947-46be-8ee3-d5cc11c51b4a" />
<img width="599" height="542" alt="image" src="https://github.com/user-attachments/assets/75b0f543-fa85-492a-90ba-b35b3cc8c97a" />

<img width="413" height="747" alt="image" src="https://github.com/user-attachments/assets/d54cb246-87b7-4d53-b775-f0b246b98e8b" />

# July 24: Added Idler mount, 1hr

Today I added the idler mount to the other side of the vslot. It works the same way as the motor mount, except it attaches to the idler by going inside it (since it has a hole) rather than around the circumfrence. Didn't do much today but yeah.

<img width="510" height="416" alt="image" src="https://github.com/user-attachments/assets/4846547d-9e09-4cb0-85c4-585a74645ddc" />

# July 25: Attached other table mount, 1hr
So today I first attached the other table mount to the other side of the vslot where the idler is. I just made an extrusion down from my idler attachemetn and put a screw hole that can be conncted via a screw to the screw hole on the mount. this is the same way the other one works. I had to dimension the whole thing in a drawing to make sure that the two table mounts were lined up, and uh yeah. The nice thing about my table mount design is that because it uses screws, depending on the length of the screws, the mounts can be moved in parrallel to the table, meaning that no matter what happens, they will be able to fit on the table as long as they are the same height. This is because if the whole vslot system is 4.9 ft but the table is 5ft I can just move the mounts farther towards the screw head (if its facing away from the table) and the vslot system will get longer.

<img width="1374" height="430" alt="image" src="https://github.com/user-attachments/assets/87b4947e-f614-456c-bd16-77f6f05ad481" />
<img width="521" height="493" alt="image" src="https://github.com/user-attachments/assets/f2354cdb-5e42-4c12-b447-b0b102175a81" />

# July 27: MCU Mount, 1.5 hr

So today I made the mount for my mcu (which has a camera) to the grantry plate I chose. Because I have the mcu already at my house I was able to measure everything and make a simple but working mount that attaches onto the sides. The reason it wont go in the middle is because I dont want to obstuct the Micro USB Port and because the chip on the back of the board bumps out, and I didnt want to waste the fillament. This is sturdy enough by keeping the board straight and attachning from both sides. The reason I didnt make it go around the front of the board more is because it would then block the ports that I will need to connect to my motor. Also, in the gantry plate that i'm going to buy, the holes o the sides are big enough to fit the timing belt. I'm making good progress currently, the only part left to do is the paddle mount, which I think can be done in 1 day of locking in. 

<img width="223" height="571" alt="image" src="https://github.com/user-attachments/assets/8b7ba88b-2d9f-4ee7-8dca-3d5c6c066b85" />

<br>
<img width="548" height="613" alt="image" src="https://github.com/user-attachments/assets/157ff2eb-d709-4ed7-9655-2407cf4864fe" />

# July 29, Paddle Mount+ Full assembly, 2hrs

OMFG I AM DONE. Today I worked on my paddle mount and did the complete CAD assembly. First I had to precisley measure my ping pong paddle's handle, which took way longer than it should have, because its not a normal oval or anything (as shown in the sketch picture) I also dont have callipers so I had to use a blue broken transperent half-ruler and constantly convert inches to mm. After that, because my paddle has a hole in it, I cadded a shaft in my mount to go inside the hole for additional grip. For attaching the mount to the gantry, I did it the same way I attached the mcu mount to the gantry, a plate with a screw hole. I had to make these twin bars connecting the plate with screw hole to the mount because they could not be directly jointed, due to the vslot being in the way. I made these bars pretty chunky because the paddle will wheigh a lot and it needs to be stable. For the complete assembly I just imported components and moved them in place. :)



<img width="1124" height="724" alt="image" src="https://github.com/user-attachments/assets/cd0e6cdc-a010-486d-a3fd-5a1bd346d75a" />

<img width="1133" height="770" alt="image" src="https://github.com/user-attachments/assets/516c8108-95ba-433c-9a8e-77207f7ab06f" />

<img width="357" height="389" alt="image" src="https://github.com/user-attachments/assets/f6eef901-731b-4745-99e8-0659e38a6f82" />


# July 30, Firmware, 0.5hr

Just did the firmware and wiring to make the motor move. Today will be the day I also submit, I have now have to do parts sourcing and CAD renders. 


<img width="1612" height="1328" alt="image" src="https://github.com/user-attachments/assets/b9500892-ea0a-45ca-ac23-b2698dfa9ee8" />
