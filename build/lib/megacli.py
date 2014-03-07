"""

"""
from subprocess import Popen, PIPE
import json, types, re

MEGACLI='/opt/MegaRAID/MegaCli/MegaCli64'

class Adapter:

    def __init__(self):
        self.device_id = 0
        self.product_name = ''
        self.serial_number = ''
        self.fw_package_build = ''
        self.fw_version = ''
        self.bios_version = ''
        self.webbios_version = ''
        self.preboot_cli_version = ''
        self.boot_block_version = ''
        self.sas_address = ''
        self.bbu_present = False
        self.alarm_present = False
        self.nvram_present = False
        self.serial_debugger_present = False
        self.flash_present = False
        self.memory_size = ''

    def load(self, adapter_id):

        try:
            ret = megacli('-AdpAllInfo -a%i -NoLog' % adapter_id)
        except OSError:
            print 'Failed to get adapter information (MegaCli -AdpAllInfo)'
            return 0

        for line in ret.readlines():
            if line.startswith('Adapter #'):
                self.device_id = int(line[9:].strip())
            if line.startswith('Product Name'):
                offset = line.find(':')
                self.product_name = line[offset+1:].strip()
            elif line.startswith('Serial No'):
                offset = line.find(':')
                self.serial_number = line[offset+1:].strip()
            elif line.startswith('FW Package Build'):
                offset = line.find(':')
                self.fw_package_build = line[offset+1:].strip()
            elif line.startswith('FW Version'):
                offset = line.find(':')
                self.fw_version = line[offset+1:].strip()
            elif line.startswith('BIOS Version'):
                offset = line.find(':')
                self.bios_version = line[offset+1:].strip()
            elif line.startswith('WebBIOS Version'):
                offset = line.find(':')
                self.webbios_version = line[offset+1:].strip()
            elif line.startswith('Preboot CLI Version'):
                offset = line.find(':')
                self.preboot_cli_version = line[offset+1:].strip()
            elif line.startswith('Boot Block Version'):
                offset = line.find(':')
                self.boot_block_version = line[offset+1:].strip()
            elif line.startswith('SAS Address'):
                offset = line.find(':')
                self.sas_address = line[offset+1:].strip()
            elif line.startswith('BBU'):
                offset = line.find(':')
                self.bbu_present = str2bool(line[offset+1:])
            elif line.startswith('Alarm'):
                offset = line.find(':')
                self.alarm_present = str2bool(line[offset+1:])
            elif line.startswith('NVRAM'):
                offset = line.find(':')
                self.nvram_present = str2bool(line[offset+1:])
            elif line.startswith('Serial Debugger'):
                offset = line.find(':')
                self.serial_debugger_present = str2bool(line[offset+1:])
            elif line.startswith('Flash'):
                offset = line.find(':')
                self.flash_present = str2bool(line[offset+1:])
            elif line.startswith('Memory Size'):
                offset = line.find(':')
                self.memory_size = line[offset+1:].strip()

    def json(self):
        return json.dumps(self.__dict__)

    def __getitem__(self, item):
        return self.__dict__[item]


    def __str__(self):
        ret = """Device ID                     : %d
Product Name                  : %s
Serial Number                 : %s
FW Package Build              : %s
FW Version                    : %s
BIOS Version                  : %s
WebBIOS Version               : %s
Preboot CLI Version           : %s
Boot Block Version            : %s
SAS Address                   : %s
BBU Present                   : %s
Alarm Present                 : %s
NVRAM Present                 : %s
Serial Debugger Present       : %s
Flash Present                 : %s
Memory Size                   : %s""" % (self.device_id, self.product_name, \
        self.serial_number, self.fw_package_build, self.fw_version, \
        self.bios_version, self.webbios_version, self.preboot_cli_version, \
        self.boot_block_version, self.sas_address, self.bbu_present, \
        self.alarm_present, self.nvram_present, self.serial_debugger_present, \
        self.flash_present, self.memory_size)

        return ret

class Enclosure:

    def __init__(self):
        self.device_id = 0
        self.adapter_id = 0
        self.number_of_slots = 0
        self.number_of_power_supplies = 0
        self.number_of_fans = 0
        self.number_of_temperature_sensors = 0
        self.number_of_alarms = 0
        self.number_of_sim_modules = 0
        self.number_of_physical_drives = 0
        self.status = ''
        self.position = 0
        self.connector_name = ''
        self.partner_device_id = ''

    def load_from_text(self, input):

        for line in input:
            if line.startswith('    Device ID'):
                offset = line.find(':')
                self.device_id = int(line[offset+1:].strip())
            if line.startswith('    Number of Slots'):
                offset = line.find(':')
                self.number_of_slots = int(line[offset+1:].strip())
            elif line.startswith('    Number of Power Supplies'):
                offset = line.find(':')
                self.number_of_power_supplies = int(line[offset+1:].strip())
            elif line.startswith('    Number of Fans'):
                offset = line.find(':')
                self.number_of_fans = int(line[offset+1:].strip())
            elif line.startswith('    Number of Temperature Sensors'):
                offset = line.find(':')
                self.number_of_temperature_sensors = int(line[offset+1:].strip())
            elif line.startswith('    Number of Alarms'):
                offset = line.find(':')
                self.number_of_alarms = int(line[offset+1:].strip())
            elif line.startswith('    Number of SIM Modules'):
                offset = line.find(':')
                self.number_of_sim_modules = int(line[offset+1:].strip())
            elif line.startswith('    Number of Physical Drives'):
                offset = line.find(':')
                self.number_of_physical_drives = int(line[offset+1:].strip())
            elif line.startswith('    Status'):
                offset = line.find(':')
                self.status = line[offset+1:].strip()
            elif line.startswith('    Position'):
                offset = line.find(':')
                self.position = line[offset+1:].strip()
            elif line.startswith('    Connector Name'):
                offset = line.find(':')
                self.connector_name = line[offset+1:].strip()
            elif line.startswith('    Partner Device Id'):
                offset = line.find(':')
                self.partner_device_id = line[offset+1:].strip()

    def json(self):
        return json.dumps(self.__dict__)

    def __getitem__(self, item):
        return self.__dict__[item]

    def __str__(self):
        ret = """Device ID                     : %i
Number of Slots               : %i
Number of Power Supplies      : %i
Number of Fans                : %i
Number of Temperature Sensors : %i
Number of Alarms              : %i
Number of SIM Modules         : %i
Number of Physical Drives     : %i
Status                        : %s
Position                      : %s
Connector Name                : %s
Partner Device Id             : %s""" % (self.device_id, self.number_of_slots, \
        self.number_of_power_supplies, self.number_of_fans, \
        self.number_of_temperature_sensors, self.number_of_alarms, \
        self.number_of_sim_modules, self.number_of_physical_drives, \
        self.status, self.position, self.connector_name, self.partner_device_id)

        return ret


class PhysicalDevice:

    def __init__(self):
        self.adapter_id = 0
        self.enclosure_id = 0
        self.slot_id = 0
        self.device_id = 0
        self.sequence_number = 0
        self.media_errors = 0
        self.other_errors = 0
        self.predictive_failures = 0
        self.last_predictive_seq_number = 0
        self.pd_type = ''
        self.raw_size = ''
        self.non_coerced_size = ''
        self.coerced_size = ''
        self.firmware_state = ''
        self.sas_address = ''
        self.connected_port_number = ''
        self.inquiry_data = ''
        self.fde_capable = ''
        self.fde_enable = ''
        self.secured = ''
        self.locked = ''
        self.foreign_state = ''
        self.device_speed = ''
        self.link_speed = ''
        self.media_type = ''

    def led_on(self):
        try:
            ret = megacli('-PdLocate -Start -PhysDrv[%i:%i] -a%i'
                % (self.enclosure_id, self.slot_id, self.adapter_id))
        except OSError:
            print 'Failed to turn location LED on (MegaCli -PdLocate -Start)'
            return False
        return True


    def led_off(self):
        try:
            ret = megacli('-PdLocate -Stop -PhysDrv[%i:%i] -a%i'
                % (self.enclosure_id, self.slot_id, self.adapter_id))
        except OSError:
            print 'Failed to turn location LED on (MegaCli -PdLocate -Stop)'
            return False
        return True


    def is_configured(self):
        if 'Unconfigured' in self.firmware_state and 'good' in self.firmware_state:
            return True
        else:
            return False

    def make_JBOD(self):
        """ Makes drive JBOD Just a Bunch Of Disks"""
        args = '-PDMakeJBOD -PhysDrv[%i:%i] -a%i' % (self.enclosure_id, self.slot_id, self.adapter_id)
        megacli(args)
        self.reload()

    def set_offline(self):
        """ Set firmware state to Offline """
        args = '-PDOffline -PhysDrv [%i:%i] -a%i' % (self.enclosure_id, self.slot_id, self.adapter_id)
        megacli(args)
        self.reload()

    def set_online(self):
        """ Set firmware state to Online """
        args = '-PDOnline -PhysDrv [%i:%i] -a%i' % (self.enclosure_id, self.slot_id, self.adapter_id)
        megacli(args)
        self.reload()

    def mark_missing(self):
        """ Mark drive as missing """
        args = '-PDMarkMissing -PhysDrv [%i:%i] -a%i' % (self.enclosure_id, self.slot_id, self.adapter_id)
        megacli(args)
        self.reload()

    def prepare_for_removal(self):
        """ Prepare drive for removal """
        args = '-PdPrpRmv -PhysDrv [%i:%i] -a%i' % (self.enclosure_id, self.slot_id, self.adapter_id)
        megacli(args)
        self.reload()

    def bad_to_good(self):
        """ Changes drive in state Unconfigured-Bad to Unconfigured-Good. """
        args = '-PDMakeGood -PhysDrv[%i:%i] -a%i' % (self.enclosure_id, self.slot_id, self.adapter_id)
        megacli(args)
        self.reload()

    def set_global_hot_spare(self):
        """ Set drive as global hot spare """
        args = '-PDHSP -Set -PhysDrv [%i:%i] -a%i' % (self.enclosure_id, self.slot_id, self.adapter_id)
        megacli(args)
        self.reload()

    def remove_global_hot_spare(self):
        """ Unset drive as global hot spare """
        args = '-PDHSP -Rmv -PhysDrv [%i:%i] -a%i' % (self.enclosure_id, self.slot_id, self.adapter_id)
        megacli(args)
        self.reload()

    def auto_remove(self):
        """ This method calls all the other necessary methods in order to
        prepare a drive for replacement
        """
        self.set_offline()
        self.mark_missing()
        self.prepare_for_removal()
        self.reload()

    def load_from_text(self, input):
        for line in input:
            if line.startswith('Enclosure Device ID'):
                offset = line.find(':')
                self.enclosure_id = int(line[offset+1:].strip())
            if line.startswith('Slot Number'):
                offset = line.find(':')
                self.slot_id = int(line[offset+1:].strip())
            elif line.startswith('Device Id'):
                offset = line.find(':')
                self.device_id = int(line[offset+1:].strip())
            elif line.startswith('Sequence Number'):
                offset = line.find(':')
                self.sequence_number = int(line[offset+1:].strip())
            elif line.startswith('Media Error Count'):
                offset = line.find(':')
                self.media_errors = int(line[offset+1:].strip())
            elif line.startswith('Other Error Count'):
                offset = line.find(':')
                self.other_errors = int(line[offset+1:].strip())
            elif line.startswith('Predictive Failure Count'):
                offset = line.find(':')
                self.predictive_failures = int(line[offset+1:].strip())
            elif line.startswith('Last Predictive Failure Event Seq Number'):
                offset = line.find(':')
                self.last_predictive_seq_number = int(line[offset+1:].strip())
            elif line.startswith('PD Type'):
                offset = line.find(':')
                self.pd_type = line[offset+1:].strip()
            elif line.startswith('Raw Size'):
                offset = line.find(':')
                delim = line.find('[') - 4
                self.raw_size = float(line[offset+1:delim].strip())
            elif line.startswith('Non Coerced Size'):
                offset = line.find(':')
                delim = line.find('[') - 4
                self.non_coerced_size = float(line[offset+1:delim].strip())
            elif line.startswith('Coerced Size'):
                offset = line.find(':')
                delim = line.find('[') - 4
                self.coerced_size = float(line[offset+1:delim].strip())
            elif line.startswith('Firmware state'):
                offset = line.find(':')
                self.firmware_state = line[offset+1:].strip()
            elif line.startswith('SAS Address'):
                offset = line.find(':')
                self.sas_address = line[offset+1:].strip()
            elif line.startswith('Connected Port Number'):
                offset = line.find(':')
                self.connected_port_number = line[offset+1:].strip()
            elif line.startswith('Inquiry Data'):
                offset = line.find(':')
                self.inquiry_data = line[offset+1:].strip()
            elif line.startswith('FDE Capable'):
                offset = line.find(':')
                self.fde_capable = line[offset+1:].strip()
            elif line.startswith('FDE Enable'):
                offset = line.find(':')
                self.fde_enable = line[offset+1:].strip()
            elif line.startswith('Secured'):
                offset = line.find(':')
                self.secured = line[offset+1:].strip()
            elif line.startswith('Locked'):
                offset = line.find(':')
                self.locked = line[offset+1:].strip()
            elif line.startswith('Foreign State'):
                offset = line.find(':')
                self.foreign_state = line[offset+1:].strip()
            elif line.startswith('Device Speed'):
                offset = line.find(':')
                self.device_speed = line[offset+1:].strip()
            elif line.startswith('Link Speed'):
                offset = line.find(':')
                self.link_speed = line[offset+1:].strip()
            elif line.startswith('Media Type'):
                offset = line.find(':')
                self.media_type = line[offset+1:].strip()

    def reload(self):

        try:
            ret = megacli('-PdInfo -PhysDrv[%i:%i] -a%i' % (self.enclosure_id, \
                    self.slot_id, self.adapter_id))
        except OSError:
            print 'Failed to get physical device information (MegaCli -PdInfo \
                    -PhysDrv[%i:%i] -a%i)' % (self.enclosure_id, self.slot_id, \
                    self.adapter_id)
            return []

        #self.adapter_id = adapter_id
        ret_lines = ret.readlines()
        self.load_from_text(ret_lines)

    def json(self):
        return json.dumps(self.__dict__)

    def __getitem__(self, item):
        return self.__dict__[item]

    def __str__(self):
        ret = """Adapter ID: %s
Enclosure Device ID: %s
Slot Number: %s
Device Id: %s
Sequence Number: %s
Media Error Count: %s
Other Error Count: %s
Predictive Failure Count: %s
Last Predictive Failure Event Seq Number: %s
PD Type: %s
Raw Size: %s
Non Coerced Size: %s
Coerced Size: %s
Firmware state: %s
SAS Address(0): %s
Connected Port Number: %s
Inquiry Data: %s
FDE Capable: %s
FDE Enable: %s
Secured: %s
Locked: %s
Foreign State: %s
Device Speed: %s
Link Speed: %s
Media Type: %s""" % (self.adapter_id, self.enclosure_id, self.slot_id, self.device_id, \
        self.sequence_number, self.media_errors, self.other_errors, \
        self.predictive_failures, \
        self.last_predictive_seq_number, \
        self.pd_type, self.raw_size, self.non_coerced_size, \
        self.coerced_size, \
        self.firmware_state, self.sas_address, self.connected_port_number, \
        self.inquiry_data, self.fde_capable, self.fde_enable, \
        self.secured, self.locked, self.foreign_state, self.device_speed, \
        self.link_speed, self.media_type)

        return ret


class VirtualDrive:

    def __init__(self):
        self.virtualdisk_id = 0
        self.adapter_id = 0
        self.name = ''
        self.raid_level = ''
        self.size = ''
        self.state = ''
        self.stripe_size = ''
        self.number_of_drives = 0
        self.span_depth = 0
        self.default_cache_policy = ''
        self.current_cache_policy = ''
        self.access_policy = ''
        self.disk_cache_policy = ''
        self.encryption = ''

    def convert_raid_level(self, raid_level):
        if raid_level in [0,1,5]:
            args = '-LDRecon -Start -r%i -L%i -a%i' % (raid_level, self.virtualdisk_id, self.adapter_id)
        else:
            raise NotImplemented('RAID %i is not yet implemented. Currently supported raid levels are 0,1,5' % raid_level)
        megacli(args)
        self.reload()

    def set_wb(self):
        args = '-LDSetProp WB -L%i -a%i -NoLog' % (self.virtualdisk_id, self.adapter_id)
        megacli(args)
        self.reload()

    def setNoCacheBadBBU(self):
        args = '-LDSetProp NoCacheBadBBU -L%i -a%i' % (self.virtualdisk_id, self.adapter_id)
        megacli(args)
        self.reload()

    def destroy(self):
        args = '-CfgLdDel -L%i -a%i' % (self.virtualdisk_id, self.adapter_id)
        megacli(args)
        self.reload()

    def view_rebuild_progress(self):
        args = '-LDRecon ShowProg L%i -a%i' % (self.virtualdisk_id, self.adapter_id)
        megacli(args)
        self.reload()

    def extend(self, drives):
        if not type(drives) == types.ListType:
            raise TypeError("drives must be in list format ['E:S', 'E:S', '...']")
        _raid_level = decode_raid_level(self.raid_level)
        drive_syntax = re.compile(r'^[0-9]+:[0-9]+$')
        for drive in drives:
            if not re.match(drive_syntax, drive):
                raise AttributeError('Invalid drive format. E:S required')
            _enclosure = drive.split(':')[0]
            _slot = drive.split(':')[-1]
            for p in pd_list(self.adapter_id):
                if _enclosure == p.enclosure_id and _slot == p.slot_id and p.firmware_state.startswith('Unconfigured'):
                    break
                raise DriveError('Drive %s is either already in use or does not exist' % drive)
        args = '-LDRecon -Start -r%i -Add -PhysDrv[%s] -L%i -a%i' % (_raid_level, ','.join(drives), self.virtualdisk_id, self.adapter_id)
        megacli(args)
        self.reload()


    def load_from_text(self, input):

        for line in input:
            if line.startswith('Virtual Drive'):
                delim = line.find('(')
                offset = line.find(':')
                self.virtualdisk_id = int(line[offset+1:delim].strip())
            if line.startswith('Name'):
                offset = line.find(':')
                self.name = line[offset+1:].strip()
            elif line.startswith('RAID Level'):
                offset = line.find(':')
                self.raid_level = line[offset+1:].strip()
            elif line.startswith('Size'):
                delim = line.find(' GB')
                offset = line.find(':')
                self.size = line[offset+1:delim].strip()
            elif line.startswith('State'):
                offset = line.find(':')
                self.state = line[offset+1:].strip()
            elif line.startswith('Strip Size'):
                delim = line.find(' KB')
                offset = line.find(':')
                self.stripe_size = line[offset+1:delim].strip()
            elif line.startswith('Number Of Drives'):
                offset = line.find(':')
                self.number_of_drives = int(line[offset+1:].strip())
            elif line.startswith('Span Depth'):
                offset = line.find(':')
                self.span_depth = int(line[offset+1:].strip())
            elif line.startswith('Default Cache Policy'):
                offset = line.find(':')
                self.default_cache_policy = line[offset+1:].strip()
            elif line.startswith('Current Cache Policy'):
                offset = line.find(':')
                self.current_cache_policy = line[offset+1:].strip()
            elif line.startswith('Current Access Policy'):
                offset = line.find(':')
                self.access_policy = line[offset+1:].strip()
            elif line.startswith('Disk Cache Policy'):
                offset = line.find(':')
                self.disk_cache_policy = line[offset+1:].strip()
            elif line.startswith('Encryption'):
                offset = line.find(':')
                self.encryption = line[offset+1:].strip()


    def reload(self):

        try:
            ret = megacli('-LdInfo -L%i -a%i' % (self.virtualdisk_id, self.adapter_id))
        except OSError:
            print 'Failed to get Virtual Drive information (MegaCli -LdInfo -L%i -a%i' % (self.virtualdisk_id, self.adapter_id)
            return []

        #self.adapter_id = adapter_id
        ret_lines = ret.readlines()
        self.load_from_text(ret_lines)

    def json(self):
        return json.dumps(self.__dict__)

    def __getitem__(self, item):
        return self.__dict__[item]

    def __str__(self):
        ret = """Virtual Drive: %d
Name: %s
RAID Level: %s
Size: %s
State: %s
Strip Size: %s
Number Of Drives: %d
Span Depth: %d
Default Cache Policy: %s
Current Cache Policy: %s
Access Policy: %s
Disk Cache Policy: %s
Encryption: %s""" % (self.virtualdisk_id, self.name, self.raid_level, \
    self.size, self.state, self.stripe_size, self.number_of_drives, \
    self.span_depth, self.default_cache_policy, self.current_cache_policy, \
    self.access_policy, self.disk_cache_policy, self.encryption)

        return ret


class BBU():

    def __init__(self):
        self.battery_type = ''
        self.voltage = ''
        self.current = ''
        self.temperature = ''
        self.state = ''
        self.charging_status = ''
        self.voltage_status = ''
        self.learn_cycle_requested = False
        self.learn_cycle_active = False
        self.learn_cycle_status = ''
        self.learn_cycle_timeout = False
        self.i2c_errors_detected = False
        self.battery_pack_missing = False
        self.battery_replacement_required = False
        self.remaining_capacity_low = False
        self.periodic_learn_required = False
        self.transparent_learn = False
        self.about_to_fail = False
        self.microcode_update_required = False
        self.gas_gauge_status = ''
        self.relative_charge = ''
        self.charger_system_state = 0
        self.charger_system_ctrl = 0
        self.charging_current = ''
        self.absolute_charge = ''
        self.max_error = ''

    def load_from_text(self, input):

        for line in input:
            if line.startswith('BatteryType'):
                offset = line.find(':')
                self.battery_type = line[offset+1:].strip()
            if line.startswith('Voltage:'):
                offset = line.find(':')
                self.voltage = line[offset+1:].strip()
            elif line.startswith('Current:'):
                offset = line.find(':')
                self.current = line[offset+1:].strip()
            elif line.startswith('Temperature'):
                offset = line.find(':')
                self.temperature = line[offset+1:].strip()
            elif line.startswith('Battery State'):
                offset = line.find(':')
                self.state = line[offset+1:].strip()
            elif line.startswith('  Charging Status'):
                offset = line.find(':')
                self.charging_status = line[offset+1:].strip()
            elif line.startswith('  Voltage'):
                offset = line.find(':')
                self.voltage_status = line[offset+1:].strip()
            elif line.startswith('  Learn Cycle Requested'):
                offset = line.find(':')
                self.learn_cycle_requested = str2bool(line[offset+1:].strip())
            elif line.startswith('  Learn Cycle Active'):
                offset = line.find(':')
                self.learn_cycle_active = str2bool(line[offset+1:].strip())
            elif line.startswith('  Learn Cycle Status'):
                offset = line.find(':')
                self.learn_cycle_status = line[offset+1:].strip()
            elif line.startswith('  Learn Cycle Timeout'):
                offset = line.find(':')
                self.learn_cycle_timeout = str2bool(line[offset+1:].strip())
            elif line.startswith('  I2c Errors Detected'):
                offset = line.find(':')
                self.i2c_errors_detected = str2bool(line[offset+1:].strip())
            elif line.startswith('  Battery Pack Missing'):
                offset = line.find(':')
                self.battery_pack_missing = str2bool(line[offset+1:].strip())
            elif line.startswith('  Battery Replacement required'):
                offset = line.find(':')
                self.battery_replacement_required = str2bool(line[offset+1:].strip())
            elif line.startswith('  Remaining Capacity Low'):
                offset = line.find(':')
                self.remaining_capacity_low = str2bool(line[offset+1:].strip())
            elif line.startswith('  Periodic Learn Required'):
                offset = line.find(':')
                self.periodic_learn_required = str2bool(line[offset+1:].strip())
            elif line.startswith('  Transparent Learn'):
                offset = line.find(':')
                self.transparent_learn = str2bool(line[offset+1:].strip())
            elif line.startswith('  Pack is about to fail'):
                offset = line.find(':')
                self.about_to_fail = str2bool(line[offset+1:].strip())
            elif line.startswith('  Module microcode update required'):
                offset = line.find(':')
                self.microcode_update_required = str2bool(line[offset+1:].strip())
            elif line.startswith('BBU GasGauge Status'):
                offset = line.find(':')
                self.gas_gauge_status = line[offset+1:].strip()
            elif line.startswith('  Relative State of Charge'):
                offset = line.find(':')
                self.relative_charge = line[offset+1:].strip()
            elif line.startswith('  Charger System State'):
                offset = line.find(':')
                self.charger_system_state = int(line[offset+1:].strip())
            elif line.startswith('  Charger System Ctrl'):
                offset = line.find(':')
                self.charger_system_ctrl = int(line[offset+1:].strip())
            elif line.startswith('  Charging current'):
                offset = line.find(':')
                self.charging_current = line[offset+1:].strip()
            elif line.startswith('  Absolute state of charge'):
                offset = line.find(':')
                self.absolute_charge = line[offset+1:].strip()
            elif line.startswith('  Max Error'):
                offset = line.find(':')
                self.max_error = line[offset+1:].strip()

    def reload(self):

        try:
            ret = megacli('-AdpBbuCmd -GetBbuStatus -a%i' % self.adapter_id)
        except OSError:
            print 'Failed to get BBU information (MegaCli --AdpBbuCmd -GetBbuStatus -a%i)' % self.adapter_id
            return []

        #self.adapter_id = adapter_id
        ret_lines = ret.readlines()
        self.load_from_text(ret_lines)

    def json(self):
        return json.dumps(self.__dict__)

    def __getitem__(self, item):
        return self.__dict__[item]

    def __str__(self):
        ret = """Battery Type:                 %s
Voltage:                      %s
Current:                      %s
Temperature:                  %s
State:                        %s
Charging Status:              %s
Voltage status:               %s
Learn Cycle Requested:        %s
Learn Cycle Active:           %s
Learn Cycle Status:           %s
Learn Cycle Timeout:          %s
I2C Errors Detected:          %s
Battery Pack Missing:         %s
Battery Replacement Required: %s
Remaining Capacity Low:       %s
Periodic Learn Required:      %s
Transparent Learn:            %s
About to Fail:                %s
Microcode Update Required:    %s
Gas Gauge Status:             %s
Relative Charge:              %s
Charger State:                %s
Charger Ctrl:                 %s
Charge Current:               %s
Absolute Charge:              %s
Max Error:                    %s
""" % (self.battery_type, self.voltage, self.current, \
    self.temperature, self.state, self.charging_status, self.voltage_status, \
    self.learn_cycle_requested, self.learn_cycle_active, self.learn_cycle_status, \
    self.learn_cycle_timeout, self.i2c_errors_detected, self.battery_pack_missing, \
    self.battery_replacement_required, self.remaining_capacity_low, \
    self.periodic_learn_required, self.transparent_learn, self.about_to_fail, \
    self.microcode_update_required, self.gas_gauge_status, self.relative_charge, \
    self.charger_system_state, self.charger_system_ctrl, self.charging_current, \
    self.absolute_charge, self.max_error)

        return ret


def adp_list():

    try:
        ret = megacli('-AdpCount -NoLog')
    except OSError:
        print 'Failed to get adapter count (MegaCli -AdpCount)'
        return []

    adp_count = 0

    for line in ret.readlines():
        if line.startswith('Controller Count'):
            offset = line.find(':')
            adp_count = int(line[offset+1:].replace('.','').strip())

    adp_list = []
    adp = Adapter()

    for adp_id in range(0, adp_count):
                adp.load(adp_id)
                adp_list.append(adp)
                adp = Adapter()

    return adp_list


def enc_list(adapter_id):

    try:
        ret = megacli('-EncInfo -a%i' % adapter_id)
    except OSError:
        print 'Failed to get enclosure information (MegaCli -EncInfo)'
        return []

    ret_lines = ret.readlines()

    enc_list = []
    enc = Enclosure()
    enc.adapter_id = adapter_id

    # Go through all lines looking for the Enclosure identifier line
    start_matcher = re.compile(r'.*Enclosure\ [0-9]+:.*')
    for line in range(0, len(ret_lines)):
        if re.match(start_matcher, ret_lines[line]):
            # Feed the enclosure's block of text to the Enclosure instance
            enc.load_from_text(ret_lines[line:line+23])

            # Add Enclosure to the enc_list and create new instance
            enc_list.append(enc)
            enc = Enclosure()
            enc.adapter_id = adapter_id

    return enc_list


def pd_list(adapter_id):

    try:
        ret = megacli('-PdList -a%i' % adapter_id)
    except OSError:
        print 'Failed to get physical device information (MegaCli -PdList)'
        return []

    ret_lines = ret.readlines()

    pd_list = []
    pd = PhysicalDevice()
    pd.adapter_id = adapter_id

    # Go through all lines looking for the first line in the disk info
    for line in range(0, len(ret_lines)):
        if ret_lines[line].startswith('Enclosure Device ID'):

            # Feed disk info to the PhysicalDevice object
            pd.load_from_text(ret_lines[line:line+46])

            # Add PhysicalDevice to the pd_list and reset it
            pd_list.append(pd)
            pd = PhysicalDevice()
            pd.adapter_id = adapter_id

    return pd_list


def vd_list(adapter_id):

    try:
        ret = megacli('-LdInfo -Lall -a%i' % adapter_id)
    except OSError:
        print 'Failed to get virtual drive information (MegaCli -LDInfo -Lall)'
        return []

    ret_lines = ret.readlines()

    vd_list = []
    vd = VirtualDrive()
    vd.adapter_id = adapter_id

    # Go through all lines looking for the Virtual Drive line
    for line in range(0, len(ret_lines)):
        if ret_lines[line].startswith('Virtual Drive'):

            # Feed the virtual drive's block of text to the VirtualDrive object
            vd.load_from_text(ret_lines[line:line+15])

            # Add VirtualDrive to the vd_list and create a new one
            vd_list.append(vd)
            vd = VirtualDrive()
            vd.adapter_id = adapter_id

    return vd_list


