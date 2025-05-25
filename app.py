from app_components import clear_background

class TildaGone:
    def __init__(self):
        self.fade = 500

    def update(self, delta):
        self.fade = (self.fade - (delta / 20))
        if self.fade < 0:
            self.fade = 500

    def draw(self, ctx):
        clear_background(ctx)
        ctx.font_size = self.fade
        ctx.rgb(*(0.5, 0.5, 1.0)).move_to(0-(self.fade/4), 0 + (self.fade /4)).text("~")


__Background__ = TildaGone