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

def display_images():
    file_list = os.listdir(app.config['UPLOAD_FOLDER'])
    file_list = [os.path.join(app.config['UPLOAD_FOLDER'], file) for file in file_list]
    sorted_pairs = sort_and_pair_images(file_list)
    return render_template('display.html', sorted_pairs=sorted_pairs)

""" 
<body>
    <div class="image-container">
        {% for question, answer in sorted_pairs %}
            <img src="{{ question }}" alt="Question Image" class="images" style="display: block; margin-left: auto; margin-right:auto;">
            <img src="{{ answer }}" alt="Answer Image" class="images" style="display: block; margin-left: auto; margin-right:auto;">
        {% endfor %}
    </div>

    <div class="button-container">
        <button onclick="plusSlides(-1)">Previous</button>
        <button onclick="plusSlides(1)">Next</button>
        <input type="button" value="Upload more images" onclick="window.location.href='/';">
    </div>

    <script>
        let slideIndex = 0;
        showSlides(slideIndex);

        // Next/previous controls
        function plusSlides(n) {
            showSlides(slideIndex += n);
        }

        function showSlides(n) {
            let i;
            let slides = document.getElementsByClassName("images");
            if (n >= slides.length) {slideIndex = 0}
            if (n < 0) {slideIndex = slides.length - 1}
            for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";
            }
            slides[slideIndex].style.display = "block";
        }
    </script>
</body>
"""
