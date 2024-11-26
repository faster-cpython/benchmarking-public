# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc1
- machine: windows-x86
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.034x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 244 ms: 1.05x faster                                                  |
| chameleon      | 6.24 ms                                                         | 5.80 ms: 1.08x faster                                                 |
| docutils       | 1.80 sec                                                        | 1.88 sec: 1.04x slower                                                |
| Geometric mean | (ref)                                                           | 1.02x faster                                                          |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 266 ms: 1.08x faster                                                  |
| async_tree_memoization     | 302 ms                                                          | 290 ms: 1.04x faster                                                  |
| async_tree_none            | 245 ms                                                          | 237 ms: 1.03x faster                                                  |
| coroutines                 | 16.1 ms                                                         | 15.7 ms: 1.03x faster                                                 |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 456 ms: 1.03x faster                                                  |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 485 ms: 1.01x faster                                                  |
| async_tree_io              | 530 ms                                                          | 550 ms: 1.04x slower                                                  |
| async_generators           | 267 ms                                                          | 280 ms: 1.05x slower                                                  |
| async_tree_io_tg           | 499 ms                                                          | 549 ms: 1.10x slower                                                  |
| Geometric mean             | (ref)                                                           | 1.00x faster                                                          |

Benchmark hidden because not significant (1): async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 77.1 ms: 1.06x faster                                                 |
| float          | 56.4 ms                                                         | 54.2 ms: 1.04x faster                                                 |
| pidigits       | 204 ms                                                          | 198 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                           | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 99.2 ms: 1.02x faster                                                 |
| regex_v8       | 15.5 ms                                                         | 16.1 ms: 1.04x slower                                                 |
| regex_effbot   | 1.82 ms                                                         | 1.90 ms: 1.04x slower                                                 |
| regex_dna      | 112 ms                                                          | 123 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                           | 1.04x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 162 us                                                          | 148 us: 1.09x faster                                                  |
| pickle_pure_python   | 239 us                                                          | 226 us: 1.06x faster                                                  |
| xml_etree_process    | 44.6 ms                                                         | 42.8 ms: 1.04x faster                                                 |
| tomli_loads          | 1.74 sec                                                        | 1.68 sec: 1.03x faster                                                |
| json_loads           | 21.7 us                                                         | 21.0 us: 1.03x faster                                                 |
| xml_etree_generate   | 61.9 ms                                                         | 60.5 ms: 1.02x faster                                                 |
| json_dumps           | 7.53 ms                                                         | 7.61 ms: 1.01x slower                                                 |
| xml_etree_parse      | 102 ms                                                          | 104 ms: 1.02x slower                                                  |
| xml_etree_iterparse  | 61.3 ms                                                         | 65.7 ms: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 23.7 ms: 1.19x faster                                                 |
| python_startup_no_site | 20.2 ms                                                         | 19.3 ms: 1.04x faster                                                 |
| Geometric mean         | (ref)                                                           | 1.12x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 45.2 ms: 1.08x faster                                                 |
| genshi_text     | 21.7 ms                                                         | 20.4 ms: 1.06x faster                                                 |
| django_template | 32.0 ms                                                         | 31.3 ms: 1.02x faster                                                 |
| mako            | 7.02 ms                                                         | 6.96 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| create_gc_cycles           | 1.08 ms                                                         | 744 us: 1.46x faster                                                  |
| bench_mp_pool              | 93.6 ms                                                         | 72.8 ms: 1.29x faster                                                 |
| gc_traversal               | 1.76 ms                                                         | 1.46 ms: 1.21x faster                                                 |
| python_startup             | 28.3 ms                                                         | 23.7 ms: 1.19x faster                                                 |
| nqueens                    | 75.1 ms                                                         | 67.1 ms: 1.12x faster                                                 |
| comprehensions             | 13.1 us                                                         | 12.0 us: 1.10x faster                                                 |
| go                         | 111 ms                                                          | 101 ms: 1.09x faster                                                  |
| pprint_safe_repr           | 658 ms                                                          | 602 ms: 1.09x faster                                                  |
| unpickle_pure_python       | 162 us                                                          | 148 us: 1.09x faster                                                  |
| deepcopy_memo              | 26.2 us                                                         | 24.0 us: 1.09x faster                                                 |
| genshi_xml                 | 49.0 ms                                                         | 45.2 ms: 1.08x faster                                                 |
| deepcopy_reduce            | 2.94 us                                                         | 2.72 us: 1.08x faster                                                 |
| async_tree_memoization_tg  | 287 ms                                                          | 266 ms: 1.08x faster                                                  |
| chameleon                  | 6.24 ms                                                         | 5.80 ms: 1.08x faster                                                 |
| logging_silent             | 62.4 ns                                                         | 57.9 ns: 1.08x faster                                                 |
| hexiom                     | 4.60 ms                                                         | 4.28 ms: 1.07x faster                                                 |
| pprint_pformat             | 1.32 sec                                                        | 1.23 sec: 1.07x faster                                                |
| deepcopy                   | 311 us                                                          | 292 us: 1.07x faster                                                  |
| pycparser                  | 869 ms                                                          | 815 ms: 1.07x faster                                                  |
| genshi_text                | 21.7 ms                                                         | 20.4 ms: 1.06x faster                                                 |
| bench_thread_pool          | 1.04 ms                                                         | 981 us: 1.06x faster                                                  |
| pickle_pure_python         | 239 us                                                          | 226 us: 1.06x faster                                                  |
| sqlglot_normalize          | 223 ms                                                          | 211 ms: 1.06x faster                                                  |
| nbody                      | 81.4 ms                                                         | 77.1 ms: 1.06x faster                                                 |
| meteor_contest             | 78.1 ms                                                         | 74.2 ms: 1.05x faster                                                 |
| raytrace                   | 203 ms                                                          | 193 ms: 1.05x faster                                                  |
| json                       | 4.40 ms                                                         | 4.19 ms: 1.05x faster                                                 |
| logging_simple             | 7.89 us                                                         | 7.53 us: 1.05x faster                                                 |
| 2to3                       | 255 ms                                                          | 244 ms: 1.05x faster                                                  |
| python_startup_no_site     | 20.2 ms                                                         | 19.3 ms: 1.04x faster                                                 |
| xml_etree_process          | 44.6 ms                                                         | 42.8 ms: 1.04x faster                                                 |
| float                      | 56.4 ms                                                         | 54.2 ms: 1.04x faster                                                 |
| logging_format             | 8.59 us                                                         | 8.25 us: 1.04x faster                                                 |
| async_tree_memoization     | 302 ms                                                          | 290 ms: 1.04x faster                                                  |
| pyflate                    | 322 ms                                                          | 310 ms: 1.04x faster                                                  |
| telco                      | 6.27 ms                                                         | 6.04 ms: 1.04x faster                                                 |
| richards                   | 33.4 ms                                                         | 32.2 ms: 1.04x faster                                                 |
| sqlglot_transpile          | 1.26 ms                                                         | 1.22 ms: 1.04x faster                                                 |
| sqlglot_parse              | 1.02 ms                                                         | 985 us: 1.04x faster                                                  |
| coverage                   | 326 ms                                                          | 315 ms: 1.04x faster                                                  |
| sqlglot_optimize           | 42.4 ms                                                         | 41.0 ms: 1.03x faster                                                 |
| tomli_loads                | 1.74 sec                                                        | 1.68 sec: 1.03x faster                                                |
| json_loads                 | 21.7 us                                                         | 21.0 us: 1.03x faster                                                 |
| deltablue                  | 2.35 ms                                                         | 2.27 ms: 1.03x faster                                                 |
| async_tree_none            | 245 ms                                                          | 237 ms: 1.03x faster                                                  |
| coroutines                 | 16.1 ms                                                         | 15.7 ms: 1.03x faster                                                 |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 456 ms: 1.03x faster                                                  |
| fannkuch                   | 288 ms                                                          | 280 ms: 1.03x faster                                                  |
| pidigits                   | 204 ms                                                          | 198 ms: 1.03x faster                                                  |
| mdp                        | 1.70 sec                                                        | 1.65 sec: 1.03x faster                                                |
| scimark_sor                | 85.8 ms                                                         | 83.5 ms: 1.03x faster                                                 |
| richards_super             | 37.0 ms                                                         | 36.1 ms: 1.02x faster                                                 |
| django_template            | 32.0 ms                                                         | 31.3 ms: 1.02x faster                                                 |
| chaos                      | 49.4 ms                                                         | 48.3 ms: 1.02x faster                                                 |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 2.82 ms: 1.02x faster                                                 |
| xml_etree_generate         | 61.9 ms                                                         | 60.5 ms: 1.02x faster                                                 |
| scimark_monte_carlo        | 48.7 ms                                                         | 47.6 ms: 1.02x faster                                                 |
| sympy_integrate            | 15.2 ms                                                         | 14.9 ms: 1.02x faster                                                 |
| regex_compile              | 101 ms                                                          | 99.2 ms: 1.02x faster                                                 |
| sympy_expand               | 377 ms                                                          | 371 ms: 1.02x faster                                                  |
| dulwich_log                | 50.2 ms                                                         | 49.3 ms: 1.02x faster                                                 |
| crypto_pyaes               | 56.6 ms                                                         | 55.7 ms: 1.02x faster                                                 |
| thrift                     | 10.3 ms                                                         | 10.1 ms: 1.01x faster                                                 |
| sympy_str                  | 214 ms                                                          | 212 ms: 1.01x faster                                                  |
| sympy_sum                  | 108 ms                                                          | 107 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 485 ms: 1.01x faster                                                  |
| mako                       | 7.02 ms                                                         | 6.96 ms: 1.01x faster                                                 |
| pathlib                    | 89.1 ms                                                         | 89.8 ms: 1.01x slower                                                 |
| json_dumps                 | 7.53 ms                                                         | 7.61 ms: 1.01x slower                                                 |
| generators                 | 21.5 ms                                                         | 21.8 ms: 1.02x slower                                                 |
| spectral_norm              | 70.0 ms                                                         | 71.1 ms: 1.02x slower                                                 |
| typing_runtime_protocols   | 141 us                                                          | 144 us: 1.02x slower                                                  |
| xml_etree_parse            | 102 ms                                                          | 104 ms: 1.02x slower                                                  |
| async_tree_io              | 530 ms                                                          | 550 ms: 1.04x slower                                                  |
| regex_v8                   | 15.5 ms                                                         | 16.1 ms: 1.04x slower                                                 |
| docutils                   | 1.80 sec                                                        | 1.88 sec: 1.04x slower                                                |
| regex_effbot               | 1.82 ms                                                         | 1.90 ms: 1.04x slower                                                 |
| async_generators           | 267 ms                                                          | 280 ms: 1.05x slower                                                  |
| xml_etree_iterparse        | 61.3 ms                                                         | 65.7 ms: 1.07x slower                                                 |
| regex_dna                  | 112 ms                                                          | 123 ms: 1.09x slower                                                  |
| async_tree_io_tg           | 499 ms                                                          | 549 ms: 1.10x slower                                                  |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                          |

Benchmark hidden because not significant (6): async_tree_none_tg, tornado_http, scimark_lu, html5lib, scimark_fft, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240731-3.13.0rc1-e4a3e78/bm-20240731-pythonperf1_win32-x86-python-v3.13.0rc1-3.13.0rc1-e4a3e78.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.034x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown