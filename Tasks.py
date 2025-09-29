from crewai import Task
from textwrap import dedent

class CustomTasks:
    def __init__(self):
        pass

    def task_1_name(self, agent, var1, var2):
        return Task(
            description=dedent(f"""
                You are working with the user {var1} {var2}.
                Your task is to provide helpful assistance and guidance based on your expertise.
                
                Please introduce yourself and explain how you can help.
                Be professional and engaging in your response.
            """),
            expected_output=dedent("""
                A professional introduction that includes:
                - Your role and capabilities
                - How you can assist the user
                - A welcoming and helpful tone
            """),
            agent=agent
        )

    def task_2_name(self, agent):
        return Task(
            description=dedent("""
                Provide a summary of your capabilities and the services you can offer.
                Focus on your unique skills and how they can benefit the user.
                
                Make sure to be specific about what you can help with.
            """),
            expected_output=dedent("""
                A clear summary that includes:
                - Specific capabilities and skills
                - Types of assistance you can provide
                - Examples of how you can help
            """),
            agent=agent
        )

    def general_assistance_task(self, agent, task_description):
        return Task(
            description=dedent(f"""
                {task_description}
                
                Please provide a thoughtful and comprehensive response.
                Use your expertise to deliver valuable insights and assistance.
            """),
            expected_output=dedent("""
                A well-structured response that:
                - Addresses the request thoroughly
                - Provides actionable insights or information
                - Maintains a professional and helpful tone
            """),
            agent=agent
        )

    def analysis_task(self, agent, subject):
        return Task(
            description=dedent(f"""
                Analyze the following subject: {subject}
                
                Provide a comprehensive analysis using your expertise.
                Include relevant insights, observations, and recommendations.
            """),
            expected_output=dedent("""
                A detailed analysis that includes:
                - Key findings and observations
                - Expert insights and interpretations
                - Relevant recommendations or next steps
            """),
            agent=agent
        )

    def research_task(self, agent, topic):
        return Task(
            description=dedent(f"""
                Research and provide information about: {topic}
                
                Use your knowledge and expertise to provide comprehensive information.
                Include relevant facts, context, and analysis.
            """),
            expected_output=dedent("""
                A comprehensive research summary that includes:
                - Key facts and information
                - Relevant context and background
                - Expert analysis and insights
            """),
            agent=agent
        )