from IPython.display import HTML
from matplotlib.animation import Animation


def render_animation_video(animation: Animation):
    return HTML(animation.to_html5_video())


def render_animation_image(animation: Animation):
    writer = PillowWriter(fps=24, bitrate=1800)

    with NamedTemporaryFile(suffix=".gif") as temp:
        animation.save(temp.name, writer=writer)
        gif = Image(data=open(temp.name, "rb").read(), format="gif")
