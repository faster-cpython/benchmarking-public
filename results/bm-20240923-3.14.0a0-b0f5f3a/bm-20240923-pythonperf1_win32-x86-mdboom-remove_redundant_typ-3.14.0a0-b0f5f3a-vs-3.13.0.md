# Results vs. 3.13.0

- fork: mdboom
- ref: remove_redundant_typ
- machine: windows-x86
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.02x faster
- HPT reliability: 99.85%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 251 ms: 1.01x faster                                                           |
| docutils       | 1.82 sec                                                        | 1.86 sec: 1.02x slower                                                         |
| html5lib       | 48.3 ms                                                         | 45.5 ms: 1.06x faster                                                          |
| tornado_http   | 104 ms                                                          | 95.6 ms: 1.09x faster                                                          |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 650 ms: 1.29x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 250 ms: 1.15x faster                                                           |
| async_tree_none            | 246 ms                                                          | 218 ms: 1.13x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 270 ms: 1.12x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 201 ms: 1.09x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 487 ms: 1.02x faster                                                           |
| async_tree_io_tg           | 509 ms                                                          | 520 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 476 ms: 1.03x slower                                                           |
| async_generators           | 274 ms                                                          | 303 ms: 1.11x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.3 ms: 1.17x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 197 ms: 1.03x faster                                                           |
| float          | 57.8 ms                                                         | 62.7 ms: 1.09x slower                                                          |
| nbody          | 81.9 ms                                                         | 93.0 ms: 1.14x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                          | 117 ms: 1.01x slower                                                           |
| regex_v8       | 15.6 ms                                                         | 16.0 ms: 1.03x slower                                                          |
| regex_compile  | 103 ms                                                          | 108 ms: 1.04x slower                                                           |
| regex_effbot   | 1.81 ms                                                         | 1.89 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle               | 8.42 us                                                         | 7.91 us: 1.06x faster                                                          |
| pickle_dict          | 21.7 us                                                         | 20.8 us: 1.04x faster                                                          |
| unpickle_list        | 3.09 us                                                         | 3.01 us: 1.03x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 107 ms: 1.01x faster                                                           |
| unpickle             | 10.5 us                                                         | 10.4 us: 1.01x faster                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 67.6 ms: 1.04x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 7.70 ms: 1.04x slower                                                          |
| tomli_loads          | 1.73 sec                                                        | 1.85 sec: 1.07x slower                                                         |
| pickle_pure_python   | 238 us                                                          | 260 us: 1.09x slower                                                           |
| unpickle_pure_python | 162 us                                                          | 177 us: 1.09x slower                                                           |
| xml_etree_generate   | 62.6 ms                                                         | 69.1 ms: 1.10x slower                                                          |
| xml_etree_process    | 45.0 ms                                                         | 49.9 ms: 1.11x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                                   |

Benchmark hidden because not significant (2): json_loads, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 23.7 ms: 1.02x faster                                                          |
| python_startup_no_site | 19.9 ms                                                         | 19.7 ms: 1.01x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 47.7 ms: 1.04x faster                                                          |
| genshi_text     | 22.4 ms                                                         | 22.3 ms: 1.01x faster                                                          |
| django_template | 32.7 ms                                                         | 33.2 ms: 1.01x slower                                                          |
| mako            | 7.31 ms                                                         | 8.09 ms: 1.11x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.02x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 779 us: 13.03x faster                                                          |
| coverage                   | 333 ms                                                          | 52.7 ms: 6.31x faster                                                          |
| asyncio_tcp                | 842 ms                                                          | 650 ms: 1.29x faster                                                           |
| deepcopy                   | 307 us                                                          | 245 us: 1.25x faster                                                           |
| deepcopy_memo              | 26.2 us                                                         | 22.5 us: 1.16x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 250 ms: 1.15x faster                                                           |
| async_tree_none            | 246 ms                                                          | 218 ms: 1.13x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 270 ms: 1.12x faster                                                           |
| deepcopy_reduce            | 2.85 us                                                         | 2.60 us: 1.10x faster                                                          |
| tornado_http               | 104 ms                                                          | 95.6 ms: 1.09x faster                                                          |
| async_tree_none_tg         | 219 ms                                                          | 201 ms: 1.09x faster                                                           |
| pathlib                    | 89.4 ms                                                         | 83.9 ms: 1.07x faster                                                          |
| pickle                     | 8.42 us                                                         | 7.91 us: 1.06x faster                                                          |
| html5lib                   | 48.3 ms                                                         | 45.5 ms: 1.06x faster                                                          |
| go                         | 111 ms                                                          | 106 ms: 1.05x faster                                                           |
| pickle_dict                | 21.7 us                                                         | 20.8 us: 1.04x faster                                                          |
| bench_mp_pool              | 74.3 ms                                                         | 71.4 ms: 1.04x faster                                                          |
| genshi_xml                 | 49.5 ms                                                         | 47.7 ms: 1.04x faster                                                          |
| gc_traversal               | 1.45 ms                                                         | 1.41 ms: 1.03x faster                                                          |
| unpickle_list              | 3.09 us                                                         | 3.01 us: 1.03x faster                                                          |
| pidigits                   | 202 ms                                                          | 197 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| python_startup             | 24.3 ms                                                         | 23.7 ms: 1.02x faster                                                          |
| crypto_pyaes               | 58.2 ms                                                         | 57.1 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 487 ms: 1.02x faster                                                           |
| python_startup_no_site     | 19.9 ms                                                         | 19.7 ms: 1.01x faster                                                          |
| xml_etree_parse            | 109 ms                                                          | 107 ms: 1.01x faster                                                           |
| unpickle                   | 10.5 us                                                         | 10.4 us: 1.01x faster                                                          |
| 2to3                       | 253 ms                                                          | 251 ms: 1.01x faster                                                           |
| genshi_text                | 22.4 ms                                                         | 22.3 ms: 1.01x faster                                                          |
| pycparser                  | 869 ms                                                          | 862 ms: 1.01x faster                                                           |
| nqueens                    | 75.1 ms                                                         | 74.6 ms: 1.01x faster                                                          |
| sqlite_synth               | 1.97 us                                                         | 1.98 us: 1.01x slower                                                          |
| regex_dna                  | 117 ms                                                          | 117 ms: 1.01x slower                                                           |
| logging_format             | 8.57 us                                                         | 8.62 us: 1.01x slower                                                          |
| django_template            | 32.7 ms                                                         | 33.2 ms: 1.01x slower                                                          |
| dulwich_log                | 49.7 ms                                                         | 50.6 ms: 1.02x slower                                                          |
| sympy_str                  | 215 ms                                                          | 219 ms: 1.02x slower                                                           |
| telco                      | 6.67 ms                                                         | 6.79 ms: 1.02x slower                                                          |
| async_tree_io_tg           | 509 ms                                                          | 520 ms: 1.02x slower                                                           |
| create_gc_cycles           | 713 us                                                          | 728 us: 1.02x slower                                                           |
| sympy_integrate            | 15.2 ms                                                         | 15.5 ms: 1.02x slower                                                          |
| docutils                   | 1.82 sec                                                        | 1.86 sec: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 476 ms: 1.03x slower                                                           |
| regex_v8                   | 15.6 ms                                                         | 16.0 ms: 1.03x slower                                                          |
| sympy_expand               | 375 ms                                                          | 387 ms: 1.03x slower                                                           |
| mdp                        | 1.67 sec                                                        | 1.73 sec: 1.03x slower                                                         |
| sqlglot_parse              | 1.05 ms                                                         | 1.09 ms: 1.04x slower                                                          |
| sqlglot_transpile          | 1.29 ms                                                         | 1.34 ms: 1.04x slower                                                          |
| xml_etree_iterparse        | 65.1 ms                                                         | 67.6 ms: 1.04x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.70 ms: 1.04x slower                                                          |
| regex_compile              | 103 ms                                                          | 108 ms: 1.04x slower                                                           |
| regex_effbot               | 1.81 ms                                                         | 1.89 ms: 1.04x slower                                                          |
| sqlglot_optimize           | 42.5 ms                                                         | 44.4 ms: 1.04x slower                                                          |
| pylint                     | 225 ms                                                          | 235 ms: 1.05x slower                                                           |
| meteor_contest             | 77.0 ms                                                         | 80.6 ms: 1.05x slower                                                          |
| pprint_safe_repr           | 644 ms                                                          | 676 ms: 1.05x slower                                                           |
| sqlglot_normalize          | 220 ms                                                          | 231 ms: 1.05x slower                                                           |
| unpack_sequence            | 42.9 ns                                                         | 45.3 ns: 1.05x slower                                                          |
| pprint_pformat             | 1.30 sec                                                        | 1.37 sec: 1.06x slower                                                         |
| typing_runtime_protocols   | 136 us                                                          | 144 us: 1.06x slower                                                           |
| spectral_norm              | 71.3 ms                                                         | 75.5 ms: 1.06x slower                                                          |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.09 ms: 1.06x slower                                                          |
| tomli_loads                | 1.73 sec                                                        | 1.85 sec: 1.07x slower                                                         |
| chaos                      | 51.2 ms                                                         | 54.7 ms: 1.07x slower                                                          |
| comprehensions             | 12.7 us                                                         | 13.7 us: 1.08x slower                                                          |
| float                      | 57.8 ms                                                         | 62.7 ms: 1.09x slower                                                          |
| pickle_pure_python         | 238 us                                                          | 260 us: 1.09x slower                                                           |
| unpickle_pure_python       | 162 us                                                          | 177 us: 1.09x slower                                                           |
| scimark_lu                 | 63.5 ms                                                         | 69.6 ms: 1.09x slower                                                          |
| pyflate                    | 326 ms                                                          | 358 ms: 1.10x slower                                                           |
| scimark_sor                | 91.8 ms                                                         | 101 ms: 1.10x slower                                                           |
| xml_etree_generate         | 62.6 ms                                                         | 69.1 ms: 1.10x slower                                                          |
| hexiom                     | 4.64 ms                                                         | 5.13 ms: 1.11x slower                                                          |
| mako                       | 7.31 ms                                                         | 8.09 ms: 1.11x slower                                                          |
| async_generators           | 274 ms                                                          | 303 ms: 1.11x slower                                                           |
| xml_etree_process          | 45.0 ms                                                         | 49.9 ms: 1.11x slower                                                          |
| fannkuch                   | 293 ms                                                          | 326 ms: 1.11x slower                                                           |
| nbody                      | 81.9 ms                                                         | 93.0 ms: 1.14x slower                                                          |
| scimark_fft                | 206 ms                                                          | 236 ms: 1.14x slower                                                           |
| scimark_monte_carlo        | 50.3 ms                                                         | 57.7 ms: 1.15x slower                                                          |
| deltablue                  | 2.41 ms                                                         | 2.76 ms: 1.15x slower                                                          |
| raytrace                   | 205 ms                                                          | 237 ms: 1.15x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.3 ms: 1.17x slower                                                          |
| generators                 | 22.1 ms                                                         | 25.8 ms: 1.17x slower                                                          |
| richards_super             | 38.0 ms                                                         | 44.8 ms: 1.18x slower                                                          |
| logging_silent             | 61.6 ns                                                         | 73.5 ns: 1.19x slower                                                          |
| richards                   | 33.8 ms                                                         | 40.5 ms: 1.20x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (7): json, sympy_sum, json_loads, pickle_list, async_tree_io, logging_simple, bench_thread_pool
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging

# HPT report

- Reliability score: 99.85% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown