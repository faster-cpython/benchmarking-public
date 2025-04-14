# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a1
- machine: windows-x86
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.056x faster
- HPT reliability: 53.80%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 264 ms: 1.03x slower                                                |
| docutils       | 1.80 sec                                                        | 2.07 sec: 1.15x slower                                              |
| sphinx         | 729 ms                                                          | 852 ms: 1.17x slower                                                |
| tornado_http   | 105 ms                                                          | 109 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                           | 1.08x slower                                                        |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 255 ms: 1.13x faster                                                |
| async_tree_none           | 245 ms                                                          | 219 ms: 1.12x faster                                                |
| async_tree_memoization    | 302 ms                                                          | 278 ms: 1.08x faster                                                |
| async_tree_none_tg        | 216 ms                                                          | 204 ms: 1.06x faster                                                |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 470 ms: 1.04x faster                                                |
| async_tree_io             | 530 ms                                                          | 523 ms: 1.01x faster                                                |
| coroutines                | 16.1 ms                                                         | 17.8 ms: 1.10x slower                                               |
| async_tree_io_tg          | 499 ms                                                          | 551 ms: 1.10x slower                                                |
| async_generators          | 267 ms                                                          | 325 ms: 1.22x slower                                                |
| Geometric mean            | (ref)                                                           | 1.00x faster                                                        |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 63.2 ms: 1.29x faster                                               |
| float          | 56.4 ms                                                         | 47.0 ms: 1.20x faster                                               |
| pidigits       | 204 ms                                                          | 200 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                           | 1.16x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 104 ms: 1.03x slower                                                |
| regex_dna      | 112 ms                                                          | 118 ms: 1.05x slower                                                |
| Geometric mean | (ref)                                                           | 1.02x slower                                                        |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|---------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads         | 1.74 sec                                                        | 1.56 sec: 1.11x faster                                              |
| xml_etree_generate  | 61.9 ms                                                         | 55.7 ms: 1.11x faster                                               |
| xml_etree_process   | 44.6 ms                                                         | 42.8 ms: 1.04x faster                                               |
| json_loads          | 21.7 us                                                         | 20.8 us: 1.04x faster                                               |
| pickle_pure_python  | 239 us                                                          | 246 us: 1.03x slower                                                |
| xml_etree_iterparse | 61.3 ms                                                         | 64.3 ms: 1.05x slower                                               |
| xml_etree_parse     | 102 ms                                                          | 109 ms: 1.06x slower                                                |
| json_dumps          | 7.53 ms                                                         | 8.11 ms: 1.08x slower                                               |
| Geometric mean      | (ref)                                                           | 1.01x faster                                                        |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.1 ms: 1.05x faster                                               |
| python_startup_no_site | 20.2 ms                                                         | 20.3 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 5.70 ms: 1.23x faster                                               |
| django_template | 32.0 ms                                                         | 33.6 ms: 1.05x slower                                               |
| genshi_xml      | 49.0 ms                                                         | 54.0 ms: 1.10x slower                                               |
| genshi_text     | 21.7 ms                                                         | 24.2 ms: 1.11x slower                                               |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                        |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| thrift                    | 10.3 ms                                                         | 770 us: 13.32x faster                                               |
| coverage                  | 326 ms                                                          | 53.8 ms: 6.07x faster                                               |
| deepcopy_memo             | 26.2 us                                                         | 16.2 us: 1.62x faster                                               |
| deepcopy                  | 311 us                                                          | 238 us: 1.30x faster                                                |
| nbody                     | 81.4 ms                                                         | 63.2 ms: 1.29x faster                                               |
| mako                      | 7.02 ms                                                         | 5.70 ms: 1.23x faster                                               |
| spectral_norm             | 70.0 ms                                                         | 57.2 ms: 1.22x faster                                               |
| scimark_sor               | 85.8 ms                                                         | 70.1 ms: 1.22x faster                                               |
| pprint_safe_repr          | 658 ms                                                          | 546 ms: 1.21x faster                                                |
| deepcopy_reduce           | 2.94 us                                                         | 2.44 us: 1.20x faster                                               |
| float                     | 56.4 ms                                                         | 47.0 ms: 1.20x faster                                               |
| pprint_pformat            | 1.32 sec                                                        | 1.12 sec: 1.18x faster                                              |
| scimark_monte_carlo       | 48.7 ms                                                         | 41.6 ms: 1.17x faster                                               |
| fannkuch                  | 288 ms                                                          | 249 ms: 1.15x faster                                                |
| go                        | 111 ms                                                          | 97.2 ms: 1.14x faster                                               |
| scimark_sparse_mat_mult   | 2.88 ms                                                         | 2.54 ms: 1.14x faster                                               |
| async_tree_memoization_tg | 287 ms                                                          | 255 ms: 1.13x faster                                                |
| async_tree_none           | 245 ms                                                          | 219 ms: 1.12x faster                                                |
| logging_silent            | 62.4 ns                                                         | 56.0 ns: 1.11x faster                                               |
| tomli_loads               | 1.74 sec                                                        | 1.56 sec: 1.11x faster                                              |
| xml_etree_generate        | 61.9 ms                                                         | 55.7 ms: 1.11x faster                                               |
| crypto_pyaes              | 56.6 ms                                                         | 51.9 ms: 1.09x faster                                               |
| scimark_fft               | 204 ms                                                          | 187 ms: 1.09x faster                                                |
| async_tree_memoization    | 302 ms                                                          | 278 ms: 1.08x faster                                                |
| meteor_contest            | 78.1 ms                                                         | 73.3 ms: 1.07x faster                                               |
| async_tree_none_tg        | 216 ms                                                          | 204 ms: 1.06x faster                                                |
| logging_simple            | 7.89 us                                                         | 7.54 us: 1.05x faster                                               |
| python_startup            | 28.3 ms                                                         | 27.1 ms: 1.05x faster                                               |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 470 ms: 1.04x faster                                                |
| xml_etree_process         | 44.6 ms                                                         | 42.8 ms: 1.04x faster                                               |
| pycparser                 | 869 ms                                                          | 834 ms: 1.04x faster                                                |
| json_loads                | 21.7 us                                                         | 20.8 us: 1.04x faster                                               |
| logging_format            | 8.59 us                                                         | 8.27 us: 1.04x faster                                               |
| bench_thread_pool         | 1.04 ms                                                         | 1.01 ms: 1.03x faster                                               |
| pyflate                   | 322 ms                                                          | 312 ms: 1.03x faster                                                |
| dulwich_log               | 50.2 ms                                                         | 49.3 ms: 1.02x faster                                               |
| pidigits                  | 204 ms                                                          | 200 ms: 1.02x faster                                                |
| async_tree_io             | 530 ms                                                          | 523 ms: 1.01x faster                                                |
| pathlib                   | 89.1 ms                                                         | 88.4 ms: 1.01x faster                                               |
| comprehensions            | 13.1 us                                                         | 13.0 us: 1.01x faster                                               |
| python_startup_no_site    | 20.2 ms                                                         | 20.3 ms: 1.01x slower                                               |
| bench_mp_pool             | 93.6 ms                                                         | 94.5 ms: 1.01x slower                                               |
| nqueens                   | 75.1 ms                                                         | 76.2 ms: 1.01x slower                                               |
| telco                     | 6.27 ms                                                         | 6.36 ms: 1.01x slower                                               |
| mdp                       | 1.70 sec                                                        | 1.73 sec: 1.02x slower                                              |
| pickle_pure_python        | 239 us                                                          | 246 us: 1.03x slower                                                |
| sqlglot_parse             | 1.02 ms                                                         | 1.05 ms: 1.03x slower                                               |
| gc_traversal              | 1.76 ms                                                         | 1.81 ms: 1.03x slower                                               |
| regex_compile             | 101 ms                                                          | 104 ms: 1.03x slower                                                |
| 2to3                      | 255 ms                                                          | 264 ms: 1.03x slower                                                |
| tornado_http              | 105 ms                                                          | 109 ms: 1.04x slower                                                |
| sympy_expand              | 377 ms                                                          | 394 ms: 1.04x slower                                                |
| regex_dna                 | 112 ms                                                          | 118 ms: 1.05x slower                                                |
| django_template           | 32.0 ms                                                         | 33.6 ms: 1.05x slower                                               |
| xml_etree_iterparse       | 61.3 ms                                                         | 64.3 ms: 1.05x slower                                               |
| typing_runtime_protocols  | 141 us                                                          | 148 us: 1.05x slower                                                |
| sympy_str                 | 214 ms                                                          | 227 ms: 1.06x slower                                                |
| xml_etree_parse           | 102 ms                                                          | 109 ms: 1.06x slower                                                |
| json_dumps                | 7.53 ms                                                         | 8.11 ms: 1.08x slower                                               |
| sympy_sum                 | 108 ms                                                          | 117 ms: 1.08x slower                                                |
| sqlglot_transpile         | 1.26 ms                                                         | 1.37 ms: 1.09x slower                                               |
| sqlglot_normalize         | 223 ms                                                          | 244 ms: 1.10x slower                                                |
| genshi_xml                | 49.0 ms                                                         | 54.0 ms: 1.10x slower                                               |
| coroutines                | 16.1 ms                                                         | 17.8 ms: 1.10x slower                                               |
| async_tree_io_tg          | 499 ms                                                          | 551 ms: 1.10x slower                                                |
| create_gc_cycles          | 1.08 ms                                                         | 1.20 ms: 1.11x slower                                               |
| genshi_text               | 21.7 ms                                                         | 24.2 ms: 1.11x slower                                               |
| deltablue                 | 2.35 ms                                                         | 2.64 ms: 1.12x slower                                               |
| chaos                     | 49.4 ms                                                         | 55.8 ms: 1.13x slower                                               |
| json                      | 4.40 ms                                                         | 5.03 ms: 1.14x slower                                               |
| docutils                  | 1.80 sec                                                        | 2.07 sec: 1.15x slower                                              |
| sympy_integrate           | 15.2 ms                                                         | 17.5 ms: 1.15x slower                                               |
| generators                | 21.5 ms                                                         | 25.1 ms: 1.17x slower                                               |
| sphinx                    | 729 ms                                                          | 852 ms: 1.17x slower                                                |
| hexiom                    | 4.60 ms                                                         | 5.38 ms: 1.17x slower                                               |
| sqlglot_optimize          | 42.4 ms                                                         | 50.3 ms: 1.19x slower                                               |
| richards                  | 33.4 ms                                                         | 40.2 ms: 1.20x slower                                               |
| async_generators          | 267 ms                                                          | 325 ms: 1.22x slower                                                |
| richards_super            | 37.0 ms                                                         | 45.6 ms: 1.23x slower                                               |
| pylint                    | 225 ms                                                          | 283 ms: 1.26x slower                                                |
| raytrace                  | 203 ms                                                          | 269 ms: 1.33x slower                                                |
| Geometric mean            | (ref)                                                           | 1.06x faster                                                        |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, regex_v8, scimark_lu, unpickle_pure_python, regex_effbot, html5lib
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241015-3.14.0a1-8cdaca8-JIT/bm-20241015-pythonperf1_win32-x86-python-v3.14.0a1-3.14.0a1-8cdaca8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.056x faster
# HPT report

- Reliability score: 53.80% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown