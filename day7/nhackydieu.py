from pygame import mixer  # Load the popular external library

mixer.init()
channel1 = mixer.Channel(0) # argument must be int
channel2 = mixer.Channel(1)
channel3 = mixer.Channel(2)
channel4 = mixer.Channel(3)
channel5 = mixer.Channel(4)
tieng_win = mixer.Sound('.\\day7\\mp3\\victory-mario-series-hq-super-smash-bros.mp3')
tieng_lose = mixer.Sound('.\\day7\\mp3\\noooo_3.mp3')
tieng_tra_loi = mixer.Sound('.\\day7\\mp3\\tieng-vo-tay.mp3')
tieng_tra_loi_sai = mixer.Sound('.\\day7\\mp3\\nmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm.mp3')
tieng_rung_ron = mixer.Sound('.\\day7\\mp3\\x-files-theme-song-copy.mp3')