def bbu_list(adapter_id):

    try:
        ret = megacli('-AdpBbuCmd -GetBbuStatus -a%i' % adapter_id)
    except OSError:
        print 'Failed to retrieve BBU information (MegaCli64 -AdpBbuCmd -GetBbuStatus -a%i)' % adapter_id
        return []

    ret_lines = ret.readlines()
    bbu_list = []
    bbu = BBU()
    bbu.adapter_id = adapter_id
    bbu.load_from_text(ret_lines)
    bbu_list.append(bbu)
    return bbu_list


def createvd(raid_level, drives, adapter):
    if not type(drives) == types.ListType:
        raise TypeError("drives must be in list format ['E:S', 'E:S', '...']")
    if not adapter in [a.device_id for a in adp_list()]:
        raise AttributeError('Invalid adapter: %s does not exist' % adapter)
    drive_syntax = re.compile(r'^[0-9]+:[0-9]+$')
    for drive in drives:
        if not re.match(drive_syntax, drive):
            raise AttributeError('Invalid drive format. E:S required')
        _enclosure = drive.split(':')[0]
        _slot = drive.split(':')[-1]
        for p in pd_list(adapter):
            if _enclosure == p.enclosure_id and _slot == p.slot_id and p.firmware_state.startswith('Unconfigured'):
                break
            raise DriveError('Drive %s is either already in use or does not exist' % drive)
    if raid_level in [0,1,5]:
        args = '-CfgLdAdd -r%i [%s] -a%i' % (raid_level, ','.join(drives), adapter)
    else:
        print 'try manually running: MegaCli64 -CfgSpanAdd -r%i -Array0[E:S,E:S] -Array1[E:S,E:S] -a%i' % (self.raid_level, self.adapter_id)
        raise NotImplemented('RAID %i is not yet implemented. Currently supported raid levels are 0,1,5' % raid_level)
    megacli(args)

def pd_list_unconfigured(drives=None):
    if drives:
        if not type(drives) == types.ListType:
            raise TypeError('pd_list_unconfigured  method requires argument in form of list of PhysicalDevice instances')
        for drive in drives:
            if not type(drive) == types.InstanceType:
                raise TypeError('pd_list_unconfigured  method requires argument in form of list of PhysicalDevice instances')
    else:
        drives = [ x for x in pd_list(i) for i in range(0, len(adp_list())) ]
    # returns in form of ['E:S', '...']
    unconfigured = [ '%i:%i' % (p.enclosure_id, p.slot_id) for p in drives if p.is_unconfigured () ]
    # returns in form of [PhysicalDevice instance, ...]
    #unconfigured  = [ p for p in drives if p.is_unconfigured () ]
    return unconfigured

def pd_list_configured():
    drives = [ x for x in pd_list(i) for i in range(0, len(adp_list())) ]
    configured = [ '%i:%i' % (p.enclosure_id, p.slot_id) for p in drives if not p.is_configured() ]
    return configured

def str2bool(str):
    if str.strip() in ['Present', 'OK', 'Yes']:
        return True
    else:
        return False

def megacli(args):
    cmd = MEGACLI + ' ' + args
    out = Popen(cmd, shell=True, stdout=PIPE).stdout
    return out

def decode_raid_level(description):
    raid_map = {
            'Primary-0, Secondary-0, RAID Level Qualifier-0': 0,
            'Primary-1, Secondary-0, RAID Level Qualifier-0': 1,
            'Primary-5, Secondary-0, RAID Level Qualifier-3': 5,
            'Primary-6, Secondary-0, RAID Level Qualifier-3': 6,
            'Primary-1, Secondary-3, RAID Level Qualifier-0': 10,
            0: 'Primary-0, Secondary-0, RAID Level Qualifier-0',
            1: 'Primary-1, Secondary-0, RAID Level Qualifier-0',
            5: 'Primary-5, Secondary-0, RAID Level Qualifier-3',
            6: 'Primary-6, Secondary-0, RAID Level Qualifier-3',
            10: 'Primary-1, Secondary-3, RAID Level Qualifier-0'
            }
    return raid_map[description]


class DriveError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


class NotImplemented(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


