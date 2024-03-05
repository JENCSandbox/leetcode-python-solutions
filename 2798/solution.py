class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        number_of_employees_who_met_target = 0

        for hours_by_employee in hours:
            if hours_by_employee >= target:
                number_of_employees_who_met_target += 1

        return number_of_employees_who_met_target


