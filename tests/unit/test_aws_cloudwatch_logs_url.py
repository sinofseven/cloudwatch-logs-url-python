from dataclasses import dataclass

import pytest

from aws_cloudwatch_logs_url import create_url_log_group, create_url_log_events


@dataclass(frozen=True)
class Text:
    value: str


class TestCreateUrlLogGroup:
    @pytest.mark.parametrize(
        "option, expected",
        [
            (
                {
                    "region": "ap-northeast-1",
                    "log_group_name": "/aws/lambda/luciferous-devio-index-cl-FunctionCheckIndividualS-qNWf7JYCZBBM",
                },
                Text(
                    "https://ap-northeast-1.console.aws.amazon.com/cloudwatch/home?region=ap-northeast-1#logsV2:log-groups/log-group/$252Faws$252Flambda$252Fluciferous-devio-index-cl-FunctionCheckIndividualS-qNWf7JYCZBBM"
                ),
            )
        ],
    )
    def test_normal(self, option, expected: Text):
        actual = create_url_log_group(**option)
        assert actual == expected.value


class TestCreateUrlLogStream:
    @pytest.mark.parametrize(
        "option, expected",
        [
            (
                {
                    "region": "ap-northeast-1",
                    "log_group_name": "/aws/lambda/luciferous-devio-index-cl-FunctionCheckIndividualS-qNWf7JYCZBBM",
                    "log_stream_name": "2024/06/30/[39]3ca88f3a2fff4810b2de52cf027d0a40",
                    "start": 1719759600000,
                    "end": 1722437999000,
                    "filter_pattern": '{ $.level = "DEBUG" }',
                },
                Text(
                    "https://ap-northeast-1.console.aws.amazon.com/cloudwatch/home?region=ap-northeast-1#logsV2:log-groups/log-group/$252Faws$252Flambda$252Fluciferous-devio-index-cl-FunctionCheckIndividualS-qNWf7JYCZBBM/log-events/2024$252F06$252F30$252F$255B39$255D3ca88f3a2fff4810b2de52cf027d0a40$3FfilterPattern$3D$257B$2B$2524.level$2B$253D$2B$2522DEBUG$2522$2B$257D$26start$3D1719759600000$26end$3D1722437999000"
                ),
            ),
            (
                {
                    "region": "ap-northeast-1",
                    "log_group_name": "/aws/lambda/luciferous-devio-index-cl-FunctionCheckIndividualS-qNWf7JYCZBBM",
                    "log_stream_name": "2024/06/30/[39]3ca88f3a2fff4810b2de52cf027d0a40",
                    "start": 1719759600000,
                    "end": 1722437999000,
                },
                Text(
                    "https://ap-northeast-1.console.aws.amazon.com/cloudwatch/home?region=ap-northeast-1#logsV2:log-groups/log-group/$252Faws$252Flambda$252Fluciferous-devio-index-cl-FunctionCheckIndividualS-qNWf7JYCZBBM/log-events/2024$252F06$252F30$252F$255B39$255D3ca88f3a2fff4810b2de52cf027d0a40$3Fstart$3D1719759600000$26end$3D1722437999000"
                ),
            ),
            (
                {
                    "region": "ap-northeast-1",
                    "log_group_name": "/aws/lambda/luciferous-devio-index-cl-FunctionCheckIndividualS-qNWf7JYCZBBM",
                    "log_stream_name": "2024/06/30/[39]3ca88f3a2fff4810b2de52cf027d0a40",
                    "start": -1800000,
                },
                Text(
                    "https://ap-northeast-1.console.aws.amazon.com/cloudwatch/home?region=ap-northeast-1#logsV2:log-groups/log-group/$252Faws$252Flambda$252Fluciferous-devio-index-cl-FunctionCheckIndividualS-qNWf7JYCZBBM/log-events/2024$252F06$252F30$252F$255B39$255D3ca88f3a2fff4810b2de52cf027d0a40$3Fstart$3D-1800000"
                ),
            ),
            (
                {
                    "region": "ap-northeast-1",
                    "log_group_name": "/aws/lambda/luciferous-devio-index-cl-FunctionCheckIndividualS-qNWf7JYCZBBM",
                    "log_stream_name": "2024/06/30/[39]3ca88f3a2fff4810b2de52cf027d0a40",
                },
                Text(
                    "https://ap-northeast-1.console.aws.amazon.com/cloudwatch/home?region=ap-northeast-1#logsV2:log-groups/log-group/$252Faws$252Flambda$252Fluciferous-devio-index-cl-FunctionCheckIndividualS-qNWf7JYCZBBM/log-events/2024$252F06$252F30$252F$255B39$255D3ca88f3a2fff4810b2de52cf027d0a40"
                ),
            ),
            (
                {
                    "region": "ap-northeast-1",
                    "log_group_name": "/aws/lambda/luciferous-devio-index-cl-FunctionCheckIndividualS-qNWf7JYCZBBM",
                },
                Text(
                    "https://ap-northeast-1.console.aws.amazon.com/cloudwatch/home?region=ap-northeast-1#logsV2:log-groups/log-group/$252Faws$252Flambda$252Fluciferous-devio-index-cl-FunctionCheckIndividualS-qNWf7JYCZBBM/log-events"
                ),
            ),
        ],
    )
    def test_normal(self, option, expected: Text):
        actual = create_url_log_events(**option)
        assert actual == expected.value
