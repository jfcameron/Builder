//Example file
#include <string>

namespace gfx
{
    class Texture
    {
        using GFXHandle = int;
    public:
        enum class WrapMode
        {
            None,
            Horizontal,
            Vertical,
            Both
        };
        
        Texture() = delete;
        Texture(const std::string &aURI);
    private:
        GFXHandle m_Handle = 0;
        WrapMode m_WrapMode = WrapMode::None;
    };
}
