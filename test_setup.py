#!/usr/bin/env python3
"""
Test script for Crew AI Agents setup
This script tests if all components can be imported and initialized correctly.
"""

import sys
import traceback

def test_imports():
    """Test if all modules can be imported successfully."""
    print("🧪 Testing imports...")
    
    try:
        print("  ✓ Testing basic Python imports...")
        import os
        import random
        from textwrap import dedent
        
        print("  ✓ Testing CrewAI import...")
        from crewai import Agent, Task, Crew
        
        print("  ✓ Testing custom modules...")
        from Agents import CustomAgents
        from Tasks import CustomTasks
        
        print("  ✓ All imports successful!")
        return True
        
    except ImportError as e:
        print(f"  ❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"  ❌ Unexpected error during import: {e}")
        traceback.print_exc()
        return False

def test_agents():
    """Test if agents can be instantiated."""
    print("\n🤖 Testing agent creation...")
    
    try:
        from Agents import CustomAgents
        agents = CustomAgents()
        
        print("  ✓ CustomAgents instance created")
        
        # Test a few agent methods
        print("  ✓ Testing agent_asmodeus...")
        agent1 = agents.agent_asmodeus()
        print(f"    - Agent role: {agent1.role}")
        
        print("  ✓ Testing agent_bael...")
        agent2 = agents.agent_bael()
        print(f"    - Agent role: {agent2.role}")
        
        print("  ✓ Agent creation successful!")
        return True
        
    except Exception as e:
        print(f"  ❌ Error creating agents: {e}")
        traceback.print_exc()
        return False

def test_tasks():
    """Test if tasks can be created."""
    print("\n📋 Testing task creation...")
    
    try:
        from Tasks import CustomTasks
        from Agents import CustomAgents
        
        tasks = CustomTasks()
        agents = CustomAgents()
        
        print("  ✓ CustomTasks instance created")
        
        # Create a simple agent for testing
        test_agent = agents.agent_asmodeus()
        
        # Test task creation
        print("  ✓ Testing task_1_name...")
        task1 = tasks.task_1_name(test_agent, "John", "Doe")
        print(f"    - Task created with agent: {task1.agent.role}")
        
        print("  ✓ Testing task_2_name...")
        task2 = tasks.task_2_name(test_agent)
        print(f"    - Task created with agent: {task2.agent.role}")
        
        print("  ✓ Task creation successful!")
        return True
        
    except Exception as e:
        print(f"  ❌ Error creating tasks: {e}")
        traceback.print_exc()
        return False

def test_crew():
    """Test if a crew can be created."""
    print("\n👥 Testing crew creation...")
    
    try:
        from crewai import Crew
        from Agents import CustomAgents
        from Tasks import CustomTasks
        
        agents = CustomAgents()
        tasks = CustomTasks()
        
        # Create agents
        agent1 = agents.agent_asmodeus()
        agent2 = agents.agent_bael()
        
        # Create tasks
        task1 = tasks.task_1_name(agent1, "Test", "User")
        task2 = tasks.task_2_name(agent2)
        
        # Create crew
        crew = Crew(
            agents=[agent1, agent2],
            tasks=[task1, task2],
            verbose=True
        )
        
        print(f"  ✓ Crew created with {len(crew.agents)} agents and {len(crew.tasks)} tasks")
        print("  ✓ Crew creation successful!")
        return True
        
    except Exception as e:
        print(f"  ❌ Error creating crew: {e}")
        traceback.print_exc()
        return False

def test_main_module():
    """Test if main module can be imported."""
    print("\n🚀 Testing main module...")
    
    try:
        import main
        print("  ✓ Main module imported successfully")
        
        # Test CustomCrew class
        custom_crew = main.CustomCrew("Test", "User")
        print("  ✓ CustomCrew instance created")
        
        print("  ✓ Main module test successful!")
        return True
        
    except Exception as e:
        print(f"  ❌ Error with main module: {e}")
        traceback.print_exc()
        return False

def main():
    """Run all tests."""
    print("🔍 Crew AI Agents - Setup Test")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_agents,
        test_tasks,
        test_crew,
        test_main_module
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"  ❌ Test failed with exception: {e}")
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Test Summary: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed! The setup is working correctly.")
        print("\n💡 Next steps:")
        print("   1. Install Ollama if not already installed")
        print("   2. Pull some models: ollama pull llama2")
        print("   3. Run the main application: python main.py")
        return True
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)