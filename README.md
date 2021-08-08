# Simple RTMP Server
A simple RTMP server using [NGINX](https://nginx.org/en/docs/). The server works by ingesting a RTMP feed and converts it into HLS. That converted HLS stream is then played on a static webpage using [video.js](https://videojs.com/)

## Setup (Docker)
1. Install docker and docker-compose
2. Clone the repository using `git clone https://github.com/migillett/simple_rtmp_server.git`
3. Change directory using `cd ./simple_rtmp_server`
4. Run the setup.py program by running `python3 setup.py`. This will ask you for a stream name and password that you want hashed. You can create more than one stream name and password if you like. Save both the stream name and password for step 6. The passwords are hashed upon entry, so there is now way to recover them once submitted.
5. Run `docker-compose build && docker-compose up` to compile and run the docker containers.
6. Using [OBS](https://obsproject.com/), connect to your server using the url `rtmp://[your server ip]/live` and the stream key `[stream name from step 4]$pwd=[unhashed stream password from step 4]`. Just make sure that your stream key matches what you set it up as in step 6. Then click "Start Streaming" in OBS.

## Viewing the Stream
### VLC
You can view the stream using [VLC](https://www.videolan.org/vlc/) by going to Media > Open Network Stream... From there, you can paste in the following url to access it: `http://[your_server_ip]:8080/hls/[stream_name]/index.m3u8`

### Embedding into Websites
You can use [Video.JS](https://videojs.com/) to embed the video stream on your website. Just copy and paste their HTML template into your website and replace the src tag with the m3u8 stream url: `http://[your_server_ip]:8080/hls/[stream_name]/index.m3u8`.
