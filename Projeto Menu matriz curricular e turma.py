import os
import json
import os.path
import itertools
from datetime import date

listaCursos = carregarDadosCurso('curso')
listaProfessores = carregarDadosProfessor('professor')
listaSemestre = carregarDadosSemestre('semestre')


def title(opcao):
    print(opcao)


def excluir():
    os.system('cls')
    print('++++++++++ Exclusão de Professores ++++++++++\n')
    print('Matrícula'.ljust(15), 'Nome'.ljust(8), '- Formação'.ljust(15), '- CPF'.ljust(15), "\n")
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


def pesquisa():
    # if len(listaCursos) == 0:
    #     print('Não há cursos cadastrados, cadastre um curso no menu principal.')
    # else:
    print('++++++++++ Pesquisa de Cursos ++++++++++\n')
    search = input('Informe o o nome do curso ou responsável pelo curso, ou ainda o nome e responsável pelo curso: ')
    find = False
    for curso, professor in zip(listaCursos, listaProfessores):
        if search == curso["nome_curso"]:
            print(f'Foi encontrado o curso: {curso["nome_curso"]}.')
            find = True
            break
        elif search == professor["nome_prof"]:
            print(f'Foi encontrado o Professor: {professor["nome_prof"]}.')
            find = True
            break
        elif search == f'curso:{curso["nome_curso"]} professor:{professor["nome_prof"]} ':  # or search == f'professor:{professor["nome_prof"]}':
            print(f'Foi encontrado o curso: {curso["nome_curso"]}. e o professor: {professor["nome_prof"]}')
            find = True
            break

    if not find:
        print('Curso/professor não localizado!')



def semestreLetivo():
    while True:
        os.system('cls')
        answer = 's'
        print('*' * 35)
        print('Sistema de Gerenciamento Estudantil')
        print('*' * 35)
        print('-------- Menu de Semestres -----------')
        title('Opções do Sistema')
        print('1 - Criar semestre')
        print('2 - Listar semestres')
        print('3 - Editar semestres')
        print('4 - Deletar semestres')
        print('5 - Voltar')

        match option:

            #Criar semestre
            case 1:
                os.system('cls')
                answer = 's'
                while answer.lower() == 's':
                    os.system('cls')
                    print('*' * 8, 'Cadastro de Semestre', '*' * 8)
                    semestre = dict()

                    semestre["ano_semestre"] = input("Informe o Ano do semestre: ")
                    semestre["semestre_letivo"]  = input('Informe o semestre letivo: ')

                    dataInicio = int(input("Informe a data de início do semestre: ")).split("/")
                    semestre["semestre_inicio"] = dataInicio(int(dataInicio[2]), int(dataInicio[1]), int(dataInicio[0])).isoformat()

                    dataFim = int(input("Informe a data do fim do semestre: ")).split("/")
                    semestre["semestre_fim"] = dataFim(int(dataFim[2]), int(dataFim[1]), int(dataFim[0])).isoformat()


                    listaSemestre.append(semestre)

                    answer = input("Deseja continuar cadastrando semestres? (S/N): ").strip()[0].lower()

             #Listar semestres
            case 2:


            #Editar semestres
            case 3:



            #Deletar semestres
            case 4:



            #voltar
            case 5:
                break





def carregarDadosCurso(nome_arquivo):
    dados = None
    if nome_arquivo == 'curso':
        arquivo = nome_arquivo + '.json'
        if os.path.exists(arquivo):
            with open(arquivo, 'r') as json_file:
                dados = json.load(json_file)
        else:
            dados = list()

    return dados


def carregarDadosProfessor(nome_arquivo):
    dados = None
    if nome_arquivo == 'professor':
        arquivo = nome_arquivo + '.json'
        if os.path.exists(arquivo):
            with open(arquivo, 'r') as json_file:
                dados = json.load(json_file)
        else:
            dados = list()

    return dados


def salvarDadosProfessor(nome, lista):
    if nome == 'professor':
        with open(nome + '.json', 'w') as json_file:
            json.dump(lista, json_file)


def salvarDadosCurso(nome, lista):
    if nome == 'curso':
        with open(nome + '.json', 'w') as json_file:
            json.dump(lista, json_file)




while True:
    os.system('cls')
    answer = 's'
    print('*' * 35)
    print('Sistema de Gerenciamento Estudantil')
    print('*' * 35)
    print('-------- Menu Inicial -----------')
    title('Opções do Sistema')
    title('1 - Listar Cursos')
    title('2 - Cadastrar Curso')
    title('3 - Pesquisar Cursos')
    title('4 - Editar Cursos')
    title('5 - Cadastrar Professor')
    title('6 - Listar Professores')
    title('7 - Excluir Professor')
    title('8 - Semestre Letivo')
    title('9 - Encerrar Programa')
    option = int(input('Opção: '))
    os.system('cls')
    match option:
        # Listar Cursos
        case 1:
            print('++++++++++ Lista dos Cursos ++++++++++\n')
            print('Código'.ljust(8), '- Curso'.ljust(25), '- Créditos'.ljust(20), '- Responsável'.ljust(20), "\n")
            for curso, professor in zip(listaCursos, listaProfessores):
                print(curso["codigo_curso"].ljust(10), end='')
                print(curso["nome_curso"].ljust(27), end='')
                print(curso["total_creditos"].ljust(21), end='')
                print(professor["nome_prof"].ljust(20), "\n", end='')

            optionInside = int(input("\n"'Para continuar digite   (1)Pesquisar ou (2)Voltar: '))
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
            os.system('cls')
            answer = 's'
            while answer.lower() == 's':
                os.system('cls')
                print('*' * 8, 'Cadastro de Curso', '*' * 8)
                curso = dict()
                professor = dict()
                codigoCurso = input("Código do curso: ")

                find = False
                for curso in listaCursos:
                    if codigoCurso == curso["codigo_curso"]:
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
                            # while answer.lower() == 's':
                            os.system('cls')
                            print('*' * 8, 'Cadastro de Professores', '*' * 8)
                            professor = dict()
                            matricula = input("Informe a matrícula do professor: ")

                            find = False
                            for search_prof in listaProfessores:
                                if matricula == search_prof["mat_prof"]:
                                    print('Professor já cadastrado')
                                    find = True
                                    break

                            if not find:
                                professor["mat_prof"] = matricula
                                professor["nome_prof"] = input("Nome do Professor: ")
                                professor["cpf_prof"] = input("Cpf do Professor: ")
                                professor["formacao_prof"] = input("Formação do Professor: ")

                                listaProfessores.append(professor)
                                listaCursos.append(curso)

                                    # answer = input("Deseja continuar cadastrando Professores? (S/N): ").strip()[0].lower()

                            else:
                                continue
                    else:
                        professor["mat_prof"] = input("Informe a matrícula do professor: ")
                        professor["nome_prof"] = input("Nome do Professor: ")
                        professor["cpf_prof"] = input("Cpf do Professor: ")
                        professor["formacao_prof"] = input("Formação do Professor: ")


                        listaProfessores.append(professor)
                        listaCursos.append(curso)
                        answer = input("Deseja continuar cadastrando Professores? (S/N): ").strip()[0].lower()

                answer = input("Deseja continuar cadastrando cursos? (S/N): ").strip()[0].lower()

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
                    for curso, professor in zip(listaCursos, listaProfessores):
                        if codigoCurso == curso["codigo_curso"]:
                            editCurso = curso
                            print(
                                'Foi encontrado o curso ** {} ** com os dados informados\n'.format(curso["nome_curso"]))
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
                print('*' * 8, 'Cadastro de Professores', '*' * 8)
                professor = dict()
                matricula = input("Informe a matrícula do professor: ")

                find = False
                for search_prof in listaProfessores:
                    if matricula == search_prof["mat_prof"]:
                        print('Professor já cadastrado')
                        find = True
                        break

                if not find:
                    professor["mat_prof"] = matricula
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
                print('Matrícula'.ljust(14), 'Nome'.ljust(17), 'Formação'.ljust(20), 'CPF'.ljust(14), "\n")
                for professor in listaProfessores:
                    print(professor["mat_prof"].ljust(15), end='')
                    print(professor["nome_prof"].ljust(18), end='')
                    print(professor["formacao_prof"].ljust(21), end='')
                    print(professor["cpf_prof"].ljust(18), "\n", end='')
            answer = str(input('Digite 1 para voltar e 2 para pesquisar: '))
            if answer == '2':
                pesqProf = input('Informe o nome ou a matrícula do professor: ')
                for professor in listaProfessores:
                    if pesqProf == professor["nome_prof"] or pesqProf == professor["mat_prof"]:
                        print(
                            f'Foi encontrado o professor: {professor["nome_prof"]}, com formacão em: {professor["formacao_prof"]}, e cpf: {professor["cpf_prof"]}')

            elif answer == '1':
                continue

        case 7:
            os.system('cls')
            print('++++++++++ Exclusão de Professores ++++++++++\n')
            print('Matrícula'.ljust(15), 'Nome'.ljust(8), '- Formação'.ljust(15), '- CPF'.ljust(15), "\n")
            for professor in listaProfessores:
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
            # excluir()

        case 8:
            semestreLetivo()

        # Encerrar Programa
        case 9:
            salvarDadosCurso('curso', listaCursos)
            salvarDadosProfessor('professor', listaProfessores)
            print('Salvando informações e encerrando Programa...')
            break

    input('\nPressione QUALQUER TECLA para continuar...')
