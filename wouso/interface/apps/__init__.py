from wouso.core.magic.models import Bazaar
from wouso.interface.apps.messaging.models import MessageApp
from wouso.interface.activity.achievements import Achievements

def get_apps():
    """ Same as wouso.core.game.get_games
    """
    return MessageApp, Bazaar, Achievements