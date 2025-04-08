# Results vs. 3.13.0

- fork: python
- ref: 275056a7fdcbe36aaac4
- machine: windows-amd64
- commit hash: 275056a
- commit date: 2025-04-03
- overall geometric mean: 1.197x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 203 ms: 1.06x faster                                                        |
| html5lib       | 38.2 ms                                                     | 34.0 ms: 1.12x faster                                                       |
| sphinx         | 617 ms                                                      | 595 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.87x faster                                                        |
| async_tree_io              | 513 ms                                                      | 342 ms: 1.50x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 182 ms: 1.45x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 345 ms: 1.44x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 195 ms: 1.44x faster                                                        |
| async_tree_none            | 219 ms                                                      | 155 ms: 1.41x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 149 ms: 1.35x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 310 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 313 ms: 1.22x faster                                                        |
| async_generators           | 223 ms                                                      | 186 ms: 1.20x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 10.9 ms: 1.15x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.37x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 35.5 ms: 1.43x faster                                                       |
| nbody          | 66.3 ms                                                     | 50.4 ms: 1.31x faster                                                       |
| pidigits       | 146 ms                                                      | 145 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.24x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.3 ms: 1.79x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 67.8 ms: 1.19x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.59 ms: 1.07x faster                                                       |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.01 sec: 1.35x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 102 us: 1.27x faster                                                        |
| pickle_pure_python   | 186 us                                                      | 165 us: 1.13x faster                                                        |
| json_loads           | 15.1 us                                                     | 13.5 us: 1.12x faster                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 48.1 ms: 1.11x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 5.59 ms: 1.11x faster                                                       |
| xml_etree_process    | 36.5 ms                                                     | 33.0 ms: 1.11x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 88.4 ms: 1.04x faster                                                       |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.5 ms: 1.09x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 21.0 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 11.2 ms: 1.36x faster                                                       |
| genshi_xml      | 33.9 ms                                                     | 28.1 ms: 1.20x faster                                                       |
| mako            | 6.56 ms                                                     | 5.66 ms: 1.16x faster                                                       |
| django_template | 20.3 ms                                                     | 19.5 ms: 1.04x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 30.9 ms: 2.44x faster                                                       |
| mdp                        | 1.43 sec                                                    | 669 ms: 2.14x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.87x faster                                                        |
| regex_v8                   | 23.8 ms                                                     | 13.3 ms: 1.79x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 13.1 us: 1.76x faster                                                       |
| deepcopy                   | 223 us                                                      | 138 us: 1.62x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 47.8 ms: 1.59x faster                                                       |
| async_tree_io              | 513 ms                                                      | 342 ms: 1.50x faster                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 27.3 ms: 1.49x faster                                                       |
| go                         | 84.7 ms                                                     | 58.2 ms: 1.46x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 182 ms: 1.45x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 345 ms: 1.44x faster                                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 195 ms: 1.44x faster                                                        |
| float                      | 50.8 ms                                                     | 35.5 ms: 1.43x faster                                                       |
| async_tree_none            | 219 ms                                                      | 155 ms: 1.41x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.48 us: 1.37x faster                                                       |
| genshi_text                | 15.2 ms                                                     | 11.2 ms: 1.36x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 46.8 ms: 1.36x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.01 sec: 1.35x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 149 ms: 1.35x faster                                                        |
| logging_silent             | 54.6 ns                                                     | 41.0 ns: 1.33x faster                                                       |
| hexiom                     | 3.84 ms                                                     | 2.91 ms: 1.32x faster                                                       |
| nbody                      | 66.3 ms                                                     | 50.4 ms: 1.31x faster                                                       |
| fannkuch                   | 252 ms                                                      | 192 ms: 1.31x faster                                                        |
| unpickle_pure_python       | 130 us                                                      | 102 us: 1.27x faster                                                        |
| generators                 | 19.0 ms                                                     | 15.0 ms: 1.27x faster                                                       |
| richards                   | 26.3 ms                                                     | 20.7 ms: 1.27x faster                                                       |
| scimark_lu                 | 56.7 ms                                                     | 45.1 ms: 1.26x faster                                                       |
| deltablue                  | 1.89 ms                                                     | 1.52 ms: 1.25x faster                                                       |
| scimark_fft                | 175 ms                                                      | 141 ms: 1.24x faster                                                        |
| comprehensions             | 10.4 us                                                     | 8.36 us: 1.24x faster                                                       |
| pyflate                    | 283 ms                                                      | 229 ms: 1.24x faster                                                        |
| chaos                      | 37.9 ms                                                     | 30.7 ms: 1.23x faster                                                       |
| pprint_safe_repr           | 485 ms                                                      | 393 ms: 1.23x faster                                                        |
| richards_super             | 29.8 ms                                                     | 24.3 ms: 1.23x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 310 ms: 1.22x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 313 ms: 1.22x faster                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.15 ms: 1.21x faster                                                       |
| genshi_xml                 | 33.9 ms                                                     | 28.1 ms: 1.20x faster                                                       |
| typing_runtime_protocols   | 103 us                                                      | 85.9 us: 1.20x faster                                                       |
| async_generators           | 223 ms                                                      | 186 ms: 1.20x faster                                                        |
| pprint_pformat             | 977 ms                                                      | 817 ms: 1.19x faster                                                        |
| regex_compile              | 80.7 ms                                                     | 67.8 ms: 1.19x faster                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 38.9 ms: 1.17x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.16 ms: 1.17x faster                                                       |
| json                       | 3.30 ms                                                     | 2.84 ms: 1.16x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.66 ms: 1.16x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 10.9 ms: 1.15x faster                                                       |
| coverage                   | 45.3 ms                                                     | 39.5 ms: 1.15x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.50 sec: 1.15x faster                                                      |
| raytrace                   | 153 ms                                                      | 135 ms: 1.14x faster                                                        |
| nqueens                    | 56.1 ms                                                     | 49.6 ms: 1.13x faster                                                       |
| pickle_pure_python         | 186 us                                                      | 165 us: 1.13x faster                                                        |
| html5lib                   | 38.2 ms                                                     | 34.0 ms: 1.12x faster                                                       |
| sympy_str                  | 167 ms                                                      | 149 ms: 1.12x faster                                                        |
| json_loads                 | 15.1 us                                                     | 13.5 us: 1.12x faster                                                       |
| pylint                     | 205 ms                                                      | 184 ms: 1.12x faster                                                        |
| xml_etree_generate         | 53.5 ms                                                     | 48.1 ms: 1.11x faster                                                       |
| sympy_expand               | 286 ms                                                      | 257 ms: 1.11x faster                                                        |
| json_dumps                 | 6.19 ms                                                     | 5.59 ms: 1.11x faster                                                       |
| xml_etree_process          | 36.5 ms                                                     | 33.0 ms: 1.11x faster                                                       |
| sympy_integrate            | 12.3 ms                                                     | 11.2 ms: 1.10x faster                                                       |
| pycparser                  | 695 ms                                                      | 636 ms: 1.09x faster                                                        |
| meteor_contest             | 72.0 ms                                                     | 66.3 ms: 1.08x faster                                                       |
| sympy_sum                  | 85.2 ms                                                     | 78.6 ms: 1.08x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.59 ms: 1.07x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.49 us: 1.06x faster                                                       |
| 2to3                       | 215 ms                                                      | 203 ms: 1.06x faster                                                        |
| dulwich_log                | 40.1 ms                                                     | 37.8 ms: 1.06x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.60 sec: 1.06x faster                                                      |
| logging_simple             | 5.77 us                                                     | 5.53 us: 1.04x faster                                                       |
| django_template            | 20.3 ms                                                     | 19.5 ms: 1.04x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 88.4 ms: 1.04x faster                                                       |
| sphinx                     | 617 ms                                                      | 595 ms: 1.04x faster                                                        |
| shortest_path              | 355 ms                                                      | 345 ms: 1.03x faster                                                        |
| logging_format             | 6.18 us                                                     | 6.00 us: 1.03x faster                                                       |
| pidigits                   | 146 ms                                                      | 145 ms: 1.01x faster                                                        |
| bench_thread_pool          | 810 us                                                      | 831 us: 1.03x slower                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 87.8 ms: 1.04x slower                                                       |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                                       |
| python_startup             | 24.4 ms                                                     | 26.5 ms: 1.09x slower                                                       |
| many_optionals             | 361 us                                                      | 393 us: 1.09x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 21.0 ms: 1.24x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 14.4 ms: 1.33x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.79 ms: 1.42x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (3): xml_etree_iterparse, docutils, connected_components
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250403-3.14.0a6+-275056a-CLANG/bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.197x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown