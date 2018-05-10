#!/usr/bin/env python
print("Content-type:text/html \n")
import media
import fresh_tomatoes
aashiqui2=media.Movie("ashiqui","aashiqui","http://i.ndtvimg.com/mt/movies/2013-04/asshiqui2-dramatic.jpg","https://www.youtube.com/embed/g4Tp8arzspw")
aashiqui=media.Movie("aashiqui2","ashiqui","https://i.ytimg.com/vi/Vj9rmKuim3M/maxresdefault.jpg","https://www.youtube.com/embed/KgsYJRnBNeE")
chennaiexpress=media.Movie("aashiqui","aashiqui","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTncJKHfE5Dkz7ZgEvYfHozAuLuSsSjCN2B8gB9M1Q7YwkCJs3wKg","https://www.youtube.com/embed/hZGR5Sj1Bfo")
premam=media.Movie("premem","premem","https://english.manoramaonline.com/content/dam/mm/en/entertainment/images/2016/May/29/premam-one-year.jpg.image.784.410.jpg",
                    "https://www.youtube.com/embed/H1-_SBacAKU")
baahubali=media.Movie("baahubali","baahubali","http://www.lovelytelugu.com/wp-content/uploads/2017/01/16298758_1322879227734849_6679850790624761842_n.jpg","https://www.youtube.com/embed/qD-6d8Wo3do")
movies=[aashiqui2,aashiqui,chennaiexpress,premam,baahubali]
fresh_tomatoes.open_movies_page(movies)

