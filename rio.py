import osmnx as ox
import matplotlib.pyplot as plt

place1 = "Ipanema, Rio de Janeiro, Brazil"
place2 = "Rocinha, Rio de Janeiro, Brazil"

print(f" Fetching street network for {place1}...")
g1 = ox.graph_from_place(place1, network_type='drive')
stats1 = ox.basic_stats(g1)
circuity1 = stats1['circuity_avg']

print(f"Fetching street network for {place2}...")
g2 = ox.graph_from_place(place2, network_type='walk')
stats2 = ox.basic_stats(g2)
circuity2 = stats2['circuity_avg']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))

ox.plot_graph(g1, ax=ax1, node_size=0, edge_color='#3399ff', edge_linewidth=1.2, show=False)
ax1.set_title(f"{place1}\nAverage Street Circuity: {circuity1:.3f}", fontsize=18)
ax1.axis('off') 

ox.plot_graph(g2, ax=ax2, node_size=0, edge_color='#ff5733', edge_linewidth=0.8, show=False)
ax2.set_title(f"{place2}\nAverage Street Circuity: {circuity2:.3f}", fontsize=18)
ax2.axis('off') 

fig.suptitle('Comparison', fontsize=24, y=0.98)
plt.savefig('rio_logistics_comparison.png', dpi=300, bbox_inches='tight')
plt.show()