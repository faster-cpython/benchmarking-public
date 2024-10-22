# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a3
- machine: windows-x86
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 232 ms: 1.09x faster                                                |
| chameleon      | 6.14 ms                                                         | 5.40 ms: 1.14x faster                                               |
| docutils       | 1.82 sec                                                        | 1.72 sec: 1.06x faster                                              |
| html5lib       | 48.3 ms                                                         | 44.0 ms: 1.10x faster                                               |
| tornado_http   | 104 ms                                                          | 96.3 ms: 1.08x faster                                               |
| Geometric mean | (ref)                                                           | 1.09x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 638 ms: 1.32x faster                                                |
| coroutines                 | 15.7 ms                                                         | 14.2 ms: 1.11x faster                                               |
| async_tree_none            | 246 ms                                                          | 241 ms: 1.02x faster                                                |
| async_generators           | 274 ms                                                          | 271 ms: 1.01x faster                                                |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 499 ms: 1.01x slower                                                |
| async_tree_none_tg         | 219 ms                                                          | 229 ms: 1.05x slower                                                |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 489 ms: 1.06x slower                                                |
| async_tree_io              | 537 ms                                                          | 588 ms: 1.10x slower                                                |
| async_tree_io_tg           | 509 ms                                                          | 571 ms: 1.12x slower                                                |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                        |

Benchmark hidden because not significant (3): asyncio_tcp_ssl, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 57.8 ms                                                         | 51.1 ms: 1.13x faster                                               |
| nbody          | 81.9 ms                                                         | 74.0 ms: 1.11x faster                                               |
| pidigits       | 202 ms                                                          | 199 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                           | 1.08x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 92.5 ms: 1.12x faster                                               |
| regex_v8       | 15.6 ms                                                         | 16.1 ms: 1.03x slower                                               |
| regex_effbot   | 1.81 ms                                                         | 1.92 ms: 1.06x slower                                               |
| regex_dna      | 117 ms                                                          | 125 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                           | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 238 us                                                          | 204 us: 1.17x faster                                                |
| unpickle_pure_python | 162 us                                                          | 140 us: 1.15x faster                                                |
| json_dumps           | 7.40 ms                                                         | 6.75 ms: 1.10x faster                                               |
| xml_etree_process    | 45.0 ms                                                         | 41.1 ms: 1.09x faster                                               |
| pickle               | 8.42 us                                                         | 7.71 us: 1.09x faster                                               |
| pickle_dict          | 21.7 us                                                         | 20.0 us: 1.09x faster                                               |
| unpickle             | 10.5 us                                                         | 9.71 us: 1.09x faster                                               |
| tomli_loads          | 1.73 sec                                                        | 1.62 sec: 1.07x faster                                              |
| xml_etree_generate   | 62.6 ms                                                         | 58.8 ms: 1.07x faster                                               |
| json_loads           | 21.0 us                                                         | 19.8 us: 1.06x faster                                               |
| pickle_list          | 3.40 us                                                         | 3.33 us: 1.02x faster                                               |
| xml_etree_iterparse  | 65.1 ms                                                         | 66.4 ms: 1.02x slower                                               |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                        |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 22.7 ms: 1.07x faster                                               |
| python_startup_no_site | 19.9 ms                                                         | 20.5 ms: 1.03x slower                                               |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 22.4 ms                                                         | 18.1 ms: 1.24x faster                                               |
| genshi_xml      | 49.5 ms                                                         | 41.6 ms: 1.19x faster                                               |
| django_template | 32.7 ms                                                         | 29.0 ms: 1.13x faster                                               |
| mako            | 7.31 ms                                                         | 6.84 ms: 1.07x faster                                               |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols   | 136 us                                                          | 87.7 us: 1.55x faster                                               |
| asyncio_tcp                | 842 ms                                                          | 638 ms: 1.32x faster                                                |
| deepcopy_reduce            | 2.85 us                                                         | 2.22 us: 1.28x faster                                               |
| genshi_text                | 22.4 ms                                                         | 18.1 ms: 1.24x faster                                               |
| sqlglot_parse              | 1.05 ms                                                         | 848 us: 1.24x faster                                                |
| richards                   | 33.8 ms                                                         | 27.8 ms: 1.21x faster                                               |
| deepcopy_memo              | 26.2 us                                                         | 21.6 us: 1.21x faster                                               |
| richards_super             | 38.0 ms                                                         | 31.4 ms: 1.21x faster                                               |
| deepcopy                   | 307 us                                                          | 255 us: 1.20x faster                                                |
| sqlglot_transpile          | 1.29 ms                                                         | 1.08 ms: 1.20x faster                                               |
| genshi_xml                 | 49.5 ms                                                         | 41.6 ms: 1.19x faster                                               |
| telco                      | 6.67 ms                                                         | 5.62 ms: 1.19x faster                                               |
| pprint_safe_repr           | 644 ms                                                          | 543 ms: 1.18x faster                                                |
| go                         | 111 ms                                                          | 95.1 ms: 1.17x faster                                               |
| pickle_pure_python         | 238 us                                                          | 204 us: 1.17x faster                                                |
| pprint_pformat             | 1.30 sec                                                        | 1.12 sec: 1.16x faster                                              |
| scimark_sor                | 91.8 ms                                                         | 79.6 ms: 1.15x faster                                               |
| unpickle_pure_python       | 162 us                                                          | 140 us: 1.15x faster                                                |
| crypto_pyaes               | 58.2 ms                                                         | 51.0 ms: 1.14x faster                                               |
| comprehensions             | 12.7 us                                                         | 11.2 us: 1.14x faster                                               |
| chameleon                  | 6.14 ms                                                         | 5.40 ms: 1.14x faster                                               |
| scimark_monte_carlo        | 50.3 ms                                                         | 44.3 ms: 1.13x faster                                               |
| spectral_norm              | 71.3 ms                                                         | 63.0 ms: 1.13x faster                                               |
| float                      | 57.8 ms                                                         | 51.1 ms: 1.13x faster                                               |
| django_template            | 32.7 ms                                                         | 29.0 ms: 1.13x faster                                               |
| chaos                      | 51.2 ms                                                         | 45.5 ms: 1.12x faster                                               |
| hexiom                     | 4.64 ms                                                         | 4.14 ms: 1.12x faster                                               |
| regex_compile              | 103 ms                                                          | 92.5 ms: 1.12x faster                                               |
| sqlglot_normalize          | 220 ms                                                          | 197 ms: 1.12x faster                                                |
| sqlglot_optimize           | 42.5 ms                                                         | 38.2 ms: 1.11x faster                                               |
| sympy_str                  | 215 ms                                                          | 194 ms: 1.11x faster                                                |
| nbody                      | 81.9 ms                                                         | 74.0 ms: 1.11x faster                                               |
| coroutines                 | 15.7 ms                                                         | 14.2 ms: 1.11x faster                                               |
| deltablue                  | 2.41 ms                                                         | 2.18 ms: 1.10x faster                                               |
| sympy_sum                  | 108 ms                                                          | 98.5 ms: 1.10x faster                                               |
| json_dumps                 | 7.40 ms                                                         | 6.75 ms: 1.10x faster                                               |
| html5lib                   | 48.3 ms                                                         | 44.0 ms: 1.10x faster                                               |
| fannkuch                   | 293 ms                                                          | 267 ms: 1.10x faster                                                |
| pycparser                  | 869 ms                                                          | 793 ms: 1.10x faster                                                |
| create_gc_cycles           | 713 us                                                          | 651 us: 1.09x faster                                                |
| xml_etree_process          | 45.0 ms                                                         | 41.1 ms: 1.09x faster                                               |
| mdp                        | 1.67 sec                                                        | 1.53 sec: 1.09x faster                                              |
| sympy_expand               | 375 ms                                                          | 343 ms: 1.09x faster                                                |
| pickle                     | 8.42 us                                                         | 7.71 us: 1.09x faster                                               |
| 2to3                       | 253 ms                                                          | 232 ms: 1.09x faster                                                |
| sqlite_synth               | 1.97 us                                                         | 1.81 us: 1.09x faster                                               |
| pickle_dict                | 21.7 us                                                         | 20.0 us: 1.09x faster                                               |
| unpickle                   | 10.5 us                                                         | 9.71 us: 1.09x faster                                               |
| sympy_integrate            | 15.2 ms                                                         | 14.0 ms: 1.09x faster                                               |
| tornado_http               | 104 ms                                                          | 96.3 ms: 1.08x faster                                               |
| logging_silent             | 61.6 ns                                                         | 57.1 ns: 1.08x faster                                               |
| raytrace                   | 205 ms                                                          | 191 ms: 1.08x faster                                                |
| tomli_loads                | 1.73 sec                                                        | 1.62 sec: 1.07x faster                                              |
| python_startup             | 24.3 ms                                                         | 22.7 ms: 1.07x faster                                               |
| mako                       | 7.31 ms                                                         | 6.84 ms: 1.07x faster                                               |
| pyflate                    | 326 ms                                                          | 306 ms: 1.07x faster                                                |
| xml_etree_generate         | 62.6 ms                                                         | 58.8 ms: 1.07x faster                                               |
| docutils                   | 1.82 sec                                                        | 1.72 sec: 1.06x faster                                              |
| json_loads                 | 21.0 us                                                         | 19.8 us: 1.06x faster                                               |
| scimark_lu                 | 63.5 ms                                                         | 60.2 ms: 1.06x faster                                               |
| meteor_contest             | 77.0 ms                                                         | 73.7 ms: 1.05x faster                                               |
| scimark_fft                | 206 ms                                                          | 198 ms: 1.04x faster                                                |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 2.79 ms: 1.04x faster                                               |
| gc_traversal               | 1.45 ms                                                         | 1.40 ms: 1.04x faster                                               |
| json                       | 4.27 ms                                                         | 4.12 ms: 1.04x faster                                               |
| pylint                     | 225 ms                                                          | 217 ms: 1.03x faster                                                |
| nqueens                    | 75.1 ms                                                         | 72.6 ms: 1.03x faster                                               |
| logging_format             | 8.57 us                                                         | 8.33 us: 1.03x faster                                               |
| logging_simple             | 7.87 us                                                         | 7.69 us: 1.02x faster                                               |
| pickle_list                | 3.40 us                                                         | 3.33 us: 1.02x faster                                               |
| async_tree_none            | 246 ms                                                          | 241 ms: 1.02x faster                                                |
| pidigits                   | 202 ms                                                          | 199 ms: 1.01x faster                                                |
| async_generators           | 274 ms                                                          | 271 ms: 1.01x faster                                                |
| pathlib                    | 89.4 ms                                                         | 88.6 ms: 1.01x faster                                               |
| flaskblogging              | 2.04 sec                                                        | 2.03 sec: 1.00x faster                                              |
| bench_mp_pool              | 74.3 ms                                                         | 74.9 ms: 1.01x slower                                               |
| thrift                     | 10.1 ms                                                         | 10.3 ms: 1.01x slower                                               |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 499 ms: 1.01x slower                                                |
| xml_etree_iterparse        | 65.1 ms                                                         | 66.4 ms: 1.02x slower                                               |
| python_startup_no_site     | 19.9 ms                                                         | 20.5 ms: 1.03x slower                                               |
| regex_v8                   | 15.6 ms                                                         | 16.1 ms: 1.03x slower                                               |
| generators                 | 22.1 ms                                                         | 22.9 ms: 1.04x slower                                               |
| async_tree_none_tg         | 219 ms                                                          | 229 ms: 1.05x slower                                                |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 489 ms: 1.06x slower                                                |
| regex_effbot               | 1.81 ms                                                         | 1.92 ms: 1.06x slower                                               |
| regex_dna                  | 117 ms                                                          | 125 ms: 1.07x slower                                                |
| async_tree_io              | 537 ms                                                          | 588 ms: 1.10x slower                                                |
| async_tree_io_tg           | 509 ms                                                          | 571 ms: 1.12x slower                                                |
| coverage                   | 333 ms                                                          | 479 ms: 1.44x slower                                                |
| Geometric mean             | (ref)                                                           | 1.08x faster                                                        |

Benchmark hidden because not significant (6): bench_thread_pool, unpickle_list, xml_etree_parse, asyncio_tcp_ssl, async_tree_memoization, async_tree_memoization_tg
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown