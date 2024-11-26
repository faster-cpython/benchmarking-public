# Results vs. 3.13.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: linux-x86_64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.009x slower
- HPT reliability: 66.85%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 319 ms: 1.09x slower                                                         |
| docutils       | 2.81 sec                                                     | 3.19 sec: 1.14x slower                                                       |
| sphinx         | 1.11 sec                                                     | 1.27 sec: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                 |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 372 ms: 1.23x faster                                                         |
| async_tree_none            | 370 ms                                                       | 336 ms: 1.10x faster                                                         |
| async_tree_memoization     | 447 ms                                                       | 409 ms: 1.09x faster                                                         |
| async_tree_none_tg         | 342 ms                                                       | 321 ms: 1.07x faster                                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 556 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 579 ms: 1.03x faster                                                         |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                        |
| async_tree_io_tg           | 823 ms                                                       | 861 ms: 1.05x slower                                                         |
| async_generators           | 364 ms                                                       | 398 ms: 1.10x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 82.8 ms: 1.11x faster                                                        |
| float          | 81.6 ms                                                      | 79.4 ms: 1.03x faster                                                        |
| pidigits       | 252 ms                                                       | 251 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 236 ms: 1.01x faster                                                         |
| regex_v8       | 24.9 ms                                                      | 25.3 ms: 1.02x slower                                                        |
| regex_effbot   | 3.51 ms                                                      | 3.59 ms: 1.02x slower                                                        |
| regex_compile  | 143 ms                                                       | 149 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.09 sec: 1.16x faster                                                       |
| xml_etree_process    | 60.7 ms                                                      | 57.5 ms: 1.06x faster                                                        |
| xml_etree_generate   | 85.2 ms                                                      | 80.9 ms: 1.05x faster                                                        |
| json_loads           | 24.7 us                                                      | 24.2 us: 1.02x faster                                                        |
| xml_etree_iterparse  | 99.8 ms                                                      | 100 ms: 1.01x slower                                                         |
| unpickle_pure_python | 216 us                                                       | 218 us: 1.01x slower                                                         |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.01x slower                                                         |
| json_dumps           | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                        |
| pickle_pure_python   | 322 us                                                       | 342 us: 1.06x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.93 ms                                                      | 9.02 ms: 1.01x slower                                                        |
| python_startup         | 15.6 ms                                                      | 15.8 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.24 ms: 1.12x faster                                                        |
| genshi_text     | 27.2 ms                                                      | 29.0 ms: 1.07x slower                                                        |
| django_template | 38.9 ms                                                      | 42.4 ms: 1.09x slower                                                        |
| genshi_xml      | 58.0 ms                                                      | 66.1 ms: 1.14x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 30.1 us: 1.29x faster                                                        |
| deepcopy                   | 388 us                                                       | 309 us: 1.26x faster                                                         |
| async_tree_memoization_tg  | 458 ms                                                       | 372 ms: 1.23x faster                                                         |
| richards                   | 52.5 ms                                                      | 44.3 ms: 1.18x faster                                                        |
| scimark_sor                | 125 ms                                                       | 107 ms: 1.17x faster                                                         |
| richards_super             | 60.2 ms                                                      | 51.8 ms: 1.16x faster                                                        |
| tomli_loads                | 2.43 sec                                                     | 2.09 sec: 1.16x faster                                                       |
| telco                      | 8.77 ms                                                      | 7.63 ms: 1.15x faster                                                        |
| deepcopy_reduce            | 3.49 us                                                      | 3.05 us: 1.14x faster                                                        |
| mako                       | 10.3 ms                                                      | 9.24 ms: 1.12x faster                                                        |
| nbody                      | 92.1 ms                                                      | 82.8 ms: 1.11x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                        |
| async_tree_none            | 370 ms                                                       | 336 ms: 1.10x faster                                                         |
| async_tree_memoization     | 447 ms                                                       | 409 ms: 1.09x faster                                                         |
| json                       | 5.62 ms                                                      | 5.15 ms: 1.09x faster                                                        |
| shortest_path              | 477 ms                                                       | 438 ms: 1.09x faster                                                         |
| connected_components       | 443 ms                                                       | 406 ms: 1.09x faster                                                         |
| go                         | 167 ms                                                       | 155 ms: 1.08x faster                                                         |
| async_tree_none_tg         | 342 ms                                                       | 321 ms: 1.07x faster                                                         |
| bpe_tokeniser              | 5.09 sec                                                     | 4.77 sec: 1.07x faster                                                       |
| logging_silent             | 97.5 ns                                                      | 92.0 ns: 1.06x faster                                                        |
| pyflate                    | 493 ms                                                       | 466 ms: 1.06x faster                                                         |
| xml_etree_process          | 60.7 ms                                                      | 57.5 ms: 1.06x faster                                                        |
| xml_etree_generate         | 85.2 ms                                                      | 80.9 ms: 1.05x faster                                                        |
| pprint_safe_repr           | 835 ms                                                       | 800 ms: 1.04x faster                                                         |
| coverage                   | 84.5 ms                                                      | 81.7 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 556 ms: 1.03x faster                                                         |
| fannkuch                   | 384 ms                                                       | 372 ms: 1.03x faster                                                         |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 579 ms: 1.03x faster                                                         |
| spectral_norm              | 97.4 ms                                                      | 94.7 ms: 1.03x faster                                                        |
| float                      | 81.6 ms                                                      | 79.4 ms: 1.03x faster                                                        |
| deltablue                  | 3.38 ms                                                      | 3.29 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.70 sec                                                     | 1.66 sec: 1.02x faster                                                       |
| json_loads                 | 24.7 us                                                      | 24.2 us: 1.02x faster                                                        |
| dulwich_log                | 65.5 ms                                                      | 64.6 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                        |
| regex_dna                  | 238 ms                                                       | 236 ms: 1.01x faster                                                         |
| scimark_lu                 | 97.4 ms                                                      | 97.0 ms: 1.00x faster                                                        |
| pidigits                   | 252 ms                                                       | 251 ms: 1.00x faster                                                         |
| scimark_fft                | 298 ms                                                       | 297 ms: 1.00x faster                                                         |
| xml_etree_iterparse        | 99.8 ms                                                      | 100 ms: 1.01x slower                                                         |
| unpickle_pure_python       | 216 us                                                       | 218 us: 1.01x slower                                                         |
| meteor_contest             | 130 ms                                                       | 132 ms: 1.01x slower                                                         |
| python_startup_no_site     | 8.93 ms                                                      | 9.02 ms: 1.01x slower                                                        |
| pycparser                  | 1.28 sec                                                     | 1.30 sec: 1.01x slower                                                       |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.01x slower                                                         |
| python_startup             | 15.6 ms                                                      | 15.8 ms: 1.01x slower                                                        |
| regex_v8                   | 24.9 ms                                                      | 25.3 ms: 1.02x slower                                                        |
| mdp                        | 2.53 sec                                                     | 2.58 sec: 1.02x slower                                                       |
| regex_effbot               | 3.51 ms                                                      | 3.59 ms: 1.02x slower                                                        |
| logging_format             | 6.95 us                                                      | 7.12 us: 1.02x slower                                                        |
| sqlalchemy_imperative      | 18.1 ms                                                      | 18.6 ms: 1.02x slower                                                        |
| bench_thread_pool          | 929 us                                                       | 961 us: 1.03x slower                                                         |
| json_dumps                 | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                        |
| typing_runtime_protocols   | 176 us                                                       | 183 us: 1.04x slower                                                         |
| logging_simple             | 6.28 us                                                      | 6.54 us: 1.04x slower                                                        |
| regex_compile              | 143 ms                                                       | 149 ms: 1.05x slower                                                         |
| async_tree_io_tg           | 823 ms                                                       | 861 ms: 1.05x slower                                                         |
| sympy_expand               | 506 ms                                                       | 530 ms: 1.05x slower                                                         |
| scimark_monte_carlo        | 65.2 ms                                                      | 69.2 ms: 1.06x slower                                                        |
| pickle_pure_python         | 322 us                                                       | 342 us: 1.06x slower                                                         |
| genshi_text                | 27.2 ms                                                      | 29.0 ms: 1.07x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.54 ms: 1.08x slower                                                        |
| sympy_str                  | 297 ms                                                       | 321 ms: 1.08x slower                                                         |
| create_gc_cycles           | 2.65 ms                                                      | 2.88 ms: 1.09x slower                                                        |
| 2to3                       | 293 ms                                                       | 319 ms: 1.09x slower                                                         |
| django_template            | 38.9 ms                                                      | 42.4 ms: 1.09x slower                                                        |
| async_generators           | 364 ms                                                       | 398 ms: 1.10x slower                                                         |
| chaos                      | 60.6 ms                                                      | 66.7 ms: 1.10x slower                                                        |
| sqlglot_parse              | 1.37 ms                                                      | 1.51 ms: 1.11x slower                                                        |
| hexiom                     | 6.47 ms                                                      | 7.17 ms: 1.11x slower                                                        |
| sqlglot_normalize          | 119 ms                                                       | 132 ms: 1.11x slower                                                         |
| pylint                     | 345 ms                                                       | 384 ms: 1.11x slower                                                         |
| nqueens                    | 92.3 ms                                                      | 103 ms: 1.12x slower                                                         |
| sqlalchemy_declarative     | 148 ms                                                       | 167 ms: 1.13x slower                                                         |
| sqlglot_transpile          | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                        |
| sympy_sum                  | 154 ms                                                       | 174 ms: 1.13x slower                                                         |
| docutils                   | 2.81 sec                                                     | 3.19 sec: 1.14x slower                                                       |
| genshi_xml                 | 58.0 ms                                                      | 66.1 ms: 1.14x slower                                                        |
| sphinx                     | 1.11 sec                                                     | 1.27 sec: 1.14x slower                                                       |
| comprehensions             | 17.3 us                                                      | 19.8 us: 1.14x slower                                                        |
| generators                 | 33.9 ms                                                      | 39.1 ms: 1.15x slower                                                        |
| gc_traversal               | 4.48 ms                                                      | 5.21 ms: 1.16x slower                                                        |
| sympy_integrate            | 23.4 ms                                                      | 27.3 ms: 1.17x slower                                                        |
| sqlglot_optimize           | 58.7 ms                                                      | 68.6 ms: 1.17x slower                                                        |
| raytrace                   | 267 ms                                                       | 323 ms: 1.21x slower                                                         |
| k_core                     | 2.18 sec                                                     | 2.99 sec: 1.37x slower                                                       |
| bench_mp_pool              | 4.82 ms                                                      | 2.44 sec: 507.01x slower                                                     |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                 |

Benchmark hidden because not significant (5): asyncio_websockets, async_tree_io, thrift, crypto_pyaes, html5lib
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-pythonperf2-x86_64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: sqlite_synth

- Geometric mean (including insignificant results): 1.009x slower
# HPT report

- Reliability score: 66.85% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x