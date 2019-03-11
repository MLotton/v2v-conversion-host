pipeline {
  agent {
    dockerfile {
      filename '.DockerFileJenkins'
      args '-v /var/run/docker.sock:/var/run/docker.sock --group-add docker'
    }

  }
  stages {
    stage('init') {
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
      }
    }
    stage('init openstack vars') {
      steps {
        withCredentials(bindings: [file(credentialsId: '90becc3f-2c57-4b3f-89ae-3b9bc3b422c9', variable: 'OPENSTACK_FILE')]) {
          sh '. $OPENSTACK_FILE | echo -n'
        }

        sh 'export testVAR="coucou"'
        sh 'env'
      }
    }
    stage('molecule openstack') {
      environment {
        OS_AUTH_URL = credentials('OS_AUTH_URL')
        OS_CACERT = credentials('OS_CACERT')
        OS_PROJECT_ID = credentials('OS_PROJECT_ID')
        OS_PROJECT_NAME = credentials('OS_PROJECT_NAME')
        OS_USER_DOMAIN_NAME = 'Default'
        OS_PROJECT_DOMAIN_ID = 'default'
        OS_USERNAME = credentials('OS_USERNAME')
        OS_PASSWORD = credentials('OS_PASSWORD')
        OS_REGIEN_NAME = 'regionOne'
        OS_INTERFACE = 'public'
        OS_IDENTITY_API_VERSION = '3'
      }
      steps {
        sh 'cd ansible/oVirt.v2v-conversion-host/ && molecule --debug test -s install-openstack'
      }
    }
    stage('molecule docker') {
      steps {
        sh 'cd ansible/oVirt.v2v-conversion-host/ && molecule --debug test -s install'
      }
    }
  }
}
