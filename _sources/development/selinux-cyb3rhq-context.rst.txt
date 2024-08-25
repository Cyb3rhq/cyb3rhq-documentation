.. Copyright (C) 2015, Cyb3rhq, Inc.

.. meta::
   :description: Learn how to use Security-Enhanced Linux (SELinux) with Cyb3rhq to define access controls for the applications, processes, and files on a system.

.. _selinux-cyb3rhq-context:

SELinux Cyb3rhq context
======================

Security-Enhanced Linux (SELinux) defines access controls for the applications, processes, and files on a system.

SELinux is based on "security contexts", assigning one to every element under supervision and a policy that defines what access and operations are allowed. The default SELinux behavior is context inheritance, so if there is no SELinux policy specifying otherwise, every process created will inherit the context of its parent.

That said, as Cyb3rhq does not have a defined context, it inherits the context from ``systemd`` which is in charge of starting the service. This context is of type ``unconfined_t``, which means that it is not under any security restriction, so only the standard Linux DAC restrictions will be applied to it.


- `Create Cyb3rhq context`_
- `Create custom SELinux module`_
- `Troubleshooting`_


Create Cyb3rhq context
--------------------

In case of having the need to run Cyb3rhq as a confined process, we propose to create a new SELinux policy module which allows the transition to a Cyb3rhq context which we will call ``cyb3rhq_t``. Besides, we will create a set of rules assigning the necessary permissions to run.

.. note::

    For the following example we used the Cyb3rhq OVA image based on centOS 7 and the default Cyb3rhq configuration. In case of an upgrade, rules will probably have to be updated according to Cyb3rhq's new functionalities.


.. _SELinux-module-example:

SELinux module example to confine Cyb3rhq
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To create a new module that allows Cyb3rhq to transition to the new context we need the following files:


Cyb3rhq manager
*************

cyb3rhqT.fc
"""""""""

.. raw:: html

  <div class="accordion-section">

.. code-block:: bash

     /var/ossec/active-response                  gen_context(system_u:object_r:cyb3rhq_var_t,s0)
     /var/ossec/active-response/bin(/.*)?        gen_context(system_u:object_r:cyb3rhq_exec_t,s0)
     /var/ossec/agentless(/.*)?                  gen_context(system_u:object_r:cyb3rhq_exec_t,s0)
     /var/ossec/api                              gen_context(system_u:object_r:cyb3rhq_var_t,s0)
     /var/ossec/api/configuration(/.*)?          gen_context(system_u:object_r:cyb3rhq_etc_t,s0)
     /var/ossec/api/scripts(/.*)?                gen_context(system_u:object_r:cyb3rhq_exec_t,s0)
     /var/ossec/backup(/.*)?                     gen_context(system_u:object_r:cyb3rhq_var_t,s0)
     /var/ossec/bin(/.*)?                        gen_context(system_u:object_r:cyb3rhq_exec_t,s0)
     /var/ossec/etc(/.*)?                        gen_context(system_u:object_r:cyb3rhq_etc_t,s0)
     /var/ossec/framework(/.*)?                  gen_context(system_u:object_r:cyb3rhq_exec_t,s0)
     /var/ossec/integrations(/.*)?               gen_context(system_u:object_r:cyb3rhq_exec_t,s0)
     /var/ossec/lib(/.*)?                        gen_context(system_u:object_r:cyb3rhq_lib_t,s0)
     /var/ossec/logs(/.*)?                       gen_context(system_u:object_r:cyb3rhq_log_t,s0)
     /var/ossec/queue(/.*)?                      gen_context(system_u:object_r:cyb3rhq_var_t,s0)
     /var/ossec/ruleset(/.*)?                    gen_context(system_u:object_r:cyb3rhq_var_t,s0)
     /var/ossec/stats(/.*)?                      gen_context(system_u:object_r:cyb3rhq_var_t,s0)
     /var/ossec/tmp(/.*)?                        gen_context(system_u:object_r:cyb3rhq_tmp_t,s0)
     /var/ossec/var(/.*)?                        gen_context(system_u:object_r:cyb3rhq_var_t,s0)
     /var/ossec/wodles(/.*)?                     gen_context(system_u:object_r:cyb3rhq_exec_t,s0)


cyb3rhqT.te
"""""""""

.. raw:: html

  <div class="accordion-section">
           

.. code-block:: bash

    policy_module(cyb3rhqT,1.0)

    require {
    type bin_t;
    type tmp_t;
    type unconfined_t;
    type initrc_t;
    type unconfined_service_t;
    type shell_exec_t;
    type var_t;
    type cert_t;
    type node_t;
    type init_t;
    type kernel_t;
    type system_dbusd_t;
    type sshd_t;
    type fs_t;
    type unlabeled_t;
    type sysctl_net_t;
    type systemd_unit_file_t;
    type cgroup_t;
    type hugetlbfs_t;
    type sysfs_t;
    type iptables_exec_t;
    type sshd_exec_t;
    type device_t;
    type fixed_disk_device_t;
    type useradd_exec_t;
    type journalctl_exec_t;
    type proc_net_t;
    type pstore_t;
    type mount_exec_t;
    type insmod_exec_t;
    type systemd_systemctl_exec_t;
    type crontab_exec_t;
    type devlog_t;
    type rpm_exec_t;
    type proc_t;
    type configfs_t;
    type http_port_t;
    type tmpfs_t;
    type gssproxy_var_lib_t;
    type rpm_log_t;
    type auditd_unit_file_t;
    type crond_unit_file_t;
    type mount_var_run_t;
    type rpm_var_lib_t;
    type usermodehelper_t;
    type var_run_t;
    type etc_t;
    type security_t;
    type firewalld_t;
    type iptables_t;
    type dhcpc_t;
    role system_r;
    role unconfined_r;
    class process { transition getattr getpgid getsession setrlimit setsched signull open read};
    class rawip_socket {bind setopt getopt create open};
    class netlink_route_socket {bind setopt create open write read nlmsg_read};
    class netlink_audit_socket {bind setopt create open write read nlmsg_read};
    class lnk_file {getattr open read};
    class file { getattr open read execute getattr read};
    class dir { getattr open read search };
    class tcp_socket { bind connect create getopt listen name_bind name_connect node_bind setopt };
    class capability { chown dac_override fowner fsetid kill net_bind_service net_raw setgid setuid sys_chroot sys_resource sys_ptrace};
    class unix_dgram_socket { read write create ioctl sendto bind getopt connect};
    class netlink_tcpdiag_socket {create getattr setopt read bind nlmsg_read write};
    class filesystem { getattr open read };
    class sock_file { getattr open read };
    class blk_file { getattr open read };
    class udp_socket name_bind;
    class unix_stream_socket {connectto ioctl getattr};
    class dbus send_msg;
    }

    # Private type declarations
    type cyb3rhq_t;
    type cyb3rhq_exec_t;
    type cyb3rhq_etc_t;
    type cyb3rhq_lib_t;
    type cyb3rhq_log_t;
    type cyb3rhq_tmp_t;
    type cyb3rhq_var_t;

    # Ports label
    type cyb3rhq_port_t;
    corenet_port(cyb3rhq_port_t)

    # domain_type macro specifies the type cyb3rhq_t to be a domain
    domain_type(cyb3rhq_t)

    # domain_entry_file specifies an entry point to the cyb3rhq_t domain for the executable file of type cyb3rhq_exec_t
    domain_entry_file(cyb3rhq_t, cyb3rhq_exec_t)

    # logging_log_file macro makes cyb3rhq_log_t become the type of log file with the necessary groups and rules
    logging_log_file(cyb3rhq_log_t)

    # Allow domain cyb3rhq_t to manipulate log files
    allow cyb3rhq_t cyb3rhq_log_t:file append_file_perms;

    # files_tmp_file takes the type of cyb3rhq_tmp_t to the necessary groups so that it becomes the type of tmp file
    files_tmp_file(cyb3rhq_tmp_t)

    # Allow the cyb3rhq_t domain write privileges into the tmp_t labeled directory, but with an automatic file transition towards cyb3rhq_tmp_t for every file written
    files_tmp_filetrans(cyb3rhq_t,cyb3rhq_tmp_t,file)

    # Allow domain cyb3rhq_t to manipulate tmp files
    allow cyb3rhq_t cyb3rhq_tmp_t:file manage_file_perms;

    #============== Allow transition
    role unconfined_r types cyb3rhq_t;
    role system_r types cyb3rhq_t;

    allow cyb3rhq_t bin_t : file execute;
    allow unconfined_t cyb3rhq_t : process transition;
    allow initrc_t cyb3rhq_t : process transition;
    allow unconfined_service_t cyb3rhq_t : process transition;
    allow unconfined_t cyb3rhq_exec_t : file execute;
    allow initrc_t cyb3rhq_exec_t : file execute;
    allow unconfined_service_t cyb3rhq_exec_t : file execute;
    allow cyb3rhq_t cyb3rhq_exec_t : file entrypoint;

    type_transition unconfined_t cyb3rhq_exec_t : process cyb3rhq_t;
    type_transition initrc_t cyb3rhq_exec_t : process cyb3rhq_t;
    type_transition unconfined_service_t cyb3rhq_exec_t : process cyb3rhq_t;

    #============== Permissions for cyb3rhq-control to run Cyb3rhq
    allow cyb3rhq_t shell_exec_t:file { execute execute_no_trans };
    allow cyb3rhq_t bin_t:file execute_no_trans;

    allow cyb3rhq_t cyb3rhq_var_t:dir { create rmdir open add_name read remove_name write getattr setattr search};
    allow cyb3rhq_t cyb3rhq_var_t:file { create getattr open read append rename setattr unlink write ioctl lock};
    allow cyb3rhq_t cyb3rhq_exec_t:dir { create rmdir open getattr add_name read remove_name write setattr search};
    allow cyb3rhq_t cyb3rhq_exec_t:file { create getattr open read append rename setattr link unlink write ioctl lock execute execute_no_trans};
    allow cyb3rhq_t cyb3rhq_log_t:dir { create rmdir open getattr add_name read remove_name write setattr search};
    allow cyb3rhq_t cyb3rhq_log_t:file { create getattr open read append rename setattr link unlink write ioctl lock};
    allow cyb3rhq_t cyb3rhq_etc_t:dir { create rmdir open getattr add_name read remove_name write setattr search};
    allow cyb3rhq_t cyb3rhq_tmp_t:dir { create rmdir open getattr add_name read remove_name write setattr search rmdir};
    allow cyb3rhq_t cyb3rhq_tmp_t:file { create getattr open read append rename setattr link unlink write ioctl lock};
    allow cyb3rhq_t cyb3rhq_lib_t:dir { create rmdir open getattr add_name read remove_name write setattr search};
    allow cyb3rhq_t cyb3rhq_lib_t:file { getattr open read map execute};
    allow cyb3rhq_t cyb3rhq_var_t:filesystem { associate};
    allow cyb3rhq_var_t fs_t:filesystem { associate};
    allow cyb3rhq_etc_t fs_t:filesystem { associate};

    # Permissions to read /proc
    allow cyb3rhq_t proc_t:dir read;
    domain_read_all_domains_state(cyb3rhq_t)
    domain_getpgid_all_domains( cyb3rhq_t )
    domain_getattr_all_domains( cyb3rhq_t )
    domain_getsession_all_domains( cyb3rhq_t )
    domain_signull_all_domains( cyb3rhq_t )

    #============== Permissions for Framework and API
    allow cyb3rhq_t self:tcp_socket { bind connect create getopt listen setopt };
    allow cyb3rhq_t self:udp_socket { bind connect create getattr ioctl setopt };
    allow cyb3rhq_t node_t:tcp_socket node_bind;
    allow cyb3rhq_t node_t:udp_socket node_bind;

    #============== Permissions for cyb3rhq-analysisd to run
    allow cyb3rhq_t self:process { getattr getpgid getsession setrlimit setsched };
    allow cyb3rhq_t cyb3rhq_etc_t:file { create getattr open read append rename setattr link unlink write ioctl lock map};

    #============== Permissions for cyb3rhq-remoted to use sockets
    allow cyb3rhq_t cyb3rhq_var_t:sock_file { read write getattr create setattr unlink} ;
    allow cyb3rhq_t cyb3rhq_t:unix_stream_socket {connectto ioctl};
    allow cyb3rhq_t cyb3rhq_port_t:tcp_socket {name_connect name_bind create read write connect recvfrom sendto send_msg setopt ioctl setattr getattr};
    allow cyb3rhq_t cyb3rhq_t:tcp_socket {accept bind name_connect name_bind create read write connect recvfrom sendto send_msg setopt ioctl setattr getattr};
    allow cyb3rhq_t cyb3rhq_port_t:udp_socket {name_bind create read write connect recvfrom sendto send_msg setopt ioctl setattr getattr};
    allow cyb3rhq_t cyb3rhq_t:udp_socket {accept name_bind create read write connect recvfrom sendto send_msg setopt ioctl setattr getattr};
    allow cyb3rhq_t cyb3rhq_t:unix_dgram_socket { read write create ioctl sendto bind getopt connect};

    #============== Permissions for cyb3rhq-syscheckd to monitor files and directories and for cyb3rhq-logcollector to read logs files
    files_read_all_files(cyb3rhq_t)
    files_read_all_chr_files(cyb3rhq_t)
    files_read_all_symlinks(cyb3rhq_t)
    fs_getattr_all_chr_files(cyb3rhq_t)
    dev_getattr_all_chr_files(cyb3rhq_t)
    allow cyb3rhq_t gssproxy_var_lib_t:sock_file { getattr open read };
    allow cyb3rhq_t fixed_disk_device_t:blk_file { getattr open read };
    allow cyb3rhq_t devlog_t:sock_file { read write getattr create setattr unlink};

    #============== Permissions for rootcheck to monitor ports
    corenet_udp_bind_all_ports(cyb3rhq_t)
    corenet_tcp_bind_all_ports(cyb3rhq_t)

    #============== Permissions for cyb3rhq-modulesd to run
    allow cyb3rhq_t sysfs_t:lnk_file read;
    allow cyb3rhq_t proc_net_t:file { getattr open read };
    allow cyb3rhq_t self:netlink_route_socket {create getattr open read bind nlmsg_read write};

    # Permissions for cyb3rhq-modulesd to run SCA scans
    allow cyb3rhq_t sshd_exec_t:file { execute execute_no_trans };
    allow cyb3rhq_t useradd_exec_t:file { execute execute_no_trans};
    allow cyb3rhq_t rpm_exec_t:file { execute execute_no_trans ioctl};
    allow cyb3rhq_t systemd_systemctl_exec_t:file { execute execute_no_trans};
    allow cyb3rhq_t insmod_exec_t:file { execute execute_no_trans };
    allow cyb3rhq_t iptables_exec_t:file { execute execute_no_trans };
    allow cyb3rhq_t crontab_exec_t:file { execute execute_no_trans };
    allow cyb3rhq_t journalctl_exec_t:file { execute execute_no_trans};
    allow cyb3rhq_t mount_exec_t:file { execute execute_no_trans getattr};
    allow cyb3rhq_t rpm_log_t:file { getattr open read append};
    allow cyb3rhq_t rpm_var_lib_t:file { write create setattr unlink rename};
    allow cyb3rhq_t rpm_var_lib_t:dir { write add_name remove_name};
    allow cyb3rhq_t cert_t:dir { search write create add_name remove_name rmdir};
    allow cyb3rhq_t cert_t:file { lock write};
    allow cyb3rhq_t tmp_t:dir { search write create add_name remove_name rmdir};
    allow cyb3rhq_t unlabeled_t:file { getattr open read };
    allow cyb3rhq_t security_t:security compute_av;
    allow cyb3rhq_t security_t:file {write};
    allow cyb3rhq_t security_t:dir {write};
    allow cyb3rhq_t init_t:unix_stream_socket {connectto ioctl getattr};
    allow cyb3rhq_t init_t:system { status };
    allow cyb3rhq_t init_t:service { status };
    allow cyb3rhq_t system_dbusd_t:dbus send_msg;
    allow cyb3rhq_t tmpfs_t:dir read;
    allow cyb3rhq_t tmpfs_t:filesystem { getattr open read };
    allow cyb3rhq_t cgroup_t:filesystem { getattr open read };
    allow cyb3rhq_t configfs_t:filesystem { getattr open read };
    allow cyb3rhq_t device_t:filesystem { getattr open read };
    allow cyb3rhq_t hugetlbfs_t:filesystem { getattr open read };
    allow cyb3rhq_t proc_t:filesystem { getattr open read };
    allow cyb3rhq_t pstore_t:filesystem { getattr open read };
    allow cyb3rhq_t sysfs_t:filesystem { getattr open read };
    allow cyb3rhq_t fs_t:filesystem { getattr open read };
    allow cyb3rhq_t self:rawip_socket {bind setopt getopt create open};
    allow cyb3rhq_t kernel_t:unix_dgram_socket sendto;
    allow cyb3rhq_t auditd_unit_file_t:service { status };
    allow cyb3rhq_t crond_unit_file_t:service { status };
    allow cyb3rhq_t systemd_unit_file_t:service { status start};
    allow cyb3rhq_t mount_var_run_t:dir { getattr open read write search write};
    allow cyb3rhq_t var_run_t:dir { getattr open read search write add_name remove_name};
    allow cyb3rhq_t var_run_t:file { getattr open read write lock create unlink};
    allow cyb3rhq_t sysctl_net_t:dir search;
    allow cyb3rhq_t sysctl_net_t:file { getattr open read };
    allow cyb3rhq_t usermodehelper_t:file { getattr open read };
    allow cyb3rhq_t self:netlink_audit_socket {create setopt open read bind nlmsg_read write};
    allow cyb3rhq_t self:netlink_tcpdiag_socket {create getattr setopt read bind nlmsg_read write};
    allow cyb3rhq_t kernel_t:system module_request;
    allow dhcpc_t unlabeled_t:file {getattr open read};

    #============== Permissions for cyb3rhq-execd to run AR
    allow cyb3rhq_t self:capability { chown dac_override fowner fsetid kill net_bind_service net_raw setgid setuid sys_chroot sys_resource sys_ptrace};
    allow cyb3rhq_t etc_t:dir { getattr open read search write add_name remove_name};
    allow sshd_t var_t:file { getattr create open append ioctl lock read setattr write};
    allow cyb3rhq_t firewalld_t:dbus send_msg;
    allow firewalld_t cyb3rhq_t:dbus send_msg;
    allow cyb3rhq_t firewalld_t:process { getattr getpgid getsession signull };
    allow iptables_t var_run_t:file {open read lock};
    allow cyb3rhq_t system_dbusd_t:unix_stream_socket connectto;
    allow cyb3rhq_t http_port_t:tcp_socket {name_bind name_connect write read};

    #============== Permissions to assign new contexts
    allow unconfined_t cyb3rhq_var_t:dir {getattr open read search relabelto};
    allow unconfined_t cyb3rhq_var_t:file {getattr relabelto};
    allow unconfined_t cyb3rhq_var_t:sock_file {getattr open read relabelto};
    allow unconfined_t cyb3rhq_lib_t:dir {getattr open read search relabelto};
    allow unconfined_t cyb3rhq_lib_t:file {getattr relabelto};
    allow unconfined_t cyb3rhq_etc_t:dir {getattr open read search relabelto};
    allow unconfined_t cyb3rhq_etc_t:file {getattr open read write relabelto}; 

Cyb3rhq agent
***********

cyb3rhqT.fc
"""""""""

.. raw:: html

  <div class="accordion-section">

.. code-block:: bash

    /var/ossec/active-response                  gen_context(system_u:object_r:cyb3rhq_var_t,s0)
    /var/ossec/active-response/bin(/.*)?        gen_context(system_u:object_r:cyb3rhq_exec_t,s0)
    /var/ossec/agentless(/.*)?                  gen_context(system_u:object_r:cyb3rhq_exec_t,s0)
    /var/ossec/backup(/.*)?                     gen_context(system_u:object_r:cyb3rhq_var_t,s0)
    /var/ossec/bin(/.*)?                        gen_context(system_u:object_r:cyb3rhq_exec_t,s0)
    /var/ossec/etc(/.*)?                        gen_context(system_u:object_r:cyb3rhq_etc_t,s0)
    /var/ossec/lib(/.*)?                        gen_context(system_u:object_r:cyb3rhq_lib_t,s0)
    /var/ossec/logs(/.*)?                       gen_context(system_u:object_r:cyb3rhq_log_t,s0)
    /var/ossec/queue(/.*)?                      gen_context(system_u:object_r:cyb3rhq_var_t,s0)
    /var/ossec/ruleset(/.*)?                    gen_context(system_u:object_r:cyb3rhq_var_t,s0)
    /var/ossec/tmp(/.*)?                        gen_context(system_u:object_r:cyb3rhq_tmp_t,s0)
    /var/ossec/var(/.*)?                        gen_context(system_u:object_r:cyb3rhq_var_t,s0)
    /var/ossec/wodles(/.*)?                     gen_context(system_u:object_r:cyb3rhq_exec_t,s0)

cyb3rhqT.te
"""""""""
.. raw:: html

  <div class="accordion-section">

