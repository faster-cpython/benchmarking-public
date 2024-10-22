# Results vs. 3.13.0

- fork: python
- ref: e256a7590a0149feadfe
- machine: windows-x86
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.02x faster
- HPT reliability: 99.52%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 249 ms: 1.01x faster                                                           |
| docutils       | 1.82 sec                                                        | 1.87 sec: 1.03x slower                                                         |
| html5lib       | 48.3 ms                                                         | 46.5 ms: 1.04x faster                                                          |
| tornado_http   | 104 ms                                                          | 94.9 ms: 1.10x faster                                                          |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 662 ms: 1.27x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.13x faster                                                           |
| async_tree_none            | 246 ms                                                          | 218 ms: 1.13x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 273 ms: 1.11x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 201 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 464 ms: 1.06x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 455 ms: 1.02x faster                                                           |
| async_tree_io_tg           | 509 ms                                                          | 518 ms: 1.02x slower                                                           |
| async_generators           | 274 ms                                                          | 301 ms: 1.10x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.0 ms: 1.15x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 197 ms: 1.02x faster                                                           |
| float          | 57.8 ms                                                         | 62.8 ms: 1.09x slower                                                          |
| nbody          | 81.9 ms                                                         | 93.0 ms: 1.14x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                          | 121 ms: 1.03x slower                                                           |
| regex_v8       | 15.6 ms                                                         | 16.2 ms: 1.04x slower                                                          |
| regex_effbot   | 1.81 ms                                                         | 1.90 ms: 1.05x slower                                                          |
| regex_compile  | 103 ms                                                          | 109 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle               | 8.42 us                                                         | 7.94 us: 1.06x faster                                                          |
| pickle_dict          | 21.7 us                                                         | 20.6 us: 1.05x faster                                                          |
| unpickle_list        | 3.09 us                                                         | 3.00 us: 1.03x faster                                                          |
| unpickle             | 10.5 us                                                         | 10.3 us: 1.03x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 107 ms: 1.01x faster                                                           |
| pickle_list          | 3.40 us                                                         | 3.35 us: 1.01x faster                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 67.5 ms: 1.04x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 7.68 ms: 1.04x slower                                                          |
| tomli_loads          | 1.73 sec                                                        | 1.85 sec: 1.07x slower                                                         |
| xml_etree_generate   | 62.6 ms                                                         | 67.5 ms: 1.08x slower                                                          |
| xml_etree_process    | 45.0 ms                                                         | 49.4 ms: 1.10x slower                                                          |
| pickle_pure_python   | 238 us                                                          | 262 us: 1.10x slower                                                           |
| unpickle_pure_python | 162 us                                                          | 180 us: 1.12x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 23.5 ms: 1.03x faster                                                          |
| python_startup_no_site | 19.9 ms                                                         | 19.4 ms: 1.03x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.03x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 50.3 ms: 1.01x slower                                                          |
| django_template | 32.7 ms                                                         | 33.6 ms: 1.03x slower                                                          |
| genshi_text     | 22.4 ms                                                         | 24.2 ms: 1.08x slower                                                          |
| mako            | 7.31 ms                                                         | 8.16 ms: 1.12x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.06x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 746 us: 13.60x faster                                                          |
| coverage                   | 333 ms                                                          | 53.2 ms: 6.26x faster                                                          |
| asyncio_tcp                | 842 ms                                                          | 662 ms: 1.27x faster                                                           |
| deepcopy                   | 307 us                                                          | 250 us: 1.23x faster                                                           |
| deepcopy_memo              | 26.2 us                                                         | 22.6 us: 1.16x faster                                                          |
| deepcopy_reduce            | 2.85 us                                                         | 2.50 us: 1.14x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.13x faster                                                           |
| async_tree_none            | 246 ms                                                          | 218 ms: 1.13x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 273 ms: 1.11x faster                                                           |
| tornado_http               | 104 ms                                                          | 94.9 ms: 1.10x faster                                                          |
| async_tree_none_tg         | 219 ms                                                          | 201 ms: 1.09x faster                                                           |
| pathlib                    | 89.4 ms                                                         | 83.5 ms: 1.07x faster                                                          |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 464 ms: 1.06x faster                                                           |
| bench_mp_pool              | 74.3 ms                                                         | 69.9 ms: 1.06x faster                                                          |
| pickle                     | 8.42 us                                                         | 7.94 us: 1.06x faster                                                          |
| pickle_dict                | 21.7 us                                                         | 20.6 us: 1.05x faster                                                          |
| go                         | 111 ms                                                          | 107 ms: 1.04x faster                                                           |
| html5lib                   | 48.3 ms                                                         | 46.5 ms: 1.04x faster                                                          |
| unpickle_list              | 3.09 us                                                         | 3.00 us: 1.03x faster                                                          |
| python_startup             | 24.3 ms                                                         | 23.5 ms: 1.03x faster                                                          |
| unpickle                   | 10.5 us                                                         | 10.3 us: 1.03x faster                                                          |
| gc_traversal               | 1.45 ms                                                         | 1.42 ms: 1.03x faster                                                          |
| python_startup_no_site     | 19.9 ms                                                         | 19.4 ms: 1.03x faster                                                          |
| pidigits                   | 202 ms                                                          | 197 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 455 ms: 1.02x faster                                                           |
| crypto_pyaes               | 58.2 ms                                                         | 57.2 ms: 1.02x faster                                                          |
| 2to3                       | 253 ms                                                          | 249 ms: 1.01x faster                                                           |
| xml_etree_parse            | 109 ms                                                          | 107 ms: 1.01x faster                                                           |
| pickle_list                | 3.40 us                                                         | 3.35 us: 1.01x faster                                                          |
| mdp                        | 1.67 sec                                                        | 1.66 sec: 1.01x faster                                                         |
| telco                      | 6.67 ms                                                         | 6.61 ms: 1.01x faster                                                          |
| sqlite_synth               | 1.97 us                                                         | 1.98 us: 1.01x slower                                                          |
| logging_simple             | 7.87 us                                                         | 7.93 us: 1.01x slower                                                          |
| sympy_integrate            | 15.2 ms                                                         | 15.3 ms: 1.01x slower                                                          |
| pycparser                  | 869 ms                                                          | 877 ms: 1.01x slower                                                           |
| logging_format             | 8.57 us                                                         | 8.66 us: 1.01x slower                                                          |
| genshi_xml                 | 49.5 ms                                                         | 50.3 ms: 1.01x slower                                                          |
| async_tree_io_tg           | 509 ms                                                          | 518 ms: 1.02x slower                                                           |
| sympy_expand               | 375 ms                                                          | 381 ms: 1.02x slower                                                           |
| create_gc_cycles           | 713 us                                                          | 727 us: 1.02x slower                                                           |
| docutils                   | 1.82 sec                                                        | 1.87 sec: 1.03x slower                                                         |
| django_template            | 32.7 ms                                                         | 33.6 ms: 1.03x slower                                                          |
| nqueens                    | 75.1 ms                                                         | 77.3 ms: 1.03x slower                                                          |
| dulwich_log                | 49.7 ms                                                         | 51.2 ms: 1.03x slower                                                          |
| regex_dna                  | 117 ms                                                          | 121 ms: 1.03x slower                                                           |
| xml_etree_iterparse        | 65.1 ms                                                         | 67.5 ms: 1.04x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.68 ms: 1.04x slower                                                          |
| regex_v8                   | 15.6 ms                                                         | 16.2 ms: 1.04x slower                                                          |
| sqlglot_transpile          | 1.29 ms                                                         | 1.35 ms: 1.04x slower                                                          |
| sqlglot_parse              | 1.05 ms                                                         | 1.10 ms: 1.04x slower                                                          |
| regex_effbot               | 1.81 ms                                                         | 1.90 ms: 1.05x slower                                                          |
| typing_runtime_protocols   | 136 us                                                          | 143 us: 1.05x slower                                                           |
| sqlglot_optimize           | 42.5 ms                                                         | 44.6 ms: 1.05x slower                                                          |
| unpack_sequence            | 42.9 ns                                                         | 45.3 ns: 1.05x slower                                                          |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.06 ms: 1.05x slower                                                          |
| regex_compile              | 103 ms                                                          | 109 ms: 1.06x slower                                                           |
| meteor_contest             | 77.0 ms                                                         | 81.4 ms: 1.06x slower                                                          |
| sqlglot_normalize          | 220 ms                                                          | 233 ms: 1.06x slower                                                           |
| chaos                      | 51.2 ms                                                         | 54.3 ms: 1.06x slower                                                          |
| pprint_safe_repr           | 644 ms                                                          | 684 ms: 1.06x slower                                                           |
| spectral_norm              | 71.3 ms                                                         | 75.9 ms: 1.06x slower                                                          |
| tomli_loads                | 1.73 sec                                                        | 1.85 sec: 1.07x slower                                                         |
| genshi_text                | 22.4 ms                                                         | 24.2 ms: 1.08x slower                                                          |
| xml_etree_generate         | 62.6 ms                                                         | 67.5 ms: 1.08x slower                                                          |
| pprint_pformat             | 1.30 sec                                                        | 1.40 sec: 1.08x slower                                                         |
| scimark_lu                 | 63.5 ms                                                         | 68.7 ms: 1.08x slower                                                          |
| float                      | 57.8 ms                                                         | 62.8 ms: 1.09x slower                                                          |
| xml_etree_process          | 45.0 ms                                                         | 49.4 ms: 1.10x slower                                                          |
| async_generators           | 274 ms                                                          | 301 ms: 1.10x slower                                                           |
| pickle_pure_python         | 238 us                                                          | 262 us: 1.10x slower                                                           |
| comprehensions             | 12.7 us                                                         | 14.1 us: 1.11x slower                                                          |
| pyflate                    | 326 ms                                                          | 362 ms: 1.11x slower                                                           |
| deltablue                  | 2.41 ms                                                         | 2.67 ms: 1.11x slower                                                          |
| hexiom                     | 4.64 ms                                                         | 5.17 ms: 1.11x slower                                                          |
| mako                       | 7.31 ms                                                         | 8.16 ms: 1.12x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 180 us: 1.12x slower                                                           |
| scimark_monte_carlo        | 50.3 ms                                                         | 56.9 ms: 1.13x slower                                                          |
| raytrace                   | 205 ms                                                          | 233 ms: 1.13x slower                                                           |
| nbody                      | 81.9 ms                                                         | 93.0 ms: 1.14x slower                                                          |
| scimark_sor                | 91.8 ms                                                         | 105 ms: 1.14x slower                                                           |
| fannkuch                   | 293 ms                                                          | 336 ms: 1.15x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.0 ms: 1.15x slower                                                          |
| scimark_fft                | 206 ms                                                          | 239 ms: 1.16x slower                                                           |
| richards                   | 33.8 ms                                                         | 39.4 ms: 1.17x slower                                                          |
| richards_super             | 38.0 ms                                                         | 44.3 ms: 1.17x slower                                                          |
| generators                 | 22.1 ms                                                         | 26.0 ms: 1.18x slower                                                          |
| logging_silent             | 61.6 ns                                                         | 74.6 ns: 1.21x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (7): bench_thread_pool, sympy_sum, async_tree_io, json_loads, sympy_str, json, pylint
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging

# HPT report

- Reliability score: 99.52% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown