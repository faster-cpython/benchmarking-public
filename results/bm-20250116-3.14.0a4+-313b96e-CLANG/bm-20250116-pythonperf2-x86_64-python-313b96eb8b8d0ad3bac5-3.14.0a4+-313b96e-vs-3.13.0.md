# Results vs. 3.13.0

- fork: python
- ref: 313b96eb8b8d0ad3bac5
- machine: linux-x86_64
- commit hash: 313b96e
- commit date: 2025-01-16
- overall geometric mean: 1.030x faster
- HPT reliability: 99.36%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 280 ms: 1.04x faster                                                         |
| docutils       | 2.83 sec                                                     | 2.85 sec: 1.01x slower                                                       |
| html5lib       | 73.5 ms                                                      | 67.1 ms: 1.10x faster                                                        |
| sphinx         | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 324 ms: 1.44x faster                                                         |
| async_tree_io              | 843 ms                                                       | 629 ms: 1.34x faster                                                         |
| async_tree_none            | 376 ms                                                       | 282 ms: 1.33x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 630 ms: 1.32x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 346 ms: 1.31x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 267 ms: 1.29x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 545 ms: 1.11x faster                                                         |
| async_generators           | 457 ms                                                       | 414 ms: 1.10x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 528 ms: 1.10x faster                                                         |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                 |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 75.1 ms: 1.08x faster                                                        |
| pidigits       | 252 ms                                                       | 285 ms: 1.13x slower                                                         |
| nbody          | 89.3 ms                                                      | 105 ms: 1.18x slower                                                         |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.03 ms: 1.21x faster                                                        |
| regex_dna      | 247 ms                                                       | 222 ms: 1.11x faster                                                         |
| regex_compile  | 143 ms                                                       | 144 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.5 ms                                                      | 85.3 ms: 1.01x faster                                                        |
| tomli_loads          | 2.46 sec                                                     | 2.48 sec: 1.01x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 106 ms: 1.04x slower                                                         |
| json_loads           | 24.7 us                                                      | 25.6 us: 1.04x slower                                                        |
| json_dumps           | 11.1 ms                                                      | 11.9 ms: 1.07x slower                                                        |
| xml_etree_parse      | 150 ms                                                       | 163 ms: 1.08x slower                                                         |
| pickle_pure_python   | 323 us                                                       | 353 us: 1.09x slower                                                         |
| unpickle_pure_python | 217 us                                                       | 239 us: 1.10x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                                 |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| python_startup_no_site | 8.96 ms                                                      | 9.05 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 25.0 ms: 1.05x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 54.9 ms: 1.04x faster                                                        |
| django_template | 36.4 ms                                                      | 35.2 ms: 1.03x faster                                                        |
| mako            | 10.4 ms                                                      | 12.0 ms: 1.16x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250116-pythonperf2-x86_64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 324 ms: 1.44x faster                                                         |
| deepcopy                   | 392 us                                                       | 286 us: 1.37x faster                                                         |
| async_tree_io              | 843 ms                                                       | 629 ms: 1.34x faster                                                         |
| async_tree_none            | 376 ms                                                       | 282 ms: 1.33x faster                                                         |
| async_tree_io_tg           | 831 ms                                                       | 630 ms: 1.32x faster                                                         |
| async_tree_memoization     | 453 ms                                                       | 346 ms: 1.31x faster                                                         |
| async_tree_none_tg         | 346 ms                                                       | 267 ms: 1.29x faster                                                         |
| regex_effbot               | 3.67 ms                                                      | 3.03 ms: 1.21x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.93 us: 1.21x faster                                                        |
| go                         | 162 ms                                                       | 137 ms: 1.18x faster                                                         |
| deepcopy_memo              | 38.6 us                                                      | 33.4 us: 1.16x faster                                                        |
| richards_super             | 59.6 ms                                                      | 52.3 ms: 1.14x faster                                                        |
| richards                   | 52.9 ms                                                      | 46.8 ms: 1.13x faster                                                        |
| telco                      | 8.79 ms                                                      | 7.84 ms: 1.12x faster                                                        |
| pathlib                    | 17.5 ms                                                      | 15.7 ms: 1.12x faster                                                        |
| regex_dna                  | 247 ms                                                       | 222 ms: 1.11x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 545 ms: 1.11x faster                                                         |
| pylint                     | 347 ms                                                       | 314 ms: 1.10x faster                                                         |
| async_generators           | 457 ms                                                       | 414 ms: 1.10x faster                                                         |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 528 ms: 1.10x faster                                                         |
| coverage                   | 80.0 ms                                                      | 72.7 ms: 1.10x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 67.1 ms: 1.10x faster                                                        |
| json                       | 5.69 ms                                                      | 5.22 ms: 1.09x faster                                                        |
| float                      | 81.3 ms                                                      | 75.1 ms: 1.08x faster                                                        |
| pyflate                    | 503 ms                                                       | 473 ms: 1.06x faster                                                         |
| thrift                     | 901 us                                                       | 853 us: 1.06x faster                                                         |
| k_core                     | 2.17 sec                                                     | 2.06 sec: 1.05x faster                                                       |
| scimark_fft                | 328 ms                                                       | 311 ms: 1.05x faster                                                         |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.54 ms: 1.05x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 25.0 ms: 1.05x faster                                                        |
| logging_simple             | 6.39 us                                                      | 6.09 us: 1.05x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.86 sec: 1.05x faster                                                       |
| sympy_expand               | 509 ms                                                       | 487 ms: 1.05x faster                                                         |
| 2to3                       | 293 ms                                                       | 280 ms: 1.04x faster                                                         |
| sympy_integrate            | 23.6 ms                                                      | 22.6 ms: 1.04x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 3.28 ms: 1.04x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 54.9 ms: 1.04x faster                                                        |
| django_template            | 36.4 ms                                                      | 35.2 ms: 1.03x faster                                                        |
| sympy_str                  | 298 ms                                                       | 289 ms: 1.03x faster                                                         |
| sqlite_synth               | 2.91 us                                                      | 2.82 us: 1.03x faster                                                        |
| sympy_sum                  | 155 ms                                                       | 150 ms: 1.03x faster                                                         |
| spectral_norm              | 97.0 ms                                                      | 94.4 ms: 1.03x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.75 us: 1.03x faster                                                        |
| sqlalchemy_declarative     | 148 ms                                                       | 145 ms: 1.03x faster                                                         |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.9 ms: 1.02x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 66.6 ms: 1.02x faster                                                        |
| raytrace                   | 273 ms                                                       | 267 ms: 1.02x faster                                                         |
| sphinx                     | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                       |
| shortest_path              | 460 ms                                                       | 452 ms: 1.02x faster                                                         |
| bench_thread_pool          | 942 us                                                       | 926 us: 1.02x faster                                                         |
| generators                 | 33.6 ms                                                      | 33.1 ms: 1.02x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 85.3 ms: 1.01x faster                                                        |
| sqlglot_normalize          | 119 ms                                                       | 118 ms: 1.01x faster                                                         |
| sqlglot_optimize           | 59.3 ms                                                      | 58.7 ms: 1.01x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                         |
| connected_components       | 432 ms                                                       | 429 ms: 1.01x faster                                                         |
| sqlglot_transpile          | 1.79 ms                                                      | 1.78 ms: 1.00x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 99.1 ms: 1.00x slower                                                        |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.85 sec: 1.01x slower                                                       |
| tomli_loads                | 2.46 sec                                                     | 2.48 sec: 1.01x slower                                                       |
| python_startup_no_site     | 8.96 ms                                                      | 9.05 ms: 1.01x slower                                                        |
| regex_compile              | 143 ms                                                       | 144 ms: 1.01x slower                                                         |
| logging_silent             | 97.9 ns                                                      | 99.8 ns: 1.02x slower                                                        |
| pycparser                  | 1.24 sec                                                     | 1.27 sec: 1.02x slower                                                       |
| scimark_sor                | 123 ms                                                       | 126 ms: 1.02x slower                                                         |
| pprint_pformat             | 1.72 sec                                                     | 1.77 sec: 1.03x slower                                                       |
| meteor_contest             | 130 ms                                                       | 134 ms: 1.03x slower                                                         |
| mdp                        | 2.54 sec                                                     | 2.63 sec: 1.04x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 106 ms: 1.04x slower                                                         |
| pprint_safe_repr           | 843 ms                                                       | 874 ms: 1.04x slower                                                         |
| json_loads                 | 24.7 us                                                      | 25.6 us: 1.04x slower                                                        |
| hexiom                     | 6.55 ms                                                      | 6.84 ms: 1.04x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 95.5 ms: 1.05x slower                                                        |
| chaos                      | 60.2 ms                                                      | 63.9 ms: 1.06x slower                                                        |
| comprehensions             | 17.0 us                                                      | 18.1 us: 1.07x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 11.9 ms: 1.07x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.87 ms: 1.07x slower                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 71.2 ms: 1.08x slower                                                        |
| many_optionals             | 930 us                                                       | 1.01 ms: 1.08x slower                                                        |
| xml_etree_parse            | 150 ms                                                       | 163 ms: 1.08x slower                                                         |
| crypto_pyaes               | 73.3 ms                                                      | 79.6 ms: 1.09x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 353 us: 1.09x slower                                                         |
| unpickle_pure_python       | 217 us                                                       | 239 us: 1.10x slower                                                         |
| pidigits                   | 252 ms                                                       | 285 ms: 1.13x slower                                                         |
| mako                       | 10.4 ms                                                      | 12.0 ms: 1.16x slower                                                        |
| nbody                      | 89.3 ms                                                      | 105 ms: 1.18x slower                                                         |
| fannkuch                   | 363 ms                                                       | 431 ms: 1.19x slower                                                         |
| gc_traversal               | 4.74 ms                                                      | 5.64 ms: 1.19x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 22.5 ms: 1.29x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 1.47 sec: 287.27x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (5): coroutines, xml_etree_process, typing_runtime_protocols, sqlglot_parse, regex_v8
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.030x faster

# HPT report

- Reliability score: 99.36% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x