# Results vs. 3.13.0b2

- fork: python
- ref: v3.14.0a1
- machine: windows-x86
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.01x slower
- HPT reliability: 99.81%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 264 ms: 1.13x slower                                                |
| docutils       | 1.81 sec                                                            | 2.07 sec: 1.14x slower                                              |
| html5lib       | 45.4 ms                                                             | 47.2 ms: 1.04x slower                                               |
| tornado_http   | 94.3 ms                                                             | 109 ms: 1.16x slower                                                |
| Geometric mean | (ref)                                                               | 1.12x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 219 ms: 1.04x faster                                                |
| async_tree_io_tg           | 529 ms                                                              | 551 ms: 1.04x slower                                                |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 466 ms: 1.04x slower                                                |
| Geometric mean             | (ref)                                                               | 1.01x slower                                                        |

Benchmark hidden because not significant (5): async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 63.2 ms: 1.22x faster                                               |
| float          | 52.4 ms                                                             | 47.0 ms: 1.11x faster                                               |
| pidigits       | 199 ms                                                              | 200 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                               | 1.10x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.82 ms: 1.04x faster                                               |
| regex_v8       | 15.7 ms                                                             | 15.4 ms: 1.02x faster                                               |
| regex_compile  | 99.9 ms                                                             | 104 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                               | 1.00x faster                                                        |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_list        | 2.93 us                                                             | 2.71 us: 1.08x faster                                               |
| xml_etree_generate   | 59.6 ms                                                             | 55.7 ms: 1.07x faster                                               |
| tomli_loads          | 1.65 sec                                                            | 1.56 sec: 1.05x faster                                              |
| pickle_list          | 3.57 us                                                             | 3.48 us: 1.03x faster                                               |
| json_loads           | 20.5 us                                                             | 20.8 us: 1.02x slower                                               |
| xml_etree_process    | 42.1 ms                                                             | 42.8 ms: 1.02x slower                                               |
| pickle_dict          | 20.8 us                                                             | 21.5 us: 1.04x slower                                               |
| xml_etree_parse      | 104 ms                                                              | 109 ms: 1.04x slower                                                |
| unpickle             | 9.79 us                                                             | 10.4 us: 1.06x slower                                               |
| pickle               | 8.07 us                                                             | 8.60 us: 1.07x slower                                               |
| unpickle_pure_python | 147 us                                                              | 161 us: 1.10x slower                                                |
| pickle_pure_python   | 213 us                                                              | 246 us: 1.15x slower                                                |
| json_dumps           | 6.84 ms                                                             | 8.11 ms: 1.19x slower                                               |
| Geometric mean       | (ref)                                                               | 1.03x slower                                                        |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                             | 20.3 ms: 1.11x slower                                               |
| python_startup         | 22.2 ms                                                             | 27.1 ms: 1.22x slower                                               |
| Geometric mean         | (ref)                                                               | 1.17x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.70 ms: 1.22x faster                                               |
| django_template | 30.1 ms                                                             | 33.6 ms: 1.12x slower                                               |
| genshi_text     | 20.1 ms                                                             | 24.2 ms: 1.20x slower                                               |
| genshi_xml      | 44.3 ms                                                             | 54.0 ms: 1.22x slower                                               |
| Geometric mean  | (ref)                                                               | 1.08x slower                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 770 us: 12.63x faster                                               |
| coverage                   | 307 ms                                                              | 53.8 ms: 5.71x faster                                               |
| deepcopy_memo              | 23.5 us                                                             | 16.2 us: 1.45x faster                                               |
| mako                       | 6.94 ms                                                             | 5.70 ms: 1.22x faster                                               |
| nbody                      | 76.9 ms                                                             | 63.2 ms: 1.22x faster                                               |
| spectral_norm              | 68.0 ms                                                             | 57.2 ms: 1.19x faster                                               |
| deepcopy                   | 280 us                                                              | 238 us: 1.17x faster                                                |
| scimark_sor                | 81.0 ms                                                             | 70.1 ms: 1.15x faster                                               |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.54 ms: 1.13x faster                                               |
| float                      | 52.4 ms                                                             | 47.0 ms: 1.11x faster                                               |
| pprint_safe_repr           | 607 ms                                                              | 546 ms: 1.11x faster                                                |
| pprint_pformat             | 1.24 sec                                                            | 1.12 sec: 1.11x faster                                              |
| scimark_monte_carlo        | 45.2 ms                                                             | 41.6 ms: 1.09x faster                                               |
| fannkuch                   | 270 ms                                                              | 249 ms: 1.08x faster                                                |
| unpickle_list              | 2.93 us                                                             | 2.71 us: 1.08x faster                                               |
| crypto_pyaes               | 55.8 ms                                                             | 51.9 ms: 1.08x faster                                               |
| xml_etree_generate         | 59.6 ms                                                             | 55.7 ms: 1.07x faster                                               |
| scimark_fft                | 198 ms                                                              | 187 ms: 1.06x faster                                                |
| deepcopy_reduce            | 2.59 us                                                             | 2.44 us: 1.06x faster                                               |
| tomli_loads                | 1.65 sec                                                            | 1.56 sec: 1.05x faster                                              |
| async_tree_none            | 228 ms                                                              | 219 ms: 1.04x faster                                                |
| regex_effbot               | 1.88 ms                                                             | 1.82 ms: 1.04x faster                                               |
| go                         | 101 ms                                                              | 97.2 ms: 1.04x faster                                               |
| logging_silent             | 57.9 ns                                                             | 56.0 ns: 1.03x faster                                               |
| pickle_list                | 3.57 us                                                             | 3.48 us: 1.03x faster                                               |
| sqlite_synth               | 1.96 us                                                             | 1.91 us: 1.03x faster                                               |
| regex_v8                   | 15.7 ms                                                             | 15.4 ms: 1.02x faster                                               |
| meteor_contest             | 74.1 ms                                                             | 73.3 ms: 1.01x faster                                               |
| pidigits                   | 199 ms                                                              | 200 ms: 1.01x slower                                                |
| logging_simple             | 7.47 us                                                             | 7.54 us: 1.01x slower                                               |
| pyflate                    | 308 ms                                                              | 312 ms: 1.01x slower                                                |
| json_loads                 | 20.5 us                                                             | 20.8 us: 1.02x slower                                               |
| logging_format             | 8.13 us                                                             | 8.27 us: 1.02x slower                                               |
| xml_etree_process          | 42.1 ms                                                             | 42.8 ms: 1.02x slower                                               |
| scimark_lu                 | 59.4 ms                                                             | 60.6 ms: 1.02x slower                                               |
| bench_thread_pool          | 985 us                                                              | 1.01 ms: 1.02x slower                                               |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.5 sec: 1.03x slower                                              |
| pickle_dict                | 20.8 us                                                             | 21.5 us: 1.04x slower                                               |
| html5lib                   | 45.4 ms                                                             | 47.2 ms: 1.04x slower                                               |
| async_tree_io_tg           | 529 ms                                                              | 551 ms: 1.04x slower                                                |
| xml_etree_parse            | 104 ms                                                              | 109 ms: 1.04x slower                                                |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 466 ms: 1.04x slower                                                |
| regex_compile              | 99.9 ms                                                             | 104 ms: 1.04x slower                                                |
| sympy_expand               | 375 ms                                                              | 394 ms: 1.05x slower                                                |
| pathlib                    | 83.9 ms                                                             | 88.4 ms: 1.05x slower                                               |
| telco                      | 6.03 ms                                                             | 6.36 ms: 1.06x slower                                               |
| unpickle                   | 9.79 us                                                             | 10.4 us: 1.06x slower                                               |
| pickle                     | 8.07 us                                                             | 8.60 us: 1.07x slower                                               |
| pycparser                  | 777 ms                                                              | 834 ms: 1.07x slower                                                |
| sympy_str                  | 211 ms                                                              | 227 ms: 1.08x slower                                                |
| mdp                        | 1.60 sec                                                            | 1.73 sec: 1.08x slower                                              |
| sqlglot_parse              | 964 us                                                              | 1.05 ms: 1.09x slower                                               |
| typing_runtime_protocols   | 136 us                                                              | 148 us: 1.09x slower                                                |
| unpickle_pure_python       | 147 us                                                              | 161 us: 1.10x slower                                                |
| comprehensions             | 11.9 us                                                             | 13.0 us: 1.10x slower                                               |
| nqueens                    | 68.7 ms                                                             | 76.2 ms: 1.11x slower                                               |
| sympy_sum                  | 105 ms                                                              | 117 ms: 1.11x slower                                                |
| python_startup_no_site     | 18.2 ms                                                             | 20.3 ms: 1.11x slower                                               |
| django_template            | 30.1 ms                                                             | 33.6 ms: 1.12x slower                                               |
| 2to3                       | 233 ms                                                              | 264 ms: 1.13x slower                                                |
| docutils                   | 1.81 sec                                                            | 2.07 sec: 1.14x slower                                              |
| coroutines                 | 15.5 ms                                                             | 17.8 ms: 1.15x slower                                               |
| sqlglot_transpile          | 1.19 ms                                                             | 1.37 ms: 1.15x slower                                               |
| pickle_pure_python         | 213 us                                                              | 246 us: 1.15x slower                                                |
| tornado_http               | 94.3 ms                                                             | 109 ms: 1.16x slower                                                |
| chaos                      | 48.0 ms                                                             | 55.8 ms: 1.16x slower                                               |
| deltablue                  | 2.23 ms                                                             | 2.64 ms: 1.18x slower                                               |
| sqlglot_normalize          | 206 ms                                                              | 244 ms: 1.19x slower                                                |
| json_dumps                 | 6.84 ms                                                             | 8.11 ms: 1.19x slower                                               |
| generators                 | 21.2 ms                                                             | 25.1 ms: 1.19x slower                                               |
| asyncio_tcp                | 662 ms                                                              | 789 ms: 1.19x slower                                                |
| sympy_integrate            | 14.6 ms                                                             | 17.5 ms: 1.20x slower                                               |
| genshi_text                | 20.1 ms                                                             | 24.2 ms: 1.20x slower                                               |
| python_startup             | 22.2 ms                                                             | 27.1 ms: 1.22x slower                                               |
| genshi_xml                 | 44.3 ms                                                             | 54.0 ms: 1.22x slower                                               |
| async_generators           | 266 ms                                                              | 325 ms: 1.22x slower                                                |
| json                       | 4.10 ms                                                             | 5.03 ms: 1.23x slower                                               |
| sqlglot_optimize           | 39.7 ms                                                             | 50.3 ms: 1.27x slower                                               |
| gc_traversal               | 1.43 ms                                                             | 1.81 ms: 1.27x slower                                               |
| hexiom                     | 4.23 ms                                                             | 5.38 ms: 1.27x slower                                               |
| richards_super             | 35.5 ms                                                             | 45.6 ms: 1.29x slower                                               |
| richards                   | 31.2 ms                                                             | 40.2 ms: 1.29x slower                                               |
| pylint                     | 217 ms                                                              | 283 ms: 1.31x slower                                                |
| bench_mp_pool              | 69.4 ms                                                             | 94.5 ms: 1.36x slower                                               |
| raytrace                   | 189 ms                                                              | 269 ms: 1.43x slower                                                |
| create_gc_cycles           | 756 us                                                              | 1.20 ms: 1.58x slower                                               |
| Geometric mean             | (ref)                                                               | 1.01x slower                                                        |

Benchmark hidden because not significant (7): async_tree_io, regex_dna, async_tree_cpu_io_mixed, xml_etree_iterparse, async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (3) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json: dulwich_log, sphinx, unpack_sequence

# HPT report

- Reliability score: 99.81% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown