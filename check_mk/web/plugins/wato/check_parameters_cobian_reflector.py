# Author: Matthias Maderer
# E-Mail: edvler@edvler-blog.de
# URL: https://github.com/edvler/
# License: GPLv2

# for 2.0
#from cmk.gui.i18n import _
#
#from cmk.gui.valuespec import (
#    Dictionary,
#    DropdownChoice,
#    TextAscii,
#    Tuple,
#    Age,
#    Filesize,
#    Integer,
#)
#
#from cmk.gui.plugins.wato import (
#    CheckParameterRulespecWithItem,
#    rulespec_registry,
#    RulespecGroupCheckParametersOperatingSystem,
#)

def _item_valuespec_cobian_reflector():
    return TextAscii(title=_("Taskname"))

def _parameter_valuespec_cobian_reflector():
    return Dictionary(
        elements = [
            ("check_backup",
             DropdownChoice(
                 title = _("Enable (default) or disable check of backup"),
                 help=_("If disabled is choosen, the check will always return OK. To enable checks of the backup, select enable. This is usefull if you have Backup-Jobs, for which no regular backups are done and you dont want them to be
checked."),
                 choices = [
                     ("ignore", _("disable")),
                     ("check", _("enable")),
                 ]
             )
            ),
            ("ignore_vss",
             DropdownChoice(
                 title = _("Ignore VSS errors?"),
                 help=_("If ignore is choosen, the check will return OK instead of change to error if VSS fails. This is usefull if you have Backup-Jobs, which has VSS fails that occur always and you want to ignore them."),
                 choices = [
                     ("ignore", _("ignore")),
                     ("check", _("check vss errors")),
                 ]
             )
            ),
            ("error_check",
             DropdownChoice(
                 title = _("Ignore Job errors?"),
                 help=_("If ignore is choosen, the check will return OK instead of change to warn or crit."),
                 choices = [
                     ("ignore", _("ignore")),
                     ("warn", _("change to warning")),
                     ("crit", _("change to critical")),
                 ]
             )

            ),

            ("file_count_limits",
             Tuple(
                 title = "Change to warn or error if copyied files below given file counts",
                     elements = [
                         Integer(
                                 title = _("Change to warn if Backup-Job copyied less or equal files than"),
                                 help = _("If Backup-Job copyied less or equal files than the given number change to warn."),
                                 minvalue = 0,
                         ),
                         Integer(
                                 title = _("Change to error if Backup-Job copyied less or equal files than"),
                                 help = _("If Backup-Job copyied less or equal files than the given number change to error."),
                                 minvalue = 0,
                         ),
                     ]
                 )
            ),
            ("backup_minsize",
                Tuple(
                    title = _("Minimal backup size"),
                    elements = [
                      Filesize(title = _("Warning if below")),
                      Filesize(title = _("Critical if below")),
                    ]
                )
            ),
            ( "backup_duration",
                Tuple(
                    title = _("Backup duration"),
                    elements = [
                      Age(title = _("Warning if backup is running longer as"),
                         default_value = 18000,
                         help=_("If the backup is longer as the given time the check changes to warn.")
                      ),
                      Age(title = _("Critical if backup is running longer as"),
                         default_value = 21600,
                         help=_("If the backup is longer as the given time the check changes to error.")
                      ),
                    ]
                )
            ),

            ('backup_age',
             Tuple(
                 title = "Age of Backup before changing to warn (default 26h) or error (default 30h).",
                 elements = [
                     Age(title=_("Warning at or above a backupage of"),
                         default_value = 93600,
                         help=_("If the backup is older than the specified time, the check changes to warning. (24h=1440m; 26h=1560m)")
                     ),
                     Age(title=_("Critical at or above a backupage of"),
                         default_value = 108000,
                         help=_("If the backup is older than the specified time, the check changes to critical. (24h=1440m; 26h=1560m)")
                     ),
                 ]
             )
            ),
        ]
    )

register_check_parameters(
    subgroup_os,
    "cobian_ref",
    _("Backup Cobian Reflector"),
    _parameter_valuespec_cobian_reflector(),
    _item_valuespec_cobian_reflector(),
    match_type = "dict"
)

# Prepared for 2.0
#rulespec_registry.register(
#    CheckParameterRulespecWithItem(
#        check_group_name="cobian_ref",
#        group=RulespecGroupCheckParametersApplications,
#        match_type="dict",
#        item_spec=_item_valuespec_cobian_reflector,
#        parameter_valuespec=_parameter_valuespec_cobian_reflector,
#        title=lambda: _("Cobian Reflector Backup"),
#    ))

