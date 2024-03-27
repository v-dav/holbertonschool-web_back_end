-- a SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUser that computes
-- and store the average weighted score for a student.

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE weighted_avg_score INT;
	DECLARE sum_weights INT;
	DECLARE score_x_weighing_factors_sum INT;

	SELECT SUM(weight) INTO sum_weights
	FROM corrections AS p
	LEFT JOIN projects
	ON p.project_id = projects.id
	WHERE p.user_id = user_id;

	SELECT SUM(score * weight) INTO score_x_weighing_factors_sum
	FROM corrections AS p
	LEFT JOIN projects
	ON p.project_id = projects.id
	WHERE p.user_id = user_id;

	SET weighted_avg_score = score_x_weighing_factors_sum / sum_weights;
	UPDATE users SET average_score = weighted_avg_score WHERE id = user_id;
END $$
DELIMITER ;

