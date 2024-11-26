# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: windows-x86
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.035x faster
- HPT reliability: 94.44%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 249 ms: 1.02x faster                                                                     |
| docutils       | 1.80 sec                                                        | 1.84 sec: 1.02x slower                                                                   |
| html5lib       | 47.1 ms                                                         | 44.7 ms: 1.05x faster                                                                    |
| tornado_http   | 105 ms                                                          | 103 ms: 1.01x faster                                                                     |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.13x faster                                                                     |
| async_tree_none            | 245 ms                                                          | 218 ms: 1.12x faster                                                                     |
| async_tree_memoization     | 302 ms                                                          | 271 ms: 1.11x faster                                                                     |
| async_tree_none_tg         | 216 ms                                                          | 200 ms: 1.08x faster                                                                     |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 470 ms: 1.04x faster                                                                     |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 454 ms: 1.03x faster                                                                     |
| async_tree_io_tg           | 499 ms                                                          | 520 ms: 1.04x slower                                                                     |
| coroutines                 | 16.1 ms                                                         | 17.5 ms: 1.09x slower                                                                    |
| async_generators           | 267 ms                                                          | 303 ms: 1.13x slower                                                                     |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                             |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| pidigits       | 204 ms                                                          | 201 ms: 1.01x faster                                                                     |
| float          | 56.4 ms                                                         | 61.2 ms: 1.08x slower                                                                    |
| nbody          | 81.4 ms                                                         | 89.4 ms: 1.10x slower                                                                    |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| regex_effbot   | 1.82 ms                                                         | 1.79 ms: 1.02x faster                                                                    |
| regex_v8       | 15.5 ms                                                         | 15.3 ms: 1.01x faster                                                                    |
| regex_compile  | 101 ms                                                          | 106 ms: 1.05x slower                                                                     |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| json_loads           | 21.7 us                                                         | 20.7 us: 1.05x faster                                                                    |
| tomli_loads          | 1.74 sec                                                        | 1.77 sec: 1.02x slower                                                                   |
| xml_etree_process    | 44.6 ms                                                         | 47.4 ms: 1.06x slower                                                                    |
| xml_etree_generate   | 61.9 ms                                                         | 66.6 ms: 1.08x slower                                                                    |
| xml_etree_parse      | 102 ms                                                          | 113 ms: 1.10x slower                                                                     |
| xml_etree_iterparse  | 61.3 ms                                                         | 68.1 ms: 1.11x slower                                                                    |
| unpickle_pure_python | 162 us                                                          | 180 us: 1.11x slower                                                                     |
| pickle_pure_python   | 239 us                                                          | 272 us: 1.14x slower                                                                     |
| json_dumps           | 7.53 ms                                                         | 9.02 ms: 1.20x slower                                                                    |
| Geometric mean       | (ref)                                                           | 1.08x slower                                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 24.3 ms: 1.16x faster                                                                    |
| python_startup_no_site | 20.2 ms                                                         | 20.0 ms: 1.01x faster                                                                    |
| Geometric mean         | (ref)                                                           | 1.08x faster                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| genshi_xml      | 49.0 ms                                                         | 45.6 ms: 1.07x faster                                                                    |
| genshi_text     | 21.7 ms                                                         | 20.6 ms: 1.05x faster                                                                    |
| django_template | 32.0 ms                                                         | 32.8 ms: 1.02x slower                                                                    |
| mako            | 7.02 ms                                                         | 7.86 ms: 1.12x slower                                                                    |
| Geometric mean  | (ref)                                                           | 1.00x slower                                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------------------------:|
| thrift                     | 10.3 ms                                                         | 739 us: 13.88x faster                                                                    |
| coverage                   | 326 ms                                                          | 52.6 ms: 6.21x faster                                                                    |
| create_gc_cycles           | 1.08 ms                                                         | 774 us: 1.40x faster                                                                     |
| deepcopy                   | 311 us                                                          | 241 us: 1.29x faster                                                                     |
| bench_mp_pool              | 93.6 ms                                                         | 73.6 ms: 1.27x faster                                                                    |
| gc_traversal               | 1.76 ms                                                         | 1.44 ms: 1.23x faster                                                                    |
| deepcopy_memo              | 26.2 us                                                         | 22.1 us: 1.18x faster                                                                    |
| python_startup             | 28.3 ms                                                         | 24.3 ms: 1.16x faster                                                                    |
| deepcopy_reduce            | 2.94 us                                                         | 2.53 us: 1.16x faster                                                                    |
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.13x faster                                                                     |
| async_tree_none            | 245 ms                                                          | 218 ms: 1.12x faster                                                                     |
| async_tree_memoization     | 302 ms                                                          | 271 ms: 1.11x faster                                                                     |
| async_tree_none_tg         | 216 ms                                                          | 200 ms: 1.08x faster                                                                     |
| go                         | 111 ms                                                          | 103 ms: 1.08x faster                                                                     |
| genshi_xml                 | 49.0 ms                                                         | 45.6 ms: 1.07x faster                                                                    |
| html5lib                   | 47.1 ms                                                         | 44.7 ms: 1.05x faster                                                                    |
| genshi_text                | 21.7 ms                                                         | 20.6 ms: 1.05x faster                                                                    |
| json_loads                 | 21.7 us                                                         | 20.7 us: 1.05x faster                                                                    |
| bench_thread_pool          | 1.04 ms                                                         | 997 us: 1.04x faster                                                                     |
| async_tree_cpu_io_mixed    | 490 ms                                                          | 470 ms: 1.04x faster                                                                     |
| pycparser                  | 869 ms                                                          | 835 ms: 1.04x faster                                                                     |
| async_tree_cpu_io_mixed_tg | 469 ms                                                          | 454 ms: 1.03x faster                                                                     |
| 2to3                       | 255 ms                                                          | 249 ms: 1.02x faster                                                                     |
| json                       | 4.40 ms                                                         | 4.30 ms: 1.02x faster                                                                    |
| nqueens                    | 75.1 ms                                                         | 73.5 ms: 1.02x faster                                                                    |
| regex_effbot               | 1.82 ms                                                         | 1.79 ms: 1.02x faster                                                                    |
| pprint_safe_repr           | 658 ms                                                          | 647 ms: 1.02x faster                                                                     |
| sympy_sum                  | 108 ms                                                          | 106 ms: 1.02x faster                                                                     |
| logging_simple             | 7.89 us                                                         | 7.77 us: 1.02x faster                                                                    |
| pathlib                    | 89.1 ms                                                         | 87.8 ms: 1.01x faster                                                                    |
| pidigits                   | 204 ms                                                          | 201 ms: 1.01x faster                                                                     |
| regex_v8                   | 15.5 ms                                                         | 15.3 ms: 1.01x faster                                                                    |
| tornado_http               | 105 ms                                                          | 103 ms: 1.01x faster                                                                     |
| pprint_pformat             | 1.32 sec                                                        | 1.31 sec: 1.01x faster                                                                   |
| python_startup_no_site     | 20.2 ms                                                         | 20.0 ms: 1.01x faster                                                                    |
| sqlglot_normalize          | 223 ms                                                          | 224 ms: 1.01x slower                                                                     |
| sympy_str                  | 214 ms                                                          | 216 ms: 1.01x slower                                                                     |
| comprehensions             | 13.1 us                                                         | 13.3 us: 1.01x slower                                                                    |
| sympy_integrate            | 15.2 ms                                                         | 15.4 ms: 1.01x slower                                                                    |
| mdp                        | 1.70 sec                                                        | 1.72 sec: 1.01x slower                                                                   |
| tomli_loads                | 1.74 sec                                                        | 1.77 sec: 1.02x slower                                                                   |
| sympy_expand               | 377 ms                                                          | 384 ms: 1.02x slower                                                                     |
| dulwich_log                | 50.2 ms                                                         | 51.2 ms: 1.02x slower                                                                    |
| meteor_contest             | 78.1 ms                                                         | 79.8 ms: 1.02x slower                                                                    |
| django_template            | 32.0 ms                                                         | 32.8 ms: 1.02x slower                                                                    |
| docutils                   | 1.80 sec                                                        | 1.84 sec: 1.02x slower                                                                   |
| sqlglot_optimize           | 42.4 ms                                                         | 43.5 ms: 1.03x slower                                                                    |
| typing_runtime_protocols   | 141 us                                                          | 145 us: 1.03x slower                                                                     |
| pylint                     | 225 ms                                                          | 234 ms: 1.04x slower                                                                     |
| async_tree_io_tg           | 499 ms                                                          | 520 ms: 1.04x slower                                                                     |
| crypto_pyaes               | 56.6 ms                                                         | 59.2 ms: 1.05x slower                                                                    |
| regex_compile              | 101 ms                                                          | 106 ms: 1.05x slower                                                                     |
| sqlglot_transpile          | 1.26 ms                                                         | 1.33 ms: 1.06x slower                                                                    |
| xml_etree_process          | 44.6 ms                                                         | 47.4 ms: 1.06x slower                                                                    |
| scimark_sparse_mat_mult    | 2.88 ms                                                         | 3.08 ms: 1.07x slower                                                                    |
| sqlglot_parse              | 1.02 ms                                                         | 1.09 ms: 1.07x slower                                                                    |
| hexiom                     | 4.60 ms                                                         | 4.94 ms: 1.08x slower                                                                    |
| xml_etree_generate         | 61.9 ms                                                         | 66.6 ms: 1.08x slower                                                                    |
| spectral_norm              | 70.0 ms                                                         | 75.9 ms: 1.08x slower                                                                    |
| float                      | 56.4 ms                                                         | 61.2 ms: 1.08x slower                                                                    |
| coroutines                 | 16.1 ms                                                         | 17.5 ms: 1.09x slower                                                                    |
| telco                      | 6.27 ms                                                         | 6.86 ms: 1.09x slower                                                                    |
| generators                 | 21.5 ms                                                         | 23.6 ms: 1.10x slower                                                                    |
| nbody                      | 81.4 ms                                                         | 89.4 ms: 1.10x slower                                                                    |
| xml_etree_parse            | 102 ms                                                          | 113 ms: 1.10x slower                                                                     |
| xml_etree_iterparse        | 61.3 ms                                                         | 68.1 ms: 1.11x slower                                                                    |
| unpickle_pure_python       | 162 us                                                          | 180 us: 1.11x slower                                                                     |
| scimark_lu                 | 60.7 ms                                                         | 67.8 ms: 1.12x slower                                                                    |
| mako                       | 7.02 ms                                                         | 7.86 ms: 1.12x slower                                                                    |
| scimark_fft                | 204 ms                                                          | 229 ms: 1.12x slower                                                                     |
| pyflate                    | 322 ms                                                          | 362 ms: 1.12x slower                                                                     |
| fannkuch                   | 288 ms                                                          | 324 ms: 1.13x slower                                                                     |
| chaos                      | 49.4 ms                                                         | 55.9 ms: 1.13x slower                                                                    |
| async_generators           | 267 ms                                                          | 303 ms: 1.13x slower                                                                     |
| pickle_pure_python         | 239 us                                                          | 272 us: 1.14x slower                                                                     |
| deltablue                  | 2.35 ms                                                         | 2.72 ms: 1.16x slower                                                                    |
| scimark_monte_carlo        | 48.7 ms                                                         | 56.7 ms: 1.16x slower                                                                    |
| logging_silent             | 62.4 ns                                                         | 73.2 ns: 1.17x slower                                                                    |
| scimark_sor                | 85.8 ms                                                         | 102 ms: 1.19x slower                                                                     |
| json_dumps                 | 7.53 ms                                                         | 9.02 ms: 1.20x slower                                                                    |
| raytrace                   | 203 ms                                                          | 249 ms: 1.23x slower                                                                     |
| richards                   | 33.4 ms                                                         | 41.3 ms: 1.24x slower                                                                    |
| richards_super             | 37.0 ms                                                         | 46.0 ms: 1.24x slower                                                                    |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                             |

Benchmark hidden because not significant (3): logging_format, regex_dna, async_tree_io
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-pythonperf1_win32-x86-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.035x faster
# HPT report

- Reliability score: 94.44% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown