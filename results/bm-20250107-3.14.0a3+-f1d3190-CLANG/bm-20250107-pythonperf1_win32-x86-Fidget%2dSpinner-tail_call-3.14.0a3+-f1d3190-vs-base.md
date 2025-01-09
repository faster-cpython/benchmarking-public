# Results vs. base

- fork: Fidget-Spinner
- ref: tail_call
- machine: windows-x86
- commit hash: f1d3190
- commit date: 2025-01-07
- overall geometric mean: 1.144x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 240 ms                                                                          | 277 ms: 1.15x slower                                                           |
| docutils       | 1.75 sec                                                                        | 1.95 sec: 1.11x slower                                                         |
| html5lib       | 41.2 ms                                                                         | 48.9 ms: 1.19x slower                                                          |
| sphinx         | 713 ms                                                                          | 795 ms: 1.12x slower                                                           |
| Geometric mean | (ref)                                                                           | 1.14x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_websockets         | 329 ms                                                                          | 338 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 432 ms                                                                          | 457 ms: 1.06x slower                                                           |
| async_tree_cpu_io_mixed    | 443 ms                                                                          | 474 ms: 1.07x slower                                                           |
| async_tree_memoization_tg  | 210 ms                                                                          | 246 ms: 1.17x slower                                                           |
| async_generators           | 261 ms                                                                          | 312 ms: 1.19x slower                                                           |
| async_tree_none_tg         | 158 ms                                                                          | 194 ms: 1.23x slower                                                           |
| async_tree_none            | 173 ms                                                                          | 213 ms: 1.23x slower                                                           |
| async_tree_io              | 374 ms                                                                          | 460 ms: 1.23x slower                                                           |
| async_tree_memoization     | 215 ms                                                                          | 266 ms: 1.24x slower                                                           |
| async_tree_io_tg           | 366 ms                                                                          | 454 ms: 1.24x slower                                                           |
| coroutines                 | 13.3 ms                                                                         | 17.7 ms: 1.33x slower                                                          |
| Geometric mean             | (ref)                                                                           | 1.18x slower                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 215 ms                                                                          | 215 ms: 1.00x slower                                                           |
| float          | 51.6 ms                                                                         | 58.8 ms: 1.14x slower                                                          |
| nbody          | 75.5 ms                                                                         | 95.9 ms: 1.27x slower                                                          |
| Geometric mean | (ref)                                                                           | 1.13x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.93 ms                                                                         | 1.94 ms: 1.01x slower                                                          |
| regex_v8       | 17.3 ms                                                                         | 17.7 ms: 1.02x slower                                                          |
| regex_compile  | 92.3 ms                                                                         | 112 ms: 1.21x slower                                                           |
| Geometric mean | (ref)                                                                           | 1.06x slower                                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 72.2 ms                                                                         | 72.9 ms: 1.01x slower                                                          |
| xml_etree_parse      | 111 ms                                                                          | 112 ms: 1.01x slower                                                           |
| json_loads           | 20.4 us                                                                         | 20.8 us: 1.02x slower                                                          |
| xml_etree_generate   | 69.1 ms                                                                         | 75.7 ms: 1.10x slower                                                          |
| json_dumps           | 7.73 ms                                                                         | 8.57 ms: 1.11x slower                                                          |
| xml_etree_process    | 48.0 ms                                                                         | 55.4 ms: 1.15x slower                                                          |
| unpickle_pure_python | 158 us                                                                          | 195 us: 1.24x slower                                                           |
| tomli_loads          | 1.43 sec                                                                        | 1.79 sec: 1.25x slower                                                         |
| pickle_pure_python   | 228 us                                                                          | 301 us: 1.32x slower                                                           |
| Geometric mean       | (ref)                                                                           | 1.13x slower                                                                   |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-----------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.97 ms                                                                         | 8.72 ms: 1.09x slower                                                          |
| django_template | 28.1 ms                                                                         | 36.1 ms: 1.29x slower                                                          |
| genshi_xml      | 35.2 ms                                                                         | 48.5 ms: 1.38x slower                                                          |
| genshi_text     | 16.3 ms                                                                         | 22.8 ms: 1.40x slower                                                          |
| Geometric mean  | (ref)                                                                           | 1.28x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20250105-pythonperf1_win32-x86-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1_win32-x86-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:-------------------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits                   | 215 ms                                                                          | 215 ms: 1.00x slower                                                           |
| regex_effbot               | 1.93 ms                                                                         | 1.94 ms: 1.01x slower                                                          |
| xml_etree_iterparse        | 72.2 ms                                                                         | 72.9 ms: 1.01x slower                                                          |
| xml_etree_parse            | 111 ms                                                                          | 112 ms: 1.01x slower                                                           |
| gc_traversal               | 2.35 ms                                                                         | 2.38 ms: 1.01x slower                                                          |
| scimark_lu                 | 74.6 ms                                                                         | 75.9 ms: 1.02x slower                                                          |
| json_loads                 | 20.4 us                                                                         | 20.8 us: 1.02x slower                                                          |
| regex_v8                   | 17.3 ms                                                                         | 17.7 ms: 1.02x slower                                                          |
| bench_mp_pool              | 97.0 ms                                                                         | 99.3 ms: 1.02x slower                                                          |
| asyncio_websockets         | 329 ms                                                                          | 338 ms: 1.03x slower                                                           |
| json                       | 4.10 ms                                                                         | 4.27 ms: 1.04x slower                                                          |
| async_tree_cpu_io_mixed_tg | 432 ms                                                                          | 457 ms: 1.06x slower                                                           |
| async_tree_cpu_io_mixed    | 443 ms                                                                          | 474 ms: 1.07x slower                                                           |
| coverage                   | 54.3 ms                                                                         | 58.1 ms: 1.07x slower                                                          |
| dulwich_log                | 46.8 ms                                                                         | 50.5 ms: 1.08x slower                                                          |
| bench_thread_pool          | 994 us                                                                          | 1.08 ms: 1.09x slower                                                          |
| bpe_tokeniser              | 3.35 sec                                                                        | 3.65 sec: 1.09x slower                                                         |
| fannkuch                   | 281 ms                                                                          | 307 ms: 1.09x slower                                                           |
| mako                       | 7.97 ms                                                                         | 8.72 ms: 1.09x slower                                                          |
| xml_etree_generate         | 69.1 ms                                                                         | 75.7 ms: 1.10x slower                                                          |
| k_core                     | 1.31 sec                                                                        | 1.44 sec: 1.10x slower                                                         |
| crypto_pyaes               | 61.1 ms                                                                         | 67.6 ms: 1.11x slower                                                          |
| json_dumps                 | 7.73 ms                                                                         | 8.57 ms: 1.11x slower                                                          |
| docutils                   | 1.75 sec                                                                        | 1.95 sec: 1.11x slower                                                         |
| sphinx                     | 713 ms                                                                          | 795 ms: 1.12x slower                                                           |
| thrift                     | 653 us                                                                          | 728 us: 1.12x slower                                                           |
| scimark_sparse_mat_mult    | 2.72 ms                                                                         | 3.04 ms: 1.12x slower                                                          |
| mdp                        | 1.77 sec                                                                        | 1.99 sec: 1.12x slower                                                         |
| telco                      | 5.67 ms                                                                         | 6.39 ms: 1.13x slower                                                          |
| meteor_contest             | 77.1 ms                                                                         | 87.0 ms: 1.13x slower                                                          |
| shortest_path              | 277 ms                                                                          | 314 ms: 1.13x slower                                                           |
| sympy_sum                  | 98.4 ms                                                                         | 112 ms: 1.13x slower                                                           |
| subparsers                 | 18.5 ms                                                                         | 21.1 ms: 1.14x slower                                                          |
| many_optionals             | 489 us                                                                          | 556 us: 1.14x slower                                                           |
| float                      | 51.6 ms                                                                         | 58.8 ms: 1.14x slower                                                          |
| connected_components       | 251 ms                                                                          | 288 ms: 1.15x slower                                                           |
| pylint                     | 207 ms                                                                          | 237 ms: 1.15x slower                                                           |
| scimark_fft                | 206 ms                                                                          | 237 ms: 1.15x slower                                                           |
| xml_etree_process          | 48.0 ms                                                                         | 55.4 ms: 1.15x slower                                                          |
| scimark_monte_carlo        | 46.4 ms                                                                         | 53.5 ms: 1.15x slower                                                          |
| 2to3                       | 240 ms                                                                          | 277 ms: 1.15x slower                                                           |
| sympy_str                  | 192 ms                                                                          | 222 ms: 1.16x slower                                                           |
| sympy_expand               | 331 ms                                                                          | 383 ms: 1.16x slower                                                           |
| sympy_integrate            | 14.3 ms                                                                         | 16.6 ms: 1.16x slower                                                          |
| async_tree_memoization_tg  | 210 ms                                                                          | 246 ms: 1.17x slower                                                           |
| pyflate                    | 315 ms                                                                          | 371 ms: 1.18x slower                                                           |
| deepcopy_memo              | 20.3 us                                                                         | 24.0 us: 1.18x slower                                                          |
| spectral_norm              | 63.8 ms                                                                         | 75.6 ms: 1.18x slower                                                          |
| html5lib                   | 41.2 ms                                                                         | 48.9 ms: 1.19x slower                                                          |
| async_generators           | 261 ms                                                                          | 312 ms: 1.19x slower                                                           |
| logging_simple             | 7.06 us                                                                         | 8.54 us: 1.21x slower                                                          |
| regex_compile              | 92.3 ms                                                                         | 112 ms: 1.21x slower                                                           |
| logging_format             | 7.52 us                                                                         | 9.16 us: 1.22x slower                                                          |
| scimark_sor                | 81.8 ms                                                                         | 99.7 ms: 1.22x slower                                                          |
| async_tree_none_tg         | 158 ms                                                                          | 194 ms: 1.23x slower                                                           |
| logging_silent             | 67.1 ns                                                                         | 82.3 ns: 1.23x slower                                                          |
| pycparser                  | 752 ms                                                                          | 925 ms: 1.23x slower                                                           |
| async_tree_none            | 173 ms                                                                          | 213 ms: 1.23x slower                                                           |
| async_tree_io              | 374 ms                                                                          | 460 ms: 1.23x slower                                                           |
| sqlglot_optimize           | 38.8 ms                                                                         | 48.0 ms: 1.24x slower                                                          |
| async_tree_memoization     | 215 ms                                                                          | 266 ms: 1.24x slower                                                           |
| unpickle_pure_python       | 158 us                                                                          | 195 us: 1.24x slower                                                           |
| async_tree_io_tg           | 366 ms                                                                          | 454 ms: 1.24x slower                                                           |
| tomli_loads                | 1.43 sec                                                                        | 1.79 sec: 1.25x slower                                                         |
| typing_runtime_protocols   | 125 us                                                                          | 157 us: 1.26x slower                                                           |
| sqlglot_normalize          | 199 ms                                                                          | 250 ms: 1.26x slower                                                           |
| pprint_safe_repr           | 540 ms                                                                          | 683 ms: 1.27x slower                                                           |
| pprint_pformat             | 1.11 sec                                                                        | 1.41 sec: 1.27x slower                                                         |
| nbody                      | 75.5 ms                                                                         | 95.9 ms: 1.27x slower                                                          |
| sqlglot_transpile          | 1.13 ms                                                                         | 1.44 ms: 1.28x slower                                                          |
| comprehensions             | 13.0 us                                                                         | 16.7 us: 1.28x slower                                                          |
| nqueens                    | 67.5 ms                                                                         | 86.8 ms: 1.29x slower                                                          |
| django_template            | 28.1 ms                                                                         | 36.1 ms: 1.29x slower                                                          |
| chaos                      | 46.0 ms                                                                         | 59.5 ms: 1.30x slower                                                          |
| sqlglot_parse              | 891 us                                                                          | 1.16 ms: 1.30x slower                                                          |
| deepcopy                   | 189 us                                                                          | 247 us: 1.31x slower                                                           |
| deepcopy_reduce            | 1.97 us                                                                         | 2.59 us: 1.31x slower                                                          |
| hexiom                     | 4.49 ms                                                                         | 5.91 ms: 1.32x slower                                                          |
| pickle_pure_python         | 228 us                                                                          | 301 us: 1.32x slower                                                           |
| raytrace                   | 193 ms                                                                          | 255 ms: 1.32x slower                                                           |
| coroutines                 | 13.3 ms                                                                         | 17.7 ms: 1.33x slower                                                          |
| go                         | 83.5 ms                                                                         | 113 ms: 1.35x slower                                                           |
| richards_super             | 36.4 ms                                                                         | 49.3 ms: 1.35x slower                                                          |
| richards                   | 32.2 ms                                                                         | 43.7 ms: 1.36x slower                                                          |
| genshi_xml                 | 35.2 ms                                                                         | 48.5 ms: 1.38x slower                                                          |
| deltablue                  | 2.08 ms                                                                         | 2.90 ms: 1.40x slower                                                          |
| genshi_text                | 16.3 ms                                                                         | 22.8 ms: 1.40x slower                                                          |
| generators                 | 17.6 ms                                                                         | 30.3 ms: 1.72x slower                                                          |
| Geometric mean             | (ref)                                                                           | 1.17x slower                                                                   |

Benchmark hidden because not significant (6): pathlib, sqlite_synth, regex_dna, create_gc_cycles, python_startup, python_startup_no_site

- Geometric mean (including insignificant results): 1.144x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: unknown