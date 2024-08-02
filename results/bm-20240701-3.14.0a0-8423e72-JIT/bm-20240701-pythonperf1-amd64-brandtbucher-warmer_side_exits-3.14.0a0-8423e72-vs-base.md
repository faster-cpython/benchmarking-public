# Results vs. base

- fork: brandtbucher
- ref: warmer_side_exits
- machine: windows-amd64
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.00x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 234 ms                                                                     | 238 ms: 1.01x slower                                                          |
| docutils       | 1.77 sec                                                                   | 1.78 sec: 1.01x slower                                                        |
| html5lib       | 37.3 ms                                                                    | 39.1 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                                      | 1.02x slower                                                                  |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 50.2 ms                                                                    | 51.5 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                                      | 1.01x slower                                                                  |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8       | 22.3 ms                                                                    | 15.4 ms: 1.45x faster                                                         |
| regex_effbot   | 1.61 ms                                                                    | 1.58 ms: 1.02x faster                                                         |
| regex_compile  | 88.5 ms                                                                    | 89.4 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                      | 1.10x faster                                                                  |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 135 us                                                                     | 118 us: 1.15x faster                                                          |
| tomli_loads          | 1.27 sec                                                                   | 1.27 sec: 1.01x slower                                                        |
| xml_etree_iterparse  | 61.0 ms                                                                    | 61.6 ms: 1.01x slower                                                         |
| xml_etree_parse      | 92.7 ms                                                                    | 94.1 ms: 1.02x slower                                                         |
| json_dumps           | 5.85 ms                                                                    | 5.95 ms: 1.02x slower                                                         |
| xml_etree_generate   | 53.4 ms                                                                    | 54.5 ms: 1.02x slower                                                         |
| pickle_pure_python   | 178 us                                                                     | 183 us: 1.03x slower                                                          |
| json_loads           | 14.1 us                                                                    | 14.5 us: 1.03x slower                                                         |
| xml_etree_process    | 38.1 ms                                                                    | 39.3 ms: 1.03x slower                                                         |
| Geometric mean       | (ref)                                                                      | 1.00x slower                                                                  |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-----------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 46.2 ms                                                                    | 43.7 ms: 1.06x faster                                                         |
| genshi_text     | 18.2 ms                                                                    | 18.6 ms: 1.02x slower                                                         |
| django_template | 26.2 ms                                                                    | 26.9 ms: 1.03x slower                                                         |
| Geometric mean  | (ref)                                                                      | 1.00x faster                                                                  |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240701-pythonperf1-amd64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 | bm-20240701-pythonperf1-amd64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|--------------------------|:--------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_v8                 | 22.3 ms                                                                    | 15.4 ms: 1.45x faster                                                         |
| unpickle_pure_python     | 135 us                                                                     | 118 us: 1.15x faster                                                          |
| genshi_xml               | 46.2 ms                                                                    | 43.7 ms: 1.06x faster                                                         |
| richards                 | 30.3 ms                                                                    | 29.0 ms: 1.05x faster                                                         |
| comprehensions           | 10.6 us                                                                    | 10.1 us: 1.04x faster                                                         |
| telco                    | 4.54 ms                                                                    | 4.39 ms: 1.03x faster                                                         |
| scimark_fft              | 152 ms                                                                     | 147 ms: 1.03x faster                                                          |
| coverage                 | 48.2 ms                                                                    | 46.6 ms: 1.03x faster                                                         |
| nqueens                  | 61.9 ms                                                                    | 60.0 ms: 1.03x faster                                                         |
| richards_super           | 33.9 ms                                                                    | 32.9 ms: 1.03x faster                                                         |
| meteor_contest           | 75.0 ms                                                                    | 73.6 ms: 1.02x faster                                                         |
| scimark_sparse_mat_mult  | 2.14 ms                                                                    | 2.10 ms: 1.02x faster                                                         |
| pprint_safe_repr         | 486 ms                                                                     | 477 ms: 1.02x faster                                                          |
| hexiom                   | 4.69 ms                                                                    | 4.61 ms: 1.02x faster                                                         |
| regex_effbot             | 1.61 ms                                                                    | 1.58 ms: 1.02x faster                                                         |
| deepcopy_reduce          | 1.85 us                                                                    | 1.83 us: 1.01x faster                                                         |
| coroutines               | 14.8 ms                                                                    | 14.6 ms: 1.01x faster                                                         |
| chaos                    | 40.6 ms                                                                    | 40.3 ms: 1.01x faster                                                         |
| crypto_pyaes             | 41.1 ms                                                                    | 40.9 ms: 1.00x faster                                                         |
| async_generators         | 272 ms                                                                     | 274 ms: 1.01x slower                                                          |
| tomli_loads              | 1.27 sec                                                                   | 1.27 sec: 1.01x slower                                                        |
| sqlglot_parse            | 823 us                                                                     | 830 us: 1.01x slower                                                          |
| xml_etree_iterparse      | 61.0 ms                                                                    | 61.6 ms: 1.01x slower                                                         |
| sympy_str                | 178 ms                                                                     | 180 ms: 1.01x slower                                                          |
| docutils                 | 1.77 sec                                                                   | 1.78 sec: 1.01x slower                                                        |
| regex_compile            | 88.5 ms                                                                    | 89.4 ms: 1.01x slower                                                         |
| sympy_integrate          | 14.0 ms                                                                    | 14.2 ms: 1.01x slower                                                         |
| pyflate                  | 263 ms                                                                     | 266 ms: 1.01x slower                                                          |
| mdp                      | 1.41 sec                                                                   | 1.43 sec: 1.01x slower                                                        |
| raytrace                 | 185 ms                                                                     | 187 ms: 1.01x slower                                                          |
| typing_runtime_protocols | 116 us                                                                     | 118 us: 1.01x slower                                                          |
| 2to3                     | 234 ms                                                                     | 238 ms: 1.01x slower                                                          |
| xml_etree_parse          | 92.7 ms                                                                    | 94.1 ms: 1.02x slower                                                         |
| sqlglot_transpile        | 1.05 ms                                                                    | 1.07 ms: 1.02x slower                                                         |
| json_dumps               | 5.85 ms                                                                    | 5.95 ms: 1.02x slower                                                         |
| deltablue                | 2.31 ms                                                                    | 2.36 ms: 1.02x slower                                                         |
| fannkuch                 | 223 ms                                                                     | 227 ms: 1.02x slower                                                          |
| xml_etree_generate       | 53.4 ms                                                                    | 54.5 ms: 1.02x slower                                                         |
| deepcopy_memo            | 15.9 us                                                                    | 16.2 us: 1.02x slower                                                         |
| genshi_text              | 18.2 ms                                                                    | 18.6 ms: 1.02x slower                                                         |
| sqlglot_optimize         | 36.2 ms                                                                    | 36.9 ms: 1.02x slower                                                         |
| sympy_sum                | 92.9 ms                                                                    | 95.0 ms: 1.02x slower                                                         |
| nbody                    | 50.2 ms                                                                    | 51.5 ms: 1.03x slower                                                         |
| django_template          | 26.2 ms                                                                    | 26.9 ms: 1.03x slower                                                         |
| logging_simple           | 5.83 us                                                                    | 5.99 us: 1.03x slower                                                         |
| pickle_pure_python       | 178 us                                                                     | 183 us: 1.03x slower                                                          |
| sympy_expand             | 307 ms                                                                     | 316 ms: 1.03x slower                                                          |
| deepcopy                 | 179 us                                                                     | 185 us: 1.03x slower                                                          |
| go                       | 94.7 ms                                                                    | 97.5 ms: 1.03x slower                                                         |
| json_loads               | 14.1 us                                                                    | 14.5 us: 1.03x slower                                                         |
| xml_etree_process        | 38.1 ms                                                                    | 39.3 ms: 1.03x slower                                                         |
| logging_format           | 6.23 us                                                                    | 6.44 us: 1.03x slower                                                         |
| asyncio_tcp              | 472 ms                                                                     | 489 ms: 1.04x slower                                                          |
| html5lib                 | 37.3 ms                                                                    | 39.1 ms: 1.05x slower                                                         |
| scimark_sor              | 88.6 ms                                                                    | 93.2 ms: 1.05x slower                                                         |
| Geometric mean           | (ref)                                                                      | 1.00x faster                                                                  |

Benchmark hidden because not significant (32): asyncio_tcp_ssl, logging_silent, async_tree_none, mako, async_tree_cpu_io_mixed, pprint_pformat, async_tree_cpu_io_mixed_tg, thrift, bench_thread_pool, scimark_monte_carlo, generators, pathlib, async_tree_io_tg, gc_traversal, pidigits, scimark_lu, sqlglot_normalize, bench_mp_pool, regex_dna, float, tornado_http, create_gc_cycles, json, async_tree_memoization, python_startup, python_startup_no_site, spectral_norm, async_tree_memoization_tg, pylint, async_tree_none_tg, async_tree_io, pycparser

# HPT report

- Reliability score: 99.92% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown