from instabot import Bot
user=input("Enter username")
bot=Bot()
bot.login(username="sasta_hacker1010",password="your password")
bot.follow(user)
bot.upload_photo("C:/Users/ACER/Desktop/me.jpg",caption="i love python")
bot.send_message("i love python",["being_chanchal.tripathi"])
followers=bot.get_user_followers("sasta_hacker1010")
for follower in followers:
    print(bot.get_user_info(follower))
following=bot.get_user_following("sasta_hacker1010")
for Following in following:
    print(bot.get_user_info(Following))

