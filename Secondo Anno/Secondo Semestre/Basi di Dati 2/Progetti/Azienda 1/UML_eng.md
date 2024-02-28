
<style>
    .edgeLabel {
        background: black !important;
        color: white !important;
    }
    .g.classGroup text	 {
        background: black !important;
        color: white !important;
    }
    body{
        background: white !important;
    }
    
</style>
```mermaid

%%{init:{
    'flowchart':{'nodeSpacing': 100, 'rankSpacing': 100},
    'themeVariables': {
      'lineColor': '#000'
    }
    }
    
}%%

classDiagram
    class Employee
    Employee : +String name
    Employee : +String surname
    Employee : +Timestamp birth
    Employee : +float Income
    Employee : + Timestamp dep_date

    class Department
    Department : +String name
    Department : +int phone_number
    

    class Project
    Project : +String name
    Project : +float budget

    class Work
    Work : +Timestamp start
    
    Employee "0..*"  -- "1..1" Department : directs
    Employee "0..*" -- "1..1" Department : affers
    Employee"1..1" --  "0..*" Work : works
    Work "0..*"  -- "1..1"Project : work_project
