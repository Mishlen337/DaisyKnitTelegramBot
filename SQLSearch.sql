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

