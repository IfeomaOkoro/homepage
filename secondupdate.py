import streamlit as st
from transformers import pipeline
import torch





# Function to respond to user input for the chatbot
def get_chatbot_response(user_input):
    if user_input in faq_data:
        return faq_data[user_input]
    else:
        return "I'm sorry, I don't have the answer to that question. Please contact our support team for further assistance."

# Sidebar Pages
st.sidebar.title("Pages")
pages = ["Home", "Learn More Resources", "Chatbot", "AI Summarizer"]
selected_page = st.sidebar.radio("", pages)

# Home page
if selected_page == "Home":
    st.title("Adopting AI and Machine Learning for your Business")
    st.markdown("""This free online tool provides guidance and resources to help your small and medium enterprise assess readiness and adopt AI/ML technologies in a responsible and effective manner. By answering a few short questions, you'll receive a customised AI readiness score and recommendations to get started on your AI journey.""")
    st.markdown("""Assess your AI readiness in 5 minutes""")
    st.markdown("Due to resource overload, the AI readiness assessment test is hosted [here](https://updatedaimlweb.streamlit.app/). Thank you very much.")

  



# Learn More Resources page
elif selected_page == "Learn More Resources":
    st.header('Learn More Resources')
    st.markdown("Here are some educational materials such as articles, videos, and ebooks on the adoption of AI")

    # Case Studies
    st.header("Case Studies")
    st.markdown("[Microsoft AI Customer Stories](https://www.microsoft.com/en-us/ai/customer-stories)")
    st.markdown("[Google Cloud AI Solutions](https://cloud.google.com/solutions/ai)")
    st.markdown("[IBM Watson Success Stories](https://www.ibm.com/watson/customer-stories)") 

    # Success Stories section
    st.header("Success Stories")
    st.markdown("[Microsoft AI Customer Stories](https://www.microsoft.com/en-us/ai/customer-stories)")
    st.markdown("[Google Cloud AI Solutions](https://cloud.google.com/solutions/ai)")
    st.markdown("[IBM Watson Success Stories](https://www.ibm.com/watson/customer-stories)")


    # Best Practices and Guides
    st.header("Best Practices and Guides")
    st.markdown("[AI/ML Adoption Playbook by Accenture](https://www.accenture.com/us-en/insights/artificial-intelligence/ai-adoption-playbook)")
    st.markdown("[Machine Learning Engineering Best Practices by Google](https://developers.google.com/machine-learning/guides/rules-of-ml)")
    st.markdown("[AI Adoption and Ethics Toolkit by The Alan Turing Institute](https://www.turing.ac.uk/research/research-programmes/ai-adoption-and-ethics)")

    # Research Papers and Reports
    st.header("Research Papers and Reports")
    st.markdown("[McKinsey Global Institute: Artificial Intelligence: The Next Digital Frontier](https://www.mckinsey.com/business-functions/mckinsey-digital/our-insights/artificial-intelligence-the-next-digital-frontier)")
    st.markdown("[Deloitte Insights: State of AI in the Enterprise](https://www2.deloitte.com/insights/us/en/focus/cognitive-technologies/state-of-ai-and-intelligent-automation-in-business-survey.html)")
    st.markdown("[Gartner: Hype Cycle for Artificial Intelligence](https://www.gartner.com/en/documents/3983831/hype-cycle-for-artificial-intelligence-2021)")

    # Online Courses and Tutorials
    st.header("Online Courses and Tutorials")
    st.markdown("[Coursera: AI for Everyone by deeplearning.ai](https://www.coursera.org/learn/ai-for-everyone)")
    st.markdown("[edX: Introduction to Artificial Intelligence (AI) by IBM](https://www.edx.org/professional-certificate/ibm-introduction-to-artificial-intelligence)")
    st.markdown("[Fast.ai: Practical courses on deep learning](https://www.fast.ai/)")

    # Industry Blogs and Publications
    st.header("Industry Blogs and Publications")
    st.markdown("[Towards Data Science](https://towardsdatascience.com/)")
    st.markdown("[KDnuggets](https://www.kdnuggets.com/)")
    st.markdown("[O'Reilly AI](https://www.oreilly.com/ai/)")



# Chatbot page
elif selected_page == "Chatbot":
    st.header("Chatbot")

    # Hardcoded FAQ data
    faq_data = {
        "What is AI?": "Artificial Intelligence (AI) is the field of study that focuses on creating intelligent machines that can perform tasks requiring human-like intelligence.",
        "What is machine learning?": "Machine Learning (ML) is a subset of AI that enables systems to learn and make predictions or decisions without being explicitly programmed.",
        "How can I adopt AI in my business?": "To adopt AI in your business, start by identifying potential use cases, collecting relevant data, and implementing appropriate machine learning models or algorithms.",
        "How can I adopt AI in my business?": "To adopt AI in your business, start by identifying potential use cases, collecting relevant data, and implementing appropriate machine learning models or algorithms.",
        "What are the different types of Machine Learning?": "There are three main types of Machine Learning: supervised learning (labeled data), unsupervised learning (unlabeled data), and reinforcement learning (learning through trial and error with rewards or penalties).",
        "are some real-life applications of AI and Machine Learning?": "AI and Machine Learning are used in various fields, such as healthcare (diagnosis, drug discovery), finance (fraud detection, risk assessment), transportation (autonomous vehicles), and customer service (chatbots).",
        "What are Neural Networks?": "Neural Networks are a type of machine learning model inspired by the structure of the human brain. They consist of interconnected layers of artificial neurons that process and analyze data to make predictions.",
        "What is Deep Learning?" : "Deep Learning is a subfield of Machine Learning that focuses on training large-scale neural networks with multiple layers. It has achieved remarkable success in tasks such as image recognition and natural language processing.",
        "What is the role of data in Machine Learning": "Data plays a crucial role in Machine Learning. High-quality, diverse, and well-labeled data is used to train models. The more data available, the better the model's performance and generalization.",
        "What are the ethical considerations in AI and Machine Learning?": "Ethical considerations in AI and Machine Learning involve issues such as privacy, bias, transparency, accountability, and the impact of automation on jobs. It is essential to develop and use AI responsibly and ethically.",
        "Can machines become more intelligent than humans?": "The concept of machines surpassing human intelligence, known as artificial general intelligence (AGI), is still hypothetical. While AI systems can excel in specific tasks, replicating the complexity and breadth of human intelligence remains a significant challenge.",
        "What is the AI Readiness Toolkit?": "The AI Readiness Toolkit is a comprehensive resource that focuses on six main dimensions of readiness: defining real-world problems that AI can address, leveraging the right technologies and best practices, optimizing operations and developing a strong team, generating and processing the right data, and providing granular recommendations for improvement on each dimension.",
        "How can the AI Readiness Toolkit help my small or medium enterprise?": "The AI Readiness Toolkit provides guidance and resources to help your organization assess its readiness and adopt AI/ML technologies in a responsible and effective manner. It offers recommendations, hyperlinked external resources, and a quantitative assessment to track improvements over time.",
        "What are some discussion questions for AI readiness?": "The discussion questions for AI readiness are designed to foster conversations and identify opportunities for AI adoption within your organization. They cover topics such as competitive advantages, employee feedback, operational optimization, AI investments, and data organization.",
        "How can the AI readiness checklist benefit my organization?": "The AI readiness checklist is a valuable resource to avoid AI pitfalls and ensure optimal AI utilization. It provides key questions that you and your stakeholders should be asking with every AI use case, helping you navigate through the complexities of AI adoption and engage stakeholders effectively.",
        "What are some organizational AI readiness factors?": "Organizational AI readiness factors are crucial for making purposeful decisions in the AI journey. While the search results did not provide specific factors, the study mentioned in the search results aims to conceptualize relevant factors that contribute to organizational AI readiness.",
        "How can I assess my organization's AI readiness level?": "Assessing your organization's AI readiness level involves considering factors such as your company's goals with AI, growth strategy, and competitive advantage. By evaluating these elements, you can determine your organization's readiness to embrace AI and identify areas for improvement.",
        "What is an AI Readiness Workshop?": "An AI Readiness Workshop offered by Google Cloud Consulting is a two- to three-week engagement designed to accelerate value realization from your AI efforts. It helps you understand your business objectives, benchmark your AI capabilities, and provides tailored recommendations and a roadmap for AI adoption.",
        "What is autonomous machine learning?": "Autonomous machine learning refers to the use of automated processes and algorithms that enable machines or systems to independently perform the entire process of learning from data, model building, and making decisions or predictions without human intervention.",
        "How can autonomous machine learning be beneficial for a business?": "Autonomous machine learning can be beneficial for a business in several ways:\n- It reduces the need for human intervention, saving time and resources.\n- It can process large volumes of data quickly and efficiently.\n- It improves decision-making by leveraging real-time data and insights.\n- It allows businesses to scale and adapt to changing conditions more effectively.",
        "Can you provide an example of how a business might adopt autonomous machine learning decisions?": "A business could use autonomous machine learning to automate customer support through chatbots. The chatbot could use natural language processing to understand customer inquiries, learn from past interactions, and autonomously provide appropriate responses or escalate issues to human agents when necessary.",
        "What types of businesses or industries can benefit the most from adopting autonomous machine learning?": "Industries dealing with vast amounts of data and complex decision-making can benefit the most, including finance, healthcare, manufacturing, logistics, e-commerce, and marketing.",
        "What are some key factors to consider when implementing autonomous machine learning into a business model?": "- Data quality and availability: Ensure that the data used for training and decision-making is accurate and sufficient.\n- Transparency and explainability: Understand how the autonomous system makes decisions and be able to explain its outputs.\n- Monitoring and auditing: Continuously monitor the system's performance and audit its decisions to detect and correct biases or errors.\n- Human oversight: Have a process in place to intervene or override the autonomous system if needed.",
        "How can autonomous machine learning improve decision-making processes in a business?": "Autonomous machine learning can improve decision-making by:\n- Analyzing large datasets quickly and accurately.\n- Identifying patterns, trends, and insights that humans might miss.\n- Providing real-time recommendations based on the latest data.\n- Reducing human biases and errors in decision-making.",
        "What are some potential challenges or risks that a business might face when adopting autonomous machine learning?": "- Data privacy and security concerns.\n- Lack of transparency and interpretability in the decision-making process.\n- Overreliance on autonomous systems without human oversight.\n- Ethical considerations regarding the impact of decisions made by machines.",
        "What steps can a business take to ensure the successful adoption of autonomous machine learning?": "- Start with a well-defined use case and a clear problem statement.\n- Invest in high-quality data collection and preparation.\n- Collaborate with data scientists and domain experts to build robust models.\n- Implement a gradual rollout to test and validate the system's performance.\n- Continuously monitor and update the system as needed.",
        "Can you explain the concept of a machine learning model and how it fits into an autonomous system?": "A machine learning model is a mathematical algorithm that learns patterns and relationships from data. In an autonomous system, the machine learning model is a crucial component responsible for processing data, making predictions, and providing decisions or actions without requiring human intervention.",
        "How can a business measure the success or effectiveness of its autonomous machine learning adoption?": "The success of autonomous machine learning adoption can be measured through various metrics, such as:\n- Accuracy and performance of the autonomous system compared to human decisions or alternative approaches.\n- Efficiency gains in terms of time and cost savings.\n- Reduction in errors"
        }


    # Text input for user questions
    user_question = st.text_input("Ask a question")

    # Chatbot response
    if st.button("Ask"):
        if user_question:
            chatbot_response = get_chatbot_response(user_question)
            st.text_area("Chatbot Response", value=chatbot_response, height=200, max_chars=None)
        else:
            st.warning("Please enter a question.")
    
 
    # Summarizer page
elif selected_page == "AI Summarizer":
	st.header("Text Summarizer")
	user_input = st.text_area("Enter text to summarize", height=200)
	if st.button("Summarize"):
		summarizer = pipeline("summarization")
		summary = summarizer(user_input, max_length=3000, min_length=30, do_sample=False)[0]['summary_text']
		st.subheader("Summary:")
		st.write(summary)
