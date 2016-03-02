


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'SpanTrafficDirection_Enum' : _MetaInfoEnum('SpanTrafficDirection_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg',
        {
            'rx-only':'RX_ONLY',
            'tx-only':'TX_ONLY',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg']),
    'SpanMirrorInterval_Enum' : _MetaInfoEnum('SpanMirrorInterval_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg',
        {
            '512':'Y_512',
            '1k':'Y_1K',
            '2k':'Y_2K',
            '4k':'Y_4K',
            '8k':'Y_8K',
            '16k':'Y_16K',
        }, 'Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg', _yang_ns._namespaces['Cisco-IOS-XR-Ethernet-SPAN-subscriber-cfg']),
}