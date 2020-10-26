# Documentation: https://docs.brew.sh/Formula-Cookbook
#                https://rubydoc.brew.sh/Formula
# PLEASE REMOVE ALL GENERATED COMMENTS BEFORE SUBMITTING YOUR PULL REQUEST!
class TxtToExcel < Formula
  include Language::Python::Virtualenv

  desc "A python program to extract info from specially formed txt-files into a Microsoft Excel file."
  homepage "https://github.com/Johnderate/homebrew-txt-to-excel"
  url "https://github.com/Johnderate/homebrew-txt-to-excel/blob/main/txt-to-excel.py"
  version "1.0.0"
  sha256 ""
  license "GPL-3.0-only"

  # Python dependencies

  resource "et_xmlfile" do
    url "https://files.pythonhosted.org/packages/22/28/a99c42aea746e18382ad9fb36f64c1c1f04216f41797f2f0fa567da11388/et_xmlfile-1.0.1.tar.gz"
    sha256 "614d9722d572f6246302c4491846d2c393c199cfa4edc9af593437691683335b"
  end

  resource "jdcal" do
    url "https://files.pythonhosted.org/packages/7b/b0/fa20fce23e9c3b55b640e629cb5edf32a85e6af3cf7af599940eb0c753fe/jdcal-1.4.1.tar.gz"
    sha256 "472872e096eb8df219c23f2689fc336668bdb43d194094b5cc1707e1640acfc8"
  end

  resource "openpyxl" do
    url "https://files.pythonhosted.org/packages/40/32/ee6469111cc624ec00c073986dbd05430ba7265138260cd6dd3771311c3b/openpyxl-3.0.5.tar.gz"
    sha256 "18e11f9a650128a12580a58e3daba14e00a11d9e907c554a17ea016bf1a2c71b"
  end

  depends_on "python@3.x"

  def install
    # ENV.deparallelize  # if your formula fails when building in parallel
    virtualenv_install_with_resources
  end
end
