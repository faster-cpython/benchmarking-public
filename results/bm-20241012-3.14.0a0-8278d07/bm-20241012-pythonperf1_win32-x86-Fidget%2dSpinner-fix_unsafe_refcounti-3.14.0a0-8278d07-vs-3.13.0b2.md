# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: windows-x86
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 249 ms: 1.07x slower                                                                     |
| docutils       | 1.81 sec                                                            | 1.84 sec: 1.02x slower                                                                   |
| html5lib       | 45.4 ms                                                             | 44.7 ms: 1.02x faster                                                                    |
| tornado_http   | 94.3 ms                                                             | 103 ms: 1.10x slower                                                                     |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 218 ms: 1.05x faster                                                                     |
| async_tree_io_tg           | 529 ms                                                              | 520 ms: 1.02x faster                                                                     |
| async_tree_memoization     | 275 ms                                                              | 271 ms: 1.02x faster                                                                     |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 454 ms: 1.02x slower                                                                     |
| Geometric mean             | (ref)                                                               | 1.01x faster                                                                             |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 201 ms: 1.01x slower                                                                     |
| nbody          | 76.9 ms                                                             | 89.4 ms: 1.16x slower                                                                    |
| float          | 52.4 ms                                                             | 61.2 ms: 1.17x slower                                                                    |
| Geometric mean | (ref)                                                               | 1.11x slower                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.79 ms: 1.05x faster                                                                    |
| regex_dna      | 118 ms                                                              | 113 ms: 1.05x faster                                                                     |
| regex_v8       | 15.7 ms                                                             | 15.3 ms: 1.03x faster                                                                    |
| regex_compile  | 99.9 ms                                                             | 106 ms: 1.06x slower                                                                     |
| Geometric mean | (ref)                                                               | 1.02x faster                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.50 us: 1.02x faster                                                                    |
| json_loads           | 20.5 us                                                             | 20.7 us: 1.01x slower                                                                    |
| unpickle_list        | 2.93 us                                                             | 2.99 us: 1.02x slower                                                                    |
| pickle_dict          | 20.8 us                                                             | 21.7 us: 1.05x slower                                                                    |
| pickle               | 8.07 us                                                             | 8.48 us: 1.05x slower                                                                    |
| xml_etree_iterparse  | 64.2 ms                                                             | 68.1 ms: 1.06x slower                                                                    |
| unpickle             | 9.79 us                                                             | 10.4 us: 1.06x slower                                                                    |
| tomli_loads          | 1.65 sec                                                            | 1.77 sec: 1.07x slower                                                                   |
| xml_etree_parse      | 104 ms                                                              | 113 ms: 1.08x slower                                                                     |
| xml_etree_generate   | 59.6 ms                                                             | 66.6 ms: 1.12x slower                                                                    |
| xml_etree_process    | 42.1 ms                                                             | 47.4 ms: 1.13x slower                                                                    |
| unpickle_pure_python | 147 us                                                              | 180 us: 1.22x slower                                                                     |
| pickle_pure_python   | 213 us                                                              | 272 us: 1.28x slower                                                                     |
| json_dumps           | 6.84 ms                                                             | 9.02 ms: 1.32x slower                                                                    |
| Geometric mean       | (ref)                                                               | 1.10x slower                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.3 ms: 1.09x slower                                                                    |
| python_startup_no_site | 18.2 ms                                                             | 20.0 ms: 1.10x slower                                                                    |
| Geometric mean         | (ref)                                                               | 1.10x slower                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| genshi_text     | 20.1 ms                                                             | 20.6 ms: 1.03x slower                                                                    |
| genshi_xml      | 44.3 ms                                                             | 45.6 ms: 1.03x slower                                                                    |
| django_template | 30.1 ms                                                             | 32.8 ms: 1.09x slower                                                                    |
| mako            | 6.94 ms                                                             | 7.86 ms: 1.13x slower                                                                    |
| Geometric mean  | (ref)                                                               | 1.07x slower                                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 739 us: 13.16x faster                                                                    |
| coverage                   | 307 ms                                                              | 52.6 ms: 5.84x faster                                                                    |
| deepcopy                   | 280 us                                                              | 241 us: 1.16x faster                                                                     |
| deepcopy_memo              | 23.5 us                                                             | 22.1 us: 1.06x faster                                                                    |
| regex_effbot               | 1.88 ms                                                             | 1.79 ms: 1.05x faster                                                                    |
| regex_dna                  | 118 ms                                                              | 113 ms: 1.05x faster                                                                     |
| async_tree_none            | 228 ms                                                              | 218 ms: 1.05x faster                                                                     |
| regex_v8                   | 15.7 ms                                                             | 15.3 ms: 1.03x faster                                                                    |
| deepcopy_reduce            | 2.59 us                                                             | 2.53 us: 1.02x faster                                                                    |
| pickle_list                | 3.57 us                                                             | 3.50 us: 1.02x faster                                                                    |
| async_tree_io_tg           | 529 ms                                                              | 520 ms: 1.02x faster                                                                     |
| html5lib                   | 45.4 ms                                                             | 44.7 ms: 1.02x faster                                                                    |
| async_tree_memoization     | 275 ms                                                              | 271 ms: 1.02x faster                                                                     |
| sqlite_synth               | 1.96 us                                                             | 1.94 us: 1.01x faster                                                                    |
| json_loads                 | 20.5 us                                                             | 20.7 us: 1.01x slower                                                                    |
| pidigits                   | 199 ms                                                              | 201 ms: 1.01x slower                                                                     |
| sympy_sum                  | 105 ms                                                              | 106 ms: 1.01x slower                                                                     |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 454 ms: 1.02x slower                                                                     |
| docutils                   | 1.81 sec                                                            | 1.84 sec: 1.02x slower                                                                   |
| unpickle_list              | 2.93 us                                                             | 2.99 us: 1.02x slower                                                                    |
| go                         | 101 ms                                                              | 103 ms: 1.02x slower                                                                     |
| sympy_expand               | 375 ms                                                              | 384 ms: 1.02x slower                                                                     |
| sympy_str                  | 211 ms                                                              | 216 ms: 1.02x slower                                                                     |
| create_gc_cycles           | 756 us                                                              | 774 us: 1.02x slower                                                                     |
| genshi_text                | 20.1 ms                                                             | 20.6 ms: 1.03x slower                                                                    |
| genshi_xml                 | 44.3 ms                                                             | 45.6 ms: 1.03x slower                                                                    |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.5 sec: 1.04x slower                                                                   |
| logging_simple             | 7.47 us                                                             | 7.77 us: 1.04x slower                                                                    |
| pickle_dict                | 20.8 us                                                             | 21.7 us: 1.05x slower                                                                    |
| pathlib                    | 83.9 ms                                                             | 87.8 ms: 1.05x slower                                                                    |
| json                       | 4.10 ms                                                             | 4.30 ms: 1.05x slower                                                                    |
| pickle                     | 8.07 us                                                             | 8.48 us: 1.05x slower                                                                    |
| sympy_integrate            | 14.6 ms                                                             | 15.4 ms: 1.05x slower                                                                    |
| pprint_pformat             | 1.24 sec                                                            | 1.31 sec: 1.05x slower                                                                   |
| logging_format             | 8.13 us                                                             | 8.58 us: 1.05x slower                                                                    |
| crypto_pyaes               | 55.8 ms                                                             | 59.2 ms: 1.06x slower                                                                    |
| bench_mp_pool              | 69.4 ms                                                             | 73.6 ms: 1.06x slower                                                                    |
| xml_etree_iterparse        | 64.2 ms                                                             | 68.1 ms: 1.06x slower                                                                    |
| unpickle                   | 9.79 us                                                             | 10.4 us: 1.06x slower                                                                    |
| regex_compile              | 99.9 ms                                                             | 106 ms: 1.06x slower                                                                     |
| pprint_safe_repr           | 607 ms                                                              | 647 ms: 1.07x slower                                                                     |
| 2to3                       | 233 ms                                                              | 249 ms: 1.07x slower                                                                     |
| typing_runtime_protocols   | 136 us                                                              | 145 us: 1.07x slower                                                                     |
| nqueens                    | 68.7 ms                                                             | 73.5 ms: 1.07x slower                                                                    |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.08 ms: 1.07x slower                                                                    |
| tomli_loads                | 1.65 sec                                                            | 1.77 sec: 1.07x slower                                                                   |
| pycparser                  | 777 ms                                                              | 835 ms: 1.07x slower                                                                     |
| mdp                        | 1.60 sec                                                            | 1.72 sec: 1.07x slower                                                                   |
| pylint                     | 217 ms                                                              | 234 ms: 1.08x slower                                                                     |
| meteor_contest             | 74.1 ms                                                             | 79.8 ms: 1.08x slower                                                                    |
| xml_etree_parse            | 104 ms                                                              | 113 ms: 1.08x slower                                                                     |
| sqlglot_normalize          | 206 ms                                                              | 224 ms: 1.09x slower                                                                     |
| django_template            | 30.1 ms                                                             | 32.8 ms: 1.09x slower                                                                    |
| python_startup             | 22.2 ms                                                             | 24.3 ms: 1.09x slower                                                                    |
| sqlglot_optimize           | 39.7 ms                                                             | 43.5 ms: 1.09x slower                                                                    |
| tornado_http               | 94.3 ms                                                             | 103 ms: 1.10x slower                                                                     |
| python_startup_no_site     | 18.2 ms                                                             | 20.0 ms: 1.10x slower                                                                    |
| asyncio_tcp                | 662 ms                                                              | 737 ms: 1.11x slower                                                                     |
| spectral_norm              | 68.0 ms                                                             | 75.9 ms: 1.12x slower                                                                    |
| generators                 | 21.2 ms                                                             | 23.6 ms: 1.12x slower                                                                    |
| xml_etree_generate         | 59.6 ms                                                             | 66.6 ms: 1.12x slower                                                                    |
| sqlglot_transpile          | 1.19 ms                                                             | 1.33 ms: 1.12x slower                                                                    |
| comprehensions             | 11.9 us                                                             | 13.3 us: 1.12x slower                                                                    |
| xml_etree_process          | 42.1 ms                                                             | 47.4 ms: 1.13x slower                                                                    |
| coroutines                 | 15.5 ms                                                             | 17.5 ms: 1.13x slower                                                                    |
| mako                       | 6.94 ms                                                             | 7.86 ms: 1.13x slower                                                                    |
| sqlglot_parse              | 964 us                                                              | 1.09 ms: 1.13x slower                                                                    |
| telco                      | 6.03 ms                                                             | 6.86 ms: 1.14x slower                                                                    |
| async_generators           | 266 ms                                                              | 303 ms: 1.14x slower                                                                     |
| scimark_lu                 | 59.4 ms                                                             | 67.8 ms: 1.14x slower                                                                    |
| scimark_fft                | 198 ms                                                              | 229 ms: 1.16x slower                                                                     |
| nbody                      | 76.9 ms                                                             | 89.4 ms: 1.16x slower                                                                    |
| chaos                      | 48.0 ms                                                             | 55.9 ms: 1.17x slower                                                                    |
| hexiom                     | 4.23 ms                                                             | 4.94 ms: 1.17x slower                                                                    |
| float                      | 52.4 ms                                                             | 61.2 ms: 1.17x slower                                                                    |
| pyflate                    | 308 ms                                                              | 362 ms: 1.17x slower                                                                     |
| fannkuch                   | 270 ms                                                              | 324 ms: 1.20x slower                                                                     |
| deltablue                  | 2.23 ms                                                             | 2.72 ms: 1.22x slower                                                                    |
| unpickle_pure_python       | 147 us                                                              | 180 us: 1.22x slower                                                                     |
| scimark_monte_carlo        | 45.2 ms                                                             | 56.7 ms: 1.25x slower                                                                    |
| scimark_sor                | 81.0 ms                                                             | 102 ms: 1.26x slower                                                                     |
| logging_silent             | 57.9 ns                                                             | 73.2 ns: 1.27x slower                                                                    |
| pickle_pure_python         | 213 us                                                              | 272 us: 1.28x slower                                                                     |
| richards_super             | 35.5 ms                                                             | 46.0 ms: 1.30x slower                                                                    |
| json_dumps                 | 6.84 ms                                                             | 9.02 ms: 1.32x slower                                                                    |
| raytrace                   | 189 ms                                                              | 249 ms: 1.32x slower                                                                     |
| richards                   | 31.2 ms                                                             | 41.3 ms: 1.32x slower                                                                    |
| Geometric mean             | (ref)                                                               | 1.03x slower                                                                             |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, gc_traversal, bench_thread_pool, async_tree_io
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (2) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown