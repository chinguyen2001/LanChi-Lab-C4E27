from youtube_dl import YoutubeDL

options = {
    'default_search': 'ytsearch', 
    'max_downloads': 1 
}
dl = YoutubeDL(options)
dl.download(['Natural - Imagine Dragons'])

options2 = {
    'default_search': 'ytsearch', 
    'max_downloads': 1 
}
dl = YoutubeDL(options2)
dl.download(['Young Blood 5 Seconds of Summer'])

options3 = {
    'default_search': 'ytsearch', 
    'max_downloads': 1 
}
dl = YoutubeDL(options3)
dl.download(['On My Way To You Cody Johnson'])


