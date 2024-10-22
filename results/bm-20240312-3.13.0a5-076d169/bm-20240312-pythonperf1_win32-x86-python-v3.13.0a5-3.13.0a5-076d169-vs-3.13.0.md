# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a5
- machine: windows-x86
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 237 ms: 1.07x faster                                                |
| chameleon      | 6.14 ms                                                         | 5.53 ms: 1.11x faster                                               |
| docutils       | 1.82 sec                                                        | 1.70 sec: 1.07x faster                                              |
| html5lib       | 48.3 ms                                                         | 42.0 ms: 1.15x faster                                               |
| tornado_http   | 104 ms                                                          | 93.5 ms: 1.11x faster                                               |
| Geometric mean | (ref)                                                           | 1.10x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 622 ms: 1.35x faster                                                |
| coroutines                 | 15.7 ms                                                         | 14.1 ms: 1.11x faster                                               |
| async_generators           | 274 ms                                                          | 261 ms: 1.05x faster                                                |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 16.7 sec: 1.04x faster                                              |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 484 ms: 1.02x faster                                                |
| async_tree_none            | 246 ms                                                          | 241 ms: 1.02x faster                                                |
| async_tree_memoization_tg  | 287 ms                                                          | 291 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 477 ms: 1.03x slower                                                |
| async_tree_none_tg         | 219 ms                                                          | 233 ms: 1.06x slower                                                |
| async_tree_io              | 537 ms                                                          | 591 ms: 1.10x slower                                                |
| async_tree_io_tg           | 509 ms                                                          | 574 ms: 1.13x slower                                                |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                        |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 74.7 ms: 1.10x faster                                               |
| float          | 57.8 ms                                                         | 53.8 ms: 1.07x faster                                               |
| pidigits       | 202 ms                                                          | 196 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                           | 1.07x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 94.7 ms: 1.09x faster                                               |
| regex_dna      | 117 ms                                                          | 119 ms: 1.02x slower                                                |
| regex_v8       | 15.6 ms                                                         | 15.9 ms: 1.02x slower                                               |
| regex_effbot   | 1.81 ms                                                         | 1.90 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                           | 1.00x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 162 us                                                          | 139 us: 1.16x faster                                                |
| pickle_pure_python   | 238 us                                                          | 206 us: 1.16x faster                                                |
| xml_etree_process    | 45.0 ms                                                         | 40.5 ms: 1.11x faster                                               |
| json_dumps           | 7.40 ms                                                         | 6.67 ms: 1.11x faster                                               |
| unpickle_list        | 3.09 us                                                         | 2.82 us: 1.10x faster                                               |
| tomli_loads          | 1.73 sec                                                        | 1.58 sec: 1.10x faster                                              |
| pickle               | 8.42 us                                                         | 7.74 us: 1.09x faster                                               |
| pickle_dict          | 21.7 us                                                         | 20.0 us: 1.08x faster                                               |
| xml_etree_generate   | 62.6 ms                                                         | 57.9 ms: 1.08x faster                                               |
| unpickle             | 10.5 us                                                         | 9.87 us: 1.07x faster                                               |
| pickle_list          | 3.40 us                                                         | 3.22 us: 1.06x faster                                               |
| json_loads           | 21.0 us                                                         | 20.1 us: 1.04x faster                                               |
| xml_etree_parse      | 109 ms                                                          | 107 ms: 1.01x faster                                                |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                        |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 22.8 ms: 1.06x faster                                               |
| python_startup_no_site | 19.9 ms                                                         | 20.6 ms: 1.03x slower                                               |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.4 ms                                                         | 18.3 ms: 1.23x faster                                               |
| genshi_xml      | 49.5 ms                                                         | 41.0 ms: 1.21x faster                                               |
| django_template | 32.7 ms                                                         | 28.6 ms: 1.14x faster                                               |
| mako            | 7.31 ms                                                         | 6.75 ms: 1.08x faster                                               |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols   | 136 us                                                          | 90.2 us: 1.51x faster                                               |
| asyncio_tcp                | 842 ms                                                          | 622 ms: 1.35x faster                                                |
| deepcopy_reduce            | 2.85 us                                                         | 2.32 us: 1.23x faster                                               |
| sqlglot_parse              | 1.05 ms                                                         | 856 us: 1.23x faster                                                |
| genshi_text                | 22.4 ms                                                         | 18.3 ms: 1.23x faster                                               |
| genshi_xml                 | 49.5 ms                                                         | 41.0 ms: 1.21x faster                                               |
| richards                   | 33.8 ms                                                         | 28.2 ms: 1.20x faster                                               |
| richards_super             | 38.0 ms                                                         | 31.8 ms: 1.20x faster                                               |
| sqlglot_transpile          | 1.29 ms                                                         | 1.08 ms: 1.19x faster                                               |
| go                         | 111 ms                                                          | 94.3 ms: 1.18x faster                                               |
| deepcopy                   | 307 us                                                          | 261 us: 1.18x faster                                                |
| deepcopy_memo              | 26.2 us                                                         | 22.4 us: 1.17x faster                                               |
| unpickle_pure_python       | 162 us                                                          | 139 us: 1.16x faster                                                |
| scimark_sor                | 91.8 ms                                                         | 79.3 ms: 1.16x faster                                               |
| pickle_pure_python         | 238 us                                                          | 206 us: 1.16x faster                                                |
| comprehensions             | 12.7 us                                                         | 11.0 us: 1.15x faster                                               |
| html5lib                   | 48.3 ms                                                         | 42.0 ms: 1.15x faster                                               |
| django_template            | 32.7 ms                                                         | 28.6 ms: 1.14x faster                                               |
| pprint_safe_repr           | 644 ms                                                          | 565 ms: 1.14x faster                                                |
| sqlglot_normalize          | 220 ms                                                          | 193 ms: 1.14x faster                                                |
| sqlglot_optimize           | 42.5 ms                                                         | 37.6 ms: 1.13x faster                                               |
| scimark_monte_carlo        | 50.3 ms                                                         | 44.5 ms: 1.13x faster                                               |
| deltablue                  | 2.41 ms                                                         | 2.13 ms: 1.13x faster                                               |
| pycparser                  | 869 ms                                                          | 777 ms: 1.12x faster                                                |
| pprint_pformat             | 1.30 sec                                                        | 1.16 sec: 1.12x faster                                              |
| hexiom                     | 4.64 ms                                                         | 4.16 ms: 1.12x faster                                               |
| tornado_http               | 104 ms                                                          | 93.5 ms: 1.11x faster                                               |
| telco                      | 6.67 ms                                                         | 5.99 ms: 1.11x faster                                               |
| xml_etree_process          | 45.0 ms                                                         | 40.5 ms: 1.11x faster                                               |
| crypto_pyaes               | 58.2 ms                                                         | 52.3 ms: 1.11x faster                                               |
| coroutines                 | 15.7 ms                                                         | 14.1 ms: 1.11x faster                                               |
| nqueens                    | 75.1 ms                                                         | 67.6 ms: 1.11x faster                                               |
| json_dumps                 | 7.40 ms                                                         | 6.67 ms: 1.11x faster                                               |
| chameleon                  | 6.14 ms                                                         | 5.53 ms: 1.11x faster                                               |
| sympy_str                  | 215 ms                                                          | 195 ms: 1.11x faster                                                |
| sympy_expand               | 375 ms                                                          | 341 ms: 1.10x faster                                                |
| unpickle_list              | 3.09 us                                                         | 2.82 us: 1.10x faster                                               |
| tomli_loads                | 1.73 sec                                                        | 1.58 sec: 1.10x faster                                              |
| sympy_sum                  | 108 ms                                                          | 98.5 ms: 1.10x faster                                               |
| nbody                      | 81.9 ms                                                         | 74.7 ms: 1.10x faster                                               |
| fannkuch                   | 293 ms                                                          | 268 ms: 1.09x faster                                                |
| regex_compile              | 103 ms                                                          | 94.7 ms: 1.09x faster                                               |
| spectral_norm              | 71.3 ms                                                         | 65.6 ms: 1.09x faster                                               |
| pickle                     | 8.42 us                                                         | 7.74 us: 1.09x faster                                               |
| create_gc_cycles           | 713 us                                                          | 657 us: 1.09x faster                                                |
| pickle_dict                | 21.7 us                                                         | 20.0 us: 1.08x faster                                               |
| mako                       | 7.31 ms                                                         | 6.75 ms: 1.08x faster                                               |
| scimark_lu                 | 63.5 ms                                                         | 58.7 ms: 1.08x faster                                               |
| xml_etree_generate         | 62.6 ms                                                         | 57.9 ms: 1.08x faster                                               |
| sympy_integrate            | 15.2 ms                                                         | 14.1 ms: 1.08x faster                                               |
| chaos                      | 51.2 ms                                                         | 47.5 ms: 1.08x faster                                               |
| logging_silent             | 61.6 ns                                                         | 57.3 ns: 1.08x faster                                               |
| float                      | 57.8 ms                                                         | 53.8 ms: 1.07x faster                                               |
| docutils                   | 1.82 sec                                                        | 1.70 sec: 1.07x faster                                              |
| raytrace                   | 205 ms                                                          | 192 ms: 1.07x faster                                                |
| unpickle                   | 10.5 us                                                         | 9.87 us: 1.07x faster                                               |
| 2to3                       | 253 ms                                                          | 237 ms: 1.07x faster                                                |
| python_startup             | 24.3 ms                                                         | 22.8 ms: 1.06x faster                                               |
| mdp                        | 1.67 sec                                                        | 1.58 sec: 1.06x faster                                              |
| logging_format             | 8.57 us                                                         | 8.10 us: 1.06x faster                                               |
| pyflate                    | 326 ms                                                          | 309 ms: 1.06x faster                                                |
| pickle_list                | 3.40 us                                                         | 3.22 us: 1.06x faster                                               |
| async_generators           | 274 ms                                                          | 261 ms: 1.05x faster                                                |
| logging_simple             | 7.87 us                                                         | 7.53 us: 1.05x faster                                               |
| json_loads                 | 21.0 us                                                         | 20.1 us: 1.04x faster                                               |
| json                       | 4.27 ms                                                         | 4.10 ms: 1.04x faster                                               |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 16.7 sec: 1.04x faster                                              |
| gc_traversal               | 1.45 ms                                                         | 1.40 ms: 1.04x faster                                               |
| pylint                     | 225 ms                                                          | 217 ms: 1.04x faster                                                |
| pidigits                   | 202 ms                                                          | 196 ms: 1.03x faster                                                |
| sqlite_synth               | 1.97 us                                                         | 1.91 us: 1.03x faster                                               |
| scimark_fft                | 206 ms                                                          | 201 ms: 1.03x faster                                                |
| meteor_contest             | 77.0 ms                                                         | 74.9 ms: 1.03x faster                                               |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 484 ms: 1.02x faster                                                |
| async_tree_none            | 246 ms                                                          | 241 ms: 1.02x faster                                                |
| xml_etree_parse            | 109 ms                                                          | 107 ms: 1.01x faster                                                |
| generators                 | 22.1 ms                                                         | 21.9 ms: 1.01x faster                                               |
| thrift                     | 10.1 ms                                                         | 10.1 ms: 1.00x faster                                               |
| flaskblogging              | 2.04 sec                                                        | 2.03 sec: 1.00x faster                                              |
| async_tree_memoization_tg  | 287 ms                                                          | 291 ms: 1.01x slower                                                |
| regex_dna                  | 117 ms                                                          | 119 ms: 1.02x slower                                                |
| regex_v8                   | 15.6 ms                                                         | 15.9 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 477 ms: 1.03x slower                                                |
| python_startup_no_site     | 19.9 ms                                                         | 20.6 ms: 1.03x slower                                               |
| regex_effbot               | 1.81 ms                                                         | 1.90 ms: 1.05x slower                                               |
| async_tree_none_tg         | 219 ms                                                          | 233 ms: 1.06x slower                                                |
| async_tree_io              | 537 ms                                                          | 591 ms: 1.10x slower                                                |
| async_tree_io_tg           | 509 ms                                                          | 574 ms: 1.13x slower                                                |
| coverage                   | 333 ms                                                          | 497 ms: 1.49x slower                                                |
| Geometric mean             | (ref)                                                           | 1.08x faster                                                        |

Benchmark hidden because not significant (6): bench_thread_pool, bench_mp_pool, pathlib, async_tree_memoization, scimark_sparse_mat_mult, xml_etree_iterparse
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown