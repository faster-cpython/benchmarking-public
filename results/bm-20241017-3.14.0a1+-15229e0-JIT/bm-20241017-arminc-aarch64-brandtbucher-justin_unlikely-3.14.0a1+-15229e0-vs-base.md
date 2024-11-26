# Results vs. base

- fork: brandtbucher
- ref: justin_unlikely
- machine: linux-aarch64
- commit hash: 15229e0
- commit date: 2024-10-17
- overall geometric mean: 1.001x slower
- HPT reliability: 78.65%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 382 ms                                                                   | 385 ms: 1.01x slower                                                      |
| html5lib       | 72.2 ms                                                                  | 71.1 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                              |

Benchmark hidden because not significant (3): docutils, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg | 1.26 sec                                                                 | 1.25 sec: 1.01x faster                                                    |
| Geometric mean   | (ref)                                                                    | 1.00x faster                                                              |

Benchmark hidden because not significant (12): async_tree_none, async_tree_cpu_io_mixed, coroutines, async_tree_memoization, async_generators, asyncio_tcp_ssl, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, asyncio_tcp, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 114 ms                                                                   | 119 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                                    | 1.02x slower                                                              |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 31.2 ms                                                                  | 31.4 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                              |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|----------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 394 us                                                                   | 387 us: 1.02x faster                                                      |
| unpickle_pure_python | 271 us                                                                   | 266 us: 1.02x faster                                                      |
| pickle               | 14.0 us                                                                  | 13.7 us: 1.01x faster                                                     |
| xml_etree_parse      | 188 ms                                                                   | 185 ms: 1.01x faster                                                      |
| xml_etree_process    | 81.4 ms                                                                  | 80.6 ms: 1.01x faster                                                     |
| tomli_loads          | 2.67 sec                                                                 | 2.65 sec: 1.01x faster                                                    |
| Geometric mean       | (ref)                                                                    | 1.00x faster                                                              |

