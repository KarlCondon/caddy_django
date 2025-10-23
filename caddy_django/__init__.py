"""Project package initialization.

Enable PyMySQL as a drop-in replacement for MySQLdb when available. This keeps
the project compatible with environments where the native `mysqlclient` binary
is not installed.
"""

try:
    import pymysql  # type: ignore

    pymysql.install_as_MySQLdb()
except Exception:
    # If PyMySQL isn't installed, silently continue. Django will attempt to
    # use mysqlclient if configured for MySQL, or another backend as set.
    pass
