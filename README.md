# Simple RTMP Server
A simple RTMP server using [NGINX](https://nginx.org/en/docs/). The server works by ingesting a RTMP feed and converts it into HLS. That converted HLS stream is then played on a static webpage using [video.js](https://videojs.com/)

## Setup (Docker)
1. Install docker and docker-compose
2. Clone the repository using `git clone https://github.com/migillett/simple_rtmp_server.git`
3. Change directory using `cd ./simple_rtmp_server`
4. Run the hash.py program by running `python3 ./auth/hash.py`. This will ask you for a stream password that you want hashed. Paste it when requested to do so. Save the unhashed password for later.
5. Copy and paste the hashed stream password into the valid_keys.py file replacing the current stream key.
6. Change the `[stream_key]` variable in the `/var/www/html/index.html` file. Change it to whatever stream key you'll be using to send your video.
7. Run `docker-compose build` to compile
8. Run `docker-compose up` to run the docker file
9. Using [OBS](https://obsproject.com/), connect to your server using the url `rtmp://[your server ip]/live` and the non-hashed stream key `[stream key from step 6]$pwd=[password from step 4]`. Just make sure that your stream key matches what you set it up as in step 6. Then click "Start Streaming" in OBS.
10. Pull up your server's IP address in your favorite web browser and you're off to the races.
