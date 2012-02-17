# Atchai CI

## Summary
Atchai scripts and configuration related to the Jenkins CI server

## Creating a Jenkins Job

1. Your project needs to have the following structure:

    * _project root_
        * _drupal.py_
        * _fabfile.py_ - Customised version of `fabfile-example.py`
        * _public_ - Your Drupal install, you can set the name of this directory in your fabfile using the `public_path` parameter to `drupal.deploy()`
        * _test_
            * _TestSuite.html_ - A selenium test suite as created by the [Selenium IDE](http://seleniumhq.org/projects/ide/)
            * _TestXXXX.html_ - Selenium tests

2. If the server that's hosting your git repository (git server) or the stage/build server have not been used by Jenkins before you will need to perform the following ssh key setup on each server:

    1. `ssh <hostname>`
    2. `sudo su jenkins`
    3. `cat ~/.ssh/id_rsa.pub`
    4. Copy the key (output of the above command) and add to the git server
    5. `cd /tmp`
    6. `git clone <repo url>`

3. Navigate and log in to the Jenkins server

4. Click "New Job"

5. Enter a name and select "Build a free-style software project" then click "OK"

6. Under "Source Code Management" select "Git"

7. Set your repository URL (e.g. "Repository URL"). If you haven't setup jenkins with this git server before you'll need to do the following:

8. Set your branch. Usually just `master` but you can use `**` to build all branches.

9. Under "Build Triggers" select "Poll SCM"

10. Set the schedule. To poll the git for changes once a day at midnight, for example, use the following:

    `0 0 * * *`

11. Under "Build" add a new build step of type "Execute shell"

12. Set the following to deploy the test site:

    `fab -f $WORKSPACE/fabfile.py test deploy`

13. Under "Build" add a new build step of type "Execute shell"

14. Set the following to run Selenium tests (be sure to change `<test site url>`):

    `DISPLAY=":99" java -jar $JENKINS_HOME/selenium-server-standalone-2.19.0.jar -browserSessionReuse -htmlSuite *firefox <test site url> $WORKSPACE/test/TestSuite.html $WORKSPACE/seleniumhq/result.html`

15. Under "Post-build Actions" select "Publish Selenium Report"

16. Set "Test report HTMLs" to `seleniumhq/result.html`

17. Under "Post-build Actions" select "E-mail Notification"

18. Set "Recipients" as appropraite

19. Select "Send e-mail for every unstable build"

20. Click "Save"
