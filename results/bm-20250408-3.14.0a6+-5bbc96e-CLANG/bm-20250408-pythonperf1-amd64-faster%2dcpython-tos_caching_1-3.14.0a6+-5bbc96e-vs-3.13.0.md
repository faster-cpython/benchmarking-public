# Results vs. 3.13.0

- fork: faster-cpython
- ref: tos_caching_1
- machine: windows-amd64
- commit hash: 5bbc96e
- commit date: 2025-04-08
- overall geometric mean: 1.206x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 198 ms: 1.09x faster                                                           |
| html5lib       | 38.2 ms                                                     | 33.3 ms: 1.15x faster                                                          |
| sphinx         | 617 ms                                                      | 592 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                   |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.85x faster                                                           |
| async_tree_io              | 513 ms                                                      | 343 ms: 1.50x faster                                                           |
| async_tree_memoization     | 265 ms                                                      | 183 ms: 1.44x faster                                                           |
| async_tree_memoization_tg  | 281 ms                                                      | 197 ms: 1.43x faster                                                           |
| async_tree_none            | 219 ms                                                      | 153 ms: 1.43x faster                                                           |
| async_tree_io_tg           | 497 ms                                                      | 350 ms: 1.42x faster                                                           |
| async_tree_none_tg         | 200 ms                                                      | 152 ms: 1.32x faster                                                           |
| async_generators           | 223 ms                                                      | 181 ms: 1.23x faster                                                           |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 311 ms: 1.22x faster                                                           |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 317 ms: 1.21x faster                                                           |
| coroutines                 | 12.5 ms                                                     | 10.9 ms: 1.15x faster                                                          |
| Geometric mean             | (ref)                                                       | 1.37x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 35.9 ms: 1.42x faster                                                          |
| nbody          | 66.3 ms                                                     | 52.8 ms: 1.26x faster                                                          |
| pidigits       | 146 ms                                                      | 144 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                       | 1.22x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 12.3 ms: 1.94x faster                                                          |
| regex_compile  | 80.7 ms                                                     | 67.5 ms: 1.20x faster                                                          |
| regex_effbot   | 1.69 ms                                                     | 1.47 ms: 1.15x faster                                                          |
| regex_dna      | 115 ms                                                      | 116 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                       | 1.28x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 981 ms: 1.40x faster                                                           |
| unpickle_pure_python | 130 us                                                      | 104 us: 1.25x faster                                                           |
| pickle_pure_python   | 186 us                                                      | 165 us: 1.12x faster                                                           |
| xml_etree_process    | 36.5 ms                                                     | 32.8 ms: 1.11x faster                                                          |
| json_dumps           | 6.19 ms                                                     | 5.58 ms: 1.11x faster                                                          |
| xml_etree_generate   | 53.5 ms                                                     | 48.8 ms: 1.10x faster                                                          |
| json_loads           | 15.1 us                                                     | 14.1 us: 1.07x faster                                                          |
| xml_etree_parse      | 92.2 ms                                                     | 89.6 ms: 1.03x faster                                                          |
| xml_etree_iterparse  | 60.5 ms                                                     | 61.0 ms: 1.01x slower                                                          |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.8 ms: 1.10x slower                                                          |
| python_startup_no_site | 16.9 ms                                                     | 20.7 ms: 1.22x slower                                                          |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 11.1 ms: 1.38x faster                                                          |
| genshi_xml      | 33.9 ms                                                     | 27.1 ms: 1.25x faster                                                          |
| mako            | 6.56 ms                                                     | 5.76 ms: 1.14x faster                                                          |
| django_template | 20.3 ms                                                     | 18.8 ms: 1.08x faster                                                          |
| Geometric mean  | (ref)                                                       | 1.21x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 30.7 ms: 2.46x faster                                                          |
| mdp                        | 1.43 sec                                                    | 671 ms: 2.13x faster                                                           |
| regex_v8                   | 23.8 ms                                                     | 12.3 ms: 1.94x faster                                                          |
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.85x faster                                                           |
| deepcopy_memo              | 23.1 us                                                     | 13.3 us: 1.74x faster                                                          |
| deepcopy                   | 223 us                                                      | 135 us: 1.66x faster                                                           |
| scimark_sor                | 76.2 ms                                                     | 47.2 ms: 1.62x faster                                                          |
| go                         | 84.7 ms                                                     | 54.8 ms: 1.54x faster                                                          |
| async_tree_io              | 513 ms                                                      | 343 ms: 1.50x faster                                                           |
| scimark_monte_carlo        | 40.7 ms                                                     | 27.5 ms: 1.48x faster                                                          |
| async_tree_memoization     | 265 ms                                                      | 183 ms: 1.44x faster                                                           |
| async_tree_memoization_tg  | 281 ms                                                      | 197 ms: 1.43x faster                                                           |
| async_tree_none            | 219 ms                                                      | 153 ms: 1.43x faster                                                           |
| deepcopy_reduce            | 2.02 us                                                     | 1.43 us: 1.42x faster                                                          |
| async_tree_io_tg           | 497 ms                                                      | 350 ms: 1.42x faster                                                           |
| float                      | 50.8 ms                                                     | 35.9 ms: 1.42x faster                                                          |
| spectral_norm              | 63.4 ms                                                     | 44.9 ms: 1.41x faster                                                          |
| tomli_loads                | 1.37 sec                                                    | 981 ms: 1.40x faster                                                           |
| genshi_text                | 15.2 ms                                                     | 11.1 ms: 1.38x faster                                                          |
| hexiom                     | 3.84 ms                                                     | 2.81 ms: 1.37x faster                                                          |
| generators                 | 19.0 ms                                                     | 14.2 ms: 1.34x faster                                                          |
| async_tree_none_tg         | 200 ms                                                      | 152 ms: 1.32x faster                                                           |
| logging_silent             | 54.6 ns                                                     | 42.4 ns: 1.29x faster                                                          |
| chaos                      | 37.9 ms                                                     | 29.5 ms: 1.28x faster                                                          |
| deltablue                  | 1.89 ms                                                     | 1.48 ms: 1.28x faster                                                          |
| pyflate                    | 283 ms                                                      | 224 ms: 1.27x faster                                                           |
| richards_super             | 29.8 ms                                                     | 23.5 ms: 1.26x faster                                                          |
| comprehensions             | 10.4 us                                                     | 8.19 us: 1.26x faster                                                          |
| richards                   | 26.3 ms                                                     | 20.8 ms: 1.26x faster                                                          |
| scimark_fft                | 175 ms                                                      | 139 ms: 1.26x faster                                                           |
| fannkuch                   | 252 ms                                                      | 200 ms: 1.26x faster                                                           |
| nbody                      | 66.3 ms                                                     | 52.8 ms: 1.26x faster                                                          |
| genshi_xml                 | 33.9 ms                                                     | 27.1 ms: 1.25x faster                                                          |
| scimark_lu                 | 56.7 ms                                                     | 45.4 ms: 1.25x faster                                                          |
| unpickle_pure_python       | 130 us                                                      | 104 us: 1.25x faster                                                           |
| async_generators           | 223 ms                                                      | 181 ms: 1.23x faster                                                           |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 311 ms: 1.22x faster                                                           |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.13 ms: 1.22x faster                                                          |
| nqueens                    | 56.1 ms                                                     | 46.2 ms: 1.21x faster                                                          |
| pprint_safe_repr           | 485 ms                                                      | 399 ms: 1.21x faster                                                           |
| crypto_pyaes               | 45.6 ms                                                     | 37.8 ms: 1.21x faster                                                          |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 317 ms: 1.21x faster                                                           |
| pprint_pformat             | 977 ms                                                      | 815 ms: 1.20x faster                                                           |
| regex_compile              | 80.7 ms                                                     | 67.5 ms: 1.20x faster                                                          |
| typing_runtime_protocols   | 103 us                                                      | 86.9 us: 1.19x faster                                                          |
| bpe_tokeniser              | 2.87 sec                                                    | 2.48 sec: 1.16x faster                                                         |
| regex_effbot               | 1.69 ms                                                     | 1.47 ms: 1.15x faster                                                          |
| telco                      | 4.85 ms                                                     | 4.22 ms: 1.15x faster                                                          |
| raytrace                   | 153 ms                                                      | 134 ms: 1.15x faster                                                           |
| json                       | 3.30 ms                                                     | 2.88 ms: 1.15x faster                                                          |
| coverage                   | 45.3 ms                                                     | 39.5 ms: 1.15x faster                                                          |
| html5lib                   | 38.2 ms                                                     | 33.3 ms: 1.15x faster                                                          |
| coroutines                 | 12.5 ms                                                     | 10.9 ms: 1.15x faster                                                          |
| mako                       | 6.56 ms                                                     | 5.76 ms: 1.14x faster                                                          |
| pickle_pure_python         | 186 us                                                      | 165 us: 1.12x faster                                                           |
| pylint                     | 205 ms                                                      | 183 ms: 1.12x faster                                                           |
| sympy_str                  | 167 ms                                                      | 149 ms: 1.12x faster                                                           |
| pycparser                  | 695 ms                                                      | 622 ms: 1.12x faster                                                           |
| sympy_expand               | 286 ms                                                      | 257 ms: 1.11x faster                                                           |
| xml_etree_process          | 36.5 ms                                                     | 32.8 ms: 1.11x faster                                                          |
| json_dumps                 | 6.19 ms                                                     | 5.58 ms: 1.11x faster                                                          |
| sympy_integrate            | 12.3 ms                                                     | 11.2 ms: 1.11x faster                                                          |
| xml_etree_generate         | 53.5 ms                                                     | 48.8 ms: 1.10x faster                                                          |
| logging_simple             | 5.77 us                                                     | 5.29 us: 1.09x faster                                                          |
| sympy_sum                  | 85.2 ms                                                     | 78.2 ms: 1.09x faster                                                          |
| 2to3                       | 215 ms                                                      | 198 ms: 1.09x faster                                                           |
| logging_format             | 6.18 us                                                     | 5.70 us: 1.08x faster                                                          |
| meteor_contest             | 72.0 ms                                                     | 66.4 ms: 1.08x faster                                                          |
| django_template            | 20.3 ms                                                     | 18.8 ms: 1.08x faster                                                          |
| sqlite_synth               | 1.59 us                                                     | 1.48 us: 1.07x faster                                                          |
| json_loads                 | 15.1 us                                                     | 14.1 us: 1.07x faster                                                          |
| k_core                     | 1.70 sec                                                    | 1.60 sec: 1.06x faster                                                         |
| sphinx                     | 617 ms                                                      | 592 ms: 1.04x faster                                                           |
| shortest_path              | 355 ms                                                      | 343 ms: 1.04x faster                                                           |
| xml_etree_parse            | 92.2 ms                                                     | 89.6 ms: 1.03x faster                                                          |
| pidigits                   | 146 ms                                                      | 144 ms: 1.01x faster                                                           |
| regex_dna                  | 115 ms                                                      | 116 ms: 1.01x slower                                                           |
| xml_etree_iterparse        | 60.5 ms                                                     | 61.0 ms: 1.01x slower                                                          |
| connected_components       | 320 ms                                                      | 325 ms: 1.02x slower                                                           |
| bench_thread_pool          | 810 us                                                      | 834 us: 1.03x slower                                                           |
| bench_mp_pool              | 84.2 ms                                                     | 88.3 ms: 1.05x slower                                                          |
| many_optionals             | 361 us                                                      | 391 us: 1.08x slower                                                           |
| python_startup             | 24.4 ms                                                     | 26.8 ms: 1.10x slower                                                          |
| create_gc_cycles           | 1.22 ms                                                     | 1.35 ms: 1.11x slower                                                          |
| python_startup_no_site     | 16.9 ms                                                     | 20.7 ms: 1.22x slower                                                          |
| subparsers                 | 10.9 ms                                                     | 14.1 ms: 1.30x slower                                                          |
| gc_traversal               | 1.96 ms                                                     | 2.77 ms: 1.41x slower                                                          |
| Geometric mean             | (ref)                                                       | 1.20x faster                                                                   |

Benchmark hidden because not significant (2): docutils, dulwich_log
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250408-3.14.0a6+-5bbc96e-CLANG/bm-20250408-pythonperf1-amd64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.206x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown