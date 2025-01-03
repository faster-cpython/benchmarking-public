# Results vs. base

- fork: eendebakpt
- ref: iter_freelists
- machine: windows-x86
- commit hash: 05f479c
- commit date: 2025-01-02
- overall geometric mean: 1.014x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 243 ms                                                                          | 240 ms: 1.01x faster                                                          |
| docutils       | 1.80 sec                                                                        | 1.75 sec: 1.03x faster                                                        |
| html5lib       | 43.5 ms                                                                         | 42.4 ms: 1.03x faster                                                         |
| sphinx         | 727 ms                                                                          | 712 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                                           | 1.02x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|---------------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_generators          | 302 ms                                                                          | 295 ms: 1.03x faster                                                          |
| async_tree_memoization_tg | 222 ms                                                                          | 218 ms: 1.01x faster                                                          |
| coroutines                | 16.6 ms                                                                         | 16.3 ms: 1.01x faster                                                         |
| async_tree_none_tg        | 177 ms                                                                          | 175 ms: 1.01x faster                                                          |
| async_tree_memoization    | 240 ms                                                                          | 237 ms: 1.01x faster                                                          |
| async_tree_none           | 194 ms                                                                          | 196 ms: 1.01x slower                                                          |
| Geometric mean            | (ref)                                                                           | 1.01x faster                                                                  |

Benchmark hidden because not significant (5): async_tree_io, async_tree_io_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 197 ms                                                                          | 196 ms: 1.00x faster                                                          |
| float          | 55.8 ms                                                                         | 56.4 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                           | 1.00x faster                                                                  |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                                          | 111 ms: 1.14x faster                                                          |
| regex_effbot   | 1.65 ms                                                                         | 1.53 ms: 1.08x faster                                                         |
| regex_compile  | 101 ms                                                                          | 98.6 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                                           | 1.05x faster                                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_process    | 50.0 ms                                                                         | 47.2 ms: 1.06x faster                                                         |
| xml_etree_generate   | 67.8 ms                                                                         | 64.7 ms: 1.05x faster                                                         |
| xml_etree_parse      | 111 ms                                                                          | 107 ms: 1.04x faster                                                          |
| unpickle_pure_python | 171 us                                                                          | 167 us: 1.02x faster                                                          |
| tomli_loads          | 1.64 sec                                                                        | 1.61 sec: 1.02x faster                                                        |
| json_dumps           | 8.81 ms                                                                         | 8.72 ms: 1.01x faster                                                         |
| xml_etree_iterparse  | 67.2 ms                                                                         | 66.5 ms: 1.01x faster                                                         |
| pickle_pure_python   | 259 us                                                                          | 263 us: 1.01x slower                                                          |
| Geometric mean       | (ref)                                                                           | 1.02x faster                                                                  |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|------------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 26.9 ms                                                                         | 25.8 ms: 1.04x faster                                                         |
| python_startup_no_site | 20.3 ms                                                                         | 19.7 ms: 1.03x faster                                                         |
| Geometric mean         | (ref)                                                                           | 1.04x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|-----------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 7.79 ms                                                                         | 7.64 ms: 1.02x faster                                                         |
| genshi_text     | 20.5 ms                                                                         | 20.7 ms: 1.01x slower                                                         |
| genshi_xml      | 45.0 ms                                                                         | 45.3 ms: 1.01x slower                                                         |
| django_template | 31.8 ms                                                                         | 32.5 ms: 1.02x slower                                                         |
| Geometric mean  | (ref)                                                                           | 1.00x slower                                                                  |

All benchmarks:
===============

| Benchmark                 | bm-20250102-pythonperf1_win32-x86-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf1_win32-x86-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|---------------------------|:-------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna                 | 126 ms                                                                          | 111 ms: 1.14x faster                                                          |
| regex_effbot              | 1.65 ms                                                                         | 1.53 ms: 1.08x faster                                                         |
| xml_etree_process         | 50.0 ms                                                                         | 47.2 ms: 1.06x faster                                                         |
| telco                     | 6.73 ms                                                                         | 6.36 ms: 1.06x faster                                                         |
| pprint_safe_repr          | 647 ms                                                                          | 616 ms: 1.05x faster                                                          |
| xml_etree_generate        | 67.8 ms                                                                         | 64.7 ms: 1.05x faster                                                         |
| nqueens                   | 75.6 ms                                                                         | 72.4 ms: 1.04x faster                                                         |
| sympy_expand              | 375 ms                                                                          | 360 ms: 1.04x faster                                                          |
| python_startup            | 26.9 ms                                                                         | 25.8 ms: 1.04x faster                                                         |
| richards_super            | 42.3 ms                                                                         | 40.7 ms: 1.04x faster                                                         |
| xml_etree_parse           | 111 ms                                                                          | 107 ms: 1.04x faster                                                          |
| richards                  | 36.8 ms                                                                         | 35.5 ms: 1.04x faster                                                         |
| pprint_pformat            | 1.32 sec                                                                        | 1.27 sec: 1.04x faster                                                        |
| deepcopy_reduce           | 2.42 us                                                                         | 2.33 us: 1.04x faster                                                         |
| comprehensions            | 13.8 us                                                                         | 13.3 us: 1.03x faster                                                         |
| python_startup_no_site    | 20.3 ms                                                                         | 19.7 ms: 1.03x faster                                                         |
| sqlglot_normalize         | 217 ms                                                                          | 211 ms: 1.03x faster                                                          |
| sympy_str                 | 213 ms                                                                          | 207 ms: 1.03x faster                                                          |
| sqlglot_optimize          | 41.7 ms                                                                         | 40.4 ms: 1.03x faster                                                         |
| many_optionals            | 520 us                                                                          | 505 us: 1.03x faster                                                          |
| docutils                  | 1.80 sec                                                                        | 1.75 sec: 1.03x faster                                                        |
| html5lib                  | 43.5 ms                                                                         | 42.4 ms: 1.03x faster                                                         |
| sympy_integrate           | 15.3 ms                                                                         | 14.9 ms: 1.03x faster                                                         |
| mdp                       | 1.73 sec                                                                        | 1.69 sec: 1.03x faster                                                        |
| async_generators          | 302 ms                                                                          | 295 ms: 1.03x faster                                                          |
| meteor_contest            | 82.2 ms                                                                         | 80.3 ms: 1.02x faster                                                         |
| subparsers                | 20.5 ms                                                                         | 20.0 ms: 1.02x faster                                                         |
| sympy_sum                 | 106 ms                                                                          | 103 ms: 1.02x faster                                                          |
| regex_compile             | 101 ms                                                                          | 98.6 ms: 1.02x faster                                                         |
| unpickle_pure_python      | 171 us                                                                          | 167 us: 1.02x faster                                                          |
| tomli_loads               | 1.64 sec                                                                        | 1.61 sec: 1.02x faster                                                        |
| gc_traversal              | 1.81 ms                                                                         | 1.77 ms: 1.02x faster                                                         |
| sphinx                    | 727 ms                                                                          | 712 ms: 1.02x faster                                                          |
| mako                      | 7.79 ms                                                                         | 7.64 ms: 1.02x faster                                                         |
| deltablue                 | 2.59 ms                                                                         | 2.54 ms: 1.02x faster                                                         |
| k_core                    | 1.35 sec                                                                        | 1.32 sec: 1.02x faster                                                        |
| pylint                    | 216 ms                                                                          | 212 ms: 1.02x faster                                                          |
| deepcopy                  | 227 us                                                                          | 223 us: 1.02x faster                                                          |
| bpe_tokeniser             | 3.46 sec                                                                        | 3.40 sec: 1.02x faster                                                        |
| spectral_norm             | 71.3 ms                                                                         | 70.1 ms: 1.02x faster                                                         |
| hexiom                    | 5.00 ms                                                                         | 4.93 ms: 1.02x faster                                                         |
| async_tree_memoization_tg | 222 ms                                                                          | 218 ms: 1.01x faster                                                          |
| chaos                     | 54.0 ms                                                                         | 53.3 ms: 1.01x faster                                                         |
| coroutines                | 16.6 ms                                                                         | 16.3 ms: 1.01x faster                                                         |
| typing_runtime_protocols  | 141 us                                                                          | 139 us: 1.01x faster                                                          |
| 2to3                      | 243 ms                                                                          | 240 ms: 1.01x faster                                                          |
| async_tree_none_tg        | 177 ms                                                                          | 175 ms: 1.01x faster                                                          |
| async_tree_memoization    | 240 ms                                                                          | 237 ms: 1.01x faster                                                          |
| mypy2                     | 680 ms                                                                          | 672 ms: 1.01x faster                                                          |
| generators                | 24.6 ms                                                                         | 24.3 ms: 1.01x faster                                                         |
| pycparser                 | 812 ms                                                                          | 803 ms: 1.01x faster                                                          |
| json_dumps                | 8.81 ms                                                                         | 8.72 ms: 1.01x faster                                                         |
| xml_etree_iterparse       | 67.2 ms                                                                         | 66.5 ms: 1.01x faster                                                         |
| scimark_fft               | 216 ms                                                                          | 214 ms: 1.01x faster                                                          |
| go                        | 96.4 ms                                                                         | 95.7 ms: 1.01x faster                                                         |
| logging_simple            | 7.80 us                                                                         | 7.76 us: 1.01x faster                                                         |
| shortest_path             | 285 ms                                                                          | 283 ms: 1.00x faster                                                          |
| bench_mp_pool             | 87.2 ms                                                                         | 86.8 ms: 1.00x faster                                                         |
| pidigits                  | 197 ms                                                                          | 196 ms: 1.00x faster                                                          |
| connected_components      | 255 ms                                                                          | 254 ms: 1.00x faster                                                          |
| sqlglot_transpile         | 1.27 ms                                                                         | 1.27 ms: 1.00x faster                                                         |
| dulwich_log               | 49.4 ms                                                                         | 49.6 ms: 1.00x slower                                                         |
| scimark_lu                | 68.6 ms                                                                         | 68.9 ms: 1.00x slower                                                         |
| pathlib                   | 82.9 ms                                                                         | 83.5 ms: 1.01x slower                                                         |
| scimark_sor               | 101 ms                                                                          | 101 ms: 1.01x slower                                                          |
| genshi_text               | 20.5 ms                                                                         | 20.7 ms: 1.01x slower                                                         |
| async_tree_none           | 194 ms                                                                          | 196 ms: 1.01x slower                                                          |
| genshi_xml                | 45.0 ms                                                                         | 45.3 ms: 1.01x slower                                                         |
| pyflate                   | 336 ms                                                                          | 339 ms: 1.01x slower                                                          |
| logging_silent            | 70.7 ns                                                                         | 71.4 ns: 1.01x slower                                                         |
| float                     | 55.8 ms                                                                         | 56.4 ms: 1.01x slower                                                         |
| sqlglot_parse             | 1.02 ms                                                                         | 1.03 ms: 1.01x slower                                                         |
| pickle_pure_python        | 259 us                                                                          | 263 us: 1.01x slower                                                          |
| crypto_pyaes              | 60.9 ms                                                                         | 61.7 ms: 1.01x slower                                                         |
| json                      | 4.17 ms                                                                         | 4.23 ms: 1.01x slower                                                         |
| django_template           | 31.8 ms                                                                         | 32.5 ms: 1.02x slower                                                         |
| coverage                  | 51.6 ms                                                                         | 53.1 ms: 1.03x slower                                                         |
| fannkuch                  | 298 ms                                                                          | 308 ms: 1.03x slower                                                          |
| raytrace                  | 242 ms                                                                          | 255 ms: 1.06x slower                                                          |
| Geometric mean            | (ref)                                                                           | 1.01x faster                                                                  |

Benchmark hidden because not significant (16): nbody, scimark_sparse_mat_mult, async_tree_io, json_loads, create_gc_cycles, bench_thread_pool, scimark_monte_carlo, async_tree_io_tg, deepcopy_memo, logging_format, sqlite_synth, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, thrift, regex_v8

- Geometric mean (including insignificant results): 1.014x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown