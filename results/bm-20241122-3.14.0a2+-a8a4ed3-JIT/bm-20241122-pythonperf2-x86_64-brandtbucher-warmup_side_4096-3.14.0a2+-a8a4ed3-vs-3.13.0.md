# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_side_4096
- machine: linux-x86_64
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.003x slower
- HPT reliability: 67.29%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 292 ms: 1.00x faster                                                           |
| docutils       | 2.81 sec                                                     | 3.04 sec: 1.08x slower                                                         |
| html5lib       | 72.9 ms                                                      | 72.1 ms: 1.01x faster                                                          |
| sphinx         | 1.11 sec                                                     | 1.18 sec: 1.06x slower                                                         |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|---------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 458 ms                                                       | 386 ms: 1.19x faster                                                           |
| async_tree_none           | 370 ms                                                       | 333 ms: 1.11x faster                                                           |
| async_tree_memoization    | 447 ms                                                       | 408 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed   | 596 ms                                                       | 576 ms: 1.03x faster                                                           |
| asyncio_websockets        | 395 ms                                                       | 386 ms: 1.02x faster                                                           |
| async_tree_io_tg          | 823 ms                                                       | 839 ms: 1.02x slower                                                           |
| async_generators          | 364 ms                                                       | 475 ms: 1.31x slower                                                           |
| Geometric mean            | (ref)                                                        | 1.01x faster                                                                   |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, async_tree_none_tg, coroutines, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 85.9 ms: 1.07x faster                                                          |
| float          | 81.6 ms                                                      | 79.9 ms: 1.02x faster                                                          |
| pidigits       | 252 ms                                                       | 251 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.34 ms: 1.05x faster                                                          |
| regex_v8       | 24.9 ms                                                      | 25.6 ms: 1.03x slower                                                          |
| regex_dna      | 238 ms                                                       | 253 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.21 sec: 1.10x faster                                                         |
| unpickle_pure_python | 216 us                                                       | 201 us: 1.07x faster                                                           |
| xml_etree_process    | 60.7 ms                                                      | 57.4 ms: 1.06x faster                                                          |
| xml_etree_generate   | 85.2 ms                                                      | 81.5 ms: 1.05x faster                                                          |
| xml_etree_iterparse  | 99.8 ms                                                      | 102 ms: 1.02x slower                                                           |
| json_loads           | 24.7 us                                                      | 25.2 us: 1.02x slower                                                          |
| json_dumps           | 10.8 ms                                                      | 11.4 ms: 1.05x slower                                                          |
| pickle_pure_python   | 322 us                                                       | 345 us: 1.07x slower                                                           |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 8.93 ms                                                      | 8.99 ms: 1.01x slower                                                          |
| python_startup         | 15.6 ms                                                      | 16.0 ms: 1.03x slower                                                          |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.42 ms: 1.10x faster                                                          |
| django_template | 38.9 ms                                                      | 40.8 ms: 1.05x slower                                                          |
| genshi_text     | 27.2 ms                                                      | 29.4 ms: 1.08x slower                                                          |
| genshi_xml      | 58.0 ms                                                      | 63.7 ms: 1.10x slower                                                          |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|---------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo             | 38.9 us                                                      | 29.1 us: 1.34x faster                                                          |
| deepcopy                  | 388 us                                                       | 310 us: 1.25x faster                                                           |
| scimark_sor               | 125 ms                                                       | 102 ms: 1.22x faster                                                           |
| richards_super            | 60.2 ms                                                      | 50.1 ms: 1.20x faster                                                          |
| richards                  | 52.5 ms                                                      | 43.8 ms: 1.20x faster                                                          |
| async_tree_memoization_tg | 458 ms                                                       | 386 ms: 1.19x faster                                                           |
| deepcopy_reduce           | 3.49 us                                                      | 3.03 us: 1.15x faster                                                          |
| telco                     | 8.77 ms                                                      | 7.64 ms: 1.15x faster                                                          |
| async_tree_none           | 370 ms                                                       | 333 ms: 1.11x faster                                                           |
| connected_components      | 443 ms                                                       | 402 ms: 1.10x faster                                                           |
| tomli_loads               | 2.43 sec                                                     | 2.21 sec: 1.10x faster                                                         |
| mako                      | 10.3 ms                                                      | 9.42 ms: 1.10x faster                                                          |
| async_tree_memoization    | 447 ms                                                       | 408 ms: 1.10x faster                                                           |
| shortest_path             | 477 ms                                                       | 436 ms: 1.09x faster                                                           |
| json                      | 5.62 ms                                                      | 5.16 ms: 1.09x faster                                                          |
| unpickle_pure_python      | 216 us                                                       | 201 us: 1.07x faster                                                           |
| nbody                     | 92.1 ms                                                      | 85.9 ms: 1.07x faster                                                          |
| pylint                    | 345 ms                                                       | 323 ms: 1.07x faster                                                           |
| coverage                  | 84.5 ms                                                      | 79.6 ms: 1.06x faster                                                          |
| go                        | 167 ms                                                       | 157 ms: 1.06x faster                                                           |
| xml_etree_process         | 60.7 ms                                                      | 57.4 ms: 1.06x faster                                                          |
| pathlib                   | 17.4 ms                                                      | 16.5 ms: 1.05x faster                                                          |
| regex_effbot              | 3.51 ms                                                      | 3.34 ms: 1.05x faster                                                          |
| bpe_tokeniser             | 5.09 sec                                                     | 4.85 sec: 1.05x faster                                                         |
| pprint_safe_repr          | 835 ms                                                       | 798 ms: 1.05x faster                                                           |
| xml_etree_generate        | 85.2 ms                                                      | 81.5 ms: 1.05x faster                                                          |
| logging_silent            | 97.5 ns                                                      | 93.6 ns: 1.04x faster                                                          |
| deltablue                 | 3.38 ms                                                      | 3.26 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed   | 596 ms                                                       | 576 ms: 1.03x faster                                                           |
| pyflate                   | 493 ms                                                       | 477 ms: 1.03x faster                                                           |
| scimark_lu                | 97.4 ms                                                      | 94.5 ms: 1.03x faster                                                          |
| thrift                    | 918 us                                                       | 896 us: 1.02x faster                                                           |
| asyncio_websockets        | 395 ms                                                       | 386 ms: 1.02x faster                                                           |
| float                     | 81.6 ms                                                      | 79.9 ms: 1.02x faster                                                          |
| pprint_pformat            | 1.70 sec                                                     | 1.67 sec: 1.02x faster                                                         |
| sqlalchemy_declarative    | 148 ms                                                       | 146 ms: 1.02x faster                                                           |
| html5lib                  | 72.9 ms                                                      | 72.1 ms: 1.01x faster                                                          |
| crypto_pyaes              | 73.5 ms                                                      | 72.9 ms: 1.01x faster                                                          |
| pidigits                  | 252 ms                                                       | 251 ms: 1.00x faster                                                           |
| 2to3                      | 293 ms                                                       | 292 ms: 1.00x faster                                                           |
| python_startup_no_site    | 8.93 ms                                                      | 8.99 ms: 1.01x slower                                                          |
| pycparser                 | 1.28 sec                                                     | 1.29 sec: 1.01x slower                                                         |
| meteor_contest            | 130 ms                                                       | 131 ms: 1.01x slower                                                           |
| scimark_fft               | 298 ms                                                       | 303 ms: 1.02x slower                                                           |
| xml_etree_iterparse       | 99.8 ms                                                      | 102 ms: 1.02x slower                                                           |
| sqlalchemy_imperative     | 18.1 ms                                                      | 18.5 ms: 1.02x slower                                                          |
| async_tree_io_tg          | 823 ms                                                       | 839 ms: 1.02x slower                                                           |
| json_loads                | 24.7 us                                                      | 25.2 us: 1.02x slower                                                          |
| python_startup            | 15.6 ms                                                      | 16.0 ms: 1.03x slower                                                          |
| regex_v8                  | 24.9 ms                                                      | 25.6 ms: 1.03x slower                                                          |
| scimark_monte_carlo       | 65.2 ms                                                      | 67.4 ms: 1.03x slower                                                          |
| dulwich_log               | 65.5 ms                                                      | 67.8 ms: 1.03x slower                                                          |
| mdp                       | 2.53 sec                                                     | 2.62 sec: 1.04x slower                                                         |
| bench_thread_pool         | 929 us                                                       | 967 us: 1.04x slower                                                           |
| sympy_integrate           | 23.4 ms                                                      | 24.4 ms: 1.04x slower                                                          |
| sympy_sum                 | 154 ms                                                       | 161 ms: 1.05x slower                                                           |
| sympy_expand              | 506 ms                                                       | 531 ms: 1.05x slower                                                           |
| sympy_str                 | 297 ms                                                       | 311 ms: 1.05x slower                                                           |
| django_template           | 38.9 ms                                                      | 40.8 ms: 1.05x slower                                                          |
| json_dumps                | 10.8 ms                                                      | 11.4 ms: 1.05x slower                                                          |
| sphinx                    | 1.11 sec                                                     | 1.18 sec: 1.06x slower                                                         |
| logging_format            | 6.95 us                                                      | 7.36 us: 1.06x slower                                                          |
| sqlglot_normalize         | 119 ms                                                       | 126 ms: 1.06x slower                                                           |
| typing_runtime_protocols  | 176 us                                                       | 186 us: 1.06x slower                                                           |
| regex_dna                 | 238 ms                                                       | 253 ms: 1.06x slower                                                           |
| sqlglot_transpile         | 1.76 ms                                                      | 1.87 ms: 1.06x slower                                                          |
| create_gc_cycles          | 2.65 ms                                                      | 2.84 ms: 1.07x slower                                                          |
| pickle_pure_python        | 322 us                                                       | 345 us: 1.07x slower                                                           |
| sqlglot_optimize          | 58.7 ms                                                      | 63.0 ms: 1.07x slower                                                          |
| logging_simple            | 6.28 us                                                      | 6.77 us: 1.08x slower                                                          |
| genshi_text               | 27.2 ms                                                      | 29.4 ms: 1.08x slower                                                          |
| docutils                  | 2.81 sec                                                     | 3.04 sec: 1.08x slower                                                         |
| sqlglot_parse             | 1.37 ms                                                      | 1.48 ms: 1.09x slower                                                          |
| chaos                     | 60.6 ms                                                      | 66.3 ms: 1.10x slower                                                          |
| genshi_xml                | 58.0 ms                                                      | 63.7 ms: 1.10x slower                                                          |
| hexiom                    | 6.47 ms                                                      | 7.12 ms: 1.10x slower                                                          |
| nqueens                   | 92.3 ms                                                      | 102 ms: 1.10x slower                                                           |
| comprehensions            | 17.3 us                                                      | 19.6 us: 1.14x slower                                                          |
| scimark_sparse_mat_mult   | 4.21 ms                                                      | 4.87 ms: 1.16x slower                                                          |
| k_core                    | 2.18 sec                                                     | 2.56 sec: 1.17x slower                                                         |
| raytrace                  | 267 ms                                                       | 322 ms: 1.20x slower                                                           |
| generators                | 33.9 ms                                                      | 42.9 ms: 1.27x slower                                                          |
| gc_traversal              | 4.48 ms                                                      | 5.82 ms: 1.30x slower                                                          |
| async_generators          | 364 ms                                                       | 475 ms: 1.31x slower                                                           |
| bench_mp_pool             | 4.82 ms                                                      | 1.37 sec: 285.35x slower                                                       |
| Geometric mean            | (ref)                                                        | 1.06x slower                                                                   |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_none_tg, spectral_norm, coroutines, fannkuch, regex_compile, xml_etree_parse, async_tree_io
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241122-3.14.0a2+-a8a4ed3-JIT/bm-20241122-pythonperf2-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.003x slower
# HPT report

- Reliability score: 67.29% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x