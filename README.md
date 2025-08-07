# Table Tennis Robot

<h2>This is a 1-axis robot that will play table tennis with me when no one else will.</h2>

<img width="1024" height="694" alt="image" src="https://github.com/user-attachments/assets/7818f7dc-db02-4fcc-95a7-84b55bdee2f5" />
<img width="606" height="492" alt="image" src="https://github.com/user-attachments/assets/c63b207c-3d51-47a2-885a-ba92e16c3a21" />


<br>
This uses a vslot with a gantry plate on top. Connected to the gantry are my camera and paddle. The gantry will move based on camera input to the motor, which is connected to the gantry via a belt. The goal is to move along one axis to return the ball. The camera uses a simple contour recognition to find the ball and uses the ball's coordinates to see if it in the mid, left or right of the view. (TableTennisBot and TableTennisRobot are interchangable)


# It has:
<h3>An ESP32-S3-EYE Microcontroller and Camera, along with a matching mount.</h3>

<img width="571" height="747" alt="image" src="https://github.com/user-attachments/assets/3202e547-4a8d-4fa1-b1b6-8f63af50e335" />

<h3>2 twin table attachements</h3>

<img width="215" height="516" alt="image" src="https://github.com/user-attachments/assets/5ed289fc-a7bc-45b1-b0dc-56c7da03cd58" />

<h3>A Paddle mount(the paddle here is much bigger than the one I have irl. The mount if designed to fit my paddle which is smaller. This is just here for the full assembly. I will also be using adhesives to connect the paddle to the mount for a more polished project. </h3>

<img width="661" height="446" alt="image" src="https://github.com/user-attachments/assets/10a31978-7a7f-444c-92dc-499676d7d243" />

<img width="109" height="672" alt="image" src="https://github.com/user-attachments/assets/e9f81d9e-e73e-4f89-8a43-be0290eba592" />


<h3>A Idler Mount</h3>

<img width="392" height="94" alt="image" src="https://github.com/user-attachments/assets/2e109109-3bba-4f94-a942-ab6bcfa1da1d" />


<h3>A Motor mount</h3>
<img width="817" height="628" alt="image" src="https://github.com/user-attachments/assets/c6d4c2a2-1068-4825-8316-878ecd202ef0" />

<h3>Here is the wiring for the motor:</h3>
<img width="483" height="339" alt="image" src="https://github.com/user-attachments/assets/2d5b9a12-8f15-4e7f-92a8-58a05e4ec7d4" />

# Why

Most Table Tennis robots are developed at Google Deepmind or MIT. Although they are way better than mine, they cost thousands of dollars to make and develop. I made mine to just return the ball to a simple practice shot, rather than all different possible shots. I also really like playing table tennis and there is not always someone to play with me. Practicing by myself is really hard since my garage is cluttered and the balls get lost easily.


# BOM (Scroll all the way down)

                                                                                                                                                          | Vendor     | Name                            | Price   | Description                          | Notes                                                                                                                                                  | Link                                                                                                                                                                                                                         | Extra Link                                                                                         |
|:-----------|:--------------------------------|:--------|:-------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------|
| VXB        | V-Slot 20 x 20mm                | $38.28  | Vslot, 1500mm                        | I know $38.28<br>is alot, so I have permission from acon. https://hackclub.slack.com/archives/C08Q1H6D79B/p1749947689245759?thread_ts=1749512474.276809&cid=C08Q1H6D79B |                                                                                                                                                | https://vxb.com/products/20mm-linear-rail-5-feet-length-tubing-2020-aluminu?variant=43583118115051 |
| Biqu       | Timing Belt                     | $4.85   | All Biqu products bought together    |                                                                                                                                                       | https://biqu.equipment/products/hot-sale-10meter-gt2-6mm-open-timing-belt-width-6mm-gt2-belt-for-3d-printer-parts?variant=12951056810082       |                                                                                                    |
| Biqu       | Idler x2                        | $5.04   | All Biqu products bought together    |                                                                                                                                                       | https://biqu.equipment/products/3d-printer-parts-16-teeth-synchronous-wheel-pulley-wheel-driven-wheel-perlin-16-2gt-toothed-gear-bore-3mm?variant=13043846873186 |                                                                                                    |
| Biqu       | Shipping+Tax                    | $6.58   | All Biqu products bought together    |                                                                                                                                                       |                                                                                                                                                |                                                                                                    |
| Aliexpress | M5 Screws                       | $2.27   | Aliexpress items bought together     |                                                                                                                                                       | https://www.aliexpress.us/item/3256805692722422.html                                                                                           |                                                                                                    |
| Aliexpress | M5 Tnuts                        | $1.52   |                                      |                                                                                                                                                       | https://www.aliexpress.us/item/3256805435856022.html                                                                                           |                                                                                                    |
| Aliexpress | Motor                           | $6.19   | Nema 17                              |                                                                                                                                                       | https://www.aliexpress.us/item/2255800222409012.html                                                                                           |                                                                                                    |
| Aliexpress | TMC2209                         | $2.38   | Motor Driver                         |                                                                                                                                                       | https://www.aliexpress.us/item/3256805074646808.html                                                                                           |                                                                                                    |
| Aliexpress | 2020 V-slot Wheels Gantry Plate | $6.28   | Gantry Plate + Wheels                |                                                                                                                                                       | https://www.aliexpress.us/item/3256808485831638.html                                                                                           |                                                                                                    |
| aliexpress | VHB                             | $3.29   | VHB Tape like @LoganPeterson said    |                                                                                                                                                       | https://www.aliexpress.us/item/3256807144002696.html                                                                                           |                                                                                                    |
| aliexpress | Shipping+Tax                    | $2.00   | All Aliexpress items bought together |                                                                                                                                                       |                                                                                                                                                |                                                                                                    |
| Total      |                                  | $78.68  |                                      |                                                                                                                                                       |                                                                                                                                                |                                                                                                    |
|
