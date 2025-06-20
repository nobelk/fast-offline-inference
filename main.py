from max.entrypoints.llm import LLM
from max.pipelines import PipelineConfig


def main():
    model_path = "modularai/Llama-3.1-8B-Instruct-GGUF"
    pipeline_config = PipelineConfig(model_path=model_path)
    llm = LLM(pipeline_config)

    prompts = [
        "How to make a perfect cup of coffee?",
        "What are the benefits of meditation?",
        "Explain the theory of relativity in simple terms.",
    ]

    print("Generating responses...")
    responses = llm.generate(prompts, max_new_tokens=50)
    for i, (prompt, response) in enumerate(zip(prompts, responses)):
        print(f"========== Response {i} ==========")
        print(prompt + response)
        print()


if __name__ == "__main__":
    main()