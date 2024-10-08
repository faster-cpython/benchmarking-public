# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a4
- machine: windows-x86
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.02x faster
- HPT reliability: 98.74%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 230 ms: 1.01x faster                                                |
| chameleon      | 5.71 ms                                                             | 5.61 ms: 1.02x faster                                               |
| docutils       | 1.81 sec                                                            | 1.71 sec: 1.06x faster                                              |
| html5lib       | 45.4 ms                                                             | 43.9 ms: 1.03x faster                                               |
| tornado_http   | 94.3 ms                                                             | 93.5 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                               | 1.03x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 239 ms: 1.05x slower                                                |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 496 ms: 1.05x slower                                                |
| async_tree_io_tg           | 529 ms                                                              | 570 ms: 1.08x slower                                                |
| async_tree_memoization     | 275 ms                                                              | 299 ms: 1.09x slower                                                |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 489 ms: 1.09x slower                                                |
| async_tree_io              | 530 ms                                                              | 584 ms: 1.10x slower                                                |
| async_tree_none_tg         | 203 ms                                                              | 225 ms: 1.11x slower                                                |
| async_tree_memoization_tg  | 254 ms                                                              | 284 ms: 1.12x slower                                                |
| Geometric mean             | (ref)                                                               | 1.09x slower                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 197 ms: 1.01x faster                                                |
| float          | 52.4 ms                                                             | 52.8 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                               | 1.00x faster                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 93.4 ms: 1.07x faster                                               |
| regex_dna      | 118 ms                                                              | 116 ms: 1.02x faster                                                |
| regex_v8       | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                               | 1.02x faster                                                        |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.25 us: 1.10x faster                                               |
| unpickle_pure_python | 147 us                                                              | 140 us: 1.05x faster                                                |
| pickle_dict          | 20.8 us                                                             | 19.8 us: 1.05x faster                                               |
| pickle               | 8.07 us                                                             | 7.90 us: 1.02x faster                                               |
| xml_etree_process    | 42.1 ms                                                             | 41.2 ms: 1.02x faster                                               |
| tomli_loads          | 1.65 sec                                                            | 1.62 sec: 1.02x faster                                              |
| json_dumps           | 6.84 ms                                                             | 6.71 ms: 1.02x faster                                               |
| unpickle_list        | 2.93 us                                                             | 2.88 us: 1.02x faster                                               |
| pickle_pure_python   | 213 us                                                              | 210 us: 1.02x faster                                                |
| json_loads           | 20.5 us                                                             | 20.2 us: 1.01x faster                                               |
| xml_etree_generate   | 59.6 ms                                                             | 60.0 ms: 1.01x slower                                               |
| unpickle             | 9.79 us                                                             | 10.0 us: 1.02x slower                                               |
| xml_etree_iterparse  | 64.2 ms                                                             | 66.2 ms: 1.03x slower                                               |
| xml_etree_parse      | 104 ms                                                              | 110 ms: 1.05x slower                                                |
| Geometric mean       | (ref)                                                               | 1.01x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 22.0 ms: 1.01x faster                                               |
| python_startup_no_site | 18.2 ms                                                             | 19.7 ms: 1.08x slower                                               |
| Geometric mean         | (ref)                                                               | 1.04x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 20.1 ms                                                             | 18.9 ms: 1.06x faster                                               |
| genshi_xml      | 44.3 ms                                                             | 41.8 ms: 1.06x faster                                               |
| mako            | 6.94 ms                                                             | 6.76 ms: 1.03x faster                                               |
| django_template | 30.1 ms                                                             | 30.4 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                               | 1.03x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols   | 136 us                                                              | 87.8 us: 1.54x faster                                               |
| create_gc_cycles           | 756 us                                                              | 662 us: 1.14x faster                                                |
| deepcopy_reduce            | 2.59 us                                                             | 2.32 us: 1.12x faster                                               |
| sqlglot_parse              | 964 us                                                              | 868 us: 1.11x faster                                                |
| sympy_expand               | 375 ms                                                              | 341 ms: 1.10x faster                                                |
| richards                   | 31.2 ms                                                             | 28.4 ms: 1.10x faster                                               |
| pickle_list                | 3.57 us                                                             | 3.25 us: 1.10x faster                                               |
| coroutines                 | 15.5 ms                                                             | 14.1 ms: 1.10x faster                                               |
| sympy_str                  | 211 ms                                                              | 194 ms: 1.09x faster                                                |
| sqlglot_transpile          | 1.19 ms                                                             | 1.10 ms: 1.08x faster                                               |
| asyncio_tcp                | 662 ms                                                              | 618 ms: 1.07x faster                                                |
| deepcopy                   | 280 us                                                              | 261 us: 1.07x faster                                                |
| deepcopy_memo              | 23.5 us                                                             | 22.0 us: 1.07x faster                                               |
| regex_compile              | 99.9 ms                                                             | 93.4 ms: 1.07x faster                                               |
| pprint_safe_repr           | 607 ms                                                              | 568 ms: 1.07x faster                                                |
| pprint_pformat             | 1.24 sec                                                            | 1.16 sec: 1.06x faster                                              |
| genshi_text                | 20.1 ms                                                             | 18.9 ms: 1.06x faster                                               |
| crypto_pyaes               | 55.8 ms                                                             | 52.6 ms: 1.06x faster                                               |
| genshi_xml                 | 44.3 ms                                                             | 41.8 ms: 1.06x faster                                               |
| sqlite_synth               | 1.96 us                                                             | 1.85 us: 1.06x faster                                               |
| go                         | 101 ms                                                              | 95.1 ms: 1.06x faster                                               |
| docutils                   | 1.81 sec                                                            | 1.71 sec: 1.06x faster                                              |
| sympy_sum                  | 105 ms                                                              | 99.4 ms: 1.06x faster                                               |
| richards_super             | 35.5 ms                                                             | 33.7 ms: 1.05x faster                                               |
| unpickle_pure_python       | 147 us                                                              | 140 us: 1.05x faster                                                |
| telco                      | 6.03 ms                                                             | 5.76 ms: 1.05x faster                                               |
| pickle_dict                | 20.8 us                                                             | 19.8 us: 1.05x faster                                               |
| sympy_integrate            | 14.6 ms                                                             | 14.0 ms: 1.04x faster                                               |
| spectral_norm              | 68.0 ms                                                             | 65.4 ms: 1.04x faster                                               |
| chaos                      | 48.0 ms                                                             | 46.3 ms: 1.04x faster                                               |
| html5lib                   | 45.4 ms                                                             | 43.9 ms: 1.03x faster                                               |
| comprehensions             | 11.9 us                                                             | 11.5 us: 1.03x faster                                               |
| gc_traversal               | 1.43 ms                                                             | 1.39 ms: 1.03x faster                                               |
| deltablue                  | 2.23 ms                                                             | 2.17 ms: 1.03x faster                                               |
| sqlglot_optimize           | 39.7 ms                                                             | 38.6 ms: 1.03x faster                                               |
| mako                       | 6.94 ms                                                             | 6.76 ms: 1.03x faster                                               |
| nqueens                    | 68.7 ms                                                             | 66.9 ms: 1.03x faster                                               |
| sqlglot_normalize          | 206 ms                                                              | 201 ms: 1.02x faster                                                |
| pickle                     | 8.07 us                                                             | 7.90 us: 1.02x faster                                               |
| xml_etree_process          | 42.1 ms                                                             | 41.2 ms: 1.02x faster                                               |
| tomli_loads                | 1.65 sec                                                            | 1.62 sec: 1.02x faster                                              |
| chameleon                  | 5.71 ms                                                             | 5.61 ms: 1.02x faster                                               |
| mdp                        | 1.60 sec                                                            | 1.57 sec: 1.02x faster                                              |
| json_dumps                 | 6.84 ms                                                             | 6.71 ms: 1.02x faster                                               |
| regex_dna                  | 118 ms                                                              | 116 ms: 1.02x faster                                                |
| logging_silent             | 57.9 ns                                                             | 56.9 ns: 1.02x faster                                               |
| unpickle_list              | 2.93 us                                                             | 2.88 us: 1.02x faster                                               |
| pickle_pure_python         | 213 us                                                              | 210 us: 1.02x faster                                                |
| json_loads                 | 20.5 us                                                             | 20.2 us: 1.01x faster                                               |
| 2to3                       | 233 ms                                                              | 230 ms: 1.01x faster                                                |
| async_generators           | 266 ms                                                              | 262 ms: 1.01x faster                                                |
| python_startup             | 22.2 ms                                                             | 22.0 ms: 1.01x faster                                               |
| pidigits                   | 199 ms                                                              | 197 ms: 1.01x faster                                                |
| tornado_http               | 94.3 ms                                                             | 93.5 ms: 1.01x faster                                               |
| hexiom                     | 4.23 ms                                                             | 4.20 ms: 1.01x faster                                               |
| scimark_monte_carlo        | 45.2 ms                                                             | 44.9 ms: 1.01x faster                                               |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 16.8 sec: 1.01x faster                                              |
| scimark_lu                 | 59.4 ms                                                             | 59.0 ms: 1.01x faster                                               |
| pyflate                    | 308 ms                                                              | 307 ms: 1.00x faster                                                |
| xml_etree_generate         | 59.6 ms                                                             | 60.0 ms: 1.01x slower                                               |
| float                      | 52.4 ms                                                             | 52.8 ms: 1.01x slower                                               |
| pycparser                  | 777 ms                                                              | 784 ms: 1.01x slower                                                |
| django_template            | 30.1 ms                                                             | 30.4 ms: 1.01x slower                                               |
| raytrace                   | 189 ms                                                              | 191 ms: 1.01x slower                                                |
| thrift                     | 9.73 ms                                                             | 9.86 ms: 1.01x slower                                               |
| bench_mp_pool              | 69.4 ms                                                             | 70.4 ms: 1.01x slower                                               |
| json                       | 4.10 ms                                                             | 4.16 ms: 1.02x slower                                               |
| regex_v8                   | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                               |
| unpickle                   | 9.79 us                                                             | 10.0 us: 1.02x slower                                               |
| xml_etree_iterparse        | 64.2 ms                                                             | 66.2 ms: 1.03x slower                                               |
| meteor_contest             | 74.1 ms                                                             | 77.4 ms: 1.05x slower                                               |
| async_tree_none            | 228 ms                                                              | 239 ms: 1.05x slower                                                |
| xml_etree_parse            | 104 ms                                                              | 110 ms: 1.05x slower                                                |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 496 ms: 1.05x slower                                                |
| pathlib                    | 83.9 ms                                                             | 88.6 ms: 1.06x slower                                               |
| generators                 | 21.2 ms                                                             | 22.7 ms: 1.07x slower                                               |
| async_tree_io_tg           | 529 ms                                                              | 570 ms: 1.08x slower                                                |
| python_startup_no_site     | 18.2 ms                                                             | 19.7 ms: 1.08x slower                                               |
| async_tree_memoization     | 275 ms                                                              | 299 ms: 1.09x slower                                                |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 489 ms: 1.09x slower                                                |
| async_tree_io              | 530 ms                                                              | 584 ms: 1.10x slower                                                |
| async_tree_none_tg         | 203 ms                                                              | 225 ms: 1.11x slower                                                |
| async_tree_memoization_tg  | 254 ms                                                              | 284 ms: 1.12x slower                                                |
| coverage                   | 307 ms                                                              | 460 ms: 1.50x slower                                                |
| Geometric mean             | (ref)                                                               | 1.02x faster                                                        |

Benchmark hidden because not significant (11): logging_format, nbody, logging_simple, scimark_sor, bench_thread_pool, pylint, flaskblogging, regex_effbot, scimark_fft, fannkuch, scimark_sparse_mat_mult

# HPT report

- Reliability score: 98.74% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown