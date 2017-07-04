<h1>Random python codes.</h1>


* The files <b>data.py, mail.py, print_and_logg.py</b> and <b>ser_status.py</b> belongs together.
It is a project I worked on from time to time, with a Raspberry pi that acted as a mediaplayer with pi_video_looper.

  The print_and_logg.py checks status from a projector thru serial and alerts by email if the projector is off, if the RPi is to hot, if the ram is running low or if the omxplayer isnt running.
  It also saves the data to a logg.txt file on the same place as the files are stored.

* The <b>relay_all_on.py</b> and <b>proj_on.py</b> is some automation examples, to turn on a projector or switch a serial connected relay (USB-RLY02) to closed state. (Projector hex code may vary)

* <b>musicbox.py</b> is for making a RPi act as a audio-player, witch plays a .wav file on button input.

* The <b>echo_client.py</b> and <b>echo_server.py</b> is examples for client/server connection.

* The <b>proj_on-off.py</b> is a little script that automates turning on and off two benq projectors, connected to one RaspberryPi. The file was in this case putted into the /boot/ folder of the RPi, and a cron job was running on the file every 3:d minute. I placed it there so it could be changed without having to connect the RPi to a network.
