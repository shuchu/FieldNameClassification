from textdistance import DamerauLevenshtein

dl = DamerauLevenshtein()


kd = {"Domain": ["domain", "dest_domain", "destination_domain","d_domain", "src_domain", "source_domain", "s_domain","query.hostname"],
"SourceIPv4Address": ["src_ip", "source_ip", "s_ip", "src_endpoint.ip", "device.ip"],
"DestinationIPv4Address": ["dest_ip", "destination_ip", "d_ip", "dst_endpoint.ip"],
"IPv4Address": ["src_ip", "source_ip", "s_ip", "src_endpoint.ip", "device.ip", "dest_ip", "destination_ip", "d_ip", "dst_endpoint.ip"],
"ProcessName": ["process_name", "proc_name", "Image", "process.name","process.file.name"],
}

query_str = 'destination_source_ip'
most_sim_field = ''
min_dist = 100
for key in kd:
    print(key)
    for val in kd[key]:
        d = dl.distance(query_str, val)
        d_nm = d / max(len(query_str), len(val))
        if d_nm < min_dist:
            min_dist = d_nm
            most_sim_field = val

        print("{}:{}".format(val, d))
    print("=====")

print('Most similar field is: {} with normalized distance: {}'.format(most_sim_field, min_dist))
    
