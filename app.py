- name: Handler test
  hosts: webserver
  become: yes
  tasks:
       - name: Install nginx
         apt:
            name: nginx
            state: present
       - name: Change config file
         copy:
            src: 1.yaml
            dest: /opt
         notify:
                - restart nginx
  handlers:
       - name: restart nginx
         service:
             name: nginx
             state: restarted
