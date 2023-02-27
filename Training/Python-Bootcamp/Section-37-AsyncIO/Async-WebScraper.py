import asyncio
import aiofiles
import aiohttp
import asyncssh


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        html = await response.text()
        return html


async def write_to_file(file, text):
    async with aiofiles.open(file, 'w') as f:
        await f.write(text)


async def main(urls):
    tasks = []
    for url in urls:
        file = f'{url.split("//")[-1]}.txt'
        html = await fetch(url)
        tasks.append(write_to_file(file, html))

    await asyncio.gather(*tasks)


urls = ('https://python.org', 'https://stackoverflow.com', 'https://google.com')


# asyncio.run(main(urls))


# running commands
async def run(cmd):
    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    print(f'{cmd} exited with status code: {proc.returncode}]')
    if stdout:
        print(f'STDOUT:\n{stdout.decode()}')

    if stderr:
        print(f'STDERROR:\n{stderr.decode()}')


async def main(commads):
    tasks = []
    for cmd in commads:
        tasks.append(run(cmd))
    await asyncio.gather(*tasks)


commands = ('ipconfig', 'dir', 'route', 'ping -n 20 -c 127.0.0.1')


# asyncio.run(main(commands))

# async ssh

async def conn_run(host, uname, passwd, cmd):
    async with asyncssh.connect(host=host, username=uname, password=passwd, known_hosts=None) as connection:
        res = await connection.run(cmd)
        return res


cmd = 'ipconfig'
result = asyncio.run(conn_run('127.0.0.1', 'test', 'test', cmd))
print(f'{result.stdout}')
print(f'{result.stderr}')


# ssh devices
async def run_client(host, username, password, command):
    async with asyncssh.connect(host=host, username=username, password=password, known_hosts=None) as connection:
        return await connection.run(command)


async def run_multiple_clients(hosts):
    tasks = list()
    for host in hosts:
        task = run_client(host['host'], host['username'], host['password'], host['command'])
        tasks.append(task)
    results = await asyncio.gather(*tasks, return_exceptions=True)

    i = 0
    for result in results:
        i += 1
        if isinstance(result, Exception):
            print(f'Task {i} failed: {str(result)}')
        elif result.exit_status != 0:
            print(f'Task {i} exited with status {result.exit_status}:')
            print(result.stderr, end='')
        else:
            print(f'Task {i} succeeded:')
            print(result.stdout, end='')

        print(50 * '#')


hosts = [
    {'host': '192.168.0.105', 'username': 'u1', 'password': 'test123', 'command': 'ifconfig'},
    {'host': '192.168.0.105', 'username': 'u1', 'password': 'test123', 'command': 'whox -a'},
    {'host': '192.168.0.105', 'username': 'u1', 'password': 'test1234', 'command': 'uname -a'}
]

asyncio.run(run_multiple_clients(hosts))
