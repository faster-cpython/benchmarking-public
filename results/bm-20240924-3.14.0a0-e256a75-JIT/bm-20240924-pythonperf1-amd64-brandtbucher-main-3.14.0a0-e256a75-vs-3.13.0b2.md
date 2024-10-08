# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: main
- machine: windows-amd64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.01x slower
- HPT reliability: 98.30%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 240 ms: 1.16x slower                                             |
| docutils       | 1.63 sec                                                        | 1.93 sec: 1.19x slower                                           |
| html5lib       | 35.0 ms                                                         | 41.4 ms: 1.18x slower                                            |
| tornado_http   | 81.8 ms                                                         | 88.1 ms: 1.08x slower                                            |
| Geometric mean | (ref)                                                           | 1.15x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 556 ms: 1.09x faster                                             |
| async_tree_none            | 218 ms                                                          | 202 ms: 1.08x faster                                             |
| async_tree_memoization     | 264 ms                                                          | 255 ms: 1.04x faster                                             |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 396 ms: 1.04x slower                                             |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                     |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 49.6 ms: 1.36x faster                                            |
| pidigits       | 150 ms                                                          | 149 ms: 1.00x faster                                             |
| float          | 49.7 ms                                                         | 53.4 ms: 1.07x slower                                            |
| Geometric mean | (ref)                                                           | 1.08x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 120 ms: 1.01x slower                                             |
| regex_effbot   | 1.58 ms                                                         | 1.61 ms: 1.02x slower                                            |
| regex_compile  | 78.0 ms                                                         | 94.7 ms: 1.21x slower                                            |
| Geometric mean | (ref)                                                           | 1.04x slower                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_process    | 36.4 ms                                                         | 34.8 ms: 1.05x faster                                            |
| tomli_loads          | 1.35 sec                                                        | 1.29 sec: 1.04x faster                                           |
| xml_etree_iterparse  | 62.3 ms                                                         | 59.8 ms: 1.04x faster                                            |
| pickle_list          | 2.90 us                                                         | 2.79 us: 1.04x faster                                            |
| pickle_dict          | 18.1 us                                                         | 17.8 us: 1.02x faster                                            |
| xml_etree_parse      | 90.9 ms                                                         | 92.1 ms: 1.01x slower                                            |
| json_loads           | 14.2 us                                                         | 14.4 us: 1.02x slower                                            |
| pickle               | 7.11 us                                                         | 7.43 us: 1.04x slower                                            |
| json_dumps           | 5.61 ms                                                         | 5.89 ms: 1.05x slower                                            |
| unpickle_list        | 2.62 us                                                         | 2.76 us: 1.05x slower                                            |
| unpickle             | 8.40 us                                                         | 9.11 us: 1.08x slower                                            |
| pickle_pure_python   | 175 us                                                          | 196 us: 1.12x slower                                             |
| unpickle_pure_python | 122 us                                                          | 143 us: 1.18x slower                                             |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                     |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.2 ms: 1.09x slower                                            |
| python_startup_no_site | 16.2 ms                                                         | 18.1 ms: 1.12x slower                                            |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 5.20 ms: 1.22x faster                                            |
| django_template | 21.7 ms                                                         | 26.4 ms: 1.22x slower                                            |
| genshi_text     | 14.4 ms                                                         | 19.2 ms: 1.34x slower                                            |
| genshi_xml      | 31.6 ms                                                         | 45.5 ms: 1.44x slower                                            |
| Geometric mean  | (ref)                                                           | 1.18x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 516 us: 15.71x faster                                            |
| deepcopy_memo              | 22.1 us                                                         | 15.3 us: 1.45x faster                                            |
| spectral_norm              | 63.7 ms                                                         | 44.8 ms: 1.42x faster                                            |
| nbody                      | 67.6 ms                                                         | 49.6 ms: 1.36x faster                                            |
| scimark_sor                | 75.3 ms                                                         | 60.5 ms: 1.24x faster                                            |
| mako                       | 6.36 ms                                                         | 5.20 ms: 1.22x faster                                            |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.06 ms: 1.22x faster                                            |
| deepcopy                   | 220 us                                                          | 183 us: 1.20x faster                                             |
| crypto_pyaes               | 45.5 ms                                                         | 38.1 ms: 1.19x faster                                            |
| scimark_fft                | 171 ms                                                          | 147 ms: 1.16x faster                                             |
| json                       | 3.19 ms                                                         | 2.90 ms: 1.10x faster                                            |
| async_tree_io_tg           | 605 ms                                                          | 556 ms: 1.09x faster                                             |
| deepcopy_reduce            | 1.99 us                                                         | 1.83 us: 1.09x faster                                            |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.37 sec: 1.08x faster                                           |
| async_tree_none            | 218 ms                                                          | 202 ms: 1.08x faster                                             |
| pycparser                  | 754 ms                                                          | 706 ms: 1.07x faster                                             |
| pyflate                    | 279 ms                                                          | 263 ms: 1.06x faster                                             |
| scimark_lu                 | 56.6 ms                                                         | 53.9 ms: 1.05x faster                                            |
| xml_etree_process          | 36.4 ms                                                         | 34.8 ms: 1.05x faster                                            |
| fannkuch                   | 243 ms                                                          | 233 ms: 1.04x faster                                             |
| tomli_loads                | 1.35 sec                                                        | 1.29 sec: 1.04x faster                                           |
| xml_etree_iterparse        | 62.3 ms                                                         | 59.8 ms: 1.04x faster                                            |
| pickle_list                | 2.90 us                                                         | 2.79 us: 1.04x faster                                            |
| async_tree_memoization     | 264 ms                                                          | 255 ms: 1.04x faster                                             |
| telco                      | 4.67 ms                                                         | 4.53 ms: 1.03x faster                                            |
| deltablue                  | 1.88 ms                                                         | 1.83 ms: 1.03x faster                                            |
| pickle_dict                | 18.1 us                                                         | 17.8 us: 1.02x faster                                            |
| gc_traversal               | 1.55 ms                                                         | 1.55 ms: 1.01x faster                                            |
| pidigits                   | 150 ms                                                          | 149 ms: 1.00x faster                                             |
| comprehensions             | 10.4 us                                                         | 10.5 us: 1.01x slower                                            |
| regex_dna                  | 119 ms                                                          | 120 ms: 1.01x slower                                             |
| xml_etree_parse            | 90.9 ms                                                         | 92.1 ms: 1.01x slower                                            |
| regex_effbot               | 1.58 ms                                                         | 1.61 ms: 1.02x slower                                            |
| logging_format             | 6.22 us                                                         | 6.33 us: 1.02x slower                                            |
| json_loads                 | 14.2 us                                                         | 14.4 us: 1.02x slower                                            |
| logging_simple             | 5.78 us                                                         | 5.91 us: 1.02x slower                                            |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 396 ms: 1.04x slower                                             |
| pickle                     | 7.11 us                                                         | 7.43 us: 1.04x slower                                            |
| json_dumps                 | 5.61 ms                                                         | 5.89 ms: 1.05x slower                                            |
| unpickle_list              | 2.62 us                                                         | 2.76 us: 1.05x slower                                            |
| chaos                      | 38.4 ms                                                         | 40.7 ms: 1.06x slower                                            |
| nqueens                    | 56.7 ms                                                         | 60.2 ms: 1.06x slower                                            |
| bench_thread_pool          | 768 us                                                          | 820 us: 1.07x slower                                             |
| coroutines                 | 12.8 ms                                                         | 13.7 ms: 1.07x slower                                            |
| float                      | 49.7 ms                                                         | 53.4 ms: 1.07x slower                                            |
| logging_silent             | 52.9 ns                                                         | 57.0 ns: 1.08x slower                                            |
| tornado_http               | 81.8 ms                                                         | 88.1 ms: 1.08x slower                                            |
| meteor_contest             | 69.9 ms                                                         | 75.3 ms: 1.08x slower                                            |
| sqlite_synth               | 1.60 us                                                         | 1.73 us: 1.08x slower                                            |
| bench_mp_pool              | 64.8 ms                                                         | 70.2 ms: 1.08x slower                                            |
| unpickle                   | 8.40 us                                                         | 9.11 us: 1.08x slower                                            |
| scimark_monte_carlo        | 39.1 ms                                                         | 42.7 ms: 1.09x slower                                            |
| python_startup             | 20.3 ms                                                         | 22.2 ms: 1.09x slower                                            |
| dulwich_log                | 38.0 ms                                                         | 42.0 ms: 1.10x slower                                            |
| typing_runtime_protocols   | 101 us                                                          | 112 us: 1.11x slower                                             |
| pprint_safe_repr           | 474 ms                                                          | 524 ms: 1.11x slower                                             |
| coverage                   | 42.1 ms                                                         | 46.5 ms: 1.11x slower                                            |
| pprint_pformat             | 966 ms                                                          | 1.07 sec: 1.11x slower                                           |
| pickle_pure_python         | 175 us                                                          | 196 us: 1.12x slower                                             |
| go                         | 82.1 ms                                                         | 91.7 ms: 1.12x slower                                            |
| python_startup_no_site     | 16.2 ms                                                         | 18.1 ms: 1.12x slower                                            |
| generators                 | 19.6 ms                                                         | 21.9 ms: 1.12x slower                                            |
| mdp                        | 1.31 sec                                                        | 1.50 sec: 1.14x slower                                           |
| sqlglot_normalize          | 173 ms                                                          | 198 ms: 1.15x slower                                             |
| async_generators           | 223 ms                                                          | 257 ms: 1.15x slower                                             |
| 2to3                       | 207 ms                                                          | 240 ms: 1.16x slower                                             |
| sympy_sum                  | 84.4 ms                                                         | 99.1 ms: 1.17x slower                                            |
| unpickle_pure_python       | 122 us                                                          | 143 us: 1.18x slower                                             |
| html5lib                   | 35.0 ms                                                         | 41.4 ms: 1.18x slower                                            |
| docutils                   | 1.63 sec                                                        | 1.93 sec: 1.19x slower                                           |
| sqlglot_parse              | 748 us                                                          | 887 us: 1.19x slower                                             |
| sympy_str                  | 159 ms                                                          | 189 ms: 1.19x slower                                             |
| sqlglot_transpile          | 955 us                                                          | 1.16 ms: 1.21x slower                                            |
| sqlglot_optimize           | 32.7 ms                                                         | 39.7 ms: 1.21x slower                                            |
| regex_compile              | 78.0 ms                                                         | 94.7 ms: 1.21x slower                                            |
| sympy_integrate            | 12.2 ms                                                         | 14.9 ms: 1.22x slower                                            |
| django_template            | 21.7 ms                                                         | 26.4 ms: 1.22x slower                                            |
| raytrace                   | 162 ms                                                          | 198 ms: 1.22x slower                                             |
| sympy_expand               | 271 ms                                                          | 332 ms: 1.23x slower                                             |
| pylint                     | 205 ms                                                          | 264 ms: 1.29x slower                                             |
| richards_super             | 30.2 ms                                                         | 39.3 ms: 1.30x slower                                            |
| hexiom                     | 3.72 ms                                                         | 4.88 ms: 1.31x slower                                            |
| genshi_text                | 14.4 ms                                                         | 19.2 ms: 1.34x slower                                            |
| richards                   | 26.7 ms                                                         | 36.6 ms: 1.37x slower                                            |
| genshi_xml                 | 31.6 ms                                                         | 45.5 ms: 1.44x slower                                            |
| Geometric mean             | (ref)                                                           | 1.01x slower                                                     |

Benchmark hidden because not significant (9): regex_v8, xml_etree_generate, async_tree_none_tg, async_tree_io, async_tree_memoization_tg, pathlib, create_gc_cycles, async_tree_cpu_io_mixed, asyncio_tcp
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-pythonperf1-amd64-brandtbucher-main-3.14.0a0-e256a75.json: unpack_sequence

# HPT report

- Reliability score: 98.30% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown