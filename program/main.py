import ipaddress

class AdaptiveNetworkMonitoring:

    def __init__(self, network_name, current_router_models, candidate_router_models):
        self.network_name = network_name
        self.current_router_models = current_router_models
        self.candidate_router_models = candidate_router_models
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

    def __init__(self, router_name, router_ip, ssh_id, ssh_pass, netflow_exportermaps, netflow_monitormaps, netflow_samplermaps, interfaces):
        self.router_name = router_name
        self.router_ip = router_ip
        self.ssh_id = ssh_id
        self.ssh_pass = ssh_pass
        self.netflow_exportermaps = netflow_exportermaps
        self.netflow_monitormaps = netflow_monitormaps
        self.netflow_samplermaps = netflow_samplermaps
        self.interfaces = interfaces

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

    def __init__(self, netflow_exporter_name, collector_addr, collector_udp_port):
        self.netflow_exporter_name = netflow_exporter_name
        self.collector_addr = collector_addr
        self.collector_udp_port = collector_udp_port

class NetflowMonitorMap:

    def __init__(self, netflow_monitormap_name, num_chache, chache_timeout, netflowexportermap):
        self.netflow_monitormap_name = netflow_monitormap_name
        self.num_chache = num_chache
        self.chache_timeout = chache_timeout
        self.netflowexportermap = netflowexportermap

class SamplerMap:

    def __init__(self, samplermap_name, sampring_rate):
        self.samplermap_name = samplermap_name
        self.sampring_rate = sampring_rate

class Interface:

    def __init__(self, interface_name, samplermap, netflow_monitormap):
        self.interface_name =  interface_name
        self.samplermap =  samplermap
        self.netflow_monitormap = netflow_monitormap

if __name__ == "__main__":
    print("hello world")
