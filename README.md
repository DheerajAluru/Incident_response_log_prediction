# Incident_response_log_prediction
This is an event log of an incident management process extracted from data gathered from the audit system of an instance of the ServiceNowTM platform used by an IT company.<b>
About the Dataset:<b>
This dataset is taken from below kaggle repository <b>

https://www.kaggle.com/vipulshinde/incident-response-log
<b>
The dataset is having incidents raised by customers.Which contains an event log of an incident management process extracted from a service desk platform of an IT company<b>
Number of instances: 141,712 events (24,918 incidents)<b>
Number of attributes: 36 attributes (1 case identifier, 1 state identifier, 32 descriptive attributes, 2 dependent variables)<b>
Attribute Information:<b>
ID<b>
Incident identifier (24,918 different values)<b>
ID_status<b>
Eight levels controlling the incident management process transitions from opening until closing the case<b>
active<b>
Boolean attribute that shows whether the record is active or closed/canceled<b>
count_reassign<b>
Number of times the incident has the group or the support analysts changed<b>
count_opening<b>
Number of times the incident resolution was rejected by the caller<b>
count_updated<b>
Number of incident updates until that moment<b>
ID_caller<b>
Identifier of the user affected<b>
opened_by<b>
Identifier of the user who reported the incident<b>
opened_time<b>
Incident user opening date and time<b>
Created_by<b>
Identifier of the user who registered the incident<b>
created_at<b>
Incident system creation date and time<b>
updated_by<b>
Identifier of the user who updated the incident and generated the current log record<b>
updated_at<b>
Incident system update date and time<b>
type_contact<b>
Categorical attribute that shows by what means the incident was reported<b>
location<b>
Identifier of the location of the place affected<b>
Category Id<b>
First-level description of the affected service<b>
user_symptom<b>
Description of the user perception about service availability<b>
Impact<b>
Description of the impact caused by the incident (values: 1“High; 2“Medium; 3“Low)<b>
Support_group<b>
Identifier of the support group in charge of the incident<b>
support_incharge<b>
Identifier of the user in charge of the incident<b>
Doc_knowledge<b>
Boolean attribute that shows whether a knowledge base document was used to resolve the incident<b>
confirmation_check<b>
Boolean attribute that shows whether the priority field has been double-checked<b>
Notify<b>
Categorical attribute that shows whether notifications were generated for the incident<b>
Problem_id<b>
identifier of the problem associated with the incident<b>
change_request<b>
identifier of the change request associated with the incident<b>

