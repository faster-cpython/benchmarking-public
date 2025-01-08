# Results vs. base

- fork: brandtbucher
- ref: nojit
- machine: windows-amd64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.001x faster
- HPT reliability: 63.47%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 223 ms                                                                      | 220 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                       |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 344 ms                                                                      | 347 ms: 1.01x slower                                               |
| async_tree_io              | 395 ms                                                                      | 399 ms: 1.01x slower                                               |
| async_generators           | 254 ms                                                                      | 259 ms: 1.02x slower                                               |
| asyncio_websockets         | 301 ms                                                                      | 325 ms: 1.08x slower                                               |
| Geometric mean             | (ref)                                                                       | 1.01x slower                                                       |

Benchmark hidden because not significant (7): async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed, coroutines, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 56.0 ms                                                                     | 54.2 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                       |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 1.43 ms                                                                     | 1.41 ms: 1.02x faster                                              |
| regex_dna      | 115 ms                                                                      | 113 ms: 1.02x faster                                               |
| regex_v8       | 14.7 ms                                                                     | 14.6 ms: 1.01x faster                                              |
| regex_compile  | 79.9 ms                                                                     | 80.5 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_generate   | 50.3 ms                                                                     | 49.6 ms: 1.01x faster                                              |
| json_loads           | 14.2 us                                                                     | 14.0 us: 1.01x faster                                              |
| tomli_loads          | 1.18 sec                                                                    | 1.19 sec: 1.01x slower                                             |
| xml_etree_parse      | 86.6 ms                                                                     | 87.4 ms: 1.01x slower                                              |
| unpickle_pure_python | 108 us                                                                      | 109 us: 1.01x slower                                               |
| pickle_pure_python   | 204 us                                                                      | 207 us: 1.01x slower                                               |
| json_dumps           | 6.19 ms                                                                     | 6.42 ms: 1.04x slower                                              |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                       |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 17.3 ms                                                                     | 17.0 ms: 1.02x faster                                              |
| Geometric mean         | (ref)                                                                       | 1.01x faster                                                       |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 27.1 ms                                                                     | 26.0 ms: 1.04x faster                                              |
| genshi_xml      | 45.2 ms                                                                     | 44.9 ms: 1.01x faster                                              |
| genshi_text     | 18.2 ms                                                                     | 18.6 ms: 1.02x slower                                              |
| mako            | 5.05 ms                                                                     | 5.16 ms: 1.02x slower                                              |
| Geometric mean  | (ref)                                                                       | 1.00x faster                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20250106-pythonperf1-amd64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------|:---------------------------------------------------------------------------:|:------------------------------------------------------------------:|
| pycparser                  | 779 ms                                                                      | 707 ms: 1.10x faster                                               |
| fannkuch                   | 252 ms                                                                      | 238 ms: 1.06x faster                                               |
| generators                 | 24.2 ms                                                                     | 23.1 ms: 1.05x faster                                              |
| django_template            | 27.1 ms                                                                     | 26.0 ms: 1.04x faster                                              |
| spectral_norm              | 51.4 ms                                                                     | 49.6 ms: 1.04x faster                                              |
| scimark_monte_carlo        | 36.9 ms                                                                     | 35.7 ms: 1.03x faster                                              |
| nbody                      | 56.0 ms                                                                     | 54.2 ms: 1.03x faster                                              |
| meteor_contest             | 74.7 ms                                                                     | 72.6 ms: 1.03x faster                                              |
| deepcopy_memo              | 16.5 us                                                                     | 16.0 us: 1.03x faster                                              |
| logging_silent             | 57.1 ns                                                                     | 55.7 ns: 1.02x faster                                              |
| crypto_pyaes               | 41.8 ms                                                                     | 40.9 ms: 1.02x faster                                              |
| scimark_fft                | 145 ms                                                                      | 142 ms: 1.02x faster                                               |
| pyflate                    | 283 ms                                                                      | 277 ms: 1.02x faster                                               |
| scimark_lu                 | 54.2 ms                                                                     | 53.2 ms: 1.02x faster                                              |
| regex_effbot               | 1.43 ms                                                                     | 1.41 ms: 1.02x faster                                              |
| go                         | 90.1 ms                                                                     | 88.6 ms: 1.02x faster                                              |
| python_startup_no_site     | 17.3 ms                                                                     | 17.0 ms: 1.02x faster                                              |
| regex_dna                  | 115 ms                                                                      | 113 ms: 1.02x faster                                               |
| xml_etree_generate         | 50.3 ms                                                                     | 49.6 ms: 1.01x faster                                              |
| 2to3                       | 223 ms                                                                      | 220 ms: 1.01x faster                                               |
| connected_components       | 311 ms                                                                      | 307 ms: 1.01x faster                                               |
| json_loads                 | 14.2 us                                                                     | 14.0 us: 1.01x faster                                              |
| sqlglot_transpile          | 1.08 ms                                                                     | 1.07 ms: 1.01x faster                                              |
| deltablue                  | 2.27 ms                                                                     | 2.25 ms: 1.01x faster                                              |
| regex_v8                   | 14.7 ms                                                                     | 14.6 ms: 1.01x faster                                              |
| scimark_sor                | 60.2 ms                                                                     | 59.7 ms: 1.01x faster                                              |
| logging_simple             | 6.25 us                                                                     | 6.20 us: 1.01x faster                                              |
| genshi_xml                 | 45.2 ms                                                                     | 44.9 ms: 1.01x faster                                              |
| sqlglot_parse              | 828 us                                                                      | 824 us: 1.00x faster                                               |
| pprint_safe_repr           | 474 ms                                                                      | 472 ms: 1.00x faster                                               |
| shortest_path              | 343 ms                                                                      | 344 ms: 1.00x slower                                               |
| scimark_sparse_mat_mult    | 2.08 ms                                                                     | 2.08 ms: 1.00x slower                                              |
| raytrace                   | 204 ms                                                                      | 205 ms: 1.01x slower                                               |
| sympy_expand               | 299 ms                                                                      | 300 ms: 1.01x slower                                               |
| pprint_pformat             | 948 ms                                                                      | 955 ms: 1.01x slower                                               |
| regex_compile              | 79.9 ms                                                                     | 80.5 ms: 1.01x slower                                              |
| sqlite_synth               | 1.56 us                                                                     | 1.57 us: 1.01x slower                                              |
| dulwich_log                | 39.6 ms                                                                     | 39.9 ms: 1.01x slower                                              |
| async_tree_cpu_io_mixed_tg | 344 ms                                                                      | 347 ms: 1.01x slower                                               |
| tomli_loads                | 1.18 sec                                                                    | 1.19 sec: 1.01x slower                                             |
| sympy_integrate            | 13.5 ms                                                                     | 13.6 ms: 1.01x slower                                              |
| xml_etree_parse            | 86.6 ms                                                                     | 87.4 ms: 1.01x slower                                              |
| sqlglot_normalize          | 201 ms                                                                      | 203 ms: 1.01x slower                                               |
| comprehensions             | 11.5 us                                                                     | 11.6 us: 1.01x slower                                              |
| async_tree_io              | 395 ms                                                                      | 399 ms: 1.01x slower                                               |
| hexiom                     | 4.98 ms                                                                     | 5.04 ms: 1.01x slower                                              |
| unpickle_pure_python       | 108 us                                                                      | 109 us: 1.01x slower                                               |
| pickle_pure_python         | 204 us                                                                      | 207 us: 1.01x slower                                               |
| sympy_sum                  | 90.5 ms                                                                     | 91.8 ms: 1.01x slower                                              |
| chaos                      | 41.2 ms                                                                     | 41.8 ms: 1.01x slower                                              |
| richards_super             | 37.8 ms                                                                     | 38.4 ms: 1.02x slower                                              |
| sqlglot_optimize           | 37.0 ms                                                                     | 37.6 ms: 1.02x slower                                              |
| json                       | 2.85 ms                                                                     | 2.90 ms: 1.02x slower                                              |
| genshi_text                | 18.2 ms                                                                     | 18.6 ms: 1.02x slower                                              |
| async_generators           | 254 ms                                                                      | 259 ms: 1.02x slower                                               |
| mako                       | 5.05 ms                                                                     | 5.16 ms: 1.02x slower                                              |
| richards                   | 33.5 ms                                                                     | 34.2 ms: 1.02x slower                                              |
| nqueens                    | 63.4 ms                                                                     | 65.1 ms: 1.03x slower                                              |
| mdp                        | 1.48 sec                                                                    | 1.52 sec: 1.03x slower                                             |
| json_dumps                 | 6.19 ms                                                                     | 6.42 ms: 1.04x slower                                              |
| typing_runtime_protocols   | 110 us                                                                      | 116 us: 1.05x slower                                               |
| asyncio_websockets         | 301 ms                                                                      | 325 ms: 1.08x slower                                               |
| Geometric mean             | (ref)                                                                       | 1.00x faster                                                       |

Benchmark hidden because not significant (33): k_core, python_startup, async_tree_none, telco, xml_etree_process, float, async_tree_memoization, subparsers, logging_format, coverage, async_tree_cpu_io_mixed, docutils, pidigits, pathlib, bpe_tokeniser, xml_etree_iterparse, pylint, gc_traversal, mypy2, coroutines, bench_mp_pool, deepcopy, thrift, html5lib, create_gc_cycles, sphinx, sympy_str, many_optionals, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg, deepcopy_reduce, bench_thread_pool

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 63.47% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown