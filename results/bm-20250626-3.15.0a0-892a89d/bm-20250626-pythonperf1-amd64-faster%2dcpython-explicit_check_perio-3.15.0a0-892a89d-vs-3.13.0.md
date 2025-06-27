# Results vs. 3.13.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: windows-amd64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.059x faster
- HPT reliability: 97.33%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                                 |
| docutils       | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                               |
| sphinx         | 617 ms                                                      | 639 ms: 1.04x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                         |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 165 ms: 1.81x faster                                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.36x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 398 ms: 1.29x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 388 ms: 1.28x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.20x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 326 ms: 1.16x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 335 ms: 1.14x faster                                                                 |
| async_generators           | 223 ms                                                      | 226 ms: 1.02x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 14.7 ms: 1.18x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.4 ms: 1.17x faster                                                                |
| nbody          | 66.3 ms                                                     | 65.3 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.0 ms: 1.70x faster                                                                |
| regex_effbot   | 1.69 ms                                                     | 1.53 ms: 1.11x faster                                                                |
| regex_compile  | 80.7 ms                                                     | 79.8 ms: 1.01x faster                                                                |
| regex_dna      | 115 ms                                                      | 120 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.6 us: 1.04x faster                                                                |
| xml_etree_parse      | 92.2 ms                                                     | 89.4 ms: 1.03x faster                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                               |
| json_dumps           | 6.19 ms                                                     | 6.26 ms: 1.01x slower                                                                |
| unpickle_pure_python | 130 us                                                      | 132 us: 1.01x slower                                                                 |
| xml_etree_generate   | 53.5 ms                                                     | 56.1 ms: 1.05x slower                                                                |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.6 ms: 1.05x slower                                                                |
| xml_etree_process    | 36.5 ms                                                     | 38.7 ms: 1.06x slower                                                                |
| pickle_pure_python   | 186 us                                                      | 210 us: 1.13x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.3 ms: 1.08x slower                                                                |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 14.8 ms: 1.02x faster                                                                |
| mako            | 6.56 ms                                                     | 6.80 ms: 1.04x slower                                                                |
| django_template | 20.3 ms                                                     | 23.8 ms: 1.17x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                                         |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 504 us: 16.79x faster                                                                |
| pathlib                    | 75.3 ms                                                     | 32.1 ms: 2.35x faster                                                                |
| asyncio_websockets         | 300 ms                                                      | 165 ms: 1.81x faster                                                                 |
| mdp                        | 1.43 sec                                                    | 811 ms: 1.77x faster                                                                 |
| regex_v8                   | 23.8 ms                                                     | 14.0 ms: 1.70x faster                                                                |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.36x faster                                                                 |
| deepcopy                   | 223 us                                                      | 169 us: 1.32x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 398 ms: 1.29x faster                                                                 |
| deepcopy_memo              | 23.1 us                                                     | 17.9 us: 1.29x faster                                                                |
| async_tree_memoization     | 265 ms                                                      | 207 ms: 1.28x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 388 ms: 1.28x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 166 ms: 1.20x faster                                                                 |
| float                      | 50.8 ms                                                     | 43.4 ms: 1.17x faster                                                                |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 326 ms: 1.16x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 335 ms: 1.14x faster                                                                 |
| deepcopy_reduce            | 2.02 us                                                     | 1.82 us: 1.11x faster                                                                |
| regex_effbot               | 1.69 ms                                                     | 1.53 ms: 1.11x faster                                                                |
| go                         | 84.7 ms                                                     | 76.5 ms: 1.11x faster                                                                |
| telco                      | 4.85 ms                                                     | 4.53 ms: 1.07x faster                                                                |
| json                       | 3.30 ms                                                     | 3.11 ms: 1.06x faster                                                                |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.51 ms: 1.04x faster                                                                |
| json_loads                 | 15.1 us                                                     | 14.6 us: 1.04x faster                                                                |
| xml_etree_parse            | 92.2 ms                                                     | 89.4 ms: 1.03x faster                                                                |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.7 ms: 1.03x faster                                                                |
| genshi_text                | 15.2 ms                                                     | 14.8 ms: 1.02x faster                                                                |
| meteor_contest             | 72.0 ms                                                     | 70.7 ms: 1.02x faster                                                                |
| nbody                      | 66.3 ms                                                     | 65.3 ms: 1.01x faster                                                                |
| regex_compile              | 80.7 ms                                                     | 79.8 ms: 1.01x faster                                                                |
| typing_runtime_protocols   | 103 us                                                      | 102 us: 1.01x faster                                                                 |
| scimark_sor                | 76.2 ms                                                     | 76.7 ms: 1.01x slower                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                               |
| json_dumps                 | 6.19 ms                                                     | 6.26 ms: 1.01x slower                                                                |
| sqlite_synth               | 1.59 us                                                     | 1.60 us: 1.01x slower                                                                |
| pyflate                    | 283 ms                                                      | 287 ms: 1.01x slower                                                                 |
| unpickle_pure_python       | 130 us                                                      | 132 us: 1.01x slower                                                                 |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.01x slower                                                                |
| async_generators           | 223 ms                                                      | 226 ms: 1.02x slower                                                                 |
| generators                 | 19.0 ms                                                     | 19.3 ms: 1.02x slower                                                                |
| scimark_lu                 | 56.7 ms                                                     | 57.8 ms: 1.02x slower                                                                |
| sympy_expand               | 286 ms                                                      | 292 ms: 1.02x slower                                                                 |
| sympy_str                  | 167 ms                                                      | 171 ms: 1.02x slower                                                                 |
| fannkuch                   | 252 ms                                                      | 258 ms: 1.02x slower                                                                 |
| shortest_path              | 355 ms                                                      | 364 ms: 1.03x slower                                                                 |
| crypto_pyaes               | 45.6 ms                                                     | 46.8 ms: 1.03x slower                                                                |
| dulwich_log                | 40.1 ms                                                     | 41.3 ms: 1.03x slower                                                                |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                                 |
| bpe_tokeniser              | 2.87 sec                                                    | 2.97 sec: 1.03x slower                                                               |
| comprehensions             | 10.4 us                                                     | 10.7 us: 1.03x slower                                                                |
| sympy_sum                  | 85.2 ms                                                     | 88.1 ms: 1.03x slower                                                                |
| sphinx                     | 617 ms                                                      | 639 ms: 1.04x slower                                                                 |
| mako                       | 6.56 ms                                                     | 6.80 ms: 1.04x slower                                                                |
| richards                   | 26.3 ms                                                     | 27.3 ms: 1.04x slower                                                                |
| richards_super             | 29.8 ms                                                     | 31.0 ms: 1.04x slower                                                                |
| spectral_norm              | 63.4 ms                                                     | 66.2 ms: 1.04x slower                                                                |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.05x slower                                                                 |
| xml_etree_generate         | 53.5 ms                                                     | 56.1 ms: 1.05x slower                                                                |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.6 ms: 1.05x slower                                                                |
| connected_components       | 320 ms                                                      | 337 ms: 1.05x slower                                                                 |
| hexiom                     | 3.84 ms                                                     | 4.04 ms: 1.05x slower                                                                |
| scimark_fft                | 175 ms                                                      | 185 ms: 1.06x slower                                                                 |
| xml_etree_process          | 36.5 ms                                                     | 38.7 ms: 1.06x slower                                                                |
| docutils                   | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                               |
| create_gc_cycles           | 1.22 ms                                                     | 1.31 ms: 1.07x slower                                                                |
| python_startup             | 24.4 ms                                                     | 26.3 ms: 1.08x slower                                                                |
| logging_simple             | 5.77 us                                                     | 6.26 us: 1.08x slower                                                                |
| coverage                   | 45.3 ms                                                     | 49.3 ms: 1.09x slower                                                                |
| logging_format             | 6.18 us                                                     | 6.72 us: 1.09x slower                                                                |
| chaos                      | 37.9 ms                                                     | 41.3 ms: 1.09x slower                                                                |
| gc_traversal               | 1.96 ms                                                     | 2.14 ms: 1.09x slower                                                                |
| nqueens                    | 56.1 ms                                                     | 61.3 ms: 1.09x slower                                                                |
| pprint_safe_repr           | 485 ms                                                      | 532 ms: 1.10x slower                                                                 |
| pprint_pformat             | 977 ms                                                      | 1.09 sec: 1.12x slower                                                               |
| pickle_pure_python         | 186 us                                                      | 210 us: 1.13x slower                                                                 |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                                |
| deltablue                  | 1.89 ms                                                     | 2.19 ms: 1.16x slower                                                                |
| raytrace                   | 153 ms                                                      | 178 ms: 1.16x slower                                                                 |
| django_template            | 20.3 ms                                                     | 23.8 ms: 1.17x slower                                                                |
| coroutines                 | 12.5 ms                                                     | 14.7 ms: 1.18x slower                                                                |
| many_optionals             | 361 us                                                      | 437 us: 1.21x slower                                                                 |
| subparsers                 | 10.9 ms                                                     | 17.2 ms: 1.59x slower                                                                |
| logging_silent             | 54.6 ns                                                     | 319 ns: 5.84x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                                         |

Benchmark hidden because not significant (6): pylint, pidigits, genshi_xml, k_core, html5lib, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250626-3.15.0a0-892a89d/bm-20250626-pythonperf1-amd64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.059x faster

# HPT report

- Reliability score: 97.33% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown