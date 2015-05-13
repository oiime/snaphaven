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
usage: snaphaven [-h] [-q] [-v {0,1,2}] [--move-snapshots] [--sync-sstables]
                 [-d [CASSANDRA_DIR]] -s SNAPSHOT_DIR [--fullsync]
                 [--snapshot_regex SNAPSHOT_REGEX]
                 keyspace [keyspace ...]

Manage locally synced snapshots.

positional arguments:
  keyspace              Keyspaces to backup

optional arguments:
  -h, --help            show this help message and exit
  -q, --quiet           Suppress Output
  -v {0,1,2}, --verbosity {0,1,2}
                        Change output verbosity
  --move-snapshots      Move snapshots
  --sync-sstables       Sync the sstables themselves, not just the snapshots
  -d [CASSANDRA_DIR], --cassandra_dir [CASSANDRA_DIR]
                        cassandra directory
  -s SNAPSHOT_DIR, --snapshot_dir SNAPSHOT_DIR
                        local snapshots directory
  --fullsync            Run full sync on existing files
  --snapshot_regex SNAPSHOT_REGEX
                        Limit snapshot backup to those containing regex
```

##### Watch keyspace `keyspace` for new snapshots and copy them
```
snaphaven -s /mnt/nas_drive/cassandra_backup keyspace
```

##### Only copy certian certain snapshots
```
snaphaven -s /mnt/nas_drive/cassandra_backup --snapshot_regex '^opcenter_' keyspace
```

##### Move snapshots as they are being written
```
snaphaven -s /mnt/nas_drive/cassandra_backup --move-snapshots keyspace

```
##### Backup all sstables in additional to snapshots
```
snaphaven -s /mnt/nas_drive/cassandra_backup --sync-sstables --fullsync keyspace
```
#### upstart script
```
description "snaphaven"

start on runlevel [2345]
stop on runlevel [!2345]

respawn

exec /usr/local/bin/snaphaven keyspace1 keyspace2  -s /mnt/nas_drive/cassandra_backup
```
