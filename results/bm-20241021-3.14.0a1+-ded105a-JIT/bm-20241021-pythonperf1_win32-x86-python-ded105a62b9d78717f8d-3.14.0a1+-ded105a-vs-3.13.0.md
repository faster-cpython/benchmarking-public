# Results vs. 3.13.0

- fork: python
- ref: ded105a62b9d78717f8d
- machine: windows-x86
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.061x faster
- HPT reliability: 54.52%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 263 ms: 1.03x slower                                                            |
| docutils       | 1.80 sec                                                        | 2.06 sec: 1.14x slower                                                          |
| html5lib       | 47.1 ms                                                         | 46.4 ms: 1.01x faster                                                           |
| sphinx         | 729 ms                                                          | 849 ms: 1.16x slower                                                            |
| tornado_http   | 105 ms                                                          | 110 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 254 ms: 1.13x faster                                                            |
| async_tree_none           | 245 ms                                                          | 220 ms: 1.11x faster                                                            |
| async_tree_memoization    | 302 ms                                                          | 280 ms: 1.08x faster                                                            |
| async_tree_none_tg        | 216 ms                                                          | 204 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 467 ms: 1.05x faster                                                            |
| coroutines                | 16.1 ms                                                         | 17.7 ms: 1.10x slower                                                           |
| async_tree_io_tg          | 499 ms                                                          | 562 ms: 1.13x slower                                                            |
| async_generators          | 267 ms                                                          | 315 ms: 1.18x slower                                                            |
| Geometric mean            | (ref)                                                           | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): async_tree_io, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 65.9 ms: 1.23x faster                                                           |
| float          | 56.4 ms                                                         | 46.7 ms: 1.21x faster                                                           |
| pidigits       | 204 ms                                                          | 205 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 15.5 ms                                                         | 15.6 ms: 1.01x slower                                                           |
| regex_compile  | 101 ms                                                          | 104 ms: 1.03x slower                                                            |
| regex_effbot   | 1.82 ms                                                         | 1.90 ms: 1.04x slower                                                           |
| regex_dna      | 112 ms                                                          | 123 ms: 1.09x slower                                                            |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.74 sec                                                        | 1.49 sec: 1.16x faster                                                          |
| xml_etree_generate   | 61.9 ms                                                         | 55.6 ms: 1.11x faster                                                           |
| xml_etree_process    | 44.6 ms                                                         | 41.4 ms: 1.08x faster                                                           |
| unpickle_pure_python | 162 us                                                          | 159 us: 1.02x faster                                                            |
| json_loads           | 21.7 us                                                         | 21.3 us: 1.02x faster                                                           |
| xml_etree_iterparse  | 61.3 ms                                                         | 65.2 ms: 1.06x slower                                                           |
| json_dumps           | 7.53 ms                                                         | 8.14 ms: 1.08x slower                                                           |
| xml_etree_parse      | 102 ms                                                          | 111 ms: 1.09x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 27.0 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 5.68 ms: 1.24x faster                                                           |
| django_template | 32.0 ms                                                         | 33.4 ms: 1.04x slower                                                           |
| genshi_text     | 21.7 ms                                                         | 23.1 ms: 1.06x slower                                                           |
| genshi_xml      | 49.0 ms                                                         | 52.7 ms: 1.08x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf1_win32-x86-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|---------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                    | 10.3 ms                                                         | 770 us: 13.33x faster                                                           |
| coverage                  | 326 ms                                                          | 54.1 ms: 6.03x faster                                                           |
| deepcopy_memo             | 26.2 us                                                         | 16.2 us: 1.62x faster                                                           |
| deepcopy                  | 311 us                                                          | 231 us: 1.34x faster                                                            |
| scimark_sor               | 85.8 ms                                                         | 66.5 ms: 1.29x faster                                                           |
| scimark_monte_carlo       | 48.7 ms                                                         | 39.0 ms: 1.25x faster                                                           |
| mako                      | 7.02 ms                                                         | 5.68 ms: 1.24x faster                                                           |
| nbody                     | 81.4 ms                                                         | 65.9 ms: 1.23x faster                                                           |
| deepcopy_reduce           | 2.94 us                                                         | 2.40 us: 1.22x faster                                                           |
| float                     | 56.4 ms                                                         | 46.7 ms: 1.21x faster                                                           |
| spectral_norm             | 70.0 ms                                                         | 58.3 ms: 1.20x faster                                                           |
| pprint_safe_repr          | 658 ms                                                          | 560 ms: 1.18x faster                                                            |
| tomli_loads               | 1.74 sec                                                        | 1.49 sec: 1.16x faster                                                          |
| logging_silent            | 62.4 ns                                                         | 53.8 ns: 1.16x faster                                                           |
| fannkuch                  | 288 ms                                                          | 248 ms: 1.16x faster                                                            |
| pprint_pformat            | 1.32 sec                                                        | 1.14 sec: 1.16x faster                                                          |
| scimark_sparse_mat_mult   | 2.88 ms                                                         | 2.50 ms: 1.16x faster                                                           |
| go                        | 111 ms                                                          | 96.7 ms: 1.15x faster                                                           |
| crypto_pyaes              | 56.6 ms                                                         | 49.6 ms: 1.14x faster                                                           |
| async_tree_memoization_tg | 287 ms                                                          | 254 ms: 1.13x faster                                                            |
| scimark_fft               | 204 ms                                                          | 182 ms: 1.12x faster                                                            |
| xml_etree_generate        | 61.9 ms                                                         | 55.6 ms: 1.11x faster                                                           |
| async_tree_none           | 245 ms                                                          | 220 ms: 1.11x faster                                                            |
| async_tree_memoization    | 302 ms                                                          | 280 ms: 1.08x faster                                                            |
| xml_etree_process         | 44.6 ms                                                         | 41.4 ms: 1.08x faster                                                           |
| meteor_contest            | 78.1 ms                                                         | 73.1 ms: 1.07x faster                                                           |
| async_tree_none_tg        | 216 ms                                                          | 204 ms: 1.06x faster                                                            |
| pycparser                 | 869 ms                                                          | 824 ms: 1.05x faster                                                            |
| bench_thread_pool         | 1.04 ms                                                         | 991 us: 1.05x faster                                                            |
| python_startup            | 28.3 ms                                                         | 27.0 ms: 1.05x faster                                                           |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 467 ms: 1.05x faster                                                            |
| logging_format            | 8.59 us                                                         | 8.28 us: 1.04x faster                                                           |
| logging_simple            | 7.89 us                                                         | 7.63 us: 1.03x faster                                                           |
| telco                     | 6.27 ms                                                         | 6.06 ms: 1.03x faster                                                           |
| scimark_lu                | 60.7 ms                                                         | 59.5 ms: 1.02x faster                                                           |
| unpickle_pure_python      | 162 us                                                          | 159 us: 1.02x faster                                                            |
| dulwich_log               | 50.2 ms                                                         | 49.3 ms: 1.02x faster                                                           |
| json_loads                | 21.7 us                                                         | 21.3 us: 1.02x faster                                                           |
| nqueens                   | 75.1 ms                                                         | 73.9 ms: 1.02x faster                                                           |
| html5lib                  | 47.1 ms                                                         | 46.4 ms: 1.01x faster                                                           |
| pathlib                   | 89.1 ms                                                         | 88.1 ms: 1.01x faster                                                           |
| pyflate                   | 322 ms                                                          | 319 ms: 1.01x faster                                                            |
| bench_mp_pool             | 93.6 ms                                                         | 94.1 ms: 1.01x slower                                                           |
| regex_v8                  | 15.5 ms                                                         | 15.6 ms: 1.01x slower                                                           |
| pidigits                  | 204 ms                                                          | 205 ms: 1.01x slower                                                            |
| 2to3                      | 255 ms                                                          | 263 ms: 1.03x slower                                                            |
| gc_traversal              | 1.76 ms                                                         | 1.82 ms: 1.03x slower                                                           |
| regex_compile             | 101 ms                                                          | 104 ms: 1.03x slower                                                            |
| typing_runtime_protocols  | 141 us                                                          | 147 us: 1.04x slower                                                            |
| django_template           | 32.0 ms                                                         | 33.4 ms: 1.04x slower                                                           |
| sqlglot_parse             | 1.02 ms                                                         | 1.06 ms: 1.04x slower                                                           |
| regex_effbot              | 1.82 ms                                                         | 1.90 ms: 1.04x slower                                                           |
| tornado_http              | 105 ms                                                          | 110 ms: 1.05x slower                                                            |
| sympy_expand              | 377 ms                                                          | 400 ms: 1.06x slower                                                            |
| genshi_text               | 21.7 ms                                                         | 23.1 ms: 1.06x slower                                                           |
| xml_etree_iterparse       | 61.3 ms                                                         | 65.2 ms: 1.06x slower                                                           |
| chaos                     | 49.4 ms                                                         | 52.8 ms: 1.07x slower                                                           |
| sympy_str                 | 214 ms                                                          | 229 ms: 1.07x slower                                                            |
| genshi_xml                | 49.0 ms                                                         | 52.7 ms: 1.08x slower                                                           |
| sqlglot_normalize         | 223 ms                                                          | 240 ms: 1.08x slower                                                            |
| json_dumps                | 7.53 ms                                                         | 8.14 ms: 1.08x slower                                                           |
| mdp                       | 1.70 sec                                                        | 1.84 sec: 1.08x slower                                                          |
| sqlglot_transpile         | 1.26 ms                                                         | 1.37 ms: 1.08x slower                                                           |
| deltablue                 | 2.35 ms                                                         | 2.55 ms: 1.09x slower                                                           |
| sympy_sum                 | 108 ms                                                          | 117 ms: 1.09x slower                                                            |
| xml_etree_parse           | 102 ms                                                          | 111 ms: 1.09x slower                                                            |
| regex_dna                 | 112 ms                                                          | 123 ms: 1.09x slower                                                            |
| coroutines                | 16.1 ms                                                         | 17.7 ms: 1.10x slower                                                           |
| create_gc_cycles          | 1.08 ms                                                         | 1.20 ms: 1.11x slower                                                           |
| async_tree_io_tg          | 499 ms                                                          | 562 ms: 1.13x slower                                                            |
| sympy_integrate           | 15.2 ms                                                         | 17.3 ms: 1.13x slower                                                           |
| json                      | 4.40 ms                                                         | 5.01 ms: 1.14x slower                                                           |
| docutils                  | 1.80 sec                                                        | 2.06 sec: 1.14x slower                                                          |
| hexiom                    | 4.60 ms                                                         | 5.27 ms: 1.15x slower                                                           |
| generators                | 21.5 ms                                                         | 24.7 ms: 1.15x slower                                                           |
| sphinx                    | 729 ms                                                          | 849 ms: 1.16x slower                                                            |
| sqlglot_optimize          | 42.4 ms                                                         | 49.8 ms: 1.17x slower                                                           |
| richards                  | 33.4 ms                                                         | 39.3 ms: 1.18x slower                                                           |
| async_generators          | 267 ms                                                          | 315 ms: 1.18x slower                                                            |
| richards_super            | 37.0 ms                                                         | 44.5 ms: 1.20x slower                                                           |
| pylint                    | 225 ms                                                          | 283 ms: 1.26x slower                                                            |
| raytrace                  | 203 ms                                                          | 271 ms: 1.34x slower                                                            |
| Geometric mean            | (ref)                                                           | 1.06x faster                                                                    |

Benchmark hidden because not significant (5): async_tree_io, async_tree_cpu_io_mixed_tg, pickle_pure_python, comprehensions, python_startup_no_site
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.061x faster
# HPT report

- Reliability score: 54.52% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown