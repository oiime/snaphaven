## sync snapshots and sstables to a different location

This could be useful in cases where the drive being used to store the sstables has limited space and you wish to transfer your snapshots as soon as possible to a different drive or in cases where you store your sstables on an ephemeral drive and want to backup your data into a more permanent storage.

I have not tested this properly, use at your own risk, might act funky in conjunction with datastax search

Installation
------------
```
  python setup.py install
```
or (I'd setup a pip repository later... maybe...)
```
  pip install snaphaven
```

Usage
------------
Note: -d must point at the actual cassandra directory, not a symlink
```
usage: snaphaven -s SNAPSHOT_DIR keyspace [keyspace ...]
          -h --help         help
          -v --verbosity    0=WARNING, 1=INFO, 2=DEBUG
          -q --quiet        suppress output
          -d                cassandra root directory
          --move-snapshots  move the snapshots instead of copying
          --sync-sstables   also copy the sstables, not just the snapshots
          --fullsync        start by syncing the existing directory tree

```
#### Watch keyspace `keyspace` for new snapshots and copy them
```
snaphaven -s /mnt/nas_drive/cassandra_backup -s /var/lib/cassandra keyspace
```

#### Move snapshots as they are being written
```
snaphaven -s /mnt/nas_drive/cassandra_backup --move-snapshots -s /var/lib/cassandra keyspace

```
#### Backup all sstables in additional to snapshots
```
snaphaven -s /mnt/nas_drive/cassandra_backup --sync-sstables --fullsync -s /var/lib/cassandra keyspace
```
#### upstart script
```
description "snaphaven"

start on runlevel [2345]
stop on runlevel [!2345]

respawn

exec /usr/local/bin/snaphaven keyspace1 keyspace2  -s /mnt/nas_drive/cassandra_backup
```
