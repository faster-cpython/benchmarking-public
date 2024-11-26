# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: windows-x86
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.102x faster
- HPT reliability: 98.41%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 1.80 sec                                                        | 1.97 sec: 1.10x slower                                                   |
| html5lib       | 47.1 ms                                                         | 46.2 ms: 1.02x faster                                                    |
| sphinx         | 729 ms                                                          | 819 ms: 1.12x slower                                                     |
| tornado_http   | 105 ms                                                          | 109 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                           | 1.05x slower                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 252 ms: 1.14x faster                                                     |
| async_tree_none            | 245 ms                                                          | 217 ms: 1.13x faster                                                     |
| async_tree_memoization     | 302 ms                                                          | 277 ms: 1.09x faster                                                     |
| async_tree_none_tg         | 216 ms                                                          | 200 ms: 1.08x faster                                                     |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 470 ms: 1.04x faster                                                     |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 463 ms: 1.01x faster                                                     |
| coroutines                 | 16.1 ms                                                         | 17.4 ms: 1.08x slower                                                    |
| async_tree_io_tg           | 499 ms                                                          | 549 ms: 1.10x slower                                                     |
| async_generators           | 267 ms                                                          | 319 ms: 1.19x slower                                                     |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                             |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 57.9 ms: 1.41x faster                                                    |
| float          | 56.4 ms                                                         | 45.9 ms: 1.23x faster                                                    |
| Geometric mean | (ref)                                                           | 1.20x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 97.7 ms: 1.03x faster                                                    |
| regex_effbot   | 1.82 ms                                                         | 1.76 ms: 1.03x faster                                                    |
| regex_v8       | 15.5 ms                                                         | 15.2 ms: 1.01x faster                                                    |
| regex_dna      | 112 ms                                                          | 113 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                           | 1.02x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 1.74 sec                                                        | 1.51 sec: 1.15x faster                                                   |
| xml_etree_generate   | 61.9 ms                                                         | 54.9 ms: 1.13x faster                                                    |
| xml_etree_process    | 44.6 ms                                                         | 40.8 ms: 1.09x faster                                                    |
| json_loads           | 21.7 us                                                         | 20.8 us: 1.04x faster                                                    |
| unpickle_pure_python | 162 us                                                          | 156 us: 1.04x faster                                                     |
| pickle_pure_python   | 239 us                                                          | 237 us: 1.01x faster                                                     |
| xml_etree_iterparse  | 61.3 ms                                                         | 63.5 ms: 1.04x slower                                                    |
| json_dumps           | 7.53 ms                                                         | 8.03 ms: 1.07x slower                                                    |
| xml_etree_parse      | 102 ms                                                          | 109 ms: 1.07x slower                                                     |
| Geometric mean       | (ref)                                                           | 1.03x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.0 ms: 1.05x faster                                                    |
| python_startup_no_site | 20.2 ms                                                         | 20.6 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 5.68 ms: 1.24x faster                                                    |
| django_template | 32.0 ms                                                         | 32.4 ms: 1.01x slower                                                    |
| genshi_text     | 21.7 ms                                                         | 22.5 ms: 1.04x slower                                                    |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                             |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 784 us: 13.08x faster                                                    |
| coverage                   | 326 ms                                                          | 53.3 ms: 6.12x faster                                                    |
| sqlglot_normalize          | 223 ms                                                          | 99.3 ms: 2.24x faster                                                    |
| deepcopy_memo              | 26.2 us                                                         | 15.8 us: 1.65x faster                                                    |
| nbody                      | 81.4 ms                                                         | 57.9 ms: 1.41x faster                                                    |
| deepcopy                   | 311 us                                                          | 233 us: 1.33x faster                                                     |
| scimark_monte_carlo        | 48.7 ms                                                         | 37.9 ms: 1.28x faster                                                    |
| scimark_sor                | 85.8 ms                                                         | 67.0 ms: 1.28x faster                                                    |
| deepcopy_reduce            | 2.94 us                                                         | 2.36 us: 1.25x faster                                                    |
| fannkuch                   | 288 ms                                                          | 232 ms: 1.24x faster                                                     |
| go                         | 111 ms                                                          | 89.2 ms: 1.24x faster                                                    |
| mako                       | 7.02 ms                                                         | 5.68 ms: 1.24x faster                                                    |
| float                      | 56.4 ms                                                         | 45.9 ms: 1.23x faster                                                    |
| spectral_norm              | 70.0 ms                                                         | 58.7 ms: 1.19x faster                                                    |
| pprint_safe_repr           | 658 ms                                                          | 556 ms: 1.18x faster                                                     |
| pprint_pformat             | 1.32 sec                                                        | 1.13 sec: 1.17x faster                                                   |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 2.48 ms: 1.16x faster                                                    |
| scimark_fft                | 204 ms                                                          | 175 ms: 1.16x faster                                                     |
| crypto_pyaes               | 56.6 ms                                                         | 48.9 ms: 1.16x faster                                                    |
| tomli_loads                | 1.74 sec                                                        | 1.51 sec: 1.15x faster                                                   |
| async_tree_memoization_tg  | 287 ms                                                          | 252 ms: 1.14x faster                                                     |
| logging_silent             | 62.4 ns                                                         | 55.1 ns: 1.13x faster                                                    |
| async_tree_none            | 245 ms                                                          | 217 ms: 1.13x faster                                                     |
| xml_etree_generate         | 61.9 ms                                                         | 54.9 ms: 1.13x faster                                                    |
| pycparser                  | 869 ms                                                          | 781 ms: 1.11x faster                                                     |
| meteor_contest             | 78.1 ms                                                         | 70.7 ms: 1.11x faster                                                    |
| xml_etree_process          | 44.6 ms                                                         | 40.8 ms: 1.09x faster                                                    |
| async_tree_memoization     | 302 ms                                                          | 277 ms: 1.09x faster                                                     |
| async_tree_none_tg         | 216 ms                                                          | 200 ms: 1.08x faster                                                     |
| pyflate                    | 322 ms                                                          | 300 ms: 1.07x faster                                                     |
| comprehensions             | 13.1 us                                                         | 12.5 us: 1.05x faster                                                    |
| scimark_lu                 | 60.7 ms                                                         | 57.7 ms: 1.05x faster                                                    |
| logging_simple             | 7.89 us                                                         | 7.50 us: 1.05x faster                                                    |
| python_startup             | 28.3 ms                                                         | 27.0 ms: 1.05x faster                                                    |
| logging_format             | 8.59 us                                                         | 8.23 us: 1.04x faster                                                    |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 470 ms: 1.04x faster                                                     |
| json_loads                 | 21.7 us                                                         | 20.8 us: 1.04x faster                                                    |
| unpickle_pure_python       | 162 us                                                          | 156 us: 1.04x faster                                                     |
| bench_thread_pool          | 1.04 ms                                                         | 1.00 ms: 1.04x faster                                                    |
| regex_compile              | 101 ms                                                          | 97.7 ms: 1.03x faster                                                    |
| regex_effbot               | 1.82 ms                                                         | 1.76 ms: 1.03x faster                                                    |
| dulwich_log                | 50.2 ms                                                         | 48.7 ms: 1.03x faster                                                    |
| nqueens                    | 75.1 ms                                                         | 73.4 ms: 1.02x faster                                                    |
| html5lib                   | 47.1 ms                                                         | 46.2 ms: 1.02x faster                                                    |
| telco                      | 6.27 ms                                                         | 6.16 ms: 1.02x faster                                                    |
| mdp                        | 1.70 sec                                                        | 1.67 sec: 1.02x faster                                                   |
| typing_runtime_protocols   | 141 us                                                          | 139 us: 1.02x faster                                                     |
| regex_v8                   | 15.5 ms                                                         | 15.2 ms: 1.01x faster                                                    |
| sqlglot_parse              | 1.02 ms                                                         | 1.01 ms: 1.01x faster                                                    |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 463 ms: 1.01x faster                                                     |
| pickle_pure_python         | 239 us                                                          | 237 us: 1.01x faster                                                     |
| pathlib                    | 89.1 ms                                                         | 88.4 ms: 1.01x faster                                                    |
| regex_dna                  | 112 ms                                                          | 113 ms: 1.01x slower                                                     |
| django_template            | 32.0 ms                                                         | 32.4 ms: 1.01x slower                                                    |
| sympy_expand               | 377 ms                                                          | 382 ms: 1.01x slower                                                     |
| hexiom                     | 4.60 ms                                                         | 4.70 ms: 1.02x slower                                                    |
| python_startup_no_site     | 20.2 ms                                                         | 20.6 ms: 1.02x slower                                                    |
| sympy_str                  | 214 ms                                                          | 219 ms: 1.02x slower                                                     |
| gc_traversal               | 1.76 ms                                                         | 1.82 ms: 1.03x slower                                                    |
| sqlglot_transpile          | 1.26 ms                                                         | 1.30 ms: 1.03x slower                                                    |
| xml_etree_iterparse        | 61.3 ms                                                         | 63.5 ms: 1.04x slower                                                    |
| genshi_text                | 21.7 ms                                                         | 22.5 ms: 1.04x slower                                                    |
| generators                 | 21.5 ms                                                         | 22.4 ms: 1.04x slower                                                    |
| tornado_http               | 105 ms                                                          | 109 ms: 1.04x slower                                                     |
| richards                   | 33.4 ms                                                         | 34.9 ms: 1.05x slower                                                    |
| sympy_sum                  | 108 ms                                                          | 114 ms: 1.05x slower                                                     |
| json_dumps                 | 7.53 ms                                                         | 8.03 ms: 1.07x slower                                                    |
| xml_etree_parse            | 102 ms                                                          | 109 ms: 1.07x slower                                                     |
| chaos                      | 49.4 ms                                                         | 53.0 ms: 1.07x slower                                                    |
| deltablue                  | 2.35 ms                                                         | 2.52 ms: 1.07x slower                                                    |
| coroutines                 | 16.1 ms                                                         | 17.4 ms: 1.08x slower                                                    |
| create_gc_cycles           | 1.08 ms                                                         | 1.18 ms: 1.09x slower                                                    |
| docutils                   | 1.80 sec                                                        | 1.97 sec: 1.10x slower                                                   |
| richards_super             | 37.0 ms                                                         | 40.7 ms: 1.10x slower                                                    |
| async_tree_io_tg           | 499 ms                                                          | 549 ms: 1.10x slower                                                     |
| sympy_integrate            | 15.2 ms                                                         | 17.0 ms: 1.12x slower                                                    |
| sphinx                     | 729 ms                                                          | 819 ms: 1.12x slower                                                     |
| sqlglot_optimize           | 42.4 ms                                                         | 47.8 ms: 1.13x slower                                                    |
| json                       | 4.40 ms                                                         | 5.15 ms: 1.17x slower                                                    |
| async_generators           | 267 ms                                                          | 319 ms: 1.19x slower                                                     |
| pylint                     | 225 ms                                                          | 278 ms: 1.24x slower                                                     |
| raytrace                   | 203 ms                                                          | 263 ms: 1.30x slower                                                     |
| Geometric mean             | (ref)                                                           | 1.10x faster                                                             |

Benchmark hidden because not significant (5): async_tree_io, genshi_xml, pidigits, 2to3, bench_mp_pool
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.102x faster
# HPT report

- Reliability score: 98.41% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown