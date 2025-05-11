import fastf1
from definitions import ROOT_DIR
import os

fastf1.Cache.enable_cache(os.path.join(ROOT_DIR, 'f1cache'))
