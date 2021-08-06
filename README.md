# Simple RTMP Server
A simple RTMP server using [NGINX](https://nginx.org/en/docs/). The server works by ingesting a RTMP feed and converts it into HLS. That converted HLS stream is then played on a static webpage using [video.js](https://videojs.com/)

## Setup
1. Install docker and docker-compose
2. Clone the repository using `git clone https://github.com/migillett/simple_rtmp_server.git`
3. Run the script `hash.py` to set your stream password. Input a password and then copy what it gives you. Save this for the next step.
4. In `auth_server.py` paste the desired stream name (stream key) stream password from step 3 into the dictionary on line 12.
5. Run `docker-compose build && docker-compose up` to compile and run the containers.
6. Using [OBS](https://obsproject.com/), connect to your server using the url `rtmp://[your server ip]/live` and the stream key `[stream key from step 4]$pwd=[password from step 3]`. Then click "Start Streaming" in OBS.
7. Pull up the stream in VLC using the view network connection feature. Type in `http://[server_ip]/hls/[stream_name]/index.m3u8` and click play.
