# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, Callable, Dict, IO, Optional, Type, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._activity_runs_operations import build_query_by_pipeline_run_request

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ActivityRunsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.datafactory.aio.DataFactoryManagementClient`'s
        :attr:`activity_runs` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def query_by_pipeline_run(
        self,
        resource_group_name: str,
        factory_name: str,
        run_id: str,
        filter_parameters: _models.RunFilterParameters,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ActivityRunsQueryResponse:
        """Query activity runs based on input filter conditions.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param run_id: The pipeline run identifier. Required.
        :type run_id: str
        :param filter_parameters: Parameters to filter the activity runs. Required.
        :type filter_parameters: ~azure.mgmt.datafactory.models.RunFilterParameters
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ActivityRunsQueryResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ActivityRunsQueryResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def query_by_pipeline_run(
        self,
        resource_group_name: str,
        factory_name: str,
        run_id: str,
        filter_parameters: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ActivityRunsQueryResponse:
        """Query activity runs based on input filter conditions.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param run_id: The pipeline run identifier. Required.
        :type run_id: str
        :param filter_parameters: Parameters to filter the activity runs. Required.
        :type filter_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ActivityRunsQueryResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ActivityRunsQueryResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def query_by_pipeline_run(
        self,
        resource_group_name: str,
        factory_name: str,
        run_id: str,
        filter_parameters: Union[_models.RunFilterParameters, IO[bytes]],
        **kwargs: Any
    ) -> _models.ActivityRunsQueryResponse:
        """Query activity runs based on input filter conditions.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param run_id: The pipeline run identifier. Required.
        :type run_id: str
        :param filter_parameters: Parameters to filter the activity runs. Is either a
         RunFilterParameters type or a IO[bytes] type. Required.
        :type filter_parameters: ~azure.mgmt.datafactory.models.RunFilterParameters or IO[bytes]
        :return: ActivityRunsQueryResponse or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ActivityRunsQueryResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ActivityRunsQueryResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(filter_parameters, (IOBase, bytes)):
            _content = filter_parameters
        else:
            _json = self._serialize.body(filter_parameters, "RunFilterParameters")

        _request = build_query_by_pipeline_run_request(
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            run_id=run_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ActivityRunsQueryResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
