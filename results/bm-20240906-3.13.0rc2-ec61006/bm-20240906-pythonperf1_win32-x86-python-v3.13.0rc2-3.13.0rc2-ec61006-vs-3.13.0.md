# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc2
- machine: windows-x86
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.030x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 245 ms: 1.04x faster                                                  |
| chameleon      | 6.24 ms                                                         | 5.83 ms: 1.07x faster                                                 |
| docutils       | 1.80 sec                                                        | 1.85 sec: 1.03x slower                                                |
| html5lib       | 47.1 ms                                                         | 45.7 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                           | 1.02x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 260 ms: 1.10x faster                                                  |
| async_tree_memoization     | 302 ms                                                          | 279 ms: 1.08x faster                                                  |
| async_tree_none            | 245 ms                                                          | 230 ms: 1.06x faster                                                  |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 452 ms: 1.04x faster                                                  |
| async_tree_none_tg         | 216 ms                                                          | 208 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 475 ms: 1.03x faster                                                  |
| coroutines                 | 16.1 ms                                                         | 16.0 ms: 1.01x faster                                                 |
| async_generators           | 267 ms                                                          | 278 ms: 1.04x slower                                                  |
| async_tree_io_tg           | 499 ms                                                          | 537 ms: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                          |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 56.4 ms                                                         | 53.5 ms: 1.05x faster                                                 |
| pidigits       | 204 ms                                                          | 199 ms: 1.02x faster                                                  |
| nbody          | 81.4 ms                                                         | 79.6 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                           | 1.03x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 15.9 ms: 1.03x slower                                                 |
| regex_effbot   | 1.82 ms                                                         | 1.88 ms: 1.04x slower                                                 |
| regex_dna      | 112 ms                                                          | 119 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                           | 1.03x slower                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 7.53 ms                                                         | 7.03 ms: 1.07x faster                                                 |
| json_loads           | 21.7 us                                                         | 20.6 us: 1.05x faster                                                 |
| tomli_loads          | 1.74 sec                                                        | 1.65 sec: 1.05x faster                                                |
| pickle_pure_python   | 239 us                                                          | 228 us: 1.05x faster                                                  |
| unpickle_pure_python | 162 us                                                          | 155 us: 1.04x faster                                                  |
| xml_etree_generate   | 61.9 ms                                                         | 62.2 ms: 1.01x slower                                                 |
| xml_etree_process    | 44.6 ms                                                         | 44.9 ms: 1.01x slower                                                 |
| xml_etree_parse      | 102 ms                                                          | 107 ms: 1.04x slower                                                  |
| xml_etree_iterparse  | 61.3 ms                                                         | 65.3 ms: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 24.2 ms: 1.17x faster                                                 |
| python_startup_no_site | 20.2 ms                                                         | 19.9 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                           | 1.09x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 43.9 ms: 1.12x faster                                                 |
| genshi_text     | 21.7 ms                                                         | 19.8 ms: 1.10x faster                                                 |
| django_template | 32.0 ms                                                         | 31.1 ms: 1.03x faster                                                 |
| mako            | 7.02 ms                                                         | 7.08 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                           | 1.06x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| create_gc_cycles           | 1.08 ms                                                         | 751 us: 1.44x faster                                                  |
| bench_mp_pool              | 93.6 ms                                                         | 73.1 ms: 1.28x faster                                                 |
| gc_traversal               | 1.76 ms                                                         | 1.44 ms: 1.22x faster                                                 |
| python_startup             | 28.3 ms                                                         | 24.2 ms: 1.17x faster                                                 |
| genshi_xml                 | 49.0 ms                                                         | 43.9 ms: 1.12x faster                                                 |
| async_tree_memoization_tg  | 287 ms                                                          | 260 ms: 1.10x faster                                                  |
| genshi_text                | 21.7 ms                                                         | 19.8 ms: 1.10x faster                                                 |
| deepcopy_reduce            | 2.94 us                                                         | 2.70 us: 1.09x faster                                                 |
| pycparser                  | 869 ms                                                          | 798 ms: 1.09x faster                                                  |
| async_tree_memoization     | 302 ms                                                          | 279 ms: 1.08x faster                                                  |
| pprint_safe_repr           | 658 ms                                                          | 608 ms: 1.08x faster                                                  |
| nqueens                    | 75.1 ms                                                         | 69.5 ms: 1.08x faster                                                 |
| deepcopy                   | 311 us                                                          | 288 us: 1.08x faster                                                  |
| chameleon                  | 6.24 ms                                                         | 5.83 ms: 1.07x faster                                                 |
| json_dumps                 | 7.53 ms                                                         | 7.03 ms: 1.07x faster                                                 |
| pylint                     | 225 ms                                                          | 210 ms: 1.07x faster                                                  |
| async_tree_none            | 245 ms                                                          | 230 ms: 1.06x faster                                                  |
| pprint_pformat             | 1.32 sec                                                        | 1.25 sec: 1.06x faster                                                |
| sqlglot_normalize          | 223 ms                                                          | 210 ms: 1.06x faster                                                  |
| float                      | 56.4 ms                                                         | 53.5 ms: 1.05x faster                                                 |
| json_loads                 | 21.7 us                                                         | 20.6 us: 1.05x faster                                                 |
| tomli_loads                | 1.74 sec                                                        | 1.65 sec: 1.05x faster                                                |
| comprehensions             | 13.1 us                                                         | 12.5 us: 1.05x faster                                                 |
| raytrace                   | 203 ms                                                          | 193 ms: 1.05x faster                                                  |
| deepcopy_memo              | 26.2 us                                                         | 24.9 us: 1.05x faster                                                 |
| pickle_pure_python         | 239 us                                                          | 228 us: 1.05x faster                                                  |
| sqlglot_optimize           | 42.4 ms                                                         | 40.6 ms: 1.04x faster                                                 |
| unpickle_pure_python       | 162 us                                                          | 155 us: 1.04x faster                                                  |
| 2to3                       | 255 ms                                                          | 245 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 452 ms: 1.04x faster                                                  |
| sqlglot_transpile          | 1.26 ms                                                         | 1.22 ms: 1.04x faster                                                 |
| async_tree_none_tg         | 216 ms                                                          | 208 ms: 1.04x faster                                                  |
| logging_silent             | 62.4 ns                                                         | 60.1 ns: 1.04x faster                                                 |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 475 ms: 1.03x faster                                                  |
| sqlglot_parse              | 1.02 ms                                                         | 989 us: 1.03x faster                                                  |
| meteor_contest             | 78.1 ms                                                         | 75.8 ms: 1.03x faster                                                 |
| html5lib                   | 47.1 ms                                                         | 45.7 ms: 1.03x faster                                                 |
| django_template            | 32.0 ms                                                         | 31.1 ms: 1.03x faster                                                 |
| json                       | 4.40 ms                                                         | 4.27 ms: 1.03x faster                                                 |
| go                         | 111 ms                                                          | 108 ms: 1.03x faster                                                  |
| mdp                        | 1.70 sec                                                        | 1.65 sec: 1.03x faster                                                |
| sympy_expand               | 377 ms                                                          | 368 ms: 1.02x faster                                                  |
| pidigits                   | 204 ms                                                          | 199 ms: 1.02x faster                                                  |
| nbody                      | 81.4 ms                                                         | 79.6 ms: 1.02x faster                                                 |
| crypto_pyaes               | 56.6 ms                                                         | 55.4 ms: 1.02x faster                                                 |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 2.82 ms: 1.02x faster                                                 |
| sympy_integrate            | 15.2 ms                                                         | 14.9 ms: 1.02x faster                                                 |
| dulwich_log                | 50.2 ms                                                         | 49.2 ms: 1.02x faster                                                 |
| typing_runtime_protocols   | 141 us                                                          | 139 us: 1.02x faster                                                  |
| sympy_str                  | 214 ms                                                          | 211 ms: 1.02x faster                                                  |
| sympy_sum                  | 108 ms                                                          | 106 ms: 1.01x faster                                                  |
| logging_simple             | 7.89 us                                                         | 7.79 us: 1.01x faster                                                 |
| thrift                     | 10.3 ms                                                         | 10.1 ms: 1.01x faster                                                 |
| python_startup_no_site     | 20.2 ms                                                         | 19.9 ms: 1.01x faster                                                 |
| logging_format             | 8.59 us                                                         | 8.48 us: 1.01x faster                                                 |
| chaos                      | 49.4 ms                                                         | 48.9 ms: 1.01x faster                                                 |
| fannkuch                   | 288 ms                                                          | 286 ms: 1.01x faster                                                  |
| coroutines                 | 16.1 ms                                                         | 16.0 ms: 1.01x faster                                                 |
| coverage                   | 326 ms                                                          | 324 ms: 1.01x faster                                                  |
| xml_etree_generate         | 61.9 ms                                                         | 62.2 ms: 1.01x slower                                                 |
| xml_etree_process          | 44.6 ms                                                         | 44.9 ms: 1.01x slower                                                 |
| mako                       | 7.02 ms                                                         | 7.08 ms: 1.01x slower                                                 |
| scimark_monte_carlo        | 48.7 ms                                                         | 49.2 ms: 1.01x slower                                                 |
| generators                 | 21.5 ms                                                         | 21.8 ms: 1.01x slower                                                 |
| richards_super             | 37.0 ms                                                         | 37.7 ms: 1.02x slower                                                 |
| scimark_sor                | 85.8 ms                                                         | 87.5 ms: 1.02x slower                                                 |
| scimark_lu                 | 60.7 ms                                                         | 62.0 ms: 1.02x slower                                                 |
| regex_v8                   | 15.5 ms                                                         | 15.9 ms: 1.03x slower                                                 |
| docutils                   | 1.80 sec                                                        | 1.85 sec: 1.03x slower                                                |
| regex_effbot               | 1.82 ms                                                         | 1.88 ms: 1.04x slower                                                 |
| xml_etree_parse            | 102 ms                                                          | 107 ms: 1.04x slower                                                  |
| async_generators           | 267 ms                                                          | 278 ms: 1.04x slower                                                  |
| telco                      | 6.27 ms                                                         | 6.56 ms: 1.05x slower                                                 |
| regex_dna                  | 112 ms                                                          | 119 ms: 1.06x slower                                                  |
| xml_etree_iterparse        | 61.3 ms                                                         | 65.3 ms: 1.07x slower                                                 |
| async_tree_io_tg           | 499 ms                                                          | 537 ms: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                          |

Benchmark hidden because not significant (11): bench_thread_pool, pyflate, tornado_http, pathlib, deltablue, hexiom, richards, regex_compile, scimark_fft, spectral_norm, async_tree_io
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-pythonperf1_win32-x86-python-v3.13.0rc2-3.13.0rc2-ec61006.json: asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.030x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown