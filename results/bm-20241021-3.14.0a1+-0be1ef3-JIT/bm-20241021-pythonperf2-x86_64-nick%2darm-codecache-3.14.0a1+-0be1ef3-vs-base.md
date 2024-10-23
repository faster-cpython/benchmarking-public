# Results vs. base

- fork: nick-arm
- ref: codecache
- machine: linux-x86_64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.01x slower
- HPT reliability: 73.81%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 315 ms                                                                       | 314 ms: 1.00x faster                                                  |
| docutils       | 3.20 sec                                                                     | 3.18 sec: 1.01x faster                                                |
| html5lib       | 71.1 ms                                                                      | 70.4 ms: 1.01x faster                                                 |
| sphinx         | 1.27 sec                                                                     | 1.26 sec: 1.01x faster                                                |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg | 864 ms                                                                       | 871 ms: 1.01x slower                                                  |
| coroutines       | 21.2 ms                                                                      | 22.3 ms: 1.05x slower                                                 |
| Geometric mean   | (ref)                                                                        | 1.01x slower                                                          |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_generators, asyncio_websockets, async_tree_memoization_tg, async_tree_memoization, async_tree_none, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 84.7 ms                                                                      | 87.0 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                          |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                                      | 25.9 ms: 1.00x faster                                                 |
| regex_dna      | 257 ms                                                                       | 257 ms: 1.00x slower                                                  |
| regex_compile  | 146 ms                                                                       | 147 ms: 1.01x slower                                                  |
| regex_effbot   | 3.62 ms                                                                      | 3.73 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|---------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate  | 80.7 ms                                                                      | 81.1 ms: 1.00x slower                                                 |
| xml_etree_iterparse | 99.7 ms                                                                      | 100 ms: 1.01x slower                                                  |
| json_loads          | 24.7 us                                                                      | 25.0 us: 1.01x slower                                                 |
| tomli_loads         | 2.07 sec                                                                     | 2.11 sec: 1.02x slower                                                |
| xml_etree_parse     | 143 ms                                                                       | 146 ms: 1.02x slower                                                  |
| Geometric mean      | (ref)                                                                        | 1.01x slower                                                          |

