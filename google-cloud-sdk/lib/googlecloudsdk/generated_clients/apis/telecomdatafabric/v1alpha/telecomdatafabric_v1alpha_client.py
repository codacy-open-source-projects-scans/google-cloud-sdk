"""Generated client library for telecomdatafabric version v1alpha."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.telecomdatafabric.v1alpha import telecomdatafabric_v1alpha_messages as messages


class TelecomdatafabricV1alpha(base_api.BaseApiClient):
  """Generated client library for service telecomdatafabric version v1alpha."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://telecomdatafabric.googleapis.com/'
  MTLS_BASE_URL = 'https://telecomdatafabric.mtls.googleapis.com/'

  _PACKAGE = 'telecomdatafabric'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1alpha'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'TelecomdatafabricV1alpha'
  _URL_VERSION = 'v1alpha'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new telecomdatafabric handle."""
    url = url or self.BASE_URL
    super(TelecomdatafabricV1alpha, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_deployments = self.ProjectsLocationsDeploymentsService(self)
    self.projects_locations_fabrics = self.ProjectsLocationsFabricsService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations_publicTemplates = self.ProjectsLocationsPublicTemplatesService(self)
    self.projects_locations_templates = self.ProjectsLocationsTemplatesService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsDeploymentsService(base_api.BaseApiService):
    """Service class for the projects_locations_deployments resource."""

    _NAME = 'projects_locations_deployments'

    def __init__(self, client):
      super(TelecomdatafabricV1alpha.ProjectsLocationsDeploymentsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new Deployment in a given project and location.

      Args:
        request: (TelecomdatafabricProjectsLocationsDeploymentsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/deployments',
        http_method='POST',
        method_id='telecomdatafabric.projects.locations.deployments.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['deploymentId', 'requestId'],
        relative_path='v1alpha/{+parent}/deployments',
        request_field='deployment',
        request_type_name='TelecomdatafabricProjectsLocationsDeploymentsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single Deployment.

      Args:
        request: (TelecomdatafabricProjectsLocationsDeploymentsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/deployments/{deploymentsId}',
        http_method='DELETE',
        method_id='telecomdatafabric.projects.locations.deployments.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId'],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='TelecomdatafabricProjectsLocationsDeploymentsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single Deployment.

      Args:
        request: (TelecomdatafabricProjectsLocationsDeploymentsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Deployment) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/deployments/{deploymentsId}',
        http_method='GET',
        method_id='telecomdatafabric.projects.locations.deployments.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='TelecomdatafabricProjectsLocationsDeploymentsGetRequest',
        response_type_name='Deployment',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists Deployments in a given project and location.

      Args:
        request: (TelecomdatafabricProjectsLocationsDeploymentsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListDeploymentsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/deployments',
        http_method='GET',
        method_id='telecomdatafabric.projects.locations.deployments.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/deployments',
        request_field='',
        request_type_name='TelecomdatafabricProjectsLocationsDeploymentsListRequest',
        response_type_name='ListDeploymentsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the parameters of a single Deployment.

      Args:
        request: (TelecomdatafabricProjectsLocationsDeploymentsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/deployments/{deploymentsId}',
        http_method='PATCH',
        method_id='telecomdatafabric.projects.locations.deployments.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId', 'updateMask'],
        relative_path='v1alpha/{+name}',
        request_field='deployment',
        request_type_name='TelecomdatafabricProjectsLocationsDeploymentsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Preview(self, request, global_params=None):
      r"""Gets View of a Deployment.

      Args:
        request: (TelecomdatafabricProjectsLocationsDeploymentsPreviewRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DeploymentView) The response message.
      """
      config = self.GetMethodConfig('Preview')
      return self._RunMethod(
          config, request, global_params=global_params)

    Preview.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/deployments:preview',
        http_method='POST',
        method_id='telecomdatafabric.projects.locations.deployments.preview',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1alpha/{+parent}/deployments:preview',
        request_field='createDeploymentRequest',
        request_type_name='TelecomdatafabricProjectsLocationsDeploymentsPreviewRequest',
        response_type_name='DeploymentView',
        supports_download=False,
    )

  class ProjectsLocationsFabricsService(base_api.BaseApiService):
    """Service class for the projects_locations_fabrics resource."""

    _NAME = 'projects_locations_fabrics'

    def __init__(self, client):
      super(TelecomdatafabricV1alpha.ProjectsLocationsFabricsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new Fabric in a given project and location.

      Args:
        request: (TelecomdatafabricProjectsLocationsFabricsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/fabrics',
        http_method='POST',
        method_id='telecomdatafabric.projects.locations.fabrics.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['fabricId', 'requestId'],
        relative_path='v1alpha/{+parent}/fabrics',
        request_field='fabric',
        request_type_name='TelecomdatafabricProjectsLocationsFabricsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single Fabric.

      Args:
        request: (TelecomdatafabricProjectsLocationsFabricsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/fabrics/{fabricsId}',
        http_method='DELETE',
        method_id='telecomdatafabric.projects.locations.fabrics.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId'],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='TelecomdatafabricProjectsLocationsFabricsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single Fabric.

      Args:
        request: (TelecomdatafabricProjectsLocationsFabricsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Fabric) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/fabrics/{fabricsId}',
        http_method='GET',
        method_id='telecomdatafabric.projects.locations.fabrics.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='TelecomdatafabricProjectsLocationsFabricsGetRequest',
        response_type_name='Fabric',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists Fabrics in a given project and location.

      Args:
        request: (TelecomdatafabricProjectsLocationsFabricsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListFabricsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/fabrics',
        http_method='GET',
        method_id='telecomdatafabric.projects.locations.fabrics.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/fabrics',
        request_field='',
        request_type_name='TelecomdatafabricProjectsLocationsFabricsListRequest',
        response_type_name='ListFabricsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the parameters of a single Fabric.

      Args:
        request: (TelecomdatafabricProjectsLocationsFabricsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/fabrics/{fabricsId}',
        http_method='PATCH',
        method_id='telecomdatafabric.projects.locations.fabrics.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId', 'updateMask'],
        relative_path='v1alpha/{+name}',
        request_field='fabric',
        request_type_name='TelecomdatafabricProjectsLocationsFabricsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(TelecomdatafabricV1alpha.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

      Args:
        request: (TelecomdatafabricProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='telecomdatafabric.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='TelecomdatafabricProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (TelecomdatafabricProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='telecomdatafabric.projects.locations.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='TelecomdatafabricProjectsLocationsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (TelecomdatafabricProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='telecomdatafabric.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='TelecomdatafabricProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

      Args:
        request: (TelecomdatafabricProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='telecomdatafabric.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+name}/operations',
        request_field='',
        request_type_name='TelecomdatafabricProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsPublicTemplatesService(base_api.BaseApiService):
    """Service class for the projects_locations_publicTemplates resource."""

    _NAME = 'projects_locations_publicTemplates'

    def __init__(self, client):
      super(TelecomdatafabricV1alpha.ProjectsLocationsPublicTemplatesService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets details of a single PublicTemplate.

      Args:
        request: (TelecomdatafabricProjectsLocationsPublicTemplatesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PublicTemplate) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/publicTemplates/{publicTemplatesId}',
        http_method='GET',
        method_id='telecomdatafabric.projects.locations.publicTemplates.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='TelecomdatafabricProjectsLocationsPublicTemplatesGetRequest',
        response_type_name='PublicTemplate',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists PublicTemplates in a given project and location.

      Args:
        request: (TelecomdatafabricProjectsLocationsPublicTemplatesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListPublicTemplatesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/publicTemplates',
        http_method='GET',
        method_id='telecomdatafabric.projects.locations.publicTemplates.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/publicTemplates',
        request_field='',
        request_type_name='TelecomdatafabricProjectsLocationsPublicTemplatesListRequest',
        response_type_name='ListPublicTemplatesResponse',
        supports_download=False,
    )

  class ProjectsLocationsTemplatesService(base_api.BaseApiService):
    """Service class for the projects_locations_templates resource."""

    _NAME = 'projects_locations_templates'

    def __init__(self, client):
      super(TelecomdatafabricV1alpha.ProjectsLocationsTemplatesService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets details of a single Template.

      Args:
        request: (TelecomdatafabricProjectsLocationsTemplatesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Template) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/templates/{templatesId}',
        http_method='GET',
        method_id='telecomdatafabric.projects.locations.templates.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='TelecomdatafabricProjectsLocationsTemplatesGetRequest',
        response_type_name='Template',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists Templates in a given project and location.

      Args:
        request: (TelecomdatafabricProjectsLocationsTemplatesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListTemplatesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/templates',
        http_method='GET',
        method_id='telecomdatafabric.projects.locations.templates.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+parent}/templates',
        request_field='',
        request_type_name='TelecomdatafabricProjectsLocationsTemplatesListRequest',
        response_type_name='ListTemplatesResponse',
        supports_download=False,
    )

    def Parse(self, request, global_params=None):
      r"""Parses a custom template will parse custom template create by user and will return template specification.

      Args:
        request: (TelecomdatafabricProjectsLocationsTemplatesParseRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TemplateSpec) The response message.
      """
      config = self.GetMethodConfig('Parse')
      return self._RunMethod(
          config, request, global_params=global_params)

    Parse.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}/templates:parse',
        http_method='POST',
        method_id='telecomdatafabric.projects.locations.templates.parse',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1alpha/{+parent}/templates:parse',
        request_field='parseTemplateSpecRequest',
        request_type_name='TelecomdatafabricProjectsLocationsTemplatesParseRequest',
        response_type_name='TemplateSpec',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(TelecomdatafabricV1alpha.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (TelecomdatafabricProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='telecomdatafabric.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha/{+name}',
        request_field='',
        request_type_name='TelecomdatafabricProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (TelecomdatafabricProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha/projects/{projectsId}/locations',
        http_method='GET',
        method_id='telecomdatafabric.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha/{+name}/locations',
        request_field='',
        request_type_name='TelecomdatafabricProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(TelecomdatafabricV1alpha.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }