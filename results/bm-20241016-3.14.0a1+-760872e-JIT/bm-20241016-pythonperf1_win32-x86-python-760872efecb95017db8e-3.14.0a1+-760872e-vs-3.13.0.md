# Results vs. 3.13.0

- fork: python
- ref: 760872efecb95017db8e
- machine: windows-x86
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.066x faster
- HPT reliability: 64.85%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 265 ms: 1.04x slower                                                            |
| docutils       | 1.80 sec                                                        | 2.03 sec: 1.13x slower                                                          |
| html5lib       | 47.1 ms                                                         | 44.6 ms: 1.06x faster                                                           |
| sphinx         | 729 ms                                                          | 837 ms: 1.15x slower                                                            |
| tornado_http   | 105 ms                                                          | 108 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 255 ms: 1.13x faster                                                            |
| async_tree_none            | 245 ms                                                          | 219 ms: 1.12x faster                                                            |
| async_tree_memoization     | 302 ms                                                          | 274 ms: 1.10x faster                                                            |
| async_tree_none_tg         | 216 ms                                                          | 199 ms: 1.08x faster                                                            |
| async_tree_io              | 530 ms                                                          | 514 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 499 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 483 ms: 1.03x slower                                                            |
| coroutines                 | 16.1 ms                                                         | 17.4 ms: 1.08x slower                                                           |
| async_tree_io_tg           | 499 ms                                                          | 543 ms: 1.09x slower                                                            |
| async_generators           | 267 ms                                                          | 324 ms: 1.21x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.00x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 65.2 ms: 1.25x faster                                                           |
| float          | 56.4 ms                                                         | 46.1 ms: 1.22x faster                                                           |
| pidigits       | 204 ms                                                          | 201 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 15.4 ms: 1.01x faster                                                           |
| regex_effbot   | 1.82 ms                                                         | 1.86 ms: 1.02x slower                                                           |
| regex_compile  | 101 ms                                                          | 104 ms: 1.03x slower                                                            |
| regex_dna      | 112 ms                                                          | 118 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|---------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads         | 1.74 sec                                                        | 1.49 sec: 1.17x faster                                                          |
| xml_etree_generate  | 61.9 ms                                                         | 55.8 ms: 1.11x faster                                                           |
| xml_etree_process   | 44.6 ms                                                         | 40.5 ms: 1.10x faster                                                           |
| json_loads          | 21.7 us                                                         | 20.6 us: 1.05x faster                                                           |
| pickle_pure_python  | 239 us                                                          | 230 us: 1.04x faster                                                            |
| xml_etree_iterparse | 61.3 ms                                                         | 63.8 ms: 1.04x slower                                                           |
| xml_etree_parse     | 102 ms                                                          | 109 ms: 1.07x slower                                                            |
| json_dumps          | 7.53 ms                                                         | 8.31 ms: 1.10x slower                                                           |
| Geometric mean      | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.7 ms: 1.06x faster                                                           |
| python_startup_no_site | 20.2 ms                                                         | 20.4 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 7.02 ms                                                         | 5.75 ms: 1.22x faster                                                           |
| genshi_text    | 21.7 ms                                                         | 22.6 ms: 1.04x slower                                                           |
| genshi_xml     | 49.0 ms                                                         | 53.8 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 767 us: 13.37x faster                                                           |
| coverage                   | 326 ms                                                          | 53.5 ms: 6.10x faster                                                           |
| deepcopy_memo              | 26.2 us                                                         | 17.0 us: 1.55x faster                                                           |
| deepcopy                   | 311 us                                                          | 236 us: 1.32x faster                                                            |
| scimark_sor                | 85.8 ms                                                         | 68.5 ms: 1.25x faster                                                           |
| nbody                      | 81.4 ms                                                         | 65.2 ms: 1.25x faster                                                           |
| scimark_monte_carlo        | 48.7 ms                                                         | 39.6 ms: 1.23x faster                                                           |
| float                      | 56.4 ms                                                         | 46.1 ms: 1.22x faster                                                           |
| mako                       | 7.02 ms                                                         | 5.75 ms: 1.22x faster                                                           |
| deepcopy_reduce            | 2.94 us                                                         | 2.43 us: 1.21x faster                                                           |
| spectral_norm              | 70.0 ms                                                         | 57.8 ms: 1.21x faster                                                           |
| tomli_loads                | 1.74 sec                                                        | 1.49 sec: 1.17x faster                                                          |
| fannkuch                   | 288 ms                                                          | 248 ms: 1.16x faster                                                            |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 2.50 ms: 1.15x faster                                                           |
| go                         | 111 ms                                                          | 96.6 ms: 1.15x faster                                                           |
| scimark_fft                | 204 ms                                                          | 180 ms: 1.14x faster                                                            |
| crypto_pyaes               | 56.6 ms                                                         | 50.2 ms: 1.13x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 255 ms: 1.13x faster                                                            |
| pprint_safe_repr           | 658 ms                                                          | 585 ms: 1.12x faster                                                            |
| async_tree_none            | 245 ms                                                          | 219 ms: 1.12x faster                                                            |
| xml_etree_generate         | 61.9 ms                                                         | 55.8 ms: 1.11x faster                                                           |
| logging_silent             | 62.4 ns                                                         | 56.2 ns: 1.11x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 274 ms: 1.10x faster                                                            |
| xml_etree_process          | 44.6 ms                                                         | 40.5 ms: 1.10x faster                                                           |
| pprint_pformat             | 1.32 sec                                                        | 1.21 sec: 1.10x faster                                                          |
| meteor_contest             | 78.1 ms                                                         | 72.1 ms: 1.08x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 199 ms: 1.08x faster                                                            |
| logging_simple             | 7.89 us                                                         | 7.36 us: 1.07x faster                                                           |
| python_startup             | 28.3 ms                                                         | 26.7 ms: 1.06x faster                                                           |
| logging_format             | 8.59 us                                                         | 8.11 us: 1.06x faster                                                           |
| pycparser                  | 869 ms                                                          | 821 ms: 1.06x faster                                                            |
| html5lib                   | 47.1 ms                                                         | 44.6 ms: 1.06x faster                                                           |
| json_loads                 | 21.7 us                                                         | 20.6 us: 1.05x faster                                                           |
| bench_thread_pool          | 1.04 ms                                                         | 995 us: 1.05x faster                                                            |
| pickle_pure_python         | 239 us                                                          | 230 us: 1.04x faster                                                            |
| comprehensions             | 13.1 us                                                         | 12.7 us: 1.03x faster                                                           |
| async_tree_io              | 530 ms                                                          | 514 ms: 1.03x faster                                                            |
| telco                      | 6.27 ms                                                         | 6.08 ms: 1.03x faster                                                           |
| scimark_lu                 | 60.7 ms                                                         | 59.5 ms: 1.02x faster                                                           |
| pyflate                    | 322 ms                                                          | 316 ms: 1.02x faster                                                            |
| dulwich_log                | 50.2 ms                                                         | 49.5 ms: 1.01x faster                                                           |
| pidigits                   | 204 ms                                                          | 201 ms: 1.01x faster                                                            |
| regex_v8                   | 15.5 ms                                                         | 15.4 ms: 1.01x faster                                                           |
| nqueens                    | 75.1 ms                                                         | 74.6 ms: 1.01x faster                                                           |
| bench_mp_pool              | 93.6 ms                                                         | 94.3 ms: 1.01x slower                                                           |
| python_startup_no_site     | 20.2 ms                                                         | 20.4 ms: 1.01x slower                                                           |
| sqlglot_parse              | 1.02 ms                                                         | 1.04 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 499 ms: 1.02x slower                                                            |
| gc_traversal               | 1.76 ms                                                         | 1.80 ms: 1.02x slower                                                           |
| regex_effbot               | 1.82 ms                                                         | 1.86 ms: 1.02x slower                                                           |
| mdp                        | 1.70 sec                                                        | 1.74 sec: 1.03x slower                                                          |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 483 ms: 1.03x slower                                                            |
| regex_compile              | 101 ms                                                          | 104 ms: 1.03x slower                                                            |
| tornado_http               | 105 ms                                                          | 108 ms: 1.03x slower                                                            |
| 2to3                       | 255 ms                                                          | 265 ms: 1.04x slower                                                            |
| xml_etree_iterparse        | 61.3 ms                                                         | 63.8 ms: 1.04x slower                                                           |
| genshi_text                | 21.7 ms                                                         | 22.6 ms: 1.04x slower                                                           |
| sympy_expand               | 377 ms                                                          | 394 ms: 1.04x slower                                                            |
| regex_dna                  | 112 ms                                                          | 118 ms: 1.05x slower                                                            |
| sqlglot_transpile          | 1.26 ms                                                         | 1.34 ms: 1.06x slower                                                           |
| sympy_str                  | 214 ms                                                          | 229 ms: 1.07x slower                                                            |
| xml_etree_parse            | 102 ms                                                          | 109 ms: 1.07x slower                                                            |
| sqlglot_normalize          | 223 ms                                                          | 239 ms: 1.07x slower                                                            |
| sympy_sum                  | 108 ms                                                          | 116 ms: 1.08x slower                                                            |
| deltablue                  | 2.35 ms                                                         | 2.53 ms: 1.08x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 17.4 ms: 1.08x slower                                                           |
| async_tree_io_tg           | 499 ms                                                          | 543 ms: 1.09x slower                                                            |
| genshi_xml                 | 49.0 ms                                                         | 53.8 ms: 1.10x slower                                                           |
| json_dumps                 | 7.53 ms                                                         | 8.31 ms: 1.10x slower                                                           |
| create_gc_cycles           | 1.08 ms                                                         | 1.20 ms: 1.11x slower                                                           |
| chaos                      | 49.4 ms                                                         | 55.1 ms: 1.12x slower                                                           |
| docutils                   | 1.80 sec                                                        | 2.03 sec: 1.13x slower                                                          |
| json                       | 4.40 ms                                                         | 4.99 ms: 1.14x slower                                                           |
| richards_super             | 37.0 ms                                                         | 42.3 ms: 1.14x slower                                                           |
| sympy_integrate            | 15.2 ms                                                         | 17.4 ms: 1.14x slower                                                           |
| sphinx                     | 729 ms                                                          | 837 ms: 1.15x slower                                                            |
| richards                   | 33.4 ms                                                         | 38.3 ms: 1.15x slower                                                           |
| generators                 | 21.5 ms                                                         | 24.9 ms: 1.16x slower                                                           |
| sqlglot_optimize           | 42.4 ms                                                         | 49.2 ms: 1.16x slower                                                           |
| hexiom                     | 4.60 ms                                                         | 5.46 ms: 1.19x slower                                                           |
| async_generators           | 267 ms                                                          | 324 ms: 1.21x slower                                                            |
| pylint                     | 225 ms                                                          | 283 ms: 1.26x slower                                                            |
| raytrace                   | 203 ms                                                          | 271 ms: 1.34x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.07x faster                                                                    |

Benchmark hidden because not significant (4): pathlib, unpickle_pure_python, django_template, typing_runtime_protocols
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-pythonperf1_win32-x86-python-760872efecb95017db8e-3.14.0a1+-760872e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.066x faster
# HPT report

- Reliability score: 64.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown