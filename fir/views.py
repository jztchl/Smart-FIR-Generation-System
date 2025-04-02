from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from .models import FIR
from .serializers import FIRSerializer
from .image_processor import extract_text, detect_objects, detect_faces
from .fir_generator import generate_fir
from .models import FIR


class FIRView(APIView):
    parser_classes = [MultiPartParser]
    queryset=FIR.objects.all()


    def get_queryset(self):
        return FIR.objects.all()

    def get(self, request):
        firs = self.get_queryset()
        return Response({"results": FIRSerializer(firs, many=True).data})


    def post(self, request):
        image = request.FILES.get("image")
        if not image:
            return Response({"error": "Image file required"}, status=400)
        crime_scene = request.data.get("crime_scene", "Unknown Location")
        more_context= request.data.get("more_context", "no context")

        
        image_path = f"media/{image.name}"
        with open(image_path, "wb") as f:
            f.write(image.read())

       
        text = extract_text(image_path)
        objects = detect_objects(image_path)
        people_identified = detect_faces(image_path)

        fir_text = generate_fir(crime_scene, objects, people_identified, text, more_context)

        
        fir = FIR.objects.create(
            crime_scene=crime_scene,
            objects_detected=objects,
            people_identified=people_identified,
            extracted_text=text,
            generated_fir=fir_text
        )

        return Response({"result":FIRSerializer(fir).data}, status=201)

