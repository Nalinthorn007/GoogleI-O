import os
import base64
from google.oauth2 import service_account
from langchain_google_vertexai import ChatVertexAI
from langchain_core.messages import HumanMessage
from langchain.schema import Document
from dotenv import load_dotenv
from typing import List, Optional

class ImageContextExtractor:
    def __init__(self):
        """Initialize the ImageContextExtractor"""
        # Load environment variables
        load_dotenv()
        
        # Configuration
        self.json_key_path = r"C:\Users\Kenshin\Desktop\GoogleI-O\key.json"
        self.project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
        self.google_location = os.getenv("GOOGLE_LOCATION")
        
        # Image paths
        self.image_paths = [
            r"C:\Users\Kenshin\Desktop\GoogleI-O\Agent\Image\LALIGENCE\1.png",
            r"C:\Users\Kenshin\Desktop\GoogleI-O\Agent\Image\LALIGENCE\2.png", 
            r"C:\Users\Kenshin\Desktop\GoogleI-O\Agent\Image\LALIGENCE\3.png"
        ]
        
        self.model = None
        self._initialize_model()
    
    def _initialize_model(self):
        """Initialize the Vertex AI model"""
        try:
            # Load credentials
            credentials = service_account.Credentials.from_service_account_file(
                self.json_key_path,
                scopes=["https://www.googleapis.com/auth/cloud-platform"]
            )
            
            # Initialize Vertex AI model
            self.model = ChatVertexAI(
                model_name="gemini-2.5-flash-lite",  
                project=self.project_id,
                location=self.google_location, 
                credentials=credentials,
                temperature=0.3
            )
            print("✅ Model initialized successfully")
            
        except Exception as e:
            print(f"❌ Error initializing model: {str(e)}")
            raise
    
    def encode_image_to_base64(self, image_path: str) -> Optional[str]:
        """Convert image to base64 encoding"""
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        except Exception as e:
            print(f"Error encoding image {image_path}: {str(e)}")
            return None
    
    def create_effective_prompt(self) -> str:
        """Create a simple and direct prompt for image context extraction"""
        return """
Extract the context from this image. Describe only what you can clearly see and identify. Do not add explanations or interpretations. Be direct and factual.
"""
    
    def extract_image_context(self, image_path: str, prompt: str) -> Optional[str]:
        """Extract context from a single image"""
        try:
            # Encode image to base64
            base64_image = self.encode_image_to_base64(image_path)
            if not base64_image:
                return None
                
            # Create message with image
            message = HumanMessage(
                content=[
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        }
                    }
                ]
            )
            
            # Get response from model
            response = self.model.invoke([message])
            return response.content
            
        except Exception as e:
            print(f"Error processing image {image_path}: {str(e)}")
            return None
    
    def extract_all_contexts(self) -> List[str]:
        """Extract contexts from all images"""
        prompt = self.create_effective_prompt()
        results = {}
        contexts = []
        
        print("🔄 Starting image context extraction...")
        print("=" * 60)
        
        for i, image_path in enumerate(self.image_paths, 1):
            print(f"\n📸 Processing Image {i}: {os.path.basename(image_path)}")
            print("-" * 40)
            
            # Check if image file exists
            if not os.path.exists(image_path):
                print(f"❌ Image not found: {image_path}")
                continue
                
            # Extract context
            context = self.extract_image_context(image_path, prompt)
            
            if context:
                results[f"image_{i}"] = {
                    "path": image_path,
                    "context": context
                }
                contexts.append(context)
                print(f"✅ Successfully extracted context from Image {i}")
                print(f"📝 Context Preview: {context[:200]}...")
            else:
                print(f"❌ Failed to extract context from Image {i}")
        
        # Display all results
        print("\n" + "=" * 60)
        print("EXTRACTED CONTEXTS")
        print("=" * 60)
        
        for context in contexts:
            print(context)
            if context != contexts[-1]:  # Don't add separator after last item
                print()
        
        print(f"\n✨ Processing completed! Analyzed {len(contexts)} images successfully.")
        
        # Save results to file (optional)
        self.save_results_to_file(results)
        
        return contexts
    
    def get_contexts_as_documents(self) -> List[Document]:
        """Get contexts as LangChain Document objects"""
        contexts = self.extract_all_contexts()
        
        documents = []
        for i, context in enumerate(contexts):
            if context:
                doc = Document(
                    page_content=context,
                    metadata={
                        "source": f"laligence_image_{i+1}",
                        "type": "image_context",
                        "image_path": self.image_paths[i] if i < len(self.image_paths) else ""
                    }
                )
                documents.append(doc)
        
        return documents
    
    def get_combined_context(self) -> str:
        """Get combined context from all images"""
        contexts = self.extract_all_contexts()
        return "\n\n".join(contexts)
    
    def save_results_to_file(self, results: dict, filename: str = "extracted_contexts.txt"):
        """Save results to a text file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                for i, (key, result) in enumerate(results.items(), 1):
                    f.write(result['context'])
                    if i < len(results):  # Don't add newline after last item
                        f.write("\n\n")
                    
            print(f"💾 Results saved to: {filename}")
            
        except Exception as e:
            print(f"Error saving results: {str(e)}")


def main():
    """Main function for standalone usage"""
    try:
        extractor = ImageContextExtractor()
        contexts = extractor.extract_all_contexts()
        return contexts
    except Exception as e:
        print(f"❌ Error occurred: {str(e)}")
        return []


if __name__ == "__main__":
    main()