
import os
import logging as logger


class MainConfigs:


    URL_CONFIGS = {
        "dev": {
            "base_url": "http:/dev.localhost:8888/localdemostore/"
        },
        "test": {
            "base_url": "http://localhost:8888/localdemostore/"
        },
        "staging": {
        },
        "prod": {
        }
    }
    DB_CONFIGS = {
          "dev": {
              "base_url": "http:/dev.localhost:8888/localdemostore/"
          },
          "test": {
              "db_host": "localhost",
              "port": 8889,
              "database": "localdemostore",
              "table_prefix": "wp_"
          },
          "staging": {
          },
          "prod": {
          }
    }


    @staticmethod
    def get_base_url():
        base_url = os.environ.get('BASE_URL')
        if not base_url:
            environment = os.environ.get('ENV', 'test')
            return MainConfigs.URL_CONFIGS[environment.lower()]['base_url']
        else:
            return base_url


    @staticmethod
    def get_db_configs():
        environment = os.environ.get('ENV', 'test')
        db_configs = MainConfigs.DB_CONFIGS[environment.lower()]
        DB_PORT_OVERRIDE = os.environ.get("DB_PORT_OVERRIDE")
        DB_HOST_OVERRIDE = os.environ.get("DB_HOST_OVERRIDE")
        DB_DATABASE_OVERRIDE = os.environ.get("DB_DATABASE_OVERRIDE")
        DB_TABLE_PREFIX_OVERRIDE = os.environ.get("DB_TABLE_PREFIX_OVERRIDE")

        if DB_PORT_OVERRIDE:
            db_configs['port'] = int(DB_PORT_OVERRIDE)
        if DB_HOST_OVERRIDE:
            db_configs['db_host'] = DB_HOST_OVERRIDE
        if DB_DATABASE_OVERRIDE:
            db_configs['database'] = DB_DATABASE_OVERRIDE
        if DB_TABLE_PREFIX_OVERRIDE:
            db_configs['table_prefix'] = DB_TABLE_PREFIX_OVERRIDE
        logger.info("ppppppppppp")
        logger.info(db_configs)
        logger.info("ppppppppppp")
        return db_configs

    @staticmethod
    def get_coupon_code(filter):
        if filter.upper() == 'FREE_COUPON':
            return 'SSQA100'
        else:
            raise Exception(f"Unknown value for parameter 'filter'. filter={filter}")