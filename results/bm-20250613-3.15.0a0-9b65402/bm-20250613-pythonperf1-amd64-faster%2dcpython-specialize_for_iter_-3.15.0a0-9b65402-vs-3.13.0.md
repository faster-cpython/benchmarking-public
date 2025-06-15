# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: windows-amd64
- commit hash: 9b65402
- commit date: 2025-06-13
- overall geometric mean: 1.023x slower
- HPT reliability: 97.05%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 222 ms: 1.03x slower                                                                 |
| docutils       | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                               |
| sphinx         | 617 ms                                                      | 637 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                         |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.28x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.28x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 345 ms: 1.11x faster                                                                 |
| async_generators           | 223 ms                                                      | 229 ms: 1.03x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.6 ms: 1.14x faster                                                                |
| nbody          | 66.3 ms                                                     | 61.8 ms: 1.07x faster                                                                |
| pidigits       | 146 ms                                                      | 149 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.9 ms: 1.72x faster                                                                |
| regex_effbot   | 1.69 ms                                                     | 1.53 ms: 1.11x faster                                                                |
| regex_dna      | 115 ms                                                      | 119 ms: 1.04x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                         |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.3 us: 1.06x faster                                                                |
| xml_etree_parse      | 92.2 ms                                                     | 90.2 ms: 1.02x faster                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                               |
| json_dumps           | 6.19 ms                                                     | 6.31 ms: 1.02x slower                                                                |
| unpickle_pure_python | 130 us                                                      | 134 us: 1.03x slower                                                                 |
| xml_etree_generate   | 53.5 ms                                                     | 55.8 ms: 1.04x slower                                                                |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.1 ms: 1.06x slower                                                                |
| xml_etree_process    | 36.5 ms                                                     | 39.3 ms: 1.08x slower                                                                |
| pickle_pure_python   | 186 us                                                      | 212 us: 1.14x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.7 ms: 1.05x slower                                                                |
| python_startup_no_site | 16.9 ms                                                     | 19.2 ms: 1.13x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                                                |
| mako            | 6.56 ms                                                     | 6.64 ms: 1.01x slower                                                                |
| django_template | 20.3 ms                                                     | 23.7 ms: 1.17x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                                         |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.4 ms: 2.32x faster                                                                |
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                                 |
| mdp                        | 1.43 sec                                                    | 805 ms: 1.78x faster                                                                 |
| regex_v8                   | 23.8 ms                                                     | 13.9 ms: 1.72x faster                                                                |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                                 |
| deepcopy                   | 223 us                                                      | 170 us: 1.31x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.28x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 208 ms: 1.28x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                                                 |
| deepcopy_memo              | 23.1 us                                                     | 18.2 us: 1.27x faster                                                                |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                                 |
| float                      | 50.8 ms                                                     | 44.6 ms: 1.14x faster                                                                |
| go                         | 84.7 ms                                                     | 76.1 ms: 1.11x faster                                                                |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 345 ms: 1.11x faster                                                                 |
| json                       | 3.30 ms                                                     | 2.98 ms: 1.11x faster                                                                |
| regex_effbot               | 1.69 ms                                                     | 1.53 ms: 1.11x faster                                                                |
| deepcopy_reduce            | 2.02 us                                                     | 1.85 us: 1.09x faster                                                                |
| nbody                      | 66.3 ms                                                     | 61.8 ms: 1.07x faster                                                                |
| spectral_norm              | 63.4 ms                                                     | 60.0 ms: 1.06x faster                                                                |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.06x faster                                                                |
| telco                      | 4.85 ms                                                     | 4.63 ms: 1.05x faster                                                                |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.51 ms: 1.04x faster                                                                |
| xml_etree_parse            | 92.2 ms                                                     | 90.2 ms: 1.02x faster                                                                |
| pyflate                    | 283 ms                                                      | 280 ms: 1.01x faster                                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                               |
| sqlite_synth               | 1.59 us                                                     | 1.58 us: 1.01x faster                                                                |
| genshi_text                | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                                                |
| meteor_contest             | 72.0 ms                                                     | 71.6 ms: 1.01x faster                                                                |
| scimark_sor                | 76.2 ms                                                     | 76.9 ms: 1.01x slower                                                                |
| sympy_expand               | 286 ms                                                      | 289 ms: 1.01x slower                                                                 |
| sympy_str                  | 167 ms                                                      | 169 ms: 1.01x slower                                                                 |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.01x slower                                                                |
| mako                       | 6.56 ms                                                     | 6.64 ms: 1.01x slower                                                                |
| pidigits                   | 146 ms                                                      | 149 ms: 1.01x slower                                                                 |
| json_dumps                 | 6.19 ms                                                     | 6.31 ms: 1.02x slower                                                                |
| chaos                      | 37.9 ms                                                     | 38.7 ms: 1.02x slower                                                                |
| crypto_pyaes               | 45.6 ms                                                     | 46.6 ms: 1.02x slower                                                                |
| fannkuch                   | 252 ms                                                      | 257 ms: 1.02x slower                                                                 |
| sympy_sum                  | 85.2 ms                                                     | 87.2 ms: 1.02x slower                                                                |
| richards                   | 26.3 ms                                                     | 26.9 ms: 1.03x slower                                                                |
| generators                 | 19.0 ms                                                     | 19.5 ms: 1.03x slower                                                                |
| bpe_tokeniser              | 2.87 sec                                                    | 2.95 sec: 1.03x slower                                                               |
| unpickle_pure_python       | 130 us                                                      | 134 us: 1.03x slower                                                                 |
| async_generators           | 223 ms                                                      | 229 ms: 1.03x slower                                                                 |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.9 ms: 1.03x slower                                                                |
| 2to3                       | 215 ms                                                      | 222 ms: 1.03x slower                                                                 |
| sphinx                     | 617 ms                                                      | 637 ms: 1.03x slower                                                                 |
| shortest_path              | 355 ms                                                      | 367 ms: 1.03x slower                                                                 |
| richards_super             | 29.8 ms                                                     | 30.8 ms: 1.04x slower                                                                |
| dulwich_log                | 40.1 ms                                                     | 41.5 ms: 1.04x slower                                                                |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.04x slower                                                                 |
| scimark_lu                 | 56.7 ms                                                     | 58.8 ms: 1.04x slower                                                                |
| scimark_fft                | 175 ms                                                      | 182 ms: 1.04x slower                                                                 |
| comprehensions             | 10.4 us                                                     | 10.8 us: 1.04x slower                                                                |
| xml_etree_generate         | 53.5 ms                                                     | 55.8 ms: 1.04x slower                                                                |
| python_startup             | 24.4 ms                                                     | 25.7 ms: 1.05x slower                                                                |
| connected_components       | 320 ms                                                      | 337 ms: 1.05x slower                                                                 |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.1 ms: 1.06x slower                                                                |
| docutils                   | 1.53 sec                                                    | 1.62 sec: 1.06x slower                                                               |
| hexiom                     | 3.84 ms                                                     | 4.08 ms: 1.06x slower                                                                |
| xml_etree_process          | 36.5 ms                                                     | 39.3 ms: 1.08x slower                                                                |
| nqueens                    | 56.1 ms                                                     | 60.6 ms: 1.08x slower                                                                |
| logging_simple             | 5.77 us                                                     | 6.29 us: 1.09x slower                                                                |
| create_gc_cycles           | 1.22 ms                                                     | 1.34 ms: 1.09x slower                                                                |
| gc_traversal               | 1.96 ms                                                     | 2.15 ms: 1.09x slower                                                                |
| logging_format             | 6.18 us                                                     | 6.77 us: 1.10x slower                                                                |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                                                |
| pprint_safe_repr           | 485 ms                                                      | 547 ms: 1.13x slower                                                                 |
| python_startup_no_site     | 16.9 ms                                                     | 19.2 ms: 1.13x slower                                                                |
| pprint_pformat             | 977 ms                                                      | 1.11 sec: 1.13x slower                                                               |
| pickle_pure_python         | 186 us                                                      | 212 us: 1.14x slower                                                                 |
| django_template            | 20.3 ms                                                     | 23.7 ms: 1.17x slower                                                                |
| deltablue                  | 1.89 ms                                                     | 2.22 ms: 1.17x slower                                                                |
| raytrace                   | 153 ms                                                      | 180 ms: 1.18x slower                                                                 |
| many_optionals             | 361 us                                                      | 442 us: 1.22x slower                                                                 |
| subparsers                 | 10.9 ms                                                     | 17.1 ms: 1.57x slower                                                                |
| logging_silent             | 54.6 ns                                                     | 316 ns: 5.80x slower                                                                 |
| coverage                   | 45.3 ms                                                     | 289 ms: 6.38x slower                                                                 |
| thrift                     | 8.47 ms                                                     | 98.5 ms: 11.63x slower                                                               |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                         |

Benchmark hidden because not significant (7): pylint, typing_runtime_protocols, regex_compile, k_core, genshi_xml, html5lib, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250613-3.15.0a0-9b65402/bm-20250613-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.023x slower

# HPT report

- Reliability score: 97.05% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown