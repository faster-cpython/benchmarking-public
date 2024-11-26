# Results vs. 3.13.0

- fork: python
- ref: 7d7d56d8b1147a6b85e1
- machine: windows-x86
- commit hash: 7d7d56d
- commit date: 2024-11-02
- overall geometric mean: 1.025x faster
- HPT reliability: 96.52%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 244 ms: 1.04x faster                                                            |
| docutils       | 1.80 sec                                                        | 1.82 sec: 1.01x slower                                                          |
| html5lib       | 47.1 ms                                                         | 44.5 ms: 1.06x faster                                                           |
| sphinx         | 729 ms                                                          | 745 ms: 1.02x slower                                                            |
| tornado_http   | 105 ms                                                          | 106 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 252 ms: 1.14x faster                                                            |
| async_tree_none            | 245 ms                                                          | 220 ms: 1.11x faster                                                            |
| async_tree_memoization     | 302 ms                                                          | 274 ms: 1.10x faster                                                            |
| async_tree_none_tg         | 216 ms                                                          | 200 ms: 1.08x faster                                                            |
| async_tree_io              | 530 ms                                                          | 519 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 482 ms: 1.02x faster                                                            |
| coroutines                 | 16.1 ms                                                         | 16.3 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 480 ms: 1.02x slower                                                            |
| async_tree_io_tg           | 499 ms                                                          | 547 ms: 1.09x slower                                                            |
| async_generators           | 267 ms                                                          | 302 ms: 1.13x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 202 ms: 1.01x faster                                                            |
| nbody          | 81.4 ms                                                         | 84.6 ms: 1.04x slower                                                           |
| float          | 56.4 ms                                                         | 60.5 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 112 ms                                                          | 116 ms: 1.03x slower                                                            |
| regex_compile  | 101 ms                                                          | 105 ms: 1.04x slower                                                            |
| regex_v8       | 15.5 ms                                                         | 16.0 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.9 us: 1.04x faster                                                           |
| tomli_loads          | 1.74 sec                                                        | 1.77 sec: 1.02x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 165 us: 1.02x slower                                                            |
| xml_etree_parse      | 102 ms                                                          | 111 ms: 1.09x slower                                                            |
| pickle_pure_python   | 239 us                                                          | 260 us: 1.09x slower                                                            |
| xml_etree_generate   | 61.9 ms                                                         | 68.3 ms: 1.10x slower                                                           |
| xml_etree_iterparse  | 61.3 ms                                                         | 67.9 ms: 1.11x slower                                                           |
| xml_etree_process    | 44.6 ms                                                         | 50.5 ms: 1.13x slower                                                           |
| json_dumps           | 7.53 ms                                                         | 9.07 ms: 1.20x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.08x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.8 ms: 1.10x faster                                                           |
| python_startup_no_site | 20.2 ms                                                         | 19.4 ms: 1.04x faster                                                           |
| Geometric mean         | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 21.7 ms                                                         | 21.1 ms: 1.03x faster                                                           |
| django_template | 32.0 ms                                                         | 34.0 ms: 1.06x slower                                                           |
| mako            | 7.02 ms                                                         | 7.59 ms: 1.08x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 759 us: 13.51x faster                                                           |
| coverage                   | 326 ms                                                          | 49.8 ms: 6.55x faster                                                           |
| deepcopy                   | 311 us                                                          | 239 us: 1.30x faster                                                            |
| deepcopy_memo              | 26.2 us                                                         | 21.1 us: 1.24x faster                                                           |
| go                         | 111 ms                                                          | 97.0 ms: 1.14x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 252 ms: 1.14x faster                                                            |
| deepcopy_reduce            | 2.94 us                                                         | 2.61 us: 1.13x faster                                                           |
| async_tree_none            | 245 ms                                                          | 220 ms: 1.11x faster                                                            |
| async_tree_memoization     | 302 ms                                                          | 274 ms: 1.10x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.8 ms: 1.10x faster                                                           |
| async_tree_none_tg         | 216 ms                                                          | 200 ms: 1.08x faster                                                            |
| bench_mp_pool              | 93.6 ms                                                         | 88.3 ms: 1.06x faster                                                           |
| html5lib                   | 47.1 ms                                                         | 44.5 ms: 1.06x faster                                                           |
| 2to3                       | 255 ms                                                          | 244 ms: 1.04x faster                                                            |
| python_startup_no_site     | 20.2 ms                                                         | 19.4 ms: 1.04x faster                                                           |
| json_loads                 | 21.7 us                                                         | 20.9 us: 1.04x faster                                                           |
| bench_thread_pool          | 1.04 ms                                                         | 1.01 ms: 1.03x faster                                                           |
| pycparser                  | 869 ms                                                          | 843 ms: 1.03x faster                                                            |
| genshi_text                | 21.7 ms                                                         | 21.1 ms: 1.03x faster                                                           |
| connected_components       | 266 ms                                                          | 259 ms: 1.03x faster                                                            |
| shortest_path              | 298 ms                                                          | 290 ms: 1.03x faster                                                            |
| sympy_sum                  | 108 ms                                                          | 105 ms: 1.02x faster                                                            |
| pathlib                    | 89.1 ms                                                         | 87.1 ms: 1.02x faster                                                           |
| async_tree_io              | 530 ms                                                          | 519 ms: 1.02x faster                                                            |
| pprint_safe_repr           | 658 ms                                                          | 647 ms: 1.02x faster                                                            |
| logging_format             | 8.59 us                                                         | 8.44 us: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 482 ms: 1.02x faster                                                            |
| mdp                        | 1.70 sec                                                        | 1.67 sec: 1.01x faster                                                          |
| json                       | 4.40 ms                                                         | 4.34 ms: 1.01x faster                                                           |
| logging_simple             | 7.89 us                                                         | 7.79 us: 1.01x faster                                                           |
| pidigits                   | 204 ms                                                          | 202 ms: 1.01x faster                                                            |
| bpe_tokeniser              | 3.49 sec                                                        | 3.47 sec: 1.01x faster                                                          |
| sympy_expand               | 377 ms                                                          | 375 ms: 1.01x faster                                                            |
| sympy_integrate            | 15.2 ms                                                         | 15.1 ms: 1.01x faster                                                           |
| docutils                   | 1.80 sec                                                        | 1.82 sec: 1.01x slower                                                          |
| coroutines                 | 16.1 ms                                                         | 16.3 ms: 1.01x slower                                                           |
| tornado_http               | 105 ms                                                          | 106 ms: 1.01x slower                                                            |
| sqlglot_optimize           | 42.4 ms                                                         | 43.0 ms: 1.01x slower                                                           |
| tomli_loads                | 1.74 sec                                                        | 1.77 sec: 1.02x slower                                                          |
| gc_traversal               | 1.76 ms                                                         | 1.80 ms: 1.02x slower                                                           |
| pprint_pformat             | 1.32 sec                                                        | 1.35 sec: 1.02x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 165 us: 1.02x slower                                                            |
| sphinx                     | 729 ms                                                          | 745 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 480 ms: 1.02x slower                                                            |
| sqlglot_parse              | 1.02 ms                                                         | 1.04 ms: 1.02x slower                                                           |
| sqlglot_normalize          | 223 ms                                                          | 228 ms: 1.02x slower                                                            |
| sqlglot_transpile          | 1.26 ms                                                         | 1.29 ms: 1.03x slower                                                           |
| regex_dna                  | 112 ms                                                          | 116 ms: 1.03x slower                                                            |
| dulwich_log                | 50.2 ms                                                         | 52.0 ms: 1.04x slower                                                           |
| regex_compile              | 101 ms                                                          | 105 ms: 1.04x slower                                                            |
| meteor_contest             | 78.1 ms                                                         | 81.1 ms: 1.04x slower                                                           |
| regex_v8                   | 15.5 ms                                                         | 16.0 ms: 1.04x slower                                                           |
| fannkuch                   | 288 ms                                                          | 299 ms: 1.04x slower                                                            |
| nbody                      | 81.4 ms                                                         | 84.6 ms: 1.04x slower                                                           |
| crypto_pyaes               | 56.6 ms                                                         | 58.9 ms: 1.04x slower                                                           |
| comprehensions             | 13.1 us                                                         | 13.8 us: 1.05x slower                                                           |
| spectral_norm              | 70.0 ms                                                         | 74.1 ms: 1.06x slower                                                           |
| django_template            | 32.0 ms                                                         | 34.0 ms: 1.06x slower                                                           |
| hexiom                     | 4.60 ms                                                         | 4.93 ms: 1.07x slower                                                           |
| create_gc_cycles           | 1.08 ms                                                         | 1.16 ms: 1.07x slower                                                           |
| float                      | 56.4 ms                                                         | 60.5 ms: 1.07x slower                                                           |
| telco                      | 6.27 ms                                                         | 6.76 ms: 1.08x slower                                                           |
| mako                       | 7.02 ms                                                         | 7.59 ms: 1.08x slower                                                           |
| logging_silent             | 62.4 ns                                                         | 67.8 ns: 1.09x slower                                                           |
| nqueens                    | 75.1 ms                                                         | 81.6 ms: 1.09x slower                                                           |
| xml_etree_parse            | 102 ms                                                          | 111 ms: 1.09x slower                                                            |
| pickle_pure_python         | 239 us                                                          | 260 us: 1.09x slower                                                            |
| async_tree_io_tg           | 499 ms                                                          | 547 ms: 1.09x slower                                                            |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.17 ms: 1.10x slower                                                           |
| generators                 | 21.5 ms                                                         | 23.7 ms: 1.10x slower                                                           |
| xml_etree_generate         | 61.9 ms                                                         | 68.3 ms: 1.10x slower                                                           |
| xml_etree_iterparse        | 61.3 ms                                                         | 67.9 ms: 1.11x slower                                                           |
| pyflate                    | 322 ms                                                          | 358 ms: 1.11x slower                                                            |
| richards                   | 33.4 ms                                                         | 37.2 ms: 1.11x slower                                                           |
| scimark_lu                 | 60.7 ms                                                         | 67.8 ms: 1.12x slower                                                           |
| deltablue                  | 2.35 ms                                                         | 2.65 ms: 1.13x slower                                                           |
| async_generators           | 267 ms                                                          | 302 ms: 1.13x slower                                                            |
| xml_etree_process          | 44.6 ms                                                         | 50.5 ms: 1.13x slower                                                           |
| chaos                      | 49.4 ms                                                         | 56.4 ms: 1.14x slower                                                           |
| scimark_monte_carlo        | 48.7 ms                                                         | 56.1 ms: 1.15x slower                                                           |
| scimark_fft                | 204 ms                                                          | 235 ms: 1.15x slower                                                            |
| richards_super             | 37.0 ms                                                         | 43.0 ms: 1.16x slower                                                           |
| scimark_sor                | 85.8 ms                                                         | 100 ms: 1.17x slower                                                            |
| json_dumps                 | 7.53 ms                                                         | 9.07 ms: 1.20x slower                                                           |
| raytrace                   | 203 ms                                                          | 253 ms: 1.25x slower                                                            |
| k_core                     | 1.43 sec                                                        | 2.00 sec: 1.39x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (6): genshi_xml, sympy_str, typing_runtime_protocols, regex_effbot, asyncio_websockets, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20241102-3.14.0a1+-7d7d56d/bm-20241102-pythonperf1_win32-x86-python-7d7d56d8b1147a6b85e1-3.14.0a1+-7d7d56d.json: sqlite_synth

- Geometric mean (including insignificant results): 1.025x faster
# HPT report

- Reliability score: 96.52% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown