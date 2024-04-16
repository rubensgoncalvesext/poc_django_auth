"""Module to define custom Django Test Runner"""
from typing import Any, List, Tuple

from django.db.backends.base.base import BaseDatabaseWrapper
from django.test.runner import DiscoverRunner


class CustomTestRunner(DiscoverRunner):
    def setup_databases(
        self, **kwargs: Any
    ) -> List[Tuple[BaseDatabaseWrapper, str, bool]]:
        """Overwrite setup-databases to avoid create a test one, it will use
        the current default db"""

    def teardown_databases(
        self, old_config: List[Tuple[BaseDatabaseWrapper, str, bool]], **kwargs: Any
    ) -> None:
        """Overwrite method since no database will be setud before hand"""
