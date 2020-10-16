# Protocol Documentation
<a name="top"></a>

## Table of Contents

- [olca.proto](#olca.proto)
    - [Actor](#protolca.Actor)
    - [AllocationFactor](#protolca.AllocationFactor)
    - [CalculationSetup](#protolca.CalculationSetup)
    - [Category](#protolca.Category)
    - [Currency](#protolca.Currency)
    - [DqIndicator](#protolca.DqIndicator)
    - [DqScore](#protolca.DqScore)
    - [DqSystem](#protolca.DqSystem)
    - [Exchange](#protolca.Exchange)
    - [ExchangeRef](#protolca.ExchangeRef)
    - [Flow](#protolca.Flow)
    - [FlowMap](#protolca.FlowMap)
    - [FlowMapEntry](#protolca.FlowMapEntry)
    - [FlowMapRef](#protolca.FlowMapRef)
    - [FlowProperty](#protolca.FlowProperty)
    - [FlowPropertyFactor](#protolca.FlowPropertyFactor)
    - [FlowRef](#protolca.FlowRef)
    - [FlowResult](#protolca.FlowResult)
    - [ImpactCategory](#protolca.ImpactCategory)
    - [ImpactCategoryRef](#protolca.ImpactCategoryRef)
    - [ImpactFactor](#protolca.ImpactFactor)
    - [ImpactMethod](#protolca.ImpactMethod)
    - [ImpactResult](#protolca.ImpactResult)
    - [Location](#protolca.Location)
    - [NwFactor](#protolca.NwFactor)
    - [NwSet](#protolca.NwSet)
    - [Parameter](#protolca.Parameter)
    - [ParameterRedef](#protolca.ParameterRedef)
    - [Process](#protolca.Process)
    - [ProcessDocumentation](#protolca.ProcessDocumentation)
    - [ProcessLink](#protolca.ProcessLink)
    - [ProcessRef](#protolca.ProcessRef)
    - [ProductSystem](#protolca.ProductSystem)
    - [Project](#protolca.Project)
    - [Ref](#protolca.Ref)
    - [SimpleResult](#protolca.SimpleResult)
    - [SocialAspect](#protolca.SocialAspect)
    - [SocialIndicator](#protolca.SocialIndicator)
    - [Source](#protolca.Source)
    - [Uncertainty](#protolca.Uncertainty)
    - [Unit](#protolca.Unit)
    - [UnitGroup](#protolca.UnitGroup)
  
    - [AllocationType](#protolca.AllocationType)
    - [CalculationType](#protolca.CalculationType)
    - [FlowPropertyType](#protolca.FlowPropertyType)
    - [FlowType](#protolca.FlowType)
    - [ModelType](#protolca.ModelType)
    - [ParameterScope](#protolca.ParameterScope)
    - [ProcessType](#protolca.ProcessType)
    - [RiskLevel](#protolca.RiskLevel)
    - [UncertaintyType](#protolca.UncertaintyType)
  
- [services.proto](#services.proto)
    - [ModelService](#protolca.services.ModelService)
  
- [Scalar Value Types](#scalar-value-types)



<a name="olca.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## olca.proto



<a name="protolca.Actor"></a>

### Actor
An actor is a person or organisation.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| category | [Ref](#protolca.Ref) |  | The category of the entity. |
| tags | [string](#string) | repeated | A list of optional tags. A tag is just a string which should not contain commas (and other special characters). |
| library | [string](#string) |  | If this entity is part of a library, this field contains the identifier of that library. The identifier is typically just the comination of the library name and version. |
| address | [string](#string) |  |  |
| city | [string](#string) |  |  |
| country | [string](#string) |  |  |
| email | [string](#string) |  |  |
| telefax | [string](#string) |  |  |
| telephone | [string](#string) |  |  |
| website | [string](#string) |  |  |
| zip_code | [string](#string) |  |  |






<a name="protolca.AllocationFactor"></a>

### AllocationFactor
A single allocation factor in a process.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| allocation_type | [AllocationType](#protolca.AllocationType) |  | The type of allocation. |
| product | [FlowRef](#protolca.FlowRef) |  | The output product (or waste input) to which this allocation factor is related. The must be an exchange with this product output (or waste input) in this process. |
| value | [double](#double) |  | The value of the allocation factor. |
| formula | [string](#string) |  | An optional formula from which the value of the allocation factor is calculated. |
| exchange | [ExchangeRef](#protolca.ExchangeRef) |  | A product input, waste output, or elementary flow exchange which is allocated by this factor. This is only valid for causal allocation where allocation factors can be assigned to single exchanges. |






<a name="protolca.CalculationSetup"></a>

### CalculationSetup
A setup for a product system calculation.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| calculation_type | [CalculationType](#protolca.CalculationType) |  | The type of calculation that should be performed. |
| product_system | [Ref](#protolca.Ref) |  | The product system that should be calculated (required). |
| impact_method | [Ref](#protolca.Ref) |  | The LCIA method for the calculation (optional). |
| with_costs | [bool](#bool) |  | Indicates whether life cycle costs should be also calculated (optional). |
| nw_set | [Ref](#protolca.Ref) |  | The normalisation and weighting set for the calculation (optional). |
| allocation_method | [AllocationType](#protolca.AllocationType) |  | The calculation type to be used in the calculation (optional). |
| parameter_redefs | [ParameterRedef](#protolca.ParameterRedef) | repeated | A list of parameter redefinitions to be used in the calculation (optional). |
| amount | [double](#double) |  | (optional) |
| unit | [Ref](#protolca.Ref) |  | (optional) |
| flow_property | [Ref](#protolca.Ref) |  | (optional) |






<a name="protolca.Category"></a>

### Category
A category is used for the categorisation of types like processes, flows,
etc. The tricky thing is that the `Category` class inherits also from the
[CategorizedEntity] type so that a category can have a category attribute
which is then the parent category of this category (uff).


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| category | [Ref](#protolca.Ref) |  | The category of the entity. |
| tags | [string](#string) | repeated | A list of optional tags. A tag is just a string which should not contain commas (and other special characters). |
| library | [string](#string) |  | If this entity is part of a library, this field contains the identifier of that library. The identifier is typically just the comination of the library name and version. |
| model_type | [ModelType](#protolca.ModelType) |  | The type of models that can be linked to the category. |






<a name="protolca.Currency"></a>

### Currency



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| category | [Ref](#protolca.Ref) |  | The category of the entity. |
| tags | [string](#string) | repeated | A list of optional tags. A tag is just a string which should not contain commas (and other special characters). |
| library | [string](#string) |  | If this entity is part of a library, this field contains the identifier of that library. The identifier is typically just the comination of the library name and version. |
| code | [string](#string) |  |  |
| conversion_factor | [double](#double) |  |  |
| reference_currency | [Ref](#protolca.Ref) |  |  |






<a name="protolca.DqIndicator"></a>

### DqIndicator
An indicator of a data quality system ([DqSystem]).


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| name | [string](#string) |  |  |
| position | [int32](#int32) |  |  |
| scores | [DqScore](#protolca.DqScore) | repeated |  |






<a name="protolca.DqScore"></a>

### DqScore
An score value of an indicator ([DqIndicator]) in a data quality system
([DqSystem]).


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| position | [int32](#int32) |  |  |
| label | [string](#string) |  |  |
| description | [string](#string) |  |  |
| uncertainty | [double](#double) |  |  |






<a name="protolca.DqSystem"></a>

### DqSystem
A data quality system (DQS) in openLCA describes a pedigree matrix of $m$
data quality indicators (DQIs) and $n$ data quality scores (DQ scores). Such
a system can then be used to assess the data quality of processes and
exchanges by tagging them with an instance of the system $D$ where $D$ is a
$m * n$ matrix with an entry $d_{ij}$ containing the value of the data
quality score $j$ for indicator $i$. As each indicator in $D$ can only have
a single score value, $D$ can be stored in a vector $d$ where $d_i$ contains
the data quality score for indicator $i$. The possible values of the data
quality scores are defined as a linear order $1 \dots n$. In openLCA, the
data quality entry $d$ of a process or exchange is stored as a string like
`(3;2;4;n.a.;2)` which means the data quality score for the first indicator
is `3`, for the second `2` etc. A specific value is `n.a.` which stands for
_not applicable_. In calculations, these data quality entries can be
aggregated in different ways. For example, the data quality entry of a flow
$f$ with a contribution of `0.5 kg` and a data quality entry of
`(3;2;4;n.a.;2)` in a process $p$ and a contribution of `1.5 kg` and a data
quality entry of `(2;3;1;n.a.;5)` in a process $q$ could be aggregated to
`(2;3;2;n.a.;4)` by applying an weighted average and rounding. Finally,
custom labels like `A, B, C, ...` or `Very good, Good, Fair, ...` for the DQ
scores can be assigned by the user. These labels are then displayed instead
of `1, 2, 3 ...` in the user interface or result exports. However,
internally the numeric values are used in the data model and calculations.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| category | [Ref](#protolca.Ref) |  | The category of the entity. |
| tags | [string](#string) | repeated | A list of optional tags. A tag is just a string which should not contain commas (and other special characters). |
| library | [string](#string) |  | If this entity is part of a library, this field contains the identifier of that library. The identifier is typically just the comination of the library name and version. |
| has_uncertainties | [bool](#bool) |  |  |
| source | [Ref](#protolca.Ref) |  |  |
| indicators | [DqIndicator](#protolca.DqIndicator) | repeated |  |






<a name="protolca.Exchange"></a>

### Exchange
An Exchange is an input or output of a [Flow] in a [Process]. The amount of
an exchange is given in a specific unit of a quantity ([FlowProperty]) of
the flow. The allowed units and flow properties that can be used for a flow
in an exchange are defined by the flow property information in that flow
(see also the [FlowPropertyFactor] type).


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| avoided_product | [bool](#bool) |  | Indicates whether this exchange is an avoided product. |
| cost_formula | [string](#string) |  | A formula for calculating the costs of this exchange. |
| cost_value | [double](#double) |  | The costs of this exchange. |
| currency | [Ref](#protolca.Ref) |  | The currency in which the costs of this exchange are given. |
| internal_id | [int32](#int32) |  | The process internal ID of the exchange. This is used to identify exchanges unambiguously within a process (e.g. when linking exchanges in a product system where multiple exchanges with the same flow are allowed). The value should be &gt;= 1. |
| flow | [FlowRef](#protolca.FlowRef) |  | The reference to the flow of the exchange. |
| flow_property | [Ref](#protolca.Ref) |  | The quantity in which the amount is given. |
| input | [bool](#bool) |  |  |
| quantitative_reference | [bool](#bool) |  | Indicates whether the exchange is the quantitative reference of the process. |
| base_uncertainty | [double](#double) |  |  |
| default_provider | [ProcessRef](#protolca.ProcessRef) |  | A default provider is a [Process] that is linked as the provider of a product input or the waste treatment provider of a waste output. It is just an optional default setting which can be also ignored when building product systems in openLCA. The user is always free to link processes in product systems ignoring these defaults (but the flows and flow directions have to match of course). |
| amount | [double](#double) |  |  |
| amount_formula | [string](#string) |  |  |
| unit | [Ref](#protolca.Ref) |  |  |
| dq_entry | [string](#string) |  | A data quality entry like `(1;3;2;5;1)`. The entry is a vector of data quality values that need to match the data quality scheme for flow inputs and outputs that is assigned to the [Process]. In such a scheme the data quality indicators have fixed positions and the respective values in the `dqEntry` vector map to these positions. |
| uncertainty | [Uncertainty](#protolca.Uncertainty) |  |  |
| description | [string](#string) |  | A general comment about the input or output. |






<a name="protolca.ExchangeRef"></a>

### ExchangeRef
An instance of this class describes a reference to an exchange in a process.
When we reference such an exchange we only need the information to indentify
that exchange unambiguously in a process.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| internal_id | [int32](#int32) |  | The internal ID of the exchange. |






<a name="protolca.Flow"></a>

### Flow
Everything that can be an input or output of a process (e.g. a substance, a
product, a waste, a service etc.)


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| category | [Ref](#protolca.Ref) |  | The category of the entity. |
| tags | [string](#string) | repeated | A list of optional tags. A tag is just a string which should not contain commas (and other special characters). |
| library | [string](#string) |  | If this entity is part of a library, this field contains the identifier of that library. The identifier is typically just the comination of the library name and version. |
| flow_type | [FlowType](#protolca.FlowType) |  | The type of the flow. Note that this type is more a descriptor of how the flow is handled in calculations. |
| cas | [string](#string) |  | A CAS number of the flow. |
| formula | [string](#string) |  | A chemical formula of the flow. |
| flow_properties | [FlowPropertyFactor](#protolca.FlowPropertyFactor) | repeated | The flow properties (quantities) in which amounts of the flow can be expressed together with conversion factors between these flow flow properties. |
| location | [Ref](#protolca.Ref) |  | The location of the flow. Normally the location of a flow is defined by the process location where the flow is an input or output. However, some data formats define a location as a property of a flow. |
| synonyms | [string](#string) |  | A list of synonyms but packed into a single field. Best is to use semicolons as separator as commas are sometimes used in names of chemicals. |
| infrastructure_flow | [bool](#bool) |  | Indicates whether this flow describes an infrastructure product. This field is part of the openLCA schema because of backward compatibility with EcoSpold 1. It does not really have a meaning in openLCA and should not be used anymore. |






<a name="protolca.FlowMap"></a>

### FlowMap
A crosswalk of flows from a source flow list to a target flow list.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| source | [Ref](#protolca.Ref) |  | The reference (id, name, description) of the source flow list. |
| target | [Ref](#protolca.Ref) |  | The reference (id, name, description) of the target flow list. |
| mappings | [FlowMapEntry](#protolca.FlowMapEntry) | repeated | A list of flow mappings from flows in a source flow list to flows in a target flow list. |






<a name="protolca.FlowMapEntry"></a>

### FlowMapEntry
A mapping from one flow to another.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| from | [FlowMapRef](#protolca.FlowMapRef) |  | The flow, flow property, and unit of the source flow. |
| to | [FlowMapRef](#protolca.FlowMapRef) |  | The flow, flow property, and unit of the target flow. |
| conversion_factor | [double](#double) |  | The factor to convert the original source flow to the target flow. |






<a name="protolca.FlowMapRef"></a>

### FlowMapRef
Describes a the source or target flow of a flow mapping in a `FlowMap`. Such
a flow reference can also optionally specify the unit and flow property
(quantity) for which the mapping is valid. If the unit and quantity are not
given, the mapping is based on the reference unit of the reference flow
property of the respective flow.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| flow | [FlowRef](#protolca.FlowRef) |  | The reference to the flow data set. |
| flow_property | [Ref](#protolca.Ref) |  | An optional reference to a flow property of the flow for which the mapping is valid. |
| unit | [Ref](#protolca.Ref) |  | An optional reference to a unit of the flow for which the mapping is valid |






<a name="protolca.FlowProperty"></a>

### FlowProperty
A flow property is a quantity that can be used to express amounts of a flow.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| category | [Ref](#protolca.Ref) |  | The category of the entity. |
| tags | [string](#string) | repeated | A list of optional tags. A tag is just a string which should not contain commas (and other special characters). |
| library | [string](#string) |  | If this entity is part of a library, this field contains the identifier of that library. The identifier is typically just the comination of the library name and version. |
| flow_property_type | [FlowPropertyType](#protolca.FlowPropertyType) |  | The type of the flow property |
| unit_group | [Ref](#protolca.Ref) |  | The units of measure that can be used to express quantities of the flow property. |






<a name="protolca.FlowPropertyFactor"></a>

### FlowPropertyFactor
A FlowPropertyFactor is a conversion factor between &lt;a
href=&#34;./FlowProperty.html&#34;&gt;flow properties (quantities)&lt;/a&gt; of a &lt;a
href=&#34;./Flow.html&#34;&gt;flow&lt;/a&gt;. As an example the amount of the flow &#39;water&#39; in
a process could be expressed in &#39;kg&#39; mass or &#39;m3&#39; volume. In this case the
flow water would have two flow property factors: one for the flow property
&#39;mass&#39; and one for &#39;volume&#39;. Each of these flow properties has a reference
to a &lt;a href=&#34;./UnitGroup.html&#34;&gt;unit group&lt;/a&gt; which again has a reference
unit. In the example the flow property &#39;mass&#39; could reference the unit group
&#39;units of mass&#39; with &#39;kg&#39; as reference unit and volume could reference the
unit group &#39;units of volume&#39; with &#39;m3&#39; as reference unit. The flow property
factor is now the conversion factor between these two reference units where
the factor of the reference flow property of the flow is 1. If the reference
flow property of &#39;water&#39; in the example would be &#39;mass&#39; the respective flow
property factor would be 1 and the factor for &#39;volume&#39; would be 0.001 (as 1
kg water is 0.001 m3). The amount of water in a process can now be also
given in liter, tons, grams etc. For this, the unit conversion factor of the
respective unit group can be used to convert into the reference unit (which
then can be used to convert to the reference unit of another flow property).
Another thing to note is that different flow properties can refer to the
same unit group (e.g. MJ upper calorific value and MJ lower calorific
value.)


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| flow_property | [Ref](#protolca.Ref) |  | The flow property (quantity) of the factor. |
| conversion_factor | [double](#double) |  | The value of the conversion factor. |
| reference_flow_property | [bool](#bool) |  | Indicates whether the flow property of the factor is the reference flow property of the flow. The reference flow property must have a conversion factor of 1.0 and there should be only one reference flow property. |






<a name="protolca.FlowRef"></a>

### FlowRef
A reference to a [Flow] data set.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| category_path | [string](#string) | repeated | The full path of the category of the referenced entity from top to bottom, e.g. `&#34;Elementary flows&#34;, &#34;Emissions to air&#34;, &#34;unspecified&#34;`. |
| ref_unit | [string](#string) |  | The name (symbol) of the reference unit of the flow. |
| location | [string](#string) |  | The location name or code of the flow. Typically, this is only used for product flows in databases like ecoinvent. |
| flow_type | [FlowType](#protolca.FlowType) |  | The type of the flow. |






<a name="protolca.FlowResult"></a>

### FlowResult
A result value for a flow; given in the reference unit of the flow.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| flow | [FlowRef](#protolca.FlowRef) |  | The flow reference. |
| input | [bool](#bool) |  | Indicates whether the flow is an input or not. |
| value | [double](#double) |  | The value of the flow amount. |






<a name="protolca.ImpactCategory"></a>

### ImpactCategory



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| category | [Ref](#protolca.Ref) |  | The category of the entity. |
| tags | [string](#string) | repeated | A list of optional tags. A tag is just a string which should not contain commas (and other special characters). |
| library | [string](#string) |  | If this entity is part of a library, this field contains the identifier of that library. The identifier is typically just the comination of the library name and version. |
| reference_unit_name | [string](#string) |  | The name of the reference unit of the LCIA category (e.g. kg CO2-eq.). |
| parameters | [Parameter](#protolca.Parameter) | repeated | A set of parameters which can be used in formulas of the characterisation factors in this impact category. |
| impact_factors | [ImpactFactor](#protolca.ImpactFactor) | repeated | The characterisation factors of the LCIA category. |






<a name="protolca.ImpactCategoryRef"></a>

### ImpactCategoryRef
A reference to a [ImpactCategory] data set.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| category_path | [string](#string) | repeated | The full path of the category of the referenced entity from top to bottom, e.g. `&#34;Elementary flows&#34;, &#34;Emissions to air&#34;, &#34;unspecified&#34;`. |
| ref_unit | [string](#string) |  | The name (symbol) of the reference unit of the impact category. |






<a name="protolca.ImpactFactor"></a>

### ImpactFactor
A single characterisation factor of a LCIA category for a flow.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| flow | [FlowRef](#protolca.FlowRef) |  | The [Flow] of the impact assessment factor. |
| location | [Ref](#protolca.Ref) |  | In case of a regionalized impact category, this field can contain the location for which this factor is valid. |
| flow_property | [Ref](#protolca.Ref) |  | The quantity of the flow to which the LCIA factor is related (e.g. Mass). |
| unit | [Ref](#protolca.Ref) |  | The flow unit to which the LCIA factor is related (e.g. kg). |
| value | [double](#double) |  | The value of the impact assessment factor. |
| formula | [string](#string) |  | A mathematical formula for calculating the value of the LCIA factor. |
| uncertainty | [Uncertainty](#protolca.Uncertainty) |  | The uncertainty distribution of the factors&#39; value. |






<a name="protolca.ImpactMethod"></a>

### ImpactMethod
An impact assessment method.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| category | [Ref](#protolca.Ref) |  | The category of the entity. |
| tags | [string](#string) | repeated | A list of optional tags. A tag is just a string which should not contain commas (and other special characters). |
| library | [string](#string) |  | If this entity is part of a library, this field contains the identifier of that library. The identifier is typically just the comination of the library name and version. |
| impact_categories | [ImpactCategoryRef](#protolca.ImpactCategoryRef) | repeated | The impact categories of the method. |
| nw_sets | [NwSet](#protolca.NwSet) | repeated | The normalization and weighting sets of the method. |






<a name="protolca.ImpactResult"></a>

### ImpactResult
A result value for an impact assessment category.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| impact_category | [ImpactCategoryRef](#protolca.ImpactCategoryRef) |  | The reference to the impact assessment category. |
| value | [double](#double) |  | The value of the flow amount. |






<a name="protolca.Location"></a>

### Location
A location like a country, state, city, etc.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| category | [Ref](#protolca.Ref) |  | The category of the entity. |
| tags | [string](#string) | repeated | A list of optional tags. A tag is just a string which should not contain commas (and other special characters). |
| library | [string](#string) |  | If this entity is part of a library, this field contains the identifier of that library. The identifier is typically just the comination of the library name and version. |
| code | [string](#string) |  | The code of the location (e.g. an ISO 2-letter country code). |
| latitude | [double](#double) |  | The average latitude of the location. |
| longitude | [double](#double) |  | The average longitude of the location. |
| geometry_bytes | [bytes](#bytes) |  | A GeoJSON object. When we map to the bytes type it means that we have no matching message type and just put the raw bytes into the field. This is specifically true for our geometry data of locations which cannot be translated to valid GeoJSON using Protocol Buffers (as they do not support arrays of arrays). To indicate that this is a different field than the field in the olca-schema definition, we append the _bytes suffix to the field name |






<a name="protolca.NwFactor"></a>

### NwFactor
A normalization and weighting factor of a [NwSet] related to an impact
category. Depending on the purpose of the [NwSet] (normalization, weighting,
or both) the normalization and weighting factor can be present or not.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| impact_category | [Ref](#protolca.Ref) |  |  |
| normalisation_factor | [double](#double) |  |  |
| weighting_factor | [double](#double) |  |  |






<a name="protolca.NwSet"></a>

### NwSet
A normalization and weighting set.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| weighted_score_unit | [string](#string) |  | This is the optional unit of the (normalized and) weighted score when this normalization and weighting set was applied on a LCIA result. |
| factors | [NwFactor](#protolca.NwFactor) | repeated | The list of normalization and weighting factors of this set. |






<a name="protolca.Parameter"></a>

### Parameter
In openLCA, parameters can be defined in different scopes: global, process,
or LCIA method. The parameter name can be used in formulas and, thus, need
to conform to a specific syntax. Within a scope the parameter name should be
unique (otherwise the evaluation is not deterministic). There are two types
of parameters in openLCA: input parameters and dependent parameters. An
input parameter can have an optional uncertainty distribution but not a
formula. A dependent parameter can (should) have a formula (where also other
parameters can be used) but no uncertainty distribution.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| category | [Ref](#protolca.Ref) |  | The category of the entity. |
| tags | [string](#string) | repeated | A list of optional tags. A tag is just a string which should not contain commas (and other special characters). |
| library | [string](#string) |  | If this entity is part of a library, this field contains the identifier of that library. The identifier is typically just the comination of the library name and version. |
| parameter_scope | [ParameterScope](#protolca.ParameterScope) |  | The scope where the parameter is valid. |
| input_parameter | [bool](#bool) |  | Indicates whether the parameter is an input parameter (true) or a dependent/calculated parameter (false). A parameter can have a formula if it is not an input parameter. |
| value | [double](#double) |  | The parameter value. |
| formula | [string](#string) |  | A mathematical expression to calculate the parameter value. |
| uncertainty | [Uncertainty](#protolca.Uncertainty) |  | An uncertainty distribution of the parameter value. This is only valid for input parameters. |






<a name="protolca.ParameterRedef"></a>

### ParameterRedef
A redefinition of a parameter in a product system.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| name | [string](#string) |  | The parameter name. |
| value | [double](#double) |  | The (new) value of the parameter. |
| context | [Ref](#protolca.Ref) |  | The context of the paramater (a process or LCIA method). If no context is provided it is assumed that this is a redefinition of a global parameter. |






<a name="protolca.Process"></a>

### Process



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| category | [Ref](#protolca.Ref) |  | The category of the entity. |
| tags | [string](#string) | repeated | A list of optional tags. A tag is just a string which should not contain commas (and other special characters). |
| library | [string](#string) |  | If this entity is part of a library, this field contains the identifier of that library. The identifier is typically just the comination of the library name and version. |
| allocation_factors | [AllocationFactor](#protolca.AllocationFactor) | repeated |  |
| default_allocation_method | [AllocationType](#protolca.AllocationType) |  |  |
| exchanges | [Exchange](#protolca.Exchange) | repeated | The inputs and outputs of the process. |
| last_internal_id | [int32](#int32) |  | This field holds the last internal ID that was used in an exchange (which may have been deleted, so it can be larger than the largest internal ID of the exchanges of the process.) The internal ID of an exchange is used to identify exchanges within a process (for updates, data exchanges (see process links), etc.). When you add an exchange to a process, you should increment this field in the process and set the resulting value as the internal ID of that exchange. The sequence of internal IDs should start with `1`. |
| location | [Location](#protolca.Location) |  |  |
| parameters | [Parameter](#protolca.Parameter) | repeated |  |
| process_documentation | [ProcessDocumentation](#protolca.ProcessDocumentation) |  |  |
| process_type | [ProcessType](#protolca.ProcessType) |  |  |
| dq_system | [Ref](#protolca.Ref) |  | A reference to a data quality system ([DqSystem]) with which the overall quality of the process can be assessed. |
| exchange_dq_system | [Ref](#protolca.Ref) |  | A reference to a data quality system ([DqSystem]) with which the quality of individual inputs and outputs ([Exchange]s) of the process can be assessed. |
| social_dq_system | [Ref](#protolca.Ref) |  | A reference to a data quality system ([DqSystem]) with which the quality of individual social aspects of the process can be assessed. |
| dq_entry | [string](#string) |  | A data quality entry like `(1;3;2;5;1)`. The entry is a vector of data quality values that need to match the overall data quality system of the process (the system that is stored in the `dqSystem` property). In such a system the data quality indicators have fixed positions and the respective values in the `dqEntry` vector map to these positions. |
| infrastructure_process | [bool](#bool) |  | Indicates whether this process describes an infrastructure process. This field is part of the openLCA schema because of backward compatibility with EcoSpold 1. It does not really have a meaning in openLCA and should not be used anymore. |
| social_aspects | [SocialAspect](#protolca.SocialAspect) | repeated | A set of social aspects related to this process. |






<a name="protolca.ProcessDocumentation"></a>

### ProcessDocumentation



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| time_description | [string](#string) |  |  |
| valid_until | [string](#string) |  |  |
| valid_from | [string](#string) |  |  |
| technology_description | [string](#string) |  |  |
| data_collection_description | [string](#string) |  |  |
| completeness_description | [string](#string) |  |  |
| data_selection_description | [string](#string) |  |  |
| review_details | [string](#string) |  |  |
| data_treatment_description | [string](#string) |  |  |
| inventory_method_description | [string](#string) |  |  |
| modeling_constants_description | [string](#string) |  |  |
| reviewer | [Ref](#protolca.Ref) |  |  |
| sampling_description | [string](#string) |  |  |
| sources | [Ref](#protolca.Ref) | repeated |  |
| restrictions_description | [string](#string) |  |  |
| copyright | [bool](#bool) |  |  |
| creation_date | [string](#string) |  |  |
| data_documentor | [Ref](#protolca.Ref) |  |  |
| data_generator | [Ref](#protolca.Ref) |  |  |
| data_set_owner | [Ref](#protolca.Ref) |  |  |
| intended_application | [string](#string) |  |  |
| project_description | [string](#string) |  |  |
| publication | [Ref](#protolca.Ref) |  |  |
| geography_description | [string](#string) |  |  |






<a name="protolca.ProcessLink"></a>

### ProcessLink
A process link is a connection between two processes in a product system.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| provider | [Ref](#protolca.Ref) |  | The descriptor of the process or product system that provides a product or a waste treatment. |
| flow | [Ref](#protolca.Ref) |  | The descriptor of the flow that is exchanged between the two processes. |
| process | [Ref](#protolca.Ref) |  | The descriptor of the process that is linked to the provider. |
| exchange | [ExchangeRef](#protolca.ExchangeRef) |  | The exchange of the linked process (this is useful if the linked process has multiple exchanges with the same flow that are linked to different provides, e.g. in an electricity mix). |






<a name="protolca.ProcessRef"></a>

### ProcessRef
A reference to a [Process] data set.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| category_path | [string](#string) | repeated | The full path of the category of the referenced entity from top to bottom, e.g. `&#34;Elementary flows&#34;, &#34;Emissions to air&#34;, &#34;unspecified&#34;`. |
| location | [string](#string) |  | The location name or code of the process. |
| process_type | [ProcessType](#protolca.ProcessType) |  | The type of the process. |






<a name="protolca.ProductSystem"></a>

### ProductSystem
A product system describes the supply chain of a product (the functional
unit) ...


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| category | [Ref](#protolca.Ref) |  | The category of the entity. |
| tags | [string](#string) | repeated | A list of optional tags. A tag is just a string which should not contain commas (and other special characters). |
| library | [string](#string) |  | If this entity is part of a library, this field contains the identifier of that library. The identifier is typically just the comination of the library name and version. |
| processes | [ProcessRef](#protolca.ProcessRef) | repeated | The descriptors of all processes that are contained in the product system. |
| reference_process | [ProcessRef](#protolca.ProcessRef) |  | The descriptor of the process that provides the flow of the functional unit of the product system. |
| reference_exchange | [Exchange](#protolca.Exchange) |  | The exchange of the reference processes (typically the product output) that provides the flow of the functional unit of the product system. |
| target_amount | [double](#double) |  | The flow amount of the functional unit of the product system. |
| target_unit | [Ref](#protolca.Ref) |  | The unit in which the flow amount of the functional unit is given. |
| target_flow_property | [Ref](#protolca.Ref) |  | The flow property in which the flow amount of the functional unit is given. |
| process_links | [ProcessLink](#protolca.ProcessLink) | repeated | The process links of the product system. |






<a name="protolca.Project"></a>

### Project



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| category | [Ref](#protolca.Ref) |  | The category of the entity. |
| tags | [string](#string) | repeated | A list of optional tags. A tag is just a string which should not contain commas (and other special characters). |
| library | [string](#string) |  | If this entity is part of a library, this field contains the identifier of that library. The identifier is typically just the comination of the library name and version. |
| impact_method | [Ref](#protolca.Ref) |  |  |
| nw_set | [NwSet](#protolca.NwSet) |  |  |






<a name="protolca.Ref"></a>

### Ref
A Ref is a reference to a [RootEntity]. When serializing an entity (e.g. a
[Process]) that references another standalone entity (e.g. a [Flow] in an
[Exchange]) we do not want to write the complete referenced entity into the
serialized JSON object but just a reference. However, the reference contains
some meta-data like name, category path etc. that are useful to display.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| category_path | [string](#string) | repeated | The full path of the category of the referenced entity from top to bottom, e.g. `&#34;Elementary flows&#34;, &#34;Emissions to air&#34;, &#34;unspecified&#34;`. |






<a name="protolca.SimpleResult"></a>

### SimpleResult



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| flow_results | [FlowResult](#protolca.FlowResult) | repeated |  |
| impact_results | [ImpactResult](#protolca.ImpactResult) | repeated |  |






<a name="protolca.SocialAspect"></a>

### SocialAspect
An instance of this class describes a social aspect related to a social
indicator in a process.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| activity_value | [double](#double) |  | The value of the activity variable of the related indicator. |
| comment | [string](#string) |  |  |
| quality | [string](#string) |  | A data quality entry, e.g. `(3,1,2,4,1)`. |
| raw_amount | [string](#string) |  | The raw amount of the indicator&#39;s unit of measurement (not required to be numeric currently) |
| risk_level | [RiskLevel](#protolca.RiskLevel) |  |  |
| social_indicator | [Ref](#protolca.Ref) |  |  |
| source | [Ref](#protolca.Ref) |  |  |






<a name="protolca.SocialIndicator"></a>

### SocialIndicator



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| category | [Ref](#protolca.Ref) |  | The category of the entity. |
| tags | [string](#string) | repeated | A list of optional tags. A tag is just a string which should not contain commas (and other special characters). |
| library | [string](#string) |  | If this entity is part of a library, this field contains the identifier of that library. The identifier is typically just the comination of the library name and version. |
| activity_variable | [string](#string) |  | The name of the activity variable of the indicator. |
| activity_quantity | [Ref](#protolca.Ref) |  | The quantity of the activity variable. |
| activity_unit | [Ref](#protolca.Ref) |  | The unit of the activity variable. |
| unit_of_measurement | [string](#string) |  | The unit in which the indicator is measured. |
| evaluation_scheme | [string](#string) |  | Documentation of the evaluation scheme of the indicator. |






<a name="protolca.Source"></a>

### Source
A source is a literature reference.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| category | [Ref](#protolca.Ref) |  | The category of the entity. |
| tags | [string](#string) | repeated | A list of optional tags. A tag is just a string which should not contain commas (and other special characters). |
| library | [string](#string) |  | If this entity is part of a library, this field contains the identifier of that library. The identifier is typically just the comination of the library name and version. |
| url | [string](#string) |  | A URL that points to the source. |
| text_reference | [string](#string) |  | The full text reference of the source. |
| year | [int32](#int32) |  | The publication year of the source. |
| external_file | [string](#string) |  | A direct link (relative or absolute URL) to the source file. |






<a name="protolca.Uncertainty"></a>

### Uncertainty
Defines the parameter values of an uncertainty distribution. Depending on
the uncertainty distribution type different parameters could be used.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| distribution_type | [UncertaintyType](#protolca.UncertaintyType) |  | The uncertainty distribution type |
| mean | [double](#double) |  | The arithmetic mean (used for normal distributions). |
| mean_formula | [string](#string) |  | A mathematical formula for the arithmetic mean. |
| geom_mean | [double](#double) |  | The geometric mean value (used for log-normal distributions). |
| geom_mean_formula | [string](#string) |  | A mathematical formula for the geometric mean. |
| minimum | [double](#double) |  | The minimum value (used for uniform and triangle distributions). |
| minimum_formula | [string](#string) |  | A mathematical formula for the minimum value. |
| sd | [double](#double) |  | The arithmetic standard deviation (used for normal distributions). |
| sd_formula | [string](#string) |  | A mathematical formula for the arithmetic standard deviation. |
| geom_sd | [double](#double) |  | The geometric standard deviation (used for log-normal distributions). |
| geom_sd_formula | [string](#string) |  | A mathematical formula for the geometric standard deviation. |
| mode | [double](#double) |  | The most likely value (used for triangle distributions). |
| mode_formula | [string](#string) |  | A mathematical formula for the most likely value. |
| maximum | [double](#double) |  | The maximum value (used for uniform and triangle distributions). |
| maximum_formula | [string](#string) |  | A mathematical formula for the maximum value. |






<a name="protolca.Unit"></a>

### Unit
An unit of measure


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| conversion_factor | [double](#double) |  | The conversion factor to the reference unit of the unit group to which this unit belongs. |
| reference_unit | [bool](#bool) |  | Indicates whether the unit is the reference unit of the unit group to which this unit belongs. If it is the reference unit the conversion factor must be 1.0. There should be always only one reference unit in a unit group. The reference unit is used to convert amounts given in one unit to amounts given in another unit of the respective unit group. |
| synonyms | [string](#string) | repeated | A list of synonyms for the unit. |






<a name="protolca.UnitGroup"></a>

### UnitGroup
A group of units that can be converted into each other.


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [string](#string) |  | The type name of the respectiven entity. This field is used for JSON-LD compatibility. |
| id | [string](#string) |  | The reference ID (typically an UUID) of the entity. |
| name | [string](#string) |  | The name of the entity. |
| description | [string](#string) |  | The description of the entity. |
| version | [string](#string) |  | A version number in MAJOR.MINOR.PATCH format where the MINOR and PATCH fields are optional and the fields may have leading zeros (so 01.00.00 is the same as 1.0.0 or 1). |
| last_change | [string](#string) |  | The timestamp when the entity was changed the last time. |
| category | [Ref](#protolca.Ref) |  | The category of the entity. |
| tags | [string](#string) | repeated | A list of optional tags. A tag is just a string which should not contain commas (and other special characters). |
| library | [string](#string) |  | If this entity is part of a library, this field contains the identifier of that library. The identifier is typically just the comination of the library name and version. |
| default_flow_property | [Ref](#protolca.Ref) |  | Some LCA data formats do not have the concept of flow properties or quantities. This field provides a default link to a flow property for units that are contained in this group. |
| units | [Unit](#protolca.Unit) | repeated | The units of the unit group. |





 


<a name="protolca.AllocationType"></a>

### AllocationType
An enumeration type for allocation methods. This type is used to define the
type of an [AllocationFactor], the default allocation method of a
multi-functional [Process], or the allocation method in a
[CalculationSetup].

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNDEFINED_ALLOCATION_TYPE | 0 | This default option was added automatically and means that no values was set. |
| PHYSICAL_ALLOCATION | 1 |  |
| ECONOMIC_ALLOCATION | 2 |  |
| CAUSAL_ALLOCATION | 3 |  |
| USE_DEFAULT_ALLOCATION | 4 |  |
| NO_ALLOCATION | 5 |  |



<a name="protolca.CalculationType"></a>

### CalculationType
An enumeration of the different calculation methods supported by openLCA.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNDEFINED_CALCULATION_TYPE | 0 | This default option was added automatically and means that no values was set. |
| SIMPLE_CALCULATION | 1 | Calculates the total results for elementary flows, LCIA indicators, costs, etc. of a product system. |
| CONTRIBUTION_ANALYSIS | 2 | Includes the total result vectors of a simple calculation but calculates also the direct contributions of each process (or better process product in case of multi-output processes) to these total results. |
| UPSTREAM_ANALYSIS | 3 | Extends the contribution analysis by providing also the upstream results of each process (process product) in the product system. The upstream result contains the direct contributions of the respective process but also the result of the supply chain up to this process scaled to the demand of the process in the product system. |
| REGIONALIZED_CALCULATION | 4 | A regionalized calculation is a contribution analysis but with an LCIA method that supports regionalized characterization factors (via region specific parameters in formulas) and a product system with processes that have geographic information assigned (point, line, or polygon shapes). |
| MONTE_CARLO_SIMULATION | 5 | A Monte Carlo simulation generates for each run, of a given number of a given number of iterations, random values according to the uncertainty distributions of process inputs/outputs, parameters, characterization factors, etc. of a product system and then performs a simple calculation for that specific run. |



<a name="protolca.FlowPropertyType"></a>

### FlowPropertyType
An enumeration of flow property types.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNDEFINED_FLOW_PROPERTY_TYPE | 0 | This default option was added automatically and means that no values was set. |
| ECONOMIC_QUANTITY | 1 |  |
| PHYSICAL_QUANTITY | 2 |  |



<a name="protolca.FlowType"></a>

### FlowType
The basic flow types.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNDEFINED_FLOW_TYPE | 0 | This default option was added automatically and means that no values was set. |
| ELEMENTARY_FLOW | 1 |  |
| PRODUCT_FLOW | 2 |  |
| WASTE_FLOW | 3 |  |



<a name="protolca.ModelType"></a>

### ModelType
An enumeration of the root entity types.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNDEFINED_MODEL_TYPE | 0 | This default option was added automatically and means that no values was set. |
| PROJECT | 1 |  |
| IMPACT_METHOD | 2 |  |
| IMPACT_CATEGORY | 3 |  |
| PRODUCT_SYSTEM | 4 |  |
| PROCESS | 5 |  |
| FLOW | 6 |  |
| FLOW_PROPERTY | 7 |  |
| UNIT_GROUP | 8 |  |
| UNIT | 9 |  |
| ACTOR | 10 |  |
| SOURCE | 11 |  |
| CATEGORY | 12 |  |
| LOCATION | 13 |  |
| NW_SET | 14 |  |
| SOCIAL_INDICATOR | 15 |  |



<a name="protolca.ParameterScope"></a>

### ParameterScope
The possible scopes of parameters. Parameters can be defined globally, in
processes, or impact categories. They can be redefined in calculation setups
on the project and product system level, but the initial definition is
always only global, in a process, or an LCIA category.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNDEFINED_PARAMETER_SCOPE | 0 | This default option was added automatically and means that no values was set. |
| PROCESS_SCOPE | 1 | Indicates that the evaluation scope of a parameter is the process where it is defined. |
| IMPACT_SCOPE | 2 | Indicates that the evaluation scope of a parameter is the impact category where it is defined. |
| GLOBAL_SCOPE | 3 | Indicates that the evaluation scope of a parameter is the global scope. |



<a name="protolca.ProcessType"></a>

### ProcessType


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNDEFINED_PROCESS_TYPE | 0 | This default option was added automatically and means that no values was set. |
| LCI_RESULT | 1 |  |
| UNIT_PROCESS | 2 |  |



<a name="protolca.RiskLevel"></a>

### RiskLevel


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNDEFINED_RISK_LEVEL | 0 | This default option was added automatically and means that no values was set. |
| NO_OPPORTUNITY | 1 |  |
| HIGH_OPPORTUNITY | 2 |  |
| MEDIUM_OPPORTUNITY | 3 |  |
| LOW_OPPORTUNITY | 4 |  |
| NO_RISK | 5 |  |
| VERY_LOW_RISK | 6 |  |
| LOW_RISK | 7 |  |
| MEDIUM_RISK | 8 |  |
| HIGH_RISK | 9 |  |
| VERY_HIGH_RISK | 10 |  |
| NO_DATA | 11 |  |
| NOT_APPLICABLE | 12 |  |



<a name="protolca.UncertaintyType"></a>

### UncertaintyType
Enumeration of uncertainty distribution types that can be used in exchanges,
parameters, LCIA factors, etc.

| Name | Number | Description |
| ---- | ------ | ----------- |
| UNDEFINED_UNCERTAINTY_TYPE | 0 | This default option was added automatically and means that no values was set. |
| LOG_NORMAL_DISTRIBUTION | 1 |  |
| NORMAL_DISTRIBUTION | 2 |  |
| TRIANGLE_DISTRIBUTION | 3 |  |
| UNIFORM_DISTRIBUTION | 4 |  |


 

 

 



<a name="services.proto"></a>
<p align="right"><a href="#top">Top</a></p>

## services.proto


 

 

 


<a name="protolca.services.ModelService"></a>

### ModelService


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| getFlow | [.protolca.Ref](#protolca.Ref) | [.protolca.Flow](#protolca.Flow) |  |

 



## Scalar Value Types

| .proto Type | Notes | C++ | Java | Python | Go | C# | PHP | Ruby |
| ----------- | ----- | --- | ---- | ------ | -- | -- | --- | ---- |
| <a name="double" /> double |  | double | double | float | float64 | double | float | Float |
| <a name="float" /> float |  | float | float | float | float32 | float | float | Float |
| <a name="int32" /> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="int64" /> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="uint32" /> uint32 | Uses variable-length encoding. | uint32 | int | int/long | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="uint64" /> uint64 | Uses variable-length encoding. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum or Fixnum (as required) |
| <a name="sint32" /> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sint64" /> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="fixed32" /> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int | uint32 | uint | integer | Bignum or Fixnum (as required) |
| <a name="fixed64" /> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long | uint64 | ulong | integer/string | Bignum |
| <a name="sfixed32" /> sfixed32 | Always four bytes. | int32 | int | int | int32 | int | integer | Bignum or Fixnum (as required) |
| <a name="sfixed64" /> sfixed64 | Always eight bytes. | int64 | long | int/long | int64 | long | integer/string | Bignum |
| <a name="bool" /> bool |  | bool | boolean | boolean | bool | bool | boolean | TrueClass/FalseClass |
| <a name="string" /> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode | string | string | string | String (UTF-8) |
| <a name="bytes" /> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str | []byte | ByteString | string | String (ASCII-8BIT) |

