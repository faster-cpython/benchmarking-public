# Results vs. 3.13.0

- fork: python
- ref: 3.14
- machine: windows-amd64
- commit hash: 964c29d
- commit date: 2025-06-16
- overall geometric mean: 1.025x faster
- HPT reliability: 96.67%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 223 ms: 1.04x slower                                        |
| docutils       | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                      |
| html5lib       | 38.2 ms                                                     | 39.2 ms: 1.03x slower                                       |
| sphinx         | 617 ms                                                      | 649 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                       | 1.05x slower                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.32x faster                                        |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                        |
| async_tree_memoization     | 265 ms                                                      | 209 ms: 1.27x faster                                        |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                        |
| async_tree_io_tg           | 497 ms                                                      | 399 ms: 1.25x faster                                        |
| async_tree_none_tg         | 200 ms                                                      | 172 ms: 1.16x faster                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                        |
| async_generators           | 223 ms                                                      | 235 ms: 1.06x slower                                        |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.11x slower                                       |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.4 ms: 1.17x faster                                       |
| nbody          | 66.3 ms                                                     | 62.4 ms: 1.06x faster                                       |
| pidigits       | 146 ms                                                      | 149 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                       | 1.07x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.2 ms: 1.81x faster                                       |
| regex_effbot   | 1.69 ms                                                     | 1.56 ms: 1.09x faster                                       |
| regex_compile  | 80.7 ms                                                     | 79.3 ms: 1.02x faster                                       |
| regex_dna      | 115 ms                                                      | 118 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                       | 1.18x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 88.6 ms: 1.04x faster                                       |
| json_loads           | 15.1 us                                                     | 14.9 us: 1.01x faster                                       |
| json_dumps           | 6.19 ms                                                     | 6.27 ms: 1.01x slower                                       |
| unpickle_pure_python | 130 us                                                      | 132 us: 1.02x slower                                        |
| xml_etree_generate   | 53.5 ms                                                     | 55.8 ms: 1.04x slower                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.4 ms: 1.05x slower                                       |
| xml_etree_process    | 36.5 ms                                                     | 39.1 ms: 1.07x slower                                       |
| pickle_pure_python   | 186 us                                                      | 209 us: 1.12x slower                                        |
| Geometric mean       | (ref)                                                       | 1.03x slower                                                |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.5 ms: 1.08x slower                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                       |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                       |
| mako            | 6.56 ms                                                     | 6.76 ms: 1.03x slower                                       |
| django_template | 20.3 ms                                                     | 24.8 ms: 1.22x slower                                       |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d |
|----------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.4 ms: 2.33x faster                                       |
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                        |
| regex_v8                   | 23.8 ms                                                     | 13.2 ms: 1.81x faster                                       |
| mdp                        | 1.43 sec                                                    | 819 ms: 1.75x faster                                        |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.32x faster                                        |
| deepcopy                   | 223 us                                                      | 172 us: 1.30x faster                                        |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                        |
| async_tree_memoization     | 265 ms                                                      | 209 ms: 1.27x faster                                        |
| deepcopy_memo              | 23.1 us                                                     | 18.3 us: 1.26x faster                                       |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                        |
| async_tree_io_tg           | 497 ms                                                      | 399 ms: 1.25x faster                                        |
| float                      | 50.8 ms                                                     | 43.4 ms: 1.17x faster                                       |
| async_tree_none_tg         | 200 ms                                                      | 172 ms: 1.16x faster                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.78 us: 1.14x faster                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 344 ms: 1.11x faster                                        |
| go                         | 84.7 ms                                                     | 77.0 ms: 1.10x faster                                       |
| spectral_norm              | 63.4 ms                                                     | 57.8 ms: 1.10x faster                                       |
| regex_effbot               | 1.69 ms                                                     | 1.56 ms: 1.09x faster                                       |
| nbody                      | 66.3 ms                                                     | 62.4 ms: 1.06x faster                                       |
| telco                      | 4.85 ms                                                     | 4.60 ms: 1.05x faster                                       |
| json                       | 3.30 ms                                                     | 3.14 ms: 1.05x faster                                       |
| xml_etree_parse            | 92.2 ms                                                     | 88.6 ms: 1.04x faster                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.53 ms: 1.03x faster                                       |
| regex_compile              | 80.7 ms                                                     | 79.3 ms: 1.02x faster                                       |
| json_loads                 | 15.1 us                                                     | 14.9 us: 1.01x faster                                       |
| scimark_fft                | 175 ms                                                      | 173 ms: 1.01x faster                                        |
| genshi_text                | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                       |
| fannkuch                   | 252 ms                                                      | 253 ms: 1.00x slower                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.0 ms: 1.01x slower                                       |
| scimark_lu                 | 56.7 ms                                                     | 57.3 ms: 1.01x slower                                       |
| sqlite_synth               | 1.59 us                                                     | 1.61 us: 1.01x slower                                       |
| json_dumps                 | 6.19 ms                                                     | 6.27 ms: 1.01x slower                                       |
| pprint_safe_repr           | 485 ms                                                      | 492 ms: 1.02x slower                                        |
| pidigits                   | 146 ms                                                      | 149 ms: 1.02x slower                                        |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.02x slower                                       |
| k_core                     | 1.70 sec                                                    | 1.73 sec: 1.02x slower                                      |
| unpickle_pure_python       | 130 us                                                      | 132 us: 1.02x slower                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.93 sec: 1.02x slower                                      |
| typing_runtime_protocols   | 103 us                                                      | 105 us: 1.02x slower                                        |
| shortest_path              | 355 ms                                                      | 363 ms: 1.02x slower                                        |
| richards                   | 26.3 ms                                                     | 26.8 ms: 1.02x slower                                       |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.02x slower                                        |
| sympy_expand               | 286 ms                                                      | 292 ms: 1.02x slower                                        |
| sympy_str                  | 167 ms                                                      | 171 ms: 1.02x slower                                        |
| meteor_contest             | 72.0 ms                                                     | 73.7 ms: 1.02x slower                                       |
| pyflate                    | 283 ms                                                      | 290 ms: 1.02x slower                                        |
| pprint_pformat             | 977 ms                                                      | 1.00 sec: 1.02x slower                                      |
| html5lib                   | 38.2 ms                                                     | 39.2 ms: 1.03x slower                                       |
| mako                       | 6.56 ms                                                     | 6.76 ms: 1.03x slower                                       |
| richards_super             | 29.8 ms                                                     | 30.7 ms: 1.03x slower                                       |
| crypto_pyaes               | 45.6 ms                                                     | 47.3 ms: 1.04x slower                                       |
| 2to3                       | 215 ms                                                      | 223 ms: 1.04x slower                                        |
| sympy_sum                  | 85.2 ms                                                     | 88.5 ms: 1.04x slower                                       |
| dulwich_log                | 40.1 ms                                                     | 41.7 ms: 1.04x slower                                       |
| generators                 | 19.0 ms                                                     | 19.8 ms: 1.04x slower                                       |
| xml_etree_generate         | 53.5 ms                                                     | 55.8 ms: 1.04x slower                                       |
| connected_components       | 320 ms                                                      | 334 ms: 1.04x slower                                        |
| chaos                      | 37.9 ms                                                     | 39.6 ms: 1.05x slower                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.4 ms: 1.05x slower                                       |
| sphinx                     | 617 ms                                                      | 649 ms: 1.05x slower                                        |
| async_generators           | 223 ms                                                      | 235 ms: 1.06x slower                                        |
| hexiom                     | 3.84 ms                                                     | 4.07 ms: 1.06x slower                                       |
| xml_etree_process          | 36.5 ms                                                     | 39.1 ms: 1.07x slower                                       |
| comprehensions             | 10.4 us                                                     | 11.2 us: 1.08x slower                                       |
| coverage                   | 45.3 ms                                                     | 49.0 ms: 1.08x slower                                       |
| python_startup             | 24.4 ms                                                     | 26.5 ms: 1.08x slower                                       |
| nqueens                    | 56.1 ms                                                     | 60.9 ms: 1.09x slower                                       |
| docutils                   | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.33 ms: 1.09x slower                                       |
| gc_traversal               | 1.96 ms                                                     | 2.15 ms: 1.09x slower                                       |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.11x slower                                       |
| deltablue                  | 1.89 ms                                                     | 2.11 ms: 1.11x slower                                       |
| logging_format             | 6.18 us                                                     | 6.88 us: 1.11x slower                                       |
| logging_simple             | 5.77 us                                                     | 6.48 us: 1.12x slower                                       |
| pickle_pure_python         | 186 us                                                      | 209 us: 1.12x slower                                        |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                       |
| raytrace                   | 153 ms                                                      | 183 ms: 1.19x slower                                        |
| django_template            | 20.3 ms                                                     | 24.8 ms: 1.22x slower                                       |
| many_optionals             | 361 us                                                      | 448 us: 1.24x slower                                        |
| subparsers                 | 10.9 ms                                                     | 17.4 ms: 1.60x slower                                       |
| logging_silent             | 54.6 ns                                                     | 317 ns: 5.81x slower                                        |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                |

Benchmark hidden because not significant (5): pylint, scimark_sor, tomli_loads, genshi_xml, pycparser
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250616-3.14.0b2+-964c29d/bm-20250616-pythonperf1-amd64-python-3.14-3.14.0b2+-964c29d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.025x faster

# HPT report

- Reliability score: 96.67% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown