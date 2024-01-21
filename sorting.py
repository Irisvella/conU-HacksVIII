def sort_and_pair_images(file_list):
    # Split files into questions and answers
    questions = sorted([f for f in file_list if "Question" in f])
    answers = sorted([f for f in file_list if "Answer" in f])

    # Pairing questions and answers
    paired_images = []
    for question in questions:
        # Extract the number from the question file name
        number = ''.join(filter(str.isdigit, question))
        # Find the corresponding answer
        answer = next((a for a in answers if number in a), None)
        if answer:
            paired_images.append((question, answer))

    return paired_images