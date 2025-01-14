


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'MgmtMplsStaticLabelStatusEnum' : _MetaInfoEnum('MgmtMplsStaticLabelStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper',
        {
            'not-created':'not_created',
            'vrf-down':'vrf_down',
            'rewrite-vrf-down':'rewrite_vrf_down',
            'lsd-disconnected':'lsd_disconnected',
            'lsd-failed':'lsd_failed',
            'wait-for-lsd-reply':'wait_for_lsd_reply',
            'label-created':'label_created',
            'label-create-failed':'label_create_failed',
            'label-rewrite-failed':'label_rewrite_failed',
            'rewrite-next-hop-interface-missing':'rewrite_next_hop_interface_missing',
            'label-discrepancy':'label_discrepancy',
            'rewrite-discrepancy':'rewrite_discrepancy',
            'label-status-unknown':'label_status_unknown',
        }, 'Cisco-IOS-XR-mpls-static-oper', _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper']),
    'MgmtStaticPathEnum' : _MetaInfoEnum('MgmtStaticPathEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper',
        {
            'cross-connect-path':'cross_connect_path',
            'pop-lookup-path':'pop_lookup_path',
        }, 'Cisco-IOS-XR-mpls-static-oper', _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper']),
    'MgmtStaticNhLblEnum' : _MetaInfoEnum('MgmtStaticNhLblEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper',
        {
            'out-label':'out_label',
            'out-pop':'out_pop',
            'out-explicit-null':'out_explicit_null',
        }, 'Cisco-IOS-XR-mpls-static-oper', _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper']),
    'MgmtStaticAddrEnum' : _MetaInfoEnum('MgmtStaticAddrEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-mpls-static-oper', _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper']),
    'MgmtMplsStaticLabelModeEnum' : _MetaInfoEnum('MgmtMplsStaticLabelModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper',
        {
            'none':'none',
            'per-prefix':'per_prefix',
            'per-vrf':'per_vrf',
            'cross-connect':'cross_connect',
        }, 'Cisco-IOS-XR-mpls-static-oper', _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper']),
    'MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix.Prefix_' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix.Prefix_',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'MgmtStaticAddrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticAddrEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 context
                ''',
                'ipv4_prefix',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 context
                ''',
                'ipv6_prefix',
                'Cisco-IOS-XR-mpls-static-oper', False),
            ],
            'Cisco-IOS-XR-mpls-static-oper',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_CLASS, 'Prefix_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix.Prefix_', 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-mpls-static-oper', False),
            ],
            'Cisco-IOS-XR-mpls-static-oper',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo',
            False, 
            [
            _MetaInfoClassMember('next-hop-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Next-Hop Interface Name
                ''',
                'next_hop_interface_name',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('next-hop-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Next-Hop Ipv4 Address
                ''',
                'next_hop_ipv4_address',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('next-hop-ipv4-address-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Next-Hop Ipv4 Set
                ''',
                'next_hop_ipv4_address_set',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('next-hop-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Next-Hop Label
                ''',
                'next_hop_label',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('next-hop-label-type', REFERENCE_ENUM_CLASS, 'MgmtStaticNhLblEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticNhLblEnum', 
                [], [], 
                '''                Next-Hop Label Type
                ''',
                'next_hop_label_type',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path Number
                ''',
                'path',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'MgmtStaticPathEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticPathEnum', 
                [], [], 
                '''                Path Type
                ''',
                'type',
                'Cisco-IOS-XR-mpls-static-oper', False),
            ],
            'Cisco-IOS-XR-mpls-static-oper',
            'path-info',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label value
                ''',
                'label',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('label-mode', REFERENCE_ENUM_CLASS, 'MgmtMplsStaticLabelModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtMplsStaticLabelModeEnum', 
                [], [], 
                '''                Label Mode
                ''',
                'label_mode',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('label-status', REFERENCE_ENUM_CLASS, 'MgmtMplsStaticLabelStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtMplsStaticLabelStatusEnum', 
                [], [], 
                '''                Label Status
                ''',
                'label_status',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('path-info', REFERENCE_LIST, 'PathInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo', 
                [], [], 
                '''                Path Information
                ''',
                'path_info',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('prefix', REFERENCE_CLASS, 'Prefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix', 
                [], [], 
                '''                Prefix Information
                ''',
                'prefix',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-mpls-static-oper', False),
            ],
            'Cisco-IOS-XR-mpls-static-oper',
            'label',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Lsps.Lsp' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Lsps.Lsp',
            False, 
            [
            _MetaInfoClassMember('lsp-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                LSP Name
                ''',
                'lsp_name',
                'Cisco-IOS-XR-mpls-static-oper', True),
            _MetaInfoClassMember('label', REFERENCE_CLASS, 'Label' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label', 
                [], [], 
                '''                Label Information
                ''',
                'label',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('lsp-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP Name
                ''',
                'lsp_name_xr',
                'Cisco-IOS-XR-mpls-static-oper', False),
            ],
            'Cisco-IOS-XR-mpls-static-oper',
            'lsp',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Lsps' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Lsps',
            False, 
            [
            _MetaInfoClassMember('lsp', REFERENCE_LIST, 'Lsp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStatic.Vrfs.Vrf.Lsps.Lsp', 
                [], [], 
                '''                Data for static lsp
                ''',
                'lsp',
                'Cisco-IOS-XR-mpls-static-oper', False),
            ],
            'Cisco-IOS-XR-mpls-static-oper',
            'lsps',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper'
        ),
    },
    'MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix_' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix_',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'MgmtStaticAddrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticAddrEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 context
                ''',
                'ipv4_prefix',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 context
                ''',
                'ipv6_prefix',
                'Cisco-IOS-XR-mpls-static-oper', False),
            ],
            'Cisco-IOS-XR-mpls-static-oper',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper'
        ),
    },
    'MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_CLASS, 'Prefix_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix_', 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-mpls-static-oper', False),
            ],
            'Cisco-IOS-XR-mpls-static-oper',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper'
        ),
    },
    'MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo',
            False, 
            [
            _MetaInfoClassMember('next-hop-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Next-Hop Interface Name
                ''',
                'next_hop_interface_name',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('next-hop-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Next-Hop Ipv4 Address
                ''',
                'next_hop_ipv4_address',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('next-hop-ipv4-address-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Next-Hop Ipv4 Set
                ''',
                'next_hop_ipv4_address_set',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('next-hop-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Next-Hop Label
                ''',
                'next_hop_label',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('next-hop-label-type', REFERENCE_ENUM_CLASS, 'MgmtStaticNhLblEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticNhLblEnum', 
                [], [], 
                '''                Next-Hop Label Type
                ''',
                'next_hop_label_type',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path Number
                ''',
                'path',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'MgmtStaticPathEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticPathEnum', 
                [], [], 
                '''                Path Type
                ''',
                'type',
                'Cisco-IOS-XR-mpls-static-oper', False),
            ],
            'Cisco-IOS-XR-mpls-static-oper',
            'path-info',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper'
        ),
    },
    'MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel',
            False, 
            [
            _MetaInfoClassMember('local-label-id', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Local Label
                ''',
                'local_label_id',
                'Cisco-IOS-XR-mpls-static-oper', True),
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label value
                ''',
                'label',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('label-mode', REFERENCE_ENUM_CLASS, 'MgmtMplsStaticLabelModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtMplsStaticLabelModeEnum', 
                [], [], 
                '''                Label Mode
                ''',
                'label_mode',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('label-status', REFERENCE_ENUM_CLASS, 'MgmtMplsStaticLabelStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtMplsStaticLabelStatusEnum', 
                [], [], 
                '''                Label Status
                ''',
                'label_status',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('path-info', REFERENCE_LIST, 'PathInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo', 
                [], [], 
                '''                Path Information
                ''',
                'path_info',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('prefix', REFERENCE_CLASS, 'Prefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix', 
                [], [], 
                '''                Prefix Information
                ''',
                'prefix',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-mpls-static-oper', False),
            ],
            'Cisco-IOS-XR-mpls-static-oper',
            'local-label',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper'
        ),
    },
    'MplsStatic.Vrfs.Vrf.LocalLabels' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.LocalLabels',
            False, 
            [
            _MetaInfoClassMember('local-label', REFERENCE_LIST, 'LocalLabel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel', 
                [], [], 
                '''                Data for static label
                ''',
                'local_label',
                'Cisco-IOS-XR-mpls-static-oper', False),
            ],
            'Cisco-IOS-XR-mpls-static-oper',
            'local-labels',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper'
        ),
    },
    'MplsStatic.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-mpls-static-oper', True),
            _MetaInfoClassMember('local-labels', REFERENCE_CLASS, 'LocalLabels' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStatic.Vrfs.Vrf.LocalLabels', 
                [], [], 
                '''                data for static local-label table
                ''',
                'local_labels',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('lsps', REFERENCE_CLASS, 'Lsps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStatic.Vrfs.Vrf.Lsps', 
                [], [], 
                '''                data for static lsp table
                ''',
                'lsps',
                'Cisco-IOS-XR-mpls-static-oper', False),
            ],
            'Cisco-IOS-XR-mpls-static-oper',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper'
        ),
    },
    'MplsStatic.Vrfs' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStatic.Vrfs.Vrf', 
                [], [], 
                '''                VRF Name
                ''',
                'vrf',
                'Cisco-IOS-XR-mpls-static-oper', False),
            ],
            'Cisco-IOS-XR-mpls-static-oper',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper'
        ),
    },
    'MplsStatic.Summary' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Summary',
            False, 
            [
            _MetaInfoClassMember('active-vrf-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Number of Active VRF Active
                ''',
                'active_vrf_count',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('im-connected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IM is connected
                ''',
                'im_connected',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Number of Interface
                ''',
                'interface_count',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('interface-foward-reference-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Number of Active Interface
                ''',
                'interface_foward_reference_count',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('label-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Number of Labels
                ''',
                'label_count',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('label-discrepancy-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Number of Labels with Discrepancies
                ''',
                'label_discrepancy_count',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('label-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Number of Labels with Errors
                ''',
                'label_error_count',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('lsd-connected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                LSD connection is up
                ''',
                'lsd_connected',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('mpls-enabled-interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Number of MPLS enabled Interface
                ''',
                'mpls_enabled_interface_count',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('rsi-connected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RSI is connected
                ''',
                'rsi_connected',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('vrf-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Number of VRF configured
                ''',
                'vrf_count',
                'Cisco-IOS-XR-mpls-static-oper', False),
            ],
            'Cisco-IOS-XR-mpls-static-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper'
        ),
    },
    'MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix_' : {
        'meta_info' : _MetaInfoClass('MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix_',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'MgmtStaticAddrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticAddrEnum', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 context
                ''',
                'ipv4_prefix',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 context
                ''',
                'ipv6_prefix',
                'Cisco-IOS-XR-mpls-static-oper', False),
            ],
            'Cisco-IOS-XR-mpls-static-oper',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper'
        ),
    },
    'MplsStatic.LocalLabels.LocalLabel.Prefix' : {
        'meta_info' : _MetaInfoClass('MplsStatic.LocalLabels.LocalLabel.Prefix',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_CLASS, 'Prefix_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix_', 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-mpls-static-oper', False),
            ],
            'Cisco-IOS-XR-mpls-static-oper',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper'
        ),
    },
    'MplsStatic.LocalLabels.LocalLabel.PathInfo' : {
        'meta_info' : _MetaInfoClass('MplsStatic.LocalLabels.LocalLabel.PathInfo',
            False, 
            [
            _MetaInfoClassMember('next-hop-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Next-Hop Interface Name
                ''',
                'next_hop_interface_name',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('next-hop-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Next-Hop Ipv4 Address
                ''',
                'next_hop_ipv4_address',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('next-hop-ipv4-address-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Next-Hop Ipv4 Set
                ''',
                'next_hop_ipv4_address_set',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('next-hop-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Next-Hop Label
                ''',
                'next_hop_label',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('next-hop-label-type', REFERENCE_ENUM_CLASS, 'MgmtStaticNhLblEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticNhLblEnum', 
                [], [], 
                '''                Next-Hop Label Type
                ''',
                'next_hop_label_type',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('path', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path Number
                ''',
                'path',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'MgmtStaticPathEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticPathEnum', 
                [], [], 
                '''                Path Type
                ''',
                'type',
                'Cisco-IOS-XR-mpls-static-oper', False),
            ],
            'Cisco-IOS-XR-mpls-static-oper',
            'path-info',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper'
        ),
    },
    'MplsStatic.LocalLabels.LocalLabel' : {
        'meta_info' : _MetaInfoClass('MplsStatic.LocalLabels.LocalLabel',
            False, 
            [
            _MetaInfoClassMember('local-label-id', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Local Label
                ''',
                'local_label_id',
                'Cisco-IOS-XR-mpls-static-oper', True),
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label value
                ''',
                'label',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('label-mode', REFERENCE_ENUM_CLASS, 'MgmtMplsStaticLabelModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtMplsStaticLabelModeEnum', 
                [], [], 
                '''                Label Mode
                ''',
                'label_mode',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('label-status', REFERENCE_ENUM_CLASS, 'MgmtMplsStaticLabelStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtMplsStaticLabelStatusEnum', 
                [], [], 
                '''                Label Status
                ''',
                'label_status',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('path-info', REFERENCE_LIST, 'PathInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStatic.LocalLabels.LocalLabel.PathInfo', 
                [], [], 
                '''                Path Information
                ''',
                'path_info',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('prefix', REFERENCE_CLASS, 'Prefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStatic.LocalLabels.LocalLabel.Prefix', 
                [], [], 
                '''                Prefix Information
                ''',
                'prefix',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-mpls-static-oper', False),
            ],
            'Cisco-IOS-XR-mpls-static-oper',
            'local-label',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper'
        ),
    },
    'MplsStatic.LocalLabels' : {
        'meta_info' : _MetaInfoClass('MplsStatic.LocalLabels',
            False, 
            [
            _MetaInfoClassMember('local-label', REFERENCE_LIST, 'LocalLabel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStatic.LocalLabels.LocalLabel', 
                [], [], 
                '''                Data for static label
                ''',
                'local_label',
                'Cisco-IOS-XR-mpls-static-oper', False),
            ],
            'Cisco-IOS-XR-mpls-static-oper',
            'local-labels',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper'
        ),
    },
    'MplsStatic' : {
        'meta_info' : _MetaInfoClass('MplsStatic',
            False, 
            [
            _MetaInfoClassMember('local-labels', REFERENCE_CLASS, 'LocalLabels' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStatic.LocalLabels', 
                [], [], 
                '''                data for static local-label table
                ''',
                'local_labels',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStatic.Summary', 
                [], [], 
                '''                MPLS STATIC summary data
                ''',
                'summary',
                'Cisco-IOS-XR-mpls-static-oper', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStatic.Vrfs', 
                [], [], 
                '''                VRF table
                ''',
                'vrfs',
                'Cisco-IOS-XR-mpls-static-oper', False),
            ],
            'Cisco-IOS-XR-mpls-static-oper',
            'mpls-static',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper'
        ),
    },
}
_meta_table['MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix.Prefix_']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Lsps.Lsp']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Lsps.Lsp']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Lsps']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix_']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.LocalLabels']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Lsps']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.LocalLabels']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf']['meta_info'].parent =_meta_table['MplsStatic.Vrfs']['meta_info']
_meta_table['MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix_']['meta_info'].parent =_meta_table['MplsStatic.LocalLabels.LocalLabel.Prefix']['meta_info']
_meta_table['MplsStatic.LocalLabels.LocalLabel.Prefix']['meta_info'].parent =_meta_table['MplsStatic.LocalLabels.LocalLabel']['meta_info']
_meta_table['MplsStatic.LocalLabels.LocalLabel.PathInfo']['meta_info'].parent =_meta_table['MplsStatic.LocalLabels.LocalLabel']['meta_info']
_meta_table['MplsStatic.LocalLabels.LocalLabel']['meta_info'].parent =_meta_table['MplsStatic.LocalLabels']['meta_info']
_meta_table['MplsStatic.Vrfs']['meta_info'].parent =_meta_table['MplsStatic']['meta_info']
_meta_table['MplsStatic.Summary']['meta_info'].parent =_meta_table['MplsStatic']['meta_info']
_meta_table['MplsStatic.LocalLabels']['meta_info'].parent =_meta_table['MplsStatic']['meta_info']
