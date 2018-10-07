# lambda-git
A git binary installed through PyPI for AWS Lambda - inspired by the JavaScript package [lambda-git](https://github.com/pimterry/lambda-git) and backported to Python.

To use this, just require it and call `exec_command`. E.g:

```python
import git

git.exec_command('init')
```

## Executing commands in a specific path:

AWS Lambda give you only `/tmp` as working directory. This package by default will execute all commands in `/tmp`, but it can be overridden by passing `cwd`.

```python
import git

new_repo_path = '/tmp/my-new-repo'
os.mkdir(new_repo_path)
git.exec_command('init', cwd=new_repo_path)
```

## Executing commands with separate environment:

By default every git command will be executed with the system environment, but it can be overridden by setting `env`.

```python
import git

commit_env = os.environ
commit_env['GIT_AUTHOR_NAME'] = 'My Name'
commit_env['GIT_AUTHOR_EMAIL'] = 'me@email.com'
commit_env['GIT_COMMITTER_NAME'] = 'My Name'
commit_env['GIT_COMMITTER_EMAIL'] = 'me@email.com'

new_repo_path = '/tmp/my-new-repo'

git.exec_command('add', '.', cwd=new_repo_path)
git.exec_command('commit', '-m "first commit"', cwd=new_repo_path, env=commit_env)
```
