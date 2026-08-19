from flask import Flask, jsonify

from inventory_service.cache import get_cached_stock, get_all_cached_stock
from inventory_service.service import poll_warehouse


app = Flask(__name__)


@app.route("/inventory/<product_name>", methods=["GET"])
def get_inventory(product_name):
    """Return cached stock for one product."""

    stock = get_cached_stock(product_name)

    if stock is None:
        return jsonify({
            "product": product_name,
            "message": "Product not found in cache"
        }), 404

    return jsonify({
        "product": product_name.strip().lower(),
        "quantity": stock
    })


@app.route("/inventory", methods=["GET"])
def get_all_inventory():
    """Return all inventory currently in the cache."""

    return jsonify(get_all_cached_stock())


@app.route("/refresh", methods=["POST"])
def refresh_inventory():
    """Manually trigger a warehouse poll."""

    poll_warehouse()

    return jsonify({
        "message": "Inventory cache updated successfully"
    })


if __name__ == "__main__":
    # Load initial warehouse data into the cache.
    poll_warehouse()

    app.run(debug=True)