.. code-block:: bash

    policy_module(cyb3rhqT,1.0)

    require {
    type bin_t;
    type tmp_t;
    type unconfined_t;
    type initrc_t;
    type unconfined_service_t;
    type shell_exec_t;
    type var_t;
    type cert_t;
    type node_t;
    type init_t;
    type kernel_t;
    type system_dbusd_t;
    type sshd_t;
    type fs_t;
    type unlabeled_t;
    type sysctl_net_t;
    type systemd_unit_file_t;
    type cgroup_t;
    type hugetlbfs_t;
    type sysfs_t;
    type iptables_exec_t;
    type sshd_exec_t;
    type device_t;
    type fixed_disk_device_t;
    type useradd_exec_t;
    type journalctl_exec_t;
    type proc_net_t;
    type pstore_t;
    type mount_exec_t;
    type insmod_exec_t;
    type systemd_systemctl_exec_t;
    type crontab_exec_t;
    type devlog_t;
    type rpm_exec_t;
    type proc_t;
    type configfs_t;
    type http_port_t;
    type tmpfs_t;
    type gssproxy_var_lib_t;
    type rpm_log_t;
    type auditd_unit_file_t;
    type crond_unit_file_t;
    type mount_var_run_t;
    type rpm_var_lib_t;
    type usermodehelper_t;
    type var_run_t;
    type etc_t;
    type security_t;
    type firewalld_t;
    type iptables_t;
    type dhcpc_t;
    role system_r;
    role unconfined_r;
    class process { transition getattr getpgid getsession setrlimit setsched signull open read};
    class rawip_socket {bind setopt getopt create open};
    class netlink_route_socket {bind setopt create open write read nlmsg_read};
    class netlink_audit_socket {bind setopt create open write read nlmsg_read};
    class lnk_file {getattr open read};
    class file { getattr open read execute getattr read};
    class dir { getattr open read search };
    class tcp_socket { bind connect create getopt listen name_bind name_connect node_bind setopt };
    class capability { chown dac_override fowner fsetid kill net_bind_service net_raw setgid setuid sys_chroot sys_resource sys_ptrace};
    class unix_dgram_socket { read write create ioctl sendto bind getopt connect};
    class netlink_tcpdiag_socket {create getattr setopt read bind nlmsg_read write};
    class filesystem { getattr open read };
    class sock_file { getattr open read };
    class blk_file { getattr open read };
    class udp_socket name_bind;
    class unix_stream_socket {connectto ioctl getattr};
    class dbus send_msg;
    }

    # Private type declarations
    type cyb3rhq_t;
    type cyb3rhq_exec_t;
    type cyb3rhq_etc_t;
    type cyb3rhq_lib_t;
    type cyb3rhq_log_t;
    type cyb3rhq_tmp_t;
    type cyb3rhq_var_t;

    # Ports label
    type cyb3rhq_port_t;
    corenet_port(cyb3rhq_port_t)

    # domain_type macro specifies the type cyb3rhq_t to be a domain
    domain_type(cyb3rhq_t)

    # domain_entry_file specifies an entry point to the cyb3rhq_t domain for the executable file of type cyb3rhq_exec_t
    domain_entry_file(cyb3rhq_t, cyb3rhq_exec_t)

    # logging_log_file macro makes cyb3rhq_log_t become the type of log file with the necessary groups and rules
    logging_log_file(cyb3rhq_log_t)

    # Allow domain cyb3rhq_t to manipulate log files
    allow cyb3rhq_t cyb3rhq_log_t:file append_file_perms;

    # files_tmp_file takes the type of cyb3rhq_tmp_t to the necessary groups so that it becomes the type of tmp file
    files_tmp_file(cyb3rhq_tmp_t)

    # Allow the cyb3rhq_t domain write privileges into the tmp_t labeled directory, but with an automatic file transition towards cyb3rhq_tmp_t for every file written
    files_tmp_filetrans(cyb3rhq_t,cyb3rhq_tmp_t,file)

    # Allow domain cyb3rhq_t to manipulate tmp files
    allow cyb3rhq_t cyb3rhq_tmp_t:file manage_file_perms;

    #============== Allow transition
    role unconfined_r types cyb3rhq_t;
    role system_r types cyb3rhq_t;

    allow cyb3rhq_t bin_t : file execute;
    allow unconfined_t cyb3rhq_t : process transition;
    allow initrc_t cyb3rhq_t : process transition;
    allow unconfined_service_t cyb3rhq_t : process transition;
    allow unconfined_t cyb3rhq_exec_t : file execute;
    allow initrc_t cyb3rhq_exec_t : file execute;
    allow unconfined_service_t cyb3rhq_exec_t : file execute;
    allow cyb3rhq_t cyb3rhq_exec_t : file entrypoint;

    type_transition unconfined_t cyb3rhq_exec_t : process cyb3rhq_t;
    type_transition initrc_t cyb3rhq_exec_t : process cyb3rhq_t;
    type_transition unconfined_service_t cyb3rhq_exec_t : process cyb3rhq_t;

    #============== Permissions for cyb3rhq-control to run Cyb3rhq
    allow cyb3rhq_t shell_exec_t:file { execute execute_no_trans };
    allow cyb3rhq_t bin_t:file execute_no_trans;

    allow cyb3rhq_t cyb3rhq_var_t:dir { create rmdir open add_name read remove_name write getattr setattr search};
    allow cyb3rhq_t cyb3rhq_var_t:file { create getattr open read append rename setattr unlink write ioctl lock};
    allow cyb3rhq_t cyb3rhq_exec_t:dir { create rmdir open getattr add_name read remove_name write setattr search};
    allow cyb3rhq_t cyb3rhq_exec_t:file { create getattr open read append rename setattr link unlink write ioctl lock execute execute_no_trans};
    allow cyb3rhq_t cyb3rhq_log_t:dir { create rmdir open getattr add_name read remove_name write setattr search};
    allow cyb3rhq_t cyb3rhq_log_t:file { create getattr open read append rename setattr link unlink write ioctl lock};
    allow cyb3rhq_t cyb3rhq_etc_t:dir { create rmdir open getattr add_name read remove_name write setattr search};
    allow cyb3rhq_t cyb3rhq_etc_t:file { create getattr open read append rename setattr link unlink write ioctl lock map};
    allow cyb3rhq_t cyb3rhq_tmp_t:dir { create rmdir open getattr add_name read remove_name write setattr search rmdir};
    allow cyb3rhq_t cyb3rhq_tmp_t:file { create getattr open read append rename setattr link unlink write ioctl lock};
    allow cyb3rhq_t cyb3rhq_lib_t:dir { create rmdir open getattr add_name read remove_name write setattr search};
    allow cyb3rhq_t cyb3rhq_lib_t:file { getattr open read map execute};
    allow cyb3rhq_t cyb3rhq_var_t:filesystem { associate};
    allow cyb3rhq_var_t fs_t:filesystem { associate};
    allow cyb3rhq_etc_t fs_t:filesystem { associate};
    allow cyb3rhq_t self:process { getattr getpgid getsession setrlimit setsched };

    # Permissions to read /proc
    allow cyb3rhq_t proc_t:dir read;
    domain_read_all_domains_state(cyb3rhq_t)
    domain_getpgid_all_domains( cyb3rhq_t )
    domain_getattr_all_domains( cyb3rhq_t )
    domain_getsession_all_domains( cyb3rhq_t )
    domain_signull_all_domains( cyb3rhq_t )

    #============== Permissions for cyb3rhq-agentd to use sockets
    allow cyb3rhq_t cyb3rhq_var_t:sock_file { read write getattr create setattr unlink};
    allow cyb3rhq_t cyb3rhq_t:unix_stream_socket {connectto ioctl};
    allow cyb3rhq_t cyb3rhq_port_t:tcp_socket {name_connect name_bind create read write connect recvfrom sendto send_msg setopt ioctl setattr getattr};
    allow cyb3rhq_t cyb3rhq_t:tcp_socket {accept bind name_connect name_bind create read write connect recvfrom sendto send_msg setopt ioctl setattr getattr};
    allow cyb3rhq_t cyb3rhq_port_t:udp_socket {name_bind create read write connect recvfrom sendto send_msg setopt ioctl setattr getattr};
    allow cyb3rhq_t cyb3rhq_t:udp_socket {accept name_bind create read write connect recvfrom sendto send_msg setopt ioctl setattr getattr};
    allow cyb3rhq_t cyb3rhq_t:unix_dgram_socket { read write create ioctl sendto bind getopt connect};
    allow cyb3rhq_t self:tcp_socket { bind connect create getopt listen setopt };
    allow cyb3rhq_t self:udp_socket { bind connect create getattr ioctl setopt };
    allow cyb3rhq_t node_t:tcp_socket node_bind;
    allow cyb3rhq_t node_t:udp_socket node_bind;

    #============== Permissions for cyb3rhq-syscheckd to monitor files and directories and for cyb3rhq-logcollector to read logs files
    files_read_all_files(cyb3rhq_t)
    files_read_all_chr_files(cyb3rhq_t)
    files_read_all_symlinks(cyb3rhq_t)
    fs_getattr_all_chr_files(cyb3rhq_t)
    dev_getattr_all_chr_files(cyb3rhq_t)
    allow cyb3rhq_t gssproxy_var_lib_t:sock_file { getattr open read };
    allow cyb3rhq_t fixed_disk_device_t:blk_file { getattr open read };
    allow cyb3rhq_t devlog_t:sock_file { read write getattr create setattr unlink};

    #============== Permissions for rootcheck to monitor ports
    corenet_udp_bind_all_ports(cyb3rhq_t)
    corenet_tcp_bind_all_ports(cyb3rhq_t)

    #============== Permissions for cyb3rhq-modulesd to run
    allow cyb3rhq_t sysfs_t:lnk_file read;
    allow cyb3rhq_t proc_net_t:file { getattr open read };
    allow cyb3rhq_t self:netlink_route_socket {create getattr open read bind nlmsg_read write};

    # Permissions for cyb3rhq-modulesd to run SCA scans
    allow cyb3rhq_t sshd_exec_t:file { execute execute_no_trans };
    allow cyb3rhq_t useradd_exec_t:file { execute execute_no_trans};
    allow cyb3rhq_t rpm_exec_t:file { execute execute_no_trans ioctl};
    allow cyb3rhq_t systemd_systemctl_exec_t:file { execute execute_no_trans};
    allow cyb3rhq_t insmod_exec_t:file { execute execute_no_trans };
    allow cyb3rhq_t iptables_exec_t:file { execute execute_no_trans };
    allow cyb3rhq_t crontab_exec_t:file { execute execute_no_trans };
    allow cyb3rhq_t journalctl_exec_t:file { execute execute_no_trans};
    allow cyb3rhq_t mount_exec_t:file { execute execute_no_trans getattr};
    allow cyb3rhq_t rpm_log_t:file { getattr open read append};
    allow cyb3rhq_t rpm_var_lib_t:file { write create setattr unlink rename};
    allow cyb3rhq_t rpm_var_lib_t:dir { write add_name remove_name};
    allow cyb3rhq_t cert_t:dir { search write create add_name remove_name rmdir};
    allow cyb3rhq_t cert_t:file { lock write};
    allow cyb3rhq_t tmp_t:dir { search write create add_name remove_name rmdir};
    allow cyb3rhq_t unlabeled_t:file { getattr open read };
    allow cyb3rhq_t security_t:security compute_av;
    allow cyb3rhq_t security_t:file {write};
    allow cyb3rhq_t security_t:dir {write};
    allow cyb3rhq_t init_t:unix_stream_socket {connectto ioctl getattr};
    allow cyb3rhq_t init_t:system { status };
    allow cyb3rhq_t init_t:service { status };
    allow cyb3rhq_t system_dbusd_t:dbus send_msg;
    allow cyb3rhq_t tmpfs_t:dir read;
    allow cyb3rhq_t tmpfs_t:filesystem { getattr open read };
    allow cyb3rhq_t cgroup_t:filesystem { getattr open read };
    allow cyb3rhq_t configfs_t:filesystem { getattr open read };
    allow cyb3rhq_t device_t:filesystem { getattr open read };
    allow cyb3rhq_t hugetlbfs_t:filesystem { getattr open read };
    allow cyb3rhq_t proc_t:filesystem { getattr open read };
    allow cyb3rhq_t pstore_t:filesystem { getattr open read };
    allow cyb3rhq_t sysfs_t:filesystem { getattr open read };
    allow cyb3rhq_t fs_t:filesystem { getattr open read };
    allow cyb3rhq_t self:rawip_socket {bind setopt getopt create open};
    allow cyb3rhq_t kernel_t:unix_dgram_socket sendto;
    allow cyb3rhq_t auditd_unit_file_t:service { status };
    allow cyb3rhq_t crond_unit_file_t:service { status };
    allow cyb3rhq_t systemd_unit_file_t:service { status start};
    allow cyb3rhq_t mount_var_run_t:dir { getattr open read write search write};
    allow cyb3rhq_t var_run_t:dir { getattr open read search write add_name remove_name};
    allow cyb3rhq_t var_run_t:file { getattr open read write lock create unlink};
    allow cyb3rhq_t sysctl_net_t:dir search;
    allow cyb3rhq_t sysctl_net_t:file { getattr open read };
    allow cyb3rhq_t usermodehelper_t:file { getattr open read };
    allow cyb3rhq_t self:netlink_audit_socket {create setopt open read bind nlmsg_read write};
    allow cyb3rhq_t self:netlink_tcpdiag_socket {create getattr setopt read bind nlmsg_read write};
    allow cyb3rhq_t kernel_t:system module_request;
    allow dhcpc_t unlabeled_t:file {getattr open read};

    #============== Permissions for cyb3rhq-execd to run AR
    allow cyb3rhq_t self:capability { chown dac_override fowner fsetid kill net_bind_service net_raw setgid setuid sys_chroot sys_resource sys_ptrace};
    allow cyb3rhq_t etc_t:dir { getattr open read search write add_name remove_name};
    allow sshd_t var_t:file { getattr create open append ioctl lock read setattr write};
    allow cyb3rhq_t firewalld_t:dbus send_msg;
    allow firewalld_t cyb3rhq_t:dbus send_msg;
    allow cyb3rhq_t firewalld_t:process { getattr getpgid getsession signull };
    allow iptables_t var_run_t:file {open read lock};
    allow cyb3rhq_t system_dbusd_t:unix_stream_socket connectto;
    allow cyb3rhq_t http_port_t:tcp_socket {name_bind name_connect write read};

    #============== Permissions to assign new contexts
    allow unconfined_t cyb3rhq_var_t:dir {getattr open read search relabelto};
    allow unconfined_t cyb3rhq_var_t:file {getattr relabelto};
    allow unconfined_t cyb3rhq_var_t:sock_file {getattr open read relabelto};
    allow unconfined_t cyb3rhq_lib_t:dir {getattr open read search relabelto};
    allow unconfined_t cyb3rhq_lib_t:file {getattr relabelto};
    allow unconfined_t cyb3rhq_etc_t:dir {getattr open read search relabelto};
    allow unconfined_t cyb3rhq_etc_t:file {getattr open read write relabelto};
 

cyb3rhqT.fc and cyb3rhqT.te file content descriptions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Below there is a description of the ``cyb3rhqT.fc`` and ``cyb3rhqT.te`` files. These descriptions are based on the Cyb3rhq manager files. 


cyb3rhqT.fc
*********

    In this file, the security contexts for each folder and file within the Cyb3rhq folder are declared. For example, we assign the context ``cyb3rhq_exec_t`` to executable files, including ``/ossec/active-response/bin/*`` and ``/ossec/bin/*``. In this way, we declare a Cyb3rhq context for each file in the ``/var/ossec`` directory:

    .. code-block:: bash

        /var/ossec/active-response                  gen_context(system_u:object_r:cyb3rhq_var_t,s0)
        /var/ossec/active-response/bin(/.*)?        gen_context(system_u:object_r:cyb3rhq_exec_t,s0)
        /var/ossec/agentless(/.*)?                  gen_context(system_u:object_r:cyb3rhq_exec_t,s0)
        /var/ossec/api                              gen_context(system_u:object_r:cyb3rhq_var_t,s0)
        /var/ossec/api/configuration(/.*)?          gen_context(system_u:object_r:cyb3rhq_etc_t,s0)
        /var/ossec/api/scripts(/.*)?                gen_context(system_u:object_r:cyb3rhq_exec_t,s0)
        /var/ossec/backup(/.*)?                     gen_context(system_u:object_r:cyb3rhq_var_t,s0)
        /var/ossec/bin(/.*)?                        gen_context(system_u:object_r:cyb3rhq_exec_t,s0)
        /var/ossec/etc(/.*)?                        gen_context(system_u:object_r:cyb3rhq_etc_t,s0)
        /var/ossec/framework(/.*)?                  gen_context(system_u:object_r:cyb3rhq_exec_t,s0)
        /var/ossec/integrations(/.*)?               gen_context(system_u:object_r:cyb3rhq_exec_t,s0)
        /var/ossec/lib(/.*)?                        gen_context(system_u:object_r:cyb3rhq_lib_t,s0)
        /var/ossec/logs(/.*)?                       gen_context(system_u:object_r:cyb3rhq_log_t,s0)
        /var/ossec/queue(/.*)?                      gen_context(system_u:object_r:cyb3rhq_var_t,s0)
        /var/ossec/ruleset(/.*)?                    gen_context(system_u:object_r:cyb3rhq_var_t,s0)
        /var/ossec/stats(/.*)?                      gen_context(system_u:object_r:cyb3rhq_var_t,s0)
        /var/ossec/tmp(/.*)?                        gen_context(system_u:object_r:cyb3rhq_tmp_t,s0)
        /var/ossec/var(/.*)?                        gen_context(system_u:object_r:cyb3rhq_var_t,s0)
        /var/ossec/wodles(/.*)?                     gen_context(system_u:object_r:cyb3rhq_exec_t,s0)

.. note::

    Note that in the definition of the contexts for each Cyb3rhq folder the default installation folder (``/var/ossec/``) was used.


cyb3rhqT.te
*********

    The ``cyb3rhqT.te`` file is the main file of the module, where it is defined:

- The name and version of the module. The module, the ``.te`` file, and the ``.fc`` file must have the same name.

    .. code-block:: console

        policy_module(cyb3rhqT,1.0)

- The private contexts of Cyb3rhq.

    .. code-block:: console

        type cyb3rhq_t;
        type cyb3rhq_exec_t;
        type cyb3rhq_etc_t;
        type cyb3rhq_lib_t;
        type cyb3rhq_log_t;
        type cyb3rhq_tmp_t;
        type cyb3rhq_var_t;

- Definition of the ``cyb3rhq_port_t`` type to which the ports used by Cyb3rhq will be associated.

    .. code-block:: console

        type cyb3rhq_port_t;
        corenet_port(cyb3rhq_port_t)

- Specifies that the ``cyb3rhq_t`` type is a domain, and that the entry point to the ``cyb3rhq_t`` domain is through an executable of type ``cyb3rhq_exec_t``.

    .. code-block:: console

        # domain_type macro specifies the type cyb3rhq_t to be a domain.
        domain_type(cyb3rhq_t)

        # domain_entry_file specifies an entry point to the cyb3rhq_t domain for the executable file of type cyb3rhq_exec_t.
        domain_entry_file(cyb3rhq_t, cyb3rhq_exec_t)

- Creation of the necessary rules to allow the transition from an ``unconfined_t`` context to the ``cyb3rhq_t`` context.

    .. code-block:: console

        role unconfined_r types cyb3rhq_t;
        role system_r types cyb3rhq_t;

        allow cyb3rhq_t bin_t : file { execute read getattr };
        allow unconfined_t cyb3rhq_t : process transition;
        allow initrc_t cyb3rhq_t : process transition;
        allow unconfined_service_t cyb3rhq_t : process transition;
        allow unconfined_t cyb3rhq_exec_t : file { execute read getattr };
        allow initrc_t cyb3rhq_exec_t : file { execute read getattr };
        allow unconfined_service_t cyb3rhq_exec_t : file { execute read getattr };
        allow cyb3rhq_t cyb3rhq_exec_t : file entrypoint;

        type_transition unconfined_t cyb3rhq_exec_t : process cyb3rhq_t;
        type_transition initrc_t cyb3rhq_exec_t : process cyb3rhq_t;
        type_transition unconfined_service_t cyb3rhq_exec_t : process cyb3rhq_t;

- Creation of the necessary rules for each Cyb3rhq module to work correctly, for example:

    +---------------------------------------------------+-------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
    | Module                                            | Rules                                                                                           | Description                                                                                                       |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | Target context            | Object type           | Permissions                                 |                                                                                                                   |
    +===================================================+===========================+=======================+=============================================+===================================================================================================================+
    | **cyb3rhq-control**                                 | shell_exec_t              | file                  | execute, execute_no_trans                   | These rules allow **cyb3rhq-control** and startup scripts to perform the necessary tasks to start Cyb3rhq.            |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | bin_t                     | file                  | execute_no_trans                            |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_var_t               | dir                   | create rmdir, open, add_name, read, write,  |                                                                                                                   |
    |                                                   |                           |                       | remove_name, getattr, setattr, search       |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_var_t               | file                  | create, getattr, open, read, append, lock,  |                                                                                                                   |
    |                                                   |                           |                       | setattr, unlink, write, ioctl, rename       |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_exec_t              | dir                   | create rmdir, open, add_name, read, write,  |                                                                                                                   |
    |                                                   |                           |                       | remove_name, getattr, setattr, search       |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_exec_t              | file                  | create, getattr, open, read, append, lock,  |                                                                                                                   |
    |                                                   |                           |                       | setattr, unlink, write, ioctl, rename,      |                                                                                                                   |
    |                                                   |                           |                       | link, execute, execute_no_trans             |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_log_t               | dir                   | create rmdir, open, add_name, read, write,  |                                                                                                                   |
    |                                                   |                           |                       | remove_name, getattr, setattr, search       |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_log_t               | file                  | create, getattr, open, read, append, lock,  |                                                                                                                   |
    |                                                   |                           |                       | setattr, unlink, write, ioctl, rename,      |                                                                                                                   |
    |                                                   |                           |                       | link                                        |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_etc_t               | dir                   | create rmdir, open, add_name, read, write,  |                                                                                                                   |
    |                                                   |                           |                       | remove_name, getattr, setattr, search       |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_tmp_t               | dir                   | create rmdir, open, add_name, read, write,  |                                                                                                                   |
    |                                                   |                           |                       | remove_name, getattr, setattr, search       |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_tmp_t               | file                  | create, getattr, open, read, append, lock,  |                                                                                                                   |
    |                                                   |                           |                       | setattr, unlink, write, ioctl, rename,      |                                                                                                                   |
    |                                                   |                           |                       | link                                        |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_lib_t               | dir                   | create rmdir, open, add_name, read, write,  |                                                                                                                   |
    |                                                   |                           |                       | remove_name, getattr, setattr, search       |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_lib_t               | file                  | getattr, open, read, map, execute           |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_var_t               | filesystem            | associate                                   |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | proc_t                    | dir                   | read                                        |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | all                       | process               | status, getpgid, getattr, getsession,       |                                                                                                                   |
    |                                                   |                           |                       | signull                                     |                                                                                                                   |
    +---------------------------------------------------+---------------------------+-----------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
    | **Framework & API**                               | cyb3rhq_t                   | tcp_socket            | bind, connect, create, getopt, listen,      | These rules allow the **API** to listen for requests.                                                             |
    |                                                   |                           |                       | setopt                                      |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_t                   | udp_socket            | bind, connect, create, getattr, ioctl,      |                                                                                                                   |
    |                                                   |                           |                       | setopt                                      |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | node_t                    | tcp_socket            | node_bind                                   |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | node_t                    | udp_socket            | node_bind                                   |                                                                                                                   |
    +---------------------------------------------------+---------------------------+-----------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
    | **cyb3rhq-analysisd**                               | cyb3rhq_t                   | process               | getattr, getpgid, getsession, setrlimit,    | These rules allow **cyb3rhq-analysisd**, for example, to set the necessary permissions, read rules files            |
    |                                                   |                           |                       | setsched                                    | and cdb lists.                                                                                                    |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_etc_t               | file                  | create, getattr, open, read, append,        |                                                                                                                   |
    |                                                   |                           |                       | rename, setattr, link, unlink, write,       |                                                                                                                   |
    |                                                   |                           |                       | ioctl, lock map                             |                                                                                                                   |
    +---------------------------------------------------+---------------------------+-----------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
    | **cyb3rhq-remoted**                                 | cyb3rhq_var_t               | sock_file             | read, write, getattr, create, setattr,      | These rules allow **cyb3rhq-remoted** to use ``tcp/udp`` sockets to communicate with agents.                        |
    |                                                   |                           |                       | unlink                                      |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_t                   | unix_stream_socket    | connectto, ioctl                            |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_port_t              | tcp_socket            | name_connect, name_bind, create, read,      |                                                                                                                   |
    |                                                   |                           |                       | write, connect, recvfrom, sendto, send_msg, |                                                                                                                   |
    |                                                   |                           |                       | setopt, ioctl, setattr, getattr             |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_t                   | tcp_socket            | name_connect, name_bind, create, read, bind |                                                                                                                   |
    |                                                   |                           |                       | write, connect, recvfrom, sendto, send_msg, |                                                                                                                   |
    |                                                   |                           |                       | setopt, ioctl, setattr, getattr, accept     |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_port_t              | udp_socket            | name_bind, create, read, write, connect,    |                                                                                                                   |
    |                                                   |                           |                       | recvfrom, sendto, send_msg, setopt, ioctl,  |                                                                                                                   |
    |                                                   |                           |                       | setattr, getattr                            |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_t                   | udp_socket            | accept, name_bind, create, read, write,     |                                                                                                                   |
    |                                                   |                           |                       | connect, recvfrom, sendto, send_msg,        |                                                                                                                   |
    |                                                   |                           |                       | setopt, ioctl, setattr, getattr             |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_t                   | unix_dgram_socket     | read, write, create, ioctl, sendto, bind,   |                                                                                                                   |
    |                                                   |                           |                       | getopt, connect                             |                                                                                                                   |
    +---------------------------------------------------+---------------------------+-----------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
    | **cyb3rhq-syscheckd** & **cyb3rhq-logcollector**      | all                       | file                  | read                                        | These rules allow **cyb3rhq-syscheckd** to monitor files and folders inside the ``/etc``, ``/usr`` or ``/bin``      |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+ directories present in Cyb3rhq's default configuration; they also allow **cyb3rhq-logcollector** to read log files.   |
    |                                                   | all                       | chr_file              | read                                        |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | all                       | symlinks              | read                                        |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | all                       | filesystem            | getattr                                     |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | all                       | device                | getattr                                     |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | gssproxy_var_lib_t        | sock_file             | getattr, open, read                         |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | fixed_disk_device_t       | blk_file              | getattr, open, read                         |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | devlog_t                  | sock_file             | read, write, getattr, create, setattr,      |                                                                                                                   |
    |                                                   |                           |                       | unlink                                      |                                                                                                                   |
    +---------------------------------------------------+---------------------------+-----------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
    | **rootcheck**                                     | all                       | udp_socket            | bind_name                                   | These rules allow **rootcheck** to check which ports are open.                                                    |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | all                       | tcp_socket            | bind_name                                   |                                                                                                                   |
    +---------------------------------------------------+---------------------------+-----------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
    | **cyb3rhq-modulesd**                                | sysfs_t                   | lnk_file              | read                                        | These are some of the rules that allow **cyb3rhq-modulesd** to, for example, run a SCA scan.                        |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | proc_net_t                | file                  | getattr, open, read                         |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_t                   | netlink_route_socket  | create, getattr, open, read, bind,          |                                                                                                                   |
    |                                                   |                           |                       | nlmsg_read, write                           |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | sshd_exec_t               | file                  | execute, execute_no_trans                   |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | useradd_exec_t            | file                  | execute, execute_no_trans                   |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | rpm_exec_t                | file                  | execute, execute_no_trans, ioctl            |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | systemd_systemctl_exec_t  | file                  | execute, execute_no_trans                   |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | insmod_exec_t             | file                  | execute, execute_no_trans                   |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | iptables_exec_t           | file                  | execute, execute_no_trans                   |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | crontab_exec_t            | file                  | execute, execute_no_trans                   |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | journalctl_exec_t         | file                  | execute, execute_no_trans                   |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | mount_exec_t              | file                  | execute, execute_no_trans, getattr          |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | rpm_log_t                 | file                  | getattr, open, read, append                 |                                                                                                                   |
    +---------------------------------------------------+---------------------------+-----------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
    | **cyb3rhq-execd**                                   | cyb3rhq_t                   | capability            | chown, dac_override, fowner, fsetid, kill,  | These rules were added to allow **cyb3rhq-execd** to run ARs such as ``firewall-drop``, ``host-deny``               |
    |                                                   |                           |                       | net_bind_service, net_raw, setgid, setuid,  | or ``cyb3rhq-slack``.                                                                                               |
    |                                                   |                           |                       | sys_chroot, sys_resource, sys_ptrace        |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | etc_t                     | dir                   | getattr, open, read, search, write,         |                                                                                                                   |
    |                                                   |                           |                       | add_name, remove_name                       |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | var_t                     | file                  | getattr, create, open, append, ioctl, lock, |                                                                                                                   |
    |                                                   |                           |                       | read, setattr, write                        |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | firewalld_t               | dbus                  | send_msg                                    |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | cyb3rhq_t                   | dbus                  | send_msg                                    |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | firewalld_t               | process               | getattr, getpgid, getsession, signull       |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | system_dbusd_t            | unix_stream_socket    | connectto                                   |                                                                                                                   |
    |                                                   +---------------------------+-----------------------+---------------------------------------------+                                                                                                                   |
    |                                                   | http_port_t               | tcp_socket            | name_bind, name_connect, write read         |                                                                                                                   |
    +---------------------------------------------------+---------------------------+-----------------------+---------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

    .. note::

        These are some of the many rules necessary for Cyb3rhq to run. The above categorization by module is for illustrative purposes only, as many of the rules are shared by different Cyb3rhq modules.


Steps to build and load the new SELinux policy module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. Install required dependencies.

    .. code-block:: console

        # yum install -y selinux-policy-devel gcc make

#. Stop Cyb3rhq.

    .. code-block:: console

        # systemctl stop cyb3rhq-manager

#. Verify current SELinux state.

    .. code-block:: console

        # getenforce

    In case the SELinux status is ``Enforcing`` we must change it to ``Permissive`` momentarily.

        .. code-block:: console

            # setenforce 0

#. Create the directory for the files ``cyb3rhqT.te`` and ``cyb3rhqT.fc``.

    .. code-block:: console

        # mkdir selinux-cyb3rhq && cd selinux-cyb3rhq

#. Download the ``cyb3rhqT.te`` and ``cyb3rhqT.fc`` files and compile the module.

    .. code-block:: console

        # curl -sO https://raw.githubusercontent.com/cyb3rhq/cyb3rhq-documentation/|CYB3RHQ_CURRENT_MINOR|/resources/selinux/manager/cyb3rhqT.fc
        # curl -sO https://raw.githubusercontent.com/cyb3rhq/cyb3rhq-documentation/|CYB3RHQ_CURRENT_MINOR|/resources/selinux/manager/cyb3rhqT.te
        # make -f /usr/share/selinux/devel/Makefile

#. Install the new policy module.

    .. code-block:: console

        # semodule -i cyb3rhqT.pp

#. Check that it has been loaded correctly.

    .. code-block:: console

        # semodule -l | grep cyb3rhqT

    .. code-block:: console
      :class: output

        cyb3rhqT 1.0

#. Run ``restorecon`` to assign the new tags defined in the ``cyb3rhqT.fc`` file to existing files in the Cyb3rhq directory.

    .. code-block:: console

        # restorecon -RFvv /var/ossec/

#. Verify that the files have the appropriate contexts.

    .. code-block:: console

        # ls -lZ /var/ossec/bin/

#. Assign the port numbers used by cyb3rhq to the context ``cyb3rhq_port_t``.

    .. code-block:: console

        # semanage port -a -t cyb3rhq_port_t -p tcp 1514
        # semanage port -a -t cyb3rhq_port_t -p udp 1514

    .. note::

        For the Cyb3rhq manager, you must add port 1515 used by **cyb3rhq-authd** and 1516 which is used by **cyb3rhq-clusterd**.

#. Change SELinux to Enforcing.

    .. code-block:: console

        # setenforce 1

#. Start Cyb3rhq.

    .. code-block:: console

        # systemctl start cyb3rhq-manager

By running the command ``ps auxZ | grep cyb3rhq`` we can see that Cyb3rhq is running with the new context ``cyb3rhq_t``:

    .. code-block:: console

        ps auxZ | grep cyb3rhq
        system_u:system_r:cyb3rhq_t:s0   cyb3rhq    18239  8.2 16.5 435332 82744 ?        Sl   18:50   0:09 /var/ossec/framework/python/bin/python3 /var/ossec/api/scripts/cyb3rhq_apid.py
        system_u:system_r:cyb3rhq_t:s0   root     18281  0.0  0.3 191524  1540 ?        Sl   18:50   0:00 /var/ossec/bin/cyb3rhq-authd
        system_u:system_r:cyb3rhq_t:s0   cyb3rhq    18298  0.6  1.3 641364  6588 ?        Sl   18:50   0:00 /var/ossec/bin/cyb3rhq-db
        system_u:system_r:cyb3rhq_t:s0   root     18322  0.0  0.2  35888  1236 ?        Sl   18:50   0:00 /var/ossec/bin/cyb3rhq-execd
        system_u:system_r:cyb3rhq_t:s0   cyb3rhq    18337  3.0 16.2 755924 80936 ?        Sl   18:50   0:03 /var/ossec/bin/cyb3rhq-analysisd
        system_u:system_r:cyb3rhq_t:s0   root     18350 21.5  0.9 349040  4528 ?        SNl  18:50   0:24 /var/ossec/bin/cyb3rhq-syscheckd
        system_u:system_r:cyb3rhq_t:s0   cyb3rhq    18367  0.3  0.3 520512  1840 ?        Sl   18:50   0:00 /var/ossec/bin/cyb3rhq-remoted
        system_u:system_r:cyb3rhq_t:s0   root     18409  0.4  0.8 478308  4172 ?        Sl   18:50   0:00 /var/ossec/bin/cyb3rhq-logcollector
        system_u:system_r:cyb3rhq_t:s0   cyb3rhq    18429  0.0  0.2  35860  1192 ?        Sl   18:50   0:00 /var/ossec/bin/cyb3rhq-monitord
        system_u:system_r:cyb3rhq_t:s0   root     18442  5.1  1.3 714180  6840 ?        Sl   18:50   0:05 /var/ossec/bin/cyb3rhq-modulesd


Create custom SELinux module
----------------------------

In this section we will see how to create a set of rules with the **audit2allow** tool in any SELinux environment.

.. note::

    For this example we assume that Cyb3rhq has already been transitioned to a proper context other than ``unconfined_t``, you can see :ref:`SELinux-module-example`.

#. Change SELinux to Permissive, this will allow denial events to be logged but will not block the required action.

    .. code-block:: console

        # setenforce 0

#. Start Cyb3rhq and use it for a while.

    .. code-block:: console

        # systemctl start cyb3rhq-manager

#. Stop Cyb3rhq.

    .. code-block:: console

        # systemctl stop cyb3rhq-manager

#. Use the **audit2allow** tool to create a set of rules.

    .. note::

        Note that you must change the ``--start`` and ``--end`` dates to the length of time your test lasted.

    .. code-block:: console

        # ausearch -m AVC --start 11/08/2021 19:58:19 --end 11/08/2021 23:58:19 | audit2allow -a -M test_audit

#. Install the new module.

    .. code-block:: console

        # semodule -i test_audit.pp

#. Change SELinux to Enforcing.

    .. code-block:: console

        # setenforce 1

#. Start Cyb3rhq.

    .. code-block:: console

        # systemctl start cyb3rhq-manager


Troubleshooting
---------------

Create missing rules
^^^^^^^^^^^^^^^^^^^^

It is possible that more rules may need to be added, as it depends on what applications are installed in the environment as well as what is being monitored. To do this, you need to follow these steps:

#. Check which action is being blocked.

    .. code-block:: console

        # grep denied /var/log/audit/audit.log | ausearch -i
        ...
        type=AVC msg=audit(11/19/2021 13:45:23.239:486) : avc:  denied  { search } for  pid=1944 comm=cyb3rhq-modulesd name=960 dev="proc" ino=17328 scontext=system_u:system_r:cyb3rhq_t:s0 tcontext=system_u:system_r:sshd_net_t:s0-s0:c0.c1023 tclass=dir permissive=0
        ...

#. Create the rule to allow the blocked action.

    Manually:
        - It is possible to create a new rule and add it to the ``cyb3rhqT.te`` file, for example:

            .. code-block:: console

                allow cyb3rhq_t sshd_net_t:dir search;

        - Re-compile and install the policy module:

            .. code-block:: console

                # make -f /usr/share/selinux/devel/Makefile
                # semodule -i cyb3rhqT.pp

    Using **audit2allow** tool:
        - It is also possible to create the rules with the **audit2allow** tool. This tool takes the logged AVCs in the ``/var/log/audit/audit.log`` file and creates the necessary rules. It is possible to filter the logs, for example by date and time.

            .. code-block:: console

                # ausearch -m AVC --start 11/19/2021 13:45:00 --end 11/19/2021 13:46:00 | audit2allow -a -M test_audit

        - Install the new module.

            .. code-block:: console

                # semodule -i test_audit.pp

Delete module and restore context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In case you need to restore the file context to the state prior to the installation of the ``cyb3rhqT`` module, you need to follow these steps:

#. Delete the assigned ports.

    .. code-block:: console

        # semanage port -d -p tcp 1514
        # semanage port -d -p udp 1514

#. Delete the loaded module.

    .. code-block:: console

        # semodule -d cyb3rhqT

#. Execute ``restorecon``.

    .. code-block:: console

        # restorecon -RFvv /var/ossec/
