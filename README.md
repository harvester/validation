# validation

Test Framework: `Pytest` </br>
Jenkins: http://172.16.1.75:8080/ 

**Pipeline Execution Process**
![image](https://user-images.githubusercontent.com/54788198/112452253-63425d00-8d91-11eb-8209-cb54e0d59fcd.png)

### Code Structure 

build.sh: script to build a Docker image that runs Pytest </br>
configure.sh: script that import the job parameters into the pipeline environment variable </br>
common.py: common code method </br>
Jenkinsfile: Jenkins Pipeline script file </br>
test_auth.py: test code example, must begin with `test_` </br>
Dockerfile.v1api: Docker image file that executes the test script </br>
requirements_v1api: python packages configuration file 

### Code Rules 

- The variable names retrieved from Jenkins begin with `CATTLE_, ADMIN, HARVESTER_, DEBUG,  DEFAULT_, DOCKER_, CLOUD_, KUBE, SLACK_`. 
- The test file begins with `test_`, and must be in `${repository}/tests/v1_api/`. 
- The test methods begin with `test_`. 

### Note

Jenkins in the Intranet environment pulls the code from GitHub timeout, job builds often fail. It is necessary to synchronize the code from GitHub to the domestic code repository(Gitee is currently used). 