Benchmark hidden because not significant (8): xml_etree_generate, xml_etree_iterparse, pickle_list, unpickle, pickle_dict, json_dumps, json_loads, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|------------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                                  | 8.73 ms: 1.01x faster                                                     |
| python_startup         | 14.7 ms                                                                  | 14.6 ms: 1.01x faster                                                     |
| Geometric mean         | (ref)                                                                    | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|-----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 52.8 ms                                                                  | 50.9 ms: 1.04x faster                                                     |
| mako            | 13.2 ms                                                                  | 13.4 ms: 1.02x slower                                                     |
| genshi_xml      | 82.2 ms                                                                  | 84.6 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                                    | 1.00x slower                                                              |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20241017-arminc-aarch64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241017-arminc-aarch64-brandtbucher-justin_unlikely-3.14.0a1+-15229e0 |
|--------------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| gc_traversal             | 6.51 ms                                                                  | 6.23 ms: 1.04x faster                                                     |
| dulwich_log              | 80.5 ms                                                                  | 77.4 ms: 1.04x faster                                                     |
| django_template          | 52.8 ms                                                                  | 50.9 ms: 1.04x faster                                                     |
| logging_simple           | 7.61 us                                                                  | 7.41 us: 1.03x faster                                                     |
| pickle_pure_python       | 394 us                                                                   | 387 us: 1.02x faster                                                      |
| unpickle_pure_python     | 271 us                                                                   | 266 us: 1.02x faster                                                      |
| html5lib                 | 72.2 ms                                                                  | 71.1 ms: 1.02x faster                                                     |
| logging_format           | 8.18 us                                                                  | 8.06 us: 1.01x faster                                                     |
| pickle                   | 14.0 us                                                                  | 13.7 us: 1.01x faster                                                     |
| xml_etree_parse          | 188 ms                                                                   | 185 ms: 1.01x faster                                                      |
| xml_etree_process        | 81.4 ms                                                                  | 80.6 ms: 1.01x faster                                                     |
| sympy_integrate          | 29.6 ms                                                                  | 29.3 ms: 1.01x faster                                                     |
| async_tree_io_tg         | 1.26 sec                                                                 | 1.25 sec: 1.01x faster                                                    |
| scimark_lu               | 149 ms                                                                   | 148 ms: 1.01x faster                                                      |
| tomli_loads              | 2.67 sec                                                                 | 2.65 sec: 1.01x faster                                                    |
| python_startup_no_site   | 8.79 ms                                                                  | 8.73 ms: 1.01x faster                                                     |
| python_startup           | 14.7 ms                                                                  | 14.6 ms: 1.01x faster                                                     |
| sqlglot_parse            | 1.71 ms                                                                  | 1.71 ms: 1.00x slower                                                     |
| regex_v8                 | 31.2 ms                                                                  | 31.4 ms: 1.01x slower                                                     |
| richards_super           | 71.2 ms                                                                  | 71.7 ms: 1.01x slower                                                     |
| comprehensions           | 24.7 us                                                                  | 24.9 us: 1.01x slower                                                     |
| 2to3                     | 382 ms                                                                   | 385 ms: 1.01x slower                                                      |
| deepcopy_memo            | 39.0 us                                                                  | 39.3 us: 1.01x slower                                                     |
| pyflate                  | 636 ms                                                                   | 643 ms: 1.01x slower                                                      |
| scimark_fft              | 458 ms                                                                   | 463 ms: 1.01x slower                                                      |
| meteor_contest           | 122 ms                                                                   | 124 ms: 1.01x slower                                                      |
| scimark_sor              | 155 ms                                                                   | 157 ms: 1.01x slower                                                      |
| thrift                   | 965 us                                                                   | 979 us: 1.01x slower                                                      |
| pprint_safe_repr         | 1.22 sec                                                                 | 1.24 sec: 1.02x slower                                                    |
| mako                     | 13.2 ms                                                                  | 13.4 ms: 1.02x slower                                                     |
| logging_silent           | 133 ns                                                                   | 135 ns: 1.02x slower                                                      |
| typing_runtime_protocols | 214 us                                                                   | 218 us: 1.02x slower                                                      |
| bpe_tokeniser            | 5.92 sec                                                                 | 6.04 sec: 1.02x slower                                                    |
| chaos                    | 85.4 ms                                                                  | 87.2 ms: 1.02x slower                                                     |
| sympy_str                | 356 ms                                                                   | 363 ms: 1.02x slower                                                      |
| json                     | 5.60 ms                                                                  | 5.74 ms: 1.02x slower                                                     |
| genshi_xml               | 82.2 ms                                                                  | 84.6 ms: 1.03x slower                                                     |
| pprint_pformat           | 2.53 sec                                                                 | 2.61 sec: 1.03x slower                                                    |
| nbody                    | 114 ms                                                                   | 119 ms: 1.04x slower                                                      |
| Geometric mean           | (ref)                                                                    | 1.00x faster                                                              |

Benchmark hidden because not significant (59): bench_mp_pool, regex_dna, scimark_sparse_mat_mult, spectral_norm, fannkuch, async_tree_none, async_tree_cpu_io_mixed, deepcopy_reduce, coverage, coroutines, xml_etree_generate, async_tree_memoization, regex_effbot, async_generators, sphinx, bench_thread_pool, xml_etree_iterparse, docutils, mdp, asyncio_tcp_ssl, telco, float, sympy_sum, nqueens, generators, pickle_list, async_tree_memoization_tg, pylint, genshi_text, scimark_monte_carlo, pathlib, async_tree_none_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, pycparser, pidigits, create_gc_cycles, sqlglot_normalize, sqlglot_optimize, sqlite_synth, asyncio_tcp, unpickle, tornado_http, go, unpack_sequence, richards, pickle_dict, sympy_expand, deepcopy, hexiom, raytrace, json_dumps, json_loads, crypto_pyaes, unpickle_list, async_tree_io, deltablue, sqlglot_transpile, regex_compile

- Geometric mean (including insignificant results): 1.001x slower
# HPT report

- Reliability score: 78.65% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x