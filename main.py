from face_detection import FaceDetection


def main():
    """
    Just put in the inputDirectory absolute path
    and the output directory absolute path 
    """

    inputDirectory = '/home/mr-paul/atmp/aaproject/scripts/sad_raw'
    outputDirectory = '/home/mr-paul/atmp/aaproject/scripts/sad_faces'

    # detects all faces from all images in inputDirectory and outputs
    # to outputDirectory
    FaceDetection.extractFaces(
        inputDirectory=inputDirectory, outputDirectory=outputDirectory)


if __name__ == "__main__":
    main()
