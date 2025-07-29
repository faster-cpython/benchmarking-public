# Results vs. 3.13.0

- fork: faster-cpython
- ref: check_periodic_at_en
- machine: windows-amd64
- commit hash: 021fc09
- commit date: 2025-07-25
- overall geometric mean: 1.050x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 250 ms: 1.16x slower                                                                 |
| docutils       | 1.53 sec                                                    | 1.77 sec: 1.16x slower                                                               |
| html5lib       | 38.2 ms                                                     | 41.5 ms: 1.09x slower                                                                |
| sphinx         | 617 ms                                                      | 668 ms: 1.08x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.12x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 168 ms: 1.79x faster                                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 221 ms: 1.27x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 223 ms: 1.19x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 438 ms: 1.17x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 426 ms: 1.17x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 192 ms: 1.14x faster                                                                 |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 350 ms: 1.09x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 185 ms: 1.08x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 355 ms: 1.08x faster                                                                 |
| async_generators           | 223 ms                                                      | 259 ms: 1.16x slower                                                                 |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.18x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.13x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.7 ms: 1.11x faster                                                                |
| pidigits       | 146 ms                                                      | 150 ms: 1.03x slower                                                                 |
| nbody          | 66.3 ms                                                     | 87.0 ms: 1.31x slower                                                                |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.67x faster                                                                |
| regex_effbot   | 1.69 ms                                                     | 1.53 ms: 1.11x faster                                                                |
| regex_dna      | 115 ms                                                      | 125 ms: 1.09x slower                                                                 |
| regex_compile  | 80.7 ms                                                     | 95.1 ms: 1.18x slower                                                                |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.5 us: 1.04x faster                                                                |
| xml_etree_parse      | 92.2 ms                                                     | 91.4 ms: 1.01x faster                                                                |
| json_dumps           | 6.19 ms                                                     | 6.30 ms: 1.02x slower                                                                |
| xml_etree_iterparse  | 60.5 ms                                                     | 70.5 ms: 1.17x slower                                                                |
| xml_etree_generate   | 53.5 ms                                                     | 65.1 ms: 1.22x slower                                                                |
| tomli_loads          | 1.37 sec                                                    | 1.70 sec: 1.24x slower                                                               |
| xml_etree_process    | 36.5 ms                                                     | 45.6 ms: 1.25x slower                                                                |
| pickle_pure_python   | 186 us                                                      | 249 us: 1.34x slower                                                                 |
| unpickle_pure_python | 130 us                                                      | 209 us: 1.61x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.18x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 27.4 ms: 1.12x slower                                                                |
| python_startup_no_site | 16.9 ms                                                     | 20.2 ms: 1.20x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 16.3 ms: 1.07x slower                                                                |
| genshi_xml      | 33.9 ms                                                     | 37.6 ms: 1.11x slower                                                                |
| django_template | 20.3 ms                                                     | 26.1 ms: 1.29x slower                                                                |
| mako            | 6.56 ms                                                     | 8.86 ms: 1.35x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.20x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 508 us: 16.66x faster                                                                |
| pathlib                    | 75.3 ms                                                     | 33.4 ms: 2.25x faster                                                                |
| asyncio_websockets         | 300 ms                                                      | 168 ms: 1.79x faster                                                                 |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.67x faster                                                                |
| mdp                        | 1.43 sec                                                    | 862 ms: 1.66x faster                                                                 |
| async_tree_memoization_tg  | 281 ms                                                      | 221 ms: 1.27x faster                                                                 |
| deepcopy_memo              | 23.1 us                                                     | 18.9 us: 1.22x faster                                                                |
| deepcopy                   | 223 us                                                      | 183 us: 1.22x faster                                                                 |
| async_tree_memoization     | 265 ms                                                      | 223 ms: 1.19x faster                                                                 |
| async_tree_io              | 513 ms                                                      | 438 ms: 1.17x faster                                                                 |
| async_tree_io_tg           | 497 ms                                                      | 426 ms: 1.17x faster                                                                 |
| async_tree_none            | 219 ms                                                      | 192 ms: 1.14x faster                                                                 |
| float                      | 50.8 ms                                                     | 45.7 ms: 1.11x faster                                                                |
| regex_effbot               | 1.69 ms                                                     | 1.53 ms: 1.11x faster                                                                |
| json                       | 3.30 ms                                                     | 3.02 ms: 1.09x faster                                                                |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 350 ms: 1.09x faster                                                                 |
| async_tree_none_tg         | 200 ms                                                      | 185 ms: 1.08x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 355 ms: 1.08x faster                                                                 |
| deepcopy_reduce            | 2.02 us                                                     | 1.89 us: 1.07x faster                                                                |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                                                |
| go                         | 84.7 ms                                                     | 83.6 ms: 1.01x faster                                                                |
| xml_etree_parse            | 92.2 ms                                                     | 91.4 ms: 1.01x faster                                                                |
| sqlite_synth               | 1.59 us                                                     | 1.60 us: 1.01x slower                                                                |
| json_dumps                 | 6.19 ms                                                     | 6.30 ms: 1.02x slower                                                                |
| pidigits                   | 146 ms                                                      | 150 ms: 1.03x slower                                                                 |
| telco                      | 4.85 ms                                                     | 5.01 ms: 1.03x slower                                                                |
| spectral_norm              | 63.4 ms                                                     | 65.6 ms: 1.03x slower                                                                |
| scimark_sor                | 76.2 ms                                                     | 79.1 ms: 1.04x slower                                                                |
| scimark_monte_carlo        | 40.7 ms                                                     | 42.6 ms: 1.05x slower                                                                |
| k_core                     | 1.70 sec                                                    | 1.79 sec: 1.06x slower                                                               |
| generators                 | 19.0 ms                                                     | 20.3 ms: 1.07x slower                                                                |
| logging_silent             | 54.6 ns                                                     | 58.6 ns: 1.07x slower                                                                |
| genshi_text                | 15.2 ms                                                     | 16.3 ms: 1.07x slower                                                                |
| scimark_lu                 | 56.7 ms                                                     | 61.3 ms: 1.08x slower                                                                |
| sphinx                     | 617 ms                                                      | 668 ms: 1.08x slower                                                                 |
| regex_dna                  | 115 ms                                                      | 125 ms: 1.09x slower                                                                 |
| html5lib                   | 38.2 ms                                                     | 41.5 ms: 1.09x slower                                                                |
| richards                   | 26.3 ms                                                     | 28.7 ms: 1.09x slower                                                                |
| richards_super             | 29.8 ms                                                     | 32.5 ms: 1.09x slower                                                                |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.10x slower                                                                |
| sympy_str                  | 167 ms                                                      | 185 ms: 1.11x slower                                                                 |
| sympy_sum                  | 85.2 ms                                                     | 94.4 ms: 1.11x slower                                                                |
| genshi_xml                 | 33.9 ms                                                     | 37.6 ms: 1.11x slower                                                                |
| gc_traversal               | 1.96 ms                                                     | 2.19 ms: 1.11x slower                                                                |
| dulwich_log                | 40.1 ms                                                     | 44.7 ms: 1.11x slower                                                                |
| logging_simple             | 5.77 us                                                     | 6.44 us: 1.11x slower                                                                |
| create_gc_cycles           | 1.22 ms                                                     | 1.37 ms: 1.12x slower                                                                |
| python_startup             | 24.4 ms                                                     | 27.4 ms: 1.12x slower                                                                |
| logging_format             | 6.18 us                                                     | 7.02 us: 1.14x slower                                                                |
| sympy_expand               | 286 ms                                                      | 326 ms: 1.14x slower                                                                 |
| shortest_path              | 355 ms                                                      | 407 ms: 1.15x slower                                                                 |
| docutils                   | 1.53 sec                                                    | 1.77 sec: 1.16x slower                                                               |
| chaos                      | 37.9 ms                                                     | 43.9 ms: 1.16x slower                                                                |
| 2to3                       | 215 ms                                                      | 250 ms: 1.16x slower                                                                 |
| async_generators           | 223 ms                                                      | 259 ms: 1.16x slower                                                                 |
| xml_etree_iterparse        | 60.5 ms                                                     | 70.5 ms: 1.17x slower                                                                |
| coverage                   | 45.3 ms                                                     | 53.0 ms: 1.17x slower                                                                |
| regex_compile              | 80.7 ms                                                     | 95.1 ms: 1.18x slower                                                                |
| coroutines                 | 12.5 ms                                                     | 14.8 ms: 1.18x slower                                                                |
| pyflate                    | 283 ms                                                      | 338 ms: 1.19x slower                                                                 |
| python_startup_no_site     | 16.9 ms                                                     | 20.2 ms: 1.20x slower                                                                |
| hexiom                     | 3.84 ms                                                     | 4.60 ms: 1.20x slower                                                                |
| meteor_contest             | 72.0 ms                                                     | 86.2 ms: 1.20x slower                                                                |
| typing_runtime_protocols   | 103 us                                                      | 124 us: 1.20x slower                                                                 |
| connected_components       | 320 ms                                                      | 389 ms: 1.22x slower                                                                 |
| xml_etree_generate         | 53.5 ms                                                     | 65.1 ms: 1.22x slower                                                                |
| pycparser                  | 695 ms                                                      | 853 ms: 1.23x slower                                                                 |
| tomli_loads                | 1.37 sec                                                    | 1.70 sec: 1.24x slower                                                               |
| xml_etree_process          | 36.5 ms                                                     | 45.6 ms: 1.25x slower                                                                |
| deltablue                  | 1.89 ms                                                     | 2.37 ms: 1.25x slower                                                                |
| bpe_tokeniser              | 2.87 sec                                                    | 3.60 sec: 1.25x slower                                                               |
| nqueens                    | 56.1 ms                                                     | 70.6 ms: 1.26x slower                                                                |
| raytrace                   | 153 ms                                                      | 193 ms: 1.26x slower                                                                 |
| scimark_fft                | 175 ms                                                      | 221 ms: 1.26x slower                                                                 |
| pprint_pformat             | 977 ms                                                      | 1.25 sec: 1.28x slower                                                               |
| django_template            | 20.3 ms                                                     | 26.1 ms: 1.29x slower                                                                |
| pprint_safe_repr           | 485 ms                                                      | 632 ms: 1.30x slower                                                                 |
| nbody                      | 66.3 ms                                                     | 87.0 ms: 1.31x slower                                                                |
| pickle_pure_python         | 186 us                                                      | 249 us: 1.34x slower                                                                 |
| mako                       | 6.56 ms                                                     | 8.86 ms: 1.35x slower                                                                |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 3.58 ms: 1.37x slower                                                                |
| fannkuch                   | 252 ms                                                      | 354 ms: 1.41x slower                                                                 |
| crypto_pyaes               | 45.6 ms                                                     | 64.6 ms: 1.42x slower                                                                |
| comprehensions             | 10.4 us                                                     | 16.6 us: 1.60x slower                                                                |
| unpickle_pure_python       | 130 us                                                      | 209 us: 1.61x slower                                                                 |
| many_optionals             | 361 us                                                      | 615 us: 1.70x slower                                                                 |
| subparsers                 | 10.9 ms                                                     | 32.2 ms: 2.97x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.06x slower                                                                         |

Benchmark hidden because not significant (1): pylint
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250725-3.15.0a0-021fc09-PYTHON_UOPS/bm-20250725-pythonperf1-amd64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.050x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown