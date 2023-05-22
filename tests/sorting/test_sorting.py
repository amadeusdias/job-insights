from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    initial_list = [
        {
            "title": "Web developer",
            "min_salary": "invalid",
            " max_salary": "invalid",
        },
        {"title": "Front end developer", "min_salary": "1000"},
        {"title": "Back end developer", "max_salary": "3000"},
        {
            "title": "Full stack end developer",
            "min_salary": "4000",
            " max_salary": "8000",
        },
    ]

    assert sort_by(initial_list, "max_salary") == initial_list
