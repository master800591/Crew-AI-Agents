# Crew-AI-Agents

A comprehensive collection of CrewAI agents powered by Ollama, featuring 375+ unique agents with diverse roles and capabilities.

## Overview

This repository contains a large set of CrewAI agents that can be used for different tasks and projects. All agents are configured to work with Ollama local language models, making this a fully self-hosted AI solution.

**Total agents: 375**

## Features

- 375+ pre-configured CrewAI agents with unique personalities and roles
- Ollama integration for local LLM execution 
- Flexible task system for agent coordination
- Comprehensive agent management system
- Easy-to-use crew creation and execution

## Quick Start

### Prerequisites

1. **Install Ollama** (if not already installed):
   ```bash
   # Visit https://ollama.ai for installation instructions
   curl -fsSL https://ollama.ai/install.sh | sh
   ```

2. **Pull required models**:
   ```bash
   ollama pull llama2
   ollama pull codellama
   ```

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/master800591/Crew-AI-Agents.git
   cd Crew-AI-Agents
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Test the setup**:
   ```bash
   python test_setup.py
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

## Configuration

### Environment Variables

Copy `.env` file and configure as needed:

```bash
# Ollama Configuration (default)
OLLAMA_BASE_URL=http://localhost:11434

# OpenAI Configuration (optional)
# OPENAI_API_KEY=your_openai_api_key_here
# OPENAI_ORGANIZATION_ID=your_openai_org_id_here
```

### Available Models

The system supports multiple Ollama models with automatic fallbacks:

- `llama2` (primary)
- `codellama` (for coding tasks)
- `llama2-uncensored` (optional)
- `solar` (optional)
- `openhermes` (optional)
- And more...

## Usage

### Basic Example

```python
from main import CustomCrew

# Create a crew with user information
crew = CustomCrew("John", "Doe")

# Execute the crew
result = crew.run()
print(result)
```

### Custom Agent Usage

```python
from Agents import CustomAgents
from Tasks import CustomTasks
from crewai import Crew

# Initialize
agents = CustomAgents()
tasks = CustomTasks()

# Create specific agents
asmodeus = agents.agent_asmodeus()
bael = agents.agent_bael()

# Create tasks
task1 = tasks.task_1_name(asmodeus, "John", "Doe")
task2 = tasks.task_2_name(bael)

# Create and run crew
crew = Crew(
    agents=[asmodeus, bael],
    tasks=[task1, task2],
    verbose=True
)

result = crew.kickoff()
```

## File Structure

- `main.py` - Main application entry point
- `Agents.py` - CustomAgents class with 375+ agent definitions
- `Tasks.py` - CustomTasks class with task templates
- `Create_agents.py` - Agent generation utilities
- `requirements.txt` - Python dependencies
- `test_setup.py` - Setup verification script
- `CSV/` - Agent data and configuration files

## Agent Categories

Agents are organized into several categories:

- **Mythological**: Demons, angels, gods from various pantheons
- **Executive**: Business leadership roles (CEO, CTO, CFO, etc.)
- **Departmental**: Specialized department managers
- **Employees**: Various professional roles

**Agent names can be found in**: `CSV/Agent_LIST.csv`  
**Agent loading utilities**: `CSV/Agent_load.csv`

## Troubleshooting

### Common Issues

1. **Ollama not running**: Make sure Ollama is installed and running
   ```bash
   ollama serve
   ```

2. **Models not available**: Pull required models
   ```bash
   ollama pull llama2
   ```

3. **Import errors**: Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. **Test setup**: Run the test script
   ```bash
   python test_setup.py
   ```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `python test_setup.py`
5. Submit a pull request

## License

This project is open source. See LICENSE file for details.

## Support

If you encounter issues:
1. Run `python test_setup.py` to diagnose problems
2. Check that Ollama is running and models are available
3. Verify all dependencies are installed
4. Open an issue with error details

