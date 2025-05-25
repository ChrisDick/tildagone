from app_components import clear_background


class TildaGone:
    def __init__(self):
        self.fade = 20

    def update(self, delta):
        self.fade = self.fade - (delta / 100)
        if self.fade < 0:
            self.fade = 0

    def draw(self, ctx):
        clear_background(ctx)
        ctx.save()
        ctx.font_size = self.fade
        ctx.text_align = ctx.LEFT
        ctx.text_baseline = ctx.TOP
        ctx.rgb()
        ctx.text("~")
        ctx.restore()


__Background__ = TildaGone
