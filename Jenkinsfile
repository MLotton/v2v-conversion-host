pipeline {
  agent {
    dockerfile {
      filename '.DockerFileJenkins'
      args '-v /var/run/docker.sock:/var/run/docker.sock --group-add docker'
    }

  }
  stages {
    stage('Launch molecule') {
      steps {
        sh 'mkdir ansible/oVirt.v2v-conversion-host/files'
        sh 'cp wrapper/virt-v2v-wrapper.py ansible/oVirt.v2v-conversion-host/files/.'
        sh 'cd ansible/oVirt.v2v-conversion-host'
        sh 'pwd'
        sh 'touch testFileIAMHERE'
        sh 'id'
        sh 'cat /etc/passwd'
        sh 'ls -l'
        sh 'ls -l /var/lib/'
        sh 'ls -l /var/lib/jenkins'
        sh 'cd ansible/oVirt.v2v-conversion-host/ && molecule --debug test -s install'
      }
    }
  }
}
