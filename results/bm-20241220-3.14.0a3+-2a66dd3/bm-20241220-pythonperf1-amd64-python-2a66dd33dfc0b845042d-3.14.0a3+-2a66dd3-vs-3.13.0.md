# Results vs. 3.13.0

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: windows-amd64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.023x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 226 ms: 1.05x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.68 sec: 1.10x slower                                                      |
| html5lib       | 38.2 ms                                                     | 40.9 ms: 1.07x slower                                                       |
| sphinx         | 617 ms                                                      | 655 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                                        |
| async_tree_io              | 513 ms                                                      | 412 ms: 1.24x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 409 ms: 1.21x faster                                                        |
| async_tree_none            | 219 ms                                                      | 186 ms: 1.18x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 229 ms: 1.16x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 175 ms: 1.14x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 355 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 354 ms: 1.07x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 308 ms: 1.03x slower                                                        |
| async_generators           | 223 ms                                                      | 235 ms: 1.05x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                      | 147 ms: 1.01x slower                                                        |
| float          | 50.8 ms                                                     | 55.3 ms: 1.09x slower                                                       |
| nbody          | 66.3 ms                                                     | 82.0 ms: 1.24x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.01x slower                                                        |
| regex_compile  | 80.7 ms                                                     | 88.7 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 88.3 ms: 1.04x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.7 us: 1.03x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.1 ms: 1.04x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.46 sec: 1.07x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 6.74 ms: 1.09x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 58.3 ms: 1.09x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 40.4 ms: 1.11x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 151 us: 1.16x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 228 us: 1.23x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 23.4 ms: 1.04x faster                                                       |
| python_startup_no_site | 16.9 ms                                                     | 17.4 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 35.0 ms: 1.03x slower                                                       |
| mako            | 6.56 ms                                                     | 6.78 ms: 1.03x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 16.7 ms: 1.10x slower                                                       |
| django_template | 20.3 ms                                                     | 25.6 ms: 1.26x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 525 us: 16.12x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 218 ms: 1.29x faster                                                        |
| async_tree_io              | 513 ms                                                      | 412 ms: 1.24x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 409 ms: 1.21x faster                                                        |
| deepcopy                   | 223 us                                                      | 187 us: 1.20x faster                                                        |
| async_tree_none            | 219 ms                                                      | 186 ms: 1.18x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 229 ms: 1.16x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 175 ms: 1.14x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 20.8 us: 1.11x faster                                                       |
| json                       | 3.30 ms                                                     | 3.00 ms: 1.10x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 355 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 354 ms: 1.07x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.91 us: 1.06x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 88.3 ms: 1.04x faster                                                       |
| python_startup             | 24.4 ms                                                     | 23.4 ms: 1.04x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.7 us: 1.03x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 82.2 ms: 1.02x faster                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                                       |
| shortest_path              | 355 ms                                                      | 351 ms: 1.01x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 62.9 ms: 1.01x faster                                                       |
| pidigits                   | 146 ms                                                      | 147 ms: 1.01x slower                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.60 us: 1.01x slower                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.62 ms: 1.01x slower                                                       |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.01x slower                                                        |
| asyncio_websockets         | 300 ms                                                      | 308 ms: 1.03x slower                                                        |
| python_startup_no_site     | 16.9 ms                                                     | 17.4 ms: 1.03x slower                                                       |
| coverage                   | 45.3 ms                                                     | 46.6 ms: 1.03x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 35.0 ms: 1.03x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.78 ms: 1.03x slower                                                       |
| go                         | 84.7 ms                                                     | 88.3 ms: 1.04x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.1 ms: 1.04x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.00 sec: 1.04x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 42.1 ms: 1.05x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 47.9 ms: 1.05x slower                                                       |
| 2to3                       | 215 ms                                                      | 226 ms: 1.05x slower                                                        |
| async_generators           | 223 ms                                                      | 235 ms: 1.05x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 90.2 ms: 1.06x slower                                                       |
| sphinx                     | 617 ms                                                      | 655 ms: 1.06x slower                                                        |
| mdp                        | 1.43 sec                                                    | 1.52 sec: 1.06x slower                                                      |
| sympy_str                  | 167 ms                                                      | 178 ms: 1.07x slower                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.46 sec: 1.07x slower                                                      |
| sympy_expand               | 286 ms                                                      | 305 ms: 1.07x slower                                                        |
| html5lib                   | 38.2 ms                                                     | 40.9 ms: 1.07x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 77.8 ms: 1.08x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| generators                 | 19.0 ms                                                     | 20.6 ms: 1.09x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.74 ms: 1.09x slower                                                       |
| float                      | 50.8 ms                                                     | 55.3 ms: 1.09x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 58.3 ms: 1.09x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 113 us: 1.09x slower                                                        |
| docutils                   | 1.53 sec                                                    | 1.68 sec: 1.10x slower                                                      |
| regex_compile              | 80.7 ms                                                     | 88.7 ms: 1.10x slower                                                       |
| pycparser                  | 695 ms                                                      | 764 ms: 1.10x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 16.7 ms: 1.10x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.6 ms: 1.10x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.81 us: 1.10x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 62.6 ms: 1.10x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 40.4 ms: 1.11x slower                                                       |
| scimark_fft                | 175 ms                                                      | 194 ms: 1.11x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.42 us: 1.11x slower                                                       |
| pyflate                    | 283 ms                                                      | 316 ms: 1.12x slower                                                        |
| sqlglot_optimize           | 32.5 ms                                                     | 36.4 ms: 1.12x slower                                                       |
| fannkuch                   | 252 ms                                                      | 282 ms: 1.12x slower                                                        |
| pprint_pformat             | 977 ms                                                      | 1.11 sec: 1.14x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 62.3 ns: 1.14x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 558 ms: 1.15x slower                                                        |
| chaos                      | 37.9 ms                                                     | 43.6 ms: 1.15x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 151 us: 1.16x slower                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 47.6 ms: 1.17x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 200 ms: 1.17x slower                                                        |
| sqlglot_transpile          | 953 us                                                      | 1.12 ms: 1.17x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 89.5 ms: 1.17x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 903 us: 1.18x slower                                                        |
| nqueens                    | 56.1 ms                                                     | 66.3 ms: 1.18x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.55 ms: 1.19x slower                                                       |
| richards                   | 26.3 ms                                                     | 31.2 ms: 1.19x slower                                                       |
| comprehensions             | 10.4 us                                                     | 12.4 us: 1.19x slower                                                       |
| richards_super             | 29.8 ms                                                     | 35.6 ms: 1.19x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.29 ms: 1.21x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 228 us: 1.23x slower                                                        |
| many_optionals             | 361 us                                                      | 445 us: 1.23x slower                                                        |
| nbody                      | 66.3 ms                                                     | 82.0 ms: 1.24x slower                                                       |
| django_template            | 20.3 ms                                                     | 25.6 ms: 1.26x slower                                                       |
| raytrace                   | 153 ms                                                      | 196 ms: 1.28x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.3 ms: 1.50x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (8): regex_v8, pylint, telco, pathlib, k_core, connected_components, gc_traversal, bench_thread_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-pythonperf1-amd64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: mypy2

- Geometric mean (including insignificant results): 1.023x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown