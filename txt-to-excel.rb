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

  depends_on "python@3.x"

  def install
    # ENV.deparallelize  # if your formula fails when building in parallel
    virtualenv_install_with_resources
  end
end
