# Results vs. 3.13.0b2

- fork: python
- ref: 6b10467fbc0b67bf217e
- machine: linux-aarch64
- commit hash: 6b10467
- commit date: 2024-06-03
- overall geometric mean: 1.00x slower
- HPT reliability: 99.73%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| html5lib       | 66.1 ms                                                      | 67.4 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                        | 1.00x slower                                                             |

Benchmark hidden because not significant (4): 2to3, chameleon, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg, async_tree_io_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 112 ms: 1.02x faster                                                     |
| float          | 91.4 ms                                                      | 91.9 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                        | 1.00x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 247 ms: 1.05x faster                                                     |
| regex_effbot   | 4.98 ms                                                      | 4.84 ms: 1.03x faster                                                    |
| regex_compile  | 128 ms                                                       | 129 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                        | 1.02x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads    | 2.57 sec                                                     | 2.58 sec: 1.00x slower                                                   |
| pickle_dict    | 37.6 us                                                      | 38.0 us: 1.01x slower                                                    |
| json_dumps     | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                                    |
| pickle_list    | 5.27 us                                                      | 5.35 us: 1.02x slower                                                    |
| pickle         | 13.4 us                                                      | 13.7 us: 1.02x slower                                                    |
| Geometric mean | (ref)                                                        | 1.01x slower                                                             |

Benchmark hidden because not significant (9): unpickle_list, json_loads, xml_etree_generate, xml_etree_parse, unpickle, unpickle_pure_python, pickle_pure_python, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 41.5 ms: 1.02x faster                                                    |
| genshi_text     | 27.4 ms                                                      | 27.9 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                             |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-arminc-aarch64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna                | 259 ms                                                       | 247 ms: 1.05x faster                                                     |
| regex_effbot             | 4.98 ms                                                      | 4.84 ms: 1.03x faster                                                    |
| gc_traversal             | 5.17 ms                                                      | 5.07 ms: 1.02x faster                                                    |
| logging_simple           | 7.21 us                                                      | 7.06 us: 1.02x faster                                                    |
| django_template          | 42.3 ms                                                      | 41.5 ms: 1.02x faster                                                    |
| nbody                    | 114 ms                                                       | 112 ms: 1.02x faster                                                     |
| comprehensions           | 20.5 us                                                      | 20.2 us: 1.02x faster                                                    |
| pprint_pformat           | 1.93 sec                                                     | 1.91 sec: 1.01x faster                                                   |
| asyncio_tcp_ssl          | 2.21 sec                                                     | 2.20 sec: 1.01x faster                                                   |
| tomli_loads              | 2.57 sec                                                     | 2.58 sec: 1.00x slower                                                   |
| float                    | 91.4 ms                                                      | 91.9 ms: 1.01x slower                                                    |
| regex_compile            | 128 ms                                                       | 129 ms: 1.01x slower                                                     |
| pickle_dict              | 37.6 us                                                      | 38.0 us: 1.01x slower                                                    |
| bench_mp_pool            | 7.03 ms                                                      | 7.11 ms: 1.01x slower                                                    |
| sympy_expand             | 457 ms                                                       | 463 ms: 1.01x slower                                                     |
| json_dumps               | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                                    |
| pickle_list              | 5.27 us                                                      | 5.35 us: 1.02x slower                                                    |
| genshi_text              | 27.4 ms                                                      | 27.9 ms: 1.02x slower                                                    |
| hexiom                   | 7.08 ms                                                      | 7.20 ms: 1.02x slower                                                    |
| deepcopy_reduce          | 4.04 us                                                      | 4.12 us: 1.02x slower                                                    |
| html5lib                 | 66.1 ms                                                      | 67.4 ms: 1.02x slower                                                    |
| typing_runtime_protocols | 193 us                                                       | 197 us: 1.02x slower                                                     |
| pycparser                | 1.22 sec                                                     | 1.25 sec: 1.02x slower                                                   |
| pickle                   | 13.4 us                                                      | 13.7 us: 1.02x slower                                                    |
| scimark_monte_carlo      | 82.3 ms                                                      | 84.2 ms: 1.02x slower                                                    |
| deepcopy_memo            | 50.8 us                                                      | 52.0 us: 1.02x slower                                                    |
| pathlib                  | 22.8 ms                                                      | 23.5 ms: 1.03x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.00x slower                                                             |

Benchmark hidden because not significant (74): regex_v8, logging_format, unpickle_list, async_tree_io, sqlglot_parse, chameleon, docutils, async_tree_cpu_io_mixed, dulwich_log, sqlglot_normalize, tornado_http, json_loads, sqlglot_optimize, fannkuch, scimark_sparse_mat_mult, async_tree_none, async_generators, xml_etree_generate, xml_etree_parse, chaos, gunicorn, pylint, unpickle, go, pidigits, async_tree_memoization_tg, deltablue, richards_super, crypto_pyaes, sympy_sum, genshi_xml, sqlite_synth, logging_silent, python_startup, json, 2to3, mdp, spectral_norm, raytrace, mako, pprint_safe_repr, scimark_lu, telco, thrift, async_tree_io_tg, pyflate, async_tree_memoization, bench_thread_pool, mypy2, asyncio_websockets, meteor_contest, python_startup_no_site, coverage, scimark_fft, aiohttp, sympy_str, nqueens, sympy_integrate, generators, unpickle_pure_python, dask, deepcopy, coroutines, async_tree_cpu_io_mixed_tg, async_tree_none_tg, asyncio_tcp, richards, pickle_pure_python, scimark_sor, flaskblogging, sqlglot_transpile, xml_etree_process, xml_etree_iterparse, create_gc_cycles
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 99.73% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x