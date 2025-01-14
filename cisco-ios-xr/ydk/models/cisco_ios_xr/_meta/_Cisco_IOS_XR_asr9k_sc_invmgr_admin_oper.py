


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'CardResetReasonEnum' : _MetaInfoEnum('CardResetReasonEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper',
        {
            'reset-unknown':'reset_unknown',
            'power-up':'power_up',
            'parity-error':'parity_error',
            'clear-config-reset':'clear_config_reset',
            'manual-reset':'manual_reset',
            'watch-dog-timeout-reset':'watch_dog_timeout_reset',
            'resource-overflow-reset':'resource_overflow_reset',
            'missing-task-reset':'missing_task_reset',
            'low-voltage-reset':'low_voltage_reset',
            'controller-reset':'controller_reset',
            'system-reset':'system_reset',
            'switchover-reset':'switchover_reset',
            'upgrade-reset':'upgrade_reset',
            'downgrade-reset':'downgrade_reset',
            'cache-error-reset':'cache_error_reset',
            'device-driver-reset':'device_driver_reset',
            'software-exception-reset':'software_exception_reset',
            'restore-config-reset':'restore_config_reset',
            'abort-rev-reset':'abort_rev_reset',
            'burn-boot-reset':'burn_boot_reset',
            'standby-cd-healthier-reset':'standby_cd_healthier_reset',
            'non-native-config-clear-reset':'non_native_config_clear_reset',
            'memory-protection-error-reset':'memory_protection_error_reset',
            'card-reset-reason-max':'card_reset_reason_max',
        }, 'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper']),
    'InvCardStateEnum' : _MetaInfoEnum('InvCardStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper',
        {
            'inv-card-not-present':'inv_card_not_present',
            'inv-card-present':'inv_card_present',
            'inv-card-reset':'inv_card_reset',
            'inv-card-booting':'inv_card_booting',
            'inv-card-mbi-booting':'inv_card_mbi_booting',
            'inv-card-running-mbi':'inv_card_running_mbi',
            'inv-card-running-ena':'inv_card_running_ena',
            'inv-card-bring-down':'inv_card_bring_down',
            'inv-card-ena-failure':'inv_card_ena_failure',
            'inv-card-f-diag-run':'inv_card_f_diag_run',
            'inv-card-f-diag-failure':'inv_card_f_diag_failure',
            'inv-card-powered':'inv_card_powered',
            'inv-card-unpowered':'inv_card_unpowered',
            'inv-card-mdr':'inv_card_mdr',
            'inv-card-mdr-running-mbi':'inv_card_mdr_running_mbi',
            'inv-card-main-t-mode':'inv_card_main_t_mode',
            'inv-card-admin-down':'inv_card_admin_down',
            'inv-card-no-mon':'inv_card_no_mon',
            'inv-card-unknown':'inv_card_unknown',
            'inv-card-failed':'inv_card_failed',
            'inv-card-ok':'inv_card_ok',
            'inv-card-missing':'inv_card_missing',
            'inv-card-field-diag-downloading':'inv_card_field_diag_downloading',
            'inv-card-field-diag-unmonitor':'inv_card_field_diag_unmonitor',
            'inv-card-fabric-field-diag-unmonitor':'inv_card_fabric_field_diag_unmonitor',
            'inv-card-field-diag-rp-launching':'inv_card_field_diag_rp_launching',
            'inv-card-field-diag-running':'inv_card_field_diag_running',
            'inv-card-field-diag-pass':'inv_card_field_diag_pass',
            'inv-card-field-diag-fail':'inv_card_field_diag_fail',
            'inv-card-field-diag-timeout':'inv_card_field_diag_timeout',
            'inv-card-disabled':'inv_card_disabled',
            'inv-card-spa-booting':'inv_card_spa_booting',
            'inv-card-not-allowed-online':'inv_card_not_allowed_online',
            'inv-card-stopped':'inv_card_stopped',
            'inv-card-incompatible-fw-ver':'inv_card_incompatible_fw_ver',
            'inv-card-fpd-hold':'inv_card_fpd_hold',
            'inv-card-node-prep':'inv_card_node_prep',
            'inv-card-updating-fpd':'inv_card_updating_fpd',
            'inv-card-num-states':'inv_card_num_states',
        }, 'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper']),
    'Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('alias', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                useful for storing an entity alias 
                ''',
                'alias',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-id-str', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                asset Identification string
                ''',
                'asset_id_str',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-identification', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                asset Identification
                ''',
                'asset_identification',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('ceport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if ce port found, 0 if not
                ''',
                'ceport',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('chip-hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                chip module hw revision string
                ''',
                'chip_hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('composite-class-code', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Major&minor class of the entity
                ''',
                'composite_class_code',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms 						what the
                entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('environmental-monitor-path', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                sysdb name of sensor in the envmon EDM
                ''',
                'environmental_monitor_path',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('group-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                indicates if this entity is group 						or not
                ''',
                'group_flag',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-asset-tags', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Manufacture Asset Tags
                ''',
                'manufacturer_asset_tags',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                manufacturer's name
                ''',
                'manufacturer_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('memory-size', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Size of memory associated with 						the entity
                where applicable
                ''',
                'memory_size',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('new-deviation-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for New Deviation Number 0x88
                ''',
                'new_deviation_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('physical-layer-interface-module-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for plim type if     applicable to
                this entity
                ''',
                'physical_layer_interface_module_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('redundancystate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for Redundancy State if    
                applicable to this entity
                ''',
                'redundancystate',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('unrecognized-fru', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if UnrecognizedFRU and 0 for recognizedFRU
                ''',
                'unrecognized_fru',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('xr-scoped', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if xr scoped, 0 if not
                ''',
                'xr_scoped',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes.BasicInfo', 
                [], [], 
                '''                Inventory information
                ''',
                'basic_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Power Shelf number
                ''',
                'number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', True),
            _MetaInfoClassMember('basic-attributes', REFERENCE_CLASS, 'BasicAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes', 
                [], [], 
                '''                Attributes
                ''',
                'basic_attributes',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'power-supply-shelf',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.PowerSupplyShelfs' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.PowerSupplyShelfs',
            False, 
            [
            _MetaInfoClassMember('power-supply-shelf', REFERENCE_LIST, 'PowerSupplyShelf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf', 
                [], [], 
                '''                Power Supply Shelf number
                ''',
                'power_supply_shelf',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'power-supply-shelfs',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'card-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('card-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card admin state: shutdown or not
                ''',
                'card_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-monitor-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card is monitored by a manager or left
                unmonitored
                ''',
                'card_monitor_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                card operation state
                ''',
                'card_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-reset-reason', REFERENCE_ENUM_CLASS, 'CardResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'CardResetReasonEnum', 
                [], [], 
                '''                card reset reason enum
                ''',
                'card_reset_reason',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-up-time', REFERENCE_CLASS, 'CardUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime', 
                [], [], 
                '''                card up time
                ''',
                'card_up_time',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                last card oper change state
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power admin state: up or down
                ''',
                'power_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-current-measurement', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power current: not implemented
                ''',
                'power_current_measurement',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Power operation state
                ''',
                'power_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('alias', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                useful for storing an entity alias 
                ''',
                'alias',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-id-str', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                asset Identification string
                ''',
                'asset_id_str',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-identification', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                asset Identification
                ''',
                'asset_identification',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('ceport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if ce port found, 0 if not
                ''',
                'ceport',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('chip-hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                chip module hw revision string
                ''',
                'chip_hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('composite-class-code', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Major&minor class of the entity
                ''',
                'composite_class_code',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms 						what the
                entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('environmental-monitor-path', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                sysdb name of sensor in the envmon EDM
                ''',
                'environmental_monitor_path',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('group-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                indicates if this entity is group 						or not
                ''',
                'group_flag',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-asset-tags', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Manufacture Asset Tags
                ''',
                'manufacturer_asset_tags',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                manufacturer's name
                ''',
                'manufacturer_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('memory-size', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Size of memory associated with 						the entity
                where applicable
                ''',
                'memory_size',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('new-deviation-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for New Deviation Number 0x88
                ''',
                'new_deviation_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('physical-layer-interface-module-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for plim type if     applicable to
                this entity
                ''',
                'physical_layer_interface_module_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('redundancystate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for Redundancy State if    
                applicable to this entity
                ''',
                'redundancystate',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('unrecognized-fru', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if UnrecognizedFRU and 0 for recognizedFRU
                ''',
                'unrecognized_fru',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('xr-scoped', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if xr scoped, 0 if not
                ''',
                'xr_scoped',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo', 
                [], [], 
                '''                Inventory information
                ''',
                'basic_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) inventory
                information
                ''',
                'fru_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port',
            False, 
            [
            _MetaInfoClassMember('basic-attributes', REFERENCE_CLASS, 'BasicAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes', 
                [], [], 
                '''                Attributes
                ''',
                'basic_attributes',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'port',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'card-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('card-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card admin state: shutdown or not
                ''',
                'card_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-monitor-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card is monitored by a manager or left
                unmonitored
                ''',
                'card_monitor_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                card operation state
                ''',
                'card_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-reset-reason', REFERENCE_ENUM_CLASS, 'CardResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'CardResetReasonEnum', 
                [], [], 
                '''                card reset reason enum
                ''',
                'card_reset_reason',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-up-time', REFERENCE_CLASS, 'CardUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime', 
                [], [], 
                '''                card up time
                ''',
                'card_up_time',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                last card oper change state
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power admin state: up or down
                ''',
                'power_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-current-measurement', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power current: not implemented
                ''',
                'power_current_measurement',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Power operation state
                ''',
                'power_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('alias', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                useful for storing an entity alias 
                ''',
                'alias',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-id-str', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                asset Identification string
                ''',
                'asset_id_str',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-identification', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                asset Identification
                ''',
                'asset_identification',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('ceport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if ce port found, 0 if not
                ''',
                'ceport',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('chip-hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                chip module hw revision string
                ''',
                'chip_hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('composite-class-code', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Major&minor class of the entity
                ''',
                'composite_class_code',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms 						what the
                entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('environmental-monitor-path', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                sysdb name of sensor in the envmon EDM
                ''',
                'environmental_monitor_path',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('group-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                indicates if this entity is group 						or not
                ''',
                'group_flag',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-asset-tags', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Manufacture Asset Tags
                ''',
                'manufacturer_asset_tags',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                manufacturer's name
                ''',
                'manufacturer_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('memory-size', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Size of memory associated with 						the entity
                where applicable
                ''',
                'memory_size',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('new-deviation-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for New Deviation Number 0x88
                ''',
                'new_deviation_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('physical-layer-interface-module-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for plim type if     applicable to
                this entity
                ''',
                'physical_layer_interface_module_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('redundancystate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for Redundancy State if    
                applicable to this entity
                ''',
                'redundancystate',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('unrecognized-fru', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if UnrecognizedFRU and 0 for recognizedFRU
                ''',
                'unrecognized_fru',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('xr-scoped', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if xr scoped, 0 if not
                ''',
                'xr_scoped',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.BasicInfo', 
                [], [], 
                '''                Inventory information
                ''',
                'basic_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) inventory
                information
                ''',
                'fru_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                portslot number
                ''',
                'number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', True),
            _MetaInfoClassMember('basic-attributes', REFERENCE_CLASS, 'BasicAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes', 
                [], [], 
                '''                Attributes
                ''',
                'basic_attributes',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('port', REFERENCE_CLASS, 'Port' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port', 
                [], [], 
                '''                Port string
                ''',
                'port',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'port-slot',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots',
            False, 
            [
            _MetaInfoClassMember('port-slot', REFERENCE_LIST, 'PortSlot' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot', 
                [], [], 
                '''                PortSlot number in the SPA/PLIM
                ''',
                'port_slot',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'port-slots',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'card-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('card-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card admin state: shutdown or not
                ''',
                'card_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-monitor-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card is monitored by a manager or left
                unmonitored
                ''',
                'card_monitor_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                card operation state
                ''',
                'card_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-reset-reason', REFERENCE_ENUM_CLASS, 'CardResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'CardResetReasonEnum', 
                [], [], 
                '''                card reset reason enum
                ''',
                'card_reset_reason',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-up-time', REFERENCE_CLASS, 'CardUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime', 
                [], [], 
                '''                card up time
                ''',
                'card_up_time',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                last card oper change state
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power admin state: up or down
                ''',
                'power_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-current-measurement', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power current: not implemented
                ''',
                'power_current_measurement',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Power operation state
                ''',
                'power_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('alias', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                useful for storing an entity alias 
                ''',
                'alias',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-id-str', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                asset Identification string
                ''',
                'asset_id_str',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-identification', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                asset Identification
                ''',
                'asset_identification',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('ceport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if ce port found, 0 if not
                ''',
                'ceport',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('chip-hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                chip module hw revision string
                ''',
                'chip_hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('composite-class-code', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Major&minor class of the entity
                ''',
                'composite_class_code',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms 						what the
                entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('environmental-monitor-path', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                sysdb name of sensor in the envmon EDM
                ''',
                'environmental_monitor_path',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('group-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                indicates if this entity is group 						or not
                ''',
                'group_flag',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-asset-tags', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Manufacture Asset Tags
                ''',
                'manufacturer_asset_tags',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                manufacturer's name
                ''',
                'manufacturer_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('memory-size', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Size of memory associated with 						the entity
                where applicable
                ''',
                'memory_size',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('new-deviation-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for New Deviation Number 0x88
                ''',
                'new_deviation_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('physical-layer-interface-module-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for plim type if     applicable to
                this entity
                ''',
                'physical_layer_interface_module_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('redundancystate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for Redundancy State if    
                applicable to this entity
                ''',
                'redundancystate',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('unrecognized-fru', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if UnrecognizedFRU and 0 for recognizedFRU
                ''',
                'unrecognized_fru',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('xr-scoped', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if xr scoped, 0 if not
                ''',
                'xr_scoped',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.BasicInfo', 
                [], [], 
                '''                Inventory information
                ''',
                'basic_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) inventory
                information
                ''',
                'fru_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                sensor number
                ''',
                'number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', True),
            _MetaInfoClassMember('basic-attributes', REFERENCE_CLASS, 'BasicAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes', 
                [], [], 
                '''                Attributes
                ''',
                'basic_attributes',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'sensor',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors',
            False, 
            [
            _MetaInfoClassMember('sensor', REFERENCE_LIST, 'Sensor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor', 
                [], [], 
                '''                Sensor number in the Module
                ''',
                'sensor',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'sensors',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.CardUpTime' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.CardUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'card-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('card-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card admin state: shutdown or not
                ''',
                'card_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-monitor-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card is monitored by a manager or left
                unmonitored
                ''',
                'card_monitor_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                card operation state
                ''',
                'card_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-reset-reason', REFERENCE_ENUM_CLASS, 'CardResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'CardResetReasonEnum', 
                [], [], 
                '''                card reset reason enum
                ''',
                'card_reset_reason',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-up-time', REFERENCE_CLASS, 'CardUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.CardUpTime', 
                [], [], 
                '''                card up time
                ''',
                'card_up_time',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                last card oper change state
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power admin state: up or down
                ''',
                'power_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-current-measurement', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power current: not implemented
                ''',
                'power_current_measurement',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Power operation state
                ''',
                'power_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('alias', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                useful for storing an entity alias 
                ''',
                'alias',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-id-str', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                asset Identification string
                ''',
                'asset_id_str',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-identification', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                asset Identification
                ''',
                'asset_identification',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('ceport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if ce port found, 0 if not
                ''',
                'ceport',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('chip-hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                chip module hw revision string
                ''',
                'chip_hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('composite-class-code', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Major&minor class of the entity
                ''',
                'composite_class_code',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms 						what the
                entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('environmental-monitor-path', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                sysdb name of sensor in the envmon EDM
                ''',
                'environmental_monitor_path',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('group-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                indicates if this entity is group 						or not
                ''',
                'group_flag',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-asset-tags', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Manufacture Asset Tags
                ''',
                'manufacturer_asset_tags',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                manufacturer's name
                ''',
                'manufacturer_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('memory-size', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Size of memory associated with 						the entity
                where applicable
                ''',
                'memory_size',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('new-deviation-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for New Deviation Number 0x88
                ''',
                'new_deviation_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('physical-layer-interface-module-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for plim type if     applicable to
                this entity
                ''',
                'physical_layer_interface_module_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('redundancystate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for Redundancy State if    
                applicable to this entity
                ''',
                'redundancystate',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('unrecognized-fru', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if UnrecognizedFRU and 0 for recognizedFRU
                ''',
                'unrecognized_fru',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('xr-scoped', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if xr scoped, 0 if not
                ''',
                'xr_scoped',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.BasicInfo', 
                [], [], 
                '''                Inventory information
                ''',
                'basic_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) inventory
                information
                ''',
                'fru_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module',
            False, 
            [
            _MetaInfoClassMember('basic-attributes', REFERENCE_CLASS, 'BasicAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes', 
                [], [], 
                '''                Attributes
                ''',
                'basic_attributes',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('port-slots', REFERENCE_CLASS, 'PortSlots' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots', 
                [], [], 
                '''                PortSlotTable contains all optics ports in a
                SPA/PLIM.
                ''',
                'port_slots',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('sensors', REFERENCE_CLASS, 'Sensors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors', 
                [], [], 
                '''                ModuleSensorTable contains all sensors in a
                Module.
                ''',
                'sensors',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'module',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.CardUpTime' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.CardUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'card-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('card-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card admin state: shutdown or not
                ''',
                'card_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-monitor-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card is monitored by a manager or left
                unmonitored
                ''',
                'card_monitor_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                card operation state
                ''',
                'card_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-reset-reason', REFERENCE_ENUM_CLASS, 'CardResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'CardResetReasonEnum', 
                [], [], 
                '''                card reset reason enum
                ''',
                'card_reset_reason',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-up-time', REFERENCE_CLASS, 'CardUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.CardUpTime', 
                [], [], 
                '''                card up time
                ''',
                'card_up_time',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                last card oper change state
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power admin state: up or down
                ''',
                'power_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-current-measurement', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power current: not implemented
                ''',
                'power_current_measurement',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Power operation state
                ''',
                'power_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('alias', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                useful for storing an entity alias 
                ''',
                'alias',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-id-str', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                asset Identification string
                ''',
                'asset_id_str',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-identification', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                asset Identification
                ''',
                'asset_identification',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('ceport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if ce port found, 0 if not
                ''',
                'ceport',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('chip-hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                chip module hw revision string
                ''',
                'chip_hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('composite-class-code', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Major&minor class of the entity
                ''',
                'composite_class_code',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms 						what the
                entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('environmental-monitor-path', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                sysdb name of sensor in the envmon EDM
                ''',
                'environmental_monitor_path',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('group-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                indicates if this entity is group 						or not
                ''',
                'group_flag',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-asset-tags', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Manufacture Asset Tags
                ''',
                'manufacturer_asset_tags',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                manufacturer's name
                ''',
                'manufacturer_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('memory-size', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Size of memory associated with 						the entity
                where applicable
                ''',
                'memory_size',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('new-deviation-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for New Deviation Number 0x88
                ''',
                'new_deviation_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('physical-layer-interface-module-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for plim type if     applicable to
                this entity
                ''',
                'physical_layer_interface_module_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('redundancystate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for Redundancy State if    
                applicable to this entity
                ''',
                'redundancystate',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('unrecognized-fru', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if UnrecognizedFRU and 0 for recognizedFRU
                ''',
                'unrecognized_fru',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('xr-scoped', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if xr scoped, 0 if not
                ''',
                'xr_scoped',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.BasicInfo', 
                [], [], 
                '''                Inventory information
                ''',
                'basic_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) inventory
                information
                ''',
                'fru_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                subslot number
                ''',
                'number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', True),
            _MetaInfoClassMember('basic-attributes', REFERENCE_CLASS, 'BasicAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes', 
                [], [], 
                '''                Attributes
                ''',
                'basic_attributes',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('module', REFERENCE_CLASS, 'Module' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module', 
                [], [], 
                '''                Module string
                ''',
                'module',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'sub-slot',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots',
            False, 
            [
            _MetaInfoClassMember('sub-slot', REFERENCE_LIST, 'SubSlot' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot', 
                [], [], 
                '''                SubSlot number
                ''',
                'sub_slot',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'sub-slots',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'card-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('card-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card admin state: shutdown or not
                ''',
                'card_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-monitor-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card is monitored by a manager or left
                unmonitored
                ''',
                'card_monitor_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                card operation state
                ''',
                'card_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-reset-reason', REFERENCE_ENUM_CLASS, 'CardResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'CardResetReasonEnum', 
                [], [], 
                '''                card reset reason enum
                ''',
                'card_reset_reason',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-up-time', REFERENCE_CLASS, 'CardUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime', 
                [], [], 
                '''                card up time
                ''',
                'card_up_time',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                last card oper change state
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power admin state: up or down
                ''',
                'power_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-current-measurement', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power current: not implemented
                ''',
                'power_current_measurement',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Power operation state
                ''',
                'power_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('alias', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                useful for storing an entity alias 
                ''',
                'alias',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-id-str', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                asset Identification string
                ''',
                'asset_id_str',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-identification', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                asset Identification
                ''',
                'asset_identification',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('ceport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if ce port found, 0 if not
                ''',
                'ceport',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('chip-hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                chip module hw revision string
                ''',
                'chip_hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('composite-class-code', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Major&minor class of the entity
                ''',
                'composite_class_code',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms 						what the
                entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('environmental-monitor-path', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                sysdb name of sensor in the envmon EDM
                ''',
                'environmental_monitor_path',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('group-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                indicates if this entity is group 						or not
                ''',
                'group_flag',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-asset-tags', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Manufacture Asset Tags
                ''',
                'manufacturer_asset_tags',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                manufacturer's name
                ''',
                'manufacturer_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('memory-size', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Size of memory associated with 						the entity
                where applicable
                ''',
                'memory_size',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('new-deviation-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for New Deviation Number 0x88
                ''',
                'new_deviation_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('physical-layer-interface-module-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for plim type if     applicable to
                this entity
                ''',
                'physical_layer_interface_module_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('redundancystate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for Redundancy State if    
                applicable to this entity
                ''',
                'redundancystate',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('unrecognized-fru', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if UnrecognizedFRU and 0 for recognizedFRU
                ''',
                'unrecognized_fru',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('xr-scoped', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if xr scoped, 0 if not
                ''',
                'xr_scoped',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.BasicInfo', 
                [], [], 
                '''                Inventory information
                ''',
                'basic_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) inventory
                information
                ''',
                'fru_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                sensor number
                ''',
                'number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', True),
            _MetaInfoClassMember('basic-attributes', REFERENCE_CLASS, 'BasicAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes', 
                [], [], 
                '''                Attributes
                ''',
                'basic_attributes',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'sensor',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors',
            False, 
            [
            _MetaInfoClassMember('sensor', REFERENCE_LIST, 'Sensor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor', 
                [], [], 
                '''                Sensor number in the Module
                ''',
                'sensor',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'sensors',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.CardUpTime' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.CardUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'card-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('card-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card admin state: shutdown or not
                ''',
                'card_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-monitor-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card is monitored by a manager or left
                unmonitored
                ''',
                'card_monitor_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                card operation state
                ''',
                'card_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-reset-reason', REFERENCE_ENUM_CLASS, 'CardResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'CardResetReasonEnum', 
                [], [], 
                '''                card reset reason enum
                ''',
                'card_reset_reason',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-up-time', REFERENCE_CLASS, 'CardUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.CardUpTime', 
                [], [], 
                '''                card up time
                ''',
                'card_up_time',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                last card oper change state
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power admin state: up or down
                ''',
                'power_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-current-measurement', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power current: not implemented
                ''',
                'power_current_measurement',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Power operation state
                ''',
                'power_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('alias', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                useful for storing an entity alias 
                ''',
                'alias',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-id-str', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                asset Identification string
                ''',
                'asset_id_str',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-identification', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                asset Identification
                ''',
                'asset_identification',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('ceport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if ce port found, 0 if not
                ''',
                'ceport',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('chip-hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                chip module hw revision string
                ''',
                'chip_hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('composite-class-code', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Major&minor class of the entity
                ''',
                'composite_class_code',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms 						what the
                entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('environmental-monitor-path', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                sysdb name of sensor in the envmon EDM
                ''',
                'environmental_monitor_path',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('group-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                indicates if this entity is group 						or not
                ''',
                'group_flag',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-asset-tags', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Manufacture Asset Tags
                ''',
                'manufacturer_asset_tags',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                manufacturer's name
                ''',
                'manufacturer_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('memory-size', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Size of memory associated with 						the entity
                where applicable
                ''',
                'memory_size',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('new-deviation-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for New Deviation Number 0x88
                ''',
                'new_deviation_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('physical-layer-interface-module-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for plim type if     applicable to
                this entity
                ''',
                'physical_layer_interface_module_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('redundancystate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for Redundancy State if    
                applicable to this entity
                ''',
                'redundancystate',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('unrecognized-fru', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if UnrecognizedFRU and 0 for recognizedFRU
                ''',
                'unrecognized_fru',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('xr-scoped', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if xr scoped, 0 if not
                ''',
                'xr_scoped',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.BasicInfo', 
                [], [], 
                '''                Inventory information
                ''',
                'basic_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) inventory
                information
                ''',
                'fru_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                node number
                ''',
                'number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', True),
            _MetaInfoClassMember('basic-attributes', REFERENCE_CLASS, 'BasicAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes', 
                [], [], 
                '''                Attributes
                ''',
                'basic_attributes',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('sensors', REFERENCE_CLASS, 'Sensors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors', 
                [], [], 
                '''                ModuleSensorTable contains all sensors in a
                Module.
                ''',
                'sensors',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'hw-component',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents',
            False, 
            [
            _MetaInfoClassMember('hw-component', REFERENCE_LIST, 'HwComponent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent', 
                [], [], 
                '''                HWComponent number
                ''',
                'hw_component',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'hw-components',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'card-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('card-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card admin state: shutdown or not
                ''',
                'card_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-monitor-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card is monitored by a manager or left
                unmonitored
                ''',
                'card_monitor_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                card operation state
                ''',
                'card_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-reset-reason', REFERENCE_ENUM_CLASS, 'CardResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'CardResetReasonEnum', 
                [], [], 
                '''                card reset reason enum
                ''',
                'card_reset_reason',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-up-time', REFERENCE_CLASS, 'CardUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime', 
                [], [], 
                '''                card up time
                ''',
                'card_up_time',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                last card oper change state
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power admin state: up or down
                ''',
                'power_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-current-measurement', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power current: not implemented
                ''',
                'power_current_measurement',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Power operation state
                ''',
                'power_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('alias', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                useful for storing an entity alias 
                ''',
                'alias',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-id-str', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                asset Identification string
                ''',
                'asset_id_str',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-identification', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                asset Identification
                ''',
                'asset_identification',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('ceport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if ce port found, 0 if not
                ''',
                'ceport',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('chip-hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                chip module hw revision string
                ''',
                'chip_hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('composite-class-code', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Major&minor class of the entity
                ''',
                'composite_class_code',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms 						what the
                entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('environmental-monitor-path', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                sysdb name of sensor in the envmon EDM
                ''',
                'environmental_monitor_path',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('group-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                indicates if this entity is group 						or not
                ''',
                'group_flag',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-asset-tags', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Manufacture Asset Tags
                ''',
                'manufacturer_asset_tags',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                manufacturer's name
                ''',
                'manufacturer_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('memory-size', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Size of memory associated with 						the entity
                where applicable
                ''',
                'memory_size',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('new-deviation-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for New Deviation Number 0x88
                ''',
                'new_deviation_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('physical-layer-interface-module-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for plim type if     applicable to
                this entity
                ''',
                'physical_layer_interface_module_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('redundancystate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for Redundancy State if    
                applicable to this entity
                ''',
                'redundancystate',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('unrecognized-fru', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if UnrecognizedFRU and 0 for recognizedFRU
                ''',
                'unrecognized_fru',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('xr-scoped', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if xr scoped, 0 if not
                ''',
                'xr_scoped',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo', 
                [], [], 
                '''                Inventory information
                ''',
                'basic_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) inventory
                information
                ''',
                'fru_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port',
            False, 
            [
            _MetaInfoClassMember('basic-attributes', REFERENCE_CLASS, 'BasicAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes', 
                [], [], 
                '''                Attributes
                ''',
                'basic_attributes',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'port',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'card-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('card-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card admin state: shutdown or not
                ''',
                'card_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-monitor-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card is monitored by a manager or left
                unmonitored
                ''',
                'card_monitor_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                card operation state
                ''',
                'card_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-reset-reason', REFERENCE_ENUM_CLASS, 'CardResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'CardResetReasonEnum', 
                [], [], 
                '''                card reset reason enum
                ''',
                'card_reset_reason',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-up-time', REFERENCE_CLASS, 'CardUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime', 
                [], [], 
                '''                card up time
                ''',
                'card_up_time',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                last card oper change state
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power admin state: up or down
                ''',
                'power_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-current-measurement', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power current: not implemented
                ''',
                'power_current_measurement',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Power operation state
                ''',
                'power_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('alias', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                useful for storing an entity alias 
                ''',
                'alias',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-id-str', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                asset Identification string
                ''',
                'asset_id_str',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-identification', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                asset Identification
                ''',
                'asset_identification',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('ceport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if ce port found, 0 if not
                ''',
                'ceport',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('chip-hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                chip module hw revision string
                ''',
                'chip_hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('composite-class-code', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Major&minor class of the entity
                ''',
                'composite_class_code',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms 						what the
                entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('environmental-monitor-path', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                sysdb name of sensor in the envmon EDM
                ''',
                'environmental_monitor_path',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('group-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                indicates if this entity is group 						or not
                ''',
                'group_flag',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-asset-tags', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Manufacture Asset Tags
                ''',
                'manufacturer_asset_tags',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                manufacturer's name
                ''',
                'manufacturer_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('memory-size', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Size of memory associated with 						the entity
                where applicable
                ''',
                'memory_size',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('new-deviation-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for New Deviation Number 0x88
                ''',
                'new_deviation_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('physical-layer-interface-module-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for plim type if     applicable to
                this entity
                ''',
                'physical_layer_interface_module_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('redundancystate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for Redundancy State if    
                applicable to this entity
                ''',
                'redundancystate',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('unrecognized-fru', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if UnrecognizedFRU and 0 for recognizedFRU
                ''',
                'unrecognized_fru',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('xr-scoped', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if xr scoped, 0 if not
                ''',
                'xr_scoped',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.BasicInfo', 
                [], [], 
                '''                Inventory information
                ''',
                'basic_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) inventory
                information
                ''',
                'fru_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                portslot number
                ''',
                'number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', True),
            _MetaInfoClassMember('basic-attributes', REFERENCE_CLASS, 'BasicAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes', 
                [], [], 
                '''                Attributes
                ''',
                'basic_attributes',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('port', REFERENCE_CLASS, 'Port' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port', 
                [], [], 
                '''                Port string
                ''',
                'port',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'port-slot',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots',
            False, 
            [
            _MetaInfoClassMember('port-slot', REFERENCE_LIST, 'PortSlot' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot', 
                [], [], 
                '''                PortSlot number in the SPA/PLIM
                ''',
                'port_slot',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'port-slots',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'card-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('card-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card admin state: shutdown or not
                ''',
                'card_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-monitor-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card is monitored by a manager or left
                unmonitored
                ''',
                'card_monitor_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                card operation state
                ''',
                'card_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-reset-reason', REFERENCE_ENUM_CLASS, 'CardResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'CardResetReasonEnum', 
                [], [], 
                '''                card reset reason enum
                ''',
                'card_reset_reason',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-up-time', REFERENCE_CLASS, 'CardUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime', 
                [], [], 
                '''                card up time
                ''',
                'card_up_time',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                last card oper change state
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power admin state: up or down
                ''',
                'power_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-current-measurement', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power current: not implemented
                ''',
                'power_current_measurement',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Power operation state
                ''',
                'power_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('alias', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                useful for storing an entity alias 
                ''',
                'alias',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-id-str', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                asset Identification string
                ''',
                'asset_id_str',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-identification', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                asset Identification
                ''',
                'asset_identification',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('ceport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if ce port found, 0 if not
                ''',
                'ceport',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('chip-hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                chip module hw revision string
                ''',
                'chip_hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('composite-class-code', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Major&minor class of the entity
                ''',
                'composite_class_code',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms 						what the
                entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('environmental-monitor-path', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                sysdb name of sensor in the envmon EDM
                ''',
                'environmental_monitor_path',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('group-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                indicates if this entity is group 						or not
                ''',
                'group_flag',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-asset-tags', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Manufacture Asset Tags
                ''',
                'manufacturer_asset_tags',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                manufacturer's name
                ''',
                'manufacturer_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('memory-size', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Size of memory associated with 						the entity
                where applicable
                ''',
                'memory_size',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('new-deviation-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for New Deviation Number 0x88
                ''',
                'new_deviation_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('physical-layer-interface-module-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for plim type if     applicable to
                this entity
                ''',
                'physical_layer_interface_module_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('redundancystate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for Redundancy State if    
                applicable to this entity
                ''',
                'redundancystate',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('unrecognized-fru', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if UnrecognizedFRU and 0 for recognizedFRU
                ''',
                'unrecognized_fru',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('xr-scoped', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if xr scoped, 0 if not
                ''',
                'xr_scoped',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.BasicInfo', 
                [], [], 
                '''                Inventory information
                ''',
                'basic_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) inventory
                information
                ''',
                'fru_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                sensor number
                ''',
                'number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', True),
            _MetaInfoClassMember('basic-attributes', REFERENCE_CLASS, 'BasicAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes', 
                [], [], 
                '''                Attributes
                ''',
                'basic_attributes',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'sensor',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors',
            False, 
            [
            _MetaInfoClassMember('sensor', REFERENCE_LIST, 'Sensor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor', 
                [], [], 
                '''                Sensor number in the Module
                ''',
                'sensor',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'sensors',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.CardUpTime' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.CardUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'card-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('card-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card admin state: shutdown or not
                ''',
                'card_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-monitor-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card is monitored by a manager or left
                unmonitored
                ''',
                'card_monitor_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                card operation state
                ''',
                'card_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-reset-reason', REFERENCE_ENUM_CLASS, 'CardResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'CardResetReasonEnum', 
                [], [], 
                '''                card reset reason enum
                ''',
                'card_reset_reason',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-up-time', REFERENCE_CLASS, 'CardUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.CardUpTime', 
                [], [], 
                '''                card up time
                ''',
                'card_up_time',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                last card oper change state
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power admin state: up or down
                ''',
                'power_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-current-measurement', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power current: not implemented
                ''',
                'power_current_measurement',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Power operation state
                ''',
                'power_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('alias', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                useful for storing an entity alias 
                ''',
                'alias',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-id-str', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                asset Identification string
                ''',
                'asset_id_str',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-identification', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                asset Identification
                ''',
                'asset_identification',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('ceport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if ce port found, 0 if not
                ''',
                'ceport',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('chip-hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                chip module hw revision string
                ''',
                'chip_hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('composite-class-code', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Major&minor class of the entity
                ''',
                'composite_class_code',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms 						what the
                entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('environmental-monitor-path', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                sysdb name of sensor in the envmon EDM
                ''',
                'environmental_monitor_path',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('group-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                indicates if this entity is group 						or not
                ''',
                'group_flag',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-asset-tags', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Manufacture Asset Tags
                ''',
                'manufacturer_asset_tags',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                manufacturer's name
                ''',
                'manufacturer_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('memory-size', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Size of memory associated with 						the entity
                where applicable
                ''',
                'memory_size',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('new-deviation-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for New Deviation Number 0x88
                ''',
                'new_deviation_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('physical-layer-interface-module-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for plim type if     applicable to
                this entity
                ''',
                'physical_layer_interface_module_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('redundancystate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for Redundancy State if    
                applicable to this entity
                ''',
                'redundancystate',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('unrecognized-fru', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if UnrecognizedFRU and 0 for recognizedFRU
                ''',
                'unrecognized_fru',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('xr-scoped', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if xr scoped, 0 if not
                ''',
                'xr_scoped',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.BasicInfo', 
                [], [], 
                '''                Inventory information
                ''',
                'basic_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) inventory
                information
                ''',
                'fru_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards.Card' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards.Card',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card number
                ''',
                'number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', True),
            _MetaInfoClassMember('basic-attributes', REFERENCE_CLASS, 'BasicAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes', 
                [], [], 
                '''                Attributes
                ''',
                'basic_attributes',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('hw-components', REFERENCE_CLASS, 'HwComponents' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents', 
                [], [], 
                '''                HWComponent table contains all HW modules
                within the card 
                ''',
                'hw_components',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('port-slots', REFERENCE_CLASS, 'PortSlots' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots', 
                [], [], 
                '''                PortSlotTable contains all optics ports in a
                SPA/PLIM.
                ''',
                'port_slots',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('sensors', REFERENCE_CLASS, 'Sensors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors', 
                [], [], 
                '''                ModuleSensorTable contains all sensors in a
                Module.
                ''',
                'sensors',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('sub-slots', REFERENCE_CLASS, 'SubSlots' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots', 
                [], [], 
                '''                SubSlotTable contains all subslots in a
                Slot
                ''',
                'sub_slots',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'card',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.Cards' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.Cards',
            False, 
            [
            _MetaInfoClassMember('card', REFERENCE_LIST, 'Card' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards.Card', 
                [], [], 
                '''                Card number
                ''',
                'card',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'cards',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.LastOperationalStateChange' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.LastOperationalStateChange',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'last-operational-state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.CardUpTime' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.CardUpTime',
            False, 
            [
            _MetaInfoClassMember('time-in-nano-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Nano-seconds
                ''',
                'time_in_nano_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('time-in-seconds', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time Value in Seconds
                ''',
                'time_in_seconds',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'card-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo',
            False, 
            [
            _MetaInfoClassMember('card-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card admin state: shutdown or not
                ''',
                'card_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-monitor-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                card is monitored by a manager or left
                unmonitored
                ''',
                'card_monitor_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                card operation state
                ''',
                'card_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-reset-reason', REFERENCE_ENUM_CLASS, 'CardResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'CardResetReasonEnum', 
                [], [], 
                '''                card reset reason enum
                ''',
                'card_reset_reason',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('card-up-time', REFERENCE_CLASS, 'CardUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.CardUpTime', 
                [], [], 
                '''                card up time
                ''',
                'card_up_time',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('last-operational-state-change', REFERENCE_CLASS, 'LastOperationalStateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.LastOperationalStateChange', 
                [], [], 
                '''                last card oper change state
                ''',
                'last_operational_state_change',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-administrative-state', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power admin state: up or down
                ''',
                'power_administrative_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-current-measurement', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                power current: not implemented
                ''',
                'power_current_measurement',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-operational-state', REFERENCE_ENUM_CLASS, 'InvCardStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'InvCardStateEnum', 
                [], [], 
                '''                Power operation state
                ''',
                'power_operational_state',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'fru-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.BasicAttributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.BasicAttributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('alias', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                useful for storing an entity alias 
                ''',
                'alias',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-id-str', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                asset Identification string
                ''',
                'asset_id_str',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-identification', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                asset Identification
                ''',
                'asset_identification',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('ceport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if ce port found, 0 if not
                ''',
                'ceport',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('chip-hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                chip module hw revision string
                ''',
                'chip_hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('composite-class-code', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Major&minor class of the entity
                ''',
                'composite_class_code',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms 						what the
                entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('environmental-monitor-path', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                sysdb name of sensor in the envmon EDM
                ''',
                'environmental_monitor_path',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('group-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                indicates if this entity is group 						or not
                ''',
                'group_flag',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-asset-tags', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Manufacture Asset Tags
                ''',
                'manufacturer_asset_tags',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                manufacturer's name
                ''',
                'manufacturer_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('memory-size', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Size of memory associated with 						the entity
                where applicable
                ''',
                'memory_size',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('new-deviation-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for New Deviation Number 0x88
                ''',
                'new_deviation_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('physical-layer-interface-module-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for plim type if     applicable to
                this entity
                ''',
                'physical_layer_interface_module_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('redundancystate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for Redundancy State if    
                applicable to this entity
                ''',
                'redundancystate',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('unrecognized-fru', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if UnrecognizedFRU and 0 for recognizedFRU
                ''',
                'unrecognized_fru',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('xr-scoped', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if xr scoped, 0 if not
                ''',
                'xr_scoped',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot.BasicAttributes' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot.BasicAttributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.BasicAttributes.BasicInfo', 
                [], [], 
                '''                Inventory information
                ''',
                'basic_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('fru-info', REFERENCE_CLASS, 'FruInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo', 
                [], [], 
                '''                Field Replaceable Unit (FRU) inventory
                information
                ''',
                'fru_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots.Slot' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots.Slot',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Slot number
                ''',
                'number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', True),
            _MetaInfoClassMember('basic-attributes', REFERENCE_CLASS, 'BasicAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.BasicAttributes', 
                [], [], 
                '''                Attributes
                ''',
                'basic_attributes',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('cards', REFERENCE_CLASS, 'Cards' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot.Cards', 
                [], [], 
                '''                Card table contains all cards in the slot
                ''',
                'cards',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'slot',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.Slots' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.Slots',
            False, 
            [
            _MetaInfoClassMember('slot', REFERENCE_LIST, 'Slot' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots.Slot', 
                [], [], 
                '''                Slot number
                ''',
                'slot',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'slots',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('alias', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                useful for storing an entity alias 
                ''',
                'alias',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-id-str', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                asset Identification string
                ''',
                'asset_id_str',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-identification', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                asset Identification
                ''',
                'asset_identification',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('ceport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if ce port found, 0 if not
                ''',
                'ceport',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('chip-hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                chip module hw revision string
                ''',
                'chip_hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('composite-class-code', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Major&minor class of the entity
                ''',
                'composite_class_code',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms 						what the
                entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('environmental-monitor-path', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                sysdb name of sensor in the envmon EDM
                ''',
                'environmental_monitor_path',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('group-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                indicates if this entity is group 						or not
                ''',
                'group_flag',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-asset-tags', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Manufacture Asset Tags
                ''',
                'manufacturer_asset_tags',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                manufacturer's name
                ''',
                'manufacturer_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('memory-size', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Size of memory associated with 						the entity
                where applicable
                ''',
                'memory_size',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('new-deviation-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for New Deviation Number 0x88
                ''',
                'new_deviation_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('physical-layer-interface-module-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for plim type if     applicable to
                this entity
                ''',
                'physical_layer_interface_module_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('redundancystate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for Redundancy State if    
                applicable to this entity
                ''',
                'redundancystate',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('unrecognized-fru', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if UnrecognizedFRU and 0 for recognizedFRU
                ''',
                'unrecognized_fru',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('xr-scoped', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if xr scoped, 0 if not
                ''',
                'xr_scoped',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes.BasicInfo', 
                [], [], 
                '''                Inventory information
                ''',
                'basic_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.FanTraies.FanTray' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.FanTraies.FanTray',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Fan tray number
                ''',
                'number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', True),
            _MetaInfoClassMember('basic-attributes', REFERENCE_CLASS, 'BasicAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes', 
                [], [], 
                '''                Attributes
                ''',
                'basic_attributes',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'fan-tray',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.FanTraies' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.FanTraies',
            False, 
            [
            _MetaInfoClassMember('fan-tray', REFERENCE_LIST, 'FanTray' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.FanTraies.FanTray', 
                [], [], 
                '''                Fan tray number
                ''',
                'fan_tray',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'fan-traies',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes.PowerSupplyGroupInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes.PowerSupplyGroupInfo',
            False, 
            [
            _MetaInfoClassMember('power-group-available-current', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                available current
                ''',
                'power_group_available_current',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-group-drawn-current', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                drawn current
                ''',
                'power_group_drawn_current',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-group-power-units', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                power units
                ''',
                'power_group_power_units',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-group-redundancy-mode', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                redundancy mode
                ''',
                'power_group_redundancy_mode',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'power-supply-group-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes',
            False, 
            [
            _MetaInfoClassMember('power-supply-group-info', REFERENCE_CLASS, 'PowerSupplyGroupInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes.PowerSupplyGroupInfo', 
                [], [], 
                '''                Power supply group information
                ''',
                'power_supply_group_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'power-supply-zone-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Power Zone number
                ''',
                'number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', True),
            _MetaInfoClassMember('power-supply-zone-attributes', REFERENCE_CLASS, 'PowerSupplyZoneAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes', 
                [], [], 
                '''                Power suppy zone attributes 
                ''',
                'power_supply_zone_attributes',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'power-supply-zone',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.PowerSupplyZones' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.PowerSupplyZones',
            False, 
            [
            _MetaInfoClassMember('power-supply-zone', REFERENCE_LIST, 'PowerSupplyZone' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone', 
                [], [], 
                '''                Power Supply Zone number
                ''',
                'power_supply_zone',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'power-supply-zones',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.BasicAttributes.BasicInfo' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.BasicAttributes.BasicInfo',
            False, 
            [
            _MetaInfoClassMember('alias', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                useful for storing an entity alias 
                ''',
                'alias',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-id-str', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                asset Identification string
                ''',
                'asset_id_str',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('asset-identification', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                asset Identification
                ''',
                'asset_identification',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('ceport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if ce port found, 0 if not
                ''',
                'ceport',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('chip-hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                chip module hw revision string
                ''',
                'chip_hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('composite-class-code', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Major&minor class of the entity
                ''',
                'composite_class_code',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                describes in user-readable terms 						what the
                entity in question does
                ''',
                'description',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('environmental-monitor-path', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                sysdb name of sensor in the envmon EDM
                ''',
                'environmental_monitor_path',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('firmware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                firmware revision string
                ''',
                'firmware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('group-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                indicates if this entity is group 						or not
                ''',
                'group_flag',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('hardware-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                hw revision string
                ''',
                'hardware_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('is-field-replaceable-unit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if Field Replaceable Unit 0, if not
                ''',
                'is_field_replaceable_unit',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-asset-tags', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Manufacture Asset Tags
                ''',
                'manufacturer_asset_tags',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('manufacturer-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                manufacturer's name
                ''',
                'manufacturer_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('memory-size', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Size of memory associated with 						the entity
                where applicable
                ''',
                'memory_size',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('model-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                model name
                ''',
                'model_name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                name string for the entity
                ''',
                'name',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('new-deviation-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for New Deviation Number 0x88
                ''',
                'new_deviation_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('physical-layer-interface-module-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for plim type if     applicable to
                this entity
                ''',
                'physical_layer_interface_module_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('redundancystate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                integer value for Redundancy State if    
                applicable to this entity
                ''',
                'redundancystate',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('software-revision', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                software revision string
                ''',
                'software_revision',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('unrecognized-fru', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if UnrecognizedFRU and 0 for recognizedFRU
                ''',
                'unrecognized_fru',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('vendor-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                maps to the vendor OID string
                ''',
                'vendor_type',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('xr-scoped', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                1 if xr scoped, 0 if not
                ''',
                'xr_scoped',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack.BasicAttributes' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack.BasicAttributes',
            False, 
            [
            _MetaInfoClassMember('basic-info', REFERENCE_CLASS, 'BasicInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.BasicAttributes.BasicInfo', 
                [], [], 
                '''                Inventory information
                ''',
                'basic_info',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'basic-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks.Rack' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks.Rack',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Rack number
                ''',
                'number',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', True),
            _MetaInfoClassMember('basic-attributes', REFERENCE_CLASS, 'BasicAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.BasicAttributes', 
                [], [], 
                '''                Attributes
                ''',
                'basic_attributes',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('fan-traies', REFERENCE_CLASS, 'FanTraies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.FanTraies', 
                [], [], 
                '''                Table for rack fan trays
                ''',
                'fan_traies',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-supply-shelfs', REFERENCE_CLASS, 'PowerSupplyShelfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.PowerSupplyShelfs', 
                [], [], 
                '''                Table for rack power supply shelves 
                ''',
                'power_supply_shelfs',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('power-supply-zones', REFERENCE_CLASS, 'PowerSupplyZones' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.PowerSupplyZones', 
                [], [], 
                '''                Table for defining rack power supply zones 
                ''',
                'power_supply_zones',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            _MetaInfoClassMember('slots', REFERENCE_CLASS, 'Slots' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack.Slots', 
                [], [], 
                '''                Slot table contains all slots in the rack
                ''',
                'slots',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'rack',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory.Racks' : {
        'meta_info' : _MetaInfoClass('Inventory.Racks',
            False, 
            [
            _MetaInfoClassMember('rack', REFERENCE_LIST, 'Rack' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks.Rack', 
                [], [], 
                '''                Rack number
                ''',
                'rack',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'racks',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
    'Inventory' : {
        'meta_info' : _MetaInfoClass('Inventory',
            False, 
            [
            _MetaInfoClassMember('racks', REFERENCE_CLASS, 'Racks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper', 'Inventory.Racks', 
                [], [], 
                '''                Table of racks
                ''',
                'racks',
                'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper',
            'inventory',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-invmgr-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_invmgr_admin_oper'
        ),
    },
}
_meta_table['Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes.BasicInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf.BasicAttributes']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf']['meta_info']
_meta_table['Inventory.Racks.Rack.PowerSupplyShelfs.PowerSupplyShelf']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.PowerSupplyShelfs']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.FruInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port.BasicAttributes']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.FruInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes.BasicInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.Port']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot.BasicAttributes']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots.PortSlot']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.FruInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes.BasicInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor.BasicAttributes']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors.Sensor']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo.CardUpTime']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.FruInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes.BasicInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.PortSlots']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.Sensors']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module.BasicAttributes']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo.CardUpTime']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.FruInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes.BasicInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.Module']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot.BasicAttributes']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots.SubSlot']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.FruInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes.BasicInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor.BasicAttributes']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors.Sensor']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo.CardUpTime']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.FruInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes.BasicInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.Sensors']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent.BasicAttributes']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents.HwComponent']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo.CardUpTime']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.FruInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes.BasicInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port.BasicAttributes']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo.CardUpTime']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.FruInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes.BasicInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.Port']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot.BasicAttributes']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots.PortSlot']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo.CardUpTime']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.FruInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes.BasicInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor.BasicAttributes']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors.Sensor']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo.CardUpTime']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.FruInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes.BasicInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.SubSlots']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.HwComponents']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.PortSlots']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.Sensors']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card.BasicAttributes']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards.Card']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.LastOperationalStateChange']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo.CardUpTime']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.BasicAttributes.FruInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.BasicAttributes.BasicInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.Cards']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot.BasicAttributes']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots.Slot']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots.Slot']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.Slots']['meta_info']
_meta_table['Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes.BasicInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.FanTraies.FanTray.BasicAttributes']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.FanTraies.FanTray']['meta_info']
_meta_table['Inventory.Racks.Rack.FanTraies.FanTray']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.FanTraies']['meta_info']
_meta_table['Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes.PowerSupplyGroupInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone.PowerSupplyZoneAttributes']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone']['meta_info']
_meta_table['Inventory.Racks.Rack.PowerSupplyZones.PowerSupplyZone']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.PowerSupplyZones']['meta_info']
_meta_table['Inventory.Racks.Rack.BasicAttributes.BasicInfo']['meta_info'].parent =_meta_table['Inventory.Racks.Rack.BasicAttributes']['meta_info']
_meta_table['Inventory.Racks.Rack.PowerSupplyShelfs']['meta_info'].parent =_meta_table['Inventory.Racks.Rack']['meta_info']
_meta_table['Inventory.Racks.Rack.Slots']['meta_info'].parent =_meta_table['Inventory.Racks.Rack']['meta_info']
_meta_table['Inventory.Racks.Rack.FanTraies']['meta_info'].parent =_meta_table['Inventory.Racks.Rack']['meta_info']
_meta_table['Inventory.Racks.Rack.PowerSupplyZones']['meta_info'].parent =_meta_table['Inventory.Racks.Rack']['meta_info']
_meta_table['Inventory.Racks.Rack.BasicAttributes']['meta_info'].parent =_meta_table['Inventory.Racks.Rack']['meta_info']
_meta_table['Inventory.Racks.Rack']['meta_info'].parent =_meta_table['Inventory.Racks']['meta_info']
_meta_table['Inventory.Racks']['meta_info'].parent =_meta_table['Inventory']['meta_info']
