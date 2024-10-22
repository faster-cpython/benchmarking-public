# Results vs. 3.13.0

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: windows-x86
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.03x faster
- HPT reliability: 99.31%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 248 ms: 1.02x faster                                                           |
| docutils       | 1.82 sec                                                        | 1.87 sec: 1.03x slower                                                         |
| tornado_http   | 104 ms                                                          | 95.1 ms: 1.10x faster                                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 669 ms: 1.26x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 250 ms: 1.15x faster                                                           |
| async_tree_none            | 246 ms                                                          | 217 ms: 1.13x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 271 ms: 1.12x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 198 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 466 ms: 1.06x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.1 sec: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 461 ms: 1.01x faster                                                           |
| async_generators           | 274 ms                                                          | 300 ms: 1.10x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.0 ms: 1.15x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 197 ms: 1.03x faster                                                           |
| float          | 57.8 ms                                                         | 62.2 ms: 1.08x slower                                                          |
| nbody          | 81.9 ms                                                         | 91.3 ms: 1.11x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                          | 118 ms: 1.01x slower                                                           |
| regex_v8       | 15.6 ms                                                         | 16.1 ms: 1.03x slower                                                          |
| regex_effbot   | 1.81 ms                                                         | 1.88 ms: 1.04x slower                                                          |
| regex_compile  | 103 ms                                                          | 108 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle               | 8.42 us                                                         | 7.77 us: 1.08x faster                                                          |
| pickle_dict          | 21.7 us                                                         | 20.3 us: 1.07x faster                                                          |
| unpickle_list        | 3.09 us                                                         | 2.96 us: 1.05x faster                                                          |
| unpickle             | 10.5 us                                                         | 10.3 us: 1.03x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 107 ms: 1.02x faster                                                           |
| json_loads           | 21.0 us                                                         | 20.8 us: 1.01x faster                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 66.8 ms: 1.03x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 7.69 ms: 1.04x slower                                                          |
| pickle_pure_python   | 238 us                                                          | 257 us: 1.08x slower                                                           |
| xml_etree_generate   | 62.6 ms                                                         | 68.3 ms: 1.09x slower                                                          |
| tomli_loads          | 1.73 sec                                                        | 1.93 sec: 1.12x slower                                                         |
| unpickle_pure_python | 162 us                                                          | 181 us: 1.12x slower                                                           |
| xml_etree_process    | 45.0 ms                                                         | 50.7 ms: 1.13x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 23.8 ms: 1.02x faster                                                          |
| python_startup_no_site | 19.9 ms                                                         | 19.8 ms: 1.01x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 48.7 ms: 1.02x faster                                                          |
| genshi_text     | 22.4 ms                                                         | 22.3 ms: 1.01x faster                                                          |
| django_template | 32.7 ms                                                         | 33.7 ms: 1.03x slower                                                          |
| mako            | 7.31 ms                                                         | 7.99 ms: 1.09x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.02x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 742 us: 13.68x faster                                                          |
| coverage                   | 333 ms                                                          | 52.7 ms: 6.31x faster                                                          |
| asyncio_tcp                | 842 ms                                                          | 669 ms: 1.26x faster                                                           |
| deepcopy                   | 307 us                                                          | 250 us: 1.23x faster                                                           |
| deepcopy_memo              | 26.2 us                                                         | 21.9 us: 1.19x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 250 ms: 1.15x faster                                                           |
| async_tree_none            | 246 ms                                                          | 217 ms: 1.13x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 271 ms: 1.12x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 198 ms: 1.10x faster                                                           |
| deepcopy_reduce            | 2.85 us                                                         | 2.60 us: 1.10x faster                                                          |
| tornado_http               | 104 ms                                                          | 95.1 ms: 1.10x faster                                                          |
| pickle                     | 8.42 us                                                         | 7.77 us: 1.08x faster                                                          |
| go                         | 111 ms                                                          | 103 ms: 1.08x faster                                                           |
| pathlib                    | 89.4 ms                                                         | 83.3 ms: 1.07x faster                                                          |
| pickle_dict                | 21.7 us                                                         | 20.3 us: 1.07x faster                                                          |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 466 ms: 1.06x faster                                                           |
| telco                      | 6.67 ms                                                         | 6.37 ms: 1.05x faster                                                          |
| unpickle_list              | 3.09 us                                                         | 2.96 us: 1.05x faster                                                          |
| bench_mp_pool              | 74.3 ms                                                         | 71.5 ms: 1.04x faster                                                          |
| gc_traversal               | 1.45 ms                                                         | 1.41 ms: 1.03x faster                                                          |
| pidigits                   | 202 ms                                                          | 197 ms: 1.03x faster                                                           |
| unpickle                   | 10.5 us                                                         | 10.3 us: 1.03x faster                                                          |
| 2to3                       | 253 ms                                                          | 248 ms: 1.02x faster                                                           |
| xml_etree_parse            | 109 ms                                                          | 107 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.1 sec: 1.02x faster                                                         |
| sqlite_synth               | 1.97 us                                                         | 1.93 us: 1.02x faster                                                          |
| python_startup             | 24.3 ms                                                         | 23.8 ms: 1.02x faster                                                          |
| genshi_xml                 | 49.5 ms                                                         | 48.7 ms: 1.02x faster                                                          |
| sympy_sum                  | 108 ms                                                          | 106 ms: 1.02x faster                                                           |
| crypto_pyaes               | 58.2 ms                                                         | 57.3 ms: 1.01x faster                                                          |
| json_loads                 | 21.0 us                                                         | 20.8 us: 1.01x faster                                                          |
| python_startup_no_site     | 19.9 ms                                                         | 19.8 ms: 1.01x faster                                                          |
| genshi_text                | 22.4 ms                                                         | 22.3 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 461 ms: 1.01x faster                                                           |
| dulwich_log                | 49.7 ms                                                         | 49.9 ms: 1.00x slower                                                          |
| sympy_str                  | 215 ms                                                          | 216 ms: 1.01x slower                                                           |
| sqlglot_transpile          | 1.29 ms                                                         | 1.30 ms: 1.01x slower                                                          |
| typing_runtime_protocols   | 136 us                                                          | 137 us: 1.01x slower                                                           |
| regex_dna                  | 117 ms                                                          | 118 ms: 1.01x slower                                                           |
| sqlglot_optimize           | 42.5 ms                                                         | 43.0 ms: 1.01x slower                                                          |
| sqlglot_normalize          | 220 ms                                                          | 223 ms: 1.01x slower                                                           |
| logging_simple             | 7.87 us                                                         | 8.00 us: 1.02x slower                                                          |
| logging_format             | 8.57 us                                                         | 8.71 us: 1.02x slower                                                          |
| mdp                        | 1.67 sec                                                        | 1.70 sec: 1.02x slower                                                         |
| pycparser                  | 869 ms                                                          | 884 ms: 1.02x slower                                                           |
| sympy_integrate            | 15.2 ms                                                         | 15.5 ms: 1.02x slower                                                          |
| sympy_expand               | 375 ms                                                          | 383 ms: 1.02x slower                                                           |
| xml_etree_iterparse        | 65.1 ms                                                         | 66.8 ms: 1.03x slower                                                          |
| create_gc_cycles           | 713 us                                                          | 733 us: 1.03x slower                                                           |
| docutils                   | 1.82 sec                                                        | 1.87 sec: 1.03x slower                                                         |
| django_template            | 32.7 ms                                                         | 33.7 ms: 1.03x slower                                                          |
| pprint_safe_repr           | 644 ms                                                          | 665 ms: 1.03x slower                                                           |
| regex_v8                   | 15.6 ms                                                         | 16.1 ms: 1.03x slower                                                          |
| meteor_contest             | 77.0 ms                                                         | 79.8 ms: 1.04x slower                                                          |
| regex_effbot               | 1.81 ms                                                         | 1.88 ms: 1.04x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.69 ms: 1.04x slower                                                          |
| chaos                      | 51.2 ms                                                         | 53.4 ms: 1.04x slower                                                          |
| regex_compile              | 103 ms                                                          | 108 ms: 1.05x slower                                                           |
| spectral_norm              | 71.3 ms                                                         | 75.2 ms: 1.05x slower                                                          |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.07 ms: 1.06x slower                                                          |
| scimark_sor                | 91.8 ms                                                         | 98.3 ms: 1.07x slower                                                          |
| pprint_pformat             | 1.30 sec                                                        | 1.39 sec: 1.07x slower                                                         |
| scimark_lu                 | 63.5 ms                                                         | 68.1 ms: 1.07x slower                                                          |
| fannkuch                   | 293 ms                                                          | 314 ms: 1.07x slower                                                           |
| float                      | 57.8 ms                                                         | 62.2 ms: 1.08x slower                                                          |
| pickle_pure_python         | 238 us                                                          | 257 us: 1.08x slower                                                           |
| pyflate                    | 326 ms                                                          | 352 ms: 1.08x slower                                                           |
| comprehensions             | 12.7 us                                                         | 13.8 us: 1.08x slower                                                          |
| xml_etree_generate         | 62.6 ms                                                         | 68.3 ms: 1.09x slower                                                          |
| mako                       | 7.31 ms                                                         | 7.99 ms: 1.09x slower                                                          |
| async_generators           | 274 ms                                                          | 300 ms: 1.10x slower                                                           |
| unpack_sequence            | 42.9 ns                                                         | 47.1 ns: 1.10x slower                                                          |
| hexiom                     | 4.64 ms                                                         | 5.10 ms: 1.10x slower                                                          |
| scimark_monte_carlo        | 50.3 ms                                                         | 55.4 ms: 1.10x slower                                                          |
| deltablue                  | 2.41 ms                                                         | 2.68 ms: 1.11x slower                                                          |
| nbody                      | 81.9 ms                                                         | 91.3 ms: 1.11x slower                                                          |
| tomli_loads                | 1.73 sec                                                        | 1.93 sec: 1.12x slower                                                         |
| richards                   | 33.8 ms                                                         | 37.9 ms: 1.12x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 181 us: 1.12x slower                                                           |
| xml_etree_process          | 45.0 ms                                                         | 50.7 ms: 1.13x slower                                                          |
| scimark_fft                | 206 ms                                                          | 233 ms: 1.13x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.0 ms: 1.15x slower                                                          |
| richards_super             | 38.0 ms                                                         | 43.5 ms: 1.15x slower                                                          |
| raytrace                   | 205 ms                                                          | 236 ms: 1.15x slower                                                           |
| generators                 | 22.1 ms                                                         | 26.2 ms: 1.18x slower                                                          |
| logging_silent             | 61.6 ns                                                         | 74.5 ns: 1.21x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (9): bench_thread_pool, async_tree_io, nqueens, html5lib, sqlglot_parse, json, pickle_list, async_tree_io_tg, pylint
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging

# HPT report

- Reliability score: 99.31% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown