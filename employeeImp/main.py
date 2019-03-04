employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
id = 1





imp = 0
ref = {}
for employee in employees:
    ref[employee[0]] = employee
imp += ref[id][1]
for sub in ref[id][2]:
    imp += ref[sub][1]
print(imp)















def getImportance(self, employees, id):
    """
    :type employees: Employee
    :type id: int
    :rtype: int
    """
    imp = 0
    ref = {}
    for employee in employees:
        ref[employee[0]] = employee
    imp += ref[id][1]
    for sub in ref[id][2]:
        imp += ref[sub][1]
    return imp















class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        imp = 0
        ref = {}
        for employee in employees:
            ref[employee[0]] = employee
        imp += ref[id][1]
        for sub in ref[id][2]:
            imp += ref[sub][1]
        return imp


getImportance(employees, id)