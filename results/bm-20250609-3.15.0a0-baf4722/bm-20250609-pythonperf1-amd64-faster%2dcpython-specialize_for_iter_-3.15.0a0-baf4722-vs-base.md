# Results vs. base

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: windows-amd64
- commit hash: baf4722
- commit date: 2025-06-09
- overall geometric mean: 1.000x slower
- HPT reliability: 68.90%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 220 ms                                                                     | 219 ms: 1.01x faster                                                                 |
| html5lib       | 38.1 ms                                                                    | 39.1 ms: 1.03x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.00x slower                                                                         |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_websockets         | 164 ms                                                                     | 159 ms: 1.03x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 341 ms                                                                     | 336 ms: 1.01x faster                                                                 |
| async_tree_cpu_io_mixed    | 328 ms                                                                     | 326 ms: 1.01x faster                                                                 |
| async_generators           | 229 ms                                                                     | 231 ms: 1.01x slower                                                                 |
| async_tree_io_tg           | 389 ms                                                                     | 393 ms: 1.01x slower                                                                 |
| Geometric mean             | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (6): async_tree_memoization, coroutines, async_tree_none, async_tree_io, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 62.7 ms                                                                    | 63.8 ms: 1.02x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                         |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_effbot   | 1.53 ms                                                                    | 1.55 ms: 1.01x slower                                                                |
| regex_dna      | 119 ms                                                                     | 121 ms: 1.02x slower                                                                 |
| regex_compile  | 78.8 ms                                                                    | 81.8 ms: 1.04x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 14.3 us                                                                    | 14.0 us: 1.02x faster                                                                |
| xml_etree_iterparse  | 63.8 ms                                                                    | 62.7 ms: 1.02x faster                                                                |
| json_dumps           | 6.29 ms                                                                    | 6.22 ms: 1.01x faster                                                                |
| pickle_pure_python   | 214 us                                                                     | 212 us: 1.01x faster                                                                 |
| xml_etree_parse      | 87.9 ms                                                                    | 87.2 ms: 1.01x faster                                                                |
| tomli_loads          | 1.35 sec                                                                   | 1.36 sec: 1.01x slower                                                               |
| unpickle_pure_python | 132 us                                                                     | 136 us: 1.03x slower                                                                 |
| Geometric mean       | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup | 25.6 ms                                                                    | 26.1 ms: 1.02x slower                                                                |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                                         |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|-----------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_xml      | 34.2 ms                                                                    | 33.2 ms: 1.03x faster                                                                |
| django_template | 24.3 ms                                                                    | 23.8 ms: 1.02x faster                                                                |
| Geometric mean  | (ref)                                                                      | 1.01x faster                                                                         |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------------------|:--------------------------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_websockets         | 164 ms                                                                     | 159 ms: 1.03x faster                                                                 |
| deepcopy_memo              | 17.9 us                                                                    | 17.4 us: 1.03x faster                                                                |
| genshi_xml                 | 34.2 ms                                                                    | 33.2 ms: 1.03x faster                                                                |
| pyflate                    | 286 ms                                                                     | 278 ms: 1.03x faster                                                                 |
| spectral_norm              | 59.0 ms                                                                    | 57.6 ms: 1.02x faster                                                                |
| coverage                   | 296 ms                                                                     | 290 ms: 1.02x faster                                                                 |
| logging_silent             | 325 ns                                                                     | 318 ns: 1.02x faster                                                                 |
| deepcopy_reduce            | 1.84 us                                                                    | 1.80 us: 1.02x faster                                                                |
| django_template            | 24.3 ms                                                                    | 23.8 ms: 1.02x faster                                                                |
| json_loads                 | 14.3 us                                                                    | 14.0 us: 1.02x faster                                                                |
| xml_etree_iterparse        | 63.8 ms                                                                    | 62.7 ms: 1.02x faster                                                                |
| gc_traversal               | 2.18 ms                                                                    | 2.14 ms: 1.02x faster                                                                |
| crypto_pyaes               | 47.4 ms                                                                    | 46.7 ms: 1.01x faster                                                                |
| async_tree_cpu_io_mixed_tg | 341 ms                                                                     | 336 ms: 1.01x faster                                                                 |
| deepcopy                   | 172 us                                                                     | 170 us: 1.01x faster                                                                 |
| fannkuch                   | 256 ms                                                                     | 252 ms: 1.01x faster                                                                 |
| json_dumps                 | 6.29 ms                                                                    | 6.22 ms: 1.01x faster                                                                |
| pickle_pure_python         | 214 us                                                                     | 212 us: 1.01x faster                                                                 |
| sqlite_synth               | 1.59 us                                                                    | 1.58 us: 1.01x faster                                                                |
| sympy_expand               | 289 ms                                                                     | 286 ms: 1.01x faster                                                                 |
| mdp                        | 808 ms                                                                     | 802 ms: 1.01x faster                                                                 |
| scimark_sor                | 74.7 ms                                                                    | 74.1 ms: 1.01x faster                                                                |
| xml_etree_parse            | 87.9 ms                                                                    | 87.2 ms: 1.01x faster                                                                |
| sqlglot_v2_transpile       | 1.01 ms                                                                    | 1.01 ms: 1.01x faster                                                                |
| scimark_sparse_mat_mult    | 2.52 ms                                                                    | 2.50 ms: 1.01x faster                                                                |
| scimark_monte_carlo        | 40.5 ms                                                                    | 40.3 ms: 1.01x faster                                                                |
| async_tree_cpu_io_mixed    | 328 ms                                                                     | 326 ms: 1.01x faster                                                                 |
| 2to3                       | 220 ms                                                                     | 219 ms: 1.01x faster                                                                 |
| many_optionals             | 435 us                                                                     | 437 us: 1.01x slower                                                                 |
| tomli_loads                | 1.35 sec                                                                   | 1.36 sec: 1.01x slower                                                               |
| richards                   | 27.0 ms                                                                    | 27.3 ms: 1.01x slower                                                                |
| async_generators           | 229 ms                                                                     | 231 ms: 1.01x slower                                                                 |
| sqlglot_v2_normalize       | 69.9 ms                                                                    | 70.5 ms: 1.01x slower                                                                |
| async_tree_io_tg           | 389 ms                                                                     | 393 ms: 1.01x slower                                                                 |
| telco                      | 4.59 ms                                                                    | 4.64 ms: 1.01x slower                                                                |
| comprehensions             | 10.7 us                                                                    | 10.8 us: 1.01x slower                                                                |
| richards_super             | 30.7 ms                                                                    | 31.1 ms: 1.01x slower                                                                |
| regex_effbot               | 1.53 ms                                                                    | 1.55 ms: 1.01x slower                                                                |
| hexiom                     | 4.01 ms                                                                    | 4.06 ms: 1.01x slower                                                                |
| pprint_safe_repr           | 531 ms                                                                     | 538 ms: 1.01x slower                                                                 |
| pprint_pformat             | 1.09 sec                                                                   | 1.11 sec: 1.01x slower                                                               |
| go                         | 75.0 ms                                                                    | 76.2 ms: 1.02x slower                                                                |
| nbody                      | 62.7 ms                                                                    | 63.8 ms: 1.02x slower                                                                |
| python_startup             | 25.6 ms                                                                    | 26.1 ms: 1.02x slower                                                                |
| scimark_fft                | 172 ms                                                                     | 176 ms: 1.02x slower                                                                 |
| dulwich_log                | 40.9 ms                                                                    | 41.8 ms: 1.02x slower                                                                |
| raytrace                   | 179 ms                                                                     | 183 ms: 1.02x slower                                                                 |
| regex_dna                  | 119 ms                                                                     | 121 ms: 1.02x slower                                                                 |
| html5lib                   | 38.1 ms                                                                    | 39.1 ms: 1.03x slower                                                                |
| unpickle_pure_python       | 132 us                                                                     | 136 us: 1.03x slower                                                                 |
| nqueens                    | 58.9 ms                                                                    | 60.5 ms: 1.03x slower                                                                |
| deltablue                  | 2.18 ms                                                                    | 2.24 ms: 1.03x slower                                                                |
| regex_compile              | 78.8 ms                                                                    | 81.8 ms: 1.04x slower                                                                |
| Geometric mean             | (ref)                                                                      | 1.00x faster                                                                         |

Benchmark hidden because not significant (39): shortest_path, typing_runtime_protocols, mako, logging_simple, async_tree_memoization, pycparser, sphinx, sympy_sum, regex_v8, subparsers, xml_etree_process, scimark_lu, create_gc_cycles, sqlglot_v2_parse, docutils, coroutines, meteor_contest, async_tree_none, async_tree_io, k_core, pathlib, connected_components, chaos, async_tree_memoization_tg, sqlglot_v2_optimize, xml_etree_generate, json, pylint, genshi_text, bpe_tokeniser, sympy_str, sympy_integrate, pidigits, thrift, async_tree_none_tg, generators, logging_format, float, python_startup_no_site

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 68.90% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown