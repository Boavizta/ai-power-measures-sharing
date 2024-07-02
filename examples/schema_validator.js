
// Node.js require:
const Ajv = require("ajv-draft-04")

const ajv = new Ajv({schemas: []})

// If you want to use both draft-04 and draft-06/07 schemas:
// var ajv = new Ajv({schemaId: 'auto'});
const algoSchema = require("../model/algorithm_schema.json")

const schema = require("../model/report_schema.json")

const data = require("./energy-report-example1.json")

const validate = ajv.addSchema(algoSchema).compile(schema)
  
const valid = validate(data)
console.log(valid)
if (!valid) console.log(validate.errors)