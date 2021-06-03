from modules import engagement_ring_purchases, shipped_rings

ring_orders = ['canary yellow asscher', 'aquamarine pear', 'ruby heart', 'pink tourmaline oval']

completed_orders = []

engagement_ring_purchases(ring_orders, completed_orders)

shipped_rings(completed_orders)