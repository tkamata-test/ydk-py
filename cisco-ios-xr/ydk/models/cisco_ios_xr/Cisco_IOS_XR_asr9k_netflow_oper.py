""" Cisco_IOS_XR_asr9k_netflow_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-netflow package operational data.

This module contains definitions
for the following management objects\:
  net\-flow\: NetFlow operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class NfmgrFemEdmExpVerEnum(Enum):
    """
    NfmgrFemEdmExpVerEnum

    Netflow export version

    .. data:: v9 = 0

    	Version 9 export format

    .. data:: ip_fix = 1

    	IPFIX export format

    """

    v9 = 0

    ip_fix = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
        return meta._meta_table['NfmgrFemEdmExpVerEnum']


class NfmgrFemEdmTransProtoEnum(Enum):
    """
    NfmgrFemEdmTransProtoEnum

    Netflow export transport protocol

    .. data:: unspecified = 0

    	Unspecified transport protocol

    .. data:: udp = 1

    	UDP transport protocol

    """

    unspecified = 0

    udp = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
        return meta._meta_table['NfmgrFemEdmTransProtoEnum']



class NetFlow(object):
    """
    NetFlow operational data
    
    .. attribute:: configuration
    
    	NetFlow configuration information
    	**type**\:   :py:class:`Configuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Configuration>`
    
    .. attribute:: statistics
    
    	Node\-specific NetFlow statistics information
    	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics>`
    
    

    """

    _prefix = 'asr9k-netflow-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.configuration = NetFlow.Configuration()
        self.configuration.parent = self
        self.statistics = NetFlow.Statistics()
        self.statistics.parent = self


    class Configuration(object):
        """
        NetFlow configuration information
        
        .. attribute:: flow_exporter_maps
        
        	Flow exporter map configuration information
        	**type**\:   :py:class:`FlowExporterMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Configuration.FlowExporterMaps>`
        
        .. attribute:: flow_monitor_maps
        
        	Flow monitor map configuration information
        	**type**\:   :py:class:`FlowMonitorMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Configuration.FlowMonitorMaps>`
        
        .. attribute:: flow_sampler_maps
        
        	Flow sampler map configuration information
        	**type**\:   :py:class:`FlowSamplerMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Configuration.FlowSamplerMaps>`
        
        

        """

        _prefix = 'asr9k-netflow-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.flow_exporter_maps = NetFlow.Configuration.FlowExporterMaps()
            self.flow_exporter_maps.parent = self
            self.flow_monitor_maps = NetFlow.Configuration.FlowMonitorMaps()
            self.flow_monitor_maps.parent = self
            self.flow_sampler_maps = NetFlow.Configuration.FlowSamplerMaps()
            self.flow_sampler_maps.parent = self


        class FlowExporterMaps(object):
            """
            Flow exporter map configuration information
            
            .. attribute:: flow_exporter_map
            
            	Flow exporter map information
            	**type**\: list of    :py:class:`FlowExporterMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Configuration.FlowExporterMaps.FlowExporterMap>`
            
            

            """

            _prefix = 'asr9k-netflow-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.flow_exporter_map = YList()
                self.flow_exporter_map.parent = self
                self.flow_exporter_map.name = 'flow_exporter_map'


            class FlowExporterMap(object):
                """
                Flow exporter map information
                
                .. attribute:: exporter_name  <key>
                
                	Exporter name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: collector
                
                	Export collector array
                	**type**\: list of    :py:class:`Collector <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Collector>`
                
                .. attribute:: id
                
                	Unique ID in the global flow exporter ID space
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: name
                
                	Name of the flow exporter map
                	**type**\:  str
                
                .. attribute:: version
                
                	Export version data
                	**type**\:   :py:class:`Version <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version>`
                
                

                """

                _prefix = 'asr9k-netflow-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.exporter_name = None
                    self.collector = YList()
                    self.collector.parent = self
                    self.collector.name = 'collector'
                    self.id = None
                    self.name = None
                    self.version = NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version()
                    self.version.parent = self


                class Version(object):
                    """
                    Export version data
                    
                    .. attribute:: ipfix
                    
                    	ipfix
                    	**type**\:   :py:class:`Ipfix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version.Ipfix>`
                    
                    .. attribute:: version
                    
                    	version
                    	**type**\:   :py:class:`NfmgrFemEdmExpVerEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NfmgrFemEdmExpVerEnum>`
                    
                    .. attribute:: version9
                    
                    	version9
                    	**type**\:   :py:class:`Version9 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version.Version9>`
                    
                    

                    """

                    _prefix = 'asr9k-netflow-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ipfix = NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version.Ipfix()
                        self.ipfix.parent = self
                        self.version = None
                        self.version9 = NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version.Version9()
                        self.version9.parent = self


                    class Version9(object):
                        """
                        version9
                        
                        .. attribute:: common_template_export_timeout
                        
                        	Common template export timeout in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: data_template_export_timeout
                        
                        	Data template export timeout in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: interface_table_export_timeout
                        
                        	Interface table export timeout in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: options_template_export_timeout
                        
                        	Options template export timeout in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: sampler_table_export_timeout
                        
                        	Sampler table export timeout in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: vrf_table_export_timeout
                        
                        	VRF table export timeout in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'asr9k-netflow-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.common_template_export_timeout = None
                            self.data_template_export_timeout = None
                            self.interface_table_export_timeout = None
                            self.options_template_export_timeout = None
                            self.sampler_table_export_timeout = None
                            self.vrf_table_export_timeout = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-netflow-oper:version9'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.common_template_export_timeout is not None:
                                return True

                            if self.data_template_export_timeout is not None:
                                return True

                            if self.interface_table_export_timeout is not None:
                                return True

                            if self.options_template_export_timeout is not None:
                                return True

                            if self.sampler_table_export_timeout is not None:
                                return True

                            if self.vrf_table_export_timeout is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                            return meta._meta_table['NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version.Version9']['meta_info']


                    class Ipfix(object):
                        """
                        ipfix
                        
                        .. attribute:: common_template_export_timeout
                        
                        	Common template export timeout in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: data_template_export_timeout
                        
                        	Data template export timeout in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: interface_table_export_timeout
                        
                        	Interface table export timeout in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: options_template_export_timeout
                        
                        	Options template export timeout in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: sampler_table_export_timeout
                        
                        	Sampler table export timeout in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: vrf_table_export_timeout
                        
                        	VRF table export timeout in seconds
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'asr9k-netflow-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.common_template_export_timeout = None
                            self.data_template_export_timeout = None
                            self.interface_table_export_timeout = None
                            self.options_template_export_timeout = None
                            self.sampler_table_export_timeout = None
                            self.vrf_table_export_timeout = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-netflow-oper:ipfix'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.common_template_export_timeout is not None:
                                return True

                            if self.data_template_export_timeout is not None:
                                return True

                            if self.interface_table_export_timeout is not None:
                                return True

                            if self.options_template_export_timeout is not None:
                                return True

                            if self.sampler_table_export_timeout is not None:
                                return True

                            if self.vrf_table_export_timeout is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                            return meta._meta_table['NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version.Ipfix']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-netflow-oper:version'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.ipfix is not None and self.ipfix._has_data():
                            return True

                        if self.version is not None:
                            return True

                        if self.version9 is not None and self.version9._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                        return meta._meta_table['NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version']['meta_info']


                class Collector(object):
                    """
                    Export collector array
                    
                    .. attribute:: destination_address
                    
                    	Destination IPv4 address in AAA.BBB.CCC.DDD format
                    	**type**\:  str
                    
                    .. attribute:: destination_port
                    
                    	Transport destination port number
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: dscp
                    
                    	DSCP
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    .. attribute:: source_address
                    
                    	Source IPv4 address in AAA.BBB.CCC.DDD format
                    	**type**\:  str
                    
                    .. attribute:: source_interface
                    
                    	Source interface name
                    	**type**\:  str
                    
                    .. attribute:: transport_protocol
                    
                    	Transport protocol
                    	**type**\:   :py:class:`NfmgrFemEdmTransProtoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NfmgrFemEdmTransProtoEnum>`
                    
                    .. attribute:: vrf_name
                    
                    	VRF name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'asr9k-netflow-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.destination_address = None
                        self.destination_port = None
                        self.dscp = None
                        self.source_address = None
                        self.source_interface = None
                        self.transport_protocol = None
                        self.vrf_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-netflow-oper:collector'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.destination_address is not None:
                            return True

                        if self.destination_port is not None:
                            return True

                        if self.dscp is not None:
                            return True

                        if self.source_address is not None:
                            return True

                        if self.source_interface is not None:
                            return True

                        if self.transport_protocol is not None:
                            return True

                        if self.vrf_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                        return meta._meta_table['NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Collector']['meta_info']

                @property
                def _common_path(self):
                    if self.exporter_name is None:
                        raise YPYModelError('Key property exporter_name is None')

                    return '/Cisco-IOS-XR-asr9k-netflow-oper:net-flow/Cisco-IOS-XR-asr9k-netflow-oper:configuration/Cisco-IOS-XR-asr9k-netflow-oper:flow-exporter-maps/Cisco-IOS-XR-asr9k-netflow-oper:flow-exporter-map[Cisco-IOS-XR-asr9k-netflow-oper:exporter-name = ' + str(self.exporter_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.exporter_name is not None:
                        return True

                    if self.collector is not None:
                        for child_ref in self.collector:
                            if child_ref._has_data():
                                return True

                    if self.id is not None:
                        return True

                    if self.name is not None:
                        return True

                    if self.version is not None and self.version._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                    return meta._meta_table['NetFlow.Configuration.FlowExporterMaps.FlowExporterMap']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-asr9k-netflow-oper:net-flow/Cisco-IOS-XR-asr9k-netflow-oper:configuration/Cisco-IOS-XR-asr9k-netflow-oper:flow-exporter-maps'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.flow_exporter_map is not None:
                    for child_ref in self.flow_exporter_map:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                return meta._meta_table['NetFlow.Configuration.FlowExporterMaps']['meta_info']


        class FlowMonitorMaps(object):
            """
            Flow monitor map configuration information
            
            .. attribute:: flow_monitor_map
            
            	Flow monitor map information
            	**type**\: list of    :py:class:`FlowMonitorMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Configuration.FlowMonitorMaps.FlowMonitorMap>`
            
            

            """

            _prefix = 'asr9k-netflow-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.flow_monitor_map = YList()
                self.flow_monitor_map.parent = self
                self.flow_monitor_map.name = 'flow_monitor_map'


            class FlowMonitorMap(object):
                """
                Flow monitor map information
                
                .. attribute:: monitor_name  <key>
                
                	Monitor name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: cache_active_timeout
                
                	Cache active flow timeout in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: cache_aging_mode
                
                	Aging mode for flow cache
                	**type**\:  str
                
                .. attribute:: cache_inactive_timeout
                
                	Cache inactive flow timeout in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: cache_max_entry
                
                	Max num of entries in flow cache
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: cache_timeout_rate_limit
                
                	Maximum number of entries to age each second
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: cache_update_timeout
                
                	Cache update timeout in seconds
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: exporter
                
                	Name of the flow exporters used by the flow monitor
                	**type**\: list of    :py:class:`Exporter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Configuration.FlowMonitorMaps.FlowMonitorMap.Exporter>`
                
                .. attribute:: id
                
                	Unique ID in the global flow monitor ID space
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: name
                
                	Name of the flow monitor map
                	**type**\:  str
                
                .. attribute:: number_of_labels
                
                	Number of MPLS labels in key
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: options
                
                	Options applied to the flow monitor
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: record_map
                
                	Name of the flow record map
                	**type**\:  str
                
                

                """

                _prefix = 'asr9k-netflow-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.monitor_name = None
                    self.cache_active_timeout = None
                    self.cache_aging_mode = None
                    self.cache_inactive_timeout = None
                    self.cache_max_entry = None
                    self.cache_timeout_rate_limit = None
                    self.cache_update_timeout = None
                    self.exporter = YList()
                    self.exporter.parent = self
                    self.exporter.name = 'exporter'
                    self.id = None
                    self.name = None
                    self.number_of_labels = None
                    self.options = None
                    self.record_map = None


                class Exporter(object):
                    """
                    Name of the flow exporters used by the flow
                    monitor
                    
                    .. attribute:: name
                    
                    	Exporter name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'asr9k-netflow-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-netflow-oper:exporter'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                        return meta._meta_table['NetFlow.Configuration.FlowMonitorMaps.FlowMonitorMap.Exporter']['meta_info']

                @property
                def _common_path(self):
                    if self.monitor_name is None:
                        raise YPYModelError('Key property monitor_name is None')

                    return '/Cisco-IOS-XR-asr9k-netflow-oper:net-flow/Cisco-IOS-XR-asr9k-netflow-oper:configuration/Cisco-IOS-XR-asr9k-netflow-oper:flow-monitor-maps/Cisco-IOS-XR-asr9k-netflow-oper:flow-monitor-map[Cisco-IOS-XR-asr9k-netflow-oper:monitor-name = ' + str(self.monitor_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.monitor_name is not None:
                        return True

                    if self.cache_active_timeout is not None:
                        return True

                    if self.cache_aging_mode is not None:
                        return True

                    if self.cache_inactive_timeout is not None:
                        return True

                    if self.cache_max_entry is not None:
                        return True

                    if self.cache_timeout_rate_limit is not None:
                        return True

                    if self.cache_update_timeout is not None:
                        return True

                    if self.exporter is not None:
                        for child_ref in self.exporter:
                            if child_ref._has_data():
                                return True

                    if self.id is not None:
                        return True

                    if self.name is not None:
                        return True

                    if self.number_of_labels is not None:
                        return True

                    if self.options is not None:
                        return True

                    if self.record_map is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                    return meta._meta_table['NetFlow.Configuration.FlowMonitorMaps.FlowMonitorMap']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-asr9k-netflow-oper:net-flow/Cisco-IOS-XR-asr9k-netflow-oper:configuration/Cisco-IOS-XR-asr9k-netflow-oper:flow-monitor-maps'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.flow_monitor_map is not None:
                    for child_ref in self.flow_monitor_map:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                return meta._meta_table['NetFlow.Configuration.FlowMonitorMaps']['meta_info']


        class FlowSamplerMaps(object):
            """
            Flow sampler map configuration information
            
            .. attribute:: flow_sampler_map
            
            	Flow sampler map information
            	**type**\: list of    :py:class:`FlowSamplerMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Configuration.FlowSamplerMaps.FlowSamplerMap>`
            
            

            """

            _prefix = 'asr9k-netflow-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.flow_sampler_map = YList()
                self.flow_sampler_map.parent = self
                self.flow_sampler_map.name = 'flow_sampler_map'


            class FlowSamplerMap(object):
                """
                Flow sampler map information
                
                .. attribute:: sampler_name  <key>
                
                	Sampler name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: id
                
                	Unique ID in the global flow sampler ID space
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: name
                
                	Name of the flow sampler map
                	**type**\:  str
                
                .. attribute:: sampling_mode
                
                	Sampling mode and parameters
                	**type**\:  str
                
                

                """

                _prefix = 'asr9k-netflow-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.sampler_name = None
                    self.id = None
                    self.name = None
                    self.sampling_mode = None

                @property
                def _common_path(self):
                    if self.sampler_name is None:
                        raise YPYModelError('Key property sampler_name is None')

                    return '/Cisco-IOS-XR-asr9k-netflow-oper:net-flow/Cisco-IOS-XR-asr9k-netflow-oper:configuration/Cisco-IOS-XR-asr9k-netflow-oper:flow-sampler-maps/Cisco-IOS-XR-asr9k-netflow-oper:flow-sampler-map[Cisco-IOS-XR-asr9k-netflow-oper:sampler-name = ' + str(self.sampler_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.sampler_name is not None:
                        return True

                    if self.id is not None:
                        return True

                    if self.name is not None:
                        return True

                    if self.sampling_mode is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                    return meta._meta_table['NetFlow.Configuration.FlowSamplerMaps.FlowSamplerMap']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-asr9k-netflow-oper:net-flow/Cisco-IOS-XR-asr9k-netflow-oper:configuration/Cisco-IOS-XR-asr9k-netflow-oper:flow-sampler-maps'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.flow_sampler_map is not None:
                    for child_ref in self.flow_sampler_map:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                return meta._meta_table['NetFlow.Configuration.FlowSamplerMaps']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-netflow-oper:net-flow/Cisco-IOS-XR-asr9k-netflow-oper:configuration'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.flow_exporter_maps is not None and self.flow_exporter_maps._has_data():
                return True

            if self.flow_monitor_maps is not None and self.flow_monitor_maps._has_data():
                return True

            if self.flow_sampler_maps is not None and self.flow_sampler_maps._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
            return meta._meta_table['NetFlow.Configuration']['meta_info']


    class Statistics(object):
        """
        Node\-specific NetFlow statistics information
        
        .. attribute:: statistic
        
        	NetFlow statistics information for a particular node
        	**type**\: list of    :py:class:`Statistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic>`
        
        

        """

        _prefix = 'asr9k-netflow-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.statistic = YList()
            self.statistic.parent = self
            self.statistic.name = 'statistic'


        class Statistic(object):
            """
            NetFlow statistics information for a particular
            node
            
            .. attribute:: node  <key>
            
            	Node location
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: producer
            
            	NetFlow producer statistics
            	**type**\:   :py:class:`Producer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Producer>`
            
            .. attribute:: server
            
            	NetFlow server statistics
            	**type**\:   :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server>`
            
            

            """

            _prefix = 'asr9k-netflow-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node = None
                self.producer = NetFlow.Statistics.Statistic.Producer()
                self.producer.parent = self
                self.server = NetFlow.Statistics.Statistic.Server()
                self.server.parent = self


            class Producer(object):
                """
                NetFlow producer statistics
                
                .. attribute:: statistics
                
                	Statistics information
                	**type**\:   :py:class:`Statistics_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Producer.Statistics_>`
                
                

                """

                _prefix = 'asr9k-netflow-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.statistics = NetFlow.Statistics.Statistic.Producer.Statistics_()
                    self.statistics.parent = self


                class Statistics_(object):
                    """
                    Statistics information
                    
                    .. attribute:: drops_no_space
                    
                    	Drops (no space)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: drops_others
                    
                    	Drops (others)
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: flow_packet_counts
                    
                    	Number of Rxed Flow Packets
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ipv4_egress_flows
                    
                    	IPv4 egress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ipv4_ingress_flows
                    
                    	IPv4 ingress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ipv6_egress_flows
                    
                    	IPv6 egress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: ipv6_ingress_flows
                    
                    	IPv6 ingress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: last_cleared
                    
                    	Last time Statistics cleared in 'Mon Jan 1 12\:00 \:00 2xxx' format
                    	**type**\:  str
                    
                    .. attribute:: mpls_egress_flows
                    
                    	MPLS egress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: mpls_ingress_flows
                    
                    	MPLS ingress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: spp_rx_counts
                    
                    	Number of Rxed SPP Packets
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: unknown_egress_flows
                    
                    	Unknown egress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: unknown_ingress_flows
                    
                    	Unknown ingress flows
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: waiting_servers
                    
                    	Number of waiting servers
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'asr9k-netflow-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.drops_no_space = None
                        self.drops_others = None
                        self.flow_packet_counts = None
                        self.ipv4_egress_flows = None
                        self.ipv4_ingress_flows = None
                        self.ipv6_egress_flows = None
                        self.ipv6_ingress_flows = None
                        self.last_cleared = None
                        self.mpls_egress_flows = None
                        self.mpls_ingress_flows = None
                        self.spp_rx_counts = None
                        self.unknown_egress_flows = None
                        self.unknown_ingress_flows = None
                        self.waiting_servers = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-netflow-oper:statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.drops_no_space is not None:
                            return True

                        if self.drops_others is not None:
                            return True

                        if self.flow_packet_counts is not None:
                            return True

                        if self.ipv4_egress_flows is not None:
                            return True

                        if self.ipv4_ingress_flows is not None:
                            return True

                        if self.ipv6_egress_flows is not None:
                            return True

                        if self.ipv6_ingress_flows is not None:
                            return True

                        if self.last_cleared is not None:
                            return True

                        if self.mpls_egress_flows is not None:
                            return True

                        if self.mpls_ingress_flows is not None:
                            return True

                        if self.spp_rx_counts is not None:
                            return True

                        if self.unknown_egress_flows is not None:
                            return True

                        if self.unknown_ingress_flows is not None:
                            return True

                        if self.waiting_servers is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                        return meta._meta_table['NetFlow.Statistics.Statistic.Producer.Statistics_']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-netflow-oper:producer'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.statistics is not None and self.statistics._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                    return meta._meta_table['NetFlow.Statistics.Statistic.Producer']['meta_info']


            class Server(object):
                """
                NetFlow server statistics
                
                .. attribute:: flow_exporters
                
                	Flow exporter information
                	**type**\:   :py:class:`FlowExporters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server.FlowExporters>`
                
                

                """

                _prefix = 'asr9k-netflow-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.flow_exporters = NetFlow.Statistics.Statistic.Server.FlowExporters()
                    self.flow_exporters.parent = self


                class FlowExporters(object):
                    """
                    Flow exporter information
                    
                    .. attribute:: flow_exporter
                    
                    	Exporter information
                    	**type**\: list of    :py:class:`FlowExporter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter>`
                    
                    

                    """

                    _prefix = 'asr9k-netflow-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.flow_exporter = YList()
                        self.flow_exporter.parent = self
                        self.flow_exporter.name = 'flow_exporter'


                    class FlowExporter(object):
                        """
                        Exporter information
                        
                        .. attribute:: exporter_name  <key>
                        
                        	Exporter name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: exporter
                        
                        	Statistics information for the exporter
                        	**type**\:   :py:class:`Exporter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter>`
                        
                        

                        """

                        _prefix = 'asr9k-netflow-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.exporter_name = None
                            self.exporter = NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter()
                            self.exporter.parent = self


                        class Exporter(object):
                            """
                            Statistics information for the exporter
                            
                            .. attribute:: statistic
                            
                            	Array of flow exporters
                            	**type**\: list of    :py:class:`Statistic_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic_>`
                            
                            

                            """

                            _prefix = 'asr9k-netflow-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.statistic = YList()
                                self.statistic.parent = self
                                self.statistic.name = 'statistic'


                            class Statistic_(object):
                                """
                                Array of flow exporters
                                
                                .. attribute:: collector
                                
                                	Statistics of all collectors
                                	**type**\: list of    :py:class:`Collector <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_netflow_oper.NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic_.Collector>`
                                
                                .. attribute:: memory_usage
                                
                                	Memory usage
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: name
                                
                                	Exporter name
                                	**type**\:  str
                                
                                .. attribute:: used_by_flow_monitor
                                
                                	List of flow monitors that use the exporter
                                	**type**\:  list of str
                                
                                

                                """

                                _prefix = 'asr9k-netflow-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.collector = YList()
                                    self.collector.parent = self
                                    self.collector.name = 'collector'
                                    self.memory_usage = None
                                    self.name = None
                                    self.used_by_flow_monitor = YLeafList()
                                    self.used_by_flow_monitor.parent = self
                                    self.used_by_flow_monitor.name = 'used_by_flow_monitor'


                                class Collector(object):
                                    """
                                    Statistics of all collectors
                                    
                                    .. attribute:: bytes_dropped
                                    
                                    	Bytes dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: bytes_sent
                                    
                                    	Bytes sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: destination_address
                                    
                                    	Destination IPv4 address in AAA.BBB.CCC.DDD format
                                    	**type**\:  str
                                    
                                    .. attribute:: destination_port
                                    
                                    	Destination port number
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: exporter_state
                                    
                                    	Exporter state
                                    	**type**\:  str
                                    
                                    .. attribute:: flow_bytes_dropped
                                    
                                    	Flow bytes dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: flow_bytes_sent
                                    
                                    	Flow bytes sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: flows_dropped
                                    
                                    	Flows dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: flows_sent
                                    
                                    	Flows sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: last_hour_bytes_sent
                                    
                                    	Total bytes exported over the last one hour
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: last_hour_flows_sent
                                    
                                    	Total flows exported over the of last one hour
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: last_hour_packest_sent
                                    
                                    	Total packets exported over the last one hour
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: last_minute_bytes_sent
                                    
                                    	Total bytes exported over the last one minute
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: last_minute_flows_sent
                                    
                                    	Total flows exported over the last one minute
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: last_minute_packets
                                    
                                    	Total packets exported over the last one minute
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: last_second_bytes_sent
                                    
                                    	Total bytes exported over the last one second
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: last_second_flows_sent
                                    
                                    	Total flows exported over the last one second
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: last_second_packets_sent
                                    
                                    	Total packets exported over the last one second
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: option_data_bytes_dropped
                                    
                                    	Option data dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: option_data_bytes_sent
                                    
                                    	Option data bytes sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: option_data_dropped
                                    
                                    	Option data dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: option_data_sent
                                    
                                    	Option data sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: option_template_bytes_dropped
                                    
                                    	Option template bytes dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: option_template_bytes_sent
                                    
                                    	Option template bytes sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: option_templates_dropped
                                    
                                    	Option templates dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: option_templates_sent
                                    
                                    	Option templates sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: packets_dropped
                                    
                                    	Packets dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: packets_sent
                                    
                                    	Packets sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: souce_port
                                    
                                    	Source port number
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: source_address
                                    
                                    	Source IPv4 address in AAA.BBB.CCC.DDD format
                                    	**type**\:  str
                                    
                                    .. attribute:: template_bytes_dropped
                                    
                                    	Template bytes dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: template_bytes_sent
                                    
                                    	Template bytes sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte
                                    
                                    .. attribute:: templates_dropped
                                    
                                    	Templates dropped
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: templates_sent
                                    
                                    	Templates sent
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: transport_protocol
                                    
                                    	Transport protocol
                                    	**type**\:  str
                                    
                                    .. attribute:: vrf_name
                                    
                                    	VRF Name
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'asr9k-netflow-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.bytes_dropped = None
                                        self.bytes_sent = None
                                        self.destination_address = None
                                        self.destination_port = None
                                        self.exporter_state = None
                                        self.flow_bytes_dropped = None
                                        self.flow_bytes_sent = None
                                        self.flows_dropped = None
                                        self.flows_sent = None
                                        self.last_hour_bytes_sent = None
                                        self.last_hour_flows_sent = None
                                        self.last_hour_packest_sent = None
                                        self.last_minute_bytes_sent = None
                                        self.last_minute_flows_sent = None
                                        self.last_minute_packets = None
                                        self.last_second_bytes_sent = None
                                        self.last_second_flows_sent = None
                                        self.last_second_packets_sent = None
                                        self.option_data_bytes_dropped = None
                                        self.option_data_bytes_sent = None
                                        self.option_data_dropped = None
                                        self.option_data_sent = None
                                        self.option_template_bytes_dropped = None
                                        self.option_template_bytes_sent = None
                                        self.option_templates_dropped = None
                                        self.option_templates_sent = None
                                        self.packets_dropped = None
                                        self.packets_sent = None
                                        self.souce_port = None
                                        self.source_address = None
                                        self.template_bytes_dropped = None
                                        self.template_bytes_sent = None
                                        self.templates_dropped = None
                                        self.templates_sent = None
                                        self.transport_protocol = None
                                        self.vrf_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-netflow-oper:collector'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.bytes_dropped is not None:
                                            return True

                                        if self.bytes_sent is not None:
                                            return True

                                        if self.destination_address is not None:
                                            return True

                                        if self.destination_port is not None:
                                            return True

                                        if self.exporter_state is not None:
                                            return True

                                        if self.flow_bytes_dropped is not None:
                                            return True

                                        if self.flow_bytes_sent is not None:
                                            return True

                                        if self.flows_dropped is not None:
                                            return True

                                        if self.flows_sent is not None:
                                            return True

                                        if self.last_hour_bytes_sent is not None:
                                            return True

                                        if self.last_hour_flows_sent is not None:
                                            return True

                                        if self.last_hour_packest_sent is not None:
                                            return True

                                        if self.last_minute_bytes_sent is not None:
                                            return True

                                        if self.last_minute_flows_sent is not None:
                                            return True

                                        if self.last_minute_packets is not None:
                                            return True

                                        if self.last_second_bytes_sent is not None:
                                            return True

                                        if self.last_second_flows_sent is not None:
                                            return True

                                        if self.last_second_packets_sent is not None:
                                            return True

                                        if self.option_data_bytes_dropped is not None:
                                            return True

                                        if self.option_data_bytes_sent is not None:
                                            return True

                                        if self.option_data_dropped is not None:
                                            return True

                                        if self.option_data_sent is not None:
                                            return True

                                        if self.option_template_bytes_dropped is not None:
                                            return True

                                        if self.option_template_bytes_sent is not None:
                                            return True

                                        if self.option_templates_dropped is not None:
                                            return True

                                        if self.option_templates_sent is not None:
                                            return True

                                        if self.packets_dropped is not None:
                                            return True

                                        if self.packets_sent is not None:
                                            return True

                                        if self.souce_port is not None:
                                            return True

                                        if self.source_address is not None:
                                            return True

                                        if self.template_bytes_dropped is not None:
                                            return True

                                        if self.template_bytes_sent is not None:
                                            return True

                                        if self.templates_dropped is not None:
                                            return True

                                        if self.templates_sent is not None:
                                            return True

                                        if self.transport_protocol is not None:
                                            return True

                                        if self.vrf_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                                        return meta._meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic_.Collector']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-netflow-oper:statistic'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.collector is not None:
                                        for child_ref in self.collector:
                                            if child_ref._has_data():
                                                return True

                                    if self.memory_usage is not None:
                                        return True

                                    if self.name is not None:
                                        return True

                                    if self.used_by_flow_monitor is not None:
                                        for child in self.used_by_flow_monitor:
                                            if child is not None:
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                                    return meta._meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic_']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-netflow-oper:exporter'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.statistic is not None:
                                    for child_ref in self.statistic:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                                return meta._meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.exporter_name is None:
                                raise YPYModelError('Key property exporter_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-netflow-oper:flow-exporter[Cisco-IOS-XR-asr9k-netflow-oper:exporter-name = ' + str(self.exporter_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.exporter_name is not None:
                                return True

                            if self.exporter is not None and self.exporter._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                            return meta._meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-netflow-oper:flow-exporters'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.flow_exporter is not None:
                            for child_ref in self.flow_exporter:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                        return meta._meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-netflow-oper:server'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.flow_exporters is not None and self.flow_exporters._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                    return meta._meta_table['NetFlow.Statistics.Statistic.Server']['meta_info']

            @property
            def _common_path(self):
                if self.node is None:
                    raise YPYModelError('Key property node is None')

                return '/Cisco-IOS-XR-asr9k-netflow-oper:net-flow/Cisco-IOS-XR-asr9k-netflow-oper:statistics/Cisco-IOS-XR-asr9k-netflow-oper:statistic[Cisco-IOS-XR-asr9k-netflow-oper:node = ' + str(self.node) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.node is not None:
                    return True

                if self.producer is not None and self.producer._has_data():
                    return True

                if self.server is not None and self.server._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
                return meta._meta_table['NetFlow.Statistics.Statistic']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-netflow-oper:net-flow/Cisco-IOS-XR-asr9k-netflow-oper:statistics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.statistic is not None:
                for child_ref in self.statistic:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
            return meta._meta_table['NetFlow.Statistics']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-asr9k-netflow-oper:net-flow'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.configuration is not None and self.configuration._has_data():
            return True

        if self.statistics is not None and self.statistics._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_netflow_oper as meta
        return meta._meta_table['NetFlow']['meta_info']


