# Results vs. 3.13.0

- fork: faster-cpython
- ref: immortal_stickiness
- machine: windows-amd64
- commit hash: 490cf8d
- commit date: 2025-03-12
- overall geometric mean: 1.010x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 226 ms: 1.05x slower                                                                 |
| docutils       | 1.53 sec                                                    | 1.68 sec: 1.09x slower                                                               |
| html5lib       | 38.2 ms                                                     | 40.9 ms: 1.07x slower                                                                |
| sphinx         | 617 ms                                                      | 655 ms: 1.06x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 217 ms: 1.29x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 220 ms: 1.20x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 426 ms: 1.20x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 420 ms: 1.18x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 189 ms: 1.16x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 177 ms: 1.13x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 343 ms: 1.11x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                                 |
| async_generators           | 223 ms                                                      | 228 ms: 1.02x slower                                                                 |
| asyncio_websockets         | 300 ms                                                      | 313 ms: 1.04x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.3 ms: 1.12x faster                                                                |
| pidigits       | 146 ms                                                      | 152 ms: 1.04x slower                                                                 |
| nbody          | 66.3 ms                                                     | 69.2 ms: 1.04x slower                                                                |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.1 ms: 1.82x faster                                                                |
| regex_effbot   | 1.69 ms                                                     | 1.40 ms: 1.21x faster                                                                |
| regex_dna      | 115 ms                                                      | 112 ms: 1.03x faster                                                                 |
| regex_compile  | 80.7 ms                                                     | 85.9 ms: 1.06x slower                                                                |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.7 us: 1.03x faster                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                               |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.9 ms: 1.07x slower                                                                |
| xml_etree_generate   | 53.5 ms                                                     | 58.9 ms: 1.10x slower                                                                |
| json_dumps           | 6.19 ms                                                     | 6.90 ms: 1.12x slower                                                                |
| unpickle_pure_python | 130 us                                                      | 146 us: 1.12x slower                                                                 |
| xml_etree_process    | 36.5 ms                                                     | 42.1 ms: 1.15x slower                                                                |
| pickle_pure_python   | 186 us                                                      | 224 us: 1.20x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                                         |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.3 ms: 1.08x slower                                                                |
| python_startup_no_site | 16.9 ms                                                     | 20.4 ms: 1.21x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.83 ms: 1.04x slower                                                                |
| genshi_xml      | 33.9 ms                                                     | 38.3 ms: 1.13x slower                                                                |
| genshi_text     | 15.2 ms                                                     | 17.3 ms: 1.14x slower                                                                |
| django_template | 20.3 ms                                                     | 26.0 ms: 1.28x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.14x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 512 us: 16.53x faster                                                                |
| pathlib                    | 75.3 ms                                                     | 32.0 ms: 2.35x faster                                                                |
| regex_v8                   | 23.8 ms                                                     | 13.1 ms: 1.82x faster                                                                |
| async_tree_memoization_tg  | 281 ms                                                      | 217 ms: 1.29x faster                                                                 |
| deepcopy                   | 223 us                                                      | 181 us: 1.23x faster                                                                 |
| regex_effbot               | 1.69 ms                                                     | 1.40 ms: 1.21x faster                                                                |
| async_tree_memoization     | 265 ms                                                      | 220 ms: 1.20x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 426 ms: 1.20x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 420 ms: 1.18x faster                                                                 |
| deepcopy_memo              | 23.1 us                                                     | 19.8 us: 1.16x faster                                                                |
| async_tree_none            | 219 ms                                                      | 189 ms: 1.16x faster                                                                 |
| spectral_norm              | 63.4 ms                                                     | 56.0 ms: 1.13x faster                                                                |
| async_tree_none_tg         | 200 ms                                                      | 177 ms: 1.13x faster                                                                 |
| float                      | 50.8 ms                                                     | 45.3 ms: 1.12x faster                                                                |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 343 ms: 1.11x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 347 ms: 1.10x faster                                                                 |
| json                       | 3.30 ms                                                     | 3.06 ms: 1.08x faster                                                                |
| deepcopy_reduce            | 2.02 us                                                     | 1.91 us: 1.06x faster                                                                |
| json_loads                 | 15.1 us                                                     | 14.7 us: 1.03x faster                                                                |
| regex_dna                  | 115 ms                                                      | 112 ms: 1.03x faster                                                                 |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.55 ms: 1.02x faster                                                                |
| create_gc_cycles           | 1.22 ms                                                     | 1.24 ms: 1.01x slower                                                                |
| scimark_fft                | 175 ms                                                      | 178 ms: 1.02x slower                                                                 |
| scimark_sor                | 76.2 ms                                                     | 77.7 ms: 1.02x slower                                                                |
| k_core                     | 1.70 sec                                                    | 1.73 sec: 1.02x slower                                                               |
| async_generators           | 223 ms                                                      | 228 ms: 1.02x slower                                                                 |
| generators                 | 19.0 ms                                                     | 19.4 ms: 1.02x slower                                                                |
| bpe_tokeniser              | 2.87 sec                                                    | 2.96 sec: 1.03x slower                                                               |
| gc_traversal               | 1.96 ms                                                     | 2.03 ms: 1.03x slower                                                                |
| shortest_path              | 355 ms                                                      | 367 ms: 1.03x slower                                                                 |
| pidigits                   | 146 ms                                                      | 152 ms: 1.04x slower                                                                 |
| connected_components       | 320 ms                                                      | 332 ms: 1.04x slower                                                                 |
| mako                       | 6.56 ms                                                     | 6.83 ms: 1.04x slower                                                                |
| sympy_sum                  | 85.2 ms                                                     | 88.7 ms: 1.04x slower                                                                |
| asyncio_websockets         | 300 ms                                                      | 313 ms: 1.04x slower                                                                 |
| nbody                      | 66.3 ms                                                     | 69.2 ms: 1.04x slower                                                                |
| sympy_str                  | 167 ms                                                      | 175 ms: 1.05x slower                                                                 |
| sympy_expand               | 286 ms                                                      | 299 ms: 1.05x slower                                                                 |
| bench_mp_pool              | 84.2 ms                                                     | 88.3 ms: 1.05x slower                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                               |
| 2to3                       | 215 ms                                                      | 226 ms: 1.05x slower                                                                 |
| go                         | 84.7 ms                                                     | 89.1 ms: 1.05x slower                                                                |
| dulwich_log                | 40.1 ms                                                     | 42.6 ms: 1.06x slower                                                                |
| sphinx                     | 617 ms                                                      | 655 ms: 1.06x slower                                                                 |
| scimark_monte_carlo        | 40.7 ms                                                     | 43.3 ms: 1.06x slower                                                                |
| regex_compile              | 80.7 ms                                                     | 85.9 ms: 1.06x slower                                                                |
| scimark_lu                 | 56.7 ms                                                     | 60.4 ms: 1.06x slower                                                                |
| pycparser                  | 695 ms                                                      | 742 ms: 1.07x slower                                                                 |
| bench_thread_pool          | 810 us                                                      | 866 us: 1.07x slower                                                                 |
| pprint_safe_repr           | 485 ms                                                      | 518 ms: 1.07x slower                                                                 |
| html5lib                   | 38.2 ms                                                     | 40.9 ms: 1.07x slower                                                                |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.9 ms: 1.07x slower                                                                |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                                |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                                |
| logging_silent             | 54.6 ns                                                     | 58.8 ns: 1.08x slower                                                                |
| python_startup             | 24.4 ms                                                     | 26.3 ms: 1.08x slower                                                                |
| pprint_pformat             | 977 ms                                                      | 1.06 sec: 1.08x slower                                                               |
| meteor_contest             | 72.0 ms                                                     | 78.3 ms: 1.09x slower                                                                |
| coverage                   | 45.3 ms                                                     | 49.5 ms: 1.09x slower                                                                |
| docutils                   | 1.53 sec                                                    | 1.68 sec: 1.09x slower                                                               |
| typing_runtime_protocols   | 103 us                                                      | 113 us: 1.09x slower                                                                 |
| pyflate                    | 283 ms                                                      | 310 ms: 1.10x slower                                                                 |
| fannkuch                   | 252 ms                                                      | 276 ms: 1.10x slower                                                                 |
| crypto_pyaes               | 45.6 ms                                                     | 50.2 ms: 1.10x slower                                                                |
| richards_super             | 29.8 ms                                                     | 32.8 ms: 1.10x slower                                                                |
| richards                   | 26.3 ms                                                     | 28.9 ms: 1.10x slower                                                                |
| xml_etree_generate         | 53.5 ms                                                     | 58.9 ms: 1.10x slower                                                                |
| json_dumps                 | 6.19 ms                                                     | 6.90 ms: 1.12x slower                                                                |
| mdp                        | 1.43 sec                                                    | 1.60 sec: 1.12x slower                                                               |
| logging_simple             | 5.77 us                                                     | 6.47 us: 1.12x slower                                                                |
| hexiom                     | 3.84 ms                                                     | 4.31 ms: 1.12x slower                                                                |
| unpickle_pure_python       | 130 us                                                      | 146 us: 1.12x slower                                                                 |
| logging_format             | 6.18 us                                                     | 6.97 us: 1.13x slower                                                                |
| genshi_xml                 | 33.9 ms                                                     | 38.3 ms: 1.13x slower                                                                |
| genshi_text                | 15.2 ms                                                     | 17.3 ms: 1.14x slower                                                                |
| comprehensions             | 10.4 us                                                     | 11.8 us: 1.14x slower                                                                |
| nqueens                    | 56.1 ms                                                     | 63.9 ms: 1.14x slower                                                                |
| chaos                      | 37.9 ms                                                     | 43.4 ms: 1.15x slower                                                                |
| xml_etree_process          | 36.5 ms                                                     | 42.1 ms: 1.15x slower                                                                |
| deltablue                  | 1.89 ms                                                     | 2.24 ms: 1.18x slower                                                                |
| pickle_pure_python         | 186 us                                                      | 224 us: 1.20x slower                                                                 |
| many_optionals             | 361 us                                                      | 435 us: 1.20x slower                                                                 |
| python_startup_no_site     | 16.9 ms                                                     | 20.4 ms: 1.21x slower                                                                |
| django_template            | 20.3 ms                                                     | 26.0 ms: 1.28x slower                                                                |
| raytrace                   | 153 ms                                                      | 200 ms: 1.30x slower                                                                 |
| subparsers                 | 10.9 ms                                                     | 16.5 ms: 1.52x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                         |

Benchmark hidden because not significant (4): pylint, xml_etree_parse, sqlite_synth, telco
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250312-3.14.0a5+-490cf8d/bm-20250312-pythonperf1-amd64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown