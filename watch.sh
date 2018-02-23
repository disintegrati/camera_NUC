#!/bin/bash
inotifywait -m /home/nuc/Scrivania/camera/video -e create -e moved_to |
    while read path action file; do
        echo "The file '$file' appeared in directory '$path' via '$action'"
        # do something with the file
        sleep 15
        curl -i -X POST -F "url=@/home/nuc/Scrivania/camera/video/$file" -F "caption=video_upload" -F "published=true" -F "access_token=EAASJMHw5q08BABKRCzzeLQ8ftneyRw9j1jTc3vwGrDtFfI5wUwmYVjUZAHm1O3PZBaRCm3wnCTIH85SPjoXem3w8aHWf3jJ6wZC8v3HnKfqxwpTufEEa8kq76FHczvoyK4tzIY6xI9lXre1vY8CjCaGqdYA3Gq04XQZCGerKoQZDZD" "https://graph.facebook.com/v2.10/1736575526639458/videos"
    done
