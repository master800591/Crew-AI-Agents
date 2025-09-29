#!/usr/bin/env python3
"""
Check system requirements and versions for Crew AI Agents
"""

import sys
import subprocess
import importlib.util

def check_python_version():
    """Check Python version."""
    print("🐍 Python Version Check")
    print(f"   Current version: {sys.version}")
    
    if sys.version_info >= (3, 8):
        print("   ✓ Python version is compatible (3.8+)")
        return True
    else:
        print("   ❌ Python 3.8+ required")
        return False

def check_package(package_name, import_name=None):
    """Check if a package is installed."""
    if import_name is None:
        import_name = package_name
    
    spec = importlib.util.find_spec(import_name)
    if spec is not None:
        try:
            module = importlib.import_module(import_name)
            version = getattr(module, '__version__', 'unknown')
            print(f"   ✓ {package_name}: {version}")
            return True
        except ImportError:
            print(f"   ❌ {package_name}: Import failed")
            return False
    else:
        print(f"   ❌ {package_name}: Not installed")
        return False

def check_ollama():
    """Check if Ollama is available."""
    print("\n🦙 Ollama Check")
    
    try:
        result = subprocess.run(['ollama', '--version'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print(f"   ✓ Ollama installed: {result.stdout.strip()}")
            
            # Check for available models
            try:
                result = subprocess.run(['ollama', 'list'], 
                                      capture_output=True, text=True, timeout=10)
                if result.returncode == 0:
                    lines = result.stdout.strip().split('\n')
                    if len(lines) > 1:  # Header + at least one model
                        print(f"   ✓ Available models: {len(lines)-1}")
                        for line in lines[1:3]:  # Show first 2 models
                            if line.strip():
                                model_name = line.split()[0]
                                print(f"     - {model_name}")
                        if len(lines) > 3:
                            print(f"     ... and {len(lines)-3} more")
                    else:
                        print("   ⚠️  No models installed. Run: ollama pull llama2")
                        return False
            except Exception as e:
                print(f"   ⚠️  Could not list models: {e}")
                
            return True
        else:
            print(f"   ❌ Ollama command failed: {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("   ❌ Ollama not found. Install from https://ollama.ai")
        return False
    except subprocess.TimeoutExpired:
        print("   ❌ Ollama command timed out")
        return False
    except Exception as e:
        print(f"   ❌ Error checking Ollama: {e}")
        return False

def check_dependencies():
    """Check required Python packages."""
    print("\n📦 Dependency Check")
    
    required_packages = [
        ('crewai', 'crewai'),
        ('langchain', 'langchain'),
        ('langchain-community', 'langchain_community'),
        ('python-decouple', 'decouple'),
    ]
    
    optional_packages = [
        ('pyttsx3', 'pyttsx3'),
        ('flask', 'flask'),
        ('cryptography', 'cryptography'),
    ]
    
    missing_required = []
    missing_optional = []
    
    print("   Required packages:")
    for package, import_name in required_packages:
        if not check_package(package, import_name):
            missing_required.append(package)
    
    print("\n   Optional packages:")
    for package, import_name in optional_packages:
        if not check_package(package, import_name):
            missing_optional.append(package)
    
    return missing_required, missing_optional

def main():
    """Main check function."""
    print("🔍 Crew AI Agents - System Requirements Check")
    print("=" * 50)
    
    all_good = True
    
    # Check Python version
    if not check_python_version():
        all_good = False
    
    # Check dependencies
    missing_required, missing_optional = check_dependencies()
    
    if missing_required:
        print(f"\n❌ Missing required packages: {', '.join(missing_required)}")
        print("   Install with: pip install " + " ".join(missing_required))
        all_good = False
    
    if missing_optional:
        print(f"\n⚠️  Missing optional packages: {', '.join(missing_optional)}")
        print("   Install with: pip install " + " ".join(missing_optional))
    
    # Check Ollama
    if not check_ollama():
        print("\n⚠️  Ollama issues detected. Some features may not work.")
    
    print("\n" + "=" * 50)
    
    if all_good and not missing_required:
        print("🎉 System ready! All requirements satisfied.")
        print("\n💡 Next steps:")
        print("   1. Run: python test_setup.py")
        print("   2. Run: python main.py")
    else:
        print("⚠️  Some requirements missing. Install them and run this check again.")
        
    return all_good

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)