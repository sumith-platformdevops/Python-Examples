import jenkins
class JenkinsWrapper:
    def getJobs(self):
        jenkins_server = jenkins.Jenkins('http://jenkins:8080/')
        print(jenkins_server.jobs_count())
        my_job = jenkins_server.get_job_config('Chef_Deploy')
        print(my_job)
