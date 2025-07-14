### install uv in cmd
```pip install uv```

### create the project folder
```uv init AI_Travel_Planner```
- it generate automatically some useful files...

### check python available virsions in uv
```uv python list```

### python specific virsion installation ... 
```uv python install cpython-3.11.0-windows-x86_64-none```  
- this not worked. so i tried this..
```uv venv --python=3.11```

### activate 
```.venv\Scripts\activate```

### install  a packege using uv
```uv pip install langchain```

### to see the current installed packeges
```uv pip list```

### to check the all commands that i have entered
```Get-History```

## install requirements
```uv pip install -r requirements.txt```

- change the setup.py file according to chatgpt.(because of an errer when installing requirements)

