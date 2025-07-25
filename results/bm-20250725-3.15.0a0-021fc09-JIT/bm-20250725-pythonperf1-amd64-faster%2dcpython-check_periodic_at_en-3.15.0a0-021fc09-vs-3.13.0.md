# Results vs. 3.13.0

- fork: faster-cpython
- ref: check_periodic_at_en
- machine: windows-amd64
- commit hash: 021fc09
- commit date: 2025-07-25
- overall geometric mean: 1.066x faster
- HPT reliability: 70.41%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 222 ms: 1.03x slower                                                                 |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                               |
| html5lib       | 38.2 ms                                                     | 38.8 ms: 1.02x slower                                                                |
| sphinx         | 617 ms                                                      | 651 ms: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 177 ms: 1.70x faster                                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 215 ms: 1.31x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 393 ms: 1.31x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 385 ms: 1.29x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 214 ms: 1.24x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 180 ms: 1.22x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.15x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 337 ms: 1.13x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                                 |
| async_generators           | 223 ms                                                      | 252 ms: 1.13x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.18x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 55.8 ms: 1.19x faster                                                                |
| float          | 50.8 ms                                                     | 44.5 ms: 1.14x faster                                                                |
| pidigits       | 146 ms                                                      | 150 ms: 1.02x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                                |
| regex_effbot   | 1.69 ms                                                     | 1.61 ms: 1.06x faster                                                                |
| regex_compile  | 80.7 ms                                                     | 78.7 ms: 1.03x faster                                                                |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.11 sec: 1.23x faster                                                               |
| unpickle_pure_python | 130 us                                                      | 113 us: 1.15x faster                                                                 |
| xml_etree_generate   | 53.5 ms                                                     | 51.4 ms: 1.04x faster                                                                |
| json_loads           | 15.1 us                                                     | 14.8 us: 1.02x faster                                                                |
| xml_etree_parse      | 92.2 ms                                                     | 91.1 ms: 1.01x faster                                                                |
| json_dumps           | 6.19 ms                                                     | 6.30 ms: 1.02x slower                                                                |
| xml_etree_iterparse  | 60.5 ms                                                     | 66.7 ms: 1.10x slower                                                                |
| pickle_pure_python   | 186 us                                                      | 207 us: 1.11x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                         |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.7 ms: 1.09x slower                                                                |
| python_startup_no_site | 16.9 ms                                                     | 19.9 ms: 1.18x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.51 ms: 1.19x faster                                                                |
| genshi_text     | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                                |
| genshi_xml      | 33.9 ms                                                     | 35.1 ms: 1.04x slower                                                                |
| django_template | 20.3 ms                                                     | 24.1 ms: 1.19x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.02x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 490 us: 17.26x faster                                                                |
| pathlib                    | 75.3 ms                                                     | 33.2 ms: 2.27x faster                                                                |
| mdp                        | 1.43 sec                                                    | 823 ms: 1.74x faster                                                                 |
| asyncio_websockets         | 300 ms                                                      | 177 ms: 1.70x faster                                                                 |
| regex_v8                   | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                                |
| deepcopy                   | 223 us                                                      | 170 us: 1.31x faster                                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 215 ms: 1.31x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 393 ms: 1.31x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 385 ms: 1.29x faster                                                                 |
| deepcopy_memo              | 23.1 us                                                     | 18.0 us: 1.28x faster                                                                |
| async_tree_memoization     | 265 ms                                                      | 214 ms: 1.24x faster                                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.11 sec: 1.23x faster                                                               |
| async_tree_none            | 219 ms                                                      | 180 ms: 1.22x faster                                                                 |
| mako                       | 6.56 ms                                                     | 5.51 ms: 1.19x faster                                                                |
| nbody                      | 66.3 ms                                                     | 55.8 ms: 1.19x faster                                                                |
| fannkuch                   | 252 ms                                                      | 217 ms: 1.16x faster                                                                 |
| scimark_fft                | 175 ms                                                      | 151 ms: 1.16x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 173 ms: 1.15x faster                                                                 |
| unpickle_pure_python       | 130 us                                                      | 113 us: 1.15x faster                                                                 |
| float                      | 50.8 ms                                                     | 44.5 ms: 1.14x faster                                                                |
| bpe_tokeniser              | 2.87 sec                                                    | 2.53 sec: 1.14x faster                                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 337 ms: 1.13x faster                                                                 |
| telco                      | 4.85 ms                                                     | 4.30 ms: 1.13x faster                                                                |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                                 |
| pyflate                    | 283 ms                                                      | 257 ms: 1.10x faster                                                                 |
| json                       | 3.30 ms                                                     | 3.02 ms: 1.09x faster                                                                |
| deepcopy_reduce            | 2.02 us                                                     | 1.85 us: 1.09x faster                                                                |
| pprint_pformat             | 977 ms                                                      | 896 ms: 1.09x faster                                                                 |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.39 ms: 1.09x faster                                                                |
| go                         | 84.7 ms                                                     | 78.8 ms: 1.08x faster                                                                |
| pprint_safe_repr           | 485 ms                                                      | 454 ms: 1.07x faster                                                                 |
| k_core                     | 1.70 sec                                                    | 1.61 sec: 1.06x faster                                                               |
| regex_effbot               | 1.69 ms                                                     | 1.61 ms: 1.06x faster                                                                |
| xml_etree_generate         | 53.5 ms                                                     | 51.4 ms: 1.04x faster                                                                |
| regex_compile              | 80.7 ms                                                     | 78.7 ms: 1.03x faster                                                                |
| json_loads                 | 15.1 us                                                     | 14.8 us: 1.02x faster                                                                |
| xml_etree_parse            | 92.2 ms                                                     | 91.1 ms: 1.01x faster                                                                |
| shortest_path              | 355 ms                                                      | 358 ms: 1.01x slower                                                                 |
| comprehensions             | 10.4 us                                                     | 10.5 us: 1.01x slower                                                                |
| connected_components       | 320 ms                                                      | 325 ms: 1.02x slower                                                                 |
| html5lib                   | 38.2 ms                                                     | 38.8 ms: 1.02x slower                                                                |
| json_dumps                 | 6.19 ms                                                     | 6.30 ms: 1.02x slower                                                                |
| logging_silent             | 54.6 ns                                                     | 55.6 ns: 1.02x slower                                                                |
| crypto_pyaes               | 45.6 ms                                                     | 46.6 ms: 1.02x slower                                                                |
| pidigits                   | 146 ms                                                      | 150 ms: 1.02x slower                                                                 |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.8 ms: 1.03x slower                                                                |
| meteor_contest             | 72.0 ms                                                     | 74.0 ms: 1.03x slower                                                                |
| scimark_sor                | 76.2 ms                                                     | 78.5 ms: 1.03x slower                                                                |
| sympy_expand               | 286 ms                                                      | 294 ms: 1.03x slower                                                                 |
| sympy_sum                  | 85.2 ms                                                     | 87.7 ms: 1.03x slower                                                                |
| sympy_str                  | 167 ms                                                      | 172 ms: 1.03x slower                                                                 |
| genshi_text                | 15.2 ms                                                     | 15.7 ms: 1.03x slower                                                                |
| 2to3                       | 215 ms                                                      | 222 ms: 1.03x slower                                                                 |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.03x slower                                                                 |
| richards_super             | 29.8 ms                                                     | 30.8 ms: 1.03x slower                                                                |
| genshi_xml                 | 33.9 ms                                                     | 35.1 ms: 1.04x slower                                                                |
| sympy_integrate            | 12.3 ms                                                     | 12.8 ms: 1.04x slower                                                                |
| generators                 | 19.0 ms                                                     | 19.8 ms: 1.04x slower                                                                |
| richards                   | 26.3 ms                                                     | 27.5 ms: 1.05x slower                                                                |
| dulwich_log                | 40.1 ms                                                     | 42.0 ms: 1.05x slower                                                                |
| sphinx                     | 617 ms                                                      | 651 ms: 1.05x slower                                                                 |
| logging_simple             | 5.77 us                                                     | 6.17 us: 1.07x slower                                                                |
| scimark_lu                 | 56.7 ms                                                     | 60.6 ms: 1.07x slower                                                                |
| nqueens                    | 56.1 ms                                                     | 60.4 ms: 1.08x slower                                                                |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                               |
| hexiom                     | 3.84 ms                                                     | 4.16 ms: 1.08x slower                                                                |
| spectral_norm              | 63.4 ms                                                     | 68.8 ms: 1.08x slower                                                                |
| python_startup             | 24.4 ms                                                     | 26.7 ms: 1.09x slower                                                                |
| create_gc_cycles           | 1.22 ms                                                     | 1.34 ms: 1.10x slower                                                                |
| chaos                      | 37.9 ms                                                     | 41.6 ms: 1.10x slower                                                                |
| logging_format             | 6.18 us                                                     | 6.79 us: 1.10x slower                                                                |
| xml_etree_iterparse        | 60.5 ms                                                     | 66.7 ms: 1.10x slower                                                                |
| gc_traversal               | 1.96 ms                                                     | 2.17 ms: 1.11x slower                                                                |
| pickle_pure_python         | 186 us                                                      | 207 us: 1.11x slower                                                                 |
| coverage                   | 45.3 ms                                                     | 50.9 ms: 1.12x slower                                                                |
| async_generators           | 223 ms                                                      | 252 ms: 1.13x slower                                                                 |
| raytrace                   | 153 ms                                                      | 177 ms: 1.15x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 14.5 ms: 1.16x slower                                                                |
| python_startup_no_site     | 16.9 ms                                                     | 19.9 ms: 1.18x slower                                                                |
| django_template            | 20.3 ms                                                     | 24.1 ms: 1.19x slower                                                                |
| deltablue                  | 1.89 ms                                                     | 2.28 ms: 1.21x slower                                                                |
| many_optionals             | 361 us                                                      | 571 us: 1.58x slower                                                                 |
| subparsers                 | 10.9 ms                                                     | 29.8 ms: 2.75x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                         |

Benchmark hidden because not significant (5): pylint, xml_etree_process, sqlite_synth, pycparser, typing_runtime_protocols
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250725-3.15.0a0-021fc09-JIT/bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.066x faster

# HPT report

- Reliability score: 70.41% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown