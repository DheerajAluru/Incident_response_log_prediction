# Incident_response_log_prediction
This is an event log of an incident management process extracted from data gathered from the audit system of an instance of the ServiceNowTM platform used by an IT company.<br>
About the Dataset:
This dataset is taken from below kaggle repository <br>

https://www.kaggle.com/vipulshinde/incident-response-log<br>
The dataset is having incidents raised by customers.Which contains an event log of an incident management process extracted from a service desk platform of an IT company<br>
Number of instances: 141,712 events (24,918 incidents)<br>
Number of attributes: 36 attributes (1 case identifier, 1 state identifier, 32 descriptive attributes, 2 dependent variables)<br>
Attribute Information:<br>
ID<br>
Incident identifier (24,918 different values)<br>
ID_status<br>
Eight levels controlling the incident management process transitions from opening until closing the case<br>
active<br>
Boolean attribute that shows whether the record is active or closed/canceled<br>
count_reassign<br>
Number of times the incident has the group or the support analysts changed<br>
count_opening<br>
Number of times the incident resolution was rejected by the caller<br>
count_updated<br>
Number of incident updates until that moment<br>
ID_caller<br>
Identifier of the user affected<br>
opened_by<br>
Identifier of the user who reported the incident<br>
opened_time<br>
Incident user opening date and time<br>
Created_by<br>
Identifier of the user who registered the incident<br>
created_at<br>
Incident system creation date and time<br>
updated_by<br>
Identifier of the user who updated the incident and generated the current log record<br>
updated_at<br>
Incident system update date and time<br>
type_contact<br>
Categorical attribute that shows by what means the incident was reported<br>
location<br>
Identifier of the location of the place affected<br>
Category Id<br>
First-level description of the affected service<br>
user_symptom<br>
Description of the user perception about service availability<br>
Impact<br>
Description of the impact caused by the incident (values: 1“High; 2“Medium; 3“Low)<br>
Support_group<br>
Identifier of the support group in charge of the incident<br>
support_incharge<br>
Identifier of the user in charge of the incident<br>
Doc_knowledge<br>
Boolean attribute that shows whether a knowledge base document was used to resolve the incident<br>
confirmation_check<br>
Boolean attribute that shows whether the priority field has been double-checked<br>
Notify<br>
Categorical attribute that shows whether notifications were generated for the incident<br>
Problem_id<br>
identifier of the problem associated with the incident<br>
change_request<br>
identifier of the change request associated with the incident<br>

