import os
import json


# with open('C:/Users/claud/Desktop/Projeto Menu/curso.txt','r') as f:
#     curso = json.load(f)

listaCursos = list()
listaProfessores = list()


def title(opcao):
    print(opcao)


def pesquisa():
    if len(listaCursos) == 0:
        print('Não há cursos cadastrados, cadastre um curso no menu principal.')
    else:
        print('++++++++++ Pesquisa de Cursos ++++++++++\n')
        search = input('Informe o o nome do curso ou responsável pelo curso, ou ainda o nome e responsável pelo curso: ')
        for buscaCurso in listaCursos:
            if search == f'curso:{curso["nome_curso"]}':
                print(f'Foi encontrado o curso: {curso["nome_curso"]}.')
            elif search == f'professor:{professor["nome_prof"]}':
                print(f'Foi encontrado o Professor: {professor["nome_prof"]}.')
            elif search == f'curso:{curso["nome_curso"]} professor:{professor["nome_prof"]} ':  #or search == f'professor:{professor["nome_prof"]}':
                print(f'Foi encontrado o curso: {curso["nome_curso"]}. e o professor: {professor["nome_prof"]}')
            else:
                print('Curso/professor não localizado!')

            # elif search.__contains__(curso["nome_curso"]) and buscaCurso.__contains__(professor["nome_prof"]):
            #     print(f'Foi encontrado o curso: {curso["nome_curso"]}. e o professor: {professor["nome_prof"]}')


def excluir():
    os.system('cls')
    print('++++++++++ Exclusão de Professores ++++++++++\n')
    print('Matrícula'.ljust(15), 'Nome'.ljust(8), '- Formação'.ljust(15), '- CPF'.ljust(15),  "\n")
    print(professor["mat_prof"].ljust(18), end='')
    print(professor["nome_prof"].ljust(12), end='')
    print(professor["formacao_prof"].ljust(15), end='')
    print(professor["cpf_prof"].ljust(18), "\n", end='')
    search = input('Informe o nome ou a matricula do professor a ser deletado: ')
    for buscaProf in listaProfessores:
        if search == professor["nome_prof"] or search == professor["mat_prof"]:
            print(f'Você informou o professor: {professor["nome_prof"]}', "\n", end='')
            answer = str(input('Tem certeza que deseja deletar? (S/N)')).strip()[0].lower()
            if answer == 's':
                listaProfessores.remove(professor)
                print('Professor deletado com sucesso!')
            else:
                break


def carregarCurso():
    with open('curso.json', 'r') as loadCurso:
        curso = json.load(loadCurso)
        listaCursos.append(curso)



def carregarProfessor():
    with open('professor.json', 'r') as loadProfessor:
        professor = json.load(loadProfessor)
        listaProfessores.append(professor)






while True:
    os.system('cls')
    answer = 's'
    print('*'*35)
    print('Sistema de Gerenciamento Estudantil')
    print('*'*35)
    print('-------- Menu Inicial -----------')
    title('Opções do Sistema')
    title('1 - Listar Cursos')
    title('2 - Cadastrar Curso')
    title('3 - Pesquisar Cursos')
    title('4 - Editar Cursos')
    title('5 - Cadastrar Professor')
    title('6 - Listar Professores')
    title('7 - Excluir Professor')
    title('8 - Encerrar Programa')
    option = int(input('Opção: '))
    os.system('cls')
    match option:
        
        # Listar Cursos
        case 1:
            carregarCurso()
            carregarProfessor()

            print('++++++++++ Lista dos Cursos ++++++++++\n')
            print('Código'.ljust(8), '- Curso'.ljust(15), '- Créditos'.ljust(15), '- Responsável'.ljust(20), "\n")
            for curso in listaCursos:
                print(curso["codigo_curso"].ljust(12), end='')
                print(curso["nome_curso"].ljust(15), end='')
                print(curso["total_creditos"].ljust(18), end='')
                for professor in listaProfessores:
                    print(professor["nome_prof"].ljust(20), "\n", end='')

            optionInside = int(input("\n"'Para continuar Digite : 1 - Pesquisar, 2 - Voltar: '))
            match optionInside:
                case 1:
                    answer == 's'
                    while answer == 's':
                        pesquisa()
                        answer = input("Deseja continuar pesquisando cursos? (S/N): ").strip()[0].lower()
                case 2:
                    continue

        # Cadastro de Cursos
        case 2:
            if len(listaCursos) != 0:
                carregarCurso()
            if len(listaProfessores) != 0:
                carregarProfessor()
            os.system('cls')
            answer = 's'
            while answer.lower() == 's':
                os.system('cls')
                print('*' * 8, 'Cadastro de Curso', '*' * 8)
                curso = dict()

                codigoCurso = input("Código do curso: ")

                find = False
                for search_curso in listaCursos:
                    if codigoCurso == search_curso["codigo_curso"]:
                        print('Curso já cadastrado')
                        find = True
                        break
                if not find:
                    curso["codigo_curso"] = codigoCurso
                    curso["nome_curso"] = input("Nome do curso: ")
                    curso["total_creditos"] = input("Total de créditos: ")
                    if len(listaProfessores) == 0:
                        cadastroProfInCurso = input("Não há professores cadastrados, deseja cadastrar (S/N)? ")

                        if cadastroProfInCurso == 's':
                            os.system('cls')
                            answer = 's'
                            while answer.lower() == 's':
                                os.system('cls')
                                print('*' * 8, 'Cadastro de Professores', '*' * 8)
                                professor = dict()
                                matProf = input("Informe a matrícula do professor: ")

                                find = False
                                for search_prof in listaProfessores:
                                    if matProf == search_prof["mat_prof"]:
                                        print('Professor já cadastrado')
                                        find = True
                                        break

                                if not find:
                                    professor["mat_prof"] = matProf
                                    professor["nome_prof"] = input("Nome do Professor: ")
                                    professor["cpf_prof"] = input("Cpf do Professor: ")
                                    professor["formacao_prof"] = input("Formação do Professor: ")

                                listaProfessores.append(professor)
                                listaCursos.append(curso)
                                answer = input("Deseja continuar cadastrando Professores? (S/N): ").strip()[0].lower()
                            else:
                                continue
                    else:
                        professor["nome_prof"] = input("Nome do Professor: ")
                        professor["cpf_prof"] = input("Cpf do Professor: ")
                        professor["formacao_prof"] = input("Formação do Professor: ")

                        # curso["professor_responsavel"] = input(professor["mat_prof"],'Informe a matrícula do professor: ')
                        # input("Professor Responsável: ")

                #listaCursos.append(curso)
                answer = input("Deseja continuar cadastrando cursos? (S/N): ").strip()[0].lower()

            with open('curso.json', 'w') as arquivo_curso:
                json.dump(curso, arquivo_curso)


            with open('professor.json', 'w') as arquivo_professor:
                json.dump(professor, arquivo_professor)

        # Pesquisar Cursos
        case 3:
           pesquisa()


        # Editar Cursos
        case 4:
            answer = 's'
            while answer == 's':
                os.system('cls')
                if len(listaCursos) == 0:
                    print('Não há cursos cadastrados, cadastre um curso utilizando o menu inicial! ')
                    break
                else:
                    print('++++++++++ Edição de Cursos ++++++++++\n')
                    editCurso = None
                    codigoCurso = input("Código do curso: ")
                    for search_curso in listaCursos:
                        if codigoCurso == search_curso["codigo_curso"]:
                            editCurso = search_curso
                            print('Foi encontrado o curso ** {} ** com os dados informados\n'.format(curso["nome_curso"]))
                            ask = input('Tem certeza que deseja editar? (S/N): ').strip()[0].lower()
                            if ask == 's':
                                curso["nome_curso"] = input("Digite o novo nome do curso: ")
                                curso["total_creditos"] = input("Digite o novo total de créditos: ")
                                professor["nome_prof"] = input("Digite o novo nome do responsável: ")
                                print("Edição Realizada com Sucesso!")
                                break
                            else:
                                print('Edição cancelada!')
                        else:
                            print('Curso inexistente!')

                answer = input("Deseja editando cursos? (S/N): ").strip()[0].lower()

        # Cadastrar Professor
        case 5:
            os.system('cls')
            answer = 's'
            while answer.lower() == 's':
                os.system('cls')
                print('*'*8,'Cadastro de Professores','*'*8)
                professor = dict()
                professor_json = json.dumps(professor)
                matProf = input("Informe a matrícula do professor: ")

                find = False
                for search_prof in listaProfessores:
                    if matProf == search_prof["mat_prof"]:
                        print('Professor já cadastrado')
                        find = True
                        break

                if not find:
                    professor["mat_prof"] = matProf
                    professor["nome_prof"] = input("Nome do Professor: ")
                    professor["cpf_prof"] = input("Cpf do Professor: ")
                    professor["formacao_prof"] = input("Formação do Professor: ")

                listaProfessores.append(professor)         
                answer = input("Deseja continuar cadastrando Professores? (S/N): ")      

        # Pesquisar Professor
        case 6:
            if len(listaProfessores) == 0:
                print('Não há professores cadastrados')
            else:
                os.system('cls')
                print('Matrícula'.ljust(15), 'Nome'.ljust(8),  "\n")
                for professor in listaProfessores:
                    print(professor["mat_prof"].ljust(12), end='')
                    print(professor["nome_prof"].ljust(20), "\n", end='')
                    # print(professor["formacao_prof"].ljust(15), end='')
                    # print(professor["cpf_prof"].ljust(18), "\n", end='')
            answer = str(input('Digite 1 para voltar e 2 para pesquisar: '))
            if answer == '2':
                pesqProf = input('Informe o nome ou a matrícula do professor: ')
                for professor in listaProfessores:
                    if pesqProf == professor["nome_prof"] or pesqProf == professor["mat_prof"]:
                        print(f'Foi encontrado o professor: {professor["nome_prof"]}, com formacão em: {professor["formacao_prof"]}, e cpf: {professor["cpf_prof"]}')
                    else:
                        print('Professor não encontrado! ')
            elif answer == '1':
                continue

        case 7:
            excluir()

        #Encerrar Programa
        case 8:
            print('Encerrando Programa...')
            break




    input('\nPressione QUALQUER TECLA para continuar...')