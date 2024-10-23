# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: linux-aarch64
- commit hash: 0be1ef3
- commit date: 2024-10-21
- overall geometric mean: 1.19x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 375 ms: 1.23x slower                                              |
| docutils       | 2.91 sec                                                 | 3.55 sec: 1.22x slower                                            |
| html5lib       | 64.3 ms                                                  | 72.7 ms: 1.13x slower                                             |
| tornado_http   | 131 ms                                                   | 150 ms: 1.14x slower                                              |
| Geometric mean | (ref)                                                    | 1.18x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 547 ms: 1.19x faster                                              |
| async_tree_none           | 493 ms                                                   | 473 ms: 1.04x faster                                              |
| async_tree_none_tg        | 467 ms                                                   | 453 ms: 1.03x faster                                              |
| async_tree_memoization    | 626 ms                                                   | 607 ms: 1.03x faster                                              |
| asyncio_websockets        | 656 ms                                                   | 662 ms: 1.01x slower                                              |
| coroutines                | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                             |
| async_generators          | 496 ms                                                   | 511 ms: 1.03x slower                                              |
| async_tree_io             | 1.11 sec                                                 | 1.17 sec: 1.05x slower                                            |
| async_tree_io_tg          | 1.09 sec                                                 | 1.27 sec: 1.16x slower                                            |
| Geometric mean            | (ref)                                                    | 1.00x faster                                                      |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 97.7 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                    | 1.01x slower                                                      |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_effbot   | 4.87 ms                                                  | 5.06 ms: 1.04x slower                                             |
| regex_compile  | 128 ms                                                   | 172 ms: 1.34x slower                                              |
| Geometric mean | (ref)                                                    | 1.08x slower                                                      |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_parse      | 188 ms                                                   | 189 ms: 1.01x slower                                              |
| json_loads           | 31.4 us                                                  | 31.8 us: 1.01x slower                                             |
| xml_etree_iterparse  | 147 ms                                                   | 149 ms: 1.02x slower                                              |
| tomli_loads          | 2.53 sec                                                 | 2.62 sec: 1.04x slower                                            |
| unpickle_pure_python | 254 us                                                   | 266 us: 1.05x slower                                              |
| json_dumps           | 13.4 ms                                                  | 14.2 ms: 1.07x slower                                             |
| pickle_pure_python   | 359 us                                                   | 389 us: 1.08x slower                                              |
| Geometric mean       | (ref)                                                    | 1.03x slower                                                      |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 14.6 ms: 1.10x slower                                             |
| Geometric mean | (ref)                                                    | 1.05x slower                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                             |
| django_template | 42.3 ms                                                  | 52.3 ms: 1.24x slower                                             |
| genshi_text     | 27.7 ms                                                  | 34.9 ms: 1.26x slower                                             |
| genshi_xml      | 60.2 ms                                                  | 82.5 ms: 1.37x slower                                             |
| Geometric mean  | (ref)                                                    | 1.21x slower                                                      |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3 |
|---------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------:|
| deepcopy_memo             | 51.0 us                                                  | 39.2 us: 1.30x faster                                             |
| deepcopy                  | 451 us                                                   | 374 us: 1.21x faster                                              |
| async_tree_memoization_tg | 649 ms                                                   | 547 ms: 1.19x faster                                              |
| deepcopy_reduce           | 4.07 us                                                  | 3.87 us: 1.05x faster                                             |
| async_tree_none           | 493 ms                                                   | 473 ms: 1.04x faster                                              |
| async_tree_none_tg        | 467 ms                                                   | 453 ms: 1.03x faster                                              |
| async_tree_memoization    | 626 ms                                                   | 607 ms: 1.03x faster                                              |
| pathlib                   | 22.4 ms                                                  | 21.8 ms: 1.03x faster                                             |
| logging_silent            | 135 ns                                                   | 133 ns: 1.02x faster                                              |
| telco                     | 9.73 ms                                                  | 9.56 ms: 1.02x faster                                             |
| mako                      | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                             |
| xml_etree_parse           | 188 ms                                                   | 189 ms: 1.01x slower                                              |
| asyncio_websockets        | 656 ms                                                   | 662 ms: 1.01x slower                                              |
| json_loads                | 31.4 us                                                  | 31.8 us: 1.01x slower                                             |
| scimark_fft               | 447 ms                                                   | 454 ms: 1.02x slower                                              |
| coroutines                | 28.2 ms                                                  | 28.7 ms: 1.02x slower                                             |
| xml_etree_iterparse       | 147 ms                                                   | 149 ms: 1.02x slower                                              |
| bpe_tokeniser             | 5.90 sec                                                 | 6.01 sec: 1.02x slower                                            |
| async_generators          | 496 ms                                                   | 511 ms: 1.03x slower                                              |
| thrift                    | 946 us                                                   | 974 us: 1.03x slower                                              |
| mdp                       | 3.36 sec                                                 | 3.48 sec: 1.03x slower                                            |
| float                     | 94.4 ms                                                  | 97.7 ms: 1.04x slower                                             |
| tomli_loads               | 2.53 sec                                                 | 2.62 sec: 1.04x slower                                            |
| regex_effbot              | 4.87 ms                                                  | 5.06 ms: 1.04x slower                                             |
| unpickle_pure_python      | 254 us                                                   | 266 us: 1.05x slower                                              |
| async_tree_io             | 1.11 sec                                                 | 1.17 sec: 1.05x slower                                            |
| logging_format            | 7.83 us                                                  | 8.26 us: 1.06x slower                                             |
| json_dumps                | 13.4 ms                                                  | 14.2 ms: 1.07x slower                                             |
| crypto_pyaes              | 82.7 ms                                                  | 89.3 ms: 1.08x slower                                             |
| bench_thread_pool         | 1.28 ms                                                  | 1.38 ms: 1.08x slower                                             |
| scimark_monte_carlo       | 83.8 ms                                                  | 90.6 ms: 1.08x slower                                             |
| scimark_lu                | 139 ms                                                   | 151 ms: 1.08x slower                                              |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 7.13 ms: 1.08x slower                                             |
| pickle_pure_python        | 359 us                                                   | 389 us: 1.08x slower                                              |
| logging_simple            | 7.04 us                                                  | 7.65 us: 1.09x slower                                             |
| meteor_contest            | 113 ms                                                   | 123 ms: 1.09x slower                                              |
| spectral_norm             | 141 ms                                                   | 154 ms: 1.09x slower                                              |
| python_startup            | 13.3 ms                                                  | 14.6 ms: 1.10x slower                                             |
| typing_runtime_protocols  | 192 us                                                   | 212 us: 1.11x slower                                              |
| pyflate                   | 556 ms                                                   | 616 ms: 1.11x slower                                              |
| richards_super            | 60.3 ms                                                  | 67.5 ms: 1.12x slower                                             |
| html5lib                  | 64.3 ms                                                  | 72.7 ms: 1.13x slower                                             |
| tornado_http              | 131 ms                                                   | 150 ms: 1.14x slower                                              |
| fannkuch                  | 452 ms                                                   | 515 ms: 1.14x slower                                              |
| richards                  | 53.5 ms                                                  | 61.1 ms: 1.14x slower                                             |
| go                        | 163 ms                                                   | 188 ms: 1.15x slower                                              |
| async_tree_io_tg          | 1.09 sec                                                 | 1.27 sec: 1.16x slower                                            |
| raytrace                  | 298 ms                                                   | 353 ms: 1.18x slower                                              |
| pycparser                 | 1.26 sec                                                 | 1.49 sec: 1.18x slower                                            |
| sqlglot_normalize         | 128 ms                                                   | 153 ms: 1.19x slower                                              |
| deltablue                 | 3.85 ms                                                  | 4.66 ms: 1.21x slower                                             |
| comprehensions            | 20.4 us                                                  | 24.7 us: 1.21x slower                                             |
| docutils                  | 2.91 sec                                                 | 3.55 sec: 1.22x slower                                            |
| 2to3                      | 306 ms                                                   | 375 ms: 1.23x slower                                              |
| django_template           | 42.3 ms                                                  | 52.3 ms: 1.24x slower                                             |
| sqlglot_transpile         | 1.73 ms                                                  | 2.16 ms: 1.25x slower                                             |
| sqlglot_parse             | 1.38 ms                                                  | 1.73 ms: 1.26x slower                                             |
| genshi_text               | 27.7 ms                                                  | 34.9 ms: 1.26x slower                                             |
| chaos                     | 68.8 ms                                                  | 86.8 ms: 1.26x slower                                             |
| sqlglot_optimize          | 62.4 ms                                                  | 79.9 ms: 1.28x slower                                             |
| sympy_expand              | 455 ms                                                   | 588 ms: 1.29x slower                                              |
| pprint_safe_repr          | 926 ms                                                   | 1.20 sec: 1.30x slower                                            |
| nqueens                   | 98.7 ms                                                  | 128 ms: 1.30x slower                                              |
| pylint                    | 343 ms                                                   | 458 ms: 1.33x slower                                              |
| regex_compile             | 128 ms                                                   | 172 ms: 1.34x slower                                              |
| sympy_str                 | 264 ms                                                   | 353 ms: 1.34x slower                                              |
| pprint_pformat            | 1.90 sec                                                 | 2.55 sec: 1.35x slower                                            |
| genshi_xml                | 60.2 ms                                                  | 82.5 ms: 1.37x slower                                             |
| gc_traversal              | 4.53 ms                                                  | 6.37 ms: 1.41x slower                                             |
| sympy_integrate           | 21.0 ms                                                  | 29.7 ms: 1.42x slower                                             |
| hexiom                    | 7.13 ms                                                  | 10.1 ms: 1.42x slower                                             |
| sympy_sum                 | 143 ms                                                   | 214 ms: 1.49x slower                                              |
| generators                | 37.8 ms                                                  | 60.0 ms: 1.59x slower                                             |
| create_gc_cycles          | 2.12 ms                                                  | 3.62 ms: 1.71x slower                                             |
| bench_mp_pool             | 7.30 ms                                                  | 2.50 sec: 341.95x slower                                          |
| Geometric mean            | (ref)                                                    | 1.19x slower                                                      |

Benchmark hidden because not significant (12): regex_v8, async_tree_cpu_io_mixed, xml_etree_generate, pidigits, scimark_sor, nbody, python_startup_no_site, coverage, json, regex_dna, async_tree_cpu_io_mixed_tg, xml_etree_process
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (2) of results/bm-20241021-3.14.0a1+-0be1ef3-JIT/bm-20241021-arminc-aarch64-nick%2darm-codecache-3.14.0a1+-0be1ef3.json: dulwich_log, sphinx

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.23x