# Results vs. 3.13.0

- fork: python
- ref: c8db0e817e7e0db50153
- machine: windows-x86
- commit hash: c8db0e8
- commit date: 2024-10-03
- overall geometric mean: 1.01x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 250 ms: 1.01x faster                                                           |
| docutils       | 1.82 sec                                                        | 1.87 sec: 1.03x slower                                                         |
| html5lib       | 48.3 ms                                                         | 46.2 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 669 ms: 1.26x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 257 ms: 1.12x faster                                                           |
| async_tree_none            | 246 ms                                                          | 220 ms: 1.12x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 276 ms: 1.09x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 202 ms: 1.08x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.1 sec: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 475 ms: 1.03x slower                                                           |
| async_tree_io_tg           | 509 ms                                                          | 527 ms: 1.03x slower                                                           |
| async_generators           | 274 ms                                                          | 302 ms: 1.10x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.5 ms: 1.18x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 200 ms: 1.01x faster                                                           |
| float          | 57.8 ms                                                         | 61.7 ms: 1.07x slower                                                          |
| nbody          | 81.9 ms                                                         | 91.6 ms: 1.12x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                          | 120 ms: 1.03x slower                                                           |
| regex_v8       | 15.6 ms                                                         | 16.2 ms: 1.04x slower                                                          |
| regex_effbot   | 1.81 ms                                                         | 1.92 ms: 1.06x slower                                                          |
| regex_compile  | 103 ms                                                          | 110 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_dict          | 21.7 us                                                         | 20.7 us: 1.05x faster                                                          |
| unpickle_list        | 3.09 us                                                         | 3.00 us: 1.03x faster                                                          |
| pickle               | 8.42 us                                                         | 8.18 us: 1.03x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 108 ms: 1.01x faster                                                           |
| unpickle             | 10.5 us                                                         | 10.4 us: 1.01x faster                                                          |
| pickle_list          | 3.40 us                                                         | 3.41 us: 1.00x slower                                                          |
| json_loads           | 21.0 us                                                         | 21.3 us: 1.01x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 7.54 ms: 1.02x slower                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 68.0 ms: 1.04x slower                                                          |
| xml_etree_generate   | 62.6 ms                                                         | 69.1 ms: 1.10x slower                                                          |
| tomli_loads          | 1.73 sec                                                        | 1.92 sec: 1.11x slower                                                         |
| xml_etree_process    | 45.0 ms                                                         | 50.7 ms: 1.13x slower                                                          |
| pickle_pure_python   | 238 us                                                          | 268 us: 1.13x slower                                                           |
| unpickle_pure_python | 162 us                                                          | 183 us: 1.13x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 19.7 ms: 1.01x faster                                                          |
| python_startup         | 24.3 ms                                                         | 24.1 ms: 1.01x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 48.7 ms: 1.02x faster                                                          |
| genshi_text     | 22.4 ms                                                         | 22.6 ms: 1.01x slower                                                          |
| django_template | 32.7 ms                                                         | 34.3 ms: 1.05x slower                                                          |
| mako            | 7.31 ms                                                         | 8.12 ms: 1.11x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.04x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 769 us: 13.19x faster                                                          |
| coverage                   | 333 ms                                                          | 53.6 ms: 6.21x faster                                                          |
| asyncio_tcp                | 842 ms                                                          | 669 ms: 1.26x faster                                                           |
| deepcopy                   | 307 us                                                          | 247 us: 1.24x faster                                                           |
| deepcopy_memo              | 26.2 us                                                         | 22.9 us: 1.15x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 257 ms: 1.12x faster                                                           |
| async_tree_none            | 246 ms                                                          | 220 ms: 1.12x faster                                                           |
| deepcopy_reduce            | 2.85 us                                                         | 2.58 us: 1.10x faster                                                          |
| async_tree_memoization     | 302 ms                                                          | 276 ms: 1.09x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 202 ms: 1.08x faster                                                           |
| pickle_dict                | 21.7 us                                                         | 20.7 us: 1.05x faster                                                          |
| html5lib                   | 48.3 ms                                                         | 46.2 ms: 1.04x faster                                                          |
| pathlib                    | 89.4 ms                                                         | 86.5 ms: 1.03x faster                                                          |
| unpickle_list              | 3.09 us                                                         | 3.00 us: 1.03x faster                                                          |
| pickle                     | 8.42 us                                                         | 8.18 us: 1.03x faster                                                          |
| telco                      | 6.67 ms                                                         | 6.48 ms: 1.03x faster                                                          |
| bench_mp_pool              | 74.3 ms                                                         | 72.9 ms: 1.02x faster                                                          |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.1 sec: 1.02x faster                                                         |
| gc_traversal               | 1.45 ms                                                         | 1.43 ms: 1.02x faster                                                          |
| genshi_xml                 | 49.5 ms                                                         | 48.7 ms: 1.02x faster                                                          |
| go                         | 111 ms                                                          | 110 ms: 1.01x faster                                                           |
| 2to3                       | 253 ms                                                          | 250 ms: 1.01x faster                                                           |
| python_startup_no_site     | 19.9 ms                                                         | 19.7 ms: 1.01x faster                                                          |
| pidigits                   | 202 ms                                                          | 200 ms: 1.01x faster                                                           |
| xml_etree_parse            | 109 ms                                                          | 108 ms: 1.01x faster                                                           |
| unpickle                   | 10.5 us                                                         | 10.4 us: 1.01x faster                                                          |
| pycparser                  | 869 ms                                                          | 861 ms: 1.01x faster                                                           |
| python_startup             | 24.3 ms                                                         | 24.1 ms: 1.01x faster                                                          |
| crypto_pyaes               | 58.2 ms                                                         | 57.8 ms: 1.01x faster                                                          |
| pickle_list                | 3.40 us                                                         | 3.41 us: 1.00x slower                                                          |
| sqlite_synth               | 1.97 us                                                         | 1.98 us: 1.01x slower                                                          |
| genshi_text                | 22.4 ms                                                         | 22.6 ms: 1.01x slower                                                          |
| sympy_str                  | 215 ms                                                          | 218 ms: 1.01x slower                                                           |
| json_loads                 | 21.0 us                                                         | 21.3 us: 1.01x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.54 ms: 1.02x slower                                                          |
| sqlglot_parse              | 1.05 ms                                                         | 1.07 ms: 1.02x slower                                                          |
| sqlglot_transpile          | 1.29 ms                                                         | 1.32 ms: 1.02x slower                                                          |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 475 ms: 1.03x slower                                                           |
| create_gc_cycles           | 713 us                                                          | 732 us: 1.03x slower                                                           |
| sympy_expand               | 375 ms                                                          | 385 ms: 1.03x slower                                                           |
| docutils                   | 1.82 sec                                                        | 1.87 sec: 1.03x slower                                                         |
| sympy_integrate            | 15.2 ms                                                         | 15.7 ms: 1.03x slower                                                          |
| regex_dna                  | 117 ms                                                          | 120 ms: 1.03x slower                                                           |
| async_tree_io_tg           | 509 ms                                                          | 527 ms: 1.03x slower                                                           |
| meteor_contest             | 77.0 ms                                                         | 79.8 ms: 1.04x slower                                                          |
| logging_simple             | 7.87 us                                                         | 8.18 us: 1.04x slower                                                          |
| regex_v8                   | 15.6 ms                                                         | 16.2 ms: 1.04x slower                                                          |
| logging_format             | 8.57 us                                                         | 8.92 us: 1.04x slower                                                          |
| xml_etree_iterparse        | 65.1 ms                                                         | 68.0 ms: 1.04x slower                                                          |
| pylint                     | 225 ms                                                          | 236 ms: 1.05x slower                                                           |
| django_template            | 32.7 ms                                                         | 34.3 ms: 1.05x slower                                                          |
| pprint_safe_repr           | 644 ms                                                          | 680 ms: 1.06x slower                                                           |
| dulwich_log                | 49.7 ms                                                         | 52.5 ms: 1.06x slower                                                          |
| mdp                        | 1.67 sec                                                        | 1.77 sec: 1.06x slower                                                         |
| regex_effbot               | 1.81 ms                                                         | 1.92 ms: 1.06x slower                                                          |
| regex_compile              | 103 ms                                                          | 110 ms: 1.07x slower                                                           |
| fannkuch                   | 293 ms                                                          | 313 ms: 1.07x slower                                                           |
| float                      | 57.8 ms                                                         | 61.7 ms: 1.07x slower                                                          |
| sqlglot_optimize           | 42.5 ms                                                         | 45.5 ms: 1.07x slower                                                          |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.11 ms: 1.07x slower                                                          |
| sqlglot_normalize          | 220 ms                                                          | 236 ms: 1.07x slower                                                           |
| pprint_pformat             | 1.30 sec                                                        | 1.40 sec: 1.08x slower                                                         |
| scimark_sor                | 91.8 ms                                                         | 99.0 ms: 1.08x slower                                                          |
| typing_runtime_protocols   | 136 us                                                          | 148 us: 1.08x slower                                                           |
| unpack_sequence            | 42.9 ns                                                         | 46.7 ns: 1.09x slower                                                          |
| scimark_lu                 | 63.5 ms                                                         | 69.2 ms: 1.09x slower                                                          |
| comprehensions             | 12.7 us                                                         | 14.0 us: 1.10x slower                                                          |
| scimark_monte_carlo        | 50.3 ms                                                         | 55.3 ms: 1.10x slower                                                          |
| chaos                      | 51.2 ms                                                         | 56.2 ms: 1.10x slower                                                          |
| spectral_norm              | 71.3 ms                                                         | 78.5 ms: 1.10x slower                                                          |
| async_generators           | 274 ms                                                          | 302 ms: 1.10x slower                                                           |
| xml_etree_generate         | 62.6 ms                                                         | 69.1 ms: 1.10x slower                                                          |
| tomli_loads                | 1.73 sec                                                        | 1.92 sec: 1.11x slower                                                         |
| mako                       | 7.31 ms                                                         | 8.12 ms: 1.11x slower                                                          |
| nbody                      | 81.9 ms                                                         | 91.6 ms: 1.12x slower                                                          |
| xml_etree_process          | 45.0 ms                                                         | 50.7 ms: 1.13x slower                                                          |
| pickle_pure_python         | 238 us                                                          | 268 us: 1.13x slower                                                           |
| hexiom                     | 4.64 ms                                                         | 5.23 ms: 1.13x slower                                                          |
| scimark_fft                | 206 ms                                                          | 233 ms: 1.13x slower                                                           |
| unpickle_pure_python       | 162 us                                                          | 183 us: 1.13x slower                                                           |
| pyflate                    | 326 ms                                                          | 370 ms: 1.13x slower                                                           |
| deltablue                  | 2.41 ms                                                         | 2.82 ms: 1.17x slower                                                          |
| coroutines                 | 15.7 ms                                                         | 18.5 ms: 1.18x slower                                                          |
| generators                 | 22.1 ms                                                         | 26.7 ms: 1.21x slower                                                          |
| logging_silent             | 61.6 ns                                                         | 74.7 ns: 1.21x slower                                                          |
| richards_super             | 38.0 ms                                                         | 46.2 ms: 1.22x slower                                                          |
| richards                   | 33.8 ms                                                         | 41.4 ms: 1.22x slower                                                          |
| raytrace                   | 205 ms                                                          | 260 ms: 1.27x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (7): bench_thread_pool, async_tree_cpu_io_mixed, nqueens, sympy_sum, json, tornado_http, async_tree_io
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown