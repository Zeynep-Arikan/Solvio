from agents.company_setup_agent import get_company_setup_chain
# diğer agentlar geldiğinde buraya eklenecek

def run_consulting_chain(user_question: str) -> str:
    """
    Kullanıcıdan gelen soruya göre doğru danışman agent'ını çalıştırır.
    """
    question_lower = user_question.lower()

    if any(keyword in question_lower for keyword in ["şirket", "kur", "ticaret", "limited", "anonim", "startup", "danışman"]):
        chain = get_company_setup_chain()
        return chain.run(question=user_question)

    return "Bu konuda henüz eğitilmedim. Lütfen daha fazla detay verin."
