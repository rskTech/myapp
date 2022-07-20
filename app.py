- name: template test
  hosts: webserver
  become: yes
  vars_prompt:
      name: port
      prompt: Enter port number for server
  tasks:
     - name: template task
       template:
               src: default
               dest: /etc/nginx/sites-enabled
     - name: restart nginx
       service:
            name: nginx
            state: restarted
