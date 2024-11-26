# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a3
- machine: windows-x86
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.078x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 232 ms: 1.10x faster                                                |
| chameleon      | 6.24 ms                                                         | 5.40 ms: 1.16x faster                                               |
| docutils       | 1.80 sec                                                        | 1.72 sec: 1.05x faster                                              |
| html5lib       | 47.1 ms                                                         | 44.0 ms: 1.07x faster                                               |
| tornado_http   | 105 ms                                                          | 96.3 ms: 1.09x faster                                               |
| Geometric mean | (ref)                                                           | 1.09x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coroutines                 | 16.1 ms                                                         | 14.2 ms: 1.14x faster                                               |
| async_tree_none            | 245 ms                                                          | 241 ms: 1.01x faster                                                |
| async_generators           | 267 ms                                                          | 271 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 499 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 489 ms: 1.04x slower                                                |
| async_tree_none_tg         | 216 ms                                                          | 229 ms: 1.06x slower                                                |
| async_tree_io              | 530 ms                                                          | 588 ms: 1.11x slower                                                |
| async_tree_io_tg           | 499 ms                                                          | 571 ms: 1.14x slower                                                |
| Geometric mean             | (ref)                                                           | 1.02x slower                                                        |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 56.4 ms                                                         | 51.1 ms: 1.10x faster                                               |
| nbody          | 81.4 ms                                                         | 74.0 ms: 1.10x faster                                               |
| pidigits       | 204 ms                                                          | 199 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                           | 1.07x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 92.5 ms: 1.09x faster                                               |
| regex_v8       | 15.5 ms                                                         | 16.1 ms: 1.04x slower                                               |
| regex_effbot   | 1.82 ms                                                         | 1.92 ms: 1.05x slower                                               |
| regex_dna      | 112 ms                                                          | 125 ms: 1.11x slower                                                |
| Geometric mean | (ref)                                                           | 1.03x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 239 us                                                          | 204 us: 1.17x faster                                                |
| unpickle_pure_python | 162 us                                                          | 140 us: 1.15x faster                                                |
| json_dumps           | 7.53 ms                                                         | 6.75 ms: 1.12x faster                                               |
| json_loads           | 21.7 us                                                         | 19.8 us: 1.09x faster                                               |
| xml_etree_process    | 44.6 ms                                                         | 41.1 ms: 1.08x faster                                               |
| tomli_loads          | 1.74 sec                                                        | 1.62 sec: 1.08x faster                                              |
| xml_etree_generate   | 61.9 ms                                                         | 58.8 ms: 1.05x faster                                               |
| xml_etree_parse      | 102 ms                                                          | 108 ms: 1.06x slower                                                |
| xml_etree_iterparse  | 61.3 ms                                                         | 66.4 ms: 1.08x slower                                               |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 22.7 ms: 1.25x faster                                               |
| python_startup_no_site | 20.2 ms                                                         | 20.5 ms: 1.02x slower                                               |
| Geometric mean         | (ref)                                                           | 1.11x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 21.7 ms                                                         | 18.1 ms: 1.20x faster                                               |
| genshi_xml      | 49.0 ms                                                         | 41.6 ms: 1.18x faster                                               |
| django_template | 32.0 ms                                                         | 29.0 ms: 1.10x faster                                               |
| mako            | 7.02 ms                                                         | 6.84 ms: 1.03x faster                                               |
| Geometric mean  | (ref)                                                           | 1.13x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| create_gc_cycles           | 1.08 ms                                                         | 651 us: 1.66x faster                                                |
| typing_runtime_protocols   | 141 us                                                          | 87.7 us: 1.61x faster                                               |
| deepcopy_reduce            | 2.94 us                                                         | 2.22 us: 1.32x faster                                               |
| gc_traversal               | 1.76 ms                                                         | 1.40 ms: 1.26x faster                                               |
| python_startup             | 28.3 ms                                                         | 22.7 ms: 1.25x faster                                               |
| bench_mp_pool              | 93.6 ms                                                         | 74.9 ms: 1.25x faster                                               |
| deepcopy                   | 311 us                                                          | 255 us: 1.22x faster                                                |
| deepcopy_memo              | 26.2 us                                                         | 21.6 us: 1.21x faster                                               |
| pprint_safe_repr           | 658 ms                                                          | 543 ms: 1.21x faster                                                |
| genshi_text                | 21.7 ms                                                         | 18.1 ms: 1.20x faster                                               |
| sqlglot_parse              | 1.02 ms                                                         | 848 us: 1.20x faster                                                |
| richards                   | 33.4 ms                                                         | 27.8 ms: 1.20x faster                                               |
| pprint_pformat             | 1.32 sec                                                        | 1.12 sec: 1.18x faster                                              |
| genshi_xml                 | 49.0 ms                                                         | 41.6 ms: 1.18x faster                                               |
| richards_super             | 37.0 ms                                                         | 31.4 ms: 1.18x faster                                               |
| comprehensions             | 13.1 us                                                         | 11.2 us: 1.17x faster                                               |
| pickle_pure_python         | 239 us                                                          | 204 us: 1.17x faster                                                |
| sqlglot_transpile          | 1.26 ms                                                         | 1.08 ms: 1.17x faster                                               |
| go                         | 111 ms                                                          | 95.1 ms: 1.17x faster                                               |
| chameleon                  | 6.24 ms                                                         | 5.40 ms: 1.16x faster                                               |
| unpickle_pure_python       | 162 us                                                          | 140 us: 1.15x faster                                                |
| coroutines                 | 16.1 ms                                                         | 14.2 ms: 1.14x faster                                               |
| sqlglot_normalize          | 223 ms                                                          | 197 ms: 1.13x faster                                                |
| telco                      | 6.27 ms                                                         | 5.62 ms: 1.12x faster                                               |
| json_dumps                 | 7.53 ms                                                         | 6.75 ms: 1.12x faster                                               |
| spectral_norm              | 70.0 ms                                                         | 63.0 ms: 1.11x faster                                               |
| hexiom                     | 4.60 ms                                                         | 4.14 ms: 1.11x faster                                               |
| mdp                        | 1.70 sec                                                        | 1.53 sec: 1.11x faster                                              |
| crypto_pyaes               | 56.6 ms                                                         | 51.0 ms: 1.11x faster                                               |
| sqlglot_optimize           | 42.4 ms                                                         | 38.2 ms: 1.11x faster                                               |
| django_template            | 32.0 ms                                                         | 29.0 ms: 1.10x faster                                               |
| float                      | 56.4 ms                                                         | 51.1 ms: 1.10x faster                                               |
| sympy_str                  | 214 ms                                                          | 194 ms: 1.10x faster                                                |
| sympy_expand               | 377 ms                                                          | 343 ms: 1.10x faster                                                |
| 2to3                       | 255 ms                                                          | 232 ms: 1.10x faster                                                |
| nbody                      | 81.4 ms                                                         | 74.0 ms: 1.10x faster                                               |
| scimark_monte_carlo        | 48.7 ms                                                         | 44.3 ms: 1.10x faster                                               |
| sympy_sum                  | 108 ms                                                          | 98.5 ms: 1.10x faster                                               |
| pycparser                  | 869 ms                                                          | 793 ms: 1.10x faster                                                |
| json_loads                 | 21.7 us                                                         | 19.8 us: 1.09x faster                                               |
| logging_silent             | 62.4 ns                                                         | 57.1 ns: 1.09x faster                                               |
| regex_compile              | 101 ms                                                          | 92.5 ms: 1.09x faster                                               |
| sympy_integrate            | 15.2 ms                                                         | 14.0 ms: 1.09x faster                                               |
| tornado_http               | 105 ms                                                          | 96.3 ms: 1.09x faster                                               |
| chaos                      | 49.4 ms                                                         | 45.5 ms: 1.08x faster                                               |
| xml_etree_process          | 44.6 ms                                                         | 41.1 ms: 1.08x faster                                               |
| scimark_sor                | 85.8 ms                                                         | 79.6 ms: 1.08x faster                                               |
| fannkuch                   | 288 ms                                                          | 267 ms: 1.08x faster                                                |
| tomli_loads                | 1.74 sec                                                        | 1.62 sec: 1.08x faster                                              |
| deltablue                  | 2.35 ms                                                         | 2.18 ms: 1.08x faster                                               |
| html5lib                   | 47.1 ms                                                         | 44.0 ms: 1.07x faster                                               |
| json                       | 4.40 ms                                                         | 4.12 ms: 1.07x faster                                               |
| raytrace                   | 203 ms                                                          | 191 ms: 1.06x faster                                                |
| meteor_contest             | 78.1 ms                                                         | 73.7 ms: 1.06x faster                                               |
| xml_etree_generate         | 61.9 ms                                                         | 58.8 ms: 1.05x faster                                               |
| pyflate                    | 322 ms                                                          | 306 ms: 1.05x faster                                                |
| docutils                   | 1.80 sec                                                        | 1.72 sec: 1.05x faster                                              |
| nqueens                    | 75.1 ms                                                         | 72.6 ms: 1.03x faster                                               |
| pylint                     | 225 ms                                                          | 217 ms: 1.03x faster                                                |
| scimark_fft                | 204 ms                                                          | 198 ms: 1.03x faster                                                |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 2.79 ms: 1.03x faster                                               |
| logging_format             | 8.59 us                                                         | 8.33 us: 1.03x faster                                               |
| logging_simple             | 7.89 us                                                         | 7.69 us: 1.03x faster                                               |
| mako                       | 7.02 ms                                                         | 6.84 ms: 1.03x faster                                               |
| pidigits                   | 204 ms                                                          | 199 ms: 1.02x faster                                                |
| async_tree_none            | 245 ms                                                          | 241 ms: 1.01x faster                                                |
| pathlib                    | 89.1 ms                                                         | 88.6 ms: 1.01x faster                                               |
| async_generators           | 267 ms                                                          | 271 ms: 1.01x slower                                                |
| python_startup_no_site     | 20.2 ms                                                         | 20.5 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 499 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 489 ms: 1.04x slower                                                |
| regex_v8                   | 15.5 ms                                                         | 16.1 ms: 1.04x slower                                               |
| regex_effbot               | 1.82 ms                                                         | 1.92 ms: 1.05x slower                                               |
| xml_etree_parse            | 102 ms                                                          | 108 ms: 1.06x slower                                                |
| async_tree_none_tg         | 216 ms                                                          | 229 ms: 1.06x slower                                                |
| generators                 | 21.5 ms                                                         | 22.9 ms: 1.06x slower                                               |
| xml_etree_iterparse        | 61.3 ms                                                         | 66.4 ms: 1.08x slower                                               |
| async_tree_io              | 530 ms                                                          | 588 ms: 1.11x slower                                                |
| regex_dna                  | 112 ms                                                          | 125 ms: 1.11x slower                                                |
| async_tree_io_tg           | 499 ms                                                          | 571 ms: 1.14x slower                                                |
| coverage                   | 326 ms                                                          | 479 ms: 1.47x slower                                                |
| Geometric mean             | (ref)                                                           | 1.08x faster                                                        |

Benchmark hidden because not significant (5): bench_thread_pool, scimark_lu, thrift, async_tree_memoization, async_tree_memoization_tg
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, dulwich_log, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-pythonperf1_win32-x86-python-v3.13.0a3-3.13.0a3-f009305.json: asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.078x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown