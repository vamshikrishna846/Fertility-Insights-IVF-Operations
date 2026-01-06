use  ivf_montaring;
DESCRIBE ivf_staff;
DESCRIBE ivf_appointments;
SELECT * FROM ivf_montaring.ivf_staff;
SELECT * FROM ivf_montaring.ivf_equipment;
SELECT * FROM ivf_montaring.ivf_operational_costs;
SELECT * FROM ivf_montaring.ivf_patient_wait_times;
SELECT * FROM ivf_montaring.ivf_performance_kpis;
SELECT * FROM ivf_montaring.ivf_room_utilization;
SELECT * FROM ivf_montaring.ivf_appointments;
SELECT staff_id, COUNT(*) AS cnt
FROM ivf_staff
GROUP BY staff_id
HAVING COUNT(*) > 1;
SELECT AVG(purchase_cost) AS mean_cost
FROM ivf_equipment;

SELECT salary AS mode_salary
FROM ivf_staff
GROUP BY salary
ORDER BY COUNT(*) DESC
LIMIT 1;
SELECT amount AS mode_cost
FROM ivf_operational_costs
GROUP BY amount
ORDER BY COUNT(*) DESC
LIMIT 1;
-- Mean
SELECT AVG(wait_time_minutes) FROM ivf_patient_wait_times;
-- Mode
SELECT wait_time_minutes
FROM ivf_patient_wait_times
GROUP BY wait_time_minutes
ORDER BY COUNT(*) DESC
LIMIT 1;
#--total maintanence cost
SELECT SUM(purchase_cost) AS total_cost
FROM ivf_equipment;
#average wait time
SELECT AVG(wait_time_minutes) AS avg_wait_time
FROM ivf_patient_wait_times;
#maximum wait time
SELECT MAX(wait_time_minutes) AS max_wait
FROM ivf_patient_wait_times;
SELECT appointment_id, COUNT(*) AS total_appointments
FROM ivf_appointments
GROUP BY  appointment_id;
SELECT staff_id, COUNT(*) AS cnt
FROM ivf_staff
GROUP BY staff_id
HAVING COUNT(*) > 1;
SELECT wait_time_minutes, COUNT(*) AS frequency
FROM ivf_patient_wait_times
GROUP BY wait_time_minutes
ORDER BY wait_time_minutes;
SELECT 
    AVG(usage_id) AS avg_utilization,
    MIN(usage_id) AS min_utilization,
    MAX(usage_id) AS max_utilization
FROM ivf_room_utilization;

#appoint_type vs duration
SELECT appointment_type, AVG(scheduled_duration_minutes) AS avg_duration
FROM ivf_appointments
GROUP BY appointment_type;
#department_role vs experience
SELECT department, AVG(experience_years) AS avg_experience
FROM ivf_staff
GROUP BY department;
#cost_id vs amount
SELECT cost_id, SUM(amount) AS total_cost
FROM ivf_operational_costs
GROUP BY cost_id;




