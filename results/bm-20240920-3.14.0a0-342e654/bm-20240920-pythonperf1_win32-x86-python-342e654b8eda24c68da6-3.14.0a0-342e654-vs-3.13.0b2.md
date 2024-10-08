# Results vs. 3.13.0b2

- fork: python
- ref: 342e654b8eda24c68da6
- machine: windows-x86
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 256 ms: 1.10x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                         |
| html5lib       | 45.4 ms                                                             | 47.1 ms: 1.04x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 95.6 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 223 ms: 1.02x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 521 ms: 1.02x faster                                                           |
| async_tree_io              | 530 ms                                                              | 544 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 460 ms: 1.03x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.00x slower                                                                   |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 197 ms: 1.01x faster                                                           |
| float          | 52.4 ms                                                             | 61.2 ms: 1.17x slower                                                          |
| nbody          | 76.9 ms                                                             | 91.0 ms: 1.18x slower                                                          |
| Geometric mean | (ref)                                                               | 1.11x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.7 ms                                                             | 16.1 ms: 1.02x slower                                                          |
| regex_effbot   | 1.88 ms                                                             | 1.99 ms: 1.06x slower                                                          |
| regex_dna      | 118 ms                                                              | 128 ms: 1.08x slower                                                           |
| regex_compile  | 99.9 ms                                                             | 110 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                               | 1.07x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.34 us: 1.07x faster                                                          |
| pickle               | 8.07 us                                                             | 7.84 us: 1.03x faster                                                          |
| unpickle_list        | 2.93 us                                                             | 2.91 us: 1.01x faster                                                          |
| xml_etree_parse      | 104 ms                                                              | 109 ms: 1.04x slower                                                           |
| unpickle             | 9.79 us                                                             | 10.2 us: 1.04x slower                                                          |
| json_loads           | 20.5 us                                                             | 21.5 us: 1.05x slower                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 67.7 ms: 1.06x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.45 ms: 1.09x slower                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 67.3 ms: 1.13x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.92 sec: 1.17x slower                                                         |
| xml_etree_process    | 42.1 ms                                                             | 49.2 ms: 1.17x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 177 us: 1.20x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 261 us: 1.22x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.07x slower                                                                   |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.4 ms: 1.10x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 20.5 ms: 1.12x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.11x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 48.5 ms: 1.10x slower                                                          |
| django_template | 30.1 ms                                                             | 33.3 ms: 1.11x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 22.5 ms: 1.12x slower                                                          |
| mako            | 6.94 ms                                                             | 8.09 ms: 1.16x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.12x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 742 us: 13.11x faster                                                          |
| coverage                   | 307 ms                                                              | 51.3 ms: 5.99x faster                                                          |
| deepcopy                   | 280 us                                                              | 243 us: 1.15x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 21.9 us: 1.07x faster                                                          |
| pickle_list                | 3.57 us                                                             | 3.34 us: 1.07x faster                                                          |
| pickle                     | 8.07 us                                                             | 7.84 us: 1.03x faster                                                          |
| create_gc_cycles           | 756 us                                                              | 739 us: 1.02x faster                                                           |
| async_tree_none            | 228 ms                                                              | 223 ms: 1.02x faster                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.53 us: 1.02x faster                                                          |
| async_tree_io_tg           | 529 ms                                                              | 521 ms: 1.02x faster                                                           |
| pidigits                   | 199 ms                                                              | 197 ms: 1.01x faster                                                           |
| pathlib                    | 83.9 ms                                                             | 83.2 ms: 1.01x faster                                                          |
| unpickle_list              | 2.93 us                                                             | 2.91 us: 1.01x faster                                                          |
| sqlite_synth               | 1.96 us                                                             | 1.97 us: 1.00x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 95.6 ms: 1.01x slower                                                          |
| regex_v8                   | 15.7 ms                                                             | 16.1 ms: 1.02x slower                                                          |
| async_tree_io              | 530 ms                                                              | 544 ms: 1.03x slower                                                           |
| sympy_sum                  | 105 ms                                                              | 108 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 460 ms: 1.03x slower                                                           |
| sympy_expand               | 375 ms                                                              | 386 ms: 1.03x slower                                                           |
| docutils                   | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                         |
| sympy_str                  | 211 ms                                                              | 219 ms: 1.04x slower                                                           |
| html5lib                   | 45.4 ms                                                             | 47.1 ms: 1.04x slower                                                          |
| xml_etree_parse            | 104 ms                                                              | 109 ms: 1.04x slower                                                           |
| unpickle                   | 9.79 us                                                             | 10.2 us: 1.04x slower                                                          |
| json_loads                 | 20.5 us                                                             | 21.5 us: 1.05x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 15.4 ms: 1.05x slower                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 67.7 ms: 1.06x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 1.99 ms: 1.06x slower                                                          |
| json                       | 4.10 ms                                                             | 4.34 ms: 1.06x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 144 us: 1.06x slower                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.06 ms: 1.07x slower                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 59.8 ms: 1.07x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 74.4 ms: 1.07x slower                                                          |
| logging_simple             | 7.47 us                                                             | 8.02 us: 1.07x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.74 us: 1.08x slower                                                          |
| pylint                     | 217 ms                                                              | 234 ms: 1.08x slower                                                           |
| regex_dna                  | 118 ms                                                              | 128 ms: 1.08x slower                                                           |
| go                         | 101 ms                                                              | 109 ms: 1.08x slower                                                           |
| meteor_contest             | 74.1 ms                                                             | 80.1 ms: 1.08x slower                                                          |
| telco                      | 6.03 ms                                                             | 6.53 ms: 1.08x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.45 ms: 1.09x slower                                                          |
| python_startup             | 22.2 ms                                                             | 24.4 ms: 1.10x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 48.5 ms: 1.10x slower                                                          |
| 2to3                       | 233 ms                                                              | 256 ms: 1.10x slower                                                           |
| nqueens                    | 68.7 ms                                                             | 75.6 ms: 1.10x slower                                                          |
| regex_compile              | 99.9 ms                                                             | 110 ms: 1.11x slower                                                           |
| django_template            | 30.1 ms                                                             | 33.3 ms: 1.11x slower                                                          |
| spectral_norm              | 68.0 ms                                                             | 75.8 ms: 1.11x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 22.5 ms: 1.12x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 20.5 ms: 1.12x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 232 ms: 1.13x slower                                                           |
| sqlglot_parse              | 964 us                                                              | 1.09 ms: 1.13x slower                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 67.3 ms: 1.13x slower                                                          |
| async_generators           | 266 ms                                                              | 300 ms: 1.13x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 44.9 ms: 1.13x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.35 ms: 1.13x slower                                                          |
| pycparser                  | 777 ms                                                              | 880 ms: 1.13x slower                                                           |
| pprint_safe_repr           | 607 ms                                                              | 687 ms: 1.13x slower                                                           |
| mdp                        | 1.60 sec                                                            | 1.82 sec: 1.14x slower                                                         |
| pprint_pformat             | 1.24 sec                                                            | 1.41 sec: 1.14x slower                                                         |
| chaos                      | 48.0 ms                                                             | 55.1 ms: 1.15x slower                                                          |
| pyflate                    | 308 ms                                                              | 357 ms: 1.16x slower                                                           |
| mako                       | 6.94 ms                                                             | 8.09 ms: 1.16x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 69.2 ms: 1.17x slower                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.92 sec: 1.17x slower                                                         |
| xml_etree_process          | 42.1 ms                                                             | 49.2 ms: 1.17x slower                                                          |
| float                      | 52.4 ms                                                             | 61.2 ms: 1.17x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 18.1 ms: 1.17x slower                                                          |
| comprehensions             | 11.9 us                                                             | 14.0 us: 1.18x slower                                                          |
| nbody                      | 76.9 ms                                                             | 91.0 ms: 1.18x slower                                                          |
| scimark_fft                | 198 ms                                                              | 236 ms: 1.19x slower                                                           |
| unpickle_pure_python       | 147 us                                                              | 177 us: 1.20x slower                                                           |
| scimark_sor                | 81.0 ms                                                             | 98.2 ms: 1.21x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.73 ms: 1.22x slower                                                          |
| fannkuch                   | 270 ms                                                              | 330 ms: 1.22x slower                                                           |
| pickle_pure_python         | 213 us                                                              | 261 us: 1.22x slower                                                           |
| generators                 | 21.2 ms                                                             | 26.2 ms: 1.24x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 5.26 ms: 1.24x slower                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 56.7 ms: 1.25x slower                                                          |
| raytrace                   | 189 ms                                                              | 243 ms: 1.29x slower                                                           |
| richards_super             | 35.5 ms                                                             | 45.9 ms: 1.29x slower                                                          |
| richards                   | 31.2 ms                                                             | 40.6 ms: 1.30x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 76.1 ns: 1.32x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.04x slower                                                                   |

Benchmark hidden because not significant (9): asyncio_tcp, async_tree_none_tg, async_tree_memoization_tg, pickle_dict, gc_traversal, asyncio_tcp_ssl, async_tree_cpu_io_mixed, async_tree_memoization, bench_thread_pool
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (2) of results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf1_win32-x86-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown