- name: First playbook
  hosts: webserver
  become: yes
  vars_prompt:
      name: myvar1
      prompt: Enter the myvar value
  tasks:
      - name: Installa the nginx
        apt:
            name: nginx
            state: present
      - name: Copy file
        copy:
            src: 1.yaml
            dest: /opt
      - name: restart nginx
        service:
            name: nginx
            state: restarted
      - name: Create user john
        user:
            name: johnd
            comment: John Doe
            uid: 1040
            group: admin
        register: myvar
      - name: debug test
        debug:
            msg: "{{myvar}}"
      - name: Another debug
        debug:
            msg: "{{myvar1}}"
