- name: Facts test
  hosts: webserver
  become: yes
  tasks:
       - name: Install nginx on Debian
         apt:
            name: nginx
            state: present
         when: ansible_os_family == "Debian"
       - name: Install nginx on redhat
         yum:
            name: nginx
            state: present
         when: ansible_os_family == "RedHat"
