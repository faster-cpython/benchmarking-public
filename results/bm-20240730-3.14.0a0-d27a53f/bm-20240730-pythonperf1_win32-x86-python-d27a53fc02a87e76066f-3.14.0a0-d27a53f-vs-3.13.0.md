# Results vs. 3.13.0

- fork: python
- ref: d27a53fc02a87e76066f
- machine: windows-x86
- commit hash: d27a53f
- commit date: 2024-07-30
- overall geometric mean: 1.05x faster
- HPT reliability: 94.33%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 251 ms: 1.01x faster                                                           |
| docutils       | 1.82 sec                                                        | 1.91 sec: 1.05x slower                                                         |
| html5lib       | 48.3 ms                                                         | 47.8 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 719 ms: 1.17x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 246 ms: 1.17x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 195 ms: 1.12x faster                                                           |
| async_tree_none            | 246 ms                                                          | 224 ms: 1.10x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 276 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 467 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 454 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| async_generators           | 274 ms                                                          | 280 ms: 1.02x slower                                                           |
| async_tree_io              | 537 ms                                                          | 549 ms: 1.02x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 17.3 ms: 1.10x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 199 ms: 1.02x faster                                                           |
| float          | 57.8 ms                                                         | 58.2 ms: 1.01x slower                                                          |
| nbody          | 81.9 ms                                                         | 88.5 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                          | 122 ms: 1.04x slower                                                           |
| regex_v8       | 15.6 ms                                                         | 16.3 ms: 1.04x slower                                                          |
| regex_effbot   | 1.81 ms                                                         | 1.91 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.0 us                                                         | 20.0 us: 1.05x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 107 ms: 1.02x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.53 ms: 1.02x slower                                                          |
| pickle_pure_python   | 238 us                                                          | 244 us: 1.02x slower                                                           |
| unpickle_pure_python | 162 us                                                          | 169 us: 1.04x slower                                                           |
| xml_etree_process    | 45.0 ms                                                         | 47.3 ms: 1.05x slower                                                          |
| tomli_loads          | 1.73 sec                                                        | 1.82 sec: 1.05x slower                                                         |
| xml_etree_iterparse  | 65.1 ms                                                         | 69.2 ms: 1.06x slower                                                          |
| xml_etree_generate   | 62.6 ms                                                         | 66.8 ms: 1.07x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 23.7 ms: 1.02x faster                                                          |
| python_startup_no_site | 19.9 ms                                                         | 19.7 ms: 1.01x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 46.4 ms: 1.07x faster                                                          |
| genshi_text     | 22.4 ms                                                         | 21.6 ms: 1.04x faster                                                          |
| django_template | 32.7 ms                                                         | 34.7 ms: 1.06x slower                                                          |
| mako            | 7.31 ms                                                         | 8.01 ms: 1.10x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240730-pythonperf1_win32-x86-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 733 us: 13.85x faster                                                          |
| coverage                   | 333 ms                                                          | 51.8 ms: 6.43x faster                                                          |
| deepcopy                   | 307 us                                                          | 241 us: 1.27x faster                                                           |
| deepcopy_memo              | 26.2 us                                                         | 21.1 us: 1.24x faster                                                          |
| asyncio_tcp                | 842 ms                                                          | 719 ms: 1.17x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 246 ms: 1.17x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 195 ms: 1.12x faster                                                           |
| deepcopy_reduce            | 2.85 us                                                         | 2.55 us: 1.12x faster                                                          |
| async_tree_none            | 246 ms                                                          | 224 ms: 1.10x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 276 ms: 1.09x faster                                                           |
| telco                      | 6.67 ms                                                         | 6.15 ms: 1.08x faster                                                          |
| genshi_xml                 | 49.5 ms                                                         | 46.4 ms: 1.07x faster                                                          |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 467 ms: 1.06x faster                                                           |
| json_loads                 | 21.0 us                                                         | 20.0 us: 1.05x faster                                                          |
| crypto_pyaes               | 58.2 ms                                                         | 55.9 ms: 1.04x faster                                                          |
| pycparser                  | 869 ms                                                          | 836 ms: 1.04x faster                                                           |
| genshi_text                | 22.4 ms                                                         | 21.6 ms: 1.04x faster                                                          |
| bench_thread_pool          | 1.02 ms                                                         | 986 us: 1.04x faster                                                           |
| python_startup             | 24.3 ms                                                         | 23.7 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 454 ms: 1.02x faster                                                           |
| xml_etree_parse            | 109 ms                                                          | 107 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| nqueens                    | 75.1 ms                                                         | 73.9 ms: 1.02x faster                                                          |
| pidigits                   | 202 ms                                                          | 199 ms: 1.02x faster                                                           |
| python_startup_no_site     | 19.9 ms                                                         | 19.7 ms: 1.01x faster                                                          |
| chaos                      | 51.2 ms                                                         | 50.5 ms: 1.01x faster                                                          |
| gc_traversal               | 1.45 ms                                                         | 1.43 ms: 1.01x faster                                                          |
| bench_mp_pool              | 74.3 ms                                                         | 73.4 ms: 1.01x faster                                                          |
| html5lib                   | 48.3 ms                                                         | 47.8 ms: 1.01x faster                                                          |
| pathlib                    | 89.4 ms                                                         | 88.6 ms: 1.01x faster                                                          |
| 2to3                       | 253 ms                                                          | 251 ms: 1.01x faster                                                           |
| go                         | 111 ms                                                          | 111 ms: 1.01x faster                                                           |
| dulwich_log                | 49.7 ms                                                         | 49.4 ms: 1.01x faster                                                          |
| meteor_contest             | 77.0 ms                                                         | 76.7 ms: 1.00x faster                                                          |
| mdp                        | 1.67 sec                                                        | 1.67 sec: 1.00x faster                                                         |
| float                      | 57.8 ms                                                         | 58.2 ms: 1.01x slower                                                          |
| sympy_sum                  | 108 ms                                                          | 109 ms: 1.01x slower                                                           |
| sqlglot_transpile          | 1.29 ms                                                         | 1.30 ms: 1.01x slower                                                          |
| sqlglot_parse              | 1.05 ms                                                         | 1.06 ms: 1.01x slower                                                          |
| sympy_str                  | 215 ms                                                          | 217 ms: 1.01x slower                                                           |
| sympy_integrate            | 15.2 ms                                                         | 15.4 ms: 1.01x slower                                                          |
| pyflate                    | 326 ms                                                          | 331 ms: 1.02x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 7.53 ms: 1.02x slower                                                          |
| pprint_safe_repr           | 644 ms                                                          | 657 ms: 1.02x slower                                                           |
| async_generators           | 274 ms                                                          | 280 ms: 1.02x slower                                                           |
| async_tree_io              | 537 ms                                                          | 549 ms: 1.02x slower                                                           |
| pickle_pure_python         | 238 us                                                          | 244 us: 1.02x slower                                                           |
| sympy_expand               | 375 ms                                                          | 385 ms: 1.03x slower                                                           |
| comprehensions             | 12.7 us                                                         | 13.1 us: 1.03x slower                                                          |
| logging_simple             | 7.87 us                                                         | 8.12 us: 1.03x slower                                                          |
| scimark_sor                | 91.8 ms                                                         | 94.8 ms: 1.03x slower                                                          |
| sqlglot_optimize           | 42.5 ms                                                         | 44.0 ms: 1.04x slower                                                          |
| logging_format             | 8.57 us                                                         | 8.87 us: 1.04x slower                                                          |
| pprint_pformat             | 1.30 sec                                                        | 1.34 sec: 1.04x slower                                                         |
| pylint                     | 225 ms                                                          | 233 ms: 1.04x slower                                                           |
| regex_dna                  | 117 ms                                                          | 122 ms: 1.04x slower                                                           |
| sqlglot_normalize          | 220 ms                                                          | 230 ms: 1.04x slower                                                           |
| regex_v8                   | 15.6 ms                                                         | 16.3 ms: 1.04x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 169 us: 1.04x slower                                                           |
| scimark_fft                | 206 ms                                                          | 217 ms: 1.05x slower                                                           |
| xml_etree_process          | 45.0 ms                                                         | 47.3 ms: 1.05x slower                                                          |
| tomli_loads                | 1.73 sec                                                        | 1.82 sec: 1.05x slower                                                         |
| docutils                   | 1.82 sec                                                        | 1.91 sec: 1.05x slower                                                         |
| fannkuch                   | 293 ms                                                          | 310 ms: 1.06x slower                                                           |
| regex_effbot               | 1.81 ms                                                         | 1.91 ms: 1.06x slower                                                          |
| richards_super             | 38.0 ms                                                         | 40.2 ms: 1.06x slower                                                          |
| richards                   | 33.8 ms                                                         | 35.8 ms: 1.06x slower                                                          |
| django_template            | 32.7 ms                                                         | 34.7 ms: 1.06x slower                                                          |
| create_gc_cycles           | 713 us                                                          | 758 us: 1.06x slower                                                           |
| xml_etree_iterparse        | 65.1 ms                                                         | 69.2 ms: 1.06x slower                                                          |
| raytrace                   | 205 ms                                                          | 218 ms: 1.06x slower                                                           |
| xml_etree_generate         | 62.6 ms                                                         | 66.8 ms: 1.07x slower                                                          |
| deltablue                  | 2.41 ms                                                         | 2.57 ms: 1.07x slower                                                          |
| spectral_norm              | 71.3 ms                                                         | 76.5 ms: 1.07x slower                                                          |
| hexiom                     | 4.64 ms                                                         | 4.99 ms: 1.08x slower                                                          |
| nbody                      | 81.9 ms                                                         | 88.5 ms: 1.08x slower                                                          |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.14 ms: 1.08x slower                                                          |
| mako                       | 7.31 ms                                                         | 8.01 ms: 1.10x slower                                                          |
| coroutines                 | 15.7 ms                                                         | 17.3 ms: 1.10x slower                                                          |
| scimark_lu                 | 63.5 ms                                                         | 70.1 ms: 1.10x slower                                                          |
| generators                 | 22.1 ms                                                         | 25.7 ms: 1.16x slower                                                          |
| logging_silent             | 61.6 ns                                                         | 74.2 ns: 1.20x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (6): tornado_http, json, regex_compile, typing_runtime_protocols, async_tree_io_tg, scimark_monte_carlo
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 94.33% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown