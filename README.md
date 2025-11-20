# 🖼️ Processamento de Imagens: Equalização de Histograma & CLAHE

Este projeto implementa algoritmos de processamento digital de imagens para melhoria de contraste. Ele aborda tanto a **Equalização de Histograma Global** (implementada manualmente via cálculo da CDF) quanto a **Equalização Adaptativa Limitada pelo Contraste (CLAHE)**.

O código segue boas práticas de engenharia de software, utilizando uma estrutura modular e organizada.

## 🚀 Funcionalidades

- **Equalização de Histograma Global:**
  - Implementação "from scratch" (manual) utilizando NumPy.
  - Cálculo de histograma e Função de Distribuição Cumulativa (CDF) normalizada.
  - Ideal para correções gerais de iluminação.

- **CLAHE (Contrast Limited Adaptive Histogram Equalization):**
  - Utilização da implementação otimizada do OpenCV.
  - Melhora o contraste localmente em pequenas regiões (tiles).
  - Evita a amplificação de ruído em áreas homogêneas.

- **Estrutura Modular:** Separação clara entre lógica de negócio (`core`), utilitários (`utils`), configurações (`config`) e execução (`main`).

## 📂 Estrutura do Projeto

```text
projeto_equalizacao/
│
├── assets/                  # Imagens de entrada e resultados
│   ├── imagem_teste.png     # (Sua imagem original aqui)
│   ├── imagem_equalizada.png
│   └── imagem_clahe.png
│
├── config/                  # Configurações globais
│   ├── __pycache__.py
│   └── settings.py          # Caminhos e nomes de arquivos
│
├── core/                    # Lógica principal (Algoritmos)
│   ├── __pycache__.py
│   └── histogram.py         # Implementação do Histograma e CLAHE
│
├── utils/                   # Funções auxiliares
│   ├── __pycache__.py
│   └── io.py                # Leitura e escrita de imagens
│
|── .gitignore               
├── main.py                  # Ponto de entrada (Orquestrador)
|── README.md                # Documentação
├── requirements.txt         # Dependências do projeto
└── setup.py                 # Configuração do pacote para instalação
```

---

## 🛠️ Instalação e Configuração

- **Clonar e preparar**

        ```bash
        # Clonagem do repositório
        git clone https://github.com/Arthurg4briel/Equal_histogram.git
        cd Equal_histogram
        
        # Criação de seu ambiente virtual (se preferir, porém recomendado)
        python -m venv venv

        # Ative o ambiente
        #Para windows:
        venv\Scripts\Activate

        # Para LINUX ou MAC:
        source venv/bin/activate

        ```


- **Instalando as dependências**
        ```bash
        pip install -r requirements.txt
        pip install -e .
        ```
- **Executando o projeto**
Observação: Certifique-se que exista uma imagem em assets e que seu nome esteja em config/settings.py
        ```bash
        python main.py
        ```

