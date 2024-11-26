# Results vs. 3.13.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: linux-x86_64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.017x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 283 ms: 1.03x faster                                                         |
| docutils       | 2.81 sec                                                     | 2.93 sec: 1.04x slower                                                       |
| html5lib       | 72.9 ms                                                      | 71.5 ms: 1.02x faster                                                        |
| sphinx         | 1.11 sec                                                     | 1.13 sec: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 376 ms: 1.22x faster                                                         |
| async_tree_none            | 370 ms                                                       | 329 ms: 1.12x faster                                                         |
| async_tree_memoization     | 447 ms                                                       | 406 ms: 1.10x faster                                                         |
| async_tree_none_tg         | 342 ms                                                       | 324 ms: 1.06x faster                                                         |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 574 ms: 1.04x faster                                                         |
| asyncio_websockets         | 395 ms                                                       | 382 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                         |
| async_generators           | 364 ms                                                       | 357 ms: 1.02x faster                                                         |
| async_tree_io              | 832 ms                                                       | 847 ms: 1.02x slower                                                         |
| async_tree_io_tg           | 823 ms                                                       | 872 ms: 1.06x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 253 ms: 1.00x slower                                                         |
| float          | 81.6 ms                                                      | 82.6 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 143 ms                                                       | 140 ms: 1.02x faster                                                         |
| regex_v8       | 24.9 ms                                                      | 24.8 ms: 1.00x faster                                                        |
| regex_dna      | 238 ms                                                       | 241 ms: 1.01x slower                                                         |
| regex_effbot   | 3.51 ms                                                      | 3.57 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|---------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate  | 85.2 ms                                                      | 84.5 ms: 1.01x faster                                                        |
| xml_etree_parse     | 144 ms                                                       | 142 ms: 1.01x faster                                                         |
| xml_etree_iterparse | 99.8 ms                                                      | 101 ms: 1.01x slower                                                         |
| pickle_pure_python  | 322 us                                                       | 332 us: 1.03x slower                                                         |
| json_dumps          | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                        |
| tomli_loads         | 2.43 sec                                                     | 2.55 sec: 1.05x slower                                                       |
| Geometric mean      | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (3): json_loads, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.93 ms                                                      | 9.05 ms: 1.01x slower                                                        |
| python_startup         | 15.6 ms                                                      | 15.9 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 58.0 ms                                                      | 54.6 ms: 1.06x faster                                                        |
| genshi_text     | 27.2 ms                                                      | 26.9 ms: 1.01x faster                                                        |
| django_template | 38.9 ms                                                      | 39.9 ms: 1.03x slower                                                        |
| mako            | 10.3 ms                                                      | 10.7 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                   | 388 us                                                       | 291 us: 1.34x faster                                                         |
| deepcopy_memo              | 38.9 us                                                      | 29.2 us: 1.33x faster                                                        |
| go                         | 167 ms                                                       | 136 ms: 1.23x faster                                                         |
| async_tree_memoization_tg  | 458 ms                                                       | 376 ms: 1.22x faster                                                         |
| deepcopy_reduce            | 3.49 us                                                      | 3.01 us: 1.16x faster                                                        |
| generators                 | 33.9 ms                                                      | 29.3 ms: 1.16x faster                                                        |
| async_tree_none            | 370 ms                                                       | 329 ms: 1.12x faster                                                         |
| telco                      | 8.77 ms                                                      | 7.95 ms: 1.10x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 406 ms: 1.10x faster                                                         |
| json                       | 5.62 ms                                                      | 5.14 ms: 1.09x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 16.0 ms: 1.09x faster                                                        |
| scimark_sor                | 125 ms                                                       | 115 ms: 1.08x faster                                                         |
| fannkuch                   | 384 ms                                                       | 359 ms: 1.07x faster                                                         |
| genshi_xml                 | 58.0 ms                                                      | 54.6 ms: 1.06x faster                                                        |
| richards_super             | 60.2 ms                                                      | 56.7 ms: 1.06x faster                                                        |
| shortest_path              | 477 ms                                                       | 450 ms: 1.06x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.81 sec: 1.06x faster                                                       |
| async_tree_none_tg         | 342 ms                                                       | 324 ms: 1.06x faster                                                         |
| nqueens                    | 92.3 ms                                                      | 87.5 ms: 1.06x faster                                                        |
| thrift                     | 918 us                                                       | 870 us: 1.05x faster                                                         |
| pprint_safe_repr           | 835 ms                                                       | 794 ms: 1.05x faster                                                         |
| meteor_contest             | 130 ms                                                       | 124 ms: 1.05x faster                                                         |
| pprint_pformat             | 1.70 sec                                                     | 1.62 sec: 1.05x faster                                                       |
| sqlalchemy_declarative     | 148 ms                                                       | 142 ms: 1.04x faster                                                         |
| connected_components       | 443 ms                                                       | 425 ms: 1.04x faster                                                         |
| coverage                   | 84.5 ms                                                      | 81.2 ms: 1.04x faster                                                        |
| richards                   | 52.5 ms                                                      | 50.6 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 574 ms: 1.04x faster                                                         |
| bench_thread_pool          | 929 us                                                       | 899 us: 1.03x faster                                                         |
| asyncio_websockets         | 395 ms                                                       | 382 ms: 1.03x faster                                                         |
| 2to3                       | 293 ms                                                       | 283 ms: 1.03x faster                                                         |
| pyflate                    | 493 ms                                                       | 478 ms: 1.03x faster                                                         |
| hexiom                     | 6.47 ms                                                      | 6.30 ms: 1.03x faster                                                        |
| pycparser                  | 1.28 sec                                                     | 1.25 sec: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                         |
| sympy_sum                  | 154 ms                                                       | 151 ms: 1.02x faster                                                         |
| mdp                        | 2.53 sec                                                     | 2.48 sec: 1.02x faster                                                       |
| html5lib                   | 72.9 ms                                                      | 71.5 ms: 1.02x faster                                                        |
| scimark_fft                | 298 ms                                                       | 293 ms: 1.02x faster                                                         |
| sympy_str                  | 297 ms                                                       | 291 ms: 1.02x faster                                                         |
| regex_compile              | 143 ms                                                       | 140 ms: 1.02x faster                                                         |
| async_generators           | 364 ms                                                       | 357 ms: 1.02x faster                                                         |
| scimark_monte_carlo        | 65.2 ms                                                      | 64.1 ms: 1.02x faster                                                        |
| sympy_expand               | 506 ms                                                       | 501 ms: 1.01x faster                                                         |
| spectral_norm              | 97.4 ms                                                      | 96.4 ms: 1.01x faster                                                        |
| genshi_text                | 27.2 ms                                                      | 26.9 ms: 1.01x faster                                                        |
| sqlglot_normalize          | 119 ms                                                       | 118 ms: 1.01x faster                                                         |
| xml_etree_generate         | 85.2 ms                                                      | 84.5 ms: 1.01x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.01x faster                                                         |
| typing_runtime_protocols   | 176 us                                                       | 174 us: 1.01x faster                                                         |
| sympy_integrate            | 23.4 ms                                                      | 23.3 ms: 1.00x faster                                                        |
| regex_v8                   | 24.9 ms                                                      | 24.8 ms: 1.00x faster                                                        |
| pidigits                   | 252 ms                                                       | 253 ms: 1.00x slower                                                         |
| scimark_lu                 | 97.4 ms                                                      | 98.1 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.25 ms: 1.01x slower                                                        |
| comprehensions             | 17.3 us                                                      | 17.4 us: 1.01x slower                                                        |
| regex_dna                  | 238 ms                                                       | 241 ms: 1.01x slower                                                         |
| xml_etree_iterparse        | 99.8 ms                                                      | 101 ms: 1.01x slower                                                         |
| float                      | 81.6 ms                                                      | 82.6 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.93 ms                                                      | 9.05 ms: 1.01x slower                                                        |
| python_startup             | 15.6 ms                                                      | 15.9 ms: 1.01x slower                                                        |
| sphinx                     | 1.11 sec                                                     | 1.13 sec: 1.01x slower                                                       |
| regex_effbot               | 3.51 ms                                                      | 3.57 ms: 1.02x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                      | 1.79 ms: 1.02x slower                                                        |
| sqlalchemy_imperative      | 18.1 ms                                                      | 18.5 ms: 1.02x slower                                                        |
| logging_simple             | 6.28 us                                                      | 6.39 us: 1.02x slower                                                        |
| async_tree_io              | 832 ms                                                       | 847 ms: 1.02x slower                                                         |
| crypto_pyaes               | 73.5 ms                                                      | 75.2 ms: 1.02x slower                                                        |
| django_template            | 38.9 ms                                                      | 39.9 ms: 1.03x slower                                                        |
| dulwich_log                | 65.5 ms                                                      | 67.4 ms: 1.03x slower                                                        |
| chaos                      | 60.6 ms                                                      | 62.5 ms: 1.03x slower                                                        |
| pickle_pure_python         | 322 us                                                       | 332 us: 1.03x slower                                                         |
| mako                       | 10.3 ms                                                      | 10.7 ms: 1.03x slower                                                        |
| raytrace                   | 267 ms                                                       | 276 ms: 1.03x slower                                                         |
| sqlglot_parse              | 1.37 ms                                                      | 1.42 ms: 1.04x slower                                                        |
| docutils                   | 2.81 sec                                                     | 2.93 sec: 1.04x slower                                                       |
| deltablue                  | 3.38 ms                                                      | 3.54 ms: 1.04x slower                                                        |
| json_dumps                 | 10.8 ms                                                      | 11.3 ms: 1.05x slower                                                        |
| tomli_loads                | 2.43 sec                                                     | 2.55 sec: 1.05x slower                                                       |
| logging_silent             | 97.5 ns                                                      | 103 ns: 1.05x slower                                                         |
| async_tree_io_tg           | 823 ms                                                       | 872 ms: 1.06x slower                                                         |
| create_gc_cycles           | 2.65 ms                                                      | 3.02 ms: 1.14x slower                                                        |
| gc_traversal               | 4.48 ms                                                      | 5.80 ms: 1.30x slower                                                        |
| k_core                     | 2.18 sec                                                     | 3.08 sec: 1.41x slower                                                       |
| bench_mp_pool              | 4.82 ms                                                      | 2.16 sec: 448.41x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                 |

Benchmark hidden because not significant (8): nbody, json_loads, unpickle_pure_python, coroutines, xml_etree_process, sqlglot_optimize, pylint, logging_format
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: sqlite_synth

- Geometric mean (including insignificant results): 1.017x faster
# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x