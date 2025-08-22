# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: windows-amd64
- commit hash: efe4628
- commit date: 2025-08-22
- overall geometric mean: 1.085x faster
- HPT reliability: 86.00%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 220 ms: 1.02x slower                                                               |
| docutils       | 1.53 sec                                                    | 1.66 sec: 1.09x slower                                                             |
| html5lib       | 38.2 ms                                                     | 38.8 ms: 1.02x slower                                                              |
| sphinx         | 617 ms                                                      | 643 ms: 1.04x slower                                                               |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                               |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                               |
| async_tree_io              | 513 ms                                                      | 392 ms: 1.31x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                               |
| async_tree_io_tg           | 497 ms                                                      | 397 ms: 1.25x faster                                                               |
| async_tree_none            | 219 ms                                                      | 175 ms: 1.25x faster                                                               |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                               |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 332 ms: 1.14x faster                                                               |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.11x faster                                                               |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                               |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 43.6 ms: 1.52x faster                                                              |
| float          | 50.8 ms                                                     | 45.1 ms: 1.13x faster                                                              |
| pidigits       | 146 ms                                                      | 147 ms: 1.00x slower                                                               |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.9 ms: 1.72x faster                                                              |
| regex_effbot   | 1.69 ms                                                     | 1.52 ms: 1.12x faster                                                              |
| regex_compile  | 80.7 ms                                                     | 79.6 ms: 1.01x faster                                                              |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                               |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.12 sec: 1.22x faster                                                             |
| unpickle_pure_python | 130 us                                                      | 106 us: 1.22x faster                                                               |
| json_dumps           | 6.19 ms                                                     | 5.50 ms: 1.13x faster                                                              |
| json_loads           | 15.1 us                                                     | 14.2 us: 1.06x faster                                                              |
| xml_etree_generate   | 53.5 ms                                                     | 51.0 ms: 1.05x faster                                                              |
| xml_etree_parse      | 92.2 ms                                                     | 88.4 ms: 1.04x faster                                                              |
| xml_etree_process    | 36.5 ms                                                     | 35.5 ms: 1.03x faster                                                              |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.4 ms: 1.06x slower                                                              |
| pickle_pure_python   | 186 us                                                      | 206 us: 1.11x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.5 ms: 1.09x slower                                                              |
| python_startup_no_site | 16.9 ms                                                     | 19.2 ms: 1.13x slower                                                              |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.43 ms: 1.21x faster                                                              |
| genshi_text     | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                              |
| django_template | 20.3 ms                                                     | 24.3 ms: 1.20x slower                                                              |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 493 us: 17.16x faster                                                              |
| pathlib                    | 75.3 ms                                                     | 29.5 ms: 2.55x faster                                                              |
| asyncio_websockets         | 300 ms                                                      | 157 ms: 1.91x faster                                                               |
| mdp                        | 1.43 sec                                                    | 810 ms: 1.77x faster                                                               |
| regex_v8                   | 23.8 ms                                                     | 13.9 ms: 1.72x faster                                                              |
| nbody                      | 66.3 ms                                                     | 43.6 ms: 1.52x faster                                                              |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                               |
| async_tree_io              | 513 ms                                                      | 392 ms: 1.31x faster                                                               |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                               |
| deepcopy                   | 223 us                                                      | 175 us: 1.28x faster                                                               |
| async_tree_io_tg           | 497 ms                                                      | 397 ms: 1.25x faster                                                               |
| async_tree_none            | 219 ms                                                      | 175 ms: 1.25x faster                                                               |
| deepcopy_memo              | 23.1 us                                                     | 18.7 us: 1.23x faster                                                              |
| tomli_loads                | 1.37 sec                                                    | 1.12 sec: 1.22x faster                                                             |
| unpickle_pure_python       | 130 us                                                      | 106 us: 1.22x faster                                                               |
| fannkuch                   | 252 ms                                                      | 206 ms: 1.22x faster                                                               |
| mako                       | 6.56 ms                                                     | 5.43 ms: 1.21x faster                                                              |
| telco                      | 4.85 ms                                                     | 4.01 ms: 1.21x faster                                                              |
| scimark_fft                | 175 ms                                                      | 146 ms: 1.20x faster                                                               |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                               |
| pprint_pformat             | 977 ms                                                      | 845 ms: 1.16x faster                                                               |
| pprint_safe_repr           | 485 ms                                                      | 421 ms: 1.15x faster                                                               |
| bpe_tokeniser              | 2.87 sec                                                    | 2.51 sec: 1.15x faster                                                             |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 332 ms: 1.14x faster                                                               |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.28 ms: 1.14x faster                                                              |
| float                      | 50.8 ms                                                     | 45.1 ms: 1.13x faster                                                              |
| json_dumps                 | 6.19 ms                                                     | 5.50 ms: 1.13x faster                                                              |
| json                       | 3.30 ms                                                     | 2.94 ms: 1.12x faster                                                              |
| regex_effbot               | 1.69 ms                                                     | 1.52 ms: 1.12x faster                                                              |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.11x faster                                                               |
| pyflate                    | 283 ms                                                      | 260 ms: 1.09x faster                                                               |
| go                         | 84.7 ms                                                     | 78.4 ms: 1.08x faster                                                              |
| deepcopy_reduce            | 2.02 us                                                     | 1.89 us: 1.07x faster                                                              |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.06x faster                                                              |
| k_core                     | 1.70 sec                                                    | 1.60 sec: 1.06x faster                                                             |
| xml_etree_generate         | 53.5 ms                                                     | 51.0 ms: 1.05x faster                                                              |
| xml_etree_parse            | 92.2 ms                                                     | 88.4 ms: 1.04x faster                                                              |
| sqlite_synth               | 1.59 us                                                     | 1.54 us: 1.03x faster                                                              |
| xml_etree_process          | 36.5 ms                                                     | 35.5 ms: 1.03x faster                                                              |
| regex_compile              | 80.7 ms                                                     | 79.6 ms: 1.01x faster                                                              |
| pidigits                   | 146 ms                                                      | 147 ms: 1.00x slower                                                               |
| dulwich_log                | 40.1 ms                                                     | 40.6 ms: 1.01x slower                                                              |
| html5lib                   | 38.2 ms                                                     | 38.8 ms: 1.02x slower                                                              |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.4 ms: 1.02x slower                                                              |
| genshi_text                | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                              |
| meteor_contest             | 72.0 ms                                                     | 73.4 ms: 1.02x slower                                                              |
| 2to3                       | 215 ms                                                      | 220 ms: 1.02x slower                                                               |
| comprehensions             | 10.4 us                                                     | 10.6 us: 1.03x slower                                                              |
| typing_runtime_protocols   | 103 us                                                      | 106 us: 1.03x slower                                                               |
| sympy_str                  | 167 ms                                                      | 171 ms: 1.03x slower                                                               |
| sympy_sum                  | 85.2 ms                                                     | 87.9 ms: 1.03x slower                                                              |
| sympy_expand               | 286 ms                                                      | 296 ms: 1.04x slower                                                               |
| sympy_integrate            | 12.3 ms                                                     | 12.8 ms: 1.04x slower                                                              |
| logging_simple             | 5.77 us                                                     | 5.99 us: 1.04x slower                                                              |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                               |
| richards_super             | 29.8 ms                                                     | 30.9 ms: 1.04x slower                                                              |
| logging_silent             | 54.6 ns                                                     | 56.7 ns: 1.04x slower                                                              |
| scimark_sor                | 76.2 ms                                                     | 79.3 ms: 1.04x slower                                                              |
| sphinx                     | 617 ms                                                      | 643 ms: 1.04x slower                                                               |
| richards                   | 26.3 ms                                                     | 27.4 ms: 1.05x slower                                                              |
| nqueens                    | 56.1 ms                                                     | 58.9 ms: 1.05x slower                                                              |
| logging_format             | 6.18 us                                                     | 6.51 us: 1.05x slower                                                              |
| create_gc_cycles           | 1.22 ms                                                     | 1.30 ms: 1.06x slower                                                              |
| scimark_lu                 | 56.7 ms                                                     | 60.1 ms: 1.06x slower                                                              |
| hexiom                     | 3.84 ms                                                     | 4.07 ms: 1.06x slower                                                              |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.4 ms: 1.06x slower                                                              |
| spectral_norm              | 63.4 ms                                                     | 67.5 ms: 1.06x slower                                                              |
| generators                 | 19.0 ms                                                     | 20.2 ms: 1.07x slower                                                              |
| gc_traversal               | 1.96 ms                                                     | 2.11 ms: 1.07x slower                                                              |
| chaos                      | 37.9 ms                                                     | 40.8 ms: 1.08x slower                                                              |
| python_startup             | 24.4 ms                                                     | 26.5 ms: 1.09x slower                                                              |
| docutils                   | 1.53 sec                                                    | 1.66 sec: 1.09x slower                                                             |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                               |
| pickle_pure_python         | 186 us                                                      | 206 us: 1.11x slower                                                               |
| coverage                   | 45.3 ms                                                     | 50.5 ms: 1.11x slower                                                              |
| python_startup_no_site     | 16.9 ms                                                     | 19.2 ms: 1.13x slower                                                              |
| raytrace                   | 153 ms                                                      | 176 ms: 1.15x slower                                                               |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                              |
| deltablue                  | 1.89 ms                                                     | 2.25 ms: 1.19x slower                                                              |
| django_template            | 20.3 ms                                                     | 24.3 ms: 1.20x slower                                                              |
| many_optionals             | 361 us                                                      | 570 us: 1.58x slower                                                               |
| subparsers                 | 10.9 ms                                                     | 30.0 ms: 2.76x slower                                                              |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                                       |

Benchmark hidden because not significant (5): pylint, crypto_pyaes, shortest_path, connected_components, genshi_xml
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, pycparser, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250822-3.15.0a0-efe4628-JIT/bm-20250822-pythonperf1-amd64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.085x faster

# HPT report

- Reliability score: 86.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown