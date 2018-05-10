#!/usr/bin/env python
print("Content-type:text/html \n")
import webbrowser
import os
import re
main_page_head='''
<html>
<head>
    <title>MOVIE TRAILER</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .container {
            display:inline-block;
            flex-wrap: wrap;
            display: flex;
            flex: 0%;
            /*justify-content: center;*/
            margin-top:50px;
        }

        body {
            margin:20px;
        }
        
       img{
            height: 300px;
            width: 300px;
            border:2px solid #023131;
            padding-left:50px;
            padding-bottom:50px;
            padding-right:50px;
            padding-top:50px;
          }
   img:hover{
            
        
            visibility: visible;
            cursor: pointer;
            border-radius:5%;
            padding-left:50px;
            padding-bottom:50px;
            padding-right:50px;
            padding-top:50px;
            background-color:pink;
          }

        
    </style>
    <script src="https://code.jquery.com/jquery-1.12.3.min.js" integrity="sha256-aaODHAgvwQW1bFOGXMeX+pC4PZIPsvn2h1sArYOhgXQ="
        crossorigin="anonymous"></script>
        <link href="https://fonts.googleapis.com/css?family=Courgette" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet" type="text/css" />
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    <script>
        $(document).ready(function () {
            $("#myVideo").on("hidden.bs.modal", function () {
                $("#myframeX").attr("src", "#");
            })
        })
        function changeVideo(vId) {
            var iframe = document.getElementById("myframeY");
            iframe.src = "https://www.youtube.com/embed/" + vId;
            $("#myVideo").modal("show");
        }
    </script>
</head>
'''
main_page_content='''
<body>
    <main>
        <div class="container">
           <div onclick="changeVideo('eHRrZ5DQCV4')">
	
		<img src = "http://i.ndtvimg.com/mt/movies/2013-04/asshiqui2-dramatic.jpg" alt = "AAshiqui2" width = "600px" height = "300px">
	
</div>
<div onclick="changeVideo('KgsYJRnBNeE')" >
	
		<img src = "https://i.ytimg.com/vi/Vj9rmKuim3M/maxresdefault.jpg" alt = "AAshiqui" width = "600px" height = "300px">
	</div>
<div onclick="changeVideo('hZGR5Sj1Bfo')">
	 <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTncJKHfE5Dkz7ZgEvYfHozAuLuSsSjCN2B8gB9M1Q7YwkCJs3wKg" alt = "chennaiexpress" width = "600px" height = "300px">
	</a>
        </div>
        <div onclick="changeVideo('H1-_SBacAKU')">
	<img src = "https://english.manoramaonline.com/content/dam/mm/en/entertainment/images/2016/May/29/premam-one-year.jpg.image.784.410.jpg" alt = "PREMAM" width = "600px" height = "300px">
          </div>
          <div onclick="changeVideo('qD-6d8Wo3do')">
          <img src = "http://www.lovelytelugu.com/wp-content/uploads/2017/01/16298758_1322879227734849_6679850790624761842_n.jpg" alt =     "BAAHUBALI2" width = "600px" height = "300px">
</div>	
               
            </div>  
        </div>       
        <div class="modal fade" id="myVideo" tabindex="-1" role="biography" aria-labelledby="myModalLabel">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-body">
                        <iframe id="myframeY" width="550" height="350" src="" frameborder="0" allowfullscreen></iframe>
                    </div>
                    <div class="close-button">
                       <button type="button" style="background-color:red" class="btn btn-default" data-dismiss="modal">X</button>
                    </div>
                </div>
            </div>
        </div>
    </main>
</body>
</html>
'''
movie_title_content='''
<div class="col-md-6 col-lg-4 movie-title text-center" data-trailer-youtube-id="{trailer_youtube_id} data-toggle="modal" data-target="#trailer">
     <img src="{poster_image_url}" width="220" height="342">
     <h2 style="color:white;">{movie_title}</h2>
</div>
'''
def create_movie_titles_content(movies):
      content=''
      for movie in movies:
          youtube_id_match=re.search(r'(?<=v=)[^&#]+',movie.trailer_youtube_url)
          youtube_id_match=youtube_id_match or re.search(r'(?<=v=)[^&#]+',movie.trailer_youtube_url)
          trailer_youtube_id=(youtube_id_match.group(0) if youtube_id_match else None)
          content+=movie_title_content.format(movie_title=movie.title,poster_image_url=movie.poster_image_url,trailer_youtube_id=movie.trailer_youtube_url)
      return content
def open_movies_page(movies):
    output_file=open('fresh_tomatoes.html','w') 
    rendered_content=main_page_content.format(movie_tiles=create_movie_titles_content (movies))                                                             
    output_file.write(main_page_head+rendered_content)
    output_file.close()
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)





