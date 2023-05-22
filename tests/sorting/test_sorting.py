from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    initial_list = [
        {
            "date_posted": "2023-05-18",
            "min_salary": "4000",
            "max_salary": "8000",
        },
        {
            "date_posted": "2023-05-20",
            "min_salary": "1000",
            "max_salary": "3500",
        },
        {
            "date_posted": "2023-05-19",
            "min_salary": "500",
            "max_salary": "3000",
        },
        {
            "date_posted": "2023-05-21",
            "min_salary": "400",
            "max_salary": "2500",
        },
    ]

    min_salary_list = [
        {
            "date_posted": "2023-05-21",
            "min_salary": "400",
            "max_salary": "2500",
        },
        {
            "date_posted": "2023-05-19",
            "min_salary": "500",
            "max_salary": "3000",
        },
        {
            "date_posted": "2023-05-20",
            "min_salary": "1000",
            "max_salary": "3500",
        },
        {
            "date_posted": "2023-05-18",
            "min_salary": "4000",
            "max_salary": "8000",
        },
    ]

    max_salary_list = [
        {
            "date_posted": "2023-05-18",
            "min_salary": "4000",
            "max_salary": "8000",
        },
        {
            "date_posted": "2023-05-20",
            "min_salary": "1000",
            "max_salary": "3500",
        },
        {
            "date_posted": "2023-05-19",
            "min_salary": "500",
            "max_salary": "3000",
        },
        {
            "date_posted": "2023-05-21",
            "min_salary": "400",
            "max_salary": "2500",
        },
    ]

    date_posted_list = [
        {
            "date_posted": "2023-05-21",
            "min_salary": "400",
            "max_salary": "2500",
        },
        {
            "date_posted": "2023-05-20",
            "min_salary": "1000",
            "max_salary": "3500",
        },
        {
            "date_posted": "2023-05-19",
            "min_salary": "500",
            "max_salary": "3000",
        },
        {
            "date_posted": "2023-05-18",
            "min_salary": "4000",
            "max_salary": "8000",
        },
    ]

    sort_by(initial_list, "min_salary")
    assert initial_list == min_salary_list
    sort_by(initial_list, "max_salary")
    assert initial_list == max_salary_list
    sort_by(initial_list, "date_posted")
    assert initial_list == date_posted_list
