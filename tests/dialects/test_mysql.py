from simple_ddl_parser import DDLParser


def test_simple_on_update():
    ddl = """CREATE TABLE t1 (
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    dt DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);"""
    result = DDLParser(ddl).run(group_by_type=True)
    expected = {
        "tables": [
            {
                "columns": [
                    {
                        "name": "ts",
                        "type": "TIMESTAMP",
                        "size": None,
                        "references": None,
                        "unique": False,
                        "nullable": True,
                        "default": "CURRENT_TIMESTAMP",
                        "check": None,
                        "on_update": "CURRENT_TIMESTAMP",
                    },
                    {
                        "name": "dt",
                        "type": "DATETIME",
                        "size": None,
                        "references": None,
                        "unique": False,
                        "nullable": True,
                        "default": "CURRENT_TIMESTAMP",
                        "check": None,
                        "on_update": "CURRENT_TIMESTAMP",
                    },
                ],
                "primary_key": [],
                "alter": {},
                "checks": [],
                "index": [],
                "partitioned_by": [],
                "tablespace": None,
                "schema": None,
                "table_name": "t1",
            }
        ],
        "types": [],
        "sequences": [],
        "domains": [],
        "schemas": [],
        "ddl_properties": [],
    }
    assert expected == result


def test_on_update_with_fcall():
    ddl = """create table test(
    `id` bigint not null,
    `updated_at` timestamp(3) not null default current_timestamp(3) on update current_timestamp(3),
    primary key (id));"""
    result = DDLParser(ddl).run(group_by_type=True)
    expcted = {
        "domains": [],
        "schemas": [],
        "sequences": [],
        "tables": [
            {
                "alter": {},
                "checks": [],
                "columns": [
                    {
                        "check": None,
                        "default": None,
                        "name": "`id`",
                        "nullable": False,
                        "references": None,
                        "size": None,
                        "type": "bigint",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": "current_timestamp(3)",
                        "name": "`updated_at`",
                        "nullable": False,
                        "on_update": "current_timestamp(3)",
                        "references": None,
                        "size": 3,
                        "type": "timestamp",
                        "unique": False,
                    },
                ],
                "index": [],
                "partitioned_by": [],
                "primary_key": ["id"],
                "schema": None,
                "table_name": "test",
                "tablespace": None,
            }
        ],
        "ddl_properties": [],
        "types": [],
    }
    assert expcted == result


def test_default_charset():
    results = DDLParser(
        """
    CREATE TABLE t_table_records (
    id VARCHAR (255) NOT NULL,
    create_time datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
    creator VARCHAR (32) DEFAULT 'sys' NOT NULL,
    current_rows BIGINT,
    edit_time datetime DEFAULT CURRENT_TIMESTAMP NOT NULL,
    editor VARCHAR (32) DEFAULT 'sys' NOT NULL,
    managed_database_database VARCHAR (255) NOT NULL,
    managed_database_schema VARCHAR (255),
    managed_database_table VARCHAR (255) NOT NULL,
    source_database_database VARCHAR (255) NOT NULL,
    source_database_jdbc VARCHAR (255) NOT NULL,
    source_database_schema VARCHAR (255),
    source_database_table VARCHAR (255) NOT NULL,
    source_database_type VARCHAR (255) NOT NULL,
    source_rows BIGINT,
    PRIMARY KEY (id)
    ) ENGINE = INNODB DEFAULT CHARSET = utf8mb4 COMMENT = '导入元数据管理';
    """
    ).run(group_by_type=True)

    expected = {
        "ddl_properties": [],
        "domains": [],
        "schemas": [],
        "sequences": [],
        "tables": [
            {
                "ENGINE": "=",
                "alter": {},
                "authorization": "INNODB",
                "checks": [],
                "columns": [
                    {
                        "check": None,
                        "default": None,
                        "name": "id",
                        "nullable": False,
                        "references": None,
                        "size": 255,
                        "type": "VARCHAR",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": "CURRENT_TIMESTAMP",
                        "name": "create_time",
                        "nullable": False,
                        "references": None,
                        "size": None,
                        "type": "datetime",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": "'sys'",
                        "name": "creator",
                        "nullable": False,
                        "references": None,
                        "size": 32,
                        "type": "VARCHAR",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "current_rows",
                        "nullable": True,
                        "references": None,
                        "size": None,
                        "type": "BIGINT",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": "CURRENT_TIMESTAMP",
                        "name": "edit_time",
                        "nullable": False,
                        "references": None,
                        "size": None,
                        "type": "datetime",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": "'sys'",
                        "name": "editor",
                        "nullable": False,
                        "references": None,
                        "size": 32,
                        "type": "VARCHAR",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "managed_database_database",
                        "nullable": False,
                        "references": None,
                        "size": 255,
                        "type": "VARCHAR",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "managed_database_schema",
                        "nullable": True,
                        "references": None,
                        "size": 255,
                        "type": "VARCHAR",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "managed_database_table",
                        "nullable": False,
                        "references": None,
                        "size": 255,
                        "type": "VARCHAR",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "source_database_database",
                        "nullable": False,
                        "references": None,
                        "size": 255,
                        "type": "VARCHAR",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "source_database_jdbc",
                        "nullable": False,
                        "references": None,
                        "size": 255,
                        "type": "VARCHAR",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "source_database_schema",
                        "nullable": True,
                        "references": None,
                        "size": 255,
                        "type": "VARCHAR",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "source_database_table",
                        "nullable": False,
                        "references": None,
                        "size": 255,
                        "type": "VARCHAR",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "source_database_type",
                        "nullable": False,
                        "references": None,
                        "size": 255,
                        "type": "VARCHAR",
                        "unique": False,
                    },
                    {
                        "check": None,
                        "default": None,
                        "name": "source_rows",
                        "nullable": True,
                        "references": None,
                        "size": None,
                        "type": "BIGINT",
                        "unique": False,
                    },
                ],
                "comment": "'\\u5bfc\\u5165\\u5143\\u6570\\u636e\\u7ba1\\u7406'",
                "default_charset": "utf8mb4",
                "index": [],
                "partitioned_by": [],
                "primary_key": ["id"],
                "schema": None,
                "table_name": "t_table_records",
                "tablespace": None,
            }
        ],
        "types": [],
    }
    assert expected == results


def test_identity_with_properties():
    ddl = """
CREATE TABLE IF NOT EXISTS database.table_name
    (
        [cifno] [numeric](10, 0) IDENTITY(1,1) NOT NULL,
        puts (1,1) in the size field
    )
"""

    result = DDLParser(ddl).run()
    expected = [
        {
            "alter": {},
            "checks": [],
            "columns": [
                {
                    "check": None,
                    "default": None,
                    "identity": (1, 1),
                    "name": "[cifno]",
                    "nullable": False,
                    "references": None,
                    "size": (10, 0),
                    "type": "[numeric]",
                    "unique": False,
                }
            ],
            "if_not_exists": True,
            "in": "the",
            "index": [],
            "partitioned_by": [],
            "primary_key": [],
            "schema": "database",
            "size": "field",
            "table_name": "table_name",
            "tablespace": None,
        }
    ]
    assert expected == result
