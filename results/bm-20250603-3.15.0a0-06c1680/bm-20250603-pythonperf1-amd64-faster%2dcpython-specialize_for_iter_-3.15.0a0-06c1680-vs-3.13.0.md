# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: windows-amd64
- commit hash: 06c1680
- commit date: 2025-06-03
- overall geometric mean: 1.015x slower
- HPT reliability: 70.55%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 219 ms: 1.02x slower                                                                 |
| docutils       | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                               |
| sphinx         | 617 ms                                                      | 632 ms: 1.02x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                         |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.86x faster                                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.35x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 394 ms: 1.30x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.12x faster                                                                 |
| async_generators           | 223 ms                                                      | 233 ms: 1.05x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.11x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.9 ms: 1.16x faster                                                                |
| nbody          | 66.3 ms                                                     | 60.9 ms: 1.09x faster                                                                |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.0 ms: 1.71x faster                                                                |
| regex_effbot   | 1.69 ms                                                     | 1.55 ms: 1.09x faster                                                                |
| regex_compile  | 80.7 ms                                                     | 79.6 ms: 1.01x faster                                                                |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.2 us: 1.06x faster                                                                |
| xml_etree_parse      | 92.2 ms                                                     | 89.5 ms: 1.03x faster                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.34 sec: 1.03x faster                                                               |
| json_dumps           | 6.19 ms                                                     | 6.30 ms: 1.02x slower                                                                |
| unpickle_pure_python | 130 us                                                      | 132 us: 1.02x slower                                                                 |
| xml_etree_generate   | 53.5 ms                                                     | 55.5 ms: 1.04x slower                                                                |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.3 ms: 1.05x slower                                                                |
| xml_etree_process    | 36.5 ms                                                     | 39.4 ms: 1.08x slower                                                                |
| pickle_pure_python   | 186 us                                                      | 208 us: 1.12x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.7 ms: 1.06x slower                                                                |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| django_template | 20.3 ms                                                     | 24.3 ms: 1.20x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                                         |

Benchmark hidden because not significant (3): genshi_text, mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 31.4 ms: 2.40x faster                                                                |
| asyncio_websockets         | 300 ms                                                      | 161 ms: 1.86x faster                                                                 |
| mdp                        | 1.43 sec                                                    | 806 ms: 1.78x faster                                                                 |
| regex_v8                   | 23.8 ms                                                     | 14.0 ms: 1.71x faster                                                                |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.35x faster                                                                 |
| deepcopy                   | 223 us                                                      | 169 us: 1.32x faster                                                                 |
| deepcopy_memo              | 23.1 us                                                     | 17.7 us: 1.30x faster                                                                |
| async_tree_io              | 513 ms                                                      | 394 ms: 1.30x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                                 |
| float                      | 50.8 ms                                                     | 43.9 ms: 1.16x faster                                                                |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.16x faster                                                                 |
| go                         | 84.7 ms                                                     | 73.9 ms: 1.15x faster                                                                |
| spectral_norm              | 63.4 ms                                                     | 56.6 ms: 1.12x faster                                                                |
| deepcopy_reduce            | 2.02 us                                                     | 1.81 us: 1.12x faster                                                                |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.12x faster                                                                 |
| regex_effbot               | 1.69 ms                                                     | 1.55 ms: 1.09x faster                                                                |
| nbody                      | 66.3 ms                                                     | 60.9 ms: 1.09x faster                                                                |
| json                       | 3.30 ms                                                     | 3.09 ms: 1.07x faster                                                                |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.06x faster                                                                |
| scimark_sor                | 76.2 ms                                                     | 73.2 ms: 1.04x faster                                                                |
| telco                      | 4.85 ms                                                     | 4.66 ms: 1.04x faster                                                                |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.51 ms: 1.04x faster                                                                |
| xml_etree_parse            | 92.2 ms                                                     | 89.5 ms: 1.03x faster                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.34 sec: 1.03x faster                                                               |
| pyflate                    | 283 ms                                                      | 277 ms: 1.02x faster                                                                 |
| regex_compile              | 80.7 ms                                                     | 79.6 ms: 1.01x faster                                                                |
| bpe_tokeniser              | 2.87 sec                                                    | 2.85 sec: 1.01x faster                                                               |
| fannkuch                   | 252 ms                                                      | 250 ms: 1.01x faster                                                                 |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.6 ms: 1.00x faster                                                                |
| sympy_expand               | 286 ms                                                      | 285 ms: 1.00x faster                                                                 |
| sympy_str                  | 167 ms                                                      | 167 ms: 1.00x slower                                                                 |
| meteor_contest             | 72.0 ms                                                     | 72.7 ms: 1.01x slower                                                                |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                                 |
| shortest_path              | 355 ms                                                      | 361 ms: 1.02x slower                                                                 |
| generators                 | 19.0 ms                                                     | 19.3 ms: 1.02x slower                                                                |
| dulwich_log                | 40.1 ms                                                     | 40.8 ms: 1.02x slower                                                                |
| json_dumps                 | 6.19 ms                                                     | 6.30 ms: 1.02x slower                                                                |
| unpickle_pure_python       | 130 us                                                      | 132 us: 1.02x slower                                                                 |
| 2to3                       | 215 ms                                                      | 219 ms: 1.02x slower                                                                 |
| crypto_pyaes               | 45.6 ms                                                     | 46.5 ms: 1.02x slower                                                                |
| sphinx                     | 617 ms                                                      | 632 ms: 1.02x slower                                                                 |
| sympy_sum                  | 85.2 ms                                                     | 87.2 ms: 1.02x slower                                                                |
| connected_components       | 320 ms                                                      | 331 ms: 1.03x slower                                                                 |
| xml_etree_generate         | 53.5 ms                                                     | 55.5 ms: 1.04x slower                                                                |
| hexiom                     | 3.84 ms                                                     | 3.99 ms: 1.04x slower                                                                |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                                 |
| scimark_lu                 | 56.7 ms                                                     | 59.1 ms: 1.04x slower                                                                |
| richards_super             | 29.8 ms                                                     | 31.1 ms: 1.04x slower                                                                |
| async_generators           | 223 ms                                                      | 233 ms: 1.05x slower                                                                 |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.3 ms: 1.05x slower                                                                |
| python_startup             | 24.4 ms                                                     | 25.7 ms: 1.06x slower                                                                |
| comprehensions             | 10.4 us                                                     | 11.0 us: 1.06x slower                                                                |
| richards                   | 26.3 ms                                                     | 27.8 ms: 1.06x slower                                                                |
| nqueens                    | 56.1 ms                                                     | 59.5 ms: 1.06x slower                                                                |
| docutils                   | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                               |
| logging_simple             | 5.77 us                                                     | 6.22 us: 1.08x slower                                                                |
| xml_etree_process          | 36.5 ms                                                     | 39.4 ms: 1.08x slower                                                                |
| logging_format             | 6.18 us                                                     | 6.70 us: 1.09x slower                                                                |
| create_gc_cycles           | 1.22 ms                                                     | 1.33 ms: 1.09x slower                                                                |
| gc_traversal               | 1.96 ms                                                     | 2.14 ms: 1.09x slower                                                                |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.11x slower                                                                |
| pprint_safe_repr           | 485 ms                                                      | 540 ms: 1.11x slower                                                                 |
| pickle_pure_python         | 186 us                                                      | 208 us: 1.12x slower                                                                 |
| pprint_pformat             | 977 ms                                                      | 1.10 sec: 1.12x slower                                                               |
| deltablue                  | 1.89 ms                                                     | 2.14 ms: 1.13x slower                                                                |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                                |
| raytrace                   | 153 ms                                                      | 179 ms: 1.17x slower                                                                 |
| django_template            | 20.3 ms                                                     | 24.3 ms: 1.20x slower                                                                |
| many_optionals             | 361 us                                                      | 433 us: 1.20x slower                                                                 |
| subparsers                 | 10.9 ms                                                     | 16.8 ms: 1.55x slower                                                                |
| logging_silent             | 54.6 ns                                                     | 310 ns: 5.68x slower                                                                 |
| coverage                   | 45.3 ms                                                     | 289 ms: 6.39x slower                                                                 |
| thrift                     | 8.47 ms                                                     | 94.3 ms: 11.14x slower                                                               |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                         |

Benchmark hidden because not significant (12): pylint, genshi_text, mako, chaos, html5lib, sqlite_synth, scimark_fft, sympy_integrate, typing_runtime_protocols, k_core, pycparser, genshi_xml
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250603-3.15.0a0-06c1680/bm-20250603-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.015x slower

# HPT report

- Reliability score: 70.55% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown