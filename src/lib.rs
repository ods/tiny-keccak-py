use pyo3::{prelude::*, types::PyBytes};
use tiny_keccak::{Hasher, Keccak};

/// The Keccak-256 hash function defined in Keccak SHA3 submission
#[pyfunction]
fn keccak256<'py>(py: Python<'py>, input: &[u8]) -> PyResult<Bound<'py, PyBytes>> {
    let mut hasher = Keccak::v256();
    hasher.update(input);
    PyBytes::new_bound_with(py, 32, |output: &mut [u8]| {
        hasher.finalize(output);
        Ok(())
    })
}

/// The Keccak-256 hash function defined in Keccak SHA3 submission
#[pymodule]
#[pyo3(name = "tiny_keccak")]
fn tiny_keccak_py(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(keccak256, m)?)?;
    Ok(())
}
