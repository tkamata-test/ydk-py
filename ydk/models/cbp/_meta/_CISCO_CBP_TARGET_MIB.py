


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOCBPTARGETMIB.CcbptTargetAttachCfg' : {
        'meta_info' : _MetaInfoClass('CISCOCBPTARGETMIB.CcbptTargetAttachCfg',
            False, 
            [
            _MetaInfoClassMember('ccbptPolicyIdNext', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the next available value of 
                ccbptPolicyId that can be used to create a new conceptual
                row in the ccbptTargetTable.  If no available identifier
                exists, then this object will have the value '0'.
                ''',
                'ccbptpolicyidnext',
                'CISCO-CBP-TARGET-MIB', False),
            _MetaInfoClassMember('ccbptTargetTableLastChange', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime at the time of the last
                change to an entry in the ccbptTargetTable.
                ''',
                'ccbpttargettablelastchange',
                'CISCO-CBP-TARGET-MIB', False),
            ],
            'CISCO-CBP-TARGET-MIB',
            'ccbptTargetAttachCfg',
            _yang_ns._namespaces['CISCO-CBP-TARGET-MIB'],
        'ydk.models.cbp.CISCO_CBP_TARGET_MIB'
        ),
    },
    'CISCOCBPTARGETMIB.CcbptTargetTable.CcbptTargetEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCBPTARGETMIB.CcbptTargetTable.CcbptTargetEntry',
            False, 
            [
            _MetaInfoClassMember('ccbptPolicyId', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                Unique identifier of this class-based policy instance.
                ''',
                'ccbptpolicyid',
                'CISCO-CBP-TARGET-MIB', True),
            _MetaInfoClassMember('ccbptPolicySourceType', REFERENCE_ENUM_CLASS, 'CcbptPolicySourceType_Enum' , 'ydk.models.cbp.CISCO_CBP_TARGET_TC_MIB', 'CcbptPolicySourceType_Enum', 
                [], [], 
                '''                The source-type of the class-based policy for this target.
                The source-type refers to the source of the class-based
                policy definition.  The intent of this object is to allow
                implementations to distinguish between different MIBs
                defining policy-maps. 
                ''',
                'ccbptpolicysourcetype',
                'CISCO-CBP-TARGET-MIB', True),
            _MetaInfoClassMember('ccbptTargetDir', REFERENCE_ENUM_CLASS, 'CcbptTargetDirection_Enum' , 'ydk.models.cbp.CISCO_CBP_TARGET_TC_MIB', 'CcbptTargetDirection_Enum', 
                [], [], 
                '''                The direction relative to the ccbptTargetId for this class
                based policy attachment.  
                ''',
                'ccbpttargetdir',
                'CISCO-CBP-TARGET-MIB', True),
            _MetaInfoClassMember('ccbptTargetId', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The target identifier for this class-based policy attachment.
                For decoding the ccbptTargetId refer to the ccbptTargetType
                object and the CcbptTargetType description.
                ''',
                'ccbpttargetid',
                'CISCO-CBP-TARGET-MIB', True),
            _MetaInfoClassMember('ccbptTargetType', REFERENCE_ENUM_CLASS, 'CcbptTargetType_Enum' , 'ydk.models.cbp.CISCO_CBP_TARGET_TC_MIB', 'CcbptTargetType_Enum', 
                [], [], 
                '''                The type of target for this class-based policy attachment.
                This object identifies the format of the ccbptTargetId for
                this entry.
                ''',
                'ccbpttargettype',
                'CISCO-CBP-TARGET-MIB', True),
            _MetaInfoClassMember('ccbptPolicyAttachTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime for the last time that the corresponding
                ccbptTargetStatus instance transitioned to the 'active' state.  
                ''',
                'ccbptpolicyattachtime',
                'CISCO-CBP-TARGET-MIB', False),
            _MetaInfoClassMember('ccbptPolicyInstance', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                Refers to the first accessible object in the policy 
                instance table used to manage policy instance information 
                for policy-maps of this ccbptPolicySourceType.
                
                Specific MIB tables are not mentioned here as the intent of
                this mapping is to allow for different implementations to 
                refer to their supported class-based policy definition table
                without requiring support of a specific MIB module.
                ''',
                'ccbptpolicyinstance',
                'CISCO-CBP-TARGET-MIB', False),
            _MetaInfoClassMember('ccbptPolicyMap', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                Refers to the first accessible object in the policy-map
                definition table used to manage policy-map information
                for policy-maps for the corresponding ccbptPolicySourceType.
                
                Specific MIB tables are not mentioned here as the intent of
                this mapping is to allow for different implementations to 
                refer to their supported class-based policy definition table
                without requiring support of a specific MIB module.
                ''',
                'ccbptpolicymap',
                'CISCO-CBP-TARGET-MIB', False),
            _MetaInfoClassMember('ccbptTargetStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of the policy attachment to this target.  The
                value for the corresponding instance of each of the 
                following objects must be valid before the attachment 
                can be activated:
                    -ccbptTargetStorageType
                    -ccbptPolicyMap
                
                Observe that no corresponding instance of any object in 
                this table can be modified when the value of this object is
                'active'.
                ''',
                'ccbpttargetstatus',
                'CISCO-CBP-TARGET-MIB', False),
            _MetaInfoClassMember('ccbptTargetStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This object indicates how the device stores the data 
                contained by the conceptual row.
                
                If an instance of this object has the value 'permanent',
                then this MIB definition does not require the SNMP entity
                to allow the instance of any object in the corresponding
                conceptual row to be writable through the SNMP.
                ''',
                'ccbpttargetstoragetype',
                'CISCO-CBP-TARGET-MIB', False),
            ],
            'CISCO-CBP-TARGET-MIB',
            'ccbptTargetEntry',
            _yang_ns._namespaces['CISCO-CBP-TARGET-MIB'],
        'ydk.models.cbp.CISCO_CBP_TARGET_MIB'
        ),
    },
    'CISCOCBPTARGETMIB.CcbptTargetTable' : {
        'meta_info' : _MetaInfoClass('CISCOCBPTARGETMIB.CcbptTargetTable',
            False, 
            [
            _MetaInfoClassMember('ccbptTargetEntry', REFERENCE_LIST, 'CcbptTargetEntry' , 'ydk.models.cbp.CISCO_CBP_TARGET_MIB', 'CISCOCBPTARGETMIB.CcbptTargetTable.CcbptTargetEntry', 
                [], [], 
                '''                Each entry describes a class-based policy attachment to a 
                particular target. 
                 
                The ccbptTargetType uniquely identifies the type of target
                in the attachment.  Additionally, the ccbptTargetId uniquely
                identifies the target in attachment and is of the format
                indicated by the ccbptTargetType.  The ccbptTargetDir 
                identifies the direction, relative to the ccbptTargetId, 
                to which the policy is attached.  The ccbptPolicySourceType
                identifies the source-type of the policy attached.  The 
                ccbptPolicyId uniquely identifies the policy within the scope
                of ccbptTargetType, ccbptTargetId, ccbptTargetDir, and 
                ccbptPolicySourceType.
                
                A class-based policy attachment to a target can be created 
                through other network management interfaces (e.g., the local
                console), in which case the SNMP entity will automatically 
                create an entry in this table.
                
                A class-based policy attachment to a target can be destroyed
                through other network management interfaces, in which case
                the SNMP entity will automatically destroy the corresponding
                entry in this table.
                
                A class-based policy attachment to a target can be created,
                destroyed, and modified through the SNMP using 
                ccbptTargetStatus using the semantics described by the 
                RowStatus Textual Convention.  However, when creating a new
                class-based policy attachment to a target, the value of
                ccbptPolicyIdNext should be used to identify the new policy
                within the scope of the target type, identifier, direction,
                and policy-source type.
                ''',
                'ccbpttargetentry',
                'CISCO-CBP-TARGET-MIB', False),
            ],
            'CISCO-CBP-TARGET-MIB',
            'ccbptTargetTable',
            _yang_ns._namespaces['CISCO-CBP-TARGET-MIB'],
        'ydk.models.cbp.CISCO_CBP_TARGET_MIB'
        ),
    },
    'CISCOCBPTARGETMIB' : {
        'meta_info' : _MetaInfoClass('CISCOCBPTARGETMIB',
            False, 
            [
            _MetaInfoClassMember('ccbptTargetAttachCfg', REFERENCE_CLASS, 'CcbptTargetAttachCfg' , 'ydk.models.cbp.CISCO_CBP_TARGET_MIB', 'CISCOCBPTARGETMIB.CcbptTargetAttachCfg', 
                [], [], 
                '''                ''',
                'ccbpttargetattachcfg',
                'CISCO-CBP-TARGET-MIB', False),
            _MetaInfoClassMember('ccbptTargetTable', REFERENCE_CLASS, 'CcbptTargetTable' , 'ydk.models.cbp.CISCO_CBP_TARGET_MIB', 'CISCOCBPTARGETMIB.CcbptTargetTable', 
                [], [], 
                '''                This table describes the class-based policy attachments to
                to specific targets.
                ''',
                'ccbpttargettable',
                'CISCO-CBP-TARGET-MIB', False),
            ],
            'CISCO-CBP-TARGET-MIB',
            'CISCO-CBP-TARGET-MIB',
            _yang_ns._namespaces['CISCO-CBP-TARGET-MIB'],
        'ydk.models.cbp.CISCO_CBP_TARGET_MIB'
        ),
    },
}
_meta_table['CISCOCBPTARGETMIB.CcbptTargetTable.CcbptTargetEntry']['meta_info'].parent =_meta_table['CISCOCBPTARGETMIB.CcbptTargetTable']['meta_info']
_meta_table['CISCOCBPTARGETMIB.CcbptTargetAttachCfg']['meta_info'].parent =_meta_table['CISCOCBPTARGETMIB']['meta_info']
_meta_table['CISCOCBPTARGETMIB.CcbptTargetTable']['meta_info'].parent =_meta_table['CISCOCBPTARGETMIB']['meta_info']