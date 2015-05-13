# sync snapshots and sstables to a different location

I have not tested this properly, use at your own risk, might act funky in conjunction with datastax search

Installation
------------
  python setup.py install


Usage (Note: -s must point at the actual cassandra directory, not a symlink)
------------
```
usage: snaphaven [-h] [-q] [-v {0,1,2}] [--move-snapshots] [--sync-sstables]
                 [-d [CASSANDRA_DIR]] -s SNAPSHOT_DIR [--fullsync]
                 param [param ...]

```
```
snaphaven -d /mnt/nas_drive/cassandra_backup -s /var/lib/cassandra keyspace
```

### Moving snapshots as they are being written
```
snaphaven -d /mnt/nas_drive/cassandra_backup --move-snapshots -s /var/lib/cassandra keyspace

```
### Backup all sstables
```
snaphaven -d /mnt/nas_drive/cassandra_backup --sync-sstables --fullsync -s /var/lib/cassandra keyspace
```
### upstart script
```
description "snaphaven"

start on runlevel [2345]
stop on runlevel [!2345]

respawn

exec /usr/local/bin/snaphaven keyspace1 keyspace2  -d /mnt/nas_drive/cassandra_backup
```
