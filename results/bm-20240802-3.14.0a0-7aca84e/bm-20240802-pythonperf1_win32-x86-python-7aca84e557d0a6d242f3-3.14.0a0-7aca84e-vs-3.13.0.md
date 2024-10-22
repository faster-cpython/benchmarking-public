# Results vs. 3.13.0

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-x86
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.00x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 264 ms: 1.04x slower                                                           |
| docutils       | 1.82 sec                                                        | 1.96 sec: 1.08x slower                                                         |
| html5lib       | 48.3 ms                                                         | 51.4 ms: 1.07x slower                                                          |
| tornado_http   | 104 ms                                                          | 107 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 256 ms: 1.12x faster                                                           |
| asyncio_tcp                | 842 ms                                                          | 785 ms: 1.07x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 204 ms: 1.07x faster                                                           |
| async_tree_none            | 246 ms                                                          | 232 ms: 1.06x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 287 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 484 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.2 sec: 1.01x faster                                                         |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 472 ms: 1.02x slower                                                           |
| async_tree_io_tg           | 509 ms                                                          | 528 ms: 1.04x slower                                                           |
| async_tree_io              | 537 ms                                                          | 570 ms: 1.06x slower                                                           |
| async_generators           | 274 ms                                                          | 306 ms: 1.12x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 17.7 ms: 1.13x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.00x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 200 ms: 1.01x faster                                                           |
| float          | 57.8 ms                                                         | 61.5 ms: 1.06x slower                                                          |
| nbody          | 81.9 ms                                                         | 102 ms: 1.24x slower                                                           |
| Geometric mean | (ref)                                                           | 1.09x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.6 ms                                                         | 16.4 ms: 1.05x slower                                                          |
| regex_compile  | 103 ms                                                          | 111 ms: 1.08x slower                                                           |
| regex_dna      | 117 ms                                                          | 129 ms: 1.10x slower                                                           |
| regex_effbot   | 1.81 ms                                                         | 2.05 ms: 1.13x slower                                                          |
| Geometric mean | (ref)                                                           | 1.09x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 109 ms                                                          | 105 ms: 1.03x faster                                                           |
| json_loads           | 21.0 us                                                         | 20.8 us: 1.01x faster                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 67.7 ms: 1.04x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 7.71 ms: 1.04x slower                                                          |
| xml_etree_generate   | 62.6 ms                                                         | 65.8 ms: 1.05x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 174 us: 1.07x slower                                                           |
| xml_etree_process    | 45.0 ms                                                         | 49.1 ms: 1.09x slower                                                          |
| tomli_loads          | 1.73 sec                                                        | 1.91 sec: 1.10x slower                                                         |
| pickle_pure_python   | 238 us                                                          | 266 us: 1.12x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 23.7 ms: 1.02x faster                                                          |
| python_startup_no_site | 19.9 ms                                                         | 19.6 ms: 1.02x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 50.4 ms: 1.02x slower                                                          |
| django_template | 32.7 ms                                                         | 34.9 ms: 1.07x slower                                                          |
| genshi_text     | 22.4 ms                                                         | 24.4 ms: 1.09x slower                                                          |
| mako            | 7.31 ms                                                         | 8.31 ms: 1.14x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.08x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 751 us: 13.51x faster                                                          |
| coverage                   | 333 ms                                                          | 52.2 ms: 6.38x faster                                                          |
| deepcopy                   | 307 us                                                          | 264 us: 1.16x faster                                                           |
| deepcopy_memo              | 26.2 us                                                         | 23.0 us: 1.14x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 256 ms: 1.12x faster                                                           |
| asyncio_tcp                | 842 ms                                                          | 785 ms: 1.07x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 204 ms: 1.07x faster                                                           |
| deepcopy_reduce            | 2.85 us                                                         | 2.66 us: 1.07x faster                                                          |
| async_tree_none            | 246 ms                                                          | 232 ms: 1.06x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 287 ms: 1.05x faster                                                           |
| xml_etree_parse            | 109 ms                                                          | 105 ms: 1.03x faster                                                           |
| python_startup             | 24.3 ms                                                         | 23.7 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 484 ms: 1.02x faster                                                           |
| python_startup_no_site     | 19.9 ms                                                         | 19.6 ms: 1.02x faster                                                          |
| pidigits                   | 202 ms                                                          | 200 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.2 sec: 1.01x faster                                                         |
| telco                      | 6.67 ms                                                         | 6.60 ms: 1.01x faster                                                          |
| json_loads                 | 21.0 us                                                         | 20.8 us: 1.01x faster                                                          |
| gc_traversal               | 1.45 ms                                                         | 1.44 ms: 1.01x faster                                                          |
| genshi_xml                 | 49.5 ms                                                         | 50.4 ms: 1.02x slower                                                          |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 472 ms: 1.02x slower                                                           |
| tornado_http               | 104 ms                                                          | 107 ms: 1.02x slower                                                           |
| crypto_pyaes               | 58.2 ms                                                         | 59.8 ms: 1.03x slower                                                          |
| async_tree_io_tg           | 509 ms                                                          | 528 ms: 1.04x slower                                                           |
| dulwich_log                | 49.7 ms                                                         | 51.6 ms: 1.04x slower                                                          |
| xml_etree_iterparse        | 65.1 ms                                                         | 67.7 ms: 1.04x slower                                                          |
| sqlglot_normalize          | 220 ms                                                          | 229 ms: 1.04x slower                                                           |
| sympy_sum                  | 108 ms                                                          | 112 ms: 1.04x slower                                                           |
| json_dumps                 | 7.40 ms                                                         | 7.71 ms: 1.04x slower                                                          |
| 2to3                       | 253 ms                                                          | 264 ms: 1.04x slower                                                           |
| sympy_str                  | 215 ms                                                          | 225 ms: 1.05x slower                                                           |
| sympy_expand               | 375 ms                                                          | 392 ms: 1.05x slower                                                           |
| logging_format             | 8.57 us                                                         | 8.98 us: 1.05x slower                                                          |
| logging_simple             | 7.87 us                                                         | 8.27 us: 1.05x slower                                                          |
| sqlglot_optimize           | 42.5 ms                                                         | 44.6 ms: 1.05x slower                                                          |
| xml_etree_generate         | 62.6 ms                                                         | 65.8 ms: 1.05x slower                                                          |
| nqueens                    | 75.1 ms                                                         | 79.0 ms: 1.05x slower                                                          |
| regex_v8                   | 15.6 ms                                                         | 16.4 ms: 1.05x slower                                                          |
| mdp                        | 1.67 sec                                                        | 1.76 sec: 1.05x slower                                                         |
| pycparser                  | 869 ms                                                          | 918 ms: 1.06x slower                                                           |
| create_gc_cycles           | 713 us                                                          | 753 us: 1.06x slower                                                           |
| sympy_integrate            | 15.2 ms                                                         | 16.1 ms: 1.06x slower                                                          |
| pprint_safe_repr           | 644 ms                                                          | 685 ms: 1.06x slower                                                           |
| async_tree_io              | 537 ms                                                          | 570 ms: 1.06x slower                                                           |
| float                      | 57.8 ms                                                         | 61.5 ms: 1.06x slower                                                          |
| html5lib                   | 48.3 ms                                                         | 51.4 ms: 1.07x slower                                                          |
| pylint                     | 225 ms                                                          | 239 ms: 1.07x slower                                                           |
| django_template            | 32.7 ms                                                         | 34.9 ms: 1.07x slower                                                          |
| sqlglot_parse              | 1.05 ms                                                         | 1.12 ms: 1.07x slower                                                          |
| chaos                      | 51.2 ms                                                         | 54.7 ms: 1.07x slower                                                          |
| sqlglot_transpile          | 1.29 ms                                                         | 1.38 ms: 1.07x slower                                                          |
| pprint_pformat             | 1.30 sec                                                        | 1.39 sec: 1.07x slower                                                         |
| unpickle_pure_python       | 162 us                                                          | 174 us: 1.07x slower                                                           |
| regex_compile              | 103 ms                                                          | 111 ms: 1.08x slower                                                           |
| docutils                   | 1.82 sec                                                        | 1.96 sec: 1.08x slower                                                         |
| genshi_text                | 22.4 ms                                                         | 24.4 ms: 1.09x slower                                                          |
| meteor_contest             | 77.0 ms                                                         | 83.9 ms: 1.09x slower                                                          |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.17 ms: 1.09x slower                                                          |
| xml_etree_process          | 45.0 ms                                                         | 49.1 ms: 1.09x slower                                                          |
| spectral_norm              | 71.3 ms                                                         | 78.0 ms: 1.09x slower                                                          |
| scimark_sor                | 91.8 ms                                                         | 101 ms: 1.10x slower                                                           |
| regex_dna                  | 117 ms                                                          | 129 ms: 1.10x slower                                                           |
| tomli_loads                | 1.73 sec                                                        | 1.91 sec: 1.10x slower                                                         |
| pyflate                    | 326 ms                                                          | 360 ms: 1.11x slower                                                           |
| comprehensions             | 12.7 us                                                         | 14.1 us: 1.11x slower                                                          |
| fannkuch                   | 293 ms                                                          | 325 ms: 1.11x slower                                                           |
| go                         | 111 ms                                                          | 124 ms: 1.11x slower                                                           |
| typing_runtime_protocols   | 136 us                                                          | 152 us: 1.12x slower                                                           |
| pickle_pure_python         | 238 us                                                          | 266 us: 1.12x slower                                                           |
| async_generators           | 274 ms                                                          | 306 ms: 1.12x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 17.7 ms: 1.13x slower                                                          |
| regex_effbot               | 1.81 ms                                                         | 2.05 ms: 1.13x slower                                                          |
| mako                       | 7.31 ms                                                         | 8.31 ms: 1.14x slower                                                          |
| scimark_fft                | 206 ms                                                          | 235 ms: 1.14x slower                                                           |
| scimark_lu                 | 63.5 ms                                                         | 72.4 ms: 1.14x slower                                                          |
| scimark_monte_carlo        | 50.3 ms                                                         | 58.2 ms: 1.16x slower                                                          |
| hexiom                     | 4.64 ms                                                         | 5.40 ms: 1.16x slower                                                          |
| raytrace                   | 205 ms                                                          | 241 ms: 1.17x slower                                                           |
| deltablue                  | 2.41 ms                                                         | 2.84 ms: 1.18x slower                                                          |
| logging_silent             | 61.6 ns                                                         | 75.3 ns: 1.22x slower                                                          |
| nbody                      | 81.9 ms                                                         | 102 ms: 1.24x slower                                                           |
| richards_super             | 38.0 ms                                                         | 47.4 ms: 1.25x slower                                                          |
| generators                 | 22.1 ms                                                         | 27.9 ms: 1.26x slower                                                          |
| richards                   | 33.8 ms                                                         | 43.7 ms: 1.29x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.00x slower                                                                   |

Benchmark hidden because not significant (4): bench_thread_pool, pathlib, bench_mp_pool, json
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown