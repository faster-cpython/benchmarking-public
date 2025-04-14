# Results vs. base

- fork: faster-cpython
- ref: c_recursion_limit
- machine: windows-x86
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.021x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250214-pythonperf1_win32-x86-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                                          | 258 ms: 1.02x faster                                                                   |
| docutils       | 1.91 sec                                                                        | 1.85 sec: 1.03x faster                                                                 |
| html5lib       | 49.1 ms                                                                         | 50.3 ms: 1.02x slower                                                                  |
| sphinx         | 775 ms                                                                          | 754 ms: 1.03x faster                                                                   |
| Geometric mean | (ref)                                                                           | 1.01x faster                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250214-pythonperf1_win32-x86-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| coroutines                 | 16.9 ms                                                                         | 16.0 ms: 1.06x faster                                                                  |
| async_tree_none_tg         | 220 ms                                                                          | 209 ms: 1.05x faster                                                                   |
| async_tree_memoization_tg  | 275 ms                                                                          | 263 ms: 1.05x faster                                                                   |
| async_tree_io_tg           | 505 ms                                                                          | 484 ms: 1.04x faster                                                                   |
| async_tree_io              | 505 ms                                                                          | 486 ms: 1.04x faster                                                                   |
| async_tree_none            | 236 ms                                                                          | 228 ms: 1.03x faster                                                                   |
| async_tree_memoization     | 288 ms                                                                          | 278 ms: 1.03x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 475 ms                                                                          | 464 ms: 1.02x faster                                                                   |
| async_generators           | 322 ms                                                                          | 317 ms: 1.02x faster                                                                   |
| async_tree_cpu_io_mixed    | 483 ms                                                                          | 481 ms: 1.00x faster                                                                   |
| Geometric mean             | (ref)                                                                           | 1.03x faster                                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250214-pythonperf1_win32-x86-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 58.7 ms                                                                         | 55.3 ms: 1.06x faster                                                                  |
| nbody          | 87.9 ms                                                                         | 91.0 ms: 1.04x slower                                                                  |
| Geometric mean | (ref)                                                                           | 1.01x faster                                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250214-pythonperf1_win32-x86-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 114 ms                                                                          | 111 ms: 1.03x faster                                                                   |
| regex_v8       | 15.8 ms                                                                         | 15.5 ms: 1.02x faster                                                                  |
| regex_dna      | 119 ms                                                                          | 120 ms: 1.01x slower                                                                   |
| regex_effbot   | 1.55 ms                                                                         | 1.59 ms: 1.03x slower                                                                  |
| Geometric mean | (ref)                                                                           | 1.01x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250214-pythonperf1_win32-x86-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 9.42 ms                                                                         | 8.32 ms: 1.13x faster                                                                  |
| pickle_pure_python   | 312 us                                                                          | 287 us: 1.08x faster                                                                   |
| tomli_loads          | 1.84 sec                                                                        | 1.75 sec: 1.05x faster                                                                 |
| xml_etree_generate   | 72.1 ms                                                                         | 68.8 ms: 1.05x faster                                                                  |
| json_loads           | 22.4 us                                                                         | 21.6 us: 1.04x faster                                                                  |
| unpickle_pure_python | 193 us                                                                          | 186 us: 1.03x faster                                                                   |
| xml_etree_process    | 52.5 ms                                                                         | 51.3 ms: 1.02x faster                                                                  |
| xml_etree_iterparse  | 67.5 ms                                                                         | 66.6 ms: 1.01x faster                                                                  |
| xml_etree_parse      | 108 ms                                                                          | 107 ms: 1.01x faster                                                                   |
| Geometric mean       | (ref)                                                                           | 1.05x faster                                                                           |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250214-pythonperf1_win32-x86-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-----------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 38.1 ms                                                                         | 34.1 ms: 1.12x faster                                                                  |
| mako            | 8.61 ms                                                                         | 7.97 ms: 1.08x faster                                                                  |
| genshi_text     | 24.6 ms                                                                         | 23.1 ms: 1.06x faster                                                                  |
| genshi_xml      | 51.5 ms                                                                         | 50.5 ms: 1.02x faster                                                                  |
| Geometric mean  | (ref)                                                                           | 1.07x faster                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20250214-pythonperf1_win32-x86-python-1775091dc163d1fa76c3-3.14.0a5+-1775091 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:-------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps                 | 9.42 ms                                                                         | 8.32 ms: 1.13x faster                                                                  |
| logging_silent             | 82.2 ns                                                                         | 72.8 ns: 1.13x faster                                                                  |
| django_template            | 38.1 ms                                                                         | 34.1 ms: 1.12x faster                                                                  |
| richards                   | 40.8 ms                                                                         | 37.3 ms: 1.09x faster                                                                  |
| raytrace                   | 278 ms                                                                          | 254 ms: 1.09x faster                                                                   |
| pickle_pure_python         | 312 us                                                                          | 287 us: 1.08x faster                                                                   |
| mako                       | 8.61 ms                                                                         | 7.97 ms: 1.08x faster                                                                  |
| telco                      | 7.08 ms                                                                         | 6.57 ms: 1.08x faster                                                                  |
| deepcopy                   | 263 us                                                                          | 244 us: 1.08x faster                                                                   |
| pprint_pformat             | 1.49 sec                                                                        | 1.39 sec: 1.07x faster                                                                 |
| mdp                        | 1.80 sec                                                                        | 1.69 sec: 1.06x faster                                                                 |
| sqlglot_optimize           | 47.6 ms                                                                         | 44.7 ms: 1.06x faster                                                                  |
| genshi_text                | 24.6 ms                                                                         | 23.1 ms: 1.06x faster                                                                  |
| generators                 | 28.5 ms                                                                         | 26.9 ms: 1.06x faster                                                                  |
| crypto_pyaes               | 65.5 ms                                                                         | 61.7 ms: 1.06x faster                                                                  |
| scimark_lu                 | 73.8 ms                                                                         | 69.6 ms: 1.06x faster                                                                  |
| float                      | 58.7 ms                                                                         | 55.3 ms: 1.06x faster                                                                  |
| pprint_safe_repr           | 708 ms                                                                          | 669 ms: 1.06x faster                                                                   |
| coroutines                 | 16.9 ms                                                                         | 16.0 ms: 1.06x faster                                                                  |
| coverage                   | 54.4 ms                                                                         | 51.5 ms: 1.06x faster                                                                  |
| tomli_loads                | 1.84 sec                                                                        | 1.75 sec: 1.05x faster                                                                 |
| deltablue                  | 3.00 ms                                                                         | 2.86 ms: 1.05x faster                                                                  |
| sqlglot_parse              | 1.21 ms                                                                         | 1.15 ms: 1.05x faster                                                                  |
| xml_etree_generate         | 72.1 ms                                                                         | 68.8 ms: 1.05x faster                                                                  |
| deepcopy_reduce            | 2.76 us                                                                         | 2.63 us: 1.05x faster                                                                  |
| async_tree_none_tg         | 220 ms                                                                          | 209 ms: 1.05x faster                                                                   |
| nqueens                    | 83.6 ms                                                                         | 79.8 ms: 1.05x faster                                                                  |
| async_tree_memoization_tg  | 275 ms                                                                          | 263 ms: 1.05x faster                                                                   |
| richards_super             | 44.9 ms                                                                         | 43.0 ms: 1.05x faster                                                                  |
| hexiom                     | 5.55 ms                                                                         | 5.31 ms: 1.05x faster                                                                  |
| sqlglot_transpile          | 1.46 ms                                                                         | 1.40 ms: 1.04x faster                                                                  |
| async_tree_io_tg           | 505 ms                                                                          | 484 ms: 1.04x faster                                                                   |
| sympy_expand               | 407 ms                                                                          | 391 ms: 1.04x faster                                                                   |
| sympy_sum                  | 114 ms                                                                          | 110 ms: 1.04x faster                                                                   |
| sympy_str                  | 232 ms                                                                          | 222 ms: 1.04x faster                                                                   |
| async_tree_io              | 505 ms                                                                          | 486 ms: 1.04x faster                                                                   |
| go                         | 113 ms                                                                          | 108 ms: 1.04x faster                                                                   |
| dulwich_log                | 54.3 ms                                                                         | 52.5 ms: 1.04x faster                                                                  |
| json_loads                 | 22.4 us                                                                         | 21.6 us: 1.04x faster                                                                  |
| async_tree_none            | 236 ms                                                                          | 228 ms: 1.03x faster                                                                   |
| regex_compile              | 114 ms                                                                          | 111 ms: 1.03x faster                                                                   |
| async_tree_memoization     | 288 ms                                                                          | 278 ms: 1.03x faster                                                                   |
| many_optionals             | 567 us                                                                          | 549 us: 1.03x faster                                                                   |
| unpickle_pure_python       | 193 us                                                                          | 186 us: 1.03x faster                                                                   |
| docutils                   | 1.91 sec                                                                        | 1.85 sec: 1.03x faster                                                                 |
| typing_runtime_protocols   | 156 us                                                                          | 151 us: 1.03x faster                                                                   |
| sqlite_synth               | 1.94 us                                                                         | 1.89 us: 1.03x faster                                                                  |
| sphinx                     | 775 ms                                                                          | 754 ms: 1.03x faster                                                                   |
| spectral_norm              | 77.2 ms                                                                         | 75.1 ms: 1.03x faster                                                                  |
| pathlib                    | 35.0 ms                                                                         | 34.1 ms: 1.03x faster                                                                  |
| sympy_integrate            | 16.6 ms                                                                         | 16.1 ms: 1.03x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 475 ms                                                                          | 464 ms: 1.02x faster                                                                   |
| xml_etree_process          | 52.5 ms                                                                         | 51.3 ms: 1.02x faster                                                                  |
| 2to3                       | 264 ms                                                                          | 258 ms: 1.02x faster                                                                   |
| pyflate                    | 362 ms                                                                          | 354 ms: 1.02x faster                                                                   |
| regex_v8                   | 15.8 ms                                                                         | 15.5 ms: 1.02x faster                                                                  |
| genshi_xml                 | 51.5 ms                                                                         | 50.5 ms: 1.02x faster                                                                  |
| fannkuch                   | 307 ms                                                                          | 301 ms: 1.02x faster                                                                   |
| pylint                     | 231 ms                                                                          | 227 ms: 1.02x faster                                                                   |
| async_generators           | 322 ms                                                                          | 317 ms: 1.02x faster                                                                   |
| xml_etree_iterparse        | 67.5 ms                                                                         | 66.6 ms: 1.01x faster                                                                  |
| xml_etree_parse            | 108 ms                                                                          | 107 ms: 1.01x faster                                                                   |
| scimark_fft                | 234 ms                                                                          | 231 ms: 1.01x faster                                                                   |
| deepcopy_memo              | 22.6 us                                                                         | 22.3 us: 1.01x faster                                                                  |
| json                       | 4.51 ms                                                                         | 4.46 ms: 1.01x faster                                                                  |
| connected_components       | 272 ms                                                                          | 269 ms: 1.01x faster                                                                   |
| scimark_sor                | 104 ms                                                                          | 103 ms: 1.01x faster                                                                   |
| comprehensions             | 14.2 us                                                                         | 14.0 us: 1.01x faster                                                                  |
| chaos                      | 59.7 ms                                                                         | 59.2 ms: 1.01x faster                                                                  |
| shortest_path              | 305 ms                                                                          | 303 ms: 1.00x faster                                                                   |
| async_tree_cpu_io_mixed    | 483 ms                                                                          | 481 ms: 1.00x faster                                                                   |
| bpe_tokeniser              | 3.49 sec                                                                        | 3.48 sec: 1.00x faster                                                                 |
| meteor_contest             | 80.2 ms                                                                         | 80.6 ms: 1.01x slower                                                                  |
| regex_dna                  | 119 ms                                                                          | 120 ms: 1.01x slower                                                                   |
| gc_traversal               | 1.79 ms                                                                         | 1.81 ms: 1.01x slower                                                                  |
| html5lib                   | 49.1 ms                                                                         | 50.3 ms: 1.02x slower                                                                  |
| regex_effbot               | 1.55 ms                                                                         | 1.59 ms: 1.03x slower                                                                  |
| nbody                      | 87.9 ms                                                                         | 91.0 ms: 1.04x slower                                                                  |
| scimark_sparse_mat_mult    | 2.92 ms                                                                         | 3.04 ms: 1.04x slower                                                                  |
| sqlglot_normalize          | 104 ms                                                                          | 235 ms: 2.27x slower                                                                   |
| Geometric mean             | (ref)                                                                           | 1.02x faster                                                                           |

Benchmark hidden because not significant (14): subparsers, thrift, python_startup, pycparser, logging_format, python_startup_no_site, k_core, pidigits, asyncio_websockets, scimark_monte_carlo, create_gc_cycles, logging_simple, bench_mp_pool, bench_thread_pool

- Geometric mean (including insignificant results): 1.021x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown