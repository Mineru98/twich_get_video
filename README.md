# twich_get_video

```shell
# 알파채널 허용 렌더링
./ffmpeg -i LandingPageScroll_3.mov -c:v libvpx-vp9 -vf "colorkey=0x000000:0.1:0.1,format=yuva420p" data_3.webm
# mov to mp4
./ffmpeg -i LandingPageScroll_3.mov -qscale 0 LandingPageScroll_3.mp4

# 재생속도 4배 빠르게
./ffmpeg -i LandingPageScroll_3.mov -vf "setpts=(1/4)*PTS" -an LandingPageScroll_3.mp4
# 재생속도 4배 느리게
./ffmpeg -i LandingPageScroll_3.mov -vf "setpts=(4/1)*PTS" -an LandingPageScroll_3.mp4
```
