# Results vs. base

- fork: mdboom
- ref: python_startup_time
- machine: windows-amd64
- commit hash: 9fc1238
- commit date: 2025-04-25
- overall geometric mean: 1.005x slower
- HPT reliability: 97.76%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|--------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets | 162 ms                                                                      | 156 ms: 1.04x faster                                                       |
| async_generators   | 229 ms                                                                      | 221 ms: 1.03x faster                                                       |
| async_tree_io_tg   | 397 ms                                                                      | 393 ms: 1.01x faster                                                       |
| async_tree_none    | 180 ms                                                                      | 178 ms: 1.01x faster                                                       |
| coroutines         | 13.4 ms                                                                     | 13.8 ms: 1.03x slower                                                      |
| Geometric mean     | (ref)                                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 42.3 ms                                                                     | 42.6 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 79.6 ms                                                                     | 80.6 ms: 1.01x slower                                                      |
| regex_effbot   | 1.41 ms                                                                     | 1.47 ms: 1.04x slower                                                      |
| regex_dna      | 115 ms                                                                      | 121 ms: 1.06x slower                                                       |
| regex_v8       | 13.4 ms                                                                     | 14.7 ms: 1.10x slower                                                      |
| Geometric mean | (ref)                                                                       | 1.05x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 6.80 ms                                                                     | 6.69 ms: 1.02x faster                                                      |
| xml_etree_parse      | 89.4 ms                                                                     | 88.5 ms: 1.01x faster                                                      |
| pickle_pure_python   | 209 us                                                                      | 210 us: 1.01x slower                                                       |
| xml_etree_process    | 39.5 ms                                                                     | 39.9 ms: 1.01x slower                                                      |
| unpickle_pure_python | 134 us                                                                      | 136 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 63.7 ms                                                                     | 64.5 ms: 1.01x slower                                                      |
| xml_etree_generate   | 55.4 ms                                                                     | 56.3 ms: 1.02x slower                                                      |
| tomli_loads          | 1.35 sec                                                                    | 1.39 sec: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 20.5 ms                                                                     | 19.9 ms: 1.03x faster                                                      |
| Geometric mean         | (ref)                                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml     | 34.3 ms                                                                     | 33.8 ms: 1.01x faster                                                      |
| genshi_text    | 15.4 ms                                                                     | 15.5 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark              | bm-20250421-pythonperf1-amd64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| generators             | 20.1 ms                                                                     | 19.2 ms: 1.05x faster                                                      |
| scimark_fft            | 178 ms                                                                      | 171 ms: 1.04x faster                                                       |
| asyncio_websockets     | 162 ms                                                                      | 156 ms: 1.04x faster                                                       |
| async_generators       | 229 ms                                                                      | 221 ms: 1.03x faster                                                       |
| spectral_norm          | 56.4 ms                                                                     | 54.7 ms: 1.03x faster                                                      |
| python_startup_no_site | 20.5 ms                                                                     | 19.9 ms: 1.03x faster                                                      |
| k_core                 | 1.76 sec                                                                    | 1.72 sec: 1.02x faster                                                     |
| logging_simple         | 6.35 us                                                                     | 6.22 us: 1.02x faster                                                      |
| json_dumps             | 6.80 ms                                                                     | 6.69 ms: 1.02x faster                                                      |
| genshi_xml             | 34.3 ms                                                                     | 33.8 ms: 1.01x faster                                                      |
| pathlib                | 32.4 ms                                                                     | 32.0 ms: 1.01x faster                                                      |
| gc_traversal           | 2.11 ms                                                                     | 2.08 ms: 1.01x faster                                                      |
| xml_etree_parse        | 89.4 ms                                                                     | 88.5 ms: 1.01x faster                                                      |
| async_tree_io_tg       | 397 ms                                                                      | 393 ms: 1.01x faster                                                       |
| logging_format         | 6.80 us                                                                     | 6.73 us: 1.01x faster                                                      |
| raytrace               | 174 ms                                                                      | 173 ms: 1.01x faster                                                       |
| async_tree_none        | 180 ms                                                                      | 178 ms: 1.01x faster                                                       |
| scimark_lu             | 58.9 ms                                                                     | 58.5 ms: 1.01x faster                                                      |
| sympy_expand           | 295 ms                                                                      | 293 ms: 1.01x faster                                                       |
| mdp                    | 785 ms                                                                      | 781 ms: 1.01x faster                                                       |
| sympy_integrate        | 12.5 ms                                                                     | 12.5 ms: 1.01x slower                                                      |
| pickle_pure_python     | 209 us                                                                      | 210 us: 1.01x slower                                                       |
| many_optionals         | 421 us                                                                      | 424 us: 1.01x slower                                                       |
| genshi_text            | 15.4 ms                                                                     | 15.5 ms: 1.01x slower                                                      |
| float                  | 42.3 ms                                                                     | 42.6 ms: 1.01x slower                                                      |
| sympy_sum              | 87.8 ms                                                                     | 88.5 ms: 1.01x slower                                                      |
| xml_etree_process      | 39.5 ms                                                                     | 39.9 ms: 1.01x slower                                                      |
| subparsers             | 15.9 ms                                                                     | 16.1 ms: 1.01x slower                                                      |
| unpickle_pure_python   | 134 us                                                                      | 136 us: 1.01x slower                                                       |
| xml_etree_iterparse    | 63.7 ms                                                                     | 64.5 ms: 1.01x slower                                                      |
| regex_compile          | 79.6 ms                                                                     | 80.6 ms: 1.01x slower                                                      |
| chaos                  | 37.9 ms                                                                     | 38.4 ms: 1.01x slower                                                      |
| sqlglot_v2_parse       | 798 us                                                                      | 808 us: 1.01x slower                                                       |
| crypto_pyaes           | 46.7 ms                                                                     | 47.4 ms: 1.01x slower                                                      |
| deepcopy_memo          | 18.2 us                                                                     | 18.5 us: 1.02x slower                                                      |
| scimark_sor            | 75.0 ms                                                                     | 76.2 ms: 1.02x slower                                                      |
| xml_etree_generate     | 55.4 ms                                                                     | 56.3 ms: 1.02x slower                                                      |
| fannkuch               | 250 ms                                                                      | 255 ms: 1.02x slower                                                       |
| telco                  | 4.53 ms                                                                     | 4.61 ms: 1.02x slower                                                      |
| bpe_tokeniser          | 2.77 sec                                                                    | 2.83 sec: 1.02x slower                                                     |
| go                     | 75.8 ms                                                                     | 77.3 ms: 1.02x slower                                                      |
| comprehensions         | 11.1 us                                                                     | 11.4 us: 1.03x slower                                                      |
| tomli_loads            | 1.35 sec                                                                    | 1.39 sec: 1.03x slower                                                     |
| coroutines             | 13.4 ms                                                                     | 13.8 ms: 1.03x slower                                                      |
| meteor_contest         | 72.7 ms                                                                     | 74.8 ms: 1.03x slower                                                      |
| pprint_pformat         | 991 ms                                                                      | 1.02 sec: 1.03x slower                                                     |
| richards               | 27.6 ms                                                                     | 28.4 ms: 1.03x slower                                                      |
| richards_super         | 31.4 ms                                                                     | 32.4 ms: 1.03x slower                                                      |
| hexiom                 | 3.94 ms                                                                     | 4.07 ms: 1.03x slower                                                      |
| scimark_monte_carlo    | 39.9 ms                                                                     | 41.3 ms: 1.03x slower                                                      |
| deltablue              | 2.10 ms                                                                     | 2.17 ms: 1.03x slower                                                      |
| pprint_safe_repr       | 486 ms                                                                      | 504 ms: 1.04x slower                                                       |
| coverage               | 49.8 ms                                                                     | 51.7 ms: 1.04x slower                                                      |
| regex_effbot           | 1.41 ms                                                                     | 1.47 ms: 1.04x slower                                                      |
| regex_dna              | 115 ms                                                                      | 121 ms: 1.06x slower                                                       |
| regex_v8               | 13.4 ms                                                                     | 14.7 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (37): bench_thread_pool, typing_runtime_protocols, connected_components, bench_mp_pool, async_tree_memoization_tg, python_startup, json, shortest_path, sympy_str, logging_silent, deepcopy_reduce, create_gc_cycles, pyflate, docutils, nbody, async_tree_io, dulwich_log, sqlite_synth, pylint, json_loads, sqlglot_v2_transpile, async_tree_cpu_io_mixed_tg, pidigits, 2to3, scimark_sparse_mat_mult, deepcopy, async_tree_memoization, sqlglot_v2_optimize, sqlglot_v2_normalize, nqueens, async_tree_cpu_io_mixed, django_template, html5lib, mako, async_tree_none_tg, pycparser, sphinx

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 97.76% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown