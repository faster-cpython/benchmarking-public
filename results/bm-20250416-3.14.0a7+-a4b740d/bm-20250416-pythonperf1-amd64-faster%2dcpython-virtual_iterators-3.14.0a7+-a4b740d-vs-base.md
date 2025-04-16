# Results vs. base

- fork: faster-cpython
- ref: virtual_iterators
- machine: windows-amd64
- commit hash: a4b740d
- commit date: 2025-04-16
- overall geometric mean: 1.003x slower
- HPT reliability: 94.68%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                                      | 217 ms: 1.02x faster                                                               |
| html5lib       | 37.6 ms                                                                     | 39.4 ms: 1.05x slower                                                              |
| sphinx         | 651 ms                                                                      | 636 ms: 1.02x faster                                                               |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                       |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_generators           | 228 ms                                                                      | 221 ms: 1.04x faster                                                               |
| async_tree_cpu_io_mixed_tg | 337 ms                                                                      | 340 ms: 1.01x slower                                                               |
| async_tree_none_tg         | 171 ms                                                                      | 173 ms: 1.01x slower                                                               |
| asyncio_websockets         | 158 ms                                                                      | 161 ms: 1.02x slower                                                               |
| async_tree_memoization     | 204 ms                                                                      | 208 ms: 1.02x slower                                                               |
| async_tree_none            | 178 ms                                                                      | 182 ms: 1.02x slower                                                               |
| async_tree_memoization_tg  | 209 ms                                                                      | 214 ms: 1.02x slower                                                               |
| async_tree_io_tg           | 394 ms                                                                      | 405 ms: 1.03x slower                                                               |
| coroutines                 | 13.3 ms                                                                     | 13.7 ms: 1.03x slower                                                              |
| Geometric mean             | (ref)                                                                       | 1.01x slower                                                                       |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                                      | 149 ms: 1.01x faster                                                               |
| float          | 42.9 ms                                                                     | 43.3 ms: 1.01x slower                                                              |
| nbody          | 61.3 ms                                                                     | 63.0 ms: 1.03x slower                                                              |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 1.49 ms                                                                     | 1.43 ms: 1.04x faster                                                              |
| regex_v8       | 14.7 ms                                                                     | 14.2 ms: 1.04x faster                                                              |
| regex_dna      | 120 ms                                                                      | 116 ms: 1.03x faster                                                               |
| regex_compile  | 79.5 ms                                                                     | 81.0 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| json_loads           | 15.5 us                                                                     | 14.9 us: 1.04x faster                                                              |
| json_dumps           | 6.79 ms                                                                     | 6.58 ms: 1.03x faster                                                              |
| xml_etree_process    | 39.9 ms                                                                     | 38.9 ms: 1.02x faster                                                              |
| xml_etree_generate   | 55.7 ms                                                                     | 55.4 ms: 1.01x faster                                                              |
| pickle_pure_python   | 210 us                                                                      | 212 us: 1.01x slower                                                               |
| xml_etree_parse      | 89.8 ms                                                                     | 90.8 ms: 1.01x slower                                                              |
| tomli_loads          | 1.36 sec                                                                    | 1.39 sec: 1.02x slower                                                             |
| xml_etree_iterparse  | 64.0 ms                                                                     | 65.4 ms: 1.02x slower                                                              |
| unpickle_pure_python | 133 us                                                                      | 139 us: 1.04x slower                                                               |
| Geometric mean       | (ref)                                                                       | 1.00x slower                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|------------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 20.9 ms                                                                     | 20.5 ms: 1.02x faster                                                              |
| Geometric mean         | (ref)                                                                       | 1.01x faster                                                                       |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|-----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| genshi_text     | 15.7 ms                                                                     | 15.5 ms: 1.02x faster                                                              |
| mako            | 6.62 ms                                                                     | 6.66 ms: 1.01x slower                                                              |
| django_template | 24.1 ms                                                                     | 24.4 ms: 1.01x slower                                                              |
| Geometric mean  | (ref)                                                                       | 1.00x slower                                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-pythonperf1-amd64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mdp                        | 813 ms                                                                      | 769 ms: 1.06x faster                                                               |
| comprehensions             | 11.2 us                                                                     | 10.7 us: 1.05x faster                                                              |
| typing_runtime_protocols   | 106 us                                                                      | 101 us: 1.04x faster                                                               |
| json_loads                 | 15.5 us                                                                     | 14.9 us: 1.04x faster                                                              |
| regex_effbot               | 1.49 ms                                                                     | 1.43 ms: 1.04x faster                                                              |
| nqueens                    | 61.9 ms                                                                     | 59.6 ms: 1.04x faster                                                              |
| regex_v8                   | 14.7 ms                                                                     | 14.2 ms: 1.04x faster                                                              |
| async_generators           | 228 ms                                                                      | 221 ms: 1.04x faster                                                               |
| regex_dna                  | 120 ms                                                                      | 116 ms: 1.03x faster                                                               |
| json_dumps                 | 6.79 ms                                                                     | 6.58 ms: 1.03x faster                                                              |
| coverage                   | 50.4 ms                                                                     | 48.8 ms: 1.03x faster                                                              |
| sqlglot_v2_normalize       | 70.9 ms                                                                     | 68.9 ms: 1.03x faster                                                              |
| meteor_contest             | 73.1 ms                                                                     | 71.2 ms: 1.03x faster                                                              |
| xml_etree_process          | 39.9 ms                                                                     | 38.9 ms: 1.02x faster                                                              |
| sphinx                     | 651 ms                                                                      | 636 ms: 1.02x faster                                                               |
| generators                 | 20.6 ms                                                                     | 20.1 ms: 1.02x faster                                                              |
| python_startup_no_site     | 20.9 ms                                                                     | 20.5 ms: 1.02x faster                                                              |
| sqlite_synth               | 1.57 us                                                                     | 1.54 us: 1.02x faster                                                              |
| 2to3                       | 221 ms                                                                      | 217 ms: 1.02x faster                                                               |
| genshi_text                | 15.7 ms                                                                     | 15.5 ms: 1.02x faster                                                              |
| sqlglot_v2_optimize        | 34.0 ms                                                                     | 33.5 ms: 1.01x faster                                                              |
| telco                      | 4.64 ms                                                                     | 4.59 ms: 1.01x faster                                                              |
| logging_simple             | 6.31 us                                                                     | 6.25 us: 1.01x faster                                                              |
| subparsers                 | 15.8 ms                                                                     | 15.7 ms: 1.01x faster                                                              |
| create_gc_cycles           | 1.26 ms                                                                     | 1.25 ms: 1.01x faster                                                              |
| pprint_pformat             | 1.00 sec                                                                    | 997 ms: 1.01x faster                                                               |
| pidigits                   | 150 ms                                                                      | 149 ms: 1.01x faster                                                               |
| xml_etree_generate         | 55.7 ms                                                                     | 55.4 ms: 1.01x faster                                                              |
| pprint_safe_repr           | 494 ms                                                                      | 492 ms: 1.00x faster                                                               |
| mako                       | 6.62 ms                                                                     | 6.66 ms: 1.01x slower                                                              |
| spectral_norm              | 57.5 ms                                                                     | 57.9 ms: 1.01x slower                                                              |
| float                      | 42.9 ms                                                                     | 43.3 ms: 1.01x slower                                                              |
| logging_silent             | 54.2 ns                                                                     | 54.7 ns: 1.01x slower                                                              |
| async_tree_cpu_io_mixed_tg | 337 ms                                                                      | 340 ms: 1.01x slower                                                               |
| pickle_pure_python         | 210 us                                                                      | 212 us: 1.01x slower                                                               |
| deepcopy_reduce            | 1.80 us                                                                     | 1.82 us: 1.01x slower                                                              |
| async_tree_none_tg         | 171 ms                                                                      | 173 ms: 1.01x slower                                                               |
| xml_etree_parse            | 89.8 ms                                                                     | 90.8 ms: 1.01x slower                                                              |
| pyflate                    | 279 ms                                                                      | 283 ms: 1.01x slower                                                               |
| raytrace                   | 174 ms                                                                      | 176 ms: 1.01x slower                                                               |
| bpe_tokeniser              | 2.90 sec                                                                    | 2.94 sec: 1.01x slower                                                             |
| django_template            | 24.1 ms                                                                     | 24.4 ms: 1.01x slower                                                              |
| connected_components       | 331 ms                                                                      | 336 ms: 1.01x slower                                                               |
| asyncio_websockets         | 158 ms                                                                      | 161 ms: 1.02x slower                                                               |
| sqlglot_v2_transpile       | 1.01 ms                                                                     | 1.03 ms: 1.02x slower                                                              |
| chaos                      | 37.9 ms                                                                     | 38.6 ms: 1.02x slower                                                              |
| regex_compile              | 79.5 ms                                                                     | 81.0 ms: 1.02x slower                                                              |
| richards_super             | 31.0 ms                                                                     | 31.6 ms: 1.02x slower                                                              |
| richards                   | 27.5 ms                                                                     | 28.1 ms: 1.02x slower                                                              |
| hexiom                     | 3.94 ms                                                                     | 4.02 ms: 1.02x slower                                                              |
| tomli_loads                | 1.36 sec                                                                    | 1.39 sec: 1.02x slower                                                             |
| dulwich_log                | 41.7 ms                                                                     | 42.6 ms: 1.02x slower                                                              |
| xml_etree_iterparse        | 64.0 ms                                                                     | 65.4 ms: 1.02x slower                                                              |
| async_tree_memoization     | 204 ms                                                                      | 208 ms: 1.02x slower                                                               |
| async_tree_none            | 178 ms                                                                      | 182 ms: 1.02x slower                                                               |
| crypto_pyaes               | 46.4 ms                                                                     | 47.5 ms: 1.02x slower                                                              |
| async_tree_memoization_tg  | 209 ms                                                                      | 214 ms: 1.02x slower                                                               |
| sqlglot_v2_parse           | 805 us                                                                      | 825 us: 1.02x slower                                                               |
| go                         | 76.4 ms                                                                     | 78.4 ms: 1.02x slower                                                              |
| async_tree_io_tg           | 394 ms                                                                      | 405 ms: 1.03x slower                                                               |
| nbody                      | 61.3 ms                                                                     | 63.0 ms: 1.03x slower                                                              |
| scimark_sor                | 74.5 ms                                                                     | 76.8 ms: 1.03x slower                                                              |
| coroutines                 | 13.3 ms                                                                     | 13.7 ms: 1.03x slower                                                              |
| scimark_monte_carlo        | 38.3 ms                                                                     | 39.9 ms: 1.04x slower                                                              |
| fannkuch                   | 246 ms                                                                      | 257 ms: 1.04x slower                                                               |
| deltablue                  | 2.10 ms                                                                     | 2.19 ms: 1.04x slower                                                              |
| unpickle_pure_python       | 133 us                                                                      | 139 us: 1.04x slower                                                               |
| html5lib                   | 37.6 ms                                                                     | 39.4 ms: 1.05x slower                                                              |
| deepcopy_memo              | 17.7 us                                                                     | 18.5 us: 1.05x slower                                                              |
| scimark_lu                 | 56.6 ms                                                                     | 59.5 ms: 1.05x slower                                                              |
| scimark_sparse_mat_mult    | 2.45 ms                                                                     | 2.59 ms: 1.06x slower                                                              |
| Geometric mean             | (ref)                                                                       | 1.00x slower                                                                       |

Benchmark hidden because not significant (17): bench_thread_pool, logging_format, many_optionals, k_core, pathlib, bench_mp_pool, genshi_xml, python_startup, docutils, pycparser, shortest_path, scimark_fft, deepcopy, json, gc_traversal, async_tree_cpu_io_mixed, async_tree_io
Ignored benchmarks (5) of results/bm-20250414-3.14.0a7+-844596c/bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c.json: pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 94.68% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown