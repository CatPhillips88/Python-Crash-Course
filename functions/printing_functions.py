from modules import engagement_ring_purchases as eg, shipped_rings as sr

ring_orders = ['canary yellow asscher', 'aquamarine pear', 'ruby heart', 'pink tourmaline oval']

completed_orders = []

eg(ring_orders, completed_orders)

sr(completed_orders)