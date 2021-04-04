import subprocess
import docker

BASE_COMMAND = 'docker'
CREATE_CONTAINER = 'volume create --name='
RUN_CONTAINER = 'run -d -p 27017:27017 --name dbname mongo'
STOP_CONTAINER = 'stop'
REMOVE_CONTAINER = 'container rm'


class ContainerService:
    def __init__(self, name):
        self.name = name
        self.client = docker.from_env()
        self.id = None

    def create(self):
        process = subprocess.run('{base} {create}{name}'.format(base=BASE_COMMAND,
                                                                create=CREATE_CONTAINER,
                                                                name=self.name), shell=True)
        print(process)

    def run(self):
        process = subprocess.run('{base} {run}'.format(base=BASE_COMMAND,
                                                       run=RUN_CONTAINER.replace('dbname', self.name), shell=True))
        print(process)
        self.id = self.get_id(self.name)

    def get_id(self, name):
        if self.client.containers.list(filters={'name': name}):
            response = self.client.containers.list(filters={'name': name})
            return str(response[0].id)[:12]
        else:
            return None

    def clear_db(self):
        self.client.dropDatabase(self.name)

    def stop(self):
        subprocess.run('{base} {stop} {id}'.format(base=BASE_COMMAND,
                                                   stop=STOP_CONTAINER,
                                                   id=self.id), shell=True)

    def remove(self):
        subprocess.run('{base} {remove} {id}'.format(base=BASE_COMMAND,
                                                     remove=REMOVE_CONTAINER,
                                                     id=self.id), shell=True)
