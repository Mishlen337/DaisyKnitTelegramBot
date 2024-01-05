SELECT
    *
FROM
    `responses_view`
WHERE
    survey_response_id IN(
    SELECT
        survey_response_id
    FROM
        `responses_view`
    WHERE
        answer = '2023-12-31'
);

SELECT
    *
FROM
    `responses_view`
WHERE
    survey_response_id IN(
    SELECT
        survey_response_id
    FROM
        `responses_view`
    WHERE
        survey_name = 'Пройти опрос' AND DATE(created) = '2024-01-05'
);
