from datasets import load_dataset


if __name__ == '__main__':
    dataset = load_dataset("readerbench/ro-text-summarization")
    dataset_guvern =[]
    dataset_educatie =[]
    dataset_social =[]

    for category, content in zip(dataset['train'].data['Category'], dataset['train'].data['Content']):
        if (str(category) == "guvern"):
            dataset_guvern.append([category, content])
        if (str(category) == "educatie"):
            dataset_educatie.append([category, content])
        if (str(category) == "social"):
            dataset_social.append([category, content])
    for elem in dataset_guvern:
        print("category:",elem[0], "content:" , elem[1])
    for elem in dataset_educatie:
        print("category:",elem[0], "content:" , elem[1])
    for elem in dataset_social:
        print("category:",elem[0], "content:" , elem[1])
