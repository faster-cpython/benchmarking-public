# Results vs. 3.13.0

- fork: brandtbucher
- ref: nojit
- machine: windows-x86
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.023x faster
- HPT reliability: 99.65%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 253 ms: 1.01x faster                                                  |
| docutils       | 1.80 sec                                                        | 1.86 sec: 1.04x slower                                                |
| tornado_http   | 105 ms                                                          | 95.1 ms: 1.10x faster                                                 |
| Geometric mean | (ref)                                                           | 1.02x faster                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 250 ms: 1.15x faster                                                  |
| async_tree_none            | 245 ms                                                          | 217 ms: 1.13x faster                                                  |
| async_tree_memoization     | 302 ms                                                          | 270 ms: 1.12x faster                                                  |
| async_tree_none_tg         | 216 ms                                                          | 200 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 470 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 463 ms: 1.01x faster                                                  |
| async_tree_io              | 530 ms                                                          | 540 ms: 1.02x slower                                                  |
| async_tree_io_tg           | 499 ms                                                          | 520 ms: 1.04x slower                                                  |
| async_generators           | 267 ms                                                          | 307 ms: 1.15x slower                                                  |
| coroutines                 | 16.1 ms                                                         | 18.7 ms: 1.16x slower                                                 |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 197 ms: 1.03x faster                                                  |
| nbody          | 81.4 ms                                                         | 90.2 ms: 1.11x slower                                                 |
| float          | 56.4 ms                                                         | 63.2 ms: 1.12x slower                                                 |
| Geometric mean | (ref)                                                           | 1.06x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 16.2 ms: 1.05x slower                                                 |
| regex_effbot   | 1.82 ms                                                         | 1.91 ms: 1.05x slower                                                 |
| regex_dna      | 112 ms                                                          | 119 ms: 1.06x slower                                                  |
| regex_compile  | 101 ms                                                          | 108 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                           | 1.06x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.6 us: 1.05x faster                                                 |
| xml_etree_parse      | 102 ms                                                          | 108 ms: 1.05x slower                                                  |
| tomli_loads          | 1.74 sec                                                        | 1.84 sec: 1.06x slower                                                |
| xml_etree_generate   | 61.9 ms                                                         | 67.0 ms: 1.08x slower                                                 |
| pickle_pure_python   | 239 us                                                          | 260 us: 1.09x slower                                                  |
| xml_etree_process    | 44.6 ms                                                         | 48.6 ms: 1.09x slower                                                 |
| xml_etree_iterparse  | 61.3 ms                                                         | 68.9 ms: 1.12x slower                                                 |
| unpickle_pure_python | 162 us                                                          | 182 us: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 23.7 ms: 1.20x faster                                                 |
| python_startup_no_site | 20.2 ms                                                         | 19.6 ms: 1.03x faster                                                 |
| Geometric mean         | (ref)                                                           | 1.11x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml     | 49.0 ms                                                         | 47.6 ms: 1.03x faster                                                 |
| genshi_text    | 21.7 ms                                                         | 22.2 ms: 1.02x slower                                                 |
| mako           | 7.02 ms                                                         | 8.30 ms: 1.18x slower                                                 |
| Geometric mean | (ref)                                                           | 1.04x slower                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 766 us: 13.39x faster                                                 |
| coverage                   | 326 ms                                                          | 53.2 ms: 6.13x faster                                                 |
| create_gc_cycles           | 1.08 ms                                                         | 735 us: 1.47x faster                                                  |
| bench_mp_pool              | 93.6 ms                                                         | 72.2 ms: 1.30x faster                                                 |
| gc_traversal               | 1.76 ms                                                         | 1.41 ms: 1.25x faster                                                 |
| deepcopy                   | 311 us                                                          | 249 us: 1.25x faster                                                  |
| deepcopy_reduce            | 2.94 us                                                         | 2.42 us: 1.22x faster                                                 |
| python_startup             | 28.3 ms                                                         | 23.7 ms: 1.20x faster                                                 |
| async_tree_memoization_tg  | 287 ms                                                          | 250 ms: 1.15x faster                                                  |
| deepcopy_memo              | 26.2 us                                                         | 23.1 us: 1.13x faster                                                 |
| async_tree_none            | 245 ms                                                          | 217 ms: 1.13x faster                                                  |
| async_tree_memoization     | 302 ms                                                          | 270 ms: 1.12x faster                                                  |
| tornado_http               | 105 ms                                                          | 95.1 ms: 1.10x faster                                                 |
| async_tree_none_tg         | 216 ms                                                          | 200 ms: 1.08x faster                                                  |
| pathlib                    | 89.1 ms                                                         | 83.8 ms: 1.06x faster                                                 |
| json                       | 4.40 ms                                                         | 4.16 ms: 1.06x faster                                                 |
| json_loads                 | 21.7 us                                                         | 20.6 us: 1.05x faster                                                 |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 470 ms: 1.04x faster                                                  |
| pprint_safe_repr           | 658 ms                                                          | 636 ms: 1.03x faster                                                  |
| pidigits                   | 204 ms                                                          | 197 ms: 1.03x faster                                                  |
| genshi_xml                 | 49.0 ms                                                         | 47.6 ms: 1.03x faster                                                 |
| python_startup_no_site     | 20.2 ms                                                         | 19.6 ms: 1.03x faster                                                 |
| go                         | 111 ms                                                          | 109 ms: 1.02x faster                                                  |
| pycparser                  | 869 ms                                                          | 854 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 463 ms: 1.01x faster                                                  |
| 2to3                       | 255 ms                                                          | 253 ms: 1.01x faster                                                  |
| pprint_pformat             | 1.32 sec                                                        | 1.32 sec: 1.00x faster                                                |
| sympy_expand               | 377 ms                                                          | 380 ms: 1.01x slower                                                  |
| sympy_str                  | 214 ms                                                          | 217 ms: 1.01x slower                                                  |
| dulwich_log                | 50.2 ms                                                         | 50.8 ms: 1.01x slower                                                 |
| sympy_integrate            | 15.2 ms                                                         | 15.5 ms: 1.02x slower                                                 |
| async_tree_io              | 530 ms                                                          | 540 ms: 1.02x slower                                                  |
| logging_format             | 8.59 us                                                         | 8.76 us: 1.02x slower                                                 |
| sqlglot_optimize           | 42.4 ms                                                         | 43.4 ms: 1.02x slower                                                 |
| crypto_pyaes               | 56.6 ms                                                         | 57.9 ms: 1.02x slower                                                 |
| genshi_text                | 21.7 ms                                                         | 22.2 ms: 1.02x slower                                                 |
| logging_simple             | 7.89 us                                                         | 8.09 us: 1.02x slower                                                 |
| sqlglot_normalize          | 223 ms                                                          | 230 ms: 1.03x slower                                                  |
| docutils                   | 1.80 sec                                                        | 1.86 sec: 1.04x slower                                                |
| nqueens                    | 75.1 ms                                                         | 78.2 ms: 1.04x slower                                                 |
| async_tree_io_tg           | 499 ms                                                          | 520 ms: 1.04x slower                                                  |
| telco                      | 6.27 ms                                                         | 6.54 ms: 1.04x slower                                                 |
| mdp                        | 1.70 sec                                                        | 1.77 sec: 1.04x slower                                                |
| regex_v8                   | 15.5 ms                                                         | 16.2 ms: 1.05x slower                                                 |
| meteor_contest             | 78.1 ms                                                         | 81.8 ms: 1.05x slower                                                 |
| regex_effbot               | 1.82 ms                                                         | 1.91 ms: 1.05x slower                                                 |
| xml_etree_parse            | 102 ms                                                          | 108 ms: 1.05x slower                                                  |
| tomli_loads                | 1.74 sec                                                        | 1.84 sec: 1.06x slower                                                |
| regex_dna                  | 112 ms                                                          | 119 ms: 1.06x slower                                                  |
| regex_compile              | 101 ms                                                          | 108 ms: 1.07x slower                                                  |
| sqlglot_transpile          | 1.26 ms                                                         | 1.36 ms: 1.08x slower                                                 |
| sqlglot_parse              | 1.02 ms                                                         | 1.10 ms: 1.08x slower                                                 |
| xml_etree_generate         | 61.9 ms                                                         | 67.0 ms: 1.08x slower                                                 |
| pickle_pure_python         | 239 us                                                          | 260 us: 1.09x slower                                                  |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.13 ms: 1.09x slower                                                 |
| xml_etree_process          | 44.6 ms                                                         | 48.6 ms: 1.09x slower                                                 |
| chaos                      | 49.4 ms                                                         | 54.6 ms: 1.11x slower                                                 |
| nbody                      | 81.4 ms                                                         | 90.2 ms: 1.11x slower                                                 |
| comprehensions             | 13.1 us                                                         | 14.6 us: 1.11x slower                                                 |
| float                      | 56.4 ms                                                         | 63.2 ms: 1.12x slower                                                 |
| xml_etree_iterparse        | 61.3 ms                                                         | 68.9 ms: 1.12x slower                                                 |
| unpickle_pure_python       | 162 us                                                          | 182 us: 1.13x slower                                                  |
| pyflate                    | 322 ms                                                          | 364 ms: 1.13x slower                                                  |
| async_generators           | 267 ms                                                          | 307 ms: 1.15x slower                                                  |
| coroutines                 | 16.1 ms                                                         | 18.7 ms: 1.16x slower                                                 |
| scimark_fft                | 204 ms                                                          | 236 ms: 1.16x slower                                                  |
| hexiom                     | 4.60 ms                                                         | 5.33 ms: 1.16x slower                                                 |
| raytrace                   | 203 ms                                                          | 237 ms: 1.17x slower                                                  |
| spectral_norm              | 70.0 ms                                                         | 82.1 ms: 1.17x slower                                                 |
| scimark_lu                 | 60.7 ms                                                         | 71.7 ms: 1.18x slower                                                 |
| mako                       | 7.02 ms                                                         | 8.30 ms: 1.18x slower                                                 |
| fannkuch                   | 288 ms                                                          | 341 ms: 1.18x slower                                                  |
| deltablue                  | 2.35 ms                                                         | 2.82 ms: 1.20x slower                                                 |
| scimark_monte_carlo        | 48.7 ms                                                         | 58.6 ms: 1.20x slower                                                 |
| logging_silent             | 62.4 ns                                                         | 75.2 ns: 1.20x slower                                                 |
| richards                   | 33.4 ms                                                         | 40.5 ms: 1.21x slower                                                 |
| scimark_sor                | 85.8 ms                                                         | 105 ms: 1.22x slower                                                  |
| richards_super             | 37.0 ms                                                         | 45.6 ms: 1.23x slower                                                 |
| generators                 | 21.5 ms                                                         | 27.2 ms: 1.26x slower                                                 |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                          |

Benchmark hidden because not significant (7): bench_thread_pool, html5lib, sympy_sum, django_template, json_dumps, typing_runtime_protocols, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-pythonperf1_win32-x86-brandtbucher-nojit-3.14.0a0-a6f1035.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.023x faster
# HPT report

- Reliability score: 99.65% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown