from slackbot.bot import Bot
import kbase


def main():
    kbase.init()
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
