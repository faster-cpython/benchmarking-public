# Results vs. 3.13.0b2

- fork: python
- ref: edb6883ef3f7a8ef0c83
- machine: linux-aarch64
- commit hash: edb6883
- commit date: 2024-06-01
- overall geometric mean: 1.00x slower
- HPT reliability: 78.35%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 3.10 sec                                                     | 3.13 sec: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                             |

Benchmark hidden because not significant (4): 2to3, chameleon, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 111 ms: 1.03x faster                                                     |
| float          | 91.4 ms                                                      | 92.1 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.0 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                             |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|---------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads         | 2.57 sec                                                     | 2.54 sec: 1.01x faster                                                   |
| unpickle            | 19.8 us                                                      | 20.0 us: 1.01x slower                                                    |
| json_loads          | 32.1 us                                                      | 32.6 us: 1.02x slower                                                    |
| xml_etree_iterparse | 147 ms                                                       | 149 ms: 1.02x slower                                                     |
| json_dumps          | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                    |
| pickle              | 13.4 us                                                      | 13.8 us: 1.03x slower                                                    |
| Geometric mean      | (ref)                                                        | 1.01x slower                                                             |

Benchmark hidden because not significant (8): unpickle_pure_python, pickle_pure_python, pickle_dict, pickle_list, unpickle_list, xml_etree_parse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                        | 1.00x slower                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                      | 27.6 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                        | 1.01x slower                                                             |

Benchmark hidden because not significant (3): django_template, mako, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-arminc-aarch64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8                 | 31.1 ms                                                      | 30.0 ms: 1.04x faster                                                    |
| telco                    | 10.0 ms                                                      | 9.73 ms: 1.03x faster                                                    |
| nbody                    | 114 ms                                                       | 111 ms: 1.03x faster                                                     |
| pprint_pformat           | 1.93 sec                                                     | 1.89 sec: 1.02x faster                                                   |
| gc_traversal             | 5.17 ms                                                      | 5.08 ms: 1.02x faster                                                    |
| deltablue                | 3.88 ms                                                      | 3.82 ms: 1.01x faster                                                    |
| comprehensions           | 20.5 us                                                      | 20.2 us: 1.01x faster                                                    |
| tomli_loads              | 2.57 sec                                                     | 2.54 sec: 1.01x faster                                                   |
| mdp                      | 3.33 sec                                                     | 3.31 sec: 1.00x faster                                                   |
| python_startup           | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                    |
| float                    | 91.4 ms                                                      | 92.1 ms: 1.01x slower                                                    |
| genshi_text              | 27.4 ms                                                      | 27.6 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl          | 2.21 sec                                                     | 2.23 sec: 1.01x slower                                                   |
| unpickle                 | 19.8 us                                                      | 20.0 us: 1.01x slower                                                    |
| docutils                 | 3.10 sec                                                     | 3.13 sec: 1.01x slower                                                   |
| sympy_str                | 265 ms                                                       | 268 ms: 1.01x slower                                                     |
| generators               | 37.1 ms                                                      | 37.6 ms: 1.01x slower                                                    |
| pathlib                  | 22.8 ms                                                      | 23.1 ms: 1.01x slower                                                    |
| fannkuch                 | 451 ms                                                       | 457 ms: 1.01x slower                                                     |
| bench_thread_pool        | 1.26 ms                                                      | 1.27 ms: 1.01x slower                                                    |
| sympy_integrate          | 20.9 ms                                                      | 21.2 ms: 1.01x slower                                                    |
| sympy_sum                | 144 ms                                                       | 146 ms: 1.02x slower                                                     |
| json_loads               | 32.1 us                                                      | 32.6 us: 1.02x slower                                                    |
| bench_mp_pool            | 7.03 ms                                                      | 7.16 ms: 1.02x slower                                                    |
| xml_etree_iterparse      | 147 ms                                                       | 149 ms: 1.02x slower                                                     |
| typing_runtime_protocols | 193 us                                                       | 197 us: 1.02x slower                                                     |
| json_dumps               | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                    |
| pickle                   | 13.4 us                                                      | 13.8 us: 1.03x slower                                                    |
| deepcopy_reduce          | 4.04 us                                                      | 4.16 us: 1.03x slower                                                    |
| flaskblogging            | 4.70 ms                                                      | 4.90 ms: 1.04x slower                                                    |
| pyflate                  | 557 ms                                                       | 581 ms: 1.04x slower                                                     |
| gunicorn                 | 1.19 ms                                                      | 1.24 ms: 1.05x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.00x slower                                                             |

Benchmark hidden because not significant (69): async_tree_io, logging_simple, async_tree_cpu_io_mixed, async_generators, async_tree_memoization_tg, django_template, logging_format, spectral_norm, deepcopy_memo, sqlglot_normalize, async_tree_io_tg, async_tree_cpu_io_mixed_tg, regex_dna, hexiom, richards_super, pprint_safe_repr, logging_silent, async_tree_memoization, scimark_sparse_mat_mult, chaos, richards, go, thrift, regex_effbot, chameleon, unpickle_pure_python, asyncio_websockets, deepcopy, async_tree_none, pidigits, scimark_fft, sqlite_synth, pickle_pure_python, crypto_pyaes, python_startup_no_site, coroutines, sqlglot_optimize, asyncio_tcp, raytrace, scimark_sor, coverage, mako, regex_compile, scimark_lu, pickle_dict, nqueens, async_tree_none_tg, aiohttp, pycparser, pickle_list, pylint, 2to3, meteor_contest, dask, create_gc_cycles, unpickle_list, mypy2, scimark_monte_carlo, sqlglot_transpile, sqlglot_parse, sympy_expand, xml_etree_parse, html5lib, json, xml_etree_process, xml_etree_generate, tornado_http, dulwich_log, genshi_xml
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 78.35% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x