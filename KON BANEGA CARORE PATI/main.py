import multiprocessing
import time

def ask_question(ques, correct_option, k, l_l):
    print(f"\n Question {k}: {ques[0]}")
    print(f"A. {ques[1]}")
    print(f"B. {ques[2]}")
    print(f"C. {ques[3]}")
    print(f"D. {ques[4]}")
    print("TYPE : 1 for A, 2 for B, 3 for C, 4 for D\n")

    time_up_flag = multiprocessing.Value('i', 0)
    timer_proc = multiprocessing.Process(target=run_timer_window, args=(10, time_up_flag))
    timer_proc.start()

    try:
        print("LIFE LINES LEFT:", l_l)
        inp = input("Your answer (1-4) OR 'll' to use Lifeline (auto skip): ").strip()
    except:
        inp = None

    timer_proc.terminate()
    timer_proc.join()

    if time_up_flag.value == 1:
        print("Time's up! You didn’t answer in time.")
        return False, l_l

    if inp == "ll":
        if l_l > 0:
            print("Lifeline used! Auto-skipping to correct answer...")
            l_l -= 1
            answer = correct_option
        else:
            print("No lifelines left!")
            return False, l_l
    else:
        try:
            answer = int(inp)
        except:
            print("Invalid input.")
            return False, l_l

    if answer == correct_option:
        print("Correct Answer!")
        return True, l_l
    else:
        print("Wrong Answer.")
        return False, l_l

def run_timer_window(seconds, flag):
    import timer_window
    timer_window.countdown_gui(seconds, flag)


ques_ans = [
    ["Who is India's current President?", "Droupadi Murmu", "Rajnath Singh", "Narendra Modi", "Manmohan Singh", 1],
    ["Which planet is known as the Red Planet?", "Venus", "Mars", "Jupiter", "Saturn", 2],
    ["Who wrote the Indian National Anthem?", "Bankim Chandra Chatterjee", "Subhash Chandra Bose", "Rabindranath Tagore", "Sardar Patel", 3],
    ["What is the chemical symbol for Gold?", "Au", "Ag", "Gd", "Go", 1],
    ["Which Indian state has the highest literacy rate?", "Kerala", "Tamil Nadu", "Goa", "Maharashtra", 1],
    ["Who invented the World Wide Web?", "Bill Gates", "Steve Jobs", "Tim Berners-Lee", "Mark Zuckerberg", 3],
    ["In which year did India win its first Cricket World Cup?", "1983", "2003", "2011", "1975", 1],
    ["Which is the longest river in the world?", "Amazon", "Yangtze", "Nile", "Mississippi", 3],
    ["Which Nobel Prize category was first awarded to an Indian?", "Peace", "Literature", "Physics", "Economics", 2],
    ["What is the name of the first artificial Earth satellite?", "Sputnik 1", "Voyager", "Aryabhata", "Apollo 11", 1]
]

money = [1000000, 5000000, 7500000, 10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000]

def main():
    l_l = 2
    score = 0
    print("Welcome to 'KON BANEGA CARORE PATI....!'")
    for i, q in enumerate(ques_ans):
        result, l_l = ask_question(q, q[5], i + 1, l_l)
        if not result:
            break
        print(f"You won ₹{money[i]:,}\n")
        score += money[i]
    print(f"\nGame Over! Total Earnings: ₹{score:,}")

if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')
    main()