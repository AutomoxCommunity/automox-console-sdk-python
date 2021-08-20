## Generating with OpenAPI Generator
1. Install generator: `npm install -g @openapitools/openapi-generator-cli`
2. Set version of generator: `npx openapi-generator-cli version-manager set 5.2.1`
3. Generate client: `npx openapi-generator-cli generate -g python -i openapi.yaml -o ./`