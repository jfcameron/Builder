//Example file
#include "texture.h"

using namespace gfx;

static int convertURIToTextureResource(const std::string &aURI)
{
    return 0;
}

Texture::Texture(const std::string &aURI)
: m_Handle(convertURIToTextureResource(aURI))
{}
