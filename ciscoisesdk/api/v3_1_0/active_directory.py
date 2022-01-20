# -*- coding: utf-8 -*-
"""Cisco Identity Services Engine ActiveDirectory API wrapper.

Copyright (c) 2021 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from builtins import *

from past.builtins import basestring

from ...restsession import RestSession
from ...utils import (
    check_type,
    dict_from_items_with_values,
    apply_path_params,
    dict_of_str,
)
from ...pagination import get_next_page


class ActiveDirectory(object):
    """Identity Services Engine ActiveDirectory API (version: 3.1.0).

    Wraps the Identity Services Engine ActiveDirectory
    API and exposes the API as native Python
    methods that return native Python objects.
    | The Active Directory API allows the user to carry out add, delete, and
      search operations on the active directory domains through Cisco ISE's
      join points. For example, if you want to connect to the domain
      cisco.com and retrieve the domain groups, you can carry out the
      following steps which are also available as APIs: Step 1 Create a
      domain join point in Cisco ISE. In the "domain" parameter use
      cisco.com.
    | Step 2 Get all defined join points and copy your join point's ID from
      the response.
    | Step 3 Join all Cisco ISE nodes to the domain. Use the ID received in
      the Step 2 in the URL. From this point onwards, you can perform
      several actions. In each action you should specify the joint point ID
      in the URL, as retrieved in step 2 in the previous configuration task.
      For example, you can: • Retrieve the user groups using the join point
      ID.
    | • Retrieve the groups of a specific domain using the join point ID.
      The domain parameter can be cisco.com or any of its trusted domains.
      You can use the get all trusted domains operation to retrieve the
      list.

    Revision History
    ----------------

    **Revision #**

    **Resource Version**

    **Cisco ISE Version**

    **Description**

    **Revision Modification**

    **Attribute**

    **Description**

    0

    1.0

    2.2

    Initial Cisco ISE Version

    1

    1.1

    2.4

    Support new attributes

    advancedSettings

    Added ERSActiveDirectoryAdvancedSettings Attribute 'advancedSettings'

    adAttributes

    Added ERSActiveDirectoryAttributes Attribute 'adAttributes'

    enableDomainWhiteList

    Added Boolean Attribute 'enableDomainWhiteList'

    2

    1.2

    3.1

    Support new attributes under ActiveDirectory AdvancedSettings

    enableFailedAuthProtection

    Added Boolean Attribute 'enableFailedAuthProtection'

    failedAuthThreshold

    Added Integer Attribute 'failedAuthThreshold'

    authProtectionType

    Added Enum Attribute 'authProtectionType'

    |

    Resource Definition
    -------------------

    +-----------+-----------+-----------+-----------+-----------+-----------+
    | **At      | **Type**  | **R       | **Desc    | **Default | **Example |
    | tribute** |           | equired** | ription** | Values**  | Values**  |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | name      | String    | Yes       | Resource  |           | Comp      |
    |           |           |           | Name.     |           | any_users |
    |           |           |           | Maximum   |           |           |
    |           |           |           | 32        |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | allowed.  |           |           |
    |           |           |           | Allowed   |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | alp       |           |           |
    |           |           |           | hanumeric |           |           |
    |           |           |           | and       |           |           |
    |           |           |           | .-_/\\\   |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | id        | String    | No        | Resource  |           | af1cd190- |
    |           |           |           | UUID      |           | 7d71-11eb |
    |           |           |           | value     |           | -b02e-ead |
    |           |           |           |           |           | 13cf60dcb |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | de        | String    | No        | No        |           | Group of  |
    | scription |           |           | character |           | Active    |
    |           |           |           | re        |           | company   |
    |           |           |           | striction |           | users     |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | domain    | String    | Yes       | The AD    |           | cisco.com |
    |           |           |           | domain.   |           |           |
    |           |           |           | Alph      |           |           |
    |           |           |           | anumeric, |           |           |
    |           |           |           | hyphen    |           |           |
    |           |           |           | (-) and   |           |           |
    |           |           |           | dot (.)   |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | allowed   |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | adSc      | String    | No        | String    | Defa      |           |
    | opesNames |           |           | that      | ult_Scope |           |
    |           |           |           | contains  |           |           |
    |           |           |           | the names |           |           |
    |           |           |           | of the    |           |           |
    |           |           |           | scopes    |           |           |
    |           |           |           | that the  |           |           |
    |           |           |           | active    |           |           |
    |           |           |           | directory |           |           |
    |           |           |           | belongs   |           |           |
    |           |           |           | to. Names |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | separated |           |           |
    |           |           |           | by comma. |           |           |
    |           |           |           | Alph      |           |           |
    |           |           |           | anumeric, |           |           |
    |           |           |           | u         |           |           |
    |           |           |           | nderscore |           |           |
    |           |           |           | (_)       |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | allowed   |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | ena       | Boolean   | No        |           | true      |           |
    | bleDomain |           |           |           |           |           |
    | WhiteList |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | adGroups  | List      | No        | Holds     |           |           |
    |           |           |           | list of   |           |           |
    |           |           |           | AD Groups |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | - groups  | List      | No        | List of   |           |           |
    |           |           |           | Groups    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   - name  | String    | Yes       | Required  |           | c         |
    |           |           |           | for each  |           | isco.com/ |
    |           |           |           | group in  |           | operators |
    |           |           |           | the group |           |           |
    |           |           |           | list with |           |           |
    |           |           |           | no        |           |           |
    |           |           |           | du        |           |           |
    |           |           |           | plication |           |           |
    |           |           |           | between   |           |           |
    |           |           |           | groups.   |           |           |
    |           |           |           | All       |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | allowed   |           |           |
    |           |           |           | except %  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   - sid   | String    | Yes       | Cisco ISE |           | S-1       |
    |           |           |           | uses      |           | -5-32-548 |
    |           |           |           | security  |           |           |
    |           |           |           | id        |           |           |
    |           |           |           | entifiers |           |           |
    |           |           |           | (SIDs)    |           |           |
    |           |           |           | for       |           |           |
    |           |           |           | opt       |           |           |
    |           |           |           | imization |           |           |
    |           |           |           | of group  |           |           |
    |           |           |           | m         |           |           |
    |           |           |           | embership |           |           |
    |           |           |           | ev        |           |           |
    |           |           |           | aluation. |           |           |
    |           |           |           | SIDs are  |           |           |
    |           |           |           | useful    |           |           |
    |           |           |           | for       |           |           |
    |           |           |           | e         |           |           |
    |           |           |           | fficiency |           |           |
    |           |           |           | (speed)   |           |           |
    |           |           |           | when the  |           |           |
    |           |           |           | groups    |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | e         |           |           |
    |           |           |           | valuated. |           |           |
    |           |           |           | All       |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | allowed   |           |           |
    |           |           |           | except %  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   - type  | String    | No        | No        |           | GLOBAL    |
    |           |           |           | character |           |           |
    |           |           |           | re        |           |           |
    |           |           |           | striction |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | adA       | List      | No        | Holds     |           |           |
    | ttributes |           |           | list of   |           |           |
    |           |           |           | AD        |           |           |
    |           |           |           | A         |           |           |
    |           |           |           | ttributes |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | List      | No        | List of   |           |           |
    | a         |           |           | A         |           |           |
    | ttributes |           |           | ttributes |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   - name  | String    | Yes       | Required  |           | name1     |
    |           |           |           | for each  |           |           |
    |           |           |           | attribute |           |           |
    |           |           |           | in the    |           |           |
    |           |           |           | attribute |           |           |
    |           |           |           | list with |           |           |
    |           |           |           | no        |           |           |
    |           |           |           | du        |           |           |
    |           |           |           | plication |           |           |
    |           |           |           | between   |           |           |
    |           |           |           | at        |           |           |
    |           |           |           | tributes. |           |           |
    |           |           |           | All       |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | allowed   |           |           |
    |           |           |           | except    |           |           |
    |           |           |           | <%"       |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   - type  | Enum      | Yes       | Required  | STRING    |           |
    |           |           |           | for each  |           |           |
    |           |           |           | group in  |           |           |
    |           |           |           | the group |           |           |
    |           |           |           | list.     |           |           |
    |           |           |           | Allowed   |           |           |
    |           |           |           | values:   |           |           |
    |           |           |           | - STRING, |           |           |
    |           |           |           | - IP,     |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | BOOLEAN,  |           |           |
    |           |           |           | - INT,    |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | OCT       |           |           |
    |           |           |           | ET_STRING |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | Yes       | Required  |           | inte      |
    | int       |           |           | for each  |           | rnalName1 |
    | ernalName |           |           | attribute |           |           |
    |           |           |           | in the    |           |           |
    |           |           |           | attribute |           |           |
    |           |           |           | list. All |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | allowed   |           |           |
    |           |           |           | except    |           |           |
    |           |           |           | <%"       |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | Yes       | Required  |           | defa      |
    | def       |           |           | for each  |           | ultString |
    | aultValue |           |           | attribute |           |           |
    |           |           |           | in the    |           |           |
    |           |           |           | attribute |           |           |
    |           |           |           | list. Can |           |           |
    |           |           |           | contain   |           |           |
    |           |           |           | an empty  |           |           |
    |           |           |           | string.   |           |           |
    |           |           |           | All       |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | allowed   |           |           |
    |           |           |           | except    |           |           |
    |           |           |           | <%"       |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | advance   | List      | No        |           |           |           |
    | dSettings |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | List      | No        | Identity  |           |           |
    | rew       |           |           | rewrite   |           |           |
    | riteRules |           |           | is an     |           |           |
    |           |           |           | advanced  |           |           |
    |           |           |           | feature   |           |           |
    |           |           |           | that      |           |           |
    |           |           |           | directs   |           |           |
    |           |           |           | Cisco ISE |           |           |
    |           |           |           | to        |           |           |
    |           |           |           | m         |           |           |
    |           |           |           | anipulate |           |           |
    |           |           |           | the       |           |           |
    |           |           |           | identity  |           |           |
    |           |           |           | before it |           |           |
    |           |           |           | is passed |           |           |
    |           |           |           | to the    |           |           |
    |           |           |           | external  |           |           |
    |           |           |           | Active    |           |           |
    |           |           |           | Directory |           |           |
    |           |           |           | system.   |           |           |
    |           |           |           | You can   |           |           |
    |           |           |           | create    |           |           |
    |           |           |           | rules to  |           |           |
    |           |           |           | change    |           |           |
    |           |           |           | the       |           |           |
    |           |           |           | identity  |           |           |
    |           |           |           | to a      |           |           |
    |           |           |           | desired   |           |           |
    |           |           |           | format    |           |           |
    |           |           |           | that      |           |           |
    |           |           |           | includes  |           |           |
    |           |           |           | or        |           |           |
    |           |           |           | excludes  |           |           |
    |           |           |           | a domain  |           |           |
    |           |           |           | prefix    |           |           |
    |           |           |           | and/or    |           |           |
    |           |           |           | suffix or |           |           |
    |           |           |           | other     |           |           |
    |           |           |           | a         |           |           |
    |           |           |           | dditional |           |           |
    |           |           |           | markup of |           |           |
    |           |           |           | your      |           |           |
    |           |           |           | choice    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   - rowId | Integer   | Yes       | Required  |           | 0         |
    |           |           |           | for each  |           |           |
    |           |           |           | rule in   |           |           |
    |           |           |           | the list  |           |           |
    |           |           |           | in serial |           |           |
    |           |           |           | order     |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | Yes       | Required  |           | exam      |
    | rew       |           |           | for each  |           | pleMatch0 |
    | riteMatch |           |           | rule in   |           |           |
    |           |           |           | the list  |           |           |
    |           |           |           | with no   |           |           |
    |           |           |           | du        |           |           |
    |           |           |           | plication |           |           |
    |           |           |           | between   |           |           |
    |           |           |           | rules.    |           |           |
    |           |           |           | All       |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | allowed   |           |           |
    |           |           |           | except %" |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    |   -       | String    | Yes       | Required  |           | examp     |
    | rewr      |           |           | for each  |           | leResult0 |
    | iteResult |           |           | rule in   |           |           |
    |           |           |           | the list. |           |           |
    |           |           |           | All       |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | allowed   |           |           |
    |           |           |           | except %" |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | Boolean   | No        |           | false     |           |
    | enabl     |           |           |           |           |           |
    | eRewrites |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | Boolean   | No        |           | true      |           |
    | enableP   |           |           |           |           |           |
    | assChange |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | Boolean   | No        |           | true      |           |
    | enableMa  |           |           |           |           |           |
    | chineAuth |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | Boolean   | No        |           | true      |           |
    | e         |           |           |           |           |           |
    | nableMach |           |           |           |           |           |
    | ineAccess |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | Boolean   | No        |           | false     |           |
    | enableDia |           |           |           |           |           |
    | linPermis |           |           |           |           |           |
    | sionCheck |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | Boolean   | No        |           | false     |           |
    | plai      |           |           |           |           |           |
    | ntextAuth |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | Integer   | No        | Range     | 5         |           |
    | agingTime |           |           | 1-8760    |           |           |
    |           |           |           | hours     |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | Boolean   | No        |           | false     |           |
    | en        |           |           |           |           |           |
    | ableCallb |           |           |           |           |           |
    | ackForDia |           |           |           |           |           |
    | linClient |           |           |           |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | Enum      | No        | Allowed   | SE        |           |
    | identi    |           |           | values:   | ARCH_JOIN |           |
    | tyNotInAd |           |           | - REJECT, | ED_FOREST |           |
    | Behaviour |           |           | -         |           |           |
    |           |           |           | SEA       |           |           |
    |           |           |           | RCH_JOINE |           |           |
    |           |           |           | D_FOREST, |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | S         |           |           |
    |           |           |           | EARCH_ALL |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | Enum      | No        | Allowed   | PROCEED   |           |
    | unreachab |           |           | values:   |           |           |
    | leDomains |           |           | -         |           |           |
    | Behaviour |           |           | PROCEED,  |           |           |
    |           |           |           | - DROP    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | - schema  | Enum      | No        | Allowed   | ACTIVE_   |           |
    |           |           |           | values:   | DIRECTORY |           |
    |           |           |           | -         |           |           |
    |           |           |           | ACTIVE_D  |           |           |
    |           |           |           | IRECTORY, |           |           |
    |           |           |           | - CUSTOM  |           |           |
    |           |           |           | Choose    |           |           |
    |           |           |           | ACTIVE_   |           |           |
    |           |           |           | DIRECTORY |           |           |
    |           |           |           | schema    |           |           |
    |           |           |           | when the  |           |           |
    |           |           |           | AD        |           |           |
    |           |           |           | a         |           |           |
    |           |           |           | ttributes |           |           |
    |           |           |           | defined   |           |           |
    |           |           |           | in AD can |           |           |
    |           |           |           | be copied |           |           |
    |           |           |           | to        |           |           |
    |           |           |           | relevant  |           |           |
    |           |           |           | a         |           |           |
    |           |           |           | ttributes |           |           |
    |           |           |           | in Cisco  |           |           |
    |           |           |           | ISE. If   |           |           |
    |           |           |           | cust      |           |           |
    |           |           |           | omization |           |           |
    |           |           |           | is        |           |           |
    |           |           |           | needed,   |           |           |
    |           |           |           | choose    |           |           |
    |           |           |           | CUSTOM    |           |           |
    |           |           |           | schema.   |           |           |
    |           |           |           | All User  |           |           |
    |           |           |           | info      |           |           |
    |           |           |           | a         |           |           |
    |           |           |           | ttributes |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | always    |           |           |
    |           |           |           | set to    |           |           |
    |           |           |           | default   |           |           |
    |           |           |           | value if  |           |           |
    |           |           |           | schema is |           |           |
    |           |           |           | ACTIVE_D  |           |           |
    |           |           |           | IRECTORY. |           |           |
    |           |           |           | Values    |           |           |
    |           |           |           | can be    |           |           |
    |           |           |           | changed   |           |           |
    |           |           |           | only for  |           |           |
    |           |           |           | CUSTOM    |           |           |
    |           |           |           | schema    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | String    | No        | User info | givenName |           |
    | firstName |           |           | a         |           |           |
    |           |           |           | ttribute. |           |           |
    |           |           |           | All       |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | allowed   |           |           |
    |           |           |           | except %  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | String    | No        | User info | d         |           |
    | d         |           |           | a         | epartment |           |
    | epartment |           |           | ttribute. |           |           |
    |           |           |           | All       |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | allowed   |           |           |
    |           |           |           | except %  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | String    | No        | User info | sn        |           |
    | lastName  |           |           | a         |           |           |
    |           |           |           | ttribute. |           |           |
    |           |           |           | All       |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | allowed   |           |           |
    |           |           |           | except %  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | String    | No        | User info | company   |           |
    | organizat |           |           | a         |           |           |
    | ionalUnit |           |           | ttribute. |           |           |
    |           |           |           | All       |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | allowed   |           |           |
    |           |           |           | except %  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | String    | No        | User info | title     |           |
    | jobTitle  |           |           | a         |           |           |
    |           |           |           | ttribute. |           |           |
    |           |           |           | All       |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | allowed   |           |           |
    |           |           |           | except %  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | String    | No        | User info | l         |           |
    | locality  |           |           | a         |           |           |
    |           |           |           | ttribute. |           |           |
    |           |           |           | All       |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | allowed   |           |           |
    |           |           |           | except %  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | - email   | String    | No        | User info | mail      |           |
    |           |           |           | a         |           |           |
    |           |           |           | ttribute. |           |           |
    |           |           |           | All       |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | allowed   |           |           |
    |           |           |           | except %  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | String    | No        | User info | st        |           |
    | stateO    |           |           | a         |           |           |
    | rProvince |           |           | ttribute. |           |           |
    |           |           |           | All       |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | allowed   |           |           |
    |           |           |           | except %  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | String    | No        | User info | teleph    |           |
    | telephone |           |           | a         | oneNumber |           |
    |           |           |           | ttribute. |           |           |
    |           |           |           | All       |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | allowed   |           |           |
    |           |           |           | except %  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | - country | String    | No        | User info | co        |           |
    |           |           |           | a         |           |           |
    |           |           |           | ttribute. |           |           |
    |           |           |           | All       |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | allowed   |           |           |
    |           |           |           | except %  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | String    | No        | User info | stre      |           |
    | stre      |           |           | a         | etAddress |           |
    | etAddress |           |           | ttribute. |           |           |
    |           |           |           | All       |           |           |
    |           |           |           | c         |           |           |
    |           |           |           | haracters |           |           |
    |           |           |           | are       |           |           |
    |           |           |           | allowed   |           |           |
    |           |           |           | except %  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | Boolean   | No        | Enable    | false     |           |
    | enableFa  |           |           | prevent   |           |           |
    | iledAuthP |           |           | AD        |           |           |
    | rotection |           |           | account   |           |           |
    |           |           |           | lockout   |           |           |
    |           |           |           | due to    |           |           |
    |           |           |           | too many  |           |           |
    |           |           |           | bad       |           |           |
    |           |           |           | password  |           |           |
    |           |           |           | attempts  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | Integer   | No        | Number of | 5         |           |
    | f         |           |           | bad       |           |           |
    | ailedAuth |           |           | password  |           |           |
    | Threshold |           |           | attempts  |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+
    | -         | Enum      | No        | Enable    | WIRELESS  |           |
    | authProte |           |           | prevent   |           |           |
    | ctionType |           |           | AD        |           |           |
    |           |           |           | account   |           |           |
    |           |           |           | lockout.  |           |           |
    |           |           |           | Allowed   |           |           |
    |           |           |           | values:   |           |           |
    |           |           |           | -         |           |           |
    |           |           |           | WIRELESS, |           |           |
    |           |           |           | - WIRED,  |           |           |
    |           |           |           | - BOTH    |           |           |
    +-----------+-----------+-----------+-----------+-----------+-----------+

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new ActiveDirectory
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Identity Services Engine service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(ActiveDirectory, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_active_directory_by_name(self,
                                     name,
                                     headers=None,
                                     **query_parameters):
        """This API allows the client to get Active Directory by name.

        Args:
            name(basestring): name path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(name, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'name': name,
        }

        e_url = ('/ers/config/activedirectory/name/{name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c6be021c4ca59e48c97afe218219bb1_v3_1_0', _api_response)

    def get_by_name(self,
                    name,
                    headers=None,
                    **query_parameters):
        """Alias for `get_active_directory_by_name <#ciscoisesdk.
        api.v3_1_0.active_directory.
        ActiveDirectory.get_active_directory_by_name>`_
        """
        return self.get_active_directory_by_name(
            name=name,
            headers=headers,
            **query_parameters
        )

    def get_user_groups(self,
                        id,
                        additional_data=None,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **query_parameters):
        """This API allows the client to get groups of which a given user
        is a member.

        Args:
            additional_data(list): additionalData, property of the
                request body (list of objects).
            id(basestring): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'additionalData':
                    additional_data,
            }
            _payload = {
                'OperationAdditionalData': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b839d4dee9b958e48ccef056603e253f_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/activedirectory/{id}/getUserGroups')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_b839d4dee9b958e48ccef056603e253f_v3_1_0', _api_response)

    def load_groups_from_domain(self,
                                id,
                                ad_attributes=None,
                                ad_scopes_names=None,
                                adgroups=None,
                                advanced_settings=None,
                                description=None,
                                domain=None,
                                enable_domain_white_list=None,
                                name=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **query_parameters):
        """This API loads domain groups configuration from Active Directory
        into Cisco ISE.

        Args:
            ad_attributes(object): Holds list of AD Attributes,
                property of the request body.
            ad_scopes_names(string): String that contains the names
                of the scopes that the active directory
                belongs to. Names are separated by
                comma. Alphanumeric, underscore (_)
                characters are allowed, property of the
                request body.
            adgroups(object): Holds list of AD Groups, property of
                the request body.
            advanced_settings(object): advancedSettings, property of
                the request body.
            description(string): No character restriction, property
                of the request body.
            domain(string): The AD domain. Alphanumeric, hyphen (-)
                and dot (.) characters are allowed,
                property of the request body.
            enable_domain_white_list(boolean):
                enableDomainWhiteList, property of the
                request body.
            id(string): Resource UUID value, property of the request
                body.
            name(string): Resource Name. Maximum 32 characters
                allowed. Allowed characters are
                alphanumeric and .-_/\\ characters,
                property of the request body.
            id(basestring): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'id':
                    id,
                'name':
                    name,
                'description':
                    description,
                'domain':
                    domain,
                'enableDomainWhiteList':
                    enable_domain_white_list,
                'adgroups':
                    adgroups,
                'advancedSettings':
                    advanced_settings,
                'adAttributes':
                    ad_attributes,
                'adScopesNames':
                    ad_scopes_names,
            }
            _payload = {
                'ERSActiveDirectory': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b05e80058df96e685baa727d578_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/activedirectory/{id}/addGroups')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_b05e80058df96e685baa727d578_v3_1_0', _api_response)

    def leave_domain(self,
                     id,
                     additional_data=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **query_parameters):
        """This API makes a Cisco ISE node to leave an Active Directory
        domain.

        Args:
            additional_data(list): additionalData, property of the
                request body (list of objects).
            id(basestring): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'additionalData':
                    additional_data,
            }
            _payload = {
                'OperationAdditionalData': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e84541805d1da1fa3d4d581102a9_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/activedirectory/{id}/leave')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_e84541805d1da1fa3d4d581102a9_v3_1_0', _api_response)

    def is_user_member_of_groups(self,
                                 id,
                                 additional_data=None,
                                 headers=None,
                                 payload=None,
                                 active_validation=True,
                                 **query_parameters):
        """This API verifies if the user is a member of the given groups.

        Args:
            additional_data(list): additionalData, property of the
                request body (list of objects).
            id(basestring): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'additionalData':
                    additional_data,
            }
            _payload = {
                'OperationAdditionalData': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_eae60ece5110590e97ddd910e8144ed2_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/activedirectory/{id}/isUserMemberOf')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_eae60ece5110590e97ddd910e8144ed2_v3_1_0', _api_response)

    def get_trusted_domains(self,
                            id,
                            headers=None,
                            **query_parameters):
        """This API gets the list of domains that are accessible through
        the given join point via trust relationships.

        Args:
            id(basestring): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        e_url = ('/ers/config/activedirectory/{id}/getTrustedDomains')
        endpoint_full_url = apply_path_params(e_url, path_params)

        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d0ed84901325292ad4e2a91a174f6b2_v3_1_0', _api_response)

    def join_domain_with_all_nodes(self,
                                   id,
                                   additional_data=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **query_parameters):
        """This API joins all Cisco ISE Nodes to an Active Directory
        domain.

        Args:
            additional_data(list): additionalData, property of the
                request body (list of objects).
            id(basestring): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'additionalData':
                    additional_data,
            }
            _payload = {
                'OperationAdditionalData': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e84705b918955b53afe61fc37911eb8b_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/activedirectory/{id}/joinAllNodes')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_e84705b918955b53afe61fc37911eb8b_v3_1_0', _api_response)

    def leave_domain_with_all_nodes(self,
                                    id,
                                    additional_data=None,
                                    headers=None,
                                    payload=None,
                                    active_validation=True,
                                    **query_parameters):
        """This API joins makes all Cisco ISE nodes leave an Active
        Directory domain.

        Args:
            additional_data(list): additionalData, property of the
                request body (list of objects).
            id(basestring): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'additionalData':
                    additional_data,
            }
            _payload = {
                'OperationAdditionalData': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_d011417d18d055ccb864c1dc2ae0456d_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/activedirectory/{id}/leaveAllNodes')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_d011417d18d055ccb864c1dc2ae0456d_v3_1_0', _api_response)

    def get_groups_by_domain(self,
                             id,
                             additional_data=None,
                             headers=None,
                             payload=None,
                             active_validation=True,
                             **query_parameters):
        """This API lists the groups of the given domain.

        Args:
            additional_data(list): additionalData, property of the
                request body (list of objects).
            id(basestring): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'additionalData':
                    additional_data,
            }
            _payload = {
                'OperationAdditionalData': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_fd729f50e65695966359b589a1606b_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/activedirectory/{id}/getGroupsByDomain')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_fd729f50e65695966359b589a1606b_v3_1_0', _api_response)

    def get_active_directory_by_id(self,
                                   id,
                                   headers=None,
                                   **query_parameters):
        """This API fetchs the join point details by ID. The ID can be
        retrieved with the Get All operation.

        Args:
            id(basestring): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        e_url = ('/ers/config/activedirectory/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cfcc7615d0492e2dd1b04dd03a9_v3_1_0', _api_response)

    def get_by_id(self,
                  id,
                  headers=None,
                  **query_parameters):
        """Alias for `get_active_directory_by_id <#ciscoisesdk.
        api.v3_1_0.active_directory.
        ActiveDirectory.get_active_directory_by_id>`_
        """
        return self.get_active_directory_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def delete_active_directory_by_id(self,
                                      id,
                                      headers=None,
                                      **query_parameters):
        """This API deletes an AD join point from Cisco ISE.

        Args:
            id(basestring): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        e_url = ('/ers/config/activedirectory/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.delete(endpoint_full_url, params=_params,
                                                 headers=_headers)
        else:
            _api_response = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_febbe79ed5bb780d97a98f292b606_v3_1_0', _api_response)

    def delete_by_id(self,
                     id,
                     headers=None,
                     **query_parameters):
        """Alias for `delete_active_directory_by_id <#ciscoisesdk.
        api.v3_1_0.active_directory.
        ActiveDirectory.delete_active_directory_by_id>`_
        """
        return self.delete_active_directory_by_id(
            id=id,
            headers=headers,
            **query_parameters
        )

    def join_domain(self,
                    id,
                    additional_data=None,
                    headers=None,
                    payload=None,
                    active_validation=True,
                    **query_parameters):
        """This API joins a Cisco ISE node to an Active Directory domain.

        Args:
            additional_data(list): additionalData, property of the
                request body (list of objects).
            id(basestring): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)
        check_type(id, basestring,
                   may_be_none=False)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'additionalData':
                    additional_data,
            }
            _payload = {
                'OperationAdditionalData': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_b3284240745e5b929c51495fe80bc1c4_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/activedirectory/{id}/join')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              headers=_headers,
                                              **request_params)

        else:
            _api_response = self._session.put(endpoint_full_url, params=_params,
                                              **request_params)

        return self._object_factory('bpm_b3284240745e5b929c51495fe80bc1c4_v3_1_0', _api_response)

    def get_active_directory(self,
                             page=None,
                             size=None,
                             headers=None,
                             **query_parameters):
        """This API lists all the join points for Active Directory domains
        in Cisco ISE.

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        check_type(page, (int, basestring, list))
        check_type(size, (int, basestring, list))

        _params = {
            'page':
                page,
            'size':
                size,
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/activedirectory')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c8dbec9679d453f78cb47d894c507a7b_v3_1_0', _api_response)

    def get_all(self,
                page=None,
                size=None,
                headers=None,
                **query_parameters):
        """Alias for `get_active_directory <#ciscoisesdk.
        api.v3_1_0.active_directory.
        ActiveDirectory.get_active_directory>`_
        """
        return self.get_active_directory(
            page=page,
            size=size,
            headers=headers,
            **query_parameters
        )

    def get_active_directory_generator(self,
                                       page=None,
                                       size=None,
                                       headers=None,
                                       **query_parameters):
        """This API lists all the join points for Active Directory domains
        in Cisco ISE.

        Args:
            page(int): page query parameter. Page number.
            size(int): size query parameter. Number of objects
                returned per page.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Generator: A generator object containing the following object.

              + RestResponse: REST response with following properties:

                  - headers(MyDict): response headers.
                  - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                    or the bracket notation.
                  - content(bytes): representation of the request's response
                  - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """

        yield from get_next_page(
            self.get_active_directory, dict(
                page=page,
                size=size,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def get_all_generator(self,
                          page=None,
                          size=None,
                          headers=None,
                          **query_parameters):
        """Alias for `get_active_directory_generator <#ciscoisesdk.
        api.v3_1_0.active_directory.
        ActiveDirectory.get_active_directory_generator>`_
        """
        yield from get_next_page(
            self.get_active_directory, dict(
                page=page,
                size=size,
                headers=headers,
                **query_parameters
            ),
            access_next_list=["SearchResult", "nextPage", "href"],
            access_resource_list=["SearchResult", "resources"])

    def create_active_directory(self,
                                ad_attributes=None,
                                ad_scopes_names=None,
                                adgroups=None,
                                advanced_settings=None,
                                description=None,
                                domain=None,
                                enable_domain_white_list=None,
                                id=None,
                                name=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **query_parameters):
        """This API creates an AD join point in Cisco ISE.

        Args:
            ad_attributes(object): Holds list of AD Attributes,
                property of the request body.
            ad_scopes_names(string): String that contains the names
                of the scopes that the active directory
                belongs to. Names are separated by
                comma. Alphanumeric, underscore (_)
                characters are allowed, property of the
                request body.
            adgroups(object): Holds list of AD Groups, property of
                the request body.
            advanced_settings(object): advancedSettings, property of
                the request body.
            description(string): No character restriction, property
                of the request body.
            domain(string): The AD domain. Alphanumeric, hyphen (-)
                and dot (.) characters are allowed,
                property of the request body.
            enable_domain_white_list(boolean):
                enableDomainWhiteList, property of the
                request body.
            id(string): Resource UUID value, property of the request
                body.
            name(string): Resource Name. Maximum 32 characters
                allowed. Allowed characters are
                alphanumeric and .-_/\\ characters,
                property of the request body.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)
            if 'ERS-Media-Type' in headers:
                check_type(headers.get('ERS-Media-Type'),
                           basestring)
            if 'X-CSRF-TOKEN' in headers:
                check_type(headers.get('X-CSRF-TOKEN'),
                           basestring)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True
        is_xml_payload = 'application/xml' in _headers.get('Content-Type', [])
        if active_validation and is_xml_payload:
            check_type(payload, basestring)
        if active_validation and not is_xml_payload:
            check_type(payload, dict)

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        if is_xml_payload:
            _payload = payload
        else:
            _tmp_payload = {
                'id':
                    id,
                'name':
                    name,
                'description':
                    description,
                'domain':
                    domain,
                'enableDomainWhiteList':
                    enable_domain_white_list,
                'adgroups':
                    adgroups,
                'advancedSettings':
                    advanced_settings,
                'adAttributes':
                    ad_attributes,
                'adScopesNames':
                    ad_scopes_names,
            }
            _payload = {
                'ERSActiveDirectory': dict_from_items_with_values(_tmp_payload)
            }
            _payload.update(payload or {})
            _payload = dict_from_items_with_values(_payload)
        if active_validation and not is_xml_payload:
            self._request_validator('jsd_e9318040a456978757d7abfa3e66b1_v3_1_0')\
                .validate(_payload)

        e_url = ('/ers/config/activedirectory')
        endpoint_full_url = apply_path_params(e_url, path_params)

        request_params = {'data': _payload} if is_xml_payload else {'json': _payload}
        if with_custom_headers:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               headers=_headers,
                                               **request_params)
        else:
            _api_response = self._session.post(endpoint_full_url, params=_params,
                                               **request_params)

        return self._object_factory('bpm_e9318040a456978757d7abfa3e66b1_v3_1_0', _api_response)

    def create(self,
               ad_attributes=None,
               ad_scopes_names=None,
               adgroups=None,
               advanced_settings=None,
               description=None,
               domain=None,
               enable_domain_white_list=None,
               id=None,
               name=None,
               headers=None,
               payload=None,
               active_validation=True,
               **query_parameters):
        """Alias for `create_active_directory <#ciscoisesdk.
        api.v3_1_0.active_directory.
        ActiveDirectory.create_active_directory>`_
        """
        return self.create_active_directory(
            ad_attributes=ad_attributes,
            ad_scopes_names=ad_scopes_names,
            adgroups=adgroups,
            advanced_settings=advanced_settings,
            description=description,
            domain=domain,
            enable_domain_white_list=enable_domain_white_list,
            id=id,
            name=name,
            payload=payload,
            active_validation=active_validation,
            headers=headers,
            **query_parameters
        )

    def get_version(self,
                    headers=None,
                    **query_parameters):
        """This API helps to retrieve the version information related to
        the active directory.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **query_parameters: Additional query parameters (provides
                support for parameters that may be added in the future).

        Returns:

            RestResponse: REST response with following properties:

              - headers(MyDict): response headers.
              - response(MyDict): response body as a MyDict object. Access the object's properties by using the dot notation
                or the bracket notation.
              - content(bytes): representation of the request's response
              - text(str): representation of the request's response

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Identity Services Engine cloud returns an error.
        """
        check_type(headers, dict)

        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           basestring, may_be_none=False)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        _params = {
        }
        _params.update(query_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        e_url = ('/ers/config/activedirectory/versioninfo')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            _api_response = self._session.get(endpoint_full_url, params=_params,
                                              headers=_headers)
        else:
            _api_response = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c2d0923990e35be1882e4dee000254a9_v3_1_0', _api_response)