Benchmark hidden because not significant (4): pickle_pure_python, unpickle_pure_python, json_dumps, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.9 ms                                                                      | 14.9 ms: 1.00x slower                                                 |
| python_startup_no_site | 9.00 ms                                                                      | 9.03 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                                        | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 29.0 ms                                                                      | 27.7 ms: 1.05x faster                                                 |
| django_template | 43.7 ms                                                                      | 43.1 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                                        | 1.02x faster                                                          |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark               | bm-20241021-pythonperf2-x86_64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-------------------------|:----------------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| coverage                | 82.5 ms                                                                      | 77.8 ms: 1.06x faster                                                 |
| genshi_text             | 29.0 ms                                                                      | 27.7 ms: 1.05x faster                                                 |
| scimark_monte_carlo     | 70.4 ms                                                                      | 68.8 ms: 1.02x faster                                                 |
| pyflate                 | 475 ms                                                                       | 466 ms: 1.02x faster                                                  |
| sqlglot_normalize       | 135 ms                                                                       | 133 ms: 1.02x faster                                                  |
| sqlglot_transpile       | 1.99 ms                                                                      | 1.96 ms: 1.02x faster                                                 |
| sqlglot_parse           | 1.52 ms                                                                      | 1.50 ms: 1.01x faster                                                 |
| django_template         | 43.7 ms                                                                      | 43.1 ms: 1.01x faster                                                 |
| raytrace                | 321 ms                                                                       | 316 ms: 1.01x faster                                                  |
| thrift                  | 909 us                                                                       | 897 us: 1.01x faster                                                  |
| html5lib                | 71.1 ms                                                                      | 70.4 ms: 1.01x faster                                                 |
| sqlglot_optimize        | 69.4 ms                                                                      | 68.8 ms: 1.01x faster                                                 |
| mdp                     | 2.59 sec                                                                     | 2.57 sec: 1.01x faster                                                |
| sphinx                  | 1.27 sec                                                                     | 1.26 sec: 1.01x faster                                                |
| scimark_fft             | 287 ms                                                                       | 285 ms: 1.01x faster                                                  |
| create_gc_cycles        | 2.92 ms                                                                      | 2.90 ms: 1.01x faster                                                 |
| pathlib                 | 15.9 ms                                                                      | 15.8 ms: 1.01x faster                                                 |
| docutils                | 3.20 sec                                                                     | 3.18 sec: 1.01x faster                                                |
| sympy_expand            | 529 ms                                                                       | 527 ms: 1.00x faster                                                  |
| sympy_str               | 318 ms                                                                       | 317 ms: 1.00x faster                                                  |
| scimark_sparse_mat_mult | 4.22 ms                                                                      | 4.21 ms: 1.00x faster                                                 |
| regex_v8                | 26.0 ms                                                                      | 25.9 ms: 1.00x faster                                                 |
| 2to3                    | 315 ms                                                                       | 314 ms: 1.00x faster                                                  |
| regex_dna               | 257 ms                                                                       | 257 ms: 1.00x slower                                                  |
| python_startup          | 14.9 ms                                                                      | 14.9 ms: 1.00x slower                                                 |
| hexiom                  | 7.19 ms                                                                      | 7.21 ms: 1.00x slower                                                 |
| python_startup_no_site  | 9.00 ms                                                                      | 9.03 ms: 1.00x slower                                                 |
| generators              | 38.6 ms                                                                      | 38.7 ms: 1.00x slower                                                 |
| xml_etree_generate      | 80.7 ms                                                                      | 81.1 ms: 1.00x slower                                                 |
| crypto_pyaes            | 72.7 ms                                                                      | 73.0 ms: 1.00x slower                                                 |
| regex_compile           | 146 ms                                                                       | 147 ms: 1.01x slower                                                  |
| async_tree_io_tg        | 864 ms                                                                       | 871 ms: 1.01x slower                                                  |
| logging_silent          | 91.6 ns                                                                      | 92.3 ns: 1.01x slower                                                 |
| xml_etree_iterparse     | 99.7 ms                                                                      | 100 ms: 1.01x slower                                                  |
| comprehensions          | 18.7 us                                                                      | 18.8 us: 1.01x slower                                                 |
| meteor_contest          | 131 ms                                                                       | 132 ms: 1.01x slower                                                  |
| pycparser               | 1.26 sec                                                                     | 1.27 sec: 1.01x slower                                                |
| dulwich_log             | 62.9 ms                                                                      | 63.5 ms: 1.01x slower                                                 |
| deltablue               | 3.30 ms                                                                      | 3.34 ms: 1.01x slower                                                 |
| chaos                   | 68.0 ms                                                                      | 68.7 ms: 1.01x slower                                                 |
| spectral_norm           | 93.8 ms                                                                      | 94.8 ms: 1.01x slower                                                 |
| json_loads              | 24.7 us                                                                      | 25.0 us: 1.01x slower                                                 |
| bpe_tokeniser           | 4.69 sec                                                                     | 4.76 sec: 1.02x slower                                                |
| logging_format          | 7.10 us                                                                      | 7.23 us: 1.02x slower                                                 |
| scimark_sor             | 103 ms                                                                       | 105 ms: 1.02x slower                                                  |
| tomli_loads             | 2.07 sec                                                                     | 2.11 sec: 1.02x slower                                                |
| xml_etree_parse         | 143 ms                                                                       | 146 ms: 1.02x slower                                                  |
| pprint_pformat          | 1.61 sec                                                                     | 1.65 sec: 1.02x slower                                                |
| nbody                   | 84.7 ms                                                                      | 87.0 ms: 1.03x slower                                                 |
| go                      | 151 ms                                                                       | 155 ms: 1.03x slower                                                  |
| regex_effbot            | 3.62 ms                                                                      | 3.73 ms: 1.03x slower                                                 |
| richards_super          | 52.9 ms                                                                      | 54.7 ms: 1.03x slower                                                 |
| logging_simple          | 6.44 us                                                                      | 6.75 us: 1.05x slower                                                 |
| coroutines              | 21.2 ms                                                                      | 22.3 ms: 1.05x slower                                                 |
| gc_traversal            | 5.20 ms                                                                      | 5.81 ms: 1.12x slower                                                 |
| Geometric mean          | (ref)                                                                        | 1.01x slower                                                          |

Benchmark hidden because not significant (34): pylint, deepcopy_memo, bench_thread_pool, tornado_http, genshi_xml, nqueens, pprint_safe_repr, async_tree_cpu_io_mixed, sympy_sum, sympy_integrate, async_tree_cpu_io_mixed_tg, typing_runtime_protocols, richards, async_generators, asyncio_websockets, pickle_pure_python, pidigits, async_tree_memoization_tg, unpickle_pure_python, json_dumps, async_tree_memoization, scimark_lu, float, async_tree_none, fannkuch, async_tree_none_tg, telco, deepcopy, json, xml_etree_process, deepcopy_reduce, mako, async_tree_io, bench_mp_pool

# HPT report

- Reliability score: 73.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x