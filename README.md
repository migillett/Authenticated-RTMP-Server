# Simple RTMP Server
A simple RTMP server using [NGINX](https://nginx.org/en/docs/). The server works by ingesting a RTMP feed and converts it into HLS. That converted HLS stream is then played on a static webpage using [video.js](https://videojs.com/)

## Setup (Shell Script)
1. Clone this repository using `git clone https://github.com/migillett/simple_rtmp_server.git`
2. Change directory using `cd ./simple_rtmp_server`
3. Login as root with `sudo su` and run the setup using `bash setup.sh` or run as your current user (with sudo privileges) using `sudo bash setup.sh`
4. The script will run and give you updates on each step.
5. The last step in the shell script will tell you to change the `[stream_key]` in the `/var/www/html/index.html` file. Change it to whatever stream key you'll be using to send your video.
6. Change the password in `/etc/nginx/nginx.conf` where it says `$arg_pwd = 'supersecretpassword'`. Change it to whatever you want, but keep it in mind. You'll need it later for OBS.
7. Using [OBS](https://obsproject.com/), connect to your server using the url `rtmp://[your server ip]/live` and the stream key `[stream key from step 5]$pwd=[password from step 6]`. Just make sure that your stream key matches what you set it up as in step 5. Then click "Start Streaming" in OBS.
8. Pull up your server's IP address in your favorite web browser and you're off to the races.
9. You may need to restart NGINX using `service nginx restart`.

## Setup (Docker)
1. Install docker and docker-compose
2. Clone the repository using `git clone https://github.com/migillett/simple_rtmp_server.git`
3. Change directory using `cd ./simple_rtmp_server`
4. Go into the `nginx.conf` file and change `$arg_pwd = 'supersecretpassword'` to whatever you want it to be (HOLD ON TO THIS).
5. Change the `[stream_key]` variable in the `/var/www/html/index.html` file. Change it to whatever stream key you'll be using to send your video.
6. Run `docker-compose build` to compile
7. Run `docker-compose up` to run the docker file
