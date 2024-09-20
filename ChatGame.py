import asyncio
from twitchio.ext import commands
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time

keyboard = KeyboardController()
mouse = MouseController()


# Twitch Bot Setup
class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token='Insert your token here', prefix='!',
                         initial_channels=['Insert Channel Name here'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        print(message.content)
        await self.handle_commands(message)
        handle_chat_message(message.content)

# Function to simulate key press
def press_key(key):
    keyboard.press(key)
    time.sleep(0.2)
    keyboard.release(key)

def left_click():
    mouse.click(Button.left)

# Function to handle chat messages
def handle_chat_message(message):
    # Normalize the message content
    normalized_message = message.strip().lower()
    
    if normalized_message == "walk forward":
        press_key('w')
    elif normalized_message == "walk backward":
        press_key('s')
    elif normalized_message == "walk left":
        press_key('a')
    elif normalized_message == "walk right":
        press_key('d')
    elif normalized_message == "dodge":
        press_key(Key.space)
    elif normalized_message == "jump":
        press_key('f')
    elif normalized_message == "lockon":
        press_key('q')
    elif normalized_message == "use item":
        press_key('r')
    elif normalized_message == "interact":
        press_key('e')
    elif normalized_message == "map":
        press_key('g')
    elif normalized_message == "look up":
        press_key('1')
    elif normalized_message == "look down":
        press_key('2')
    elif normalized_message == "look left":
        press_key('3')
    elif normalized_message == "look right":
        press_key('4')
    elif normalized_message == "light attack":
        left_click()
    elif normalized_message == "heavy attack":
        press_key('8')
    elif normalized_message == "block":
        press_key('5')
    elif normalized_message == "skill":
        press_key('6')
    elif normalized_message == "reset camera":
        press_key('*')
    elif normalized_message == "up":
        press_key(Key.up)
    elif normalized_message == "down":
        press_key(Key.down)
    elif normalized_message == "right":
        press_key(Key.right)
    elif normalized_message == "left":
        press_key(Key.left)
    elif normalized_message == "menu":
        press_key(Key.esc)
    elif normalized_message == "switch magic":
        press_key('m')
    elif normalized_message == "switch item":
        press_key('i')
    elif normalized_message == "switch righthand weapon":
        press_key('0')
    elif normalized_message == "switch lefthand weapon":
        press_key('y')
    elif normalized_message == "exit":
        press_key(Key.backspace)
    elif normalized_message == "select":
        press_key(Key.enter)

bot = Bot()

if __name__ == "__main__":
    bot.run()
