# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: windows-amd64
- commit hash: f03f745
- commit date: 2024-10-29
- overall geometric mean: 1.114x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 247 ms: 1.12x slower                                                           |
| docutils       | 1.57 sec                                                    | 1.77 sec: 1.13x slower                                                         |
| html5lib       | 38.9 ms                                                     | 45.0 ms: 1.16x slower                                                          |
| sphinx         | 633 ms                                                      | 705 ms: 1.11x slower                                                           |
| tornado_http   | 93.0 ms                                                     | 96.4 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                       | 1.11x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 276 ms: 1.05x faster                                                           |
| asyncio_websockets         | 318 ms                                                      | 313 ms: 1.01x faster                                                           |
| async_tree_none            | 226 ms                                                      | 237 ms: 1.05x slower                                                           |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 402 ms: 1.05x slower                                                           |
| async_tree_memoization     | 276 ms                                                      | 294 ms: 1.07x slower                                                           |
| async_tree_none_tg         | 209 ms                                                      | 224 ms: 1.07x slower                                                           |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 407 ms: 1.08x slower                                                           |
| async_tree_io              | 521 ms                                                      | 592 ms: 1.14x slower                                                           |
| coroutines                 | 12.8 ms                                                     | 15.1 ms: 1.18x slower                                                          |
| async_generators           | 223 ms                                                      | 273 ms: 1.22x slower                                                           |
| async_tree_io_tg           | 518 ms                                                      | 660 ms: 1.27x slower                                                           |
| Geometric mean             | (ref)                                                       | 1.09x slower                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 49.9 ms                                                     | 61.5 ms: 1.23x slower                                                          |
| nbody          | 68.4 ms                                                     | 89.4 ms: 1.31x slower                                                          |
| Geometric mean | (ref)                                                       | 1.17x slower                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.1 ms: 1.42x faster                                                          |
| regex_dna      | 115 ms                                                      | 114 ms: 1.02x faster                                                           |
| regex_compile  | 80.5 ms                                                     | 99.9 ms: 1.24x slower                                                          |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.6 ms                                                     | 96.0 ms: 1.03x slower                                                          |
| xml_etree_iterparse  | 61.8 ms                                                     | 69.9 ms: 1.13x slower                                                          |
| xml_etree_generate   | 54.0 ms                                                     | 63.6 ms: 1.18x slower                                                          |
| json_dumps           | 5.92 ms                                                     | 7.13 ms: 1.21x slower                                                          |
| xml_etree_process    | 37.0 ms                                                     | 45.9 ms: 1.24x slower                                                          |
| tomli_loads          | 1.39 sec                                                    | 1.77 sec: 1.27x slower                                                         |
| pickle_pure_python   | 190 us                                                      | 249 us: 1.32x slower                                                           |
| unpickle_pure_python | 133 us                                                      | 183 us: 1.37x slower                                                           |
| Geometric mean       | (ref)                                                       | 1.19x slower                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 24.1 ms: 1.06x faster                                                          |
| python_startup_no_site | 18.1 ms                                                     | 17.7 ms: 1.03x faster                                                          |
| Geometric mean         | (ref)                                                       | 1.04x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 42.6 ms: 1.20x slower                                                          |
| mako            | 6.35 ms                                                     | 8.02 ms: 1.26x slower                                                          |
| django_template | 22.4 ms                                                     | 28.4 ms: 1.27x slower                                                          |
| genshi_text     | 15.6 ms                                                     | 20.1 ms: 1.29x slower                                                          |
| Geometric mean  | (ref)                                                       | 1.25x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 572 us: 15.37x faster                                                          |
| regex_v8                   | 21.4 ms                                                     | 15.1 ms: 1.42x faster                                                          |
| deepcopy                   | 226 us                                                      | 212 us: 1.07x faster                                                           |
| python_startup             | 25.4 ms                                                     | 24.1 ms: 1.06x faster                                                          |
| async_tree_memoization_tg  | 288 ms                                                      | 276 ms: 1.05x faster                                                           |
| bench_mp_pool              | 86.4 ms                                                     | 84.0 ms: 1.03x faster                                                          |
| python_startup_no_site     | 18.1 ms                                                     | 17.7 ms: 1.03x faster                                                          |
| gc_traversal               | 1.97 ms                                                     | 1.92 ms: 1.03x faster                                                          |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.02x faster                                                           |
| pathlib                    | 80.9 ms                                                     | 79.7 ms: 1.01x faster                                                          |
| asyncio_websockets         | 318 ms                                                      | 313 ms: 1.01x faster                                                           |
| xml_etree_parse            | 93.6 ms                                                     | 96.0 ms: 1.03x slower                                                          |
| tornado_http               | 93.0 ms                                                     | 96.4 ms: 1.04x slower                                                          |
| connected_components       | 332 ms                                                      | 348 ms: 1.05x slower                                                           |
| shortest_path              | 362 ms                                                      | 379 ms: 1.05x slower                                                           |
| async_tree_none            | 226 ms                                                      | 237 ms: 1.05x slower                                                           |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 402 ms: 1.05x slower                                                           |
| deepcopy_reduce            | 2.06 us                                                     | 2.19 us: 1.06x slower                                                          |
| deepcopy_memo              | 23.3 us                                                     | 24.9 us: 1.07x slower                                                          |
| async_tree_memoization     | 276 ms                                                      | 294 ms: 1.07x slower                                                           |
| coverage                   | 45.6 ms                                                     | 48.8 ms: 1.07x slower                                                          |
| async_tree_none_tg         | 209 ms                                                      | 224 ms: 1.07x slower                                                           |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 407 ms: 1.08x slower                                                           |
| telco                      | 4.79 ms                                                     | 5.17 ms: 1.08x slower                                                          |
| create_gc_cycles           | 1.26 ms                                                     | 1.37 ms: 1.09x slower                                                          |
| dulwich_log                | 40.8 ms                                                     | 44.7 ms: 1.10x slower                                                          |
| sympy_sum                  | 86.9 ms                                                     | 95.9 ms: 1.10x slower                                                          |
| meteor_contest             | 73.5 ms                                                     | 81.5 ms: 1.11x slower                                                          |
| pylint                     | 211 ms                                                      | 234 ms: 1.11x slower                                                           |
| sphinx                     | 633 ms                                                      | 705 ms: 1.11x slower                                                           |
| 2to3                       | 221 ms                                                      | 247 ms: 1.12x slower                                                           |
| sympy_expand               | 291 ms                                                      | 329 ms: 1.13x slower                                                           |
| docutils                   | 1.57 sec                                                    | 1.77 sec: 1.13x slower                                                         |
| sympy_str                  | 169 ms                                                      | 191 ms: 1.13x slower                                                           |
| xml_etree_iterparse        | 61.8 ms                                                     | 69.9 ms: 1.13x slower                                                          |
| async_tree_io              | 521 ms                                                      | 592 ms: 1.14x slower                                                           |
| sympy_integrate            | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                          |
| html5lib                   | 38.9 ms                                                     | 45.0 ms: 1.16x slower                                                          |
| bpe_tokeniser              | 2.91 sec                                                    | 3.42 sec: 1.17x slower                                                         |
| xml_etree_generate         | 54.0 ms                                                     | 63.6 ms: 1.18x slower                                                          |
| mdp                        | 1.39 sec                                                    | 1.64 sec: 1.18x slower                                                         |
| coroutines                 | 12.8 ms                                                     | 15.1 ms: 1.18x slower                                                          |
| typing_runtime_protocols   | 105 us                                                      | 126 us: 1.20x slower                                                           |
| logging_simple             | 5.96 us                                                     | 7.15 us: 1.20x slower                                                          |
| genshi_xml                 | 35.5 ms                                                     | 42.6 ms: 1.20x slower                                                          |
| pycparser                  | 683 ms                                                      | 820 ms: 1.20x slower                                                           |
| json_dumps                 | 5.92 ms                                                     | 7.13 ms: 1.21x slower                                                          |
| logging_format             | 6.26 us                                                     | 7.61 us: 1.22x slower                                                          |
| async_generators           | 223 ms                                                      | 273 ms: 1.22x slower                                                           |
| sqlglot_normalize          | 175 ms                                                      | 214 ms: 1.22x slower                                                           |
| sqlglot_optimize           | 32.9 ms                                                     | 40.3 ms: 1.22x slower                                                          |
| float                      | 49.9 ms                                                     | 61.5 ms: 1.23x slower                                                          |
| xml_etree_process          | 37.0 ms                                                     | 45.9 ms: 1.24x slower                                                          |
| regex_compile              | 80.5 ms                                                     | 99.9 ms: 1.24x slower                                                          |
| pprint_safe_repr           | 494 ms                                                      | 614 ms: 1.24x slower                                                           |
| pprint_pformat             | 999 ms                                                      | 1.25 sec: 1.25x slower                                                         |
| go                         | 87.0 ms                                                     | 110 ms: 1.26x slower                                                           |
| mako                       | 6.35 ms                                                     | 8.02 ms: 1.26x slower                                                          |
| crypto_pyaes               | 45.4 ms                                                     | 57.4 ms: 1.26x slower                                                          |
| pyflate                    | 283 ms                                                      | 358 ms: 1.26x slower                                                           |
| tomli_loads                | 1.39 sec                                                    | 1.77 sec: 1.27x slower                                                         |
| django_template            | 22.4 ms                                                     | 28.4 ms: 1.27x slower                                                          |
| async_tree_io_tg           | 518 ms                                                      | 660 ms: 1.27x slower                                                           |
| spectral_norm              | 62.8 ms                                                     | 80.7 ms: 1.29x slower                                                          |
| genshi_text                | 15.6 ms                                                     | 20.1 ms: 1.29x slower                                                          |
| nqueens                    | 56.7 ms                                                     | 73.3 ms: 1.29x slower                                                          |
| generators                 | 19.5 ms                                                     | 25.2 ms: 1.29x slower                                                          |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 3.18 ms: 1.30x slower                                                          |
| fannkuch                   | 253 ms                                                      | 330 ms: 1.30x slower                                                           |
| logging_silent             | 54.6 ns                                                     | 71.3 ns: 1.31x slower                                                          |
| sqlglot_transpile          | 956 us                                                      | 1.25 ms: 1.31x slower                                                          |
| nbody                      | 68.4 ms                                                     | 89.4 ms: 1.31x slower                                                          |
| scimark_fft                | 172 ms                                                      | 226 ms: 1.31x slower                                                           |
| pickle_pure_python         | 190 us                                                      | 249 us: 1.32x slower                                                           |
| hexiom                     | 3.89 ms                                                     | 5.14 ms: 1.32x slower                                                          |
| sqlglot_parse              | 771 us                                                      | 1.02 ms: 1.33x slower                                                          |
| scimark_monte_carlo        | 40.8 ms                                                     | 54.7 ms: 1.34x slower                                                          |
| richards_super             | 30.9 ms                                                     | 41.4 ms: 1.34x slower                                                          |
| chaos                      | 38.5 ms                                                     | 52.0 ms: 1.35x slower                                                          |
| richards                   | 27.3 ms                                                     | 36.9 ms: 1.35x slower                                                          |
| deltablue                  | 1.92 ms                                                     | 2.60 ms: 1.36x slower                                                          |
| scimark_sor                | 76.2 ms                                                     | 103 ms: 1.36x slower                                                           |
| unpickle_pure_python       | 133 us                                                      | 183 us: 1.37x slower                                                           |
| raytrace                   | 160 ms                                                      | 220 ms: 1.38x slower                                                           |
| scimark_lu                 | 53.0 ms                                                     | 74.6 ms: 1.41x slower                                                          |
| comprehensions             | 10.3 us                                                     | 14.6 us: 1.42x slower                                                          |
| k_core                     | 1.74 sec                                                    | 2.59 sec: 1.49x slower                                                         |
| Geometric mean             | (ref)                                                       | 1.13x slower                                                                   |

Benchmark hidden because not significant (5): json_loads, pidigits, regex_effbot, bench_thread_pool, json
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of results/bm-20241029-3.14.0a1+-f03f745/bm-20241029-pythonperf1-amd64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745.json: sqlite_synth

- Geometric mean (including insignificant results): 1.114x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.12x

# Memory
- memory change: unknown