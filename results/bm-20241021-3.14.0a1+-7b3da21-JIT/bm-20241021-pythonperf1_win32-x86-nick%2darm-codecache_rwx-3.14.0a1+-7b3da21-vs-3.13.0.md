# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache_rwx
- machine: windows-x86
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.087x faster
- HPT reliability: 89.24%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 251 ms: 1.02x faster                                                         |
| docutils       | 1.80 sec                                                        | 1.94 sec: 1.08x slower                                                       |
| html5lib       | 47.1 ms                                                         | 45.1 ms: 1.04x faster                                                        |
| sphinx         | 729 ms                                                          | 795 ms: 1.09x slower                                                         |
| tornado_http   | 105 ms                                                          | 109 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 256 ms: 1.12x faster                                                         |
| async_tree_none            | 245 ms                                                          | 222 ms: 1.10x faster                                                         |
| async_tree_memoization     | 302 ms                                                          | 278 ms: 1.09x faster                                                         |
| async_tree_none_tg         | 216 ms                                                          | 203 ms: 1.06x faster                                                         |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 468 ms: 1.05x faster                                                         |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 462 ms: 1.02x faster                                                         |
| coroutines                 | 16.1 ms                                                         | 17.6 ms: 1.09x slower                                                        |
| async_tree_io_tg           | 499 ms                                                          | 549 ms: 1.10x slower                                                         |
| async_generators           | 267 ms                                                          | 324 ms: 1.21x slower                                                         |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 56.4 ms: 1.44x faster                                                        |
| float          | 56.4 ms                                                         | 45.8 ms: 1.23x faster                                                        |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 98.5 ms: 1.03x faster                                                        |
| regex_effbot   | 1.82 ms                                                         | 1.79 ms: 1.02x faster                                                        |
| regex_v8       | 15.5 ms                                                         | 15.6 ms: 1.01x slower                                                        |
| regex_dna      | 112 ms                                                          | 116 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 1.74 sec                                                        | 1.52 sec: 1.15x faster                                                       |
| xml_etree_generate   | 61.9 ms                                                         | 55.5 ms: 1.11x faster                                                        |
| xml_etree_process    | 44.6 ms                                                         | 41.0 ms: 1.09x faster                                                        |
| json_loads           | 21.7 us                                                         | 20.8 us: 1.04x faster                                                        |
| unpickle_pure_python | 162 us                                                          | 158 us: 1.02x faster                                                         |
| pickle_pure_python   | 239 us                                                          | 241 us: 1.01x slower                                                         |
| xml_etree_iterparse  | 61.3 ms                                                         | 64.1 ms: 1.05x slower                                                        |
| json_dumps           | 7.53 ms                                                         | 8.11 ms: 1.08x slower                                                        |
| xml_etree_parse      | 102 ms                                                          | 111 ms: 1.09x slower                                                         |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.0 ms: 1.05x faster                                                        |
| python_startup_no_site | 20.2 ms                                                         | 20.4 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 5.68 ms: 1.24x faster                                                        |
| genshi_text     | 21.7 ms                                                         | 22.3 ms: 1.02x slower                                                        |
| django_template | 32.0 ms                                                         | 33.5 ms: 1.05x slower                                                        |
| genshi_xml      | 49.0 ms                                                         | 52.2 ms: 1.06x slower                                                        |
| Geometric mean  | (ref)                                                           | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 789 us: 13.00x faster                                                        |
| coverage                   | 326 ms                                                          | 53.1 ms: 6.14x faster                                                        |
| deepcopy_memo              | 26.2 us                                                         | 16.3 us: 1.61x faster                                                        |
| nbody                      | 81.4 ms                                                         | 56.4 ms: 1.44x faster                                                        |
| deepcopy                   | 311 us                                                          | 227 us: 1.37x faster                                                         |
| fannkuch                   | 288 ms                                                          | 219 ms: 1.31x faster                                                         |
| scimark_monte_carlo        | 48.7 ms                                                         | 38.3 ms: 1.27x faster                                                        |
| mako                       | 7.02 ms                                                         | 5.68 ms: 1.24x faster                                                        |
| float                      | 56.4 ms                                                         | 45.8 ms: 1.23x faster                                                        |
| deepcopy_reduce            | 2.94 us                                                         | 2.41 us: 1.22x faster                                                        |
| scimark_sor                | 85.8 ms                                                         | 70.4 ms: 1.22x faster                                                        |
| go                         | 111 ms                                                          | 92.2 ms: 1.20x faster                                                        |
| spectral_norm              | 70.0 ms                                                         | 58.4 ms: 1.20x faster                                                        |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 2.46 ms: 1.17x faster                                                        |
| pprint_safe_repr           | 658 ms                                                          | 570 ms: 1.15x faster                                                         |
| tomli_loads                | 1.74 sec                                                        | 1.52 sec: 1.15x faster                                                       |
| crypto_pyaes               | 56.6 ms                                                         | 49.7 ms: 1.14x faster                                                        |
| pprint_pformat             | 1.32 sec                                                        | 1.17 sec: 1.13x faster                                                       |
| comprehensions             | 13.1 us                                                         | 11.7 us: 1.13x faster                                                        |
| async_tree_memoization_tg  | 287 ms                                                          | 256 ms: 1.12x faster                                                         |
| meteor_contest             | 78.1 ms                                                         | 69.9 ms: 1.12x faster                                                        |
| logging_silent             | 62.4 ns                                                         | 55.8 ns: 1.12x faster                                                        |
| xml_etree_generate         | 61.9 ms                                                         | 55.5 ms: 1.11x faster                                                        |
| scimark_fft                | 204 ms                                                          | 184 ms: 1.11x faster                                                         |
| async_tree_none            | 245 ms                                                          | 222 ms: 1.10x faster                                                         |
| telco                      | 6.27 ms                                                         | 5.72 ms: 1.10x faster                                                        |
| pycparser                  | 869 ms                                                          | 798 ms: 1.09x faster                                                         |
| xml_etree_process          | 44.6 ms                                                         | 41.0 ms: 1.09x faster                                                        |
| pyflate                    | 322 ms                                                          | 296 ms: 1.09x faster                                                         |
| async_tree_memoization     | 302 ms                                                          | 278 ms: 1.09x faster                                                         |
| async_tree_none_tg         | 216 ms                                                          | 203 ms: 1.06x faster                                                         |
| python_startup             | 28.3 ms                                                         | 27.0 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 468 ms: 1.05x faster                                                         |
| html5lib                   | 47.1 ms                                                         | 45.1 ms: 1.04x faster                                                        |
| json_loads                 | 21.7 us                                                         | 20.8 us: 1.04x faster                                                        |
| logging_simple             | 7.89 us                                                         | 7.58 us: 1.04x faster                                                        |
| dulwich_log                | 50.2 ms                                                         | 48.3 ms: 1.04x faster                                                        |
| logging_format             | 8.59 us                                                         | 8.28 us: 1.04x faster                                                        |
| regex_compile              | 101 ms                                                          | 98.5 ms: 1.03x faster                                                        |
| unpickle_pure_python       | 162 us                                                          | 158 us: 1.02x faster                                                         |
| bench_mp_pool              | 93.6 ms                                                         | 91.8 ms: 1.02x faster                                                        |
| scimark_lu                 | 60.7 ms                                                         | 59.6 ms: 1.02x faster                                                        |
| regex_effbot               | 1.82 ms                                                         | 1.79 ms: 1.02x faster                                                        |
| 2to3                       | 255 ms                                                          | 251 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 462 ms: 1.02x faster                                                         |
| mdp                        | 1.70 sec                                                        | 1.68 sec: 1.01x faster                                                       |
| sqlglot_parse              | 1.02 ms                                                         | 1.01 ms: 1.01x faster                                                        |
| pathlib                    | 89.1 ms                                                         | 88.1 ms: 1.01x faster                                                        |
| regex_v8                   | 15.5 ms                                                         | 15.6 ms: 1.01x slower                                                        |
| pickle_pure_python         | 239 us                                                          | 241 us: 1.01x slower                                                         |
| nqueens                    | 75.1 ms                                                         | 75.9 ms: 1.01x slower                                                        |
| python_startup_no_site     | 20.2 ms                                                         | 20.4 ms: 1.01x slower                                                        |
| typing_runtime_protocols   | 141 us                                                          | 143 us: 1.01x slower                                                         |
| sympy_sum                  | 108 ms                                                          | 109 ms: 1.01x slower                                                         |
| generators                 | 21.5 ms                                                         | 21.8 ms: 1.01x slower                                                        |
| gc_traversal               | 1.76 ms                                                         | 1.80 ms: 1.02x slower                                                        |
| genshi_text                | 21.7 ms                                                         | 22.3 ms: 1.02x slower                                                        |
| sympy_expand               | 377 ms                                                          | 387 ms: 1.03x slower                                                         |
| sympy_str                  | 214 ms                                                          | 220 ms: 1.03x slower                                                         |
| hexiom                     | 4.60 ms                                                         | 4.75 ms: 1.03x slower                                                        |
| regex_dna                  | 112 ms                                                          | 116 ms: 1.04x slower                                                         |
| sqlglot_transpile          | 1.26 ms                                                         | 1.31 ms: 1.04x slower                                                        |
| tornado_http               | 105 ms                                                          | 109 ms: 1.04x slower                                                         |
| xml_etree_iterparse        | 61.3 ms                                                         | 64.1 ms: 1.05x slower                                                        |
| django_template            | 32.0 ms                                                         | 33.5 ms: 1.05x slower                                                        |
| sqlglot_normalize          | 223 ms                                                          | 236 ms: 1.06x slower                                                         |
| genshi_xml                 | 49.0 ms                                                         | 52.2 ms: 1.06x slower                                                        |
| json_dumps                 | 7.53 ms                                                         | 8.11 ms: 1.08x slower                                                        |
| deltablue                  | 2.35 ms                                                         | 2.54 ms: 1.08x slower                                                        |
| docutils                   | 1.80 sec                                                        | 1.94 sec: 1.08x slower                                                       |
| coroutines                 | 16.1 ms                                                         | 17.6 ms: 1.09x slower                                                        |
| xml_etree_parse            | 102 ms                                                          | 111 ms: 1.09x slower                                                         |
| sphinx                     | 729 ms                                                          | 795 ms: 1.09x slower                                                         |
| async_tree_io_tg           | 499 ms                                                          | 549 ms: 1.10x slower                                                         |
| richards                   | 33.4 ms                                                         | 36.7 ms: 1.10x slower                                                        |
| create_gc_cycles           | 1.08 ms                                                         | 1.19 ms: 1.10x slower                                                        |
| sympy_integrate            | 15.2 ms                                                         | 16.8 ms: 1.10x slower                                                        |
| chaos                      | 49.4 ms                                                         | 54.5 ms: 1.10x slower                                                        |
| sqlglot_optimize           | 42.4 ms                                                         | 46.9 ms: 1.11x slower                                                        |
| richards_super             | 37.0 ms                                                         | 41.6 ms: 1.12x slower                                                        |
| json                       | 4.40 ms                                                         | 5.03 ms: 1.14x slower                                                        |
| pylint                     | 225 ms                                                          | 261 ms: 1.16x slower                                                         |
| async_generators           | 267 ms                                                          | 324 ms: 1.21x slower                                                         |
| raytrace                   | 203 ms                                                          | 274 ms: 1.35x slower                                                         |
| Geometric mean             | (ref)                                                           | 1.09x faster                                                                 |

Benchmark hidden because not significant (3): bench_thread_pool, async_tree_io, pidigits
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.087x faster
# HPT report

- Reliability score: 89.24% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown