import requests,time
i=0
j=274142303
while(i!=1):

    f=open("suntv.m3u8",'w')
    f.write("#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-MEDIA-SEQUENCE:0\n#EXT-X-ALLOW-CACHE:YES\n#EXT-X-TARGETDURATION:13\n")
#EXT-X-TARGETDURATION:13
    i=0
    for i in range(j,j+1):
        if(i==20):
            break
        else:
            f.write("https://suntvlive.s.llnwi.net/SunTVHD/SunTVHD.isml/SunTVHD-audio_1=64000-video=2499968-"+str(i)+".ts\n")
            f.write('#EXTINF:12.080000,\n')
            i+=1
    f.write("#EXT-X-ENDLIST")
    f.close()
    j=j+1
    time.sleep(5) 
    print(1)
