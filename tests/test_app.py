from .context import kafka_cli
import pytest

def test_app(capsys):
    # pylint: disable=W0612,W0613
    kafka_cli.Kafka.run()
    captured = capsys.readouterr()

    assert "Started building the Kakfa CLI" in captured.out