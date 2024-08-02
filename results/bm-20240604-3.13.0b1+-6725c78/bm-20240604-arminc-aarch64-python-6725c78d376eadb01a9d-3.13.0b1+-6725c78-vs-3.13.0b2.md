# Results vs. 3.13.0b2

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: linux-aarch64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.00x faster
- HPT reliability: 97.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 3.10 sec                                                     | 3.07 sec: 1.01x faster                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                             |

Benchmark hidden because not significant (4): 2to3, chameleon, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io  | 1.22 sec                                                     | 1.19 sec: 1.03x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                             |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_none, async_tree_none_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 112 ms: 1.02x faster                                                     |
| float          | 91.4 ms                                                      | 91.1 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 249 ms: 1.04x faster                                                     |
| regex_effbot   | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 30.7 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|---------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle            | 19.8 us                                                      | 19.7 us: 1.00x faster                                                    |
| pickle_list         | 5.27 us                                                      | 5.30 us: 1.00x slower                                                    |
| xml_etree_iterparse | 147 ms                                                       | 149 ms: 1.01x slower                                                     |
| pickle              | 13.4 us                                                      | 13.6 us: 1.02x slower                                                    |
| json_dumps          | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                    |
| Geometric mean      | (ref)                                                        | 1.00x slower                                                             |

Benchmark hidden because not significant (9): xml_etree_parse, unpickle_list, tomli_loads, pickle_dict, json_loads, pickle_pure_python, xml_etree_generate, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 41.8 ms: 1.01x faster                                                    |
| mako            | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                    |
| genshi_text     | 27.4 ms                                                      | 28.0 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark           | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-arminc-aarch64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|---------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna           | 259 ms                                                       | 249 ms: 1.04x faster                                                     |
| async_tree_io       | 1.22 sec                                                     | 1.19 sec: 1.03x faster                                                   |
| logging_simple      | 7.21 us                                                      | 7.01 us: 1.03x faster                                                    |
| regex_effbot        | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                    |
| pprint_pformat      | 1.93 sec                                                     | 1.90 sec: 1.02x faster                                                   |
| nbody               | 114 ms                                                       | 112 ms: 1.02x faster                                                     |
| telco               | 10.0 ms                                                      | 9.87 ms: 1.02x faster                                                    |
| regex_v8            | 31.1 ms                                                      | 30.7 ms: 1.01x faster                                                    |
| django_template     | 42.3 ms                                                      | 41.8 ms: 1.01x faster                                                    |
| docutils            | 3.10 sec                                                     | 3.07 sec: 1.01x faster                                                   |
| pprint_safe_repr    | 933 ms                                                       | 926 ms: 1.01x faster                                                     |
| asyncio_tcp_ssl     | 2.21 sec                                                     | 2.20 sec: 1.01x faster                                                   |
| float               | 91.4 ms                                                      | 91.1 ms: 1.00x faster                                                    |
| unpickle            | 19.8 us                                                      | 19.7 us: 1.00x faster                                                    |
| pickle_list         | 5.27 us                                                      | 5.30 us: 1.00x slower                                                    |
| xml_etree_iterparse | 147 ms                                                       | 149 ms: 1.01x slower                                                     |
| pathlib             | 22.8 ms                                                      | 23.1 ms: 1.02x slower                                                    |
| pickle              | 13.4 us                                                      | 13.6 us: 1.02x slower                                                    |
| json_dumps          | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                    |
| mako                | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                    |
| dulwich_log         | 58.5 ms                                                      | 59.7 ms: 1.02x slower                                                    |
| genshi_text         | 27.4 ms                                                      | 28.0 ms: 1.02x slower                                                    |
| flaskblogging       | 4.70 ms                                                      | 4.83 ms: 1.03x slower                                                    |
| gunicorn            | 1.19 ms                                                      | 1.24 ms: 1.05x slower                                                    |
| Geometric mean      | (ref)                                                        | 1.00x faster                                                             |

Benchmark hidden because not significant (77): sqlglot_parse, sqlglot_normalize, asyncio_tcp, async_tree_cpu_io_mixed, logging_format, thrift, async_tree_none, create_gc_cycles, async_tree_none_tg, xml_etree_parse, scimark_sor, json, deltablue, meteor_contest, scimark_lu, async_tree_io_tg, python_startup_no_site, tornado_http, comprehensions, unpickle_list, pycparser, dask, mypy2, tomli_loads, go, scimark_fft, aiohttp, nqueens, pickle_dict, fannkuch, spectral_norm, deepcopy, 2to3, generators, async_tree_memoization_tg, coverage, async_tree_cpu_io_mixed_tg, html5lib, sqlglot_optimize, richards_super, crypto_pyaes, richards, bench_mp_pool, deepcopy_memo, scimark_sparse_mat_mult, mdp, sqlite_synth, pidigits, json_loads, async_tree_memoization, sympy_str, hexiom, typing_runtime_protocols, scimark_monte_carlo, pyflate, pickle_pure_python, pylint, xml_etree_generate, chameleon, raytrace, unpickle_pure_python, bench_thread_pool, chaos, coroutines, deepcopy_reduce, asyncio_websockets, sympy_expand, regex_compile, genshi_xml, gc_traversal, async_generators, logging_silent, sympy_integrate, xml_etree_process, sympy_sum, python_startup, sqlglot_transpile
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 97.50% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x