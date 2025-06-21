# app.py

from chains.multi_agent_chain import run_consulting_chain

def main():
    print("🔷 Solvio - Akıllı Danışman v0.1\n")
    while True:
        question = input("👤 Soru: ")
        if question.lower() in ["exit", "quit"]:
            break
        answer = run_consulting_chain(question)
        print(f"\n🤖 Solvio: {answer}\n")

if __name__ == "__main__":
    main()
