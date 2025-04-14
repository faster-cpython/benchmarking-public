# Results vs. base

- fork: mdboom
- ref: aa_test_2025_2
- machine: windows-amd64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.002x slower
- HPT reliability: 94.73%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 232 ms                                                                      | 233 ms: 1.01x slower                                                  |
| docutils       | 1.68 sec                                                                    | 1.70 sec: 1.01x slower                                                |
| html5lib       | 39.9 ms                                                                     | 40.7 ms: 1.02x slower                                                 |
| sphinx         | 659 ms                                                                      | 666 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_websockets         | 312 ms                                                                      | 298 ms: 1.05x faster                                                  |
| async_generators           | 227 ms                                                                      | 225 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed    | 344 ms                                                                      | 347 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg | 344 ms                                                                      | 348 ms: 1.01x slower                                                  |
| async_tree_none            | 183 ms                                                                      | 186 ms: 1.02x slower                                                  |
| coroutines                 | 14.8 ms                                                                     | 15.3 ms: 1.03x slower                                                 |
| Geometric mean             | (ref)                                                                       | 1.00x slower                                                          |

Benchmark hidden because not significant (5): async_tree_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 147 ms                                                                      | 148 ms: 1.01x slower                                                  |
| nbody          | 73.6 ms                                                                     | 77.3 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 88.7 ms                                                                     | 88.2 ms: 1.01x faster                                                 |
| regex_dna      | 116 ms                                                                      | 117 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                          |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|---------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python  | 240 us                                                                      | 239 us: 1.01x faster                                                  |
| xml_etree_process   | 43.5 ms                                                                     | 43.7 ms: 1.00x slower                                                 |
| json_loads          | 14.4 us                                                                     | 14.5 us: 1.01x slower                                                 |
| xml_etree_iterparse | 64.7 ms                                                                     | 65.2 ms: 1.01x slower                                                 |
| xml_etree_parse     | 87.7 ms                                                                     | 88.5 ms: 1.01x slower                                                 |
| Geometric mean      | (ref)                                                                       | 1.00x slower                                                          |

Benchmark hidden because not significant (4): unpickle_pure_python, xml_etree_generate, json_dumps, tomli_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 36.4 ms                                                                     | 35.1 ms: 1.04x faster                                                 |
| genshi_text     | 16.9 ms                                                                     | 16.6 ms: 1.02x faster                                                 |
| mako            | 6.95 ms                                                                     | 6.89 ms: 1.01x faster                                                 |
| django_template | 25.0 ms                                                                     | 25.9 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                                       | 1.01x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20250121-pythonperf1-amd64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| scimark_lu                 | 68.4 ms                                                                     | 64.9 ms: 1.05x faster                                                 |
| asyncio_websockets         | 312 ms                                                                      | 298 ms: 1.05x faster                                                  |
| scimark_sor                | 91.2 ms                                                                     | 87.8 ms: 1.04x faster                                                 |
| genshi_xml                 | 36.4 ms                                                                     | 35.1 ms: 1.04x faster                                                 |
| crypto_pyaes               | 49.3 ms                                                                     | 48.0 ms: 1.03x faster                                                 |
| chaos                      | 42.8 ms                                                                     | 41.7 ms: 1.03x faster                                                 |
| scimark_fft                | 192 ms                                                                      | 187 ms: 1.02x faster                                                  |
| genshi_text                | 16.9 ms                                                                     | 16.6 ms: 1.02x faster                                                 |
| many_optionals             | 446 us                                                                      | 437 us: 1.02x faster                                                  |
| coverage                   | 50.3 ms                                                                     | 49.4 ms: 1.02x faster                                                 |
| bpe_tokeniser              | 3.07 sec                                                                    | 3.02 sec: 1.02x faster                                                |
| subparsers                 | 16.4 ms                                                                     | 16.1 ms: 1.02x faster                                                 |
| fannkuch                   | 273 ms                                                                      | 269 ms: 1.02x faster                                                  |
| meteor_contest             | 76.6 ms                                                                     | 75.5 ms: 1.01x faster                                                 |
| scimark_monte_carlo        | 48.0 ms                                                                     | 47.3 ms: 1.01x faster                                                 |
| async_generators           | 227 ms                                                                      | 225 ms: 1.01x faster                                                  |
| spectral_norm              | 63.9 ms                                                                     | 63.4 ms: 1.01x faster                                                 |
| mako                       | 6.95 ms                                                                     | 6.89 ms: 1.01x faster                                                 |
| pprint_safe_repr           | 540 ms                                                                      | 536 ms: 1.01x faster                                                  |
| regex_compile              | 88.7 ms                                                                     | 88.2 ms: 1.01x faster                                                 |
| shortest_path              | 351 ms                                                                      | 349 ms: 1.01x faster                                                  |
| pickle_pure_python         | 240 us                                                                      | 239 us: 1.01x faster                                                  |
| scimark_sparse_mat_mult    | 2.51 ms                                                                     | 2.50 ms: 1.01x faster                                                 |
| nqueens                    | 64.9 ms                                                                     | 64.6 ms: 1.00x faster                                                 |
| dulwich_log                | 42.6 ms                                                                     | 42.5 ms: 1.00x faster                                                 |
| sympy_integrate            | 13.6 ms                                                                     | 13.6 ms: 1.00x slower                                                 |
| raytrace                   | 209 ms                                                                      | 209 ms: 1.00x slower                                                  |
| logging_silent             | 72.3 ns                                                                     | 72.5 ns: 1.00x slower                                                 |
| connected_components       | 318 ms                                                                      | 320 ms: 1.00x slower                                                  |
| xml_etree_process          | 43.5 ms                                                                     | 43.7 ms: 1.00x slower                                                 |
| 2to3                       | 232 ms                                                                      | 233 ms: 1.01x slower                                                  |
| sqlglot_parse              | 885 us                                                                      | 890 us: 1.01x slower                                                  |
| json_loads                 | 14.4 us                                                                     | 14.5 us: 1.01x slower                                                 |
| richards                   | 31.6 ms                                                                     | 31.8 ms: 1.01x slower                                                 |
| deltablue                  | 2.37 ms                                                                     | 2.38 ms: 1.01x slower                                                 |
| sympy_expand               | 303 ms                                                                      | 305 ms: 1.01x slower                                                  |
| deepcopy_reduce            | 1.85 us                                                                     | 1.86 us: 1.01x slower                                                 |
| xml_etree_iterparse        | 64.7 ms                                                                     | 65.2 ms: 1.01x slower                                                 |
| sympy_str                  | 178 ms                                                                      | 179 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed    | 344 ms                                                                      | 347 ms: 1.01x slower                                                  |
| sqlglot_normalize          | 197 ms                                                                      | 199 ms: 1.01x slower                                                  |
| docutils                   | 1.68 sec                                                                    | 1.70 sec: 1.01x slower                                                |
| xml_etree_parse            | 87.7 ms                                                                     | 88.5 ms: 1.01x slower                                                 |
| pidigits                   | 147 ms                                                                      | 148 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg | 344 ms                                                                      | 348 ms: 1.01x slower                                                  |
| regex_dna                  | 116 ms                                                                      | 117 ms: 1.01x slower                                                  |
| deepcopy                   | 182 us                                                                      | 184 us: 1.01x slower                                                  |
| sphinx                     | 659 ms                                                                      | 666 ms: 1.01x slower                                                  |
| sympy_sum                  | 90.2 ms                                                                     | 91.3 ms: 1.01x slower                                                 |
| sqlglot_optimize           | 36.1 ms                                                                     | 36.7 ms: 1.02x slower                                                 |
| async_tree_none            | 183 ms                                                                      | 186 ms: 1.02x slower                                                  |
| html5lib                   | 39.9 ms                                                                     | 40.7 ms: 1.02x slower                                                 |
| logging_simple             | 6.39 us                                                                     | 6.53 us: 1.02x slower                                                 |
| deepcopy_memo              | 19.6 us                                                                     | 20.0 us: 1.02x slower                                                 |
| logging_format             | 6.80 us                                                                     | 6.99 us: 1.03x slower                                                 |
| coroutines                 | 14.8 ms                                                                     | 15.3 ms: 1.03x slower                                                 |
| django_template            | 25.0 ms                                                                     | 25.9 ms: 1.04x slower                                                 |
| nbody                      | 73.6 ms                                                                     | 77.3 ms: 1.05x slower                                                 |
| mdp                        | 1.46 sec                                                                    | 1.56 sec: 1.07x slower                                                |
| sqlite_synth               | 1.63 us                                                                     | 1.74 us: 1.07x slower                                                 |
| telco                      | 4.77 ms                                                                     | 5.44 ms: 1.14x slower                                                 |
| Geometric mean             | (ref)                                                                       | 1.00x slower                                                          |

Benchmark hidden because not significant (33): unpickle_pure_python, typing_runtime_protocols, json, richards_super, regex_effbot, python_startup_no_site, python_startup, sqlglot_transpile, pprint_pformat, xml_etree_generate, gc_traversal, pathlib, go, hexiom, bench_mp_pool, json_dumps, pyflate, float, tomli_loads, create_gc_cycles, async_tree_io, async_tree_none_tg, async_tree_memoization_tg, generators, async_tree_io_tg, thrift, async_tree_memoization, pylint, comprehensions, pycparser, k_core, bench_thread_pool, regex_v8

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 94.73% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown