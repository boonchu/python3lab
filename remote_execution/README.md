##### Executor
  * https://github.com/xolox/python-executor {origin}
  * https://github.com/david-caro/Python-clfu {inspired}

##### Tools
  * http://www.paramiko.org/
  * http://www.fabfile.org/

```
>>> from executor import execute
>>> execute('true')
True
>>> execute('false')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/site-packages/executor/__init__.py", line 186, in execute
    cmd.start()
  File "/usr/local/lib/python2.7/site-packages/executor/__init__.py", line 1169, in start
    self.wait()
  File "/usr/local/lib/python2.7/site-packages/executor/__init__.py", line 1201, in wait
    self.check_errors(check=check)
  File "/usr/local/lib/python2.7/site-packages/executor/__init__.py", line 1294, in check_errors
    raise self.error_type(self)
executor.ExternalCommandFailed: External command failed with exit code 1! (command: bash -c false)
>>> execute('tr a-z A-Z', input='Hello world from Python!\n')
HELLO WORLD FROM PYTHON!
True
>>> execute('hostname', capture=True)
u'MacPro.local'
>>> execute('echo test > /etc/hostname', sudo=True)
Password:
True
>>> execute('hostname', capture=True)
u'MacPro.local'

>>> import logging
>>> logging.basicConfig()
>>> logging.getLogger().setLevel(logging.DEBUG)

>>> from executor import execute
>>> execute('echo test', sudo=False)
DEBUG:executor:Executing external command: bash -c 'echo test'
test
True
```

  * Fabric 

```

from fabric.context_managers import cd
from fabric.operations import sudo
from fabric.api import run, env
import os

HOME = os.getenv('HOME')

def ec2():
    """ use environment ec2 """
    env.user = 'ubuntu'
    env.hosts = ['PUBLICDNS.ap-southeast-1.compute.amazonaws.com','ANOTHERSERVER.compute.amazonaws.com']
    # 
    #env.key_filename = [ '%s/<your-keypair-file>.pem'%HOME ] 
    #http://stackoverflow.com/questions/14652965/how-to-pass-ssh-options-with-fabric?rq=1
    env.disable_known_hosts = True
    

def update():
    """ initialize with update ec2 """
    with cd('/var/www'):
            sudo('svn update')
                 with cd ('/var/www/cache'):
                       run('rm -rf *')
    sudo('service lighttpd restart')

$ fab -i keyec2.pem ec2 update

```

  * Use Fabric with ssh-agent
     * http://stackoverflow.com/questions/7772373/run-ssh-add-with-fabric-in-a-machine?rq=1


  * Testing ssh with Fabric

```
>>> from fabric.api import *
>>> from fabric.network import ssh_config
>>> env.use_ssh_config = True
>>> env.host_string = 'test'
>>> ssh_config()
{'gssapidelegatecredentials': 'yes', 'hostname': '8.8.8.8', 'gssapiauthentication': 'yes', 'passwordauthentication': 'no', 'user': 'root', 'forwardagent': 'yes', 'controlpath': '~/.ssh/cm_socket/%r@%h:%p', 'controlmaster': 'auto', 'controlpersist': '7200'}
>>> ssh_config('test')
{'gssapidelegatecredentials': 'yes', 'hostname': '8.8.8.8', 'gssapiauthentication': 'yes', 'passwordauthentication': 'no', 'user': 'root', 'forwardagent': 'yes', 'controlpath': '~/.ssh/cm_socket/%r@%h:%p', 'controlmaster': 'auto', 'controlpersist': '7200'}
>>> 
```

  * Fab with host role

```
from fabric.api import env,hosts,run,execute
 
env.roledefs['webservers'] = ['foo01.bang.whiz.com', 'foo02.bang.whiz.com']
env.roledefs['dbservers'] = ['db.bang.whiz.com']
 
@roles('webservers')
def install_apache():
    run('apt-get install apache2', with_sudo=True)
 
@roles('dbservers')
def install_mysql():
    run('apt-get install mysql-server', with_sudo=True)
 
def deploy():
    execute(install_apache)
    execute(install_mysql)
```
