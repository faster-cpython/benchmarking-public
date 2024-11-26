# Results vs. 3.13.0

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: windows-x86
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.112x faster
- HPT reliability: 95.83%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 264 ms: 1.03x slower                                                           |
| docutils       | 1.80 sec                                                        | 2.01 sec: 1.12x slower                                                         |
| html5lib       | 47.1 ms                                                         | 46.3 ms: 1.02x faster                                                          |
| tornado_http   | 105 ms                                                          | 110 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 256 ms: 1.12x faster                                                           |
| async_tree_none            | 245 ms                                                          | 220 ms: 1.11x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 276 ms: 1.10x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 201 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 470 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 465 ms: 1.01x faster                                                           |
| async_tree_io              | 530 ms                                                          | 544 ms: 1.03x slower                                                           |
| async_tree_io_tg           | 499 ms                                                          | 524 ms: 1.05x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 18.5 ms: 1.15x slower                                                          |
| async_generators           | 267 ms                                                          | 322 ms: 1.21x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.00x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 50.1 ms: 1.62x faster                                                          |
| float          | 56.4 ms                                                         | 44.5 ms: 1.27x faster                                                          |
| pidigits       | 204 ms                                                          | 198 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                           | 1.29x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 15.9 ms: 1.02x slower                                                          |
| regex_effbot   | 1.82 ms                                                         | 2.00 ms: 1.10x slower                                                          |
| regex_dna      | 112 ms                                                          | 129 ms: 1.15x slower                                                           |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|---------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads         | 1.74 sec                                                        | 1.48 sec: 1.17x faster                                                         |
| xml_etree_generate  | 61.9 ms                                                         | 53.3 ms: 1.16x faster                                                          |
| xml_etree_process   | 44.6 ms                                                         | 40.1 ms: 1.11x faster                                                          |
| json_dumps          | 7.53 ms                                                         | 6.92 ms: 1.09x faster                                                          |
| json_loads          | 21.7 us                                                         | 20.6 us: 1.05x faster                                                          |
| pickle_pure_python  | 239 us                                                          | 241 us: 1.01x slower                                                           |
| xml_etree_iterparse | 61.3 ms                                                         | 62.4 ms: 1.02x slower                                                          |
| xml_etree_parse     | 102 ms                                                          | 105 ms: 1.03x slower                                                           |
| Geometric mean      | (ref)                                                           | 1.06x faster                                                                   |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.0 ms: 1.13x faster                                                          |
| python_startup_no_site | 20.2 ms                                                         | 20.9 ms: 1.04x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 5.57 ms: 1.26x faster                                                          |
| django_template | 32.0 ms                                                         | 33.5 ms: 1.05x slower                                                          |
| genshi_text     | 21.7 ms                                                         | 23.7 ms: 1.09x slower                                                          |
| genshi_xml      | 49.0 ms                                                         | 55.6 ms: 1.13x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 756 us: 13.57x faster                                                          |
| coverage                   | 326 ms                                                          | 54.7 ms: 5.97x faster                                                          |
| sqlglot_normalize          | 223 ms                                                          | 100 ms: 2.22x faster                                                           |
| deepcopy_memo              | 26.2 us                                                         | 15.7 us: 1.67x faster                                                          |
| nbody                      | 81.4 ms                                                         | 50.1 ms: 1.62x faster                                                          |
| create_gc_cycles           | 1.08 ms                                                         | 752 us: 1.44x faster                                                           |
| spectral_norm              | 70.0 ms                                                         | 49.2 ms: 1.42x faster                                                          |
| deepcopy                   | 311 us                                                          | 232 us: 1.34x faster                                                           |
| float                      | 56.4 ms                                                         | 44.5 ms: 1.27x faster                                                          |
| scimark_sor                | 85.8 ms                                                         | 68.1 ms: 1.26x faster                                                          |
| mako                       | 7.02 ms                                                         | 5.57 ms: 1.26x faster                                                          |
| gc_traversal               | 1.76 ms                                                         | 1.44 ms: 1.23x faster                                                          |
| fannkuch                   | 288 ms                                                          | 237 ms: 1.22x faster                                                           |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 2.40 ms: 1.20x faster                                                          |
| scimark_fft                | 204 ms                                                          | 172 ms: 1.19x faster                                                           |
| tomli_loads                | 1.74 sec                                                        | 1.48 sec: 1.17x faster                                                         |
| crypto_pyaes               | 56.6 ms                                                         | 48.4 ms: 1.17x faster                                                          |
| pyflate                    | 322 ms                                                          | 275 ms: 1.17x faster                                                           |
| bench_mp_pool              | 93.6 ms                                                         | 80.2 ms: 1.17x faster                                                          |
| deepcopy_reduce            | 2.94 us                                                         | 2.52 us: 1.17x faster                                                          |
| xml_etree_generate         | 61.9 ms                                                         | 53.3 ms: 1.16x faster                                                          |
| deltablue                  | 2.35 ms                                                         | 2.04 ms: 1.15x faster                                                          |
| pprint_safe_repr           | 658 ms                                                          | 574 ms: 1.15x faster                                                           |
| python_startup             | 28.3 ms                                                         | 25.0 ms: 1.13x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 256 ms: 1.12x faster                                                           |
| go                         | 111 ms                                                          | 98.9 ms: 1.12x faster                                                          |
| async_tree_none            | 245 ms                                                          | 220 ms: 1.11x faster                                                           |
| xml_etree_process          | 44.6 ms                                                         | 40.1 ms: 1.11x faster                                                          |
| comprehensions             | 13.1 us                                                         | 12.0 us: 1.10x faster                                                          |
| pprint_pformat             | 1.32 sec                                                        | 1.20 sec: 1.10x faster                                                         |
| async_tree_memoization     | 302 ms                                                          | 276 ms: 1.10x faster                                                           |
| json                       | 4.40 ms                                                         | 4.03 ms: 1.09x faster                                                          |
| json_dumps                 | 7.53 ms                                                         | 6.92 ms: 1.09x faster                                                          |
| async_tree_none_tg         | 216 ms                                                          | 201 ms: 1.07x faster                                                           |
| pycparser                  | 869 ms                                                          | 821 ms: 1.06x faster                                                           |
| telco                      | 6.27 ms                                                         | 5.93 ms: 1.06x faster                                                          |
| json_loads                 | 21.7 us                                                         | 20.6 us: 1.05x faster                                                          |
| meteor_contest             | 78.1 ms                                                         | 74.5 ms: 1.05x faster                                                          |
| bench_thread_pool          | 1.04 ms                                                         | 996 us: 1.05x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 470 ms: 1.04x faster                                                           |
| pidigits                   | 204 ms                                                          | 198 ms: 1.03x faster                                                           |
| richards_super             | 37.0 ms                                                         | 36.2 ms: 1.02x faster                                                          |
| pathlib                    | 89.1 ms                                                         | 87.4 ms: 1.02x faster                                                          |
| logging_simple             | 7.89 us                                                         | 7.75 us: 1.02x faster                                                          |
| html5lib                   | 47.1 ms                                                         | 46.3 ms: 1.02x faster                                                          |
| richards                   | 33.4 ms                                                         | 32.9 ms: 1.02x faster                                                          |
| logging_silent             | 62.4 ns                                                         | 61.5 ns: 1.02x faster                                                          |
| logging_format             | 8.59 us                                                         | 8.46 us: 1.02x faster                                                          |
| mdp                        | 1.70 sec                                                        | 1.68 sec: 1.01x faster                                                         |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 465 ms: 1.01x faster                                                           |
| dulwich_log                | 50.2 ms                                                         | 49.8 ms: 1.01x faster                                                          |
| scimark_lu                 | 60.7 ms                                                         | 60.3 ms: 1.01x faster                                                          |
| pickle_pure_python         | 239 us                                                          | 241 us: 1.01x slower                                                           |
| xml_etree_iterparse        | 61.3 ms                                                         | 62.4 ms: 1.02x slower                                                          |
| scimark_monte_carlo        | 48.7 ms                                                         | 49.6 ms: 1.02x slower                                                          |
| sqlglot_parse              | 1.02 ms                                                         | 1.04 ms: 1.02x slower                                                          |
| regex_v8                   | 15.5 ms                                                         | 15.9 ms: 1.02x slower                                                          |
| async_tree_io              | 530 ms                                                          | 544 ms: 1.03x slower                                                           |
| xml_etree_parse            | 102 ms                                                          | 105 ms: 1.03x slower                                                           |
| typing_runtime_protocols   | 141 us                                                          | 145 us: 1.03x slower                                                           |
| 2to3                       | 255 ms                                                          | 264 ms: 1.03x slower                                                           |
| python_startup_no_site     | 20.2 ms                                                         | 20.9 ms: 1.04x slower                                                          |
| sympy_str                  | 214 ms                                                          | 224 ms: 1.04x slower                                                           |
| django_template            | 32.0 ms                                                         | 33.5 ms: 1.05x slower                                                          |
| tornado_http               | 105 ms                                                          | 110 ms: 1.05x slower                                                           |
| async_tree_io_tg           | 499 ms                                                          | 524 ms: 1.05x slower                                                           |
| nqueens                    | 75.1 ms                                                         | 79.3 ms: 1.06x slower                                                          |
| sympy_expand               | 377 ms                                                          | 402 ms: 1.06x slower                                                           |
| sympy_sum                  | 108 ms                                                          | 115 ms: 1.07x slower                                                           |
| sqlglot_transpile          | 1.26 ms                                                         | 1.35 ms: 1.07x slower                                                          |
| hexiom                     | 4.60 ms                                                         | 4.96 ms: 1.08x slower                                                          |
| genshi_text                | 21.7 ms                                                         | 23.7 ms: 1.09x slower                                                          |
| generators                 | 21.5 ms                                                         | 23.6 ms: 1.10x slower                                                          |
| regex_effbot               | 1.82 ms                                                         | 2.00 ms: 1.10x slower                                                          |
| sympy_integrate            | 15.2 ms                                                         | 16.8 ms: 1.10x slower                                                          |
| sqlglot_optimize           | 42.4 ms                                                         | 46.8 ms: 1.10x slower                                                          |
| chaos                      | 49.4 ms                                                         | 55.0 ms: 1.11x slower                                                          |
| docutils                   | 1.80 sec                                                        | 2.01 sec: 1.12x slower                                                         |
| genshi_xml                 | 49.0 ms                                                         | 55.6 ms: 1.13x slower                                                          |
| coroutines                 | 16.1 ms                                                         | 18.5 ms: 1.15x slower                                                          |
| regex_dna                  | 112 ms                                                          | 129 ms: 1.15x slower                                                           |
| pylint                     | 225 ms                                                          | 270 ms: 1.20x slower                                                           |
| async_generators           | 267 ms                                                          | 322 ms: 1.21x slower                                                           |
| raytrace                   | 203 ms                                                          | 248 ms: 1.23x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                                   |

Benchmark hidden because not significant (2): unpickle_pure_python, regex_compile
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.112x faster
# HPT report

- Reliability score: 95.83% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown