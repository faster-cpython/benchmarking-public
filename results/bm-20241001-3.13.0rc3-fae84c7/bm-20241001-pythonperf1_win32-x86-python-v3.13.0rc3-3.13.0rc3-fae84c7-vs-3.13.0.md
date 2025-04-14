# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc3
- machine: windows-x86
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.033x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 243 ms: 1.05x faster                                                  |
| chameleon      | 6.24 ms                                                         | 5.98 ms: 1.04x faster                                                 |
| docutils       | 1.80 sec                                                        | 1.77 sec: 1.02x faster                                                |
| html5lib       | 47.1 ms                                                         | 45.6 ms: 1.03x faster                                                 |
| tornado_http   | 105 ms                                                          | 102 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                           | 1.03x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization     | 302 ms                                                          | 281 ms: 1.07x faster                                                  |
| async_tree_none            | 245 ms                                                          | 231 ms: 1.06x faster                                                  |
| async_tree_memoization_tg  | 287 ms                                                          | 273 ms: 1.05x faster                                                  |
| async_tree_none_tg         | 216 ms                                                          | 206 ms: 1.05x faster                                                  |
| async_tree_io              | 530 ms                                                          | 508 ms: 1.04x faster                                                  |
| async_tree_io_tg           | 499 ms                                                          | 482 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 473 ms: 1.03x faster                                                  |
| coroutines                 | 16.1 ms                                                         | 15.6 ms: 1.03x faster                                                 |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 456 ms: 1.03x faster                                                  |
| async_generators           | 267 ms                                                          | 263 ms: 1.02x faster                                                  |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 78.0 ms: 1.04x faster                                                 |
| float          | 56.4 ms                                                         | 55.2 ms: 1.02x faster                                                 |
| pidigits       | 204 ms                                                          | 200 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                           | 1.03x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 99.5 ms: 1.01x faster                                                 |
| regex_v8       | 15.5 ms                                                         | 15.8 ms: 1.02x slower                                                 |
| regex_effbot   | 1.82 ms                                                         | 1.90 ms: 1.05x slower                                                 |
| regex_dna      | 112 ms                                                          | 119 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                           | 1.03x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.6 us: 1.05x faster                                                 |
| tomli_loads          | 1.74 sec                                                        | 1.67 sec: 1.04x faster                                                |
| pickle_pure_python   | 239 us                                                          | 231 us: 1.04x faster                                                  |
| unpickle_pure_python | 162 us                                                          | 157 us: 1.03x faster                                                  |
| xml_etree_process    | 44.6 ms                                                         | 44.3 ms: 1.01x faster                                                 |
| xml_etree_generate   | 61.9 ms                                                         | 62.6 ms: 1.01x slower                                                 |
| xml_etree_iterparse  | 61.3 ms                                                         | 62.2 ms: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                          |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 24.7 ms: 1.15x faster                                                 |
| python_startup_no_site | 20.2 ms                                                         | 20.6 ms: 1.02x slower                                                 |
| Geometric mean         | (ref)                                                           | 1.06x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 32.0 ms                                                         | 29.3 ms: 1.09x faster                                                 |
| genshi_xml      | 49.0 ms                                                         | 45.1 ms: 1.09x faster                                                 |
| genshi_text     | 21.7 ms                                                         | 20.9 ms: 1.04x faster                                                 |
| mako            | 7.02 ms                                                         | 7.06 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                           | 1.05x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| create_gc_cycles           | 1.08 ms                                                         | 699 us: 1.55x faster                                                  |
| bench_mp_pool              | 93.6 ms                                                         | 76.8 ms: 1.22x faster                                                 |
| gc_traversal               | 1.76 ms                                                         | 1.45 ms: 1.21x faster                                                 |
| python_startup             | 28.3 ms                                                         | 24.7 ms: 1.15x faster                                                 |
| django_template            | 32.0 ms                                                         | 29.3 ms: 1.09x faster                                                 |
| genshi_xml                 | 49.0 ms                                                         | 45.1 ms: 1.09x faster                                                 |
| nqueens                    | 75.1 ms                                                         | 69.1 ms: 1.09x faster                                                 |
| deepcopy_reduce            | 2.94 us                                                         | 2.72 us: 1.08x faster                                                 |
| pprint_safe_repr           | 658 ms                                                          | 610 ms: 1.08x faster                                                  |
| async_tree_memoization     | 302 ms                                                          | 281 ms: 1.07x faster                                                  |
| pycparser                  | 869 ms                                                          | 810 ms: 1.07x faster                                                  |
| deepcopy                   | 311 us                                                          | 291 us: 1.07x faster                                                  |
| sqlglot_normalize          | 223 ms                                                          | 209 ms: 1.07x faster                                                  |
| sqlglot_parse              | 1.02 ms                                                         | 956 us: 1.07x faster                                                  |
| comprehensions             | 13.1 us                                                         | 12.4 us: 1.06x faster                                                 |
| raytrace                   | 203 ms                                                          | 191 ms: 1.06x faster                                                  |
| sqlglot_transpile          | 1.26 ms                                                         | 1.19 ms: 1.06x faster                                                 |
| async_tree_none            | 245 ms                                                          | 231 ms: 1.06x faster                                                  |
| pprint_pformat             | 1.32 sec                                                        | 1.25 sec: 1.05x faster                                                |
| bench_thread_pool          | 1.04 ms                                                         | 989 us: 1.05x faster                                                  |
| json_loads                 | 21.7 us                                                         | 20.6 us: 1.05x faster                                                 |
| 2to3                       | 255 ms                                                          | 243 ms: 1.05x faster                                                  |
| go                         | 111 ms                                                          | 105 ms: 1.05x faster                                                  |
| async_tree_memoization_tg  | 287 ms                                                          | 273 ms: 1.05x faster                                                  |
| logging_silent             | 62.4 ns                                                         | 59.5 ns: 1.05x faster                                                 |
| sqlglot_optimize           | 42.4 ms                                                         | 40.5 ms: 1.05x faster                                                 |
| async_tree_none_tg         | 216 ms                                                          | 206 ms: 1.05x faster                                                  |
| chameleon                  | 6.24 ms                                                         | 5.98 ms: 1.04x faster                                                 |
| async_tree_io              | 530 ms                                                          | 508 ms: 1.04x faster                                                  |
| tomli_loads                | 1.74 sec                                                        | 1.67 sec: 1.04x faster                                                |
| nbody                      | 81.4 ms                                                         | 78.0 ms: 1.04x faster                                                 |
| genshi_text                | 21.7 ms                                                         | 20.9 ms: 1.04x faster                                                 |
| pickle_pure_python         | 239 us                                                          | 231 us: 1.04x faster                                                  |
| async_tree_io_tg           | 499 ms                                                          | 482 ms: 1.04x faster                                                  |
| mdp                        | 1.70 sec                                                        | 1.64 sec: 1.03x faster                                                |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 473 ms: 1.03x faster                                                  |
| json                       | 4.40 ms                                                         | 4.25 ms: 1.03x faster                                                 |
| coroutines                 | 16.1 ms                                                         | 15.6 ms: 1.03x faster                                                 |
| logging_format             | 8.59 us                                                         | 8.31 us: 1.03x faster                                                 |
| deltablue                  | 2.35 ms                                                         | 2.27 ms: 1.03x faster                                                 |
| html5lib                   | 47.1 ms                                                         | 45.6 ms: 1.03x faster                                                 |
| unpickle_pure_python       | 162 us                                                          | 157 us: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 456 ms: 1.03x faster                                                  |
| pyflate                    | 322 ms                                                          | 313 ms: 1.03x faster                                                  |
| logging_simple             | 7.89 us                                                         | 7.68 us: 1.03x faster                                                 |
| typing_runtime_protocols   | 141 us                                                          | 137 us: 1.03x faster                                                  |
| meteor_contest             | 78.1 ms                                                         | 76.3 ms: 1.02x faster                                                 |
| dulwich_log                | 50.2 ms                                                         | 49.0 ms: 1.02x faster                                                 |
| tornado_http               | 105 ms                                                          | 102 ms: 1.02x faster                                                  |
| sympy_integrate            | 15.2 ms                                                         | 14.9 ms: 1.02x faster                                                 |
| float                      | 56.4 ms                                                         | 55.2 ms: 1.02x faster                                                 |
| chaos                      | 49.4 ms                                                         | 48.3 ms: 1.02x faster                                                 |
| sympy_sum                  | 108 ms                                                          | 106 ms: 1.02x faster                                                  |
| hexiom                     | 4.60 ms                                                         | 4.50 ms: 1.02x faster                                                 |
| fannkuch                   | 288 ms                                                          | 282 ms: 1.02x faster                                                  |
| deepcopy_memo              | 26.2 us                                                         | 25.7 us: 1.02x faster                                                 |
| pidigits                   | 204 ms                                                          | 200 ms: 1.02x faster                                                  |
| docutils                   | 1.80 sec                                                        | 1.77 sec: 1.02x faster                                                |
| scimark_monte_carlo        | 48.7 ms                                                         | 47.9 ms: 1.02x faster                                                 |
| async_generators           | 267 ms                                                          | 263 ms: 1.02x faster                                                  |
| sympy_expand               | 377 ms                                                          | 371 ms: 1.02x faster                                                  |
| regex_compile              | 101 ms                                                          | 99.5 ms: 1.01x faster                                                 |
| thrift                     | 10.3 ms                                                         | 10.1 ms: 1.01x faster                                                 |
| sympy_str                  | 214 ms                                                          | 212 ms: 1.01x faster                                                  |
| pathlib                    | 89.1 ms                                                         | 88.3 ms: 1.01x faster                                                 |
| coverage                   | 326 ms                                                          | 324 ms: 1.01x faster                                                  |
| xml_etree_process          | 44.6 ms                                                         | 44.3 ms: 1.01x faster                                                 |
| mako                       | 7.02 ms                                                         | 7.06 ms: 1.01x slower                                                 |
| scimark_fft                | 204 ms                                                          | 205 ms: 1.01x slower                                                  |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 2.90 ms: 1.01x slower                                                 |
| xml_etree_generate         | 61.9 ms                                                         | 62.6 ms: 1.01x slower                                                 |
| telco                      | 6.27 ms                                                         | 6.35 ms: 1.01x slower                                                 |
| crypto_pyaes               | 56.6 ms                                                         | 57.5 ms: 1.02x slower                                                 |
| xml_etree_iterparse        | 61.3 ms                                                         | 62.2 ms: 1.02x slower                                                 |
| python_startup_no_site     | 20.2 ms                                                         | 20.6 ms: 1.02x slower                                                 |
| scimark_lu                 | 60.7 ms                                                         | 62.1 ms: 1.02x slower                                                 |
| regex_v8                   | 15.5 ms                                                         | 15.8 ms: 1.02x slower                                                 |
| scimark_sor                | 85.8 ms                                                         | 88.0 ms: 1.03x slower                                                 |
| spectral_norm              | 70.0 ms                                                         | 73.1 ms: 1.04x slower                                                 |
| regex_effbot               | 1.82 ms                                                         | 1.90 ms: 1.05x slower                                                 |
| regex_dna                  | 112 ms                                                          | 119 ms: 1.06x slower                                                  |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                          |

Benchmark hidden because not significant (6): pylint, json_dumps, richards_super, generators, richards, xml_etree_parse
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20241001-3.13.0rc3-fae84c7/bm-20241001-pythonperf1_win32-x86-python-v3.13.0rc3-3.13.0rc3-fae84c7.json: asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.033x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown