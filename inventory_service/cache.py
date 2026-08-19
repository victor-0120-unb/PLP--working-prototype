# Stock cache

stock_cache = {}


def update_cache(inventory):
    """
    Updates the cache with the latest warehouse inventory.
    """
    global stock_cache
    stock_cache = inventory.copy()


def get_cached_stock(product_name):
    """
    Returns the cached quantity for a product.
    """
    product_name = product_name.strip().lower()

    if product_name in stock_cache:
        return stock_cache[product_name]

    return None


def get_all_cached_stock():
    """
    Returns all currently cached inventory.
    """
    return stock_cache.copy()