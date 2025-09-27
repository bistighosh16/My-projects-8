#include <stdio.h>
#include <stdlib.h>
struct Student {
    int id;
    char name[50];
    int age;
    float grade;
};
void readStudentsFromFile(FILE *file, struct Student students[], int *count) {
    while (fscanf(file, "%d %49s %d %f", &students[*count].id, students[*count].name,
                  &students[*count].age, &students[*count].grade) != EOF) {
        (*count)++;
    }
}
void printStudentDatabase(struct Student students[], int count) {
    printf("----------------------------------------------------\n");
    printf("| %-4s | %-20s | %-3s | %-5s |\n", "ID", "Name", "Age", "Grade");
    printf("----------------------------------------------------\n");
    for (int i = 0; i < count; i++) {
        printf("| %-4d | %-20s | %-3d | %-5.2f |\n", students[i].id, students[i].name,
               students[i].age, students[i].grade);
    }
    printf("----------------------------------------------------\n");
}
int main() {
    FILE *file = fopen("TextExample.txt", "r");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    struct Student students[100];
    int studentCount = 0;
    readStudentsFromFile(file, students, &studentCount);
    fclose(file);
    printStudentDatabase(students, studentCount);
    return 0;
}
