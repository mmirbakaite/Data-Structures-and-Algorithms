#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

struct OffObject {
    std::vector<std::string> vertices;
    std::vector<std::string> faces;
};

OffObject ReadOffFile(const std::string& filename) {
    std::ifstream file(filename);

    if (!file.is_open()) {
        std::cerr << "Unable to open file: " << filename << std::endl;
        exit(1);
    }

    OffObject object;
    std::string line;
    getline(file, line); // Skip OFF

    int verticesCount, facesCount, edgesCount;
    file >> verticesCount >> facesCount >> edgesCount;
    file.ignore();  // Ignore the rest of the line

    // Read vertices
    for (int i = 0; i < verticesCount; ++i) {
        getline(file, line);
        object.vertices.push_back(line);
    }

    // Read faces and update indices
    for (int i = 0; i < facesCount; ++i) {
        getline(file, line);
        object.faces.push_back(line);
    }

    return object;
}

void WriteOffFile(const std::string& filename, const OffObject& object) {
    std::ofstream file(filename);

    if (!file.is_open()) {
        std::cerr << "Unable to open file: " << filename << std::endl;
        exit(1);
    }

    file << "OFF\n";
    file << object.vertices.size() << " " << object.faces.size() << " 0\n";

    for (const auto& vertex : object.vertices)
        file << vertex << "\n";

    for (const auto& face : object.faces)
        file << face << "\n";
}

OffObject MergeOffFiles(const OffObject& object1, const OffObject& object2) {
    OffObject mergedObject = object1;

    // Add vertices from object2
    for (const auto& vertex : object2.vertices)
        mergedObject.vertices.push_back(vertex);

    // Add faces from object2, adjusting indices
    int offset = object1.vertices.size();
    for (const auto& face : object2.faces) {
        std::istringstream iss(face);
        std::ostringstream oss;
        int count, index;

        iss >> count;
        oss << count;
        for (int i = 0; i < count; ++i) {
            iss >> index;
            oss << " " << index + offset;
        }

        mergedObject.faces.push_back(oss.str());
    }

    return mergedObject;
}

int main() {
    OffObject object1 = ReadOffFile("file1.off");
    OffObject object2 = ReadOffFile("merged.off");

    OffObject mergedObject = MergeOffFiles(object1, object2);

    WriteOffFile("mergedd.off", mergedObject);

    return 0;
}


