


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'BgpSubsequentAddressFamilyEnum' : _MetaInfoEnum('BgpSubsequentAddressFamilyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes',
        {
            'unicast':'unicast',
            'multicast':'multicast',
            'labeled-unicast':'labeled_unicast',
            'mvpn':'mvpn',
            'mspw':'mspw',
            'tunnel':'tunnel',
            'vpls':'vpls',
            'mdt':'mdt',
            'vpws':'vpws',
            'evpn':'evpn',
            'ls':'ls',
            'vpn':'vpn',
            'vpn-mcast':'vpn_mcast',
            'rt-filter':'rt_filter',
            'flowspec':'flowspec',
            'vpn-flowspec':'vpn_flowspec',
            'all':'all',
        }, 'Cisco-IOS-XR-ipv4-bgp-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-datatypes']),
    'BgpNbrCapAdditionalPathsCfgEnum' : _MetaInfoEnum('BgpNbrCapAdditionalPathsCfgEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes',
        {
            'enable':'enable',
            'disable':'disable',
        }, 'Cisco-IOS-XR-ipv4-bgp-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-datatypes']),
    'BgpOfficialAddressFamilyEnum' : _MetaInfoEnum('BgpOfficialAddressFamilyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
            'l2vpn':'l2vpn',
            'ls':'ls',
            'all':'all',
        }, 'Cisco-IOS-XR-ipv4-bgp-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-datatypes']),
    'BgpafAdditionalPathsCfgEnum' : _MetaInfoEnum('BgpafAdditionalPathsCfgEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes',
        {
            'enable':'enable',
            'disable':'disable',
        }, 'Cisco-IOS-XR-ipv4-bgp-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-datatypes']),
    'BgpTosEnum' : _MetaInfoEnum('BgpTosEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes',
        {
            'precedence':'precedence',
            'dscp':'dscp',
        }, 'Cisco-IOS-XR-ipv4-bgp-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-datatypes']),
    'BgpAddressFamilyEnum' : _MetaInfoEnum('BgpAddressFamilyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes',
        {
            'ipv4-unicast':'ipv4_unicast',
            'ipv4-multicast':'ipv4_multicast',
            'ipv4-labeled-unicast':'ipv4_labeled_unicast',
            'ipv4-tunnel':'ipv4_tunnel',
            'vp-nv4-unicast':'vp_nv4_unicast',
            'ipv6-unicast':'ipv6_unicast',
            'ipv6-multicast':'ipv6_multicast',
            'ipv6-labeled-unicast':'ipv6_labeled_unicast',
            'vp-nv6-unicast':'vp_nv6_unicast',
            'ipv4mdt':'ipv4mdt',
            'l2vpnvpls':'l2vpnvpls',
            'ipv4rt-constraint':'ipv4rt_constraint',
            'ipv4mvpn':'ipv4mvpn',
            'ipv6mvpn':'ipv6mvpn',
            'l2vpnevpn':'l2vpnevpn',
            'lsls':'lsls',
            'vp-nv4-multicast':'vp_nv4_multicast',
            'vp-nv6-multicast':'vp_nv6_multicast',
            'ipv4-flowspec':'ipv4_flowspec',
            'ipv6-flowspec':'ipv6_flowspec',
            'vp-nv4-flowspec':'vp_nv4_flowspec',
            'vp-nv6-flowspec':'vp_nv6_flowspec',
            'l2vpnmspw':'l2vpnmspw',
            'all-address-family':'all_address_family',
        }, 'Cisco-IOS-XR-ipv4-bgp-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-datatypes']),
    'BgpPrecedenceDscpEnum' : _MetaInfoEnum('BgpPrecedenceDscpEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes',
        {
            'af11':'af11',
            'af12':'af12',
            'af13':'af13',
            'af21':'af21',
            'af22':'af22',
            'af23':'af23',
            'af31':'af31',
            'af32':'af32',
            'af33':'af33',
            'af41':'af41',
            'af42':'af42',
            'af43':'af43',
            'cs1':'cs1',
            'cs2':'cs2',
            'cs3':'cs3',
            'cs4':'cs4',
            'cs5':'cs5',
            'cs6':'cs6',
            'cs7':'cs7',
            'ef':'ef',
            'critical':'critical',
            'flash':'flash',
            'flash-override':'flash_override',
            'immediate':'immediate',
            'internet':'internet',
            'network':'network',
            'priority':'priority',
            'default-or-routine':'default_or_routine',
        }, 'Cisco-IOS-XR-ipv4-bgp-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-datatypes']),
    'BgpUpdateFilterActionEnum' : _MetaInfoEnum('BgpUpdateFilterActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes',
        {
            'treat-as-withdraw':'treat_as_withdraw',
            'discard-attibute':'discard_attibute',
        }, 'Cisco-IOS-XR-ipv4-bgp-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-datatypes']),
}
