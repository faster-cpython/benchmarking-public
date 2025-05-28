# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: windows-amd64
- commit hash: a684067
- commit date: 2025-05-28
- overall geometric mean: 1.027x slower
- HPT reliability: 99.32%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 219 ms: 1.02x slower                                                                 |
| docutils       | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                               |
| sphinx         | 617 ms                                                      | 637 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                         |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.88x faster                                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.28x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 402 ms: 1.28x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 401 ms: 1.24x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.17x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                                 |
| async_generators           | 223 ms                                                      | 233 ms: 1.05x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.8 ms: 1.11x faster                                                                |
| nbody          | 66.3 ms                                                     | 64.1 ms: 1.03x faster                                                                |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                                |
| regex_effbot   | 1.69 ms                                                     | 1.58 ms: 1.08x faster                                                                |
| regex_compile  | 80.7 ms                                                     | 81.6 ms: 1.01x slower                                                                |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 87.6 ms: 1.05x faster                                                                |
| json_loads           | 15.1 us                                                     | 14.9 us: 1.01x faster                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                               |
| json_dumps           | 6.19 ms                                                     | 6.28 ms: 1.01x slower                                                                |
| xml_etree_generate   | 53.5 ms                                                     | 55.2 ms: 1.03x slower                                                                |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.3 ms: 1.05x slower                                                                |
| xml_etree_process    | 36.5 ms                                                     | 38.7 ms: 1.06x slower                                                                |
| unpickle_pure_python | 130 us                                                      | 139 us: 1.07x slower                                                                 |
| pickle_pure_python   | 186 us                                                      | 214 us: 1.15x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                                |
| python_startup_no_site | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.64 ms: 1.01x slower                                                                |
| django_template | 20.3 ms                                                     | 23.9 ms: 1.18x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                                         |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 29.6 ms: 2.54x faster                                                                |
| asyncio_websockets         | 300 ms                                                      | 160 ms: 1.88x faster                                                                 |
| mdp                        | 1.43 sec                                                    | 817 ms: 1.75x faster                                                                 |
| regex_v8                   | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                                |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                                 |
| deepcopy                   | 223 us                                                      | 172 us: 1.30x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.28x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 402 ms: 1.28x faster                                                                 |
| deepcopy_memo              | 23.1 us                                                     | 18.5 us: 1.25x faster                                                                |
| async_tree_io_tg           | 497 ms                                                      | 401 ms: 1.24x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.17x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 328 ms: 1.16x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                                 |
| float                      | 50.8 ms                                                     | 45.8 ms: 1.11x faster                                                                |
| go                         | 84.7 ms                                                     | 77.2 ms: 1.10x faster                                                                |
| spectral_norm              | 63.4 ms                                                     | 58.5 ms: 1.08x faster                                                                |
| deepcopy_reduce            | 2.02 us                                                     | 1.88 us: 1.08x faster                                                                |
| regex_effbot               | 1.69 ms                                                     | 1.58 ms: 1.08x faster                                                                |
| xml_etree_parse            | 92.2 ms                                                     | 87.6 ms: 1.05x faster                                                                |
| json                       | 3.30 ms                                                     | 3.15 ms: 1.05x faster                                                                |
| telco                      | 4.85 ms                                                     | 4.67 ms: 1.04x faster                                                                |
| nbody                      | 66.3 ms                                                     | 64.1 ms: 1.03x faster                                                                |
| typing_runtime_protocols   | 103 us                                                      | 101 us: 1.02x faster                                                                 |
| pyflate                    | 283 ms                                                      | 279 ms: 1.01x faster                                                                 |
| json_loads                 | 15.1 us                                                     | 14.9 us: 1.01x faster                                                                |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.9 ms: 1.00x slower                                                                |
| sqlite_synth               | 1.59 us                                                     | 1.59 us: 1.01x slower                                                                |
| shortest_path              | 355 ms                                                      | 358 ms: 1.01x slower                                                                 |
| scimark_sor                | 76.2 ms                                                     | 76.8 ms: 1.01x slower                                                                |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                                 |
| bpe_tokeniser              | 2.87 sec                                                    | 2.90 sec: 1.01x slower                                                               |
| regex_compile              | 80.7 ms                                                     | 81.6 ms: 1.01x slower                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                               |
| mako                       | 6.56 ms                                                     | 6.64 ms: 1.01x slower                                                                |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.01x slower                                                                |
| meteor_contest             | 72.0 ms                                                     | 72.9 ms: 1.01x slower                                                                |
| json_dumps                 | 6.19 ms                                                     | 6.28 ms: 1.01x slower                                                                |
| sympy_str                  | 167 ms                                                      | 169 ms: 1.01x slower                                                                 |
| sympy_expand               | 286 ms                                                      | 290 ms: 1.02x slower                                                                 |
| 2to3                       | 215 ms                                                      | 219 ms: 1.02x slower                                                                 |
| chaos                      | 37.9 ms                                                     | 38.5 ms: 1.02x slower                                                                |
| fannkuch                   | 252 ms                                                      | 256 ms: 1.02x slower                                                                 |
| dulwich_log                | 40.1 ms                                                     | 40.9 ms: 1.02x slower                                                                |
| sphinx                     | 617 ms                                                      | 637 ms: 1.03x slower                                                                 |
| xml_etree_generate         | 53.5 ms                                                     | 55.2 ms: 1.03x slower                                                                |
| sympy_sum                  | 85.2 ms                                                     | 88.0 ms: 1.03x slower                                                                |
| connected_components       | 320 ms                                                      | 331 ms: 1.03x slower                                                                 |
| python_startup             | 24.4 ms                                                     | 25.2 ms: 1.03x slower                                                                |
| scimark_fft                | 175 ms                                                      | 181 ms: 1.04x slower                                                                 |
| crypto_pyaes               | 45.6 ms                                                     | 47.3 ms: 1.04x slower                                                                |
| scimark_lu                 | 56.7 ms                                                     | 58.8 ms: 1.04x slower                                                                |
| bench_thread_pool          | 810 us                                                      | 843 us: 1.04x slower                                                                 |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.3 ms: 1.05x slower                                                                |
| async_generators           | 223 ms                                                      | 233 ms: 1.05x slower                                                                 |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                                 |
| richards                   | 26.3 ms                                                     | 27.6 ms: 1.05x slower                                                                |
| generators                 | 19.0 ms                                                     | 20.0 ms: 1.06x slower                                                                |
| docutils                   | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                               |
| xml_etree_process          | 36.5 ms                                                     | 38.7 ms: 1.06x slower                                                                |
| comprehensions             | 10.4 us                                                     | 11.0 us: 1.06x slower                                                                |
| richards_super             | 29.8 ms                                                     | 31.6 ms: 1.06x slower                                                                |
| unpickle_pure_python       | 130 us                                                      | 139 us: 1.07x slower                                                                 |
| create_gc_cycles           | 1.22 ms                                                     | 1.31 ms: 1.07x slower                                                                |
| hexiom                     | 3.84 ms                                                     | 4.15 ms: 1.08x slower                                                                |
| logging_simple             | 5.77 us                                                     | 6.33 us: 1.10x slower                                                                |
| logging_format             | 6.18 us                                                     | 6.79 us: 1.10x slower                                                                |
| bench_mp_pool              | 84.2 ms                                                     | 92.7 ms: 1.10x slower                                                                |
| gc_traversal               | 1.96 ms                                                     | 2.19 ms: 1.12x slower                                                                |
| nqueens                    | 56.1 ms                                                     | 62.9 ms: 1.12x slower                                                                |
| python_startup_no_site     | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                                |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                                |
| pickle_pure_python         | 186 us                                                      | 214 us: 1.15x slower                                                                 |
| pprint_safe_repr           | 485 ms                                                      | 558 ms: 1.15x slower                                                                 |
| deltablue                  | 1.89 ms                                                     | 2.20 ms: 1.16x slower                                                                |
| pprint_pformat             | 977 ms                                                      | 1.14 sec: 1.16x slower                                                               |
| django_template            | 20.3 ms                                                     | 23.9 ms: 1.18x slower                                                                |
| raytrace                   | 153 ms                                                      | 182 ms: 1.19x slower                                                                 |
| many_optionals             | 361 us                                                      | 435 us: 1.20x slower                                                                 |
| subparsers                 | 10.9 ms                                                     | 17.0 ms: 1.57x slower                                                                |
| logging_silent             | 54.6 ns                                                     | 318 ns: 5.83x slower                                                                 |
| coverage                   | 45.3 ms                                                     | 291 ms: 6.43x slower                                                                 |
| thrift                     | 8.47 ms                                                     | 93.3 ms: 11.02x slower                                                               |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                                         |

Benchmark hidden because not significant (7): pylint, k_core, scimark_sparse_mat_mult, genshi_text, html5lib, genshi_xml, pycparser
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250528-3.15.0a0-a684067/bm-20250528-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.027x slower

# HPT report

- Reliability score: 99.32% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown