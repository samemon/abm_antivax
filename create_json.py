# This file will take in nodes and edges file and create json out of it


nodes = map(lambda l: l.rstrip().split(","), open("nodes_er_close.ctl"))
edges = map(lambda l: l.rstrip().split(","), open("result_edges_far.ctl"))

json_string = '{"nodes":['


for node in nodes:
	b = node[1]
	b = str(int(b) + 1)
	json_string = json_string + '{"group":'+b+',"name":'+node[0]+'},'

json_string = json_string[:-1]+'],"links":['

for edge in edges:
	f = edge[0]
	t = edge[1]
	json_string = json_string + '{"source":' + f + ', "target":' + t + ',"value":157},'

json_string = json_string[:-1] + ']}' 
print(json_string)

