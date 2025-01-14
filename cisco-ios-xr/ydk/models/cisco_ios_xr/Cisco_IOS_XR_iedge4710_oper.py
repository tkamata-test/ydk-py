""" Cisco_IOS_XR_iedge4710_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR iedge4710 package operational data.

This module contains definitions
for the following management objects\:
  subscriber\: Subscriber operational data
  iedge\-license\-manager\: iedge license manager

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AaaAuthServiceEnum(Enum):
    """
    AaaAuthServiceEnum

    AAA authorization service types

    .. data:: none = 0

    	None

    .. data:: login = 1

    	Login

    .. data:: framed = 2

    	Framed

    .. data:: callback_login = 3

    	Callback login

    .. data:: callback_framed = 4

    	Callback framed

    .. data:: outbound = 5

    	Outbound

    .. data:: administrator = 6

    	Administrator

    .. data:: prompt = 7

    	Prompt

    .. data:: authentication_only = 8

    	Authentication only

    .. data:: callback_nas_prompt = 9

    	Callback NAS prompt

    .. data:: call_check = 10

    	Call check

    .. data:: callback_administrator = 11

    	Callback administrator

    .. data:: voice = 12

    	Voice

    .. data:: fax = 13

    	Fax

    .. data:: modem_relay = 14

    	Modem relay

    .. data:: eap_over_udp = 15

    	EAP over UDP

    """

    none = 0

    login = 1

    framed = 2

    callback_login = 3

    callback_framed = 4

    outbound = 5

    administrator = 6

    prompt = 7

    authentication_only = 8

    callback_nas_prompt = 9

    call_check = 10

    callback_administrator = 11

    voice = 12

    fax = 13

    modem_relay = 14

    eap_over_udp = 15


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
        return meta._meta_table['AaaAuthServiceEnum']


class AaaInterfaceEnum(Enum):
    """
    AaaInterfaceEnum

    AAA interface types

    .. data:: none = 0

    	None

    .. data:: primary_rate = 1

    	Primary rate

    .. data:: basic_rate = 2

    	Basic rate

    .. data:: serial = 3

    	Serial

    .. data:: asynchronous = 4

    	Asynchronous

    .. data:: vty = 5

    	VTY

    .. data:: atm = 6

    	ATM

    .. data:: ethernet = 7

    	Ethernet

    .. data:: ppp_over_atm = 8

    	PPP over ATM

    .. data:: pppoe_over_atm = 9

    	PPPoE over ATM

    .. data:: pppoe_over_ethernet = 10

    	PPPoE over ethernet

    .. data:: ppp_over_vlan = 11

    	PPP over VLAN

    .. data:: ppp_over_qinq = 12

    	PPP over Q in Q

    .. data:: v120 = 13

    	V120

    .. data:: v110 = 14

    	V110

    .. data:: piafs = 15

    	PHS internet access forum standard

    .. data:: x75 = 16

    	X75

    .. data:: ip_sec = 17

    	IP sec

    .. data:: other = 18

    	Other

    .. data:: virtual_pppoe_over_ethernet = 19

    	Virtual PPPoE over ethernet

    .. data:: virtual_pppoe_over_vlan = 20

    	Virtual PPPoE over VLAN

    .. data:: virtual_pppoe_over_qinq = 21

    	Virtual PPPoE over Q in Q

    .. data:: ipo_e_over_ethernet = 22

    	IPoE over ethernet

    .. data:: ipo_e_over_vlan = 23

    	IPoE over VLAN

    .. data:: ipo_e_over_qinq = 24

    	IPoE over Q in Q

    .. data:: virtual_i_po_e_over_ethernet = 25

    	Virtual IPoE over ethernet

    .. data:: virtual_i_po_e_over_vlan = 26

    	Virtual IPoE over VLAN

    .. data:: virtual_i_po_e_over_qinq = 27

    	Virtual IPoE over Q in Q

    """

    none = 0

    primary_rate = 1

    basic_rate = 2

    serial = 3

    asynchronous = 4

    vty = 5

    atm = 6

    ethernet = 7

    ppp_over_atm = 8

    pppoe_over_atm = 9

    pppoe_over_ethernet = 10

    ppp_over_vlan = 11

    ppp_over_qinq = 12

    v120 = 13

    v110 = 14

    piafs = 15

    x75 = 16

    ip_sec = 17

    other = 18

    virtual_pppoe_over_ethernet = 19

    virtual_pppoe_over_vlan = 20

    virtual_pppoe_over_qinq = 21

    ipo_e_over_ethernet = 22

    ipo_e_over_vlan = 23

    ipo_e_over_qinq = 24

    virtual_i_po_e_over_ethernet = 25

    virtual_i_po_e_over_vlan = 26

    virtual_i_po_e_over_qinq = 27


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
        return meta._meta_table['AaaInterfaceEnum']


class AaaTerminateCauseEnum(Enum):
    """
    AaaTerminateCauseEnum

    AAA terminate cause types

    .. data:: none = 0

    	None

    .. data:: user_request = 1

    	User request

    .. data:: lost_carrier = 2

    	Lost carrier

    .. data:: lost_service = 3

    	Lost service

    .. data:: idle_timeout = 4

    	Idle timeout

    .. data:: session_timeout = 5

    	Session timeout

    .. data:: admin_reset = 6

    	Admin reset

    .. data:: admin_reboot = 7

    	Admin reboot

    .. data:: port_error = 8

    	Port error

    .. data:: nas_error = 9

    	NAS error

    .. data:: nas_request = 10

    	NAS request

    .. data:: nas_reboot = 11

    	NAS reboot

    .. data:: port_unneeded = 12

    	Port unneeded

    .. data:: port_preempted = 13

    	Port preempted

    .. data:: port_suspended = 14

    	Port suspended

    .. data:: service_unavailable = 15

    	Service unavailable

    .. data:: callback = 16

    	Callback

    .. data:: user_error = 17

    	User error

    .. data:: host_request = 18

    	Host request

    .. data:: supplicant_restart = 19

    	Supplicant restart

    .. data:: reauthorization_failure = 20

    	Reauthorization failure

    .. data:: port_reinitialized = 21

    	Port reinitialized

    .. data:: admin_disabled = 22

    	Admin disabled

    """

    none = 0

    user_request = 1

    lost_carrier = 2

    lost_service = 3

    idle_timeout = 4

    session_timeout = 5

    admin_reset = 6

    admin_reboot = 7

    port_error = 8

    nas_error = 9

    nas_request = 10

    nas_reboot = 11

    port_unneeded = 12

    port_preempted = 13

    port_suspended = 14

    service_unavailable = 15

    callback = 16

    user_error = 17

    host_request = 18

    supplicant_restart = 19

    reauthorization_failure = 20

    port_reinitialized = 21

    admin_disabled = 22


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
        return meta._meta_table['AaaTerminateCauseEnum']


class AaaTunnelMediumEnum(Enum):
    """
    AaaTunnelMediumEnum

    Tunnel medium types

    .. data:: none = 0

    	None

    .. data:: ipv4 = 1

    	IPv4

    .. data:: ipv6 = 2

    	IPv6

    .. data:: nsap = 3

    	NSAP

    .. data:: hdlc = 4

    	HDLC

    .. data:: bbn = 5

    	BBN

    .. data:: all802 = 6

    	ALL 802

    """

    none = 0

    ipv4 = 1

    ipv6 = 2

    nsap = 3

    hdlc = 4

    bbn = 5

    all802 = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
        return meta._meta_table['AaaTunnelMediumEnum']


class AaaTunnelProtoEnum(Enum):
    """
    AaaTunnelProtoEnum

    Tunnel protocol types

    .. data:: none = 0

    	None

    .. data:: pptp = 1

    	Point-to-point tunneling protocol

    .. data:: l2f = 2

    	Layer 2 forwarding

    .. data:: l2tp = 3

    	Layer 2 tunneling protocol

    .. data:: atmp = 4

    	Ascend tunnel management protocol

    .. data:: vtp = 5

    	VLAN trunk protocol

    .. data:: ah = 6

    	Authentication header

    .. data:: ip_over_ip = 7

    	IP over IP

    .. data:: minimum_ip_over_ip = 8

    	Minimum IP over IP

    .. data:: esp = 9

    	Encapsulating security payload

    .. data:: gre = 10

    	Generic routing encapsulation

    .. data:: bay_dvs = 11

    	Bay dial virtual services

    .. data:: ip_in_ip = 12

    	IP in IP

    .. data:: vlan = 13

    	VLAN

    """

    none = 0

    pptp = 1

    l2f = 2

    l2tp = 3

    atmp = 4

    vtp = 5

    ah = 6

    ip_over_ip = 7

    minimum_ip_over_ip = 8

    esp = 9

    gre = 10

    bay_dvs = 11

    ip_in_ip = 12

    vlan = 13


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
        return meta._meta_table['AaaTunnelProtoEnum']


class IedgeOperSessionAfStateEnum(Enum):
    """
    IedgeOperSessionAfStateEnum

    Subscriber session address family state

    .. data:: not_started = 0

    	Not started

    .. data:: down = 1

    	Down

    .. data:: up_pending = 2

    	Up Pending

    .. data:: up = 3

    	Up

    """

    not_started = 0

    down = 1

    up_pending = 2

    up = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
        return meta._meta_table['IedgeOperSessionAfStateEnum']


class IedgeOperSessionEnum(Enum):
    """
    IedgeOperSessionEnum

    Subscriber session types

    .. data:: unknown = 0

    	Unknown

    .. data:: pppoe = 1

    	PPPoE/PPP client

    .. data:: ppp = 2

    	PPP serial client

    .. data:: ip_packet_trigger = 3

    	IP subscriber - packet trigger

    .. data:: ip_packet_dhcp_trigger = 4

    	IP subscriber - DHCP trigger

    """

    unknown = 0

    pppoe = 1

    ppp = 2

    ip_packet_trigger = 3

    ip_packet_dhcp_trigger = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
        return meta._meta_table['IedgeOperSessionEnum']


class IedgeOperSessionStateEnum(Enum):
    """
    IedgeOperSessionStateEnum

    Subscriber session states

    .. data:: initialize = 0

    	Initialize

    .. data:: connecting = 1

    	Connecting

    .. data:: connected = 2

    	Connected

    .. data:: activated = 3

    	Activated

    .. data:: idle = 4

    	Idle

    .. data:: disconnecting = 5

    	Disconnecting

    .. data:: end = 6

    	End

    """

    initialize = 0

    connecting = 1

    connected = 2

    activated = 3

    idle = 4

    disconnecting = 5

    end = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
        return meta._meta_table['IedgeOperSessionStateEnum']


class IedgePppSubEnum(Enum):
    """
    IedgePppSubEnum

    PPPoE sub types

    .. data:: pta = 0

    	PPP termination and aggregation

    .. data:: lac = 1

    	L2TP access controller

    """

    pta = 0

    lac = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
        return meta._meta_table['IedgePppSubEnum']


class SubscriberAddressFamilyFilterFlagEnum(Enum):
    """
    SubscriberAddressFamilyFilterFlagEnum

    Subscriber address family filter flag

    .. data:: ipv4_only = 0

    	IPv4 only

    .. data:: ipv6_only = 1

    	IPv6 only

    .. data:: ipv4_all = 2

    	IPv4 all

    .. data:: ipv6_all = 3

    	IPv6 all

    .. data:: dual_all = 4

    	Dual all

    .. data:: dual_part_up = 5

    	Dual part up

    .. data:: dual_up = 6

    	Dual up

    .. data:: lac = 7

    	LAC

    """

    ipv4_only = 0

    ipv6_only = 1

    ipv4_all = 2

    ipv6_all = 3

    dual_all = 4

    dual_part_up = 5

    dual_up = 6

    lac = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
        return meta._meta_table['SubscriberAddressFamilyFilterFlagEnum']


class SubscriberAuthenStateFilterFlagEnum(Enum):
    """
    SubscriberAuthenStateFilterFlagEnum

    Subscriber authen state filter flag

    .. data:: un_authenticated = 0

    	UnAuthenticated

    .. data:: authenticated = 1

    	Authenticated

    """

    un_authenticated = 0

    authenticated = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
        return meta._meta_table['SubscriberAuthenStateFilterFlagEnum']


class SubscriberAuthorStateFilterFlagEnum(Enum):
    """
    SubscriberAuthorStateFilterFlagEnum

    Subscriber author state filter flag

    .. data:: un_authorized = 0

    	UnAuthorized

    .. data:: authorized = 1

    	Authorized

    """

    un_authorized = 0

    authorized = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
        return meta._meta_table['SubscriberAuthorStateFilterFlagEnum']


class SubscriberStateFilterFlagEnum(Enum):
    """
    SubscriberStateFilterFlagEnum

    Subscriber state filter flag

    .. data:: initializing = 0

    	Initializing

    .. data:: connecting = 1

    	Connecting

    .. data:: connected = 2

    	Connected

    .. data:: activated = 3

    	Activated

    .. data:: idle = 4

    	Idle

    .. data:: disconnecting = 5

    	Disconnecting

    .. data:: end = 6

    	End

    """

    initializing = 0

    connecting = 1

    connected = 2

    activated = 3

    idle = 4

    disconnecting = 5

    end = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
        return meta._meta_table['SubscriberStateFilterFlagEnum']



class Subscriber(object):
    """
    Subscriber operational data
    
    .. attribute:: manager
    
    	Subscriber manager operational data
    	**type**\:   :py:class:`Manager <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager>`
    
    .. attribute:: session
    
    	Subscriber session operational data
    	**type**\:   :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session>`
    
    

    """

    _prefix = 'iedge4710-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.manager = Subscriber.Manager()
        self.manager.parent = self
        self.session = Subscriber.Session()
        self.session.parent = self


    class Manager(object):
        """
        Subscriber manager operational data
        
        .. attribute:: nodes
        
        	Subscriber manager list of nodes
        	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes>`
        
        

        """

        _prefix = 'iedge4710-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.nodes = Subscriber.Manager.Nodes()
            self.nodes.parent = self


        class Nodes(object):
            """
            Subscriber manager list of nodes
            
            .. attribute:: node
            
            	Subscriber manager operational data for a particular node
            	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node>`
            
            

            """

            _prefix = 'iedge4710-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node = YList()
                self.node.parent = self
                self.node.name = 'node'


            class Node(object):
                """
                Subscriber manager operational data for a
                particular node
                
                .. attribute:: node_name  <key>
                
                	Node name
                	**type**\:  str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: statistics
                
                	Subscriber manager statistics
                	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics>`
                
                

                """

                _prefix = 'iedge4710-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.node_name = None
                    self.statistics = Subscriber.Manager.Nodes.Node.Statistics()
                    self.statistics.parent = self


                class Statistics(object):
                    """
                    Subscriber manager statistics
                    
                    .. attribute:: aaa
                    
                    	AAA statistics
                    	**type**\:   :py:class:`Aaa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa>`
                    
                    .. attribute:: aggregate_summary
                    
                    	Aggregate summary of statistics
                    	**type**\:   :py:class:`AggregateSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.AggregateSummary>`
                    
                    .. attribute:: srg
                    
                    	Geo Redundancy statistics
                    	**type**\:   :py:class:`Srg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Srg>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.aaa = Subscriber.Manager.Nodes.Node.Statistics.Aaa()
                        self.aaa.parent = self
                        self.aggregate_summary = Subscriber.Manager.Nodes.Node.Statistics.AggregateSummary()
                        self.aggregate_summary.parent = self
                        self.srg = Subscriber.Manager.Nodes.Node.Statistics.Srg()
                        self.srg.parent = self


                    class Aaa(object):
                        """
                        AAA statistics
                        
                        .. attribute:: accounting
                        
                        	Accounting statistics
                        	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting>`
                        
                        .. attribute:: aggregate_accounting
                        
                        	Aggregate accounting statistics
                        	**type**\:   :py:class:`AggregateAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting>`
                        
                        .. attribute:: aggregate_authentication
                        
                        	Aggregate authentication statistics
                        	**type**\:   :py:class:`AggregateAuthentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthentication>`
                        
                        .. attribute:: aggregate_authorization
                        
                        	Aggregate authorization statistics
                        	**type**\:   :py:class:`AggregateAuthorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthorization>`
                        
                        .. attribute:: aggregate_change_of_authorization
                        
                        	Aggregate change of authorization (COA) statistics
                        	**type**\:   :py:class:`AggregateChangeOfAuthorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization>`
                        
                        .. attribute:: aggregate_mobility
                        
                        	Aggregate mobility statistics
                        	**type**\:   :py:class:`AggregateMobility <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateMobility>`
                        
                        .. attribute:: authentication
                        
                        	Authentication statistics
                        	**type**\:   :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authentication>`
                        
                        .. attribute:: authorization
                        
                        	Authorization statistics
                        	**type**\:   :py:class:`Authorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authorization>`
                        
                        .. attribute:: change_of_authorization
                        
                        	Change of authorization (COA) statistics
                        	**type**\:   :py:class:`ChangeOfAuthorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization>`
                        
                        .. attribute:: mobility
                        
                        	Mobility statistics
                        	**type**\:   :py:class:`Mobility <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Mobility>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.accounting = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting()
                            self.accounting.parent = self
                            self.aggregate_accounting = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting()
                            self.aggregate_accounting.parent = self
                            self.aggregate_authentication = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthentication()
                            self.aggregate_authentication.parent = self
                            self.aggregate_authorization = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthorization()
                            self.aggregate_authorization.parent = self
                            self.aggregate_change_of_authorization = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization()
                            self.aggregate_change_of_authorization.parent = self
                            self.aggregate_mobility = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateMobility()
                            self.aggregate_mobility.parent = self
                            self.authentication = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authentication()
                            self.authentication.parent = self
                            self.authorization = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authorization()
                            self.authorization.parent = self
                            self.change_of_authorization = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization()
                            self.change_of_authorization.parent = self
                            self.mobility = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Mobility()
                            self.mobility.parent = self


                        class AggregateAccounting(object):
                            """
                            Aggregate accounting statistics
                            
                            .. attribute:: active_sessions
                            
                            	Active sessions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: interim
                            
                            	Interim statistics
                            	**type**\:   :py:class:`Interim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Interim>`
                            
                            .. attribute:: interim_inflight
                            
                            	Interim inflight details
                            	**type**\:   :py:class:`InterimInflight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.InterimInflight>`
                            
                            .. attribute:: pass_through
                            
                            	Pass\-through statistics
                            	**type**\:   :py:class:`PassThrough <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.PassThrough>`
                            
                            .. attribute:: policy_plane_errored_requests
                            
                            	Policy plane errored requests
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: policy_plane_unknown_requests
                            
                            	Policy plane unknown requests
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: start
                            
                            	Start statistics
                            	**type**\:   :py:class:`Start <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Start>`
                            
                            .. attribute:: started_sessions
                            
                            	Started sessions
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: stop
                            
                            	Stop statistics
                            	**type**\:   :py:class:`Stop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Stop>`
                            
                            .. attribute:: stopped_sessions
                            
                            	Stopped sessions
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: update
                            
                            	Update statistics
                            	**type**\:   :py:class:`Update <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Update>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.active_sessions = None
                                self.interim = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Interim()
                                self.interim.parent = self
                                self.interim_inflight = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.InterimInflight()
                                self.interim_inflight.parent = self
                                self.pass_through = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.PassThrough()
                                self.pass_through.parent = self
                                self.policy_plane_errored_requests = None
                                self.policy_plane_unknown_requests = None
                                self.start = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Start()
                                self.start.parent = self
                                self.started_sessions = None
                                self.stop = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Stop()
                                self.stop.parent = self
                                self.stopped_sessions = None
                                self.update = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Update()
                                self.update.parent = self


                            class Start(object):
                                """
                                Start statistics
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.aaa_errored_requests = None
                                    self.aaa_failed_responses = None
                                    self.aaa_sent_requests = None
                                    self.aaa_succeeded_responses = None
                                    self.errored_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:start'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.aaa_errored_requests is not None:
                                        return True

                                    if self.aaa_failed_responses is not None:
                                        return True

                                    if self.aaa_sent_requests is not None:
                                        return True

                                    if self.aaa_succeeded_responses is not None:
                                        return True

                                    if self.errored_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Start']['meta_info']


                            class Stop(object):
                                """
                                Stop statistics
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.aaa_errored_requests = None
                                    self.aaa_failed_responses = None
                                    self.aaa_sent_requests = None
                                    self.aaa_succeeded_responses = None
                                    self.errored_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:stop'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.aaa_errored_requests is not None:
                                        return True

                                    if self.aaa_failed_responses is not None:
                                        return True

                                    if self.aaa_sent_requests is not None:
                                        return True

                                    if self.aaa_succeeded_responses is not None:
                                        return True

                                    if self.errored_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Stop']['meta_info']


                            class Interim(object):
                                """
                                Interim statistics
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.aaa_errored_requests = None
                                    self.aaa_failed_responses = None
                                    self.aaa_sent_requests = None
                                    self.aaa_succeeded_responses = None
                                    self.errored_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:interim'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.aaa_errored_requests is not None:
                                        return True

                                    if self.aaa_failed_responses is not None:
                                        return True

                                    if self.aaa_sent_requests is not None:
                                        return True

                                    if self.aaa_succeeded_responses is not None:
                                        return True

                                    if self.errored_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Interim']['meta_info']


                            class PassThrough(object):
                                """
                                Pass\-through statistics
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.aaa_errored_requests = None
                                    self.aaa_failed_responses = None
                                    self.aaa_sent_requests = None
                                    self.aaa_succeeded_responses = None
                                    self.errored_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pass-through'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.aaa_errored_requests is not None:
                                        return True

                                    if self.aaa_failed_responses is not None:
                                        return True

                                    if self.aaa_sent_requests is not None:
                                        return True

                                    if self.aaa_succeeded_responses is not None:
                                        return True

                                    if self.errored_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.PassThrough']['meta_info']


                            class Update(object):
                                """
                                Update statistics
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.aaa_errored_requests = None
                                    self.aaa_failed_responses = None
                                    self.aaa_sent_requests = None
                                    self.aaa_succeeded_responses = None
                                    self.errored_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:update'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.aaa_errored_requests is not None:
                                        return True

                                    if self.aaa_failed_responses is not None:
                                        return True

                                    if self.aaa_sent_requests is not None:
                                        return True

                                    if self.aaa_succeeded_responses is not None:
                                        return True

                                    if self.errored_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.Update']['meta_info']


                            class InterimInflight(object):
                                """
                                Interim inflight details
                                
                                .. attribute:: accepted_requests
                                
                                	Accepted requests
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: denied_requests
                                
                                	Denied requests
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: low_water_mark_quota_of_requests
                                
                                	Low water mark quota of requests
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: quota_exhausts
                                
                                	Quota exhausts
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: remaining_quota_of_requests
                                
                                	Remaining quota of requests
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: total_quota_of_requests
                                
                                	Total quota of requests
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.accepted_requests = None
                                    self.denied_requests = None
                                    self.low_water_mark_quota_of_requests = None
                                    self.quota_exhausts = None
                                    self.remaining_quota_of_requests = None
                                    self.total_quota_of_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:interim-inflight'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.accepted_requests is not None:
                                        return True

                                    if self.denied_requests is not None:
                                        return True

                                    if self.low_water_mark_quota_of_requests is not None:
                                        return True

                                    if self.quota_exhausts is not None:
                                        return True

                                    if self.remaining_quota_of_requests is not None:
                                        return True

                                    if self.total_quota_of_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting.InterimInflight']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:aggregate-accounting'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.active_sessions is not None:
                                    return True

                                if self.interim is not None and self.interim._has_data():
                                    return True

                                if self.interim_inflight is not None and self.interim_inflight._has_data():
                                    return True

                                if self.pass_through is not None and self.pass_through._has_data():
                                    return True

                                if self.policy_plane_errored_requests is not None:
                                    return True

                                if self.policy_plane_unknown_requests is not None:
                                    return True

                                if self.start is not None and self.start._has_data():
                                    return True

                                if self.started_sessions is not None:
                                    return True

                                if self.stop is not None and self.stop._has_data():
                                    return True

                                if self.stopped_sessions is not None:
                                    return True

                                if self.update is not None and self.update._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAccounting']['meta_info']


                        class Authentication(object):
                            """
                            Authentication statistics
                            
                            .. attribute:: accepted_requests
                            
                            	Request accepted by Radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: errored_requests
                            
                            	Unexpected errors
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: incomplete_requests
                            
                            	Incomplete requests \- missing attributes
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rejected_requests
                            
                            	Requests rejected by radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sent_requests
                            
                            	Requests sent to radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: successful_requests
                            
                            	Requests which are successful
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: terminated_requests
                            
                            	Requests terminated by disconnect
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unreachable_requests
                            
                            	Radius server not available
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.accepted_requests = None
                                self.errored_requests = None
                                self.incomplete_requests = None
                                self.rejected_requests = None
                                self.sent_requests = None
                                self.successful_requests = None
                                self.terminated_requests = None
                                self.unreachable_requests = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:authentication'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.accepted_requests is not None:
                                    return True

                                if self.errored_requests is not None:
                                    return True

                                if self.incomplete_requests is not None:
                                    return True

                                if self.rejected_requests is not None:
                                    return True

                                if self.sent_requests is not None:
                                    return True

                                if self.successful_requests is not None:
                                    return True

                                if self.terminated_requests is not None:
                                    return True

                                if self.unreachable_requests is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authentication']['meta_info']


                        class AggregateMobility(object):
                            """
                            Aggregate mobility statistics
                            
                            .. attribute:: receive_response_failures
                            
                            	Response receive failures
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: receive_response_successes
                            
                            	Response receive success
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: send_request_failures
                            
                            	Request send failures
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: send_request_successes
                            
                            	Request send success
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.receive_response_failures = None
                                self.receive_response_successes = None
                                self.send_request_failures = None
                                self.send_request_successes = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:aggregate-mobility'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.receive_response_failures is not None:
                                    return True

                                if self.receive_response_successes is not None:
                                    return True

                                if self.send_request_failures is not None:
                                    return True

                                if self.send_request_successes is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateMobility']['meta_info']


                        class AggregateAuthentication(object):
                            """
                            Aggregate authentication statistics
                            
                            .. attribute:: accepted_requests
                            
                            	Request accepted by Radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: errored_requests
                            
                            	Unexpected errors
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: incomplete_requests
                            
                            	Incomplete requests \- missing attributes
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rejected_requests
                            
                            	Requests rejected by radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sent_requests
                            
                            	Requests sent to radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: successful_requests
                            
                            	Requests which are successful
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: terminated_requests
                            
                            	Requests terminated by disconnect
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unreachable_requests
                            
                            	Radius server not available
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.accepted_requests = None
                                self.errored_requests = None
                                self.incomplete_requests = None
                                self.rejected_requests = None
                                self.sent_requests = None
                                self.successful_requests = None
                                self.terminated_requests = None
                                self.unreachable_requests = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:aggregate-authentication'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.accepted_requests is not None:
                                    return True

                                if self.errored_requests is not None:
                                    return True

                                if self.incomplete_requests is not None:
                                    return True

                                if self.rejected_requests is not None:
                                    return True

                                if self.sent_requests is not None:
                                    return True

                                if self.successful_requests is not None:
                                    return True

                                if self.terminated_requests is not None:
                                    return True

                                if self.unreachable_requests is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthentication']['meta_info']


                        class ChangeOfAuthorization(object):
                            """
                            Change of authorization (COA) statistics
                            
                            .. attribute:: account_logoff
                            
                            	Account logoff request statistics
                            	**type**\:   :py:class:`AccountLogoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogoff>`
                            
                            .. attribute:: account_logon
                            
                            	Account logon request statistics
                            	**type**\:   :py:class:`AccountLogon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogon>`
                            
                            .. attribute:: account_update
                            
                            	Account update request statistics
                            	**type**\:   :py:class:`AccountUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountUpdate>`
                            
                            .. attribute:: attr_list_retrieve_failure_resps
                            
                            	Responses to attribute list failure errors
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: internal_err_resps
                            
                            	Responses to internal error
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: no_cmd_resps
                            
                            	Responses empty (no command) COA request
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: no_session_found_resps
                            
                            	Responses to COA with unknown session identifier
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: no_session_peer_resps
                            
                            	Responses to session peer not found error
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: resp_send_failure
                            
                            	Response send failures
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: service_multi
                            
                            	MA\-CoA Service request statistics
                            	**type**\:   :py:class:`ServiceMulti <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.ServiceMulti>`
                            
                            .. attribute:: service_profile_push_failure_resps
                            
                            	Responses to service profile push failures
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: session_disconnect
                            
                            	Session disconnect request statistics
                            	**type**\:   :py:class:`SessionDisconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SessionDisconnect>`
                            
                            .. attribute:: single_service_logoff
                            
                            	Single Service logoff request statistics
                            	**type**\:   :py:class:`SingleServiceLogoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogoff>`
                            
                            .. attribute:: single_service_logon
                            
                            	Service logon request statistics
                            	**type**\:   :py:class:`SingleServiceLogon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogon>`
                            
                            .. attribute:: single_service_modify
                            
                            	Single Service Modify request statistics
                            	**type**\:   :py:class:`SingleServiceModify <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceModify>`
                            
                            .. attribute:: unknown_account_cmd_resps
                            
                            	Responses to unknown account command
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unknown_cmd_resps
                            
                            	Responses to unknown command
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unknown_service_cmd_resps
                            
                            	Responses to unknown service command
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.account_logoff = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogoff()
                                self.account_logoff.parent = self
                                self.account_logon = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogon()
                                self.account_logon.parent = self
                                self.account_update = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountUpdate()
                                self.account_update.parent = self
                                self.attr_list_retrieve_failure_resps = None
                                self.internal_err_resps = None
                                self.no_cmd_resps = None
                                self.no_session_found_resps = None
                                self.no_session_peer_resps = None
                                self.resp_send_failure = None
                                self.service_multi = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.ServiceMulti()
                                self.service_multi.parent = self
                                self.service_profile_push_failure_resps = None
                                self.session_disconnect = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SessionDisconnect()
                                self.session_disconnect.parent = self
                                self.single_service_logoff = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogoff()
                                self.single_service_logoff.parent = self
                                self.single_service_logon = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogon()
                                self.single_service_logon.parent = self
                                self.single_service_modify = Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceModify()
                                self.single_service_modify.parent = self
                                self.unknown_account_cmd_resps = None
                                self.unknown_cmd_resps = None
                                self.unknown_service_cmd_resps = None


                            class AccountLogon(object):
                                """
                                Account logon request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.acknowledged_requests = None
                                    self.non_acknowledged_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:account-logon'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.acknowledged_requests is not None:
                                        return True

                                    if self.non_acknowledged_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogon']['meta_info']


                            class AccountLogoff(object):
                                """
                                Account logoff request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.acknowledged_requests = None
                                    self.non_acknowledged_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:account-logoff'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.acknowledged_requests is not None:
                                        return True

                                    if self.non_acknowledged_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountLogoff']['meta_info']


                            class AccountUpdate(object):
                                """
                                Account update request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.acknowledged_requests = None
                                    self.non_acknowledged_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:account-update'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.acknowledged_requests is not None:
                                        return True

                                    if self.non_acknowledged_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.AccountUpdate']['meta_info']


                            class SessionDisconnect(object):
                                """
                                Session disconnect request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.acknowledged_requests = None
                                    self.non_acknowledged_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:session-disconnect'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.acknowledged_requests is not None:
                                        return True

                                    if self.non_acknowledged_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SessionDisconnect']['meta_info']


                            class SingleServiceLogon(object):
                                """
                                Service logon request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.acknowledged_requests = None
                                    self.non_acknowledged_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:single-service-logon'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.acknowledged_requests is not None:
                                        return True

                                    if self.non_acknowledged_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogon']['meta_info']


                            class SingleServiceLogoff(object):
                                """
                                Single Service logoff request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.acknowledged_requests = None
                                    self.non_acknowledged_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:single-service-logoff'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.acknowledged_requests is not None:
                                        return True

                                    if self.non_acknowledged_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceLogoff']['meta_info']


                            class SingleServiceModify(object):
                                """
                                Single Service Modify request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.acknowledged_requests = None
                                    self.non_acknowledged_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:single-service-modify'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.acknowledged_requests is not None:
                                        return True

                                    if self.non_acknowledged_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.SingleServiceModify']['meta_info']


                            class ServiceMulti(object):
                                """
                                MA\-CoA Service request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.acknowledged_requests = None
                                    self.non_acknowledged_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:service-multi'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.acknowledged_requests is not None:
                                        return True

                                    if self.non_acknowledged_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization.ServiceMulti']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:change-of-authorization'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.account_logoff is not None and self.account_logoff._has_data():
                                    return True

                                if self.account_logon is not None and self.account_logon._has_data():
                                    return True

                                if self.account_update is not None and self.account_update._has_data():
                                    return True

                                if self.attr_list_retrieve_failure_resps is not None:
                                    return True

                                if self.internal_err_resps is not None:
                                    return True

                                if self.no_cmd_resps is not None:
                                    return True

                                if self.no_session_found_resps is not None:
                                    return True

                                if self.no_session_peer_resps is not None:
                                    return True

                                if self.resp_send_failure is not None:
                                    return True

                                if self.service_multi is not None and self.service_multi._has_data():
                                    return True

                                if self.service_profile_push_failure_resps is not None:
                                    return True

                                if self.session_disconnect is not None and self.session_disconnect._has_data():
                                    return True

                                if self.single_service_logoff is not None and self.single_service_logoff._has_data():
                                    return True

                                if self.single_service_logon is not None and self.single_service_logon._has_data():
                                    return True

                                if self.single_service_modify is not None and self.single_service_modify._has_data():
                                    return True

                                if self.unknown_account_cmd_resps is not None:
                                    return True

                                if self.unknown_cmd_resps is not None:
                                    return True

                                if self.unknown_service_cmd_resps is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.ChangeOfAuthorization']['meta_info']


                        class Authorization(object):
                            """
                            Authorization statistics
                            
                            .. attribute:: accepted_requests
                            
                            	Request accepted by Radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: errored_requests
                            
                            	Unexpected errors
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: incomplete_requests
                            
                            	Incomplete requests \- missing attributes
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rejected_requests
                            
                            	Requests rejected by radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sent_requests
                            
                            	Requests sent to radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: successful_requests
                            
                            	Requests which are successful
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: terminated_requests
                            
                            	Requests terminated by disconnect
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unreachable_requests
                            
                            	Radius server not available
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.accepted_requests = None
                                self.errored_requests = None
                                self.incomplete_requests = None
                                self.rejected_requests = None
                                self.sent_requests = None
                                self.successful_requests = None
                                self.terminated_requests = None
                                self.unreachable_requests = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:authorization'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.accepted_requests is not None:
                                    return True

                                if self.errored_requests is not None:
                                    return True

                                if self.incomplete_requests is not None:
                                    return True

                                if self.rejected_requests is not None:
                                    return True

                                if self.sent_requests is not None:
                                    return True

                                if self.successful_requests is not None:
                                    return True

                                if self.terminated_requests is not None:
                                    return True

                                if self.unreachable_requests is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Authorization']['meta_info']


                        class AggregateAuthorization(object):
                            """
                            Aggregate authorization statistics
                            
                            .. attribute:: accepted_requests
                            
                            	Request accepted by Radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: errored_requests
                            
                            	Unexpected errors
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: incomplete_requests
                            
                            	Incomplete requests \- missing attributes
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rejected_requests
                            
                            	Requests rejected by radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sent_requests
                            
                            	Requests sent to radius server
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: successful_requests
                            
                            	Requests which are successful
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: terminated_requests
                            
                            	Requests terminated by disconnect
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unreachable_requests
                            
                            	Radius server not available
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.accepted_requests = None
                                self.errored_requests = None
                                self.incomplete_requests = None
                                self.rejected_requests = None
                                self.sent_requests = None
                                self.successful_requests = None
                                self.terminated_requests = None
                                self.unreachable_requests = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:aggregate-authorization'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.accepted_requests is not None:
                                    return True

                                if self.errored_requests is not None:
                                    return True

                                if self.incomplete_requests is not None:
                                    return True

                                if self.rejected_requests is not None:
                                    return True

                                if self.sent_requests is not None:
                                    return True

                                if self.successful_requests is not None:
                                    return True

                                if self.terminated_requests is not None:
                                    return True

                                if self.unreachable_requests is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateAuthorization']['meta_info']


                        class Accounting(object):
                            """
                            Accounting statistics
                            
                            .. attribute:: active_sessions
                            
                            	Active sessions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: interim
                            
                            	Interim statistics
                            	**type**\:   :py:class:`Interim <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Interim>`
                            
                            .. attribute:: interim_inflight
                            
                            	Interim inflight details
                            	**type**\:   :py:class:`InterimInflight <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.InterimInflight>`
                            
                            .. attribute:: pass_through
                            
                            	Pass\-through statistics
                            	**type**\:   :py:class:`PassThrough <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.PassThrough>`
                            
                            .. attribute:: policy_plane_errored_requests
                            
                            	Policy plane errored requests
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: policy_plane_unknown_requests
                            
                            	Policy plane unknown requests
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: start
                            
                            	Start statistics
                            	**type**\:   :py:class:`Start <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Start>`
                            
                            .. attribute:: started_sessions
                            
                            	Started sessions
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: stop
                            
                            	Stop statistics
                            	**type**\:   :py:class:`Stop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Stop>`
                            
                            .. attribute:: stopped_sessions
                            
                            	Stopped sessions
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: update
                            
                            	Update statistics
                            	**type**\:   :py:class:`Update <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Update>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.active_sessions = None
                                self.interim = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Interim()
                                self.interim.parent = self
                                self.interim_inflight = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.InterimInflight()
                                self.interim_inflight.parent = self
                                self.pass_through = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.PassThrough()
                                self.pass_through.parent = self
                                self.policy_plane_errored_requests = None
                                self.policy_plane_unknown_requests = None
                                self.start = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Start()
                                self.start.parent = self
                                self.started_sessions = None
                                self.stop = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Stop()
                                self.stop.parent = self
                                self.stopped_sessions = None
                                self.update = Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Update()
                                self.update.parent = self


                            class Start(object):
                                """
                                Start statistics
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.aaa_errored_requests = None
                                    self.aaa_failed_responses = None
                                    self.aaa_sent_requests = None
                                    self.aaa_succeeded_responses = None
                                    self.errored_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:start'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.aaa_errored_requests is not None:
                                        return True

                                    if self.aaa_failed_responses is not None:
                                        return True

                                    if self.aaa_sent_requests is not None:
                                        return True

                                    if self.aaa_succeeded_responses is not None:
                                        return True

                                    if self.errored_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Start']['meta_info']


                            class Stop(object):
                                """
                                Stop statistics
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.aaa_errored_requests = None
                                    self.aaa_failed_responses = None
                                    self.aaa_sent_requests = None
                                    self.aaa_succeeded_responses = None
                                    self.errored_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:stop'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.aaa_errored_requests is not None:
                                        return True

                                    if self.aaa_failed_responses is not None:
                                        return True

                                    if self.aaa_sent_requests is not None:
                                        return True

                                    if self.aaa_succeeded_responses is not None:
                                        return True

                                    if self.errored_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Stop']['meta_info']


                            class Interim(object):
                                """
                                Interim statistics
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.aaa_errored_requests = None
                                    self.aaa_failed_responses = None
                                    self.aaa_sent_requests = None
                                    self.aaa_succeeded_responses = None
                                    self.errored_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:interim'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.aaa_errored_requests is not None:
                                        return True

                                    if self.aaa_failed_responses is not None:
                                        return True

                                    if self.aaa_sent_requests is not None:
                                        return True

                                    if self.aaa_succeeded_responses is not None:
                                        return True

                                    if self.errored_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Interim']['meta_info']


                            class PassThrough(object):
                                """
                                Pass\-through statistics
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.aaa_errored_requests = None
                                    self.aaa_failed_responses = None
                                    self.aaa_sent_requests = None
                                    self.aaa_succeeded_responses = None
                                    self.errored_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pass-through'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.aaa_errored_requests is not None:
                                        return True

                                    if self.aaa_failed_responses is not None:
                                        return True

                                    if self.aaa_sent_requests is not None:
                                        return True

                                    if self.aaa_succeeded_responses is not None:
                                        return True

                                    if self.errored_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.PassThrough']['meta_info']


                            class Update(object):
                                """
                                Update statistics
                                
                                .. attribute:: aaa_errored_requests
                                
                                	AAA errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_failed_responses
                                
                                	AAA failed responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_sent_requests
                                
                                	AAA requests sent
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: aaa_succeeded_responses
                                
                                	AAA succeeded responses
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: errored_requests
                                
                                	Errored requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.aaa_errored_requests = None
                                    self.aaa_failed_responses = None
                                    self.aaa_sent_requests = None
                                    self.aaa_succeeded_responses = None
                                    self.errored_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:update'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.aaa_errored_requests is not None:
                                        return True

                                    if self.aaa_failed_responses is not None:
                                        return True

                                    if self.aaa_sent_requests is not None:
                                        return True

                                    if self.aaa_succeeded_responses is not None:
                                        return True

                                    if self.errored_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.Update']['meta_info']


                            class InterimInflight(object):
                                """
                                Interim inflight details
                                
                                .. attribute:: accepted_requests
                                
                                	Accepted requests
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: denied_requests
                                
                                	Denied requests
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: low_water_mark_quota_of_requests
                                
                                	Low water mark quota of requests
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: quota_exhausts
                                
                                	Quota exhausts
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: remaining_quota_of_requests
                                
                                	Remaining quota of requests
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: total_quota_of_requests
                                
                                	Total quota of requests
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.accepted_requests = None
                                    self.denied_requests = None
                                    self.low_water_mark_quota_of_requests = None
                                    self.quota_exhausts = None
                                    self.remaining_quota_of_requests = None
                                    self.total_quota_of_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:interim-inflight'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.accepted_requests is not None:
                                        return True

                                    if self.denied_requests is not None:
                                        return True

                                    if self.low_water_mark_quota_of_requests is not None:
                                        return True

                                    if self.quota_exhausts is not None:
                                        return True

                                    if self.remaining_quota_of_requests is not None:
                                        return True

                                    if self.total_quota_of_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting.InterimInflight']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:accounting'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.active_sessions is not None:
                                    return True

                                if self.interim is not None and self.interim._has_data():
                                    return True

                                if self.interim_inflight is not None and self.interim_inflight._has_data():
                                    return True

                                if self.pass_through is not None and self.pass_through._has_data():
                                    return True

                                if self.policy_plane_errored_requests is not None:
                                    return True

                                if self.policy_plane_unknown_requests is not None:
                                    return True

                                if self.start is not None and self.start._has_data():
                                    return True

                                if self.started_sessions is not None:
                                    return True

                                if self.stop is not None and self.stop._has_data():
                                    return True

                                if self.stopped_sessions is not None:
                                    return True

                                if self.update is not None and self.update._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Accounting']['meta_info']


                        class Mobility(object):
                            """
                            Mobility statistics
                            
                            .. attribute:: receive_response_failures
                            
                            	Response receive failures
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: receive_response_successes
                            
                            	Response receive success
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: send_request_failures
                            
                            	Request send failures
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: send_request_successes
                            
                            	Request send success
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.receive_response_failures = None
                                self.receive_response_successes = None
                                self.send_request_failures = None
                                self.send_request_successes = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:mobility'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.receive_response_failures is not None:
                                    return True

                                if self.receive_response_successes is not None:
                                    return True

                                if self.send_request_failures is not None:
                                    return True

                                if self.send_request_successes is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.Mobility']['meta_info']


                        class AggregateChangeOfAuthorization(object):
                            """
                            Aggregate change of authorization (COA)
                            statistics
                            
                            .. attribute:: account_logoff
                            
                            	Account logoff request statistics
                            	**type**\:   :py:class:`AccountLogoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogoff>`
                            
                            .. attribute:: account_logon
                            
                            	Account logon request statistics
                            	**type**\:   :py:class:`AccountLogon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogon>`
                            
                            .. attribute:: account_update
                            
                            	Account update request statistics
                            	**type**\:   :py:class:`AccountUpdate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountUpdate>`
                            
                            .. attribute:: attr_list_retrieve_failure_resps
                            
                            	Responses to attribute list failure errors
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: internal_err_resps
                            
                            	Responses to internal error
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: no_cmd_resps
                            
                            	Responses empty (no command) COA request
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: no_session_found_resps
                            
                            	Responses to COA with unknown session identifier
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: no_session_peer_resps
                            
                            	Responses to session peer not found error
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: resp_send_failure
                            
                            	Response send failures
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: service_multi
                            
                            	MA\-CoA Service request statistics
                            	**type**\:   :py:class:`ServiceMulti <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.ServiceMulti>`
                            
                            .. attribute:: service_profile_push_failure_resps
                            
                            	Responses to service profile push failures
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: session_disconnect
                            
                            	Session disconnect request statistics
                            	**type**\:   :py:class:`SessionDisconnect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SessionDisconnect>`
                            
                            .. attribute:: single_service_logoff
                            
                            	Single Service logoff request statistics
                            	**type**\:   :py:class:`SingleServiceLogoff <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogoff>`
                            
                            .. attribute:: single_service_logon
                            
                            	Service logon request statistics
                            	**type**\:   :py:class:`SingleServiceLogon <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogon>`
                            
                            .. attribute:: single_service_modify
                            
                            	Single Service Modify request statistics
                            	**type**\:   :py:class:`SingleServiceModify <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceModify>`
                            
                            .. attribute:: unknown_account_cmd_resps
                            
                            	Responses to unknown account command
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unknown_cmd_resps
                            
                            	Responses to unknown command
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: unknown_service_cmd_resps
                            
                            	Responses to unknown service command
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.account_logoff = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogoff()
                                self.account_logoff.parent = self
                                self.account_logon = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogon()
                                self.account_logon.parent = self
                                self.account_update = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountUpdate()
                                self.account_update.parent = self
                                self.attr_list_retrieve_failure_resps = None
                                self.internal_err_resps = None
                                self.no_cmd_resps = None
                                self.no_session_found_resps = None
                                self.no_session_peer_resps = None
                                self.resp_send_failure = None
                                self.service_multi = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.ServiceMulti()
                                self.service_multi.parent = self
                                self.service_profile_push_failure_resps = None
                                self.session_disconnect = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SessionDisconnect()
                                self.session_disconnect.parent = self
                                self.single_service_logoff = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogoff()
                                self.single_service_logoff.parent = self
                                self.single_service_logon = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogon()
                                self.single_service_logon.parent = self
                                self.single_service_modify = Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceModify()
                                self.single_service_modify.parent = self
                                self.unknown_account_cmd_resps = None
                                self.unknown_cmd_resps = None
                                self.unknown_service_cmd_resps = None


                            class AccountLogon(object):
                                """
                                Account logon request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.acknowledged_requests = None
                                    self.non_acknowledged_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:account-logon'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.acknowledged_requests is not None:
                                        return True

                                    if self.non_acknowledged_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogon']['meta_info']


                            class AccountLogoff(object):
                                """
                                Account logoff request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.acknowledged_requests = None
                                    self.non_acknowledged_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:account-logoff'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.acknowledged_requests is not None:
                                        return True

                                    if self.non_acknowledged_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountLogoff']['meta_info']


                            class AccountUpdate(object):
                                """
                                Account update request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.acknowledged_requests = None
                                    self.non_acknowledged_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:account-update'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.acknowledged_requests is not None:
                                        return True

                                    if self.non_acknowledged_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.AccountUpdate']['meta_info']


                            class SessionDisconnect(object):
                                """
                                Session disconnect request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.acknowledged_requests = None
                                    self.non_acknowledged_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:session-disconnect'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.acknowledged_requests is not None:
                                        return True

                                    if self.non_acknowledged_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SessionDisconnect']['meta_info']


                            class SingleServiceLogon(object):
                                """
                                Service logon request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.acknowledged_requests = None
                                    self.non_acknowledged_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:single-service-logon'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.acknowledged_requests is not None:
                                        return True

                                    if self.non_acknowledged_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogon']['meta_info']


                            class SingleServiceLogoff(object):
                                """
                                Single Service logoff request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.acknowledged_requests = None
                                    self.non_acknowledged_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:single-service-logoff'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.acknowledged_requests is not None:
                                        return True

                                    if self.non_acknowledged_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceLogoff']['meta_info']


                            class SingleServiceModify(object):
                                """
                                Single Service Modify request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.acknowledged_requests = None
                                    self.non_acknowledged_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:single-service-modify'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.acknowledged_requests is not None:
                                        return True

                                    if self.non_acknowledged_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.SingleServiceModify']['meta_info']


                            class ServiceMulti(object):
                                """
                                MA\-CoA Service request statistics
                                
                                .. attribute:: acknowledged_requests
                                
                                	Acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: non_acknowledged_requests
                                
                                	Non acknowledged requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_requests
                                
                                	Received requests
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.acknowledged_requests = None
                                    self.non_acknowledged_requests = None
                                    self.received_requests = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:service-multi'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.acknowledged_requests is not None:
                                        return True

                                    if self.non_acknowledged_requests is not None:
                                        return True

                                    if self.received_requests is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization.ServiceMulti']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:aggregate-change-of-authorization'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.account_logoff is not None and self.account_logoff._has_data():
                                    return True

                                if self.account_logon is not None and self.account_logon._has_data():
                                    return True

                                if self.account_update is not None and self.account_update._has_data():
                                    return True

                                if self.attr_list_retrieve_failure_resps is not None:
                                    return True

                                if self.internal_err_resps is not None:
                                    return True

                                if self.no_cmd_resps is not None:
                                    return True

                                if self.no_session_found_resps is not None:
                                    return True

                                if self.no_session_peer_resps is not None:
                                    return True

                                if self.resp_send_failure is not None:
                                    return True

                                if self.service_multi is not None and self.service_multi._has_data():
                                    return True

                                if self.service_profile_push_failure_resps is not None:
                                    return True

                                if self.session_disconnect is not None and self.session_disconnect._has_data():
                                    return True

                                if self.single_service_logoff is not None and self.single_service_logoff._has_data():
                                    return True

                                if self.single_service_logon is not None and self.single_service_logon._has_data():
                                    return True

                                if self.single_service_modify is not None and self.single_service_modify._has_data():
                                    return True

                                if self.unknown_account_cmd_resps is not None:
                                    return True

                                if self.unknown_cmd_resps is not None:
                                    return True

                                if self.unknown_service_cmd_resps is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa.AggregateChangeOfAuthorization']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:aaa'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.accounting is not None and self.accounting._has_data():
                                return True

                            if self.aggregate_accounting is not None and self.aggregate_accounting._has_data():
                                return True

                            if self.aggregate_authentication is not None and self.aggregate_authentication._has_data():
                                return True

                            if self.aggregate_authorization is not None and self.aggregate_authorization._has_data():
                                return True

                            if self.aggregate_change_of_authorization is not None and self.aggregate_change_of_authorization._has_data():
                                return True

                            if self.aggregate_mobility is not None and self.aggregate_mobility._has_data():
                                return True

                            if self.authentication is not None and self.authentication._has_data():
                                return True

                            if self.authorization is not None and self.authorization._has_data():
                                return True

                            if self.change_of_authorization is not None and self.change_of_authorization._has_data():
                                return True

                            if self.mobility is not None and self.mobility._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                            return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Aaa']['meta_info']


                    class AggregateSummary(object):
                        """
                        Aggregate summary of statistics
                        
                        .. attribute:: calling_station_id_attribute_format_warnings
                        
                        	Calling station ID attribute format warnings
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: destination_station_id_attribute_format_warnings
                        
                        	Destination station ID attribute format warnings
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: install_user_profiles
                        
                        	User profiles installed
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: nas_port_attribute_format_warnings
                        
                        	NAS port attribute format warnings
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: nas_port_id_attribute_format_warnings
                        
                        	NAS port ID attribute format warnings
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: no_class_match_in_start_request
                        
                        	No control policy class match during subscriber start
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: no_subscriber_control_policy_on_interface
                        
                        	Subscriber control policy not applied on interface
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sess_disc_no_quota
                        
                        	Session Disconnect Request Queued, no quota
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sess_disc_none_started
                        
                        	Session Disconnect Requests not Dequeued, no quota
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sess_disc_q_count
                        
                        	Session Disconnect Requests Queued
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sess_disc_quota
                        
                        	Session Disconnect Quota
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sess_disc_quota_avail
                        
                        	Session Disconnect Request Accepted, quota available
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sess_disc_quota_exhausts
                        
                        	Session Disconnect Quota Exhausts
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sess_disc_quota_remaining
                        
                        	Session Disconnect Quota Remaining
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sess_disc_recon_ip
                        
                        	Session Disconnect Requests not Dequeued, reconciliation in progress
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: user_profile_errors
                        
                        	User profile errors
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: user_profile_install_errors
                        
                        	User profile install errors
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: user_profile_removals
                        
                        	User profile removals
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: username_attribute_format_warnings
                        
                        	Username attribute format warnings
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.calling_station_id_attribute_format_warnings = None
                            self.destination_station_id_attribute_format_warnings = None
                            self.install_user_profiles = None
                            self.nas_port_attribute_format_warnings = None
                            self.nas_port_id_attribute_format_warnings = None
                            self.no_class_match_in_start_request = None
                            self.no_subscriber_control_policy_on_interface = None
                            self.sess_disc_no_quota = None
                            self.sess_disc_none_started = None
                            self.sess_disc_q_count = None
                            self.sess_disc_quota = None
                            self.sess_disc_quota_avail = None
                            self.sess_disc_quota_exhausts = None
                            self.sess_disc_quota_remaining = None
                            self.sess_disc_recon_ip = None
                            self.user_profile_errors = None
                            self.user_profile_install_errors = None
                            self.user_profile_removals = None
                            self.username_attribute_format_warnings = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:aggregate-summary'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.calling_station_id_attribute_format_warnings is not None:
                                return True

                            if self.destination_station_id_attribute_format_warnings is not None:
                                return True

                            if self.install_user_profiles is not None:
                                return True

                            if self.nas_port_attribute_format_warnings is not None:
                                return True

                            if self.nas_port_id_attribute_format_warnings is not None:
                                return True

                            if self.no_class_match_in_start_request is not None:
                                return True

                            if self.no_subscriber_control_policy_on_interface is not None:
                                return True

                            if self.sess_disc_no_quota is not None:
                                return True

                            if self.sess_disc_none_started is not None:
                                return True

                            if self.sess_disc_q_count is not None:
                                return True

                            if self.sess_disc_quota is not None:
                                return True

                            if self.sess_disc_quota_avail is not None:
                                return True

                            if self.sess_disc_quota_exhausts is not None:
                                return True

                            if self.sess_disc_quota_remaining is not None:
                                return True

                            if self.sess_disc_recon_ip is not None:
                                return True

                            if self.user_profile_errors is not None:
                                return True

                            if self.user_profile_install_errors is not None:
                                return True

                            if self.user_profile_removals is not None:
                                return True

                            if self.username_attribute_format_warnings is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                            return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.AggregateSummary']['meta_info']


                    class Srg(object):
                        """
                        Geo Redundancy statistics
                        
                        .. attribute:: ack_to_srg
                        
                        	Number of ACKs sent to Srg
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: actual_txlist_sent
                        
                        	Txlist Send Success
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: alreadyin_txlist
                        
                        	Element already in Txlist
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: create_upd_clean_callback
                        
                        	Txlist Create/update clean callback
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: create_update_encode
                        
                        	Txlist Create Update Encode
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: delete_clean_callback
                        
                        	Txlist Delete clean callback
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: delete_encode
                        
                        	Txlist Delete Encode
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: eod_count
                        
                        	Number of EODs Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: flow_control_resume_threshold
                        
                        	Threshold Limit to resume the flow control
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_add_count
                        
                        	No.of inflight sessions added
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_alloc_fails
                        
                        	Memory Alloc Failures for Inflight Entry
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_delete_failures
                        
                        	Inflight Entry Delete Failures
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_deletes
                        
                        	Inflight Deletes Count
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_insert_failures
                        
                        	Inflight Entry Insert Failures
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_not_found
                        
                        	Inflight Entries not found during delete
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_session_count
                        
                        	No.of Sessions inflight at given time
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: inflight_under_run_count
                        
                        	Inflight Underrun Counter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_srg_flow_control_enabled
                        
                        	Flag indicating SRG Flow control enabled or not
                        	**type**\:  bool
                        
                        .. attribute:: last_pause_period
                        
                        	Amount of time paused during last flow control window
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: last_pause_time
                        
                        	Timestamp of recent Pause Event
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: last_resume_time
                        
                        	Timestamp of recent Resume Event
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: max_inflight_sessoin_count
                        
                        	Maximum no.of inflight sessions allowed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nack_to_srg
                        
                        	Number of NACKs sent to Srg
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nack_to_srg_fail_cnt
                        
                        	Number of NACKs Failed to send to Srg
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: slave_create_update
                        
                        	Create Update received on slave
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: slave_decode_fail
                        
                        	Decode failed on Slave
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: slave_delete
                        
                        	Delete received on slave
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: slave_recv_entry
                        
                        	Slave Recieved Sync
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sod_count
                        
                        	Number of SODs Received
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sod_eod_dirty_delete_count
                        
                        	Number of Sessions Invalid Deletes Within SOD EOD Window
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sod_eod_dirty_mark_count
                        
                        	Number of Sessions Marked as Invalid Within SOD EOD Window
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sod_eod_replay_req_count
                        
                        	Number of Replay Requests Within SOD EOD Window
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: srg_context_free
                        
                        	SRG context freed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: srg_context_malloc
                        
                        	SRG context allocated
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_dont_send_to_txlist
                        
                        	Total No of times Dont send to Txlist
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_master_eoms_pending
                        
                        	Total No of times Master EOMS Pending
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_pause_count
                        
                        	Total No.of times Pause is Enabled
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_pause_time
                        
                        	Total Amount of time paused during all flow control windows
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: total_resume_count
                        
                        	Total No.of times Resume is triggered
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_srg_not_master
                        
                        	Total No of times SRG Not Master
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_clean_invalid_state
                        
                        	Number of Txlist Cleanup called on Invalid subscriber srg state
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_del_app
                        
                        	Number of Txlist delete for App msg
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_del_app_notlinked
                        
                        	Number of Txlist delete for App which are not linked
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_del_sync
                        
                        	Number for Txlist delete for sync msg
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_del_sync_notlinked
                        
                        	Number of Txlist delete for sync which are not linked
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_encode
                        
                        	Txlist Encode
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_encode_fail
                        
                        	Txlist encode Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_remove_all
                        
                        	Number of Txlist remove all calls
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_remove_all_internal_error
                        
                        	Number of Internal errors upon Master Txlist remove all call
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_send_failed
                        
                        	Txlist Send Failed
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_send_failed_notactive
                        
                        	Txlist send failed due to not active
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: txlist_send_triggered
                        
                        	Txlist Send Triggered
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ack_to_srg = None
                            self.actual_txlist_sent = None
                            self.alreadyin_txlist = None
                            self.create_upd_clean_callback = None
                            self.create_update_encode = None
                            self.delete_clean_callback = None
                            self.delete_encode = None
                            self.eod_count = None
                            self.flow_control_resume_threshold = None
                            self.inflight_add_count = None
                            self.inflight_alloc_fails = None
                            self.inflight_delete_failures = None
                            self.inflight_deletes = None
                            self.inflight_insert_failures = None
                            self.inflight_not_found = None
                            self.inflight_session_count = None
                            self.inflight_under_run_count = None
                            self.is_srg_flow_control_enabled = None
                            self.last_pause_period = None
                            self.last_pause_time = None
                            self.last_resume_time = None
                            self.max_inflight_sessoin_count = None
                            self.nack_to_srg = None
                            self.nack_to_srg_fail_cnt = None
                            self.slave_create_update = None
                            self.slave_decode_fail = None
                            self.slave_delete = None
                            self.slave_recv_entry = None
                            self.sod_count = None
                            self.sod_eod_dirty_delete_count = None
                            self.sod_eod_dirty_mark_count = None
                            self.sod_eod_replay_req_count = None
                            self.srg_context_free = None
                            self.srg_context_malloc = None
                            self.total_dont_send_to_txlist = None
                            self.total_master_eoms_pending = None
                            self.total_pause_count = None
                            self.total_pause_time = None
                            self.total_resume_count = None
                            self.total_srg_not_master = None
                            self.txlist_clean_invalid_state = None
                            self.txlist_del_app = None
                            self.txlist_del_app_notlinked = None
                            self.txlist_del_sync = None
                            self.txlist_del_sync_notlinked = None
                            self.txlist_encode = None
                            self.txlist_encode_fail = None
                            self.txlist_remove_all = None
                            self.txlist_remove_all_internal_error = None
                            self.txlist_send_failed = None
                            self.txlist_send_failed_notactive = None
                            self.txlist_send_triggered = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:srg'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.ack_to_srg is not None:
                                return True

                            if self.actual_txlist_sent is not None:
                                return True

                            if self.alreadyin_txlist is not None:
                                return True

                            if self.create_upd_clean_callback is not None:
                                return True

                            if self.create_update_encode is not None:
                                return True

                            if self.delete_clean_callback is not None:
                                return True

                            if self.delete_encode is not None:
                                return True

                            if self.eod_count is not None:
                                return True

                            if self.flow_control_resume_threshold is not None:
                                return True

                            if self.inflight_add_count is not None:
                                return True

                            if self.inflight_alloc_fails is not None:
                                return True

                            if self.inflight_delete_failures is not None:
                                return True

                            if self.inflight_deletes is not None:
                                return True

                            if self.inflight_insert_failures is not None:
                                return True

                            if self.inflight_not_found is not None:
                                return True

                            if self.inflight_session_count is not None:
                                return True

                            if self.inflight_under_run_count is not None:
                                return True

                            if self.is_srg_flow_control_enabled is not None:
                                return True

                            if self.last_pause_period is not None:
                                return True

                            if self.last_pause_time is not None:
                                return True

                            if self.last_resume_time is not None:
                                return True

                            if self.max_inflight_sessoin_count is not None:
                                return True

                            if self.nack_to_srg is not None:
                                return True

                            if self.nack_to_srg_fail_cnt is not None:
                                return True

                            if self.slave_create_update is not None:
                                return True

                            if self.slave_decode_fail is not None:
                                return True

                            if self.slave_delete is not None:
                                return True

                            if self.slave_recv_entry is not None:
                                return True

                            if self.sod_count is not None:
                                return True

                            if self.sod_eod_dirty_delete_count is not None:
                                return True

                            if self.sod_eod_dirty_mark_count is not None:
                                return True

                            if self.sod_eod_replay_req_count is not None:
                                return True

                            if self.srg_context_free is not None:
                                return True

                            if self.srg_context_malloc is not None:
                                return True

                            if self.total_dont_send_to_txlist is not None:
                                return True

                            if self.total_master_eoms_pending is not None:
                                return True

                            if self.total_pause_count is not None:
                                return True

                            if self.total_pause_time is not None:
                                return True

                            if self.total_resume_count is not None:
                                return True

                            if self.total_srg_not_master is not None:
                                return True

                            if self.txlist_clean_invalid_state is not None:
                                return True

                            if self.txlist_del_app is not None:
                                return True

                            if self.txlist_del_app_notlinked is not None:
                                return True

                            if self.txlist_del_sync is not None:
                                return True

                            if self.txlist_del_sync_notlinked is not None:
                                return True

                            if self.txlist_encode is not None:
                                return True

                            if self.txlist_encode_fail is not None:
                                return True

                            if self.txlist_remove_all is not None:
                                return True

                            if self.txlist_remove_all_internal_error is not None:
                                return True

                            if self.txlist_send_failed is not None:
                                return True

                            if self.txlist_send_failed_notactive is not None:
                                return True

                            if self.txlist_send_triggered is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                            return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics.Srg']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.aaa is not None and self.aaa._has_data():
                            return True

                        if self.aggregate_summary is not None and self.aggregate_summary._has_data():
                            return True

                        if self.srg is not None and self.srg._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                        return meta._meta_table['Subscriber.Manager.Nodes.Node.Statistics']['meta_info']

                @property
                def _common_path(self):
                    if self.node_name is None:
                        raise YPYModelError('Key property node_name is None')

                    return '/Cisco-IOS-XR-iedge4710-oper:subscriber/Cisco-IOS-XR-iedge4710-oper:manager/Cisco-IOS-XR-iedge4710-oper:nodes/Cisco-IOS-XR-iedge4710-oper:node[Cisco-IOS-XR-iedge4710-oper:node-name = ' + str(self.node_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.node_name is not None:
                        return True

                    if self.statistics is not None and self.statistics._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                    return meta._meta_table['Subscriber.Manager.Nodes.Node']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-iedge4710-oper:subscriber/Cisco-IOS-XR-iedge4710-oper:manager/Cisco-IOS-XR-iedge4710-oper:nodes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.node is not None:
                    for child_ref in self.node:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                return meta._meta_table['Subscriber.Manager.Nodes']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-iedge4710-oper:subscriber/Cisco-IOS-XR-iedge4710-oper:manager'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.nodes is not None and self.nodes._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
            return meta._meta_table['Subscriber.Manager']['meta_info']


    class Session(object):
        """
        Subscriber session operational data
        
        .. attribute:: nodes
        
        	List of subscriber session supported nodes
        	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes>`
        
        

        """

        _prefix = 'iedge4710-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.nodes = Subscriber.Session.Nodes()
            self.nodes.parent = self


        class Nodes(object):
            """
            List of subscriber session supported nodes
            
            .. attribute:: node
            
            	Subscriber session operational data for a particular node
            	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node>`
            
            

            """

            _prefix = 'iedge4710-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node = YList()
                self.node.parent = self
                self.node.name = 'node'


            class Node(object):
                """
                Subscriber session operational data for a
                particular node
                
                .. attribute:: node_name  <key>
                
                	Node name
                	**type**\:  str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: access_interface_summaries
                
                	Summary information filtered by access interface
                	**type**\:   :py:class:`AccessInterfaceSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries>`
                
                .. attribute:: address_family_summaries
                
                	Summary information filtered by address family
                	**type**\:   :py:class:`AddressFamilySummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries>`
                
                .. attribute:: authentication_summaries
                
                	Summary information filtered by authentication state
                	**type**\:   :py:class:`AuthenticationSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries>`
                
                .. attribute:: author_summaries
                
                	Summary information filtered by authorization state
                	**type**\:   :py:class:`AuthorSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries>`
                
                .. attribute:: interface_summaries
                
                	Summary information filtered by interface
                	**type**\:   :py:class:`InterfaceSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries>`
                
                .. attribute:: ipv4_address_summaries
                
                	Summary information filtered by subscriber IPv4 address
                	**type**\:   :py:class:`Ipv4AddressSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries>`
                
                .. attribute:: ipv4_address_vrf_summaries
                
                	Summary information filtered by IPv4 address and VRF
                	**type**\:   :py:class:`Ipv4AddressVrfSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries>`
                
                .. attribute:: mac_summaries
                
                	Summary information filtered by MAC address
                	**type**\:   :py:class:`MacSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries>`
                
                .. attribute:: sessions
                
                	IP subscriber sessions
                	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Sessions>`
                
                .. attribute:: state_summaries
                
                	Summary information filtered by session state
                	**type**\:   :py:class:`StateSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries>`
                
                .. attribute:: summary
                
                	Subscriber session summary information
                	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary>`
                
                .. attribute:: username_summaries
                
                	Summary information filtered by username
                	**type**\:   :py:class:`UsernameSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries>`
                
                .. attribute:: vrf_summaries
                
                	Summary information filtered by VRF
                	**type**\:   :py:class:`VrfSummaries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries>`
                
                

                """

                _prefix = 'iedge4710-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.node_name = None
                    self.access_interface_summaries = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries()
                    self.access_interface_summaries.parent = self
                    self.address_family_summaries = Subscriber.Session.Nodes.Node.AddressFamilySummaries()
                    self.address_family_summaries.parent = self
                    self.authentication_summaries = Subscriber.Session.Nodes.Node.AuthenticationSummaries()
                    self.authentication_summaries.parent = self
                    self.author_summaries = Subscriber.Session.Nodes.Node.AuthorSummaries()
                    self.author_summaries.parent = self
                    self.interface_summaries = Subscriber.Session.Nodes.Node.InterfaceSummaries()
                    self.interface_summaries.parent = self
                    self.ipv4_address_summaries = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries()
                    self.ipv4_address_summaries.parent = self
                    self.ipv4_address_vrf_summaries = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries()
                    self.ipv4_address_vrf_summaries.parent = self
                    self.mac_summaries = Subscriber.Session.Nodes.Node.MacSummaries()
                    self.mac_summaries.parent = self
                    self.sessions = Subscriber.Session.Nodes.Node.Sessions()
                    self.sessions.parent = self
                    self.state_summaries = Subscriber.Session.Nodes.Node.StateSummaries()
                    self.state_summaries.parent = self
                    self.summary = Subscriber.Session.Nodes.Node.Summary()
                    self.summary.parent = self
                    self.username_summaries = Subscriber.Session.Nodes.Node.UsernameSummaries()
                    self.username_summaries.parent = self
                    self.vrf_summaries = Subscriber.Session.Nodes.Node.VrfSummaries()
                    self.vrf_summaries.parent = self


                class AuthorSummaries(object):
                    """
                    Summary information filtered by authorization
                    state
                    
                    .. attribute:: author_summary
                    
                    	authorization summary
                    	**type**\: list of    :py:class:`AuthorSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.author_summary = YList()
                        self.author_summary.parent = self
                        self.author_summary.name = 'author_summary'


                    class AuthorSummary(object):
                        """
                        authorization summary
                        
                        .. attribute:: author_state  <key>
                        
                        	Authorization state
                        	**type**\:   :py:class:`SubscriberAuthorStateFilterFlagEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.SubscriberAuthorStateFilterFlagEnum>`
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.author_state = None
                            self.address_family_xr = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self.state_xr = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr()
                            self.state_xr.parent = self


                        class StateXr(object):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:state-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.StateXr']['meta_info']


                        class AddressFamilyXr(object):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:address-family-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary.AddressFamilyXr']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.author_state is None:
                                raise YPYModelError('Key property author_state is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:author-summary[Cisco-IOS-XR-iedge4710-oper:author-state = ' + str(self.author_state) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.author_state is not None:
                                return True

                            if self.address_family_xr is not None and self.address_family_xr._has_data():
                                return True

                            if self.state_xr is not None and self.state_xr._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                            return meta._meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries.AuthorSummary']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:author-summaries'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.author_summary is not None:
                            for child_ref in self.author_summary:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                        return meta._meta_table['Subscriber.Session.Nodes.Node.AuthorSummaries']['meta_info']


                class Summary(object):
                    """
                    Subscriber session summary information
                    
                    .. attribute:: address_family_xr
                    
                    	Address family summary
                    	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr>`
                    
                    .. attribute:: state_xr
                    
                    	State summary
                    	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.StateXr>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.address_family_xr = Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr()
                        self.address_family_xr.parent = self
                        self.state_xr = Subscriber.Session.Nodes.Node.Summary.StateXr()
                        self.state_xr.parent = self


                    class StateXr(object):
                        """
                        State summary
                        
                        .. attribute:: ip_subscriber_dhcp
                        
                        	IP subscriber DHCP summary
                        	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberDhcp>`
                        
                        .. attribute:: ip_subscriber_packet
                        
                        	IP subscriber packet summary
                        	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberPacket>`
                        
                        .. attribute:: pppoe
                        
                        	PPPoE summary
                        	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.StateXr.Pppoe>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberDhcp()
                            self.ip_subscriber_dhcp.parent = self
                            self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberPacket()
                            self.ip_subscriber_packet.parent = self
                            self.pppoe = Subscriber.Session.Nodes.Node.Summary.StateXr.Pppoe()
                            self.pppoe.parent = self


                        class Pppoe(object):
                            """
                            PPPoE summary
                            
                            .. attribute:: activated_sessions
                            
                            	Sessions in activated state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connected_sessions
                            
                            	Sessions in connected state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connecting_sessions
                            
                            	Sessions in connecting state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnecting_sessions
                            
                            	Sessions in disconnecting state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: end_sessions
                            
                            	Sessions in end state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: idle_sessions
                            
                            	Sessions in idle state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initialized_sessions
                            
                            	Sessions in initialized state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.activated_sessions = None
                                self.connected_sessions = None
                                self.connecting_sessions = None
                                self.disconnecting_sessions = None
                                self.end_sessions = None
                                self.idle_sessions = None
                                self.initialized_sessions = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.activated_sessions is not None:
                                    return True

                                if self.connected_sessions is not None:
                                    return True

                                if self.connecting_sessions is not None:
                                    return True

                                if self.disconnecting_sessions is not None:
                                    return True

                                if self.end_sessions is not None:
                                    return True

                                if self.idle_sessions is not None:
                                    return True

                                if self.initialized_sessions is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.Summary.StateXr.Pppoe']['meta_info']


                        class IpSubscriberDhcp(object):
                            """
                            IP subscriber DHCP summary
                            
                            .. attribute:: activated_sessions
                            
                            	Sessions in activated state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connected_sessions
                            
                            	Sessions in connected state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connecting_sessions
                            
                            	Sessions in connecting state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnecting_sessions
                            
                            	Sessions in disconnecting state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: end_sessions
                            
                            	Sessions in end state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: idle_sessions
                            
                            	Sessions in idle state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initialized_sessions
                            
                            	Sessions in initialized state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.activated_sessions = None
                                self.connected_sessions = None
                                self.connecting_sessions = None
                                self.disconnecting_sessions = None
                                self.end_sessions = None
                                self.idle_sessions = None
                                self.initialized_sessions = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.activated_sessions is not None:
                                    return True

                                if self.connected_sessions is not None:
                                    return True

                                if self.connecting_sessions is not None:
                                    return True

                                if self.disconnecting_sessions is not None:
                                    return True

                                if self.end_sessions is not None:
                                    return True

                                if self.idle_sessions is not None:
                                    return True

                                if self.initialized_sessions is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberDhcp']['meta_info']


                        class IpSubscriberPacket(object):
                            """
                            IP subscriber packet summary
                            
                            .. attribute:: activated_sessions
                            
                            	Sessions in activated state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connected_sessions
                            
                            	Sessions in connected state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connecting_sessions
                            
                            	Sessions in connecting state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: disconnecting_sessions
                            
                            	Sessions in disconnecting state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: end_sessions
                            
                            	Sessions in end state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: idle_sessions
                            
                            	Sessions in idle state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: initialized_sessions
                            
                            	Sessions in initialized state
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.activated_sessions = None
                                self.connected_sessions = None
                                self.connecting_sessions = None
                                self.disconnecting_sessions = None
                                self.end_sessions = None
                                self.idle_sessions = None
                                self.initialized_sessions = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.activated_sessions is not None:
                                    return True

                                if self.connected_sessions is not None:
                                    return True

                                if self.connecting_sessions is not None:
                                    return True

                                if self.disconnecting_sessions is not None:
                                    return True

                                if self.end_sessions is not None:
                                    return True

                                if self.idle_sessions is not None:
                                    return True

                                if self.initialized_sessions is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.Summary.StateXr.IpSubscriberPacket']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:state-xr'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                return True

                            if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                return True

                            if self.pppoe is not None and self.pppoe._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                            return meta._meta_table['Subscriber.Session.Nodes.Node.Summary.StateXr']['meta_info']


                    class AddressFamilyXr(object):
                        """
                        Address family summary
                        
                        .. attribute:: ip_subscriber_dhcp
                        
                        	IP subscriber DHCP summary
                        	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberDhcp>`
                        
                        .. attribute:: ip_subscriber_packet
                        
                        	IP subscriber packet summary
                        	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberPacket>`
                        
                        .. attribute:: pppoe
                        
                        	PPPoE summary
                        	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.Pppoe>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberDhcp()
                            self.ip_subscriber_dhcp.parent = self
                            self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberPacket()
                            self.ip_subscriber_packet.parent = self
                            self.pppoe = Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.Pppoe()
                            self.pppoe.parent = self


                        class Pppoe(object):
                            """
                            PPPoE summary
                            
                            .. attribute:: dual_part_up_sessions
                            
                            	Dual stack partially up sessions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dual_up_sessions
                            
                            	Dual stack up sessions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_progress_sessions
                            
                            	Sessions with undecided address family
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv4_only_sessions
                            
                            	IPv4 only sessions 
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv6_only_sessions
                            
                            	IPv6 only sessions 
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: lac_sessions
                            
                            	LAC sessions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.dual_part_up_sessions = None
                                self.dual_up_sessions = None
                                self.in_progress_sessions = None
                                self.ipv4_only_sessions = None
                                self.ipv6_only_sessions = None
                                self.lac_sessions = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.dual_part_up_sessions is not None:
                                    return True

                                if self.dual_up_sessions is not None:
                                    return True

                                if self.in_progress_sessions is not None:
                                    return True

                                if self.ipv4_only_sessions is not None:
                                    return True

                                if self.ipv6_only_sessions is not None:
                                    return True

                                if self.lac_sessions is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.Pppoe']['meta_info']


                        class IpSubscriberDhcp(object):
                            """
                            IP subscriber DHCP summary
                            
                            .. attribute:: dual_part_up_sessions
                            
                            	Dual stack partially up sessions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dual_up_sessions
                            
                            	Dual stack up sessions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_progress_sessions
                            
                            	Sessions with undecided address family
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv4_only_sessions
                            
                            	IPv4 only sessions 
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv6_only_sessions
                            
                            	IPv6 only sessions 
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: lac_sessions
                            
                            	LAC sessions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.dual_part_up_sessions = None
                                self.dual_up_sessions = None
                                self.in_progress_sessions = None
                                self.ipv4_only_sessions = None
                                self.ipv6_only_sessions = None
                                self.lac_sessions = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.dual_part_up_sessions is not None:
                                    return True

                                if self.dual_up_sessions is not None:
                                    return True

                                if self.in_progress_sessions is not None:
                                    return True

                                if self.ipv4_only_sessions is not None:
                                    return True

                                if self.ipv6_only_sessions is not None:
                                    return True

                                if self.lac_sessions is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberDhcp']['meta_info']


                        class IpSubscriberPacket(object):
                            """
                            IP subscriber packet summary
                            
                            .. attribute:: dual_part_up_sessions
                            
                            	Dual stack partially up sessions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dual_up_sessions
                            
                            	Dual stack up sessions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: in_progress_sessions
                            
                            	Sessions with undecided address family
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv4_only_sessions
                            
                            	IPv4 only sessions 
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv6_only_sessions
                            
                            	IPv6 only sessions 
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: lac_sessions
                            
                            	LAC sessions
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.dual_part_up_sessions = None
                                self.dual_up_sessions = None
                                self.in_progress_sessions = None
                                self.ipv4_only_sessions = None
                                self.ipv6_only_sessions = None
                                self.lac_sessions = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.dual_part_up_sessions is not None:
                                    return True

                                if self.dual_up_sessions is not None:
                                    return True

                                if self.in_progress_sessions is not None:
                                    return True

                                if self.ipv4_only_sessions is not None:
                                    return True

                                if self.ipv6_only_sessions is not None:
                                    return True

                                if self.lac_sessions is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr.IpSubscriberPacket']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:address-family-xr'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                return True

                            if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                return True

                            if self.pppoe is not None and self.pppoe._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                            return meta._meta_table['Subscriber.Session.Nodes.Node.Summary.AddressFamilyXr']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:summary'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.address_family_xr is not None and self.address_family_xr._has_data():
                            return True

                        if self.state_xr is not None and self.state_xr._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                        return meta._meta_table['Subscriber.Session.Nodes.Node.Summary']['meta_info']


                class MacSummaries(object):
                    """
                    Summary information filtered by MAC address
                    
                    .. attribute:: mac_summary
                    
                    	MAC address summary
                    	**type**\: list of    :py:class:`MacSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.mac_summary = YList()
                        self.mac_summary.parent = self
                        self.mac_summary.name = 'mac_summary'


                    class MacSummary(object):
                        """
                        MAC address summary
                        
                        .. attribute:: mac_address  <key>
                        
                        	Subscriber MAC address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.mac_address = None
                            self.address_family_xr = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self.state_xr = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr()
                            self.state_xr.parent = self


                        class StateXr(object):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:state-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.StateXr']['meta_info']


                        class AddressFamilyXr(object):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:address-family-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary.AddressFamilyXr']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.mac_address is None:
                                raise YPYModelError('Key property mac_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:mac-summary[Cisco-IOS-XR-iedge4710-oper:mac-address = ' + str(self.mac_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.mac_address is not None:
                                return True

                            if self.address_family_xr is not None and self.address_family_xr._has_data():
                                return True

                            if self.state_xr is not None and self.state_xr._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                            return meta._meta_table['Subscriber.Session.Nodes.Node.MacSummaries.MacSummary']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:mac-summaries'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.mac_summary is not None:
                            for child_ref in self.mac_summary:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                        return meta._meta_table['Subscriber.Session.Nodes.Node.MacSummaries']['meta_info']


                class InterfaceSummaries(object):
                    """
                    Summary information filtered by interface
                    
                    .. attribute:: interface_summary
                    
                    	Interface summary
                    	**type**\: list of    :py:class:`InterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface_summary = YList()
                        self.interface_summary.parent = self
                        self.interface_summary.name = 'interface_summary'


                    class InterfaceSummary(object):
                        """
                        Interface summary
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None
                            self.address_family_xr = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self.state_xr = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr()
                            self.state_xr.parent = self


                        class StateXr(object):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:state-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.StateXr']['meta_info']


                        class AddressFamilyXr(object):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:address-family-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary.AddressFamilyXr']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.interface_name is None:
                                raise YPYModelError('Key property interface_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:interface-summary[Cisco-IOS-XR-iedge4710-oper:interface-name = ' + str(self.interface_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.interface_name is not None:
                                return True

                            if self.address_family_xr is not None and self.address_family_xr._has_data():
                                return True

                            if self.state_xr is not None and self.state_xr._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                            return meta._meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries.InterfaceSummary']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:interface-summaries'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.interface_summary is not None:
                            for child_ref in self.interface_summary:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                        return meta._meta_table['Subscriber.Session.Nodes.Node.InterfaceSummaries']['meta_info']


                class AuthenticationSummaries(object):
                    """
                    Summary information filtered by
                    authentication state
                    
                    .. attribute:: authentication_summary
                    
                    	authentication summary
                    	**type**\: list of    :py:class:`AuthenticationSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.authentication_summary = YList()
                        self.authentication_summary.parent = self
                        self.authentication_summary.name = 'authentication_summary'


                    class AuthenticationSummary(object):
                        """
                        authentication summary
                        
                        .. attribute:: authentication_state  <key>
                        
                        	Authentication state
                        	**type**\:   :py:class:`SubscriberAuthenStateFilterFlagEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.SubscriberAuthenStateFilterFlagEnum>`
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.authentication_state = None
                            self.address_family_xr = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self.state_xr = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr()
                            self.state_xr.parent = self


                        class StateXr(object):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:state-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.StateXr']['meta_info']


                        class AddressFamilyXr(object):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:address-family-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary.AddressFamilyXr']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.authentication_state is None:
                                raise YPYModelError('Key property authentication_state is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:authentication-summary[Cisco-IOS-XR-iedge4710-oper:authentication-state = ' + str(self.authentication_state) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.authentication_state is not None:
                                return True

                            if self.address_family_xr is not None and self.address_family_xr._has_data():
                                return True

                            if self.state_xr is not None and self.state_xr._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                            return meta._meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries.AuthenticationSummary']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:authentication-summaries'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.authentication_summary is not None:
                            for child_ref in self.authentication_summary:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                        return meta._meta_table['Subscriber.Session.Nodes.Node.AuthenticationSummaries']['meta_info']


                class StateSummaries(object):
                    """
                    Summary information filtered by session state
                    
                    .. attribute:: state_summary
                    
                    	State summary
                    	**type**\: list of    :py:class:`StateSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.state_summary = YList()
                        self.state_summary.parent = self
                        self.state_summary.name = 'state_summary'


                    class StateSummary(object):
                        """
                        State summary
                        
                        .. attribute:: state  <key>
                        
                        	Subscriber state
                        	**type**\:   :py:class:`SubscriberStateFilterFlagEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.SubscriberStateFilterFlagEnum>`
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.state = None
                            self.address_family_xr = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self.state_xr = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr()
                            self.state_xr.parent = self


                        class StateXr(object):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:state-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.StateXr']['meta_info']


                        class AddressFamilyXr(object):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:address-family-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary.AddressFamilyXr']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.state is None:
                                raise YPYModelError('Key property state is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:state-summary[Cisco-IOS-XR-iedge4710-oper:state = ' + str(self.state) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.state is not None:
                                return True

                            if self.address_family_xr is not None and self.address_family_xr._has_data():
                                return True

                            if self.state_xr is not None and self.state_xr._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                            return meta._meta_table['Subscriber.Session.Nodes.Node.StateSummaries.StateSummary']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:state-summaries'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.state_summary is not None:
                            for child_ref in self.state_summary:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                        return meta._meta_table['Subscriber.Session.Nodes.Node.StateSummaries']['meta_info']


                class Ipv4AddressVrfSummaries(object):
                    """
                    Summary information filtered by IPv4 address
                    and VRF
                    
                    .. attribute:: ipv4_address_vrf_summary
                    
                    	IPv4 address and VRF summary
                    	**type**\: list of    :py:class:`Ipv4AddressVrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ipv4_address_vrf_summary = YList()
                        self.ipv4_address_vrf_summary.parent = self
                        self.ipv4_address_vrf_summary.name = 'ipv4_address_vrf_summary'


                    class Ipv4AddressVrfSummary(object):
                        """
                        IPv4 address and VRF summary
                        
                        .. attribute:: address
                        
                        	Subscriber IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr>`
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.address = None
                            self.address_family_xr = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self.state_xr = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr()
                            self.state_xr.parent = self
                            self.vrf_name = None


                        class StateXr(object):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:state-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.StateXr']['meta_info']


                        class AddressFamilyXr(object):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:address-family-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary.AddressFamilyXr']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ipv4-address-vrf-summary'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.address is not None:
                                return True

                            if self.address_family_xr is not None and self.address_family_xr._has_data():
                                return True

                            if self.state_xr is not None and self.state_xr._has_data():
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                            return meta._meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries.Ipv4AddressVrfSummary']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ipv4-address-vrf-summaries'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.ipv4_address_vrf_summary is not None:
                            for child_ref in self.ipv4_address_vrf_summary:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                        return meta._meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressVrfSummaries']['meta_info']


                class AddressFamilySummaries(object):
                    """
                    Summary information filtered by address
                    family
                    
                    .. attribute:: address_family_summary
                    
                    	Address family summary
                    	**type**\: list of    :py:class:`AddressFamilySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.address_family_summary = YList()
                        self.address_family_summary.parent = self
                        self.address_family_summary.name = 'address_family_summary'


                    class AddressFamilySummary(object):
                        """
                        Address family summary
                        
                        .. attribute:: address_family  <key>
                        
                        	Address family
                        	**type**\:   :py:class:`SubscriberAddressFamilyFilterFlagEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.SubscriberAddressFamilyFilterFlagEnum>`
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.address_family = None
                            self.address_family_xr = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self.state_xr = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr()
                            self.state_xr.parent = self


                        class StateXr(object):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:state-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.StateXr']['meta_info']


                        class AddressFamilyXr(object):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:address-family-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary.AddressFamilyXr']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.address_family is None:
                                raise YPYModelError('Key property address_family is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:address-family-summary[Cisco-IOS-XR-iedge4710-oper:address-family = ' + str(self.address_family) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.address_family is not None:
                                return True

                            if self.address_family_xr is not None and self.address_family_xr._has_data():
                                return True

                            if self.state_xr is not None and self.state_xr._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                            return meta._meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries.AddressFamilySummary']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:address-family-summaries'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.address_family_summary is not None:
                            for child_ref in self.address_family_summary:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                        return meta._meta_table['Subscriber.Session.Nodes.Node.AddressFamilySummaries']['meta_info']


                class UsernameSummaries(object):
                    """
                    Summary information filtered by username
                    
                    .. attribute:: username_summary
                    
                    	Username summary
                    	**type**\: list of    :py:class:`UsernameSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.username_summary = YList()
                        self.username_summary.parent = self
                        self.username_summary.name = 'username_summary'


                    class UsernameSummary(object):
                        """
                        Username summary
                        
                        .. attribute:: username  <key>
                        
                        	Subscriber username
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.username = None
                            self.address_family_xr = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self.state_xr = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr()
                            self.state_xr.parent = self


                        class StateXr(object):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:state-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.StateXr']['meta_info']


                        class AddressFamilyXr(object):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:address-family-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary.AddressFamilyXr']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.username is None:
                                raise YPYModelError('Key property username is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:username-summary[Cisco-IOS-XR-iedge4710-oper:username = ' + str(self.username) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.username is not None:
                                return True

                            if self.address_family_xr is not None and self.address_family_xr._has_data():
                                return True

                            if self.state_xr is not None and self.state_xr._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                            return meta._meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries.UsernameSummary']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:username-summaries'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.username_summary is not None:
                            for child_ref in self.username_summary:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                        return meta._meta_table['Subscriber.Session.Nodes.Node.UsernameSummaries']['meta_info']


                class AccessInterfaceSummaries(object):
                    """
                    Summary information filtered by access
                    interface
                    
                    .. attribute:: access_interface_summary
                    
                    	Access interface summary
                    	**type**\: list of    :py:class:`AccessInterfaceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.access_interface_summary = YList()
                        self.access_interface_summary.parent = self
                        self.access_interface_summary.name = 'access_interface_summary'


                    class AccessInterfaceSummary(object):
                        """
                        Access interface summary
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None
                            self.address_family_xr = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self.state_xr = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr()
                            self.state_xr.parent = self


                        class StateXr(object):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:state-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.StateXr']['meta_info']


                        class AddressFamilyXr(object):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:address-family-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary.AddressFamilyXr']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.interface_name is None:
                                raise YPYModelError('Key property interface_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:access-interface-summary[Cisco-IOS-XR-iedge4710-oper:interface-name = ' + str(self.interface_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.interface_name is not None:
                                return True

                            if self.address_family_xr is not None and self.address_family_xr._has_data():
                                return True

                            if self.state_xr is not None and self.state_xr._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                            return meta._meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries.AccessInterfaceSummary']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:access-interface-summaries'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.access_interface_summary is not None:
                            for child_ref in self.access_interface_summary:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                        return meta._meta_table['Subscriber.Session.Nodes.Node.AccessInterfaceSummaries']['meta_info']


                class Ipv4AddressSummaries(object):
                    """
                    Summary information filtered by subscriber
                    IPv4 address
                    
                    .. attribute:: ipv4_address_summary
                    
                    	IPv4 address summary
                    	**type**\: list of    :py:class:`Ipv4AddressSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ipv4_address_summary = YList()
                        self.ipv4_address_summary.parent = self
                        self.ipv4_address_summary.name = 'ipv4_address_summary'


                    class Ipv4AddressSummary(object):
                        """
                        IPv4 address summary
                        
                        .. attribute:: address  <key>
                        
                        	Subscriber IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.address = None
                            self.address_family_xr = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self.state_xr = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr()
                            self.state_xr.parent = self


                        class StateXr(object):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:state-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.StateXr']['meta_info']


                        class AddressFamilyXr(object):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:address-family-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary.AddressFamilyXr']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.address is None:
                                raise YPYModelError('Key property address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ipv4-address-summary[Cisco-IOS-XR-iedge4710-oper:address = ' + str(self.address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.address is not None:
                                return True

                            if self.address_family_xr is not None and self.address_family_xr._has_data():
                                return True

                            if self.state_xr is not None and self.state_xr._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                            return meta._meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries.Ipv4AddressSummary']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ipv4-address-summaries'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.ipv4_address_summary is not None:
                            for child_ref in self.ipv4_address_summary:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                        return meta._meta_table['Subscriber.Session.Nodes.Node.Ipv4AddressSummaries']['meta_info']


                class VrfSummaries(object):
                    """
                    Summary information filtered by VRF
                    
                    .. attribute:: vrf_summary
                    
                    	VRF summary
                    	**type**\: list of    :py:class:`VrfSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.vrf_summary = YList()
                        self.vrf_summary.parent = self
                        self.vrf_summary.name = 'vrf_summary'


                    class VrfSummary(object):
                        """
                        VRF summary
                        
                        .. attribute:: vrf_name  <key>
                        
                        	VRF name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: address_family_xr
                        
                        	Address family summary
                        	**type**\:   :py:class:`AddressFamilyXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr>`
                        
                        .. attribute:: state_xr
                        
                        	State summary
                        	**type**\:   :py:class:`StateXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr>`
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.vrf_name = None
                            self.address_family_xr = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr()
                            self.address_family_xr.parent = self
                            self.state_xr = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr()
                            self.state_xr.parent = self


                        class StateXr(object):
                            """
                            State summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: activated_sessions
                                
                                	Sessions in activated state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connected_sessions
                                
                                	Sessions in connected state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: connecting_sessions
                                
                                	Sessions in connecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: disconnecting_sessions
                                
                                	Sessions in disconnecting state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: end_sessions
                                
                                	Sessions in end state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: idle_sessions
                                
                                	Sessions in idle state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: initialized_sessions
                                
                                	Sessions in initialized state
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.activated_sessions = None
                                    self.connected_sessions = None
                                    self.connecting_sessions = None
                                    self.disconnecting_sessions = None
                                    self.end_sessions = None
                                    self.idle_sessions = None
                                    self.initialized_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.activated_sessions is not None:
                                        return True

                                    if self.connected_sessions is not None:
                                        return True

                                    if self.connecting_sessions is not None:
                                        return True

                                    if self.disconnecting_sessions is not None:
                                        return True

                                    if self.end_sessions is not None:
                                        return True

                                    if self.idle_sessions is not None:
                                        return True

                                    if self.initialized_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:state-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.StateXr']['meta_info']


                        class AddressFamilyXr(object):
                            """
                            Address family summary
                            
                            .. attribute:: ip_subscriber_dhcp
                            
                            	IP subscriber DHCP summary
                            	**type**\:   :py:class:`IpSubscriberDhcp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberDhcp>`
                            
                            .. attribute:: ip_subscriber_packet
                            
                            	IP subscriber packet summary
                            	**type**\:   :py:class:`IpSubscriberPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberPacket>`
                            
                            .. attribute:: pppoe
                            
                            	PPPoE summary
                            	**type**\:   :py:class:`Pppoe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.Pppoe>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.ip_subscriber_dhcp = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberDhcp()
                                self.ip_subscriber_dhcp.parent = self
                                self.ip_subscriber_packet = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberPacket()
                                self.ip_subscriber_packet.parent = self
                                self.pppoe = Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.Pppoe()
                                self.pppoe.parent = self


                            class Pppoe(object):
                                """
                                PPPoE summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:pppoe'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.Pppoe']['meta_info']


                            class IpSubscriberDhcp(object):
                                """
                                IP subscriber DHCP summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-dhcp'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberDhcp']['meta_info']


                            class IpSubscriberPacket(object):
                                """
                                IP subscriber packet summary
                                
                                .. attribute:: dual_part_up_sessions
                                
                                	Dual stack partially up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: dual_up_sessions
                                
                                	Dual stack up sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: in_progress_sessions
                                
                                	Sessions with undecided address family
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv4_only_sessions
                                
                                	IPv4 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ipv6_only_sessions
                                
                                	IPv6 only sessions 
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: lac_sessions
                                
                                	LAC sessions
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.dual_part_up_sessions = None
                                    self.dual_up_sessions = None
                                    self.in_progress_sessions = None
                                    self.ipv4_only_sessions = None
                                    self.ipv6_only_sessions = None
                                    self.lac_sessions = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:ip-subscriber-packet'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.dual_part_up_sessions is not None:
                                        return True

                                    if self.dual_up_sessions is not None:
                                        return True

                                    if self.in_progress_sessions is not None:
                                        return True

                                    if self.ipv4_only_sessions is not None:
                                        return True

                                    if self.ipv6_only_sessions is not None:
                                        return True

                                    if self.lac_sessions is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr.IpSubscriberPacket']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:address-family-xr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ip_subscriber_dhcp is not None and self.ip_subscriber_dhcp._has_data():
                                    return True

                                if self.ip_subscriber_packet is not None and self.ip_subscriber_packet._has_data():
                                    return True

                                if self.pppoe is not None and self.pppoe._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary.AddressFamilyXr']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.vrf_name is None:
                                raise YPYModelError('Key property vrf_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:vrf-summary[Cisco-IOS-XR-iedge4710-oper:vrf-name = ' + str(self.vrf_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.vrf_name is not None:
                                return True

                            if self.address_family_xr is not None and self.address_family_xr._has_data():
                                return True

                            if self.state_xr is not None and self.state_xr._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                            return meta._meta_table['Subscriber.Session.Nodes.Node.VrfSummaries.VrfSummary']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:vrf-summaries'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.vrf_summary is not None:
                            for child_ref in self.vrf_summary:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                        return meta._meta_table['Subscriber.Session.Nodes.Node.VrfSummaries']['meta_info']


                class Sessions(object):
                    """
                    IP subscriber sessions
                    
                    .. attribute:: session
                    
                    	Subscriber session information
                    	**type**\: list of    :py:class:`Session_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Sessions.Session_>`
                    
                    

                    """

                    _prefix = 'iedge4710-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.session = YList()
                        self.session.parent = self
                        self.session.name = 'session'


                    class Session_(object):
                        """
                        Subscriber session information
                        
                        .. attribute:: session_id  <key>
                        
                        	Session ID
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: access_interface_name
                        
                        	Access interface name associated with the session
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: account_session_id
                        
                        	Accounting session ID
                        	**type**\:  str
                        
                        .. attribute:: accounting
                        
                        	Accounting information
                        	**type**\:   :py:class:`Accounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Sessions.Session_.Accounting>`
                        
                        .. attribute:: af_up_status
                        
                        	AF status per Subscriber Session
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: circuit_id
                        
                        	Circuit ID
                        	**type**\:  str
                        
                        .. attribute:: clientname
                        
                        	Client Username
                        	**type**\:  str
                        
                        .. attribute:: delegated_ipv6_prefix
                        
                        	Session delegated IPv6 prefix
                        	**type**\:  str
                        
                        .. attribute:: formattedname
                        
                        	Formatted Username
                        	**type**\:  str
                        
                        .. attribute:: idle_state_change_time
                        
                        	Time when idle state change occurred in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Apr 11 21\:30\:47 2011
                        	**type**\:  str
                        
                        .. attribute:: interface_name
                        
                        	Interface name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: ipv6_interface_id
                        
                        	IPv6 Interface ID
                        	**type**\:  str
                        
                        	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                        
                        .. attribute:: is_session_authentic
                        
                        	If true, session is authentic
                        	**type**\:  bool
                        
                        .. attribute:: is_session_author
                        
                        	If true, session is authorized
                        	**type**\:  bool
                        
                        .. attribute:: lac_address
                        
                        	PPPoE LAC address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: lns_address
                        
                        	PPPoE LNS address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: mobility_attributes
                        
                        	List of mobility attributes collected for subscriber session
                        	**type**\:   :py:class:`MobilityAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Sessions.Session_.MobilityAttributes>`
                        
                        .. attribute:: nas_port
                        
                        	NAS port
                        	**type**\:  str
                        
                        .. attribute:: pending_callbacks
                        
                        	Active pending callbacks bitmask
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: pppoe_sub_type
                        
                        	PPPoE sub type
                        	**type**\:   :py:class:`IedgePppSubEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgePppSubEnum>`
                        
                        .. attribute:: remote_id
                        
                        	Remote ID
                        	**type**\:  str
                        
                        .. attribute:: session_change_of_authorization
                        
                        	Subscriber change of authorization information
                        	**type**\: list of    :py:class:`SessionChangeOfAuthorization <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Sessions.Session_.SessionChangeOfAuthorization>`
                        
                        .. attribute:: session_creation_time
                        
                        	Session creation time in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Apr 11 21\:30\:47 2011
                        	**type**\:  str
                        
                        .. attribute:: session_ip_address
                        
                        	Session ip address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: session_ipv4_state
                        
                        	Session IPv4 state
                        	**type**\:   :py:class:`IedgeOperSessionAfStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgeOperSessionAfStateEnum>`
                        
                        .. attribute:: session_ipv6_address
                        
                        	Session IPv6 address
                        	**type**\:  str
                        
                        .. attribute:: session_ipv6_prefix
                        
                        	Session IPv6 prefix
                        	**type**\:  str
                        
                        .. attribute:: session_ipv6_state
                        
                        	Session IPv6 state
                        	**type**\:   :py:class:`IedgeOperSessionAfStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgeOperSessionAfStateEnum>`
                        
                        .. attribute:: session_state
                        
                        	Session state
                        	**type**\:   :py:class:`IedgeOperSessionStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgeOperSessionStateEnum>`
                        
                        .. attribute:: session_type
                        
                        	Subscriber session type
                        	**type**\:   :py:class:`IedgeOperSessionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgeOperSessionEnum>`
                        
                        .. attribute:: total_session_idle_time
                        
                        	Total session idle time (in seconds)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: tunnel_client_authentication_id
                        
                        	PPPoE LAC tunnel client authentication ID
                        	**type**\:  str
                        
                        .. attribute:: tunnel_server_authentication_id
                        
                        	PPPoE LAC tunnel server authentication ID
                        	**type**\:  str
                        
                        .. attribute:: user_profile_attributes
                        
                        	List of user profile attributes collected for subscriber session
                        	**type**\:   :py:class:`UserProfileAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Sessions.Session_.UserProfileAttributes>`
                        
                        .. attribute:: username
                        
                        	Username
                        	**type**\:  str
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'iedge4710-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.session_id = None
                            self.access_interface_name = None
                            self.account_session_id = None
                            self.accounting = Subscriber.Session.Nodes.Node.Sessions.Session_.Accounting()
                            self.accounting.parent = self
                            self.af_up_status = None
                            self.circuit_id = None
                            self.clientname = None
                            self.delegated_ipv6_prefix = None
                            self.formattedname = None
                            self.idle_state_change_time = None
                            self.interface_name = None
                            self.ipv6_interface_id = None
                            self.is_session_authentic = None
                            self.is_session_author = None
                            self.lac_address = None
                            self.lns_address = None
                            self.mac_address = None
                            self.mobility_attributes = Subscriber.Session.Nodes.Node.Sessions.Session_.MobilityAttributes()
                            self.mobility_attributes.parent = self
                            self.nas_port = None
                            self.pending_callbacks = None
                            self.pppoe_sub_type = None
                            self.remote_id = None
                            self.session_change_of_authorization = YList()
                            self.session_change_of_authorization.parent = self
                            self.session_change_of_authorization.name = 'session_change_of_authorization'
                            self.session_creation_time = None
                            self.session_ip_address = None
                            self.session_ipv4_state = None
                            self.session_ipv6_address = None
                            self.session_ipv6_prefix = None
                            self.session_ipv6_state = None
                            self.session_state = None
                            self.session_type = None
                            self.total_session_idle_time = None
                            self.tunnel_client_authentication_id = None
                            self.tunnel_server_authentication_id = None
                            self.user_profile_attributes = Subscriber.Session.Nodes.Node.Sessions.Session_.UserProfileAttributes()
                            self.user_profile_attributes.parent = self
                            self.username = None
                            self.vrf_name = None


                        class Accounting(object):
                            """
                            Accounting information
                            
                            .. attribute:: accounting_session
                            
                            	Accounting information
                            	**type**\: list of    :py:class:`AccountingSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.Subscriber.Session.Nodes.Node.Sessions.Session_.Accounting.AccountingSession>`
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.accounting_session = YList()
                                self.accounting_session.parent = self
                                self.accounting_session.name = 'accounting_session'


                            class AccountingSession(object):
                                """
                                Accounting information
                                
                                .. attribute:: accepted_interim_updates
                                
                                	Number of interim updates accepted
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: account_session_id
                                
                                	Accounting session ID
                                	**type**\:  str
                                
                                .. attribute:: accounting_start_time
                                
                                	Accounting start time in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Feb 15 15\:12\:49 2011
                                	**type**\:  str
                                
                                .. attribute:: accounting_state_rc
                                
                                	Accounting State Error Code for Accounting Session
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: accounting_stop_state
                                
                                	Accounting Stop State
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: interim_interval
                                
                                	Interim accounting interval (in minutes)
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: minute
                                
                                .. attribute:: is_interim_accounting_enabled
                                
                                	True if interim accounting is enabled
                                	**type**\:  bool
                                
                                .. attribute:: last_interim_update_attempt_time
                                
                                	Time of last interim update attempt in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Apr 11 21\:30\:47 2011
                                	**type**\:  str
                                
                                .. attribute:: last_successful_interim_update_time
                                
                                	Time of last successful interim update in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Apr 11 21\:30 \:47 2011
                                	**type**\:  str
                                
                                .. attribute:: method_list_name
                                
                                	AAA method list name used to perform accounting
                                	**type**\:  str
                                
                                .. attribute:: next_interim_update_attempt_time
                                
                                	Time of next interim update attempt (in seconds)
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: record_context_name
                                
                                	Accounting record context name
                                	**type**\:  str
                                
                                .. attribute:: rejected_interim_updates
                                
                                	Number of interim updates rejected
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: sent_interim_update_failures
                                
                                	Number of interim update send failures
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: sent_interim_updates
                                
                                	Number of interim updates sent
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'iedge4710-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.accepted_interim_updates = None
                                    self.account_session_id = None
                                    self.accounting_start_time = None
                                    self.accounting_state_rc = None
                                    self.accounting_stop_state = None
                                    self.interim_interval = None
                                    self.is_interim_accounting_enabled = None
                                    self.last_interim_update_attempt_time = None
                                    self.last_successful_interim_update_time = None
                                    self.method_list_name = None
                                    self.next_interim_update_attempt_time = None
                                    self.record_context_name = None
                                    self.rejected_interim_updates = None
                                    self.sent_interim_update_failures = None
                                    self.sent_interim_updates = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:accounting-session'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.accepted_interim_updates is not None:
                                        return True

                                    if self.account_session_id is not None:
                                        return True

                                    if self.accounting_start_time is not None:
                                        return True

                                    if self.accounting_state_rc is not None:
                                        return True

                                    if self.accounting_stop_state is not None:
                                        return True

                                    if self.interim_interval is not None:
                                        return True

                                    if self.is_interim_accounting_enabled is not None:
                                        return True

                                    if self.last_interim_update_attempt_time is not None:
                                        return True

                                    if self.last_successful_interim_update_time is not None:
                                        return True

                                    if self.method_list_name is not None:
                                        return True

                                    if self.next_interim_update_attempt_time is not None:
                                        return True

                                    if self.record_context_name is not None:
                                        return True

                                    if self.rejected_interim_updates is not None:
                                        return True

                                    if self.sent_interim_update_failures is not None:
                                        return True

                                    if self.sent_interim_updates is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                    return meta._meta_table['Subscriber.Session.Nodes.Node.Sessions.Session_.Accounting.AccountingSession']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:accounting'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.accounting_session is not None:
                                    for child_ref in self.accounting_session:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.Sessions.Session_.Accounting']['meta_info']


                        class UserProfileAttributes(object):
                            """
                            List of user profile attributes collected for
                            subscriber session
                            
                            .. attribute:: accounting_session_id
                            
                            	Accounting session ID
                            	**type**\:  str
                            
                            .. attribute:: actual_data_rate_downstream
                            
                            	Actual data rate downstream (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: actual_data_rate_upstream
                            
                            	Actual data rate upstream (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: attainable_data_rate_downstream
                            
                            	Attainable data rate downstream (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: attainable_data_rate_upstream
                            
                            	Attainable data rate upstream (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: authorization_service_type
                            
                            	Authorization service type
                            	**type**\:   :py:class:`AaaAuthServiceEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.AaaAuthServiceEnum>`
                            
                            .. attribute:: circuit_id
                            
                            	Circuit ID
                            	**type**\:  str
                            
                            .. attribute:: connection_receive_speed
                            
                            	Connection receive speed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: connection_transmission_speed
                            
                            	Connection transmission speed
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: destination_station_id
                            
                            	Destination station ID
                            	**type**\:  str
                            
                            .. attribute:: downstream_parameterized_qos_policy
                            
                            	Downstream parameterized QoS policy to be applied on the subscriber side
                            	**type**\:  str
                            
                            .. attribute:: downstream_qos_policy
                            
                            	Downstream QoS policy to be applied on the subscriber side
                            	**type**\:  str
                            
                            .. attribute:: egress_access_list
                            
                            	Egress access list
                            	**type**\:  str
                            
                            .. attribute:: formatted_calling_station_id
                            
                            	Formatted calling station id
                            	**type**\:  str
                            
                            .. attribute:: ingress_access_list
                            
                            	Ingress access list
                            	**type**\:  str
                            
                            .. attribute:: interface_name
                            
                            	Interface name
                            	**type**\:  str
                            
                            .. attribute:: interface_type
                            
                            	Interface type
                            	**type**\:   :py:class:`AaaInterfaceEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.AaaInterfaceEnum>`
                            
                            .. attribute:: interim_accounting_interval
                            
                            	Interim accounting interval
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ip_netmask
                            
                            	IP netmask for the user
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv4_unnumbered
                            
                            	IPv4 unnumbered
                            	**type**\:  str
                            
                            .. attribute:: ipv4mtu
                            
                            	IPv4 maximum transmission unit
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_interworking_functionality
                            
                            	True, if interworking functionality
                            	**type**\:  bool
                            
                            .. attribute:: max_data_rate_downstream
                            
                            	Maximum data rate downstream (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: max_data_rate_upstream
                            
                            	Maximum data rate upstream (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: max_interleaving_delay_downstream
                            
                            	Maximum interleaving delay downstream (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: max_interleaving_delay_upstream
                            
                            	Maximum interleaving delay upstream (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: min_data_rate_downstream
                            
                            	Minimum data rate downstream (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: min_data_rate_downstream_low_power
                            
                            	Minimum data rate downstream low power (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: min_data_rate_upstream_low_power
                            
                            	Minimum data rate upstream low power (in Mbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: Mbit/s
                            
                            .. attribute:: parent_interface_name
                            
                            	Parent interface name
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: pool_address
                            
                            	IP address pool
                            	**type**\:  str
                            
                            .. attribute:: primary_dns_server_address
                            
                            	Primary DNS server address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: primary_net_bios_server_address
                            
                            	Primary net bios server address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: remote_id
                            
                            	Remote ID
                            	**type**\:  str
                            
                            .. attribute:: route
                            
                            	Route information for a user session
                            	**type**\:  str
                            
                            .. attribute:: secondary_dns_server_address
                            
                            	Secondary DNS server address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: secondary_net_bios_server_address
                            
                            	Secondary net bios server address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: session_termination_cause
                            
                            	Session termination cause
                            	**type**\:   :py:class:`AaaTerminateCauseEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.AaaTerminateCauseEnum>`
                            
                            .. attribute:: session_timeout
                            
                            	Session timeout (in seconds)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: strict_rpf_packets
                            
                            	Strict RPF packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: tunnel_client_authentication_id
                            
                            	Tunnel client authentication ID
                            	**type**\:  str
                            
                            .. attribute:: tunnel_client_endpoint
                            
                            	Tunnel client endpoint
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: tunnel_medium
                            
                            	Tunnel medium
                            	**type**\:   :py:class:`AaaTunnelMediumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.AaaTunnelMediumEnum>`
                            
                            .. attribute:: tunnel_preference
                            
                            	Tunnel preference
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: tunnel_protocol
                            
                            	Tunnel protocol
                            	**type**\:   :py:class:`AaaTunnelProtoEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.AaaTunnelProtoEnum>`
                            
                            .. attribute:: tunnel_server_endpoint
                            
                            	Tunnel server endpoint
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: tunnel_tos_setting
                            
                            	Tunnel TOS setting
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: upstream_parameterized_qos_policy
                            
                            	Upstream parameterized QoS policy to be applied on the subscriber side
                            	**type**\:  str
                            
                            .. attribute:: upstream_qos_policy
                            
                            	Upstream QoS policy to be applied on the subscriber side
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.accounting_session_id = None
                                self.actual_data_rate_downstream = None
                                self.actual_data_rate_upstream = None
                                self.attainable_data_rate_downstream = None
                                self.attainable_data_rate_upstream = None
                                self.authorization_service_type = None
                                self.circuit_id = None
                                self.connection_receive_speed = None
                                self.connection_transmission_speed = None
                                self.destination_station_id = None
                                self.downstream_parameterized_qos_policy = None
                                self.downstream_qos_policy = None
                                self.egress_access_list = None
                                self.formatted_calling_station_id = None
                                self.ingress_access_list = None
                                self.interface_name = None
                                self.interface_type = None
                                self.interim_accounting_interval = None
                                self.ip_netmask = None
                                self.ipv4_unnumbered = None
                                self.ipv4mtu = None
                                self.is_interworking_functionality = None
                                self.max_data_rate_downstream = None
                                self.max_data_rate_upstream = None
                                self.max_interleaving_delay_downstream = None
                                self.max_interleaving_delay_upstream = None
                                self.min_data_rate_downstream = None
                                self.min_data_rate_downstream_low_power = None
                                self.min_data_rate_upstream_low_power = None
                                self.parent_interface_name = None
                                self.pool_address = None
                                self.primary_dns_server_address = None
                                self.primary_net_bios_server_address = None
                                self.remote_id = None
                                self.route = None
                                self.secondary_dns_server_address = None
                                self.secondary_net_bios_server_address = None
                                self.session_termination_cause = None
                                self.session_timeout = None
                                self.strict_rpf_packets = None
                                self.tunnel_client_authentication_id = None
                                self.tunnel_client_endpoint = None
                                self.tunnel_medium = None
                                self.tunnel_preference = None
                                self.tunnel_protocol = None
                                self.tunnel_server_endpoint = None
                                self.tunnel_tos_setting = None
                                self.upstream_parameterized_qos_policy = None
                                self.upstream_qos_policy = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:user-profile-attributes'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.accounting_session_id is not None:
                                    return True

                                if self.actual_data_rate_downstream is not None:
                                    return True

                                if self.actual_data_rate_upstream is not None:
                                    return True

                                if self.attainable_data_rate_downstream is not None:
                                    return True

                                if self.attainable_data_rate_upstream is not None:
                                    return True

                                if self.authorization_service_type is not None:
                                    return True

                                if self.circuit_id is not None:
                                    return True

                                if self.connection_receive_speed is not None:
                                    return True

                                if self.connection_transmission_speed is not None:
                                    return True

                                if self.destination_station_id is not None:
                                    return True

                                if self.downstream_parameterized_qos_policy is not None:
                                    return True

                                if self.downstream_qos_policy is not None:
                                    return True

                                if self.egress_access_list is not None:
                                    return True

                                if self.formatted_calling_station_id is not None:
                                    return True

                                if self.ingress_access_list is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.interface_type is not None:
                                    return True

                                if self.interim_accounting_interval is not None:
                                    return True

                                if self.ip_netmask is not None:
                                    return True

                                if self.ipv4_unnumbered is not None:
                                    return True

                                if self.ipv4mtu is not None:
                                    return True

                                if self.is_interworking_functionality is not None:
                                    return True

                                if self.max_data_rate_downstream is not None:
                                    return True

                                if self.max_data_rate_upstream is not None:
                                    return True

                                if self.max_interleaving_delay_downstream is not None:
                                    return True

                                if self.max_interleaving_delay_upstream is not None:
                                    return True

                                if self.min_data_rate_downstream is not None:
                                    return True

                                if self.min_data_rate_downstream_low_power is not None:
                                    return True

                                if self.min_data_rate_upstream_low_power is not None:
                                    return True

                                if self.parent_interface_name is not None:
                                    return True

                                if self.pool_address is not None:
                                    return True

                                if self.primary_dns_server_address is not None:
                                    return True

                                if self.primary_net_bios_server_address is not None:
                                    return True

                                if self.remote_id is not None:
                                    return True

                                if self.route is not None:
                                    return True

                                if self.secondary_dns_server_address is not None:
                                    return True

                                if self.secondary_net_bios_server_address is not None:
                                    return True

                                if self.session_termination_cause is not None:
                                    return True

                                if self.session_timeout is not None:
                                    return True

                                if self.strict_rpf_packets is not None:
                                    return True

                                if self.tunnel_client_authentication_id is not None:
                                    return True

                                if self.tunnel_client_endpoint is not None:
                                    return True

                                if self.tunnel_medium is not None:
                                    return True

                                if self.tunnel_preference is not None:
                                    return True

                                if self.tunnel_protocol is not None:
                                    return True

                                if self.tunnel_server_endpoint is not None:
                                    return True

                                if self.tunnel_tos_setting is not None:
                                    return True

                                if self.upstream_parameterized_qos_policy is not None:
                                    return True

                                if self.upstream_qos_policy is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.Sessions.Session_.UserProfileAttributes']['meta_info']


                        class MobilityAttributes(object):
                            """
                            List of mobility attributes collected for
                            subscriber session
                            
                            .. attribute:: domain_name
                            
                            	Domain Name
                            	**type**\:  str
                            
                            .. attribute:: downlink_gre_key
                            
                            	Downlink GRE Key
                            	**type**\:  str
                            
                            .. attribute:: lease_time
                            
                            	Duration of lease in seconds
                            	**type**\:  str
                            
                            	**units**\: second
                            
                            .. attribute:: mobility_default_ipv4_gateway
                            
                            	Default Gateway IPv4 Address
                            	**type**\:  str
                            
                            .. attribute:: mobility_dhcp_server
                            
                            	DHCP Server
                            	**type**\:  str
                            
                            .. attribute:: mobility_dns_server
                            
                            	DNS Server Primary
                            	**type**\:  str
                            
                            .. attribute:: mobility_ipv4_address
                            
                            	IPv4 address of Mobility Node
                            	**type**\:  str
                            
                            .. attribute:: mobility_ipv4_netmask
                            
                            	IPv4 Netmask
                            	**type**\:  str
                            
                            .. attribute:: mpc_protocol
                            
                            	Cisco MPC Protocol
                            	**type**\:  bool
                            
                            .. attribute:: uplink_gre_key
                            
                            	Uplink GRE Key
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.domain_name = None
                                self.downlink_gre_key = None
                                self.lease_time = None
                                self.mobility_default_ipv4_gateway = None
                                self.mobility_dhcp_server = None
                                self.mobility_dns_server = None
                                self.mobility_ipv4_address = None
                                self.mobility_ipv4_netmask = None
                                self.mpc_protocol = None
                                self.uplink_gre_key = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:mobility-attributes'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.domain_name is not None:
                                    return True

                                if self.downlink_gre_key is not None:
                                    return True

                                if self.lease_time is not None:
                                    return True

                                if self.mobility_default_ipv4_gateway is not None:
                                    return True

                                if self.mobility_dhcp_server is not None:
                                    return True

                                if self.mobility_dns_server is not None:
                                    return True

                                if self.mobility_ipv4_address is not None:
                                    return True

                                if self.mobility_ipv4_netmask is not None:
                                    return True

                                if self.mpc_protocol is not None:
                                    return True

                                if self.uplink_gre_key is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.Sessions.Session_.MobilityAttributes']['meta_info']


                        class SessionChangeOfAuthorization(object):
                            """
                            Subscriber change of authorization information
                            
                            .. attribute:: coa_reply_attributes
                            
                            	List of Reply Attributes collected in COA response
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: coa_request_attributes
                            
                            	List of Request Attributes collected in COA response
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                            
                            .. attribute:: reply_time
                            
                            	Reply time in DDD MMM DD HH\:MM\:SS YYYY format eg \: Tue Apr 11 21\:30\:47 2011
                            	**type**\:  str
                            
                            .. attribute:: request_acked
                            
                            	Coa Request Acked
                            	**type**\:  bool
                            
                            .. attribute:: request_time
                            
                            	Request time in DDD MMM DD HH\:MM\:SS YYYY format eg\: Tue Apr 11 21\:30\:47 2011
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'iedge4710-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.coa_reply_attributes = None
                                self.coa_request_attributes = None
                                self.reply_time = None
                                self.request_acked = None
                                self.request_time = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:session-change-of-authorization'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.coa_reply_attributes is not None:
                                    return True

                                if self.coa_request_attributes is not None:
                                    return True

                                if self.reply_time is not None:
                                    return True

                                if self.request_acked is not None:
                                    return True

                                if self.request_time is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                                return meta._meta_table['Subscriber.Session.Nodes.Node.Sessions.Session_.SessionChangeOfAuthorization']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.session_id is None:
                                raise YPYModelError('Key property session_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:session[Cisco-IOS-XR-iedge4710-oper:session-id = ' + str(self.session_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.session_id is not None:
                                return True

                            if self.access_interface_name is not None:
                                return True

                            if self.account_session_id is not None:
                                return True

                            if self.accounting is not None and self.accounting._has_data():
                                return True

                            if self.af_up_status is not None:
                                return True

                            if self.circuit_id is not None:
                                return True

                            if self.clientname is not None:
                                return True

                            if self.delegated_ipv6_prefix is not None:
                                return True

                            if self.formattedname is not None:
                                return True

                            if self.idle_state_change_time is not None:
                                return True

                            if self.interface_name is not None:
                                return True

                            if self.ipv6_interface_id is not None:
                                return True

                            if self.is_session_authentic is not None:
                                return True

                            if self.is_session_author is not None:
                                return True

                            if self.lac_address is not None:
                                return True

                            if self.lns_address is not None:
                                return True

                            if self.mac_address is not None:
                                return True

                            if self.mobility_attributes is not None and self.mobility_attributes._has_data():
                                return True

                            if self.nas_port is not None:
                                return True

                            if self.pending_callbacks is not None:
                                return True

                            if self.pppoe_sub_type is not None:
                                return True

                            if self.remote_id is not None:
                                return True

                            if self.session_change_of_authorization is not None:
                                for child_ref in self.session_change_of_authorization:
                                    if child_ref._has_data():
                                        return True

                            if self.session_creation_time is not None:
                                return True

                            if self.session_ip_address is not None:
                                return True

                            if self.session_ipv4_state is not None:
                                return True

                            if self.session_ipv6_address is not None:
                                return True

                            if self.session_ipv6_prefix is not None:
                                return True

                            if self.session_ipv6_state is not None:
                                return True

                            if self.session_state is not None:
                                return True

                            if self.session_type is not None:
                                return True

                            if self.total_session_idle_time is not None:
                                return True

                            if self.tunnel_client_authentication_id is not None:
                                return True

                            if self.tunnel_server_authentication_id is not None:
                                return True

                            if self.user_profile_attributes is not None and self.user_profile_attributes._has_data():
                                return True

                            if self.username is not None:
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                            return meta._meta_table['Subscriber.Session.Nodes.Node.Sessions.Session_']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:sessions'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.session is not None:
                            for child_ref in self.session:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                        return meta._meta_table['Subscriber.Session.Nodes.Node.Sessions']['meta_info']

                @property
                def _common_path(self):
                    if self.node_name is None:
                        raise YPYModelError('Key property node_name is None')

                    return '/Cisco-IOS-XR-iedge4710-oper:subscriber/Cisco-IOS-XR-iedge4710-oper:session/Cisco-IOS-XR-iedge4710-oper:nodes/Cisco-IOS-XR-iedge4710-oper:node[Cisco-IOS-XR-iedge4710-oper:node-name = ' + str(self.node_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.node_name is not None:
                        return True

                    if self.access_interface_summaries is not None and self.access_interface_summaries._has_data():
                        return True

                    if self.address_family_summaries is not None and self.address_family_summaries._has_data():
                        return True

                    if self.authentication_summaries is not None and self.authentication_summaries._has_data():
                        return True

                    if self.author_summaries is not None and self.author_summaries._has_data():
                        return True

                    if self.interface_summaries is not None and self.interface_summaries._has_data():
                        return True

                    if self.ipv4_address_summaries is not None and self.ipv4_address_summaries._has_data():
                        return True

                    if self.ipv4_address_vrf_summaries is not None and self.ipv4_address_vrf_summaries._has_data():
                        return True

                    if self.mac_summaries is not None and self.mac_summaries._has_data():
                        return True

                    if self.sessions is not None and self.sessions._has_data():
                        return True

                    if self.state_summaries is not None and self.state_summaries._has_data():
                        return True

                    if self.summary is not None and self.summary._has_data():
                        return True

                    if self.username_summaries is not None and self.username_summaries._has_data():
                        return True

                    if self.vrf_summaries is not None and self.vrf_summaries._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                    return meta._meta_table['Subscriber.Session.Nodes.Node']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-iedge4710-oper:subscriber/Cisco-IOS-XR-iedge4710-oper:session/Cisco-IOS-XR-iedge4710-oper:nodes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.node is not None:
                    for child_ref in self.node:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                return meta._meta_table['Subscriber.Session.Nodes']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-iedge4710-oper:subscriber/Cisco-IOS-XR-iedge4710-oper:session'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.nodes is not None and self.nodes._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
            return meta._meta_table['Subscriber.Session']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-iedge4710-oper:subscriber'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.manager is not None and self.manager._has_data():
            return True

        if self.session is not None and self.session._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
        return meta._meta_table['Subscriber']['meta_info']


class IedgeLicenseManager(object):
    """
    iedge license manager
    
    .. attribute:: nodes
    
    	Session License Manager operational data for a location
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgeLicenseManager.Nodes>`
    
    

    """

    _prefix = 'iedge4710-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = IedgeLicenseManager.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Session License Manager operational data for a
        location
        
        .. attribute:: node
        
        	Location. For example, 0/1/CPU0
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgeLicenseManager.Nodes.Node>`
        
        

        """

        _prefix = 'iedge4710-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Location. For example, 0/1/CPU0
            
            .. attribute:: nodeid  <key>
            
            	The node id to filter on. For example, 0/1/CPU0
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: iedge_license_manager_summary
            
            	Display Session License Manager summary data
            	**type**\:   :py:class:`IedgeLicenseManagerSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_iedge4710_oper.IedgeLicenseManager.Nodes.Node.IedgeLicenseManagerSummary>`
            
            

            """

            _prefix = 'iedge4710-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.nodeid = None
                self.iedge_license_manager_summary = IedgeLicenseManager.Nodes.Node.IedgeLicenseManagerSummary()
                self.iedge_license_manager_summary.parent = self


            class IedgeLicenseManagerSummary(object):
                """
                Display Session License Manager summary data
                
                .. attribute:: session_count
                
                	number of sessions
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: session_license_count
                
                	number of license
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: session_limit
                
                	configured session limit
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: session_threshold
                
                	configured session threshold
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'iedge4710-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.session_count = None
                    self.session_license_count = None
                    self.session_limit = None
                    self.session_threshold = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-iedge4710-oper:iedge-license-manager-summary'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.session_count is not None:
                        return True

                    if self.session_license_count is not None:
                        return True

                    if self.session_limit is not None:
                        return True

                    if self.session_threshold is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                    return meta._meta_table['IedgeLicenseManager.Nodes.Node.IedgeLicenseManagerSummary']['meta_info']

            @property
            def _common_path(self):
                if self.nodeid is None:
                    raise YPYModelError('Key property nodeid is None')

                return '/Cisco-IOS-XR-iedge4710-oper:iedge-license-manager/Cisco-IOS-XR-iedge4710-oper:nodes/Cisco-IOS-XR-iedge4710-oper:node[Cisco-IOS-XR-iedge4710-oper:nodeid = ' + str(self.nodeid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.nodeid is not None:
                    return True

                if self.iedge_license_manager_summary is not None and self.iedge_license_manager_summary._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
                return meta._meta_table['IedgeLicenseManager.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-iedge4710-oper:iedge-license-manager/Cisco-IOS-XR-iedge4710-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
            return meta._meta_table['IedgeLicenseManager.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-iedge4710-oper:iedge-license-manager'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_iedge4710_oper as meta
        return meta._meta_table['IedgeLicenseManager']['meta_info']


