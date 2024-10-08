# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a5
- machine: windows-x86
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.02x faster
- HPT reliability: 99.09%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 237 ms: 1.02x slower                                                |
| chameleon      | 5.71 ms                                                             | 5.53 ms: 1.03x faster                                               |
| docutils       | 1.81 sec                                                            | 1.70 sec: 1.07x faster                                              |
| html5lib       | 45.4 ms                                                             | 42.0 ms: 1.08x faster                                               |
| tornado_http   | 94.3 ms                                                             | 93.5 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                               | 1.03x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 471 ms                                                              | 484 ms: 1.03x slower                                                |
| async_tree_none            | 228 ms                                                              | 241 ms: 1.06x slower                                                |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 477 ms: 1.07x slower                                                |
| async_tree_io_tg           | 529 ms                                                              | 574 ms: 1.08x slower                                                |
| async_tree_memoization     | 275 ms                                                              | 301 ms: 1.09x slower                                                |
| async_tree_io              | 530 ms                                                              | 591 ms: 1.12x slower                                                |
| async_tree_memoization_tg  | 254 ms                                                              | 291 ms: 1.14x slower                                                |
| async_tree_none_tg         | 203 ms                                                              | 233 ms: 1.15x slower                                                |
| Geometric mean             | (ref)                                                               | 1.09x slower                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 74.7 ms: 1.03x faster                                               |
| pidigits       | 199 ms                                                              | 196 ms: 1.01x faster                                                |
| float          | 52.4 ms                                                             | 53.8 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                               | 1.00x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 94.7 ms: 1.06x faster                                               |
| regex_effbot   | 1.88 ms                                                             | 1.90 ms: 1.01x slower                                               |
| regex_dna      | 118 ms                                                              | 119 ms: 1.01x slower                                                |
| regex_v8       | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                               | 1.01x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.22 us: 1.11x faster                                               |
| unpickle_pure_python | 147 us                                                              | 139 us: 1.06x faster                                                |
| tomli_loads          | 1.65 sec                                                            | 1.58 sec: 1.05x faster                                              |
| pickle               | 8.07 us                                                             | 7.74 us: 1.04x faster                                               |
| unpickle_list        | 2.93 us                                                             | 2.82 us: 1.04x faster                                               |
| xml_etree_process    | 42.1 ms                                                             | 40.5 ms: 1.04x faster                                               |
| pickle_pure_python   | 213 us                                                              | 206 us: 1.04x faster                                                |
| pickle_dict          | 20.8 us                                                             | 20.0 us: 1.04x faster                                               |
| xml_etree_generate   | 59.6 ms                                                             | 57.9 ms: 1.03x faster                                               |
| json_dumps           | 6.84 ms                                                             | 6.67 ms: 1.03x faster                                               |
| json_loads           | 20.5 us                                                             | 20.1 us: 1.02x faster                                               |
| unpickle             | 9.79 us                                                             | 9.87 us: 1.01x slower                                               |
| xml_etree_iterparse  | 64.2 ms                                                             | 65.4 ms: 1.02x slower                                               |
| xml_etree_parse      | 104 ms                                                              | 107 ms: 1.03x slower                                                |
| Geometric mean       | (ref)                                                               | 1.03x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 22.8 ms: 1.02x slower                                               |
| python_startup_no_site | 18.2 ms                                                             | 20.6 ms: 1.13x slower                                               |
| Geometric mean         | (ref)                                                               | 1.08x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 20.1 ms                                                             | 18.3 ms: 1.10x faster                                               |
| genshi_xml      | 44.3 ms                                                             | 41.0 ms: 1.08x faster                                               |
| django_template | 30.1 ms                                                             | 28.6 ms: 1.05x faster                                               |
| mako            | 6.94 ms                                                             | 6.75 ms: 1.03x faster                                               |
| Geometric mean  | (ref)                                                               | 1.06x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols   | 136 us                                                              | 90.2 us: 1.50x faster                                               |
| create_gc_cycles           | 756 us                                                              | 657 us: 1.15x faster                                                |
| sqlglot_parse              | 964 us                                                              | 856 us: 1.13x faster                                                |
| richards_super             | 35.5 ms                                                             | 31.8 ms: 1.12x faster                                               |
| deepcopy_reduce            | 2.59 us                                                             | 2.32 us: 1.12x faster                                               |
| pickle_list                | 3.57 us                                                             | 3.22 us: 1.11x faster                                               |
| richards                   | 31.2 ms                                                             | 28.2 ms: 1.11x faster                                               |
| sympy_expand               | 375 ms                                                              | 341 ms: 1.10x faster                                                |
| genshi_text                | 20.1 ms                                                             | 18.3 ms: 1.10x faster                                               |
| sqlglot_transpile          | 1.19 ms                                                             | 1.08 ms: 1.10x faster                                               |
| coroutines                 | 15.5 ms                                                             | 14.1 ms: 1.10x faster                                               |
| sympy_str                  | 211 ms                                                              | 195 ms: 1.09x faster                                                |
| html5lib                   | 45.4 ms                                                             | 42.0 ms: 1.08x faster                                               |
| genshi_xml                 | 44.3 ms                                                             | 41.0 ms: 1.08x faster                                               |
| comprehensions             | 11.9 us                                                             | 11.0 us: 1.08x faster                                               |
| pprint_safe_repr           | 607 ms                                                              | 565 ms: 1.07x faster                                                |
| deepcopy                   | 280 us                                                              | 261 us: 1.07x faster                                                |
| pprint_pformat             | 1.24 sec                                                            | 1.16 sec: 1.07x faster                                              |
| docutils                   | 1.81 sec                                                            | 1.70 sec: 1.07x faster                                              |
| go                         | 101 ms                                                              | 94.3 ms: 1.07x faster                                               |
| sympy_sum                  | 105 ms                                                              | 98.5 ms: 1.07x faster                                               |
| crypto_pyaes               | 55.8 ms                                                             | 52.3 ms: 1.07x faster                                               |
| sqlglot_normalize          | 206 ms                                                              | 193 ms: 1.07x faster                                                |
| asyncio_tcp                | 662 ms                                                              | 622 ms: 1.06x faster                                                |
| unpickle_pure_python       | 147 us                                                              | 139 us: 1.06x faster                                                |
| sqlglot_optimize           | 39.7 ms                                                             | 37.6 ms: 1.06x faster                                               |
| regex_compile              | 99.9 ms                                                             | 94.7 ms: 1.06x faster                                               |
| django_template            | 30.1 ms                                                             | 28.6 ms: 1.05x faster                                               |
| deltablue                  | 2.23 ms                                                             | 2.13 ms: 1.05x faster                                               |
| deepcopy_memo              | 23.5 us                                                             | 22.4 us: 1.05x faster                                               |
| tomli_loads                | 1.65 sec                                                            | 1.58 sec: 1.05x faster                                              |
| pickle                     | 8.07 us                                                             | 7.74 us: 1.04x faster                                               |
| sympy_integrate            | 14.6 ms                                                             | 14.1 ms: 1.04x faster                                               |
| unpickle_list              | 2.93 us                                                             | 2.82 us: 1.04x faster                                               |
| xml_etree_process          | 42.1 ms                                                             | 40.5 ms: 1.04x faster                                               |
| pickle_pure_python         | 213 us                                                              | 206 us: 1.04x faster                                                |
| pickle_dict                | 20.8 us                                                             | 20.0 us: 1.04x faster                                               |
| spectral_norm              | 68.0 ms                                                             | 65.6 ms: 1.04x faster                                               |
| chameleon                  | 5.71 ms                                                             | 5.53 ms: 1.03x faster                                               |
| xml_etree_generate         | 59.6 ms                                                             | 57.9 ms: 1.03x faster                                               |
| nbody                      | 76.9 ms                                                             | 74.7 ms: 1.03x faster                                               |
| mako                       | 6.94 ms                                                             | 6.75 ms: 1.03x faster                                               |
| sqlite_synth               | 1.96 us                                                             | 1.91 us: 1.03x faster                                               |
| json_dumps                 | 6.84 ms                                                             | 6.67 ms: 1.03x faster                                               |
| gc_traversal               | 1.43 ms                                                             | 1.40 ms: 1.02x faster                                               |
| scimark_sor                | 81.0 ms                                                             | 79.3 ms: 1.02x faster                                               |
| json_loads                 | 20.5 us                                                             | 20.1 us: 1.02x faster                                               |
| async_generators           | 266 ms                                                              | 261 ms: 1.02x faster                                                |
| hexiom                     | 4.23 ms                                                             | 4.16 ms: 1.02x faster                                               |
| mdp                        | 1.60 sec                                                            | 1.58 sec: 1.02x faster                                              |
| nqueens                    | 68.7 ms                                                             | 67.6 ms: 1.02x faster                                               |
| scimark_monte_carlo        | 45.2 ms                                                             | 44.5 ms: 1.01x faster                                               |
| pidigits                   | 199 ms                                                              | 196 ms: 1.01x faster                                                |
| scimark_lu                 | 59.4 ms                                                             | 58.7 ms: 1.01x faster                                               |
| logging_silent             | 57.9 ns                                                             | 57.3 ns: 1.01x faster                                               |
| chaos                      | 48.0 ms                                                             | 47.5 ms: 1.01x faster                                               |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 16.7 sec: 1.01x faster                                              |
| tornado_http               | 94.3 ms                                                             | 93.5 ms: 1.01x faster                                               |
| fannkuch                   | 270 ms                                                              | 268 ms: 1.01x faster                                                |
| telco                      | 6.03 ms                                                             | 5.99 ms: 1.01x faster                                               |
| regex_effbot               | 1.88 ms                                                             | 1.90 ms: 1.01x slower                                               |
| regex_dna                  | 118 ms                                                              | 119 ms: 1.01x slower                                                |
| unpickle                   | 9.79 us                                                             | 9.87 us: 1.01x slower                                               |
| logging_simple             | 7.47 us                                                             | 7.53 us: 1.01x slower                                               |
| meteor_contest             | 74.1 ms                                                             | 74.9 ms: 1.01x slower                                               |
| scimark_fft                | 198 ms                                                              | 201 ms: 1.01x slower                                                |
| regex_v8                   | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                               |
| raytrace                   | 189 ms                                                              | 192 ms: 1.02x slower                                                |
| 2to3                       | 233 ms                                                              | 237 ms: 1.02x slower                                                |
| xml_etree_iterparse        | 64.2 ms                                                             | 65.4 ms: 1.02x slower                                               |
| python_startup             | 22.2 ms                                                             | 22.8 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 484 ms: 1.03x slower                                                |
| float                      | 52.4 ms                                                             | 53.8 ms: 1.03x slower                                               |
| xml_etree_parse            | 104 ms                                                              | 107 ms: 1.03x slower                                                |
| generators                 | 21.2 ms                                                             | 21.9 ms: 1.03x slower                                               |
| thrift                     | 9.73 ms                                                             | 10.1 ms: 1.04x slower                                               |
| async_tree_none            | 228 ms                                                              | 241 ms: 1.06x slower                                                |
| pathlib                    | 83.9 ms                                                             | 89.2 ms: 1.06x slower                                               |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 477 ms: 1.07x slower                                                |
| bench_mp_pool              | 69.4 ms                                                             | 74.1 ms: 1.07x slower                                               |
| async_tree_io_tg           | 529 ms                                                              | 574 ms: 1.08x slower                                                |
| async_tree_memoization     | 275 ms                                                              | 301 ms: 1.09x slower                                                |
| async_tree_io              | 530 ms                                                              | 591 ms: 1.12x slower                                                |
| python_startup_no_site     | 18.2 ms                                                             | 20.6 ms: 1.13x slower                                               |
| async_tree_memoization_tg  | 254 ms                                                              | 291 ms: 1.14x slower                                                |
| async_tree_none_tg         | 203 ms                                                              | 233 ms: 1.15x slower                                                |
| coverage                   | 307 ms                                                              | 497 ms: 1.62x slower                                                |
| Geometric mean             | (ref)                                                               | 1.02x faster                                                        |

Benchmark hidden because not significant (8): logging_format, json, pycparser, flaskblogging, pylint, bench_thread_pool, pyflate, scimark_sparse_mat_mult

# HPT report

- Reliability score: 99.09% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown