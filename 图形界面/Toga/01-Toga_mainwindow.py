"""
A little app to show my meeting history with her
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import datetime


class MeetHistory(toga.App):

    def __init__(
            self,
            formal_name=None,
            app_id=None,
            app_name=None,
            id=None,
            icon=None,
            author=None,
            version=None,
            home_page=None,
            description=None,
            startup=None,
            windows=None,
            on_exit=None,
            factory=None,
    ):
        super().__init__(formal_name, app_id, app_name, id, icon, author, version, home_page, description, startup,
                         windows, on_exit, factory)
        self.output = None

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN,color='pink', background_color='pink'))
        hbox = toga.Box(style=Pack(flex=1, direction=ROW, height=50))
        # hbox.parent = main_box
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.meetText()
        self.label = toga.Label(self.output, style=Pack(padding=(50, 5),
                                                   color='red',
                                                   font_size=20,
                                                   alignment='center',
                                                   text_align='center'))
        self.label.style.update()

        banner = toga.ImageView(image=r'resources/bannert.jpg', style=Pack( alignment='top'))

        image = toga.ImageView(style=Pack(height=500, alignment='left'))
        image.image = r'resources/couple2.jpg'
        # image.style.update(Pack())
        # print(image.style.IntrinsicSize.height)


        btn = toga.Button('update', style=Pack(font_size=12, height=50, flex=1, direction=ROW, alignment= 'center'), on_press=self.update)
        btn2 = toga.Button('quit', style=Pack(font_size=12, height=50, flex=1, direction = COLUMN, alignment= 'center'), on_press=self.quit)
        # main_box.add(banner)
        main_box.add(self.label)
        hbox.add(btn)
        hbox.add(btn2)

        main_box.add(image)
        main_box.add(hbox)
        # print(main_box.children)

        self.main_window.content = main_box

        self.main_window.show()

    def meetText(self):
        meet = datetime.datetime(2020, 4, 6, 18, 0, 0)
        history = datetime.datetime.now() - meet
        days = history.days
        seconds = history.seconds
        hours = seconds // 3600
        minutes = seconds % 3600 // 60
        second = seconds % 60
        self.output = f'我和亲爱的老公大人已相识\n  ❤{days}天{hours}小时{minutes}分{second}秒❤'

    def update(self, button):
        meet = datetime.datetime(2020, 4, 6, 18, 0, 0)
        history = datetime.datetime.now() - meet
        days = history.days
        seconds = history.seconds
        hours = seconds // 3600
        minutes = seconds % 3600 // 60
        second = seconds % 60
        self.output = f'我和亲爱的老婆大人已相识\n  ❤{days}天{hours}小时{minutes}分{second}秒❤'
        self.label.text = self.output
        self.label.refresh()


    def quit(self, button):
        self.exit()

def main():
    return MeetHistory('Meet History', '123', icon='resources/sakuran.ico')


if __name__ == '__main__':
    main().main_loop()