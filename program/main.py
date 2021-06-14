
class AdaptiveNetworkMonitoring:
    network_name
    current_router_models
    candidate_router_models

    def __init__(self, routers_csv):
        return 0
    def currentize_router_models():
        return 0
    def show_current_netflow_monitoring_statuses():
        return 0
    def show_current_router_models():
        return 0
    def show_current_router_models():
        return 0
    def alluser_netflow_monitoring():
        return 0
    def golduser_netflow_monitoring():
        return 0
    def halt_netflow_monitoring():
        return 0
    def commit_candidate_router_models():
        return 0
    def acm_demo():
        return 0

class RouterModel:
    router_name
    router_ip
    ssh_id
    ssh_pass
    netflow_exportermaps
    netflow_monitormaps
    netflow_samplermaps
    interfaces

    def __init__(self, router_name, router_ip, ssh_id, ssh_pass, netflow_exportermaps, netflow_monitormaps, netflow_samplermaps, interfaces)
        return 0
    def currentize_router_model():
        return 0
    def get_runnning_netflow_configuration():
        return 0
    def get_runnning_netflow_configuration():
        return 0
    def parse_netflow_configuration(netflow_configuration):
        return 0
    def show_current_netflow_monitoring_status():
        return 0
    def show_router_model():
        return 0
    def clear_netflow_monitoring():
        return 0
    def commit_router_model():
        return 0

class NetflowExporterMap:
      netflow_exporter_name
      collector_addr
      collector_udp_port

    def __init__(self, netflow_exporter_name, collector_addr, collector_udp_port):
        return 0

class NetflowMonitorMap:
      netflow_monitormap_name
      num_chache
      chache_timeout
      netflowexportermap

    def __init__(self, netflow_monitormap_name, num_cache, chache_timeout, netflowexportermap):
        return 0

class NetflowMonitorMap:
    interface_name
    samplermap
    netflow_monitormap

    def __init__(self, interface_name, samplermap, netflow_monitormap):
        return 0

if __name__ == "__main__":
    print("hello world")
