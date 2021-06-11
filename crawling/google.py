from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"사자,호랑이,고양이,고라니,두더지,판다,나무늘보,사슴,강아지,토끼,여우,다람쥐,북극곰,코알라,너구리,반달가슴곰,코끼리,사막여우,오리,닭,원숭이,악어,뱀,스컹크,펭귄,수달,오소리,청설모,곰,치타,기린,캥거루,미어캣,햄스터,돼지,고슴도치,늑대,라마,낙타,쿼카,기니피그,친칠라,페럿","limit":50,"print_urls":True,"format":"jpg"}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images