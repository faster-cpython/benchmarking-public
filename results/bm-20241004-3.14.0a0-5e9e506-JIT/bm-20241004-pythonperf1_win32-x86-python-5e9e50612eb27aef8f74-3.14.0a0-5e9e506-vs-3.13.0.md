# Results vs. 3.13.0

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: windows-x86
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.081x faster
- HPT reliability: 86.41%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 261 ms: 1.02x slower                                                           |
| docutils       | 1.80 sec                                                        | 2.04 sec: 1.14x slower                                                         |
| html5lib       | 47.1 ms                                                         | 46.9 ms: 1.00x faster                                                          |
| sphinx         | 729 ms                                                          | 848 ms: 1.16x slower                                                           |
| tornado_http   | 105 ms                                                          | 109 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 255 ms: 1.12x faster                                                           |
| async_tree_none           | 245 ms                                                          | 223 ms: 1.10x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 279 ms: 1.08x faster                                                           |
| async_tree_none_tg        | 216 ms                                                          | 201 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 468 ms: 1.05x faster                                                           |
| async_tree_io_tg          | 499 ms                                                          | 514 ms: 1.03x slower                                                           |
| coroutines                | 16.1 ms                                                         | 17.5 ms: 1.08x slower                                                          |
| async_generators          | 267 ms                                                          | 326 ms: 1.22x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_io, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 50.4 ms: 1.62x faster                                                          |
| float          | 56.4 ms                                                         | 46.2 ms: 1.22x faster                                                          |
| pidigits       | 204 ms                                                          | 199 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 15.3 ms: 1.01x faster                                                          |
| regex_compile  | 101 ms                                                          | 105 ms: 1.04x slower                                                           |
| regex_dna      | 112 ms                                                          | 116 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.74 sec                                                        | 1.51 sec: 1.15x faster                                                         |
| xml_etree_generate   | 61.9 ms                                                         | 54.7 ms: 1.13x faster                                                          |
| json_dumps           | 7.53 ms                                                         | 6.98 ms: 1.08x faster                                                          |
| xml_etree_process    | 44.6 ms                                                         | 41.5 ms: 1.07x faster                                                          |
| json_loads           | 21.7 us                                                         | 21.0 us: 1.03x faster                                                          |
| unpickle_pure_python | 162 us                                                          | 158 us: 1.02x faster                                                           |
| xml_etree_iterparse  | 61.3 ms                                                         | 64.5 ms: 1.05x slower                                                          |
| xml_etree_parse      | 102 ms                                                          | 109 ms: 1.07x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.8 ms: 1.06x faster                                                          |
| python_startup_no_site | 20.2 ms                                                         | 20.5 ms: 1.02x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako           | 7.02 ms                                                         | 5.57 ms: 1.26x faster                                                          |
| genshi_text    | 21.7 ms                                                         | 23.8 ms: 1.10x slower                                                          |
| genshi_xml     | 49.0 ms                                                         | 56.2 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 10.3 ms                                                         | 774 us: 13.25x faster                                                          |
| coverage                  | 326 ms                                                          | 53.5 ms: 6.10x faster                                                          |
| sqlglot_normalize         | 223 ms                                                          | 102 ms: 2.18x faster                                                           |
| deepcopy_memo             | 26.2 us                                                         | 16.0 us: 1.64x faster                                                          |
| nbody                     | 81.4 ms                                                         | 50.4 ms: 1.62x faster                                                          |
| deepcopy                  | 311 us                                                          | 234 us: 1.33x faster                                                           |
| mako                      | 7.02 ms                                                         | 5.57 ms: 1.26x faster                                                          |
| scimark_sor               | 85.8 ms                                                         | 68.5 ms: 1.25x faster                                                          |
| scimark_monte_carlo       | 48.7 ms                                                         | 39.0 ms: 1.25x faster                                                          |
| float                     | 56.4 ms                                                         | 46.2 ms: 1.22x faster                                                          |
| deepcopy_reduce           | 2.94 us                                                         | 2.43 us: 1.21x faster                                                          |
| spectral_norm             | 70.0 ms                                                         | 58.4 ms: 1.20x faster                                                          |
| fannkuch                  | 288 ms                                                          | 245 ms: 1.18x faster                                                           |
| pprint_safe_repr          | 658 ms                                                          | 565 ms: 1.16x faster                                                           |
| scimark_fft               | 204 ms                                                          | 177 ms: 1.15x faster                                                           |
| tomli_loads               | 1.74 sec                                                        | 1.51 sec: 1.15x faster                                                         |
| go                        | 111 ms                                                          | 97.1 ms: 1.14x faster                                                          |
| xml_etree_generate        | 61.9 ms                                                         | 54.7 ms: 1.13x faster                                                          |
| async_tree_memoization_tg | 287 ms                                                          | 255 ms: 1.12x faster                                                           |
| pprint_pformat            | 1.32 sec                                                        | 1.18 sec: 1.12x faster                                                         |
| scimark_sparse_mat_mult   | 2.88 ms                                                         | 2.60 ms: 1.11x faster                                                          |
| crypto_pyaes              | 56.6 ms                                                         | 51.2 ms: 1.11x faster                                                          |
| async_tree_none           | 245 ms                                                          | 223 ms: 1.10x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 279 ms: 1.08x faster                                                           |
| json_dumps                | 7.53 ms                                                         | 6.98 ms: 1.08x faster                                                          |
| xml_etree_process         | 44.6 ms                                                         | 41.5 ms: 1.07x faster                                                          |
| async_tree_none_tg        | 216 ms                                                          | 201 ms: 1.07x faster                                                           |
| comprehensions            | 13.1 us                                                         | 12.3 us: 1.07x faster                                                          |
| logging_silent            | 62.4 ns                                                         | 58.6 ns: 1.07x faster                                                          |
| python_startup            | 28.3 ms                                                         | 26.8 ms: 1.06x faster                                                          |
| pycparser                 | 869 ms                                                          | 822 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 468 ms: 1.05x faster                                                           |
| meteor_contest            | 78.1 ms                                                         | 75.0 ms: 1.04x faster                                                          |
| json                      | 4.40 ms                                                         | 4.22 ms: 1.04x faster                                                          |
| json_loads                | 21.7 us                                                         | 21.0 us: 1.03x faster                                                          |
| scimark_lu                | 60.7 ms                                                         | 59.1 ms: 1.03x faster                                                          |
| pidigits                  | 204 ms                                                          | 199 ms: 1.03x faster                                                           |
| unpickle_pure_python      | 162 us                                                          | 158 us: 1.02x faster                                                           |
| nqueens                   | 75.1 ms                                                         | 73.9 ms: 1.02x faster                                                          |
| pathlib                   | 89.1 ms                                                         | 87.8 ms: 1.01x faster                                                          |
| regex_v8                  | 15.5 ms                                                         | 15.3 ms: 1.01x faster                                                          |
| typing_runtime_protocols  | 141 us                                                          | 139 us: 1.01x faster                                                           |
| logging_format            | 8.59 us                                                         | 8.52 us: 1.01x faster                                                          |
| dulwich_log               | 50.2 ms                                                         | 49.8 ms: 1.01x faster                                                          |
| html5lib                  | 47.1 ms                                                         | 46.9 ms: 1.00x faster                                                          |
| bench_mp_pool             | 93.6 ms                                                         | 94.3 ms: 1.01x slower                                                          |
| gc_traversal              | 1.76 ms                                                         | 1.78 ms: 1.01x slower                                                          |
| pyflate                   | 322 ms                                                          | 325 ms: 1.01x slower                                                           |
| logging_simple            | 7.89 us                                                         | 8.02 us: 1.02x slower                                                          |
| python_startup_no_site    | 20.2 ms                                                         | 20.5 ms: 1.02x slower                                                          |
| telco                     | 6.27 ms                                                         | 6.42 ms: 1.02x slower                                                          |
| 2to3                      | 255 ms                                                          | 261 ms: 1.02x slower                                                           |
| async_tree_io_tg          | 499 ms                                                          | 514 ms: 1.03x slower                                                           |
| regex_compile             | 101 ms                                                          | 105 ms: 1.04x slower                                                           |
| regex_dna                 | 112 ms                                                          | 116 ms: 1.04x slower                                                           |
| sympy_expand              | 377 ms                                                          | 394 ms: 1.04x slower                                                           |
| tornado_http              | 105 ms                                                          | 109 ms: 1.05x slower                                                           |
| sqlglot_parse             | 1.02 ms                                                         | 1.07 ms: 1.05x slower                                                          |
| xml_etree_iterparse       | 61.3 ms                                                         | 64.5 ms: 1.05x slower                                                          |
| sympy_str                 | 214 ms                                                          | 227 ms: 1.06x slower                                                           |
| chaos                     | 49.4 ms                                                         | 52.4 ms: 1.06x slower                                                          |
| xml_etree_parse           | 102 ms                                                          | 109 ms: 1.07x slower                                                           |
| create_gc_cycles          | 1.08 ms                                                         | 1.16 ms: 1.07x slower                                                          |
| sqlglot_transpile         | 1.26 ms                                                         | 1.37 ms: 1.08x slower                                                          |
| coroutines                | 16.1 ms                                                         | 17.5 ms: 1.08x slower                                                          |
| sympy_sum                 | 108 ms                                                          | 117 ms: 1.09x slower                                                           |
| genshi_text               | 21.7 ms                                                         | 23.8 ms: 1.10x slower                                                          |
| deltablue                 | 2.35 ms                                                         | 2.63 ms: 1.12x slower                                                          |
| sympy_integrate           | 15.2 ms                                                         | 17.1 ms: 1.13x slower                                                          |
| docutils                  | 1.80 sec                                                        | 2.04 sec: 1.14x slower                                                         |
| genshi_xml                | 49.0 ms                                                         | 56.2 ms: 1.15x slower                                                          |
| sphinx                    | 729 ms                                                          | 848 ms: 1.16x slower                                                           |
| sqlglot_optimize          | 42.4 ms                                                         | 49.7 ms: 1.17x slower                                                          |
| hexiom                    | 4.60 ms                                                         | 5.48 ms: 1.19x slower                                                          |
| richards                  | 33.4 ms                                                         | 39.9 ms: 1.20x slower                                                          |
| richards_super            | 37.0 ms                                                         | 45.2 ms: 1.22x slower                                                          |
| async_generators          | 267 ms                                                          | 326 ms: 1.22x slower                                                           |
| pylint                    | 225 ms                                                          | 282 ms: 1.25x slower                                                           |
| raytrace                  | 203 ms                                                          | 255 ms: 1.26x slower                                                           |
| generators                | 21.5 ms                                                         | 27.1 ms: 1.26x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.08x faster                                                                   |

Benchmark hidden because not significant (7): bench_thread_pool, async_tree_io, async_tree_cpu_io_mixed_tg, regex_effbot, django_template, mdp, pickle_pure_python
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-pythonperf1_win32-x86-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.081x faster
# HPT report

- Reliability score: 86.41% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown