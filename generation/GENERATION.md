# Generating the Automox Python SDK

## Generating with OpenAPI Generator
1. Install generator: `npm install -g @openapitools/openapi-generator-cli`
2. Set version of generator: `npx openapi-generator-cli version-manager set 5.2.1`
3. Generate client: `npx openapi-generator-cli generate -g python -i ax_console.yaml -o ./`



## Failures to Generate

### components.schemas.PolicyDeviceFiltersPreview.items is missing

Update `PolicyDeviceFiltersPreview` schema within spec to define types of `value` array. Valid values are:
string, number. Example spec update:
```
                    - type: array
                      items:
                        oneOf: 
                          - type: string
                          - type: number
```

### codegenModel is null. Default to UNKNOWN_BASE_TYPE

Common issue with multiple schema types defined for response: https://github.com/OpenAPITools/openapi-generator/issues/2236

### ModuleNotFoundError: No module named 'automox_console_sdk.model.unknownbasetype'

Remove `from automox_console_sdk.model.unknownbasetype import UNKNOWNBASETYPE` from all api files in `apis` dir.

