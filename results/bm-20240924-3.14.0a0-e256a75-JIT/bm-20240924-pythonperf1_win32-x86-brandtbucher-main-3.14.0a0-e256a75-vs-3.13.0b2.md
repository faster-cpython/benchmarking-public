# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: main
- machine: windows-x86
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.05x faster
- HPT reliability: 85.53%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 258 ms: 1.11x slower                                                 |
| docutils       | 1.81 sec                                                            | 2.01 sec: 1.11x slower                                               |
| html5lib       | 45.4 ms                                                             | 46.6 ms: 1.03x slower                                                |
| tornado_http   | 94.3 ms                                                             | 99.4 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                               | 1.07x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 216 ms: 1.06x faster                                                 |
| async_tree_io_tg           | 529 ms                                                              | 517 ms: 1.02x faster                                                 |
| async_tree_memoization     | 275 ms                                                              | 272 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 470 ms: 1.05x slower                                                 |
| Geometric mean             | (ref)                                                               | 1.01x faster                                                         |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 49.5 ms: 1.55x faster                                                |
| float          | 52.4 ms                                                             | 44.1 ms: 1.19x faster                                                |
| pidigits       | 199 ms                                                              | 198 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                               | 1.23x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 121 ms: 1.03x slower                                                 |
| regex_compile  | 99.9 ms                                                             | 103 ms: 1.03x slower                                                 |
| regex_effbot   | 1.88 ms                                                             | 1.95 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                               | 1.02x slower                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate   | 59.6 ms                                                             | 53.6 ms: 1.11x faster                                                |
| unpickle_list        | 2.93 us                                                             | 2.70 us: 1.08x faster                                                |
| pickle_list          | 3.57 us                                                             | 3.32 us: 1.07x faster                                                |
| tomli_loads          | 1.65 sec                                                            | 1.54 sec: 1.07x faster                                               |
| xml_etree_process    | 42.1 ms                                                             | 39.6 ms: 1.06x faster                                                |
| pickle_dict          | 20.8 us                                                             | 19.7 us: 1.05x faster                                                |
| xml_etree_iterparse  | 64.2 ms                                                             | 61.9 ms: 1.04x faster                                                |
| pickle               | 8.07 us                                                             | 8.12 us: 1.01x slower                                                |
| json_loads           | 20.5 us                                                             | 20.9 us: 1.02x slower                                                |
| json_dumps           | 6.84 ms                                                             | 7.06 ms: 1.03x slower                                                |
| unpickle             | 9.79 us                                                             | 10.4 us: 1.06x slower                                                |
| unpickle_pure_python | 147 us                                                              | 162 us: 1.10x slower                                                 |
| pickle_pure_python   | 213 us                                                              | 236 us: 1.11x slower                                                 |
| Geometric mean       | (ref)                                                               | 1.01x faster                                                         |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.3 ms: 1.10x slower                                                |
| python_startup_no_site | 18.2 ms                                                             | 20.1 ms: 1.11x slower                                                |
| Geometric mean         | (ref)                                                               | 1.10x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.52 ms: 1.26x faster                                                |
| django_template | 30.1 ms                                                             | 33.4 ms: 1.11x slower                                                |
| genshi_text     | 20.1 ms                                                             | 23.6 ms: 1.18x slower                                                |
| genshi_xml      | 44.3 ms                                                             | 55.9 ms: 1.26x slower                                                |
| Geometric mean  | (ref)                                                               | 1.07x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:-------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 762 us: 12.76x faster                                                |
| coverage                   | 307 ms                                                              | 51.6 ms: 5.96x faster                                                |
| sqlglot_normalize          | 206 ms                                                              | 102 ms: 2.02x faster                                                 |
| deepcopy_memo              | 23.5 us                                                             | 15.1 us: 1.56x faster                                                |
| nbody                      | 76.9 ms                                                             | 49.5 ms: 1.55x faster                                                |
| spectral_norm              | 68.0 ms                                                             | 46.1 ms: 1.47x faster                                                |
| mako                       | 6.94 ms                                                             | 5.52 ms: 1.26x faster                                                |
| scimark_sor                | 81.0 ms                                                             | 67.4 ms: 1.20x faster                                                |
| float                      | 52.4 ms                                                             | 44.1 ms: 1.19x faster                                                |
| deepcopy                   | 280 us                                                              | 238 us: 1.17x faster                                                 |
| crypto_pyaes               | 55.8 ms                                                             | 48.6 ms: 1.15x faster                                                |
| scimark_fft                | 198 ms                                                              | 173 ms: 1.15x faster                                                 |
| fannkuch                   | 270 ms                                                              | 243 ms: 1.11x faster                                                 |
| xml_etree_generate         | 59.6 ms                                                             | 53.6 ms: 1.11x faster                                                |
| pyflate                    | 308 ms                                                              | 279 ms: 1.11x faster                                                 |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.62 ms: 1.10x faster                                                |
| unpickle_list              | 2.93 us                                                             | 2.70 us: 1.08x faster                                                |
| deltablue                  | 2.23 ms                                                             | 2.07 ms: 1.08x faster                                                |
| pickle_list                | 3.57 us                                                             | 3.32 us: 1.07x faster                                                |
| tomli_loads                | 1.65 sec                                                            | 1.54 sec: 1.07x faster                                               |
| asyncio_tcp                | 662 ms                                                              | 620 ms: 1.07x faster                                                 |
| telco                      | 6.03 ms                                                             | 5.68 ms: 1.06x faster                                                |
| xml_etree_process          | 42.1 ms                                                             | 39.6 ms: 1.06x faster                                                |
| async_tree_none            | 228 ms                                                              | 216 ms: 1.06x faster                                                 |
| pickle_dict                | 20.8 us                                                             | 19.7 us: 1.05x faster                                                |
| sqlite_synth               | 1.96 us                                                             | 1.89 us: 1.04x faster                                                |
| xml_etree_iterparse        | 64.2 ms                                                             | 61.9 ms: 1.04x faster                                                |
| deepcopy_reduce            | 2.59 us                                                             | 2.51 us: 1.03x faster                                                |
| async_tree_io_tg           | 529 ms                                                              | 517 ms: 1.02x faster                                                 |
| pprint_safe_repr           | 607 ms                                                              | 595 ms: 1.02x faster                                                 |
| create_gc_cycles           | 756 us                                                              | 742 us: 1.02x faster                                                 |
| go                         | 101 ms                                                              | 99.3 ms: 1.01x faster                                                |
| async_tree_memoization     | 275 ms                                                              | 272 ms: 1.01x faster                                                 |
| json                       | 4.10 ms                                                             | 4.06 ms: 1.01x faster                                                |
| pidigits                   | 199 ms                                                              | 198 ms: 1.00x faster                                                 |
| scimark_lu                 | 59.4 ms                                                             | 59.7 ms: 1.01x slower                                                |
| pickle                     | 8.07 us                                                             | 8.12 us: 1.01x slower                                                |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.0 sec: 1.01x slower                                               |
| logging_silent             | 57.9 ns                                                             | 58.5 ns: 1.01x slower                                                |
| richards_super             | 35.5 ms                                                             | 35.9 ms: 1.01x slower                                                |
| pprint_pformat             | 1.24 sec                                                            | 1.26 sec: 1.02x slower                                               |
| json_loads                 | 20.5 us                                                             | 20.9 us: 1.02x slower                                                |
| html5lib                   | 45.4 ms                                                             | 46.6 ms: 1.03x slower                                                |
| regex_dna                  | 118 ms                                                              | 121 ms: 1.03x slower                                                 |
| regex_compile              | 99.9 ms                                                             | 103 ms: 1.03x slower                                                 |
| json_dumps                 | 6.84 ms                                                             | 7.06 ms: 1.03x slower                                                |
| regex_effbot               | 1.88 ms                                                             | 1.95 ms: 1.03x slower                                                |
| mdp                        | 1.60 sec                                                            | 1.66 sec: 1.04x slower                                               |
| logging_simple             | 7.47 us                                                             | 7.80 us: 1.04x slower                                                |
| logging_format             | 8.13 us                                                             | 8.51 us: 1.05x slower                                                |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 470 ms: 1.05x slower                                                 |
| richards                   | 31.2 ms                                                             | 32.9 ms: 1.05x slower                                                |
| pycparser                  | 777 ms                                                              | 819 ms: 1.05x slower                                                 |
| tornado_http               | 94.3 ms                                                             | 99.4 ms: 1.05x slower                                                |
| sympy_str                  | 211 ms                                                              | 223 ms: 1.06x slower                                                 |
| unpickle                   | 9.79 us                                                             | 10.4 us: 1.06x slower                                                |
| sympy_expand               | 375 ms                                                              | 399 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 136 us                                                              | 144 us: 1.07x slower                                                 |
| sympy_sum                  | 105 ms                                                              | 114 ms: 1.08x slower                                                 |
| bench_mp_pool              | 69.4 ms                                                             | 75.9 ms: 1.09x slower                                                |
| sqlglot_parse              | 964 us                                                              | 1.06 ms: 1.10x slower                                                |
| python_startup             | 22.2 ms                                                             | 24.3 ms: 1.10x slower                                                |
| unpickle_pure_python       | 147 us                                                              | 162 us: 1.10x slower                                                 |
| pickle_pure_python         | 213 us                                                              | 236 us: 1.11x slower                                                 |
| python_startup_no_site     | 18.2 ms                                                             | 20.1 ms: 1.11x slower                                                |
| 2to3                       | 233 ms                                                              | 258 ms: 1.11x slower                                                 |
| docutils                   | 1.81 sec                                                            | 2.01 sec: 1.11x slower                                               |
| django_template            | 30.1 ms                                                             | 33.4 ms: 1.11x slower                                                |
| generators                 | 21.2 ms                                                             | 23.7 ms: 1.12x slower                                                |
| scimark_monte_carlo        | 45.2 ms                                                             | 50.6 ms: 1.12x slower                                                |
| sqlglot_transpile          | 1.19 ms                                                             | 1.35 ms: 1.14x slower                                                |
| nqueens                    | 68.7 ms                                                             | 78.2 ms: 1.14x slower                                                |
| chaos                      | 48.0 ms                                                             | 55.1 ms: 1.15x slower                                                |
| sympy_integrate            | 14.6 ms                                                             | 16.8 ms: 1.15x slower                                                |
| hexiom                     | 4.23 ms                                                             | 4.91 ms: 1.16x slower                                                |
| genshi_text                | 20.1 ms                                                             | 23.6 ms: 1.18x slower                                                |
| sqlglot_optimize           | 39.7 ms                                                             | 47.7 ms: 1.20x slower                                                |
| async_generators           | 266 ms                                                              | 327 ms: 1.23x slower                                                 |
| pylint                     | 217 ms                                                              | 268 ms: 1.24x slower                                                 |
| coroutines                 | 15.5 ms                                                             | 19.2 ms: 1.24x slower                                                |
| genshi_xml                 | 44.3 ms                                                             | 55.9 ms: 1.26x slower                                                |
| raytrace                   | 189 ms                                                              | 248 ms: 1.32x slower                                                 |
| Geometric mean             | (ref)                                                               | 1.05x faster                                                         |

Benchmark hidden because not significant (11): async_tree_none_tg, async_tree_memoization_tg, pathlib, xml_etree_parse, comprehensions, meteor_contest, gc_traversal, regex_v8, async_tree_cpu_io_mixed, async_tree_io, bench_thread_pool
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (2) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 85.53% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown