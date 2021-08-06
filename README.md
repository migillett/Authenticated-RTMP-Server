# Simple RTMP Server
A simple RTMP server using [NGINX](https://nginx.org/en/docs/). The server works by ingesting a RTMP feed and converts it into HLS. That converted HLS stream is then played on a static webpage using [video.js](https://videojs.com/)

## Setup (Docker)
1. Install docker and docker-compose
2. Clone the repository using `git clone https://github.com/migillett/simple_rtmp_server.git`
3. Change directory using `cd ./simple_rtmp_server`
4. Run the hash.py program by running `python3 setup.py`. This will ask you for a stream name and password that you want hashed. Paste it when requested to do so. Save the unhashed password for later.
5. Run `docker-compose build && docker-compose up` to compile and run the docker containers.
6. Using [OBS](https://obsproject.com/), connect to your server using the url `rtmp://[your server ip]/live` and the stream key `[stream name from step 6]$pwd=[unhashed stream password from step 4]`. Just make sure that your stream key matches what you set it up as in step 6. Then click "Start Streaming" in OBS.
10. Pull up your server's IP address in your favorite web browser and you're off to the races.
