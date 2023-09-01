from evonote import EvolverInstance

def save_cache():
    EvolverInstance.save_all_cache_to_file()

def discard_cache():
    EvolverInstance.discard_cache_update()

