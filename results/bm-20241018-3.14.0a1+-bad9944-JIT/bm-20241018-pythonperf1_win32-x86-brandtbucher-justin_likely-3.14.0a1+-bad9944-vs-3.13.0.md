# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_likely
- machine: windows-x86
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.063x faster
- HPT reliability: 66.85%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 266 ms: 1.04x slower                                                           |
| docutils       | 1.80 sec                                                        | 2.05 sec: 1.14x slower                                                         |
| html5lib       | 47.1 ms                                                         | 46.0 ms: 1.02x faster                                                          |
| sphinx         | 729 ms                                                          | 849 ms: 1.16x slower                                                           |
| tornado_http   | 105 ms                                                          | 109 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 251 ms: 1.14x faster                                                           |
| async_tree_none            | 245 ms                                                          | 215 ms: 1.14x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 273 ms: 1.11x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 201 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 465 ms: 1.05x faster                                                           |
| async_tree_io              | 530 ms                                                          | 510 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 464 ms: 1.01x faster                                                           |
| coroutines                 | 16.1 ms                                                         | 17.5 ms: 1.09x slower                                                          |
| async_tree_io_tg           | 499 ms                                                          | 547 ms: 1.09x slower                                                           |
| async_generators           | 267 ms                                                          | 322 ms: 1.21x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 59.6 ms: 1.37x faster                                                          |
| float          | 56.4 ms                                                         | 45.7 ms: 1.23x faster                                                          |
| pidigits       | 204 ms                                                          | 199 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.20x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.82 ms                                                         | 1.76 ms: 1.03x faster                                                          |
| regex_v8       | 15.5 ms                                                         | 15.6 ms: 1.01x slower                                                          |
| regex_compile  | 101 ms                                                          | 106 ms: 1.05x slower                                                           |
| regex_dna      | 112 ms                                                          | 118 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.74 sec                                                        | 1.51 sec: 1.15x faster                                                         |
| xml_etree_generate   | 61.9 ms                                                         | 56.1 ms: 1.10x faster                                                          |
| json_loads           | 21.7 us                                                         | 20.5 us: 1.06x faster                                                          |
| xml_etree_process    | 44.6 ms                                                         | 42.3 ms: 1.05x faster                                                          |
| unpickle_pure_python | 162 us                                                          | 164 us: 1.02x slower                                                           |
| xml_etree_iterparse  | 61.3 ms                                                         | 64.0 ms: 1.04x slower                                                          |
| pickle_pure_python   | 239 us                                                          | 251 us: 1.05x slower                                                           |
| xml_etree_parse      | 102 ms                                                          | 110 ms: 1.08x slower                                                           |
| json_dumps           | 7.53 ms                                                         | 8.74 ms: 1.16x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.00x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 26.9 ms: 1.05x faster                                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 5.78 ms: 1.21x faster                                                          |
| django_template | 32.0 ms                                                         | 33.1 ms: 1.03x slower                                                          |
| genshi_text     | 21.7 ms                                                         | 22.9 ms: 1.05x slower                                                          |
| genshi_xml      | 49.0 ms                                                         | 53.7 ms: 1.10x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.00x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 790 us: 12.98x faster                                                          |
| coverage                   | 326 ms                                                          | 52.7 ms: 6.19x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 16.7 us: 1.57x faster                                                          |
| nbody                      | 81.4 ms                                                         | 59.6 ms: 1.37x faster                                                          |
| deepcopy                   | 311 us                                                          | 231 us: 1.35x faster                                                           |
| scimark_sor                | 85.8 ms                                                         | 69.2 ms: 1.24x faster                                                          |
| deepcopy_reduce            | 2.94 us                                                         | 2.38 us: 1.24x faster                                                          |
| float                      | 56.4 ms                                                         | 45.7 ms: 1.23x faster                                                          |
| scimark_monte_carlo        | 48.7 ms                                                         | 39.6 ms: 1.23x faster                                                          |
| mako                       | 7.02 ms                                                         | 5.78 ms: 1.21x faster                                                          |
| spectral_norm              | 70.0 ms                                                         | 57.8 ms: 1.21x faster                                                          |
| go                         | 111 ms                                                          | 96.0 ms: 1.15x faster                                                          |
| tomli_loads                | 1.74 sec                                                        | 1.51 sec: 1.15x faster                                                         |
| async_tree_memoization_tg  | 287 ms                                                          | 251 ms: 1.14x faster                                                           |
| pprint_safe_repr           | 658 ms                                                          | 577 ms: 1.14x faster                                                           |
| async_tree_none            | 245 ms                                                          | 215 ms: 1.14x faster                                                           |
| fannkuch                   | 288 ms                                                          | 254 ms: 1.13x faster                                                           |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 2.55 ms: 1.13x faster                                                          |
| crypto_pyaes               | 56.6 ms                                                         | 50.3 ms: 1.13x faster                                                          |
| logging_silent             | 62.4 ns                                                         | 55.7 ns: 1.12x faster                                                          |
| scimark_fft                | 204 ms                                                          | 184 ms: 1.11x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 273 ms: 1.11x faster                                                           |
| xml_etree_generate         | 61.9 ms                                                         | 56.1 ms: 1.10x faster                                                          |
| pprint_pformat             | 1.32 sec                                                        | 1.20 sec: 1.10x faster                                                         |
| meteor_contest             | 78.1 ms                                                         | 72.1 ms: 1.08x faster                                                          |
| async_tree_none_tg         | 216 ms                                                          | 201 ms: 1.07x faster                                                           |
| json_loads                 | 21.7 us                                                         | 20.5 us: 1.06x faster                                                          |
| pycparser                  | 869 ms                                                          | 824 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 465 ms: 1.05x faster                                                           |
| xml_etree_process          | 44.6 ms                                                         | 42.3 ms: 1.05x faster                                                          |
| python_startup             | 28.3 ms                                                         | 26.9 ms: 1.05x faster                                                          |
| bench_thread_pool          | 1.04 ms                                                         | 998 us: 1.04x faster                                                           |
| logging_format             | 8.59 us                                                         | 8.24 us: 1.04x faster                                                          |
| async_tree_io              | 530 ms                                                          | 510 ms: 1.04x faster                                                           |
| logging_simple             | 7.89 us                                                         | 7.62 us: 1.04x faster                                                          |
| regex_effbot               | 1.82 ms                                                         | 1.76 ms: 1.03x faster                                                          |
| telco                      | 6.27 ms                                                         | 6.10 ms: 1.03x faster                                                          |
| comprehensions             | 13.1 us                                                         | 12.8 us: 1.03x faster                                                          |
| pidigits                   | 204 ms                                                          | 199 ms: 1.02x faster                                                           |
| html5lib                   | 47.1 ms                                                         | 46.0 ms: 1.02x faster                                                          |
| pyflate                    | 322 ms                                                          | 317 ms: 1.01x faster                                                           |
| dulwich_log                | 50.2 ms                                                         | 49.5 ms: 1.01x faster                                                          |
| scimark_lu                 | 60.7 ms                                                         | 59.9 ms: 1.01x faster                                                          |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 464 ms: 1.01x faster                                                           |
| bench_mp_pool              | 93.6 ms                                                         | 94.1 ms: 1.01x slower                                                          |
| regex_v8                   | 15.5 ms                                                         | 15.6 ms: 1.01x slower                                                          |
| nqueens                    | 75.1 ms                                                         | 76.0 ms: 1.01x slower                                                          |
| sqlglot_parse              | 1.02 ms                                                         | 1.04 ms: 1.02x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 164 us: 1.02x slower                                                           |
| mdp                        | 1.70 sec                                                        | 1.75 sec: 1.03x slower                                                         |
| django_template            | 32.0 ms                                                         | 33.1 ms: 1.03x slower                                                          |
| gc_traversal               | 1.76 ms                                                         | 1.83 ms: 1.04x slower                                                          |
| sympy_expand               | 377 ms                                                          | 392 ms: 1.04x slower                                                           |
| 2to3                       | 255 ms                                                          | 266 ms: 1.04x slower                                                           |
| xml_etree_iterparse        | 61.3 ms                                                         | 64.0 ms: 1.04x slower                                                          |
| tornado_http               | 105 ms                                                          | 109 ms: 1.05x slower                                                           |
| pickle_pure_python         | 239 us                                                          | 251 us: 1.05x slower                                                           |
| genshi_text                | 21.7 ms                                                         | 22.9 ms: 1.05x slower                                                          |
| sympy_str                  | 214 ms                                                          | 226 ms: 1.05x slower                                                           |
| regex_compile              | 101 ms                                                          | 106 ms: 1.05x slower                                                           |
| regex_dna                  | 112 ms                                                          | 118 ms: 1.06x slower                                                           |
| sqlglot_transpile          | 1.26 ms                                                         | 1.34 ms: 1.07x slower                                                          |
| json                       | 4.40 ms                                                         | 4.74 ms: 1.08x slower                                                          |
| xml_etree_parse            | 102 ms                                                          | 110 ms: 1.08x slower                                                           |
| sympy_sum                  | 108 ms                                                          | 117 ms: 1.08x slower                                                           |
| coroutines                 | 16.1 ms                                                         | 17.5 ms: 1.09x slower                                                          |
| sqlglot_normalize          | 223 ms                                                          | 244 ms: 1.09x slower                                                           |
| async_tree_io_tg           | 499 ms                                                          | 547 ms: 1.09x slower                                                           |
| genshi_xml                 | 49.0 ms                                                         | 53.7 ms: 1.10x slower                                                          |
| deltablue                  | 2.35 ms                                                         | 2.58 ms: 1.10x slower                                                          |
| create_gc_cycles           | 1.08 ms                                                         | 1.20 ms: 1.11x slower                                                          |
| chaos                      | 49.4 ms                                                         | 55.3 ms: 1.12x slower                                                          |
| generators                 | 21.5 ms                                                         | 24.3 ms: 1.13x slower                                                          |
| docutils                   | 1.80 sec                                                        | 2.05 sec: 1.14x slower                                                         |
| sympy_integrate            | 15.2 ms                                                         | 17.4 ms: 1.14x slower                                                          |
| json_dumps                 | 7.53 ms                                                         | 8.74 ms: 1.16x slower                                                          |
| richards                   | 33.4 ms                                                         | 38.8 ms: 1.16x slower                                                          |
| sphinx                     | 729 ms                                                          | 849 ms: 1.16x slower                                                           |
| hexiom                     | 4.60 ms                                                         | 5.42 ms: 1.18x slower                                                          |
| sqlglot_optimize           | 42.4 ms                                                         | 50.3 ms: 1.19x slower                                                          |
| async_generators           | 267 ms                                                          | 322 ms: 1.21x slower                                                           |
| richards_super             | 37.0 ms                                                         | 45.2 ms: 1.22x slower                                                          |
| pylint                     | 225 ms                                                          | 284 ms: 1.27x slower                                                           |
| raytrace                   | 203 ms                                                          | 272 ms: 1.34x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.06x faster                                                                   |

Benchmark hidden because not significant (3): pathlib, python_startup_no_site, typing_runtime_protocols
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.063x faster
# HPT report

- Reliability score: 66.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown