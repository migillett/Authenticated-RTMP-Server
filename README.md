# Simple RTMP Server
A simple RTMP server using [NGINX](https://nginx.org/en/docs/). The server works by ingesting a RTMP feed and converts it into HLS. That converted HLS stream is then played on a static webpage using [video.js](https://videojs.com/)

## Setup How-To
1. Clone this repository using `git clone https://github.com/migillett/simple_rtmp_server.git`
2. Change directory using `cd ./simple_rtmp_server`
3. Login as root with `sudo su` and run the setup using `bash setup.sh` or run as your current user (with sudo privileges) using `sudo bash setup.sh`
4. The script will run and give you updates on each step.
5. The last step in the shell script will tell you to change the `[stream_key]` in the `/var/www/html/index.html` file. Change it to whatever stream key you'll be using to send your video.
6. Using [OBS](https://obsproject.com/), connect to your server using the url `rtmp://[your server ip]/live` and a stream key of your choice (just make sure it matches the `index.html` stream key in step 9.
7. Pull up your server's IP address in your favorite web browser and you're off to the races.
8. You may need to restart NGINX using `service nginx restart`.

## Upcoming updates
This is still in the early stages, but I plan to implement a python authentication server. That's coming soon-ish.
