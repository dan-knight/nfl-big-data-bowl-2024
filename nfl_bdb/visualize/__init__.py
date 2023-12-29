from IPython.display import HTML
from matplotlib.animation import Animation


def render_animation_video(animation: Animation):
    return HTML(animation.to_html5_video())
