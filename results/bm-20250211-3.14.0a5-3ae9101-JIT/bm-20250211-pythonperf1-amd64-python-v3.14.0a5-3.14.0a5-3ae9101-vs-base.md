# Results vs. base

- fork: python
- ref: v3.14.0a5
- machine: windows-amd64
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.001x faster
- HPT reliability: 80.04%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| html5lib       | 38.3 ms                                                                     | 37.7 ms: 1.02x faster                                           |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                    |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_websockets      | 316 ms                                                                      | 304 ms: 1.04x faster                                            |
| async_tree_cpu_io_mixed | 344 ms                                                                      | 341 ms: 1.01x faster                                            |
| async_tree_none_tg      | 176 ms                                                                      | 177 ms: 1.01x slower                                            |
| async_generators        | 246 ms                                                                      | 251 ms: 1.02x slower                                            |
| coroutines              | 14.4 ms                                                                     | 14.9 ms: 1.03x slower                                           |
| Geometric mean          | (ref)                                                                       | 1.00x slower                                                    |

Benchmark hidden because not significant (6): async_tree_memoization, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none, async_tree_io_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_dna      | 116 ms                                                                      | 114 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                    |

Benchmark hidden because not significant (3): regex_v8, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 1.20 sec                                                                    | 1.18 sec: 1.02x faster                                          |
| json_dumps           | 6.76 ms                                                                     | 6.66 ms: 1.01x faster                                           |
| pickle_pure_python   | 213 us                                                                      | 211 us: 1.01x faster                                            |
| xml_etree_parse      | 89.9 ms                                                                     | 90.5 ms: 1.01x slower                                           |
| json_loads           | 16.0 us                                                                     | 16.2 us: 1.01x slower                                           |
| xml_etree_process    | 36.2 ms                                                                     | 36.7 ms: 1.01x slower                                           |
| xml_etree_generate   | 50.3 ms                                                                     | 51.1 ms: 1.02x slower                                           |
| unpickle_pure_python | 112 us                                                                      | 115 us: 1.02x slower                                            |
| Geometric mean       | (ref)                                                                       | 1.00x slower                                                    |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 19.3 ms                                                                     | 18.9 ms: 1.02x faster                                           |
| Geometric mean         | (ref)                                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 5.33 ms                                                                     | 5.26 ms: 1.01x faster                                           |
| django_template | 25.8 ms                                                                     | 25.5 ms: 1.01x faster                                           |
| genshi_text     | 16.8 ms                                                                     | 16.7 ms: 1.01x faster                                           |
| Geometric mean  | (ref)                                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|--------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mdp                      | 1.67 sec                                                                    | 1.51 sec: 1.11x faster                                          |
| asyncio_websockets       | 316 ms                                                                      | 304 ms: 1.04x faster                                            |
| coverage                 | 50.0 ms                                                                     | 48.2 ms: 1.04x faster                                           |
| python_startup_no_site   | 19.3 ms                                                                     | 18.9 ms: 1.02x faster                                           |
| k_core                   | 1.64 sec                                                                    | 1.61 sec: 1.02x faster                                          |
| logging_format           | 7.01 us                                                                     | 6.88 us: 1.02x faster                                           |
| logging_simple           | 6.58 us                                                                     | 6.48 us: 1.02x faster                                           |
| fannkuch                 | 232 ms                                                                      | 229 ms: 1.02x faster                                            |
| pyflate                  | 282 ms                                                                      | 278 ms: 1.02x faster                                            |
| tomli_loads              | 1.20 sec                                                                    | 1.18 sec: 1.02x faster                                          |
| html5lib                 | 38.3 ms                                                                     | 37.7 ms: 1.02x faster                                           |
| comprehensions           | 11.6 us                                                                     | 11.5 us: 1.01x faster                                           |
| typing_runtime_protocols | 112 us                                                                      | 110 us: 1.01x faster                                            |
| json_dumps               | 6.76 ms                                                                     | 6.66 ms: 1.01x faster                                           |
| mako                     | 5.33 ms                                                                     | 5.26 ms: 1.01x faster                                           |
| regex_dna                | 116 ms                                                                      | 114 ms: 1.01x faster                                            |
| bpe_tokeniser            | 2.60 sec                                                                    | 2.57 sec: 1.01x faster                                          |
| generators               | 20.7 ms                                                                     | 20.4 ms: 1.01x faster                                           |
| django_template          | 25.8 ms                                                                     | 25.5 ms: 1.01x faster                                           |
| genshi_text              | 16.8 ms                                                                     | 16.7 ms: 1.01x faster                                           |
| hexiom                   | 4.58 ms                                                                     | 4.54 ms: 1.01x faster                                           |
| thrift                   | 503 us                                                                      | 498 us: 1.01x faster                                            |
| pickle_pure_python       | 213 us                                                                      | 211 us: 1.01x faster                                            |
| create_gc_cycles         | 1.22 ms                                                                     | 1.21 ms: 1.01x faster                                           |
| nqueens                  | 63.5 ms                                                                     | 63.0 ms: 1.01x faster                                           |
| crypto_pyaes             | 46.3 ms                                                                     | 45.9 ms: 1.01x faster                                           |
| async_tree_cpu_io_mixed  | 344 ms                                                                      | 341 ms: 1.01x faster                                            |
| sqlglot_transpile        | 1.08 ms                                                                     | 1.07 ms: 1.01x faster                                           |
| sqlglot_parse            | 844 us                                                                      | 839 us: 1.01x faster                                            |
| sqlite_synth             | 1.54 us                                                                     | 1.53 us: 1.01x faster                                           |
| logging_silent           | 65.8 ns                                                                     | 66.1 ns: 1.00x slower                                           |
| connected_components     | 311 ms                                                                      | 313 ms: 1.01x slower                                            |
| scimark_fft              | 147 ms                                                                      | 148 ms: 1.01x slower                                            |
| xml_etree_parse          | 89.9 ms                                                                     | 90.5 ms: 1.01x slower                                           |
| sqlglot_optimize         | 37.1 ms                                                                     | 37.3 ms: 1.01x slower                                           |
| async_tree_none_tg       | 176 ms                                                                      | 177 ms: 1.01x slower                                            |
| sympy_expand             | 301 ms                                                                      | 303 ms: 1.01x slower                                            |
| deepcopy_memo            | 21.1 us                                                                     | 21.3 us: 1.01x slower                                           |
| shortest_path            | 345 ms                                                                      | 348 ms: 1.01x slower                                            |
| go                       | 87.1 ms                                                                     | 88.1 ms: 1.01x slower                                           |
| json_loads               | 16.0 us                                                                     | 16.2 us: 1.01x slower                                           |
| richards                 | 32.1 ms                                                                     | 32.5 ms: 1.01x slower                                           |
| meteor_contest           | 76.0 ms                                                                     | 77.0 ms: 1.01x slower                                           |
| subparsers               | 15.8 ms                                                                     | 16.0 ms: 1.01x slower                                           |
| xml_etree_process        | 36.2 ms                                                                     | 36.7 ms: 1.01x slower                                           |
| xml_etree_generate       | 50.3 ms                                                                     | 51.1 ms: 1.02x slower                                           |
| json                     | 3.17 ms                                                                     | 3.22 ms: 1.02x slower                                           |
| telco                    | 4.32 ms                                                                     | 4.39 ms: 1.02x slower                                           |
| async_generators         | 246 ms                                                                      | 251 ms: 1.02x slower                                            |
| unpickle_pure_python     | 112 us                                                                      | 115 us: 1.02x slower                                            |
| scimark_monte_carlo      | 45.6 ms                                                                     | 46.6 ms: 1.02x slower                                           |
| dulwich_log              | 38.8 ms                                                                     | 39.8 ms: 1.03x slower                                           |
| scimark_lu               | 64.2 ms                                                                     | 66.1 ms: 1.03x slower                                           |
| coroutines               | 14.4 ms                                                                     | 14.9 ms: 1.03x slower                                           |
| scimark_sor              | 88.9 ms                                                                     | 92.5 ms: 1.04x slower                                           |
| scimark_sparse_mat_mult  | 2.05 ms                                                                     | 2.15 ms: 1.05x slower                                           |
| Geometric mean           | (ref)                                                                       | 1.00x faster                                                    |

Benchmark hidden because not significant (38): pprint_safe_repr, gc_traversal, regex_v8, regex_effbot, genshi_xml, docutils, pycparser, float, bench_mp_pool, pprint_pformat, deepcopy, deepcopy_reduce, sympy_integrate, python_startup, pidigits, deltablue, pathlib, async_tree_memoization, bench_thread_pool, async_tree_io, raytrace, richards_super, sympy_str, sqlglot_normalize, nbody, regex_compile, chaos, 2to3, sympy_sum, spectral_norm, xml_etree_iterparse, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, pylint, many_optionals, async_tree_none, sphinx, async_tree_io_tg

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 80.04% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown