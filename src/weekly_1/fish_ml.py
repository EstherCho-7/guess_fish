from sklearn.neighbors import KNeighborsClassifier
import numpy as np

def guess_fish():
    fish_data=[]
    fish_target=[]

    k=5
    model=KNeighborsClassifier(n_neighbors=k)

    while True:
        length=float(input("물고기의 길이: "))
        weight=float(input("물고기의 무게: "))

        if fish_data:
            if len(fish_data)<k:
                model.set_params(k=len(fish_data))

            prediction=model.predict([[length, weight]])
            predicted_type="도미" if prediction[0]==1 else "빙어"
        
            print(f"입력하신 물고기는 {predicted_type}")

        else:
            predicted_type="도미" if np.random.choice([0, 1])==1 else "빙어"
            print(f"입력하신 물고기는 {predicted_type}")

        answer=input("맞습니까? 맞으면 T, 아니라면 F를 입력해주시기 바랍니다.: ")

        if answer=="T":
            target=1 if predicted_type=="도미" else 0
            fish_data.append([length, weight])
            fish_target.append(target)
            print("저는 물고기 민수입니다.")
        elif answer=="F":
            target=0 if predicted_type=="도미" else 1
            fish_data.append([length, weight])
            fish_target.append(target)
            print("저는 물고기 준수입니다.")
        else:
            print("잘못 입력하셨습니다. 다시 길이부터 묻겠습니다.")
            continue
        
        model.fit(fish_data, fish_target)
