# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0rc2
- machine: windows-x86
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 245 ms: 1.05x slower                                                  |
| chameleon      | 5.71 ms                                                             | 5.83 ms: 1.02x slower                                                 |
| docutils       | 1.81 sec                                                            | 1.85 sec: 1.02x slower                                                |
| html5lib       | 45.4 ms                                                             | 45.7 ms: 1.01x slower                                                 |
| tornado_http   | 94.3 ms                                                             | 104 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                               | 1.04x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|---------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg          | 529 ms                                                              | 537 ms: 1.01x slower                                                  |
| async_tree_memoization_tg | 254 ms                                                              | 260 ms: 1.02x slower                                                  |
| async_tree_none_tg        | 203 ms                                                              | 208 ms: 1.02x slower                                                  |
| Geometric mean            | (ref)                                                               | 1.01x slower                                                          |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 199 ms: 1.00x slower                                                  |
| float          | 52.4 ms                                                             | 53.5 ms: 1.02x slower                                                 |
| nbody          | 76.9 ms                                                             | 79.6 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                               | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                 |
| regex_compile  | 99.9 ms                                                             | 101 ms: 1.01x slower                                                  |
| regex_dna      | 118 ms                                                              | 119 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                               | 1.01x slower                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.15 us: 1.13x faster                                                 |
| pickle_dict          | 20.8 us                                                             | 20.4 us: 1.02x faster                                                 |
| pickle               | 8.07 us                                                             | 8.01 us: 1.01x faster                                                 |
| xml_etree_iterparse  | 64.2 ms                                                             | 65.3 ms: 1.02x slower                                                 |
| xml_etree_parse      | 104 ms                                                              | 107 ms: 1.02x slower                                                  |
| unpickle             | 9.79 us                                                             | 10.0 us: 1.02x slower                                                 |
| json_dumps           | 6.84 ms                                                             | 7.03 ms: 1.03x slower                                                 |
| xml_etree_generate   | 59.6 ms                                                             | 62.2 ms: 1.04x slower                                                 |
| unpickle_pure_python | 147 us                                                              | 155 us: 1.06x slower                                                  |
| xml_etree_process    | 42.1 ms                                                             | 44.9 ms: 1.07x slower                                                 |
| pickle_pure_python   | 213 us                                                              | 228 us: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.01x slower                                                          |

Benchmark hidden because not significant (3): unpickle_list, json_loads, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.2 ms: 1.09x slower                                                 |
| python_startup_no_site | 18.2 ms                                                             | 19.9 ms: 1.09x slower                                                 |
| Geometric mean         | (ref)                                                               | 1.09x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 20.1 ms                                                             | 19.8 ms: 1.02x faster                                                 |
| genshi_xml      | 44.3 ms                                                             | 43.9 ms: 1.01x faster                                                 |
| mako            | 6.94 ms                                                             | 7.08 ms: 1.02x slower                                                 |
| django_template | 30.1 ms                                                             | 31.1 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                               | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|---------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_list               | 3.57 us                                                             | 3.15 us: 1.13x faster                                                 |
| pylint                    | 217 ms                                                              | 210 ms: 1.03x faster                                                  |
| sympy_expand              | 375 ms                                                              | 368 ms: 1.02x faster                                                  |
| genshi_text               | 20.1 ms                                                             | 19.8 ms: 1.02x faster                                                 |
| scimark_sparse_mat_mult   | 2.87 ms                                                             | 2.82 ms: 1.02x faster                                                 |
| pickle_dict               | 20.8 us                                                             | 20.4 us: 1.02x faster                                                 |
| genshi_xml                | 44.3 ms                                                             | 43.9 ms: 1.01x faster                                                 |
| pickle                    | 8.07 us                                                             | 8.01 us: 1.01x faster                                                 |
| crypto_pyaes              | 55.8 ms                                                             | 55.4 ms: 1.01x faster                                                 |
| pidigits                  | 199 ms                                                              | 199 ms: 1.00x slower                                                  |
| flaskblogging             | 2.03 sec                                                            | 2.04 sec: 1.00x slower                                                |
| pprint_pformat            | 1.24 sec                                                            | 1.25 sec: 1.00x slower                                                |
| html5lib                  | 45.4 ms                                                             | 45.7 ms: 1.01x slower                                                 |
| regex_v8                  | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                 |
| sqlite_synth              | 1.96 us                                                             | 1.98 us: 1.01x slower                                                 |
| regex_compile             | 99.9 ms                                                             | 101 ms: 1.01x slower                                                  |
| regex_dna                 | 118 ms                                                              | 119 ms: 1.01x slower                                                  |
| nqueens                   | 68.7 ms                                                             | 69.5 ms: 1.01x slower                                                 |
| sympy_sum                 | 105 ms                                                              | 106 ms: 1.01x slower                                                  |
| async_tree_io_tg          | 529 ms                                                              | 537 ms: 1.01x slower                                                  |
| xml_etree_iterparse       | 64.2 ms                                                             | 65.3 ms: 1.02x slower                                                 |
| asyncio_tcp_ssl           | 16.9 sec                                                            | 17.2 sec: 1.02x slower                                                |
| sympy_integrate           | 14.6 ms                                                             | 14.9 ms: 1.02x slower                                                 |
| mako                      | 6.94 ms                                                             | 7.08 ms: 1.02x slower                                                 |
| chameleon                 | 5.71 ms                                                             | 5.83 ms: 1.02x slower                                                 |
| xml_etree_parse           | 104 ms                                                              | 107 ms: 1.02x slower                                                  |
| chaos                     | 48.0 ms                                                             | 48.9 ms: 1.02x slower                                                 |
| sqlglot_normalize         | 206 ms                                                              | 210 ms: 1.02x slower                                                  |
| sqlglot_transpile         | 1.19 ms                                                             | 1.22 ms: 1.02x slower                                                 |
| raytrace                  | 189 ms                                                              | 193 ms: 1.02x slower                                                  |
| docutils                  | 1.81 sec                                                            | 1.85 sec: 1.02x slower                                                |
| float                     | 52.4 ms                                                             | 53.5 ms: 1.02x slower                                                 |
| unpickle                  | 9.79 us                                                             | 10.0 us: 1.02x slower                                                 |
| typing_runtime_protocols  | 136 us                                                              | 139 us: 1.02x slower                                                  |
| sqlglot_optimize          | 39.7 ms                                                             | 40.6 ms: 1.02x slower                                                 |
| meteor_contest            | 74.1 ms                                                             | 75.8 ms: 1.02x slower                                                 |
| async_tree_memoization_tg | 254 ms                                                              | 260 ms: 1.02x slower                                                  |
| async_tree_none_tg        | 203 ms                                                              | 208 ms: 1.02x slower                                                  |
| sqlglot_parse             | 964 us                                                              | 989 us: 1.03x slower                                                  |
| pycparser                 | 777 ms                                                              | 798 ms: 1.03x slower                                                  |
| bench_thread_pool         | 985 us                                                              | 1.01 ms: 1.03x slower                                                 |
| json_dumps                | 6.84 ms                                                             | 7.03 ms: 1.03x slower                                                 |
| generators                | 21.2 ms                                                             | 21.8 ms: 1.03x slower                                                 |
| mdp                       | 1.60 sec                                                            | 1.65 sec: 1.03x slower                                                |
| deepcopy                  | 280 us                                                              | 288 us: 1.03x slower                                                  |
| scimark_fft               | 198 ms                                                              | 204 ms: 1.03x slower                                                  |
| coroutines                | 15.5 ms                                                             | 16.0 ms: 1.03x slower                                                 |
| spectral_norm             | 68.0 ms                                                             | 70.3 ms: 1.03x slower                                                 |
| nbody                     | 76.9 ms                                                             | 79.6 ms: 1.04x slower                                                 |
| django_template           | 30.1 ms                                                             | 31.1 ms: 1.04x slower                                                 |
| pyflate                   | 308 ms                                                              | 319 ms: 1.04x slower                                                  |
| logging_silent            | 57.9 ns                                                             | 60.1 ns: 1.04x slower                                                 |
| thrift                    | 9.73 ms                                                             | 10.1 ms: 1.04x slower                                                 |
| json                      | 4.10 ms                                                             | 4.27 ms: 1.04x slower                                                 |
| logging_format            | 8.13 us                                                             | 8.48 us: 1.04x slower                                                 |
| logging_simple            | 7.47 us                                                             | 7.79 us: 1.04x slower                                                 |
| xml_etree_generate        | 59.6 ms                                                             | 62.2 ms: 1.04x slower                                                 |
| deepcopy_reduce           | 2.59 us                                                             | 2.70 us: 1.04x slower                                                 |
| scimark_lu                | 59.4 ms                                                             | 62.0 ms: 1.05x slower                                                 |
| async_generators          | 266 ms                                                              | 278 ms: 1.05x slower                                                  |
| deltablue                 | 2.23 ms                                                             | 2.34 ms: 1.05x slower                                                 |
| 2to3                      | 233 ms                                                              | 245 ms: 1.05x slower                                                  |
| bench_mp_pool             | 69.4 ms                                                             | 73.1 ms: 1.05x slower                                                 |
| comprehensions            | 11.9 us                                                             | 12.5 us: 1.05x slower                                                 |
| unpickle_pure_python      | 147 us                                                              | 155 us: 1.06x slower                                                  |
| coverage                  | 307 ms                                                              | 324 ms: 1.06x slower                                                  |
| pathlib                   | 83.9 ms                                                             | 88.7 ms: 1.06x slower                                                 |
| fannkuch                  | 270 ms                                                              | 286 ms: 1.06x slower                                                  |
| deepcopy_memo             | 23.5 us                                                             | 24.9 us: 1.06x slower                                                 |
| richards_super            | 35.5 ms                                                             | 37.7 ms: 1.06x slower                                                 |
| xml_etree_process         | 42.1 ms                                                             | 44.9 ms: 1.07x slower                                                 |
| richards                  | 31.2 ms                                                             | 33.3 ms: 1.07x slower                                                 |
| pickle_pure_python        | 213 us                                                              | 228 us: 1.07x slower                                                  |
| go                        | 101 ms                                                              | 108 ms: 1.07x slower                                                  |
| scimark_sor               | 81.0 ms                                                             | 87.5 ms: 1.08x slower                                                 |
| asyncio_tcp               | 662 ms                                                              | 717 ms: 1.08x slower                                                  |
| hexiom                    | 4.23 ms                                                             | 4.58 ms: 1.08x slower                                                 |
| python_startup            | 22.2 ms                                                             | 24.2 ms: 1.09x slower                                                 |
| telco                     | 6.03 ms                                                             | 6.56 ms: 1.09x slower                                                 |
| scimark_monte_carlo       | 45.2 ms                                                             | 49.2 ms: 1.09x slower                                                 |
| python_startup_no_site    | 18.2 ms                                                             | 19.9 ms: 1.09x slower                                                 |
| tornado_http              | 94.3 ms                                                             | 104 ms: 1.10x slower                                                  |
| Geometric mean            | (ref)                                                               | 1.03x slower                                                          |

Benchmark hidden because not significant (13): create_gc_cycles, unpickle_list, sympy_str, regex_effbot, json_loads, pprint_safe_repr, tomli_loads, gc_traversal, async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io
Ignored benchmarks (2) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown