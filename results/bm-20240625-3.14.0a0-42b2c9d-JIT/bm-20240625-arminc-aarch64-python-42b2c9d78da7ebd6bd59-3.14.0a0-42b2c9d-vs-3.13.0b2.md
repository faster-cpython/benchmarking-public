# Results vs. 3.13.0b2

- fork: python
- ref: 42b2c9d78da7ebd6bd59
- machine: linux-aarch64
- commit hash: 42b2c9d
- commit date: 2024-06-25
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 358 ms: 1.17x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.53 sec: 1.14x slower                                                  |
| html5lib       | 66.1 ms                                                      | 71.8 ms: 1.09x slower                                                   |
| tornado_http   | 128 ms                                                       | 141 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                        | 1.12x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 410 ms: 1.16x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.14x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.14x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 547 ms: 1.11x faster                                                    |
| async_tree_none            | 492 ms                                                       | 448 ms: 1.10x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 586 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 748 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 729 ms: 1.05x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 89.0 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                                   |
| regex_compile  | 128 ms                                                       | 173 ms: 1.36x slower                                                    |
| Geometric mean | (ref)                                                        | 1.07x slower                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| pickle_list          | 5.27 us                                                      | 5.29 us: 1.00x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 149 ms: 1.01x slower                                                    |
| unpickle_list        | 6.52 us                                                      | 6.65 us: 1.02x slower                                                   |
| pickle               | 13.4 us                                                      | 13.8 us: 1.03x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 13.6 ms: 1.04x slower                                                   |
| json_loads           | 32.1 us                                                      | 33.3 us: 1.04x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.67 sec: 1.04x slower                                                  |
| pickle_pure_python   | 359 us                                                       | 393 us: 1.10x slower                                                    |
| unpickle_pure_python | 251 us                                                       | 277 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_parse, pickle_dict, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 15.6 ms: 1.20x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 11.1 ms: 1.29x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.24x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 50.2 ms: 1.19x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 34.9 ms: 1.27x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 82.5 ms: 1.37x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.20x slower                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240625-arminc-aarch64-python-42b2c9d78da7ebd6bd59-3.14.0a0-42b2c9d |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 39.7 us: 1.28x faster                                                   |
| deepcopy                   | 448 us                                                       | 377 us: 1.19x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 410 ms: 1.16x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.11 sec: 1.14x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.14x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 547 ms: 1.11x faster                                                    |
| async_tree_none            | 492 ms                                                       | 448 ms: 1.10x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 586 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 748 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 729 ms: 1.05x faster                                                    |
| regex_v8                   | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                                   |
| pathlib                    | 22.8 ms                                                      | 22.1 ms: 1.03x faster                                                   |
| float                      | 91.4 ms                                                      | 89.0 ms: 1.03x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| richards                   | 55.9 ms                                                      | 55.1 ms: 1.01x faster                                                   |
| sqlite_synth               | 3.90 us                                                      | 3.85 us: 1.01x faster                                                   |
| pickle_list                | 5.27 us                                                      | 5.29 us: 1.00x slower                                                   |
| asyncio_websockets         | 657 ms                                                       | 662 ms: 1.01x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                       | 149 ms: 1.01x slower                                                    |
| meteor_contest             | 113 ms                                                       | 116 ms: 1.02x slower                                                    |
| unpickle_list              | 6.52 us                                                      | 6.65 us: 1.02x slower                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 4.13 us: 1.02x slower                                                   |
| coroutines                 | 29.0 ms                                                      | 29.7 ms: 1.02x slower                                                   |
| coverage                   | 98.4 ms                                                      | 101 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.27 sec: 1.03x slower                                                  |
| pickle                     | 13.4 us                                                      | 13.8 us: 1.03x slower                                                   |
| scimark_fft                | 445 ms                                                       | 460 ms: 1.03x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.6 ms: 1.04x slower                                                   |
| json_loads                 | 32.1 us                                                      | 33.3 us: 1.04x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.67 sec: 1.04x slower                                                  |
| scimark_monte_carlo        | 82.3 ms                                                      | 85.5 ms: 1.04x slower                                                   |
| json                       | 5.64 ms                                                      | 5.87 ms: 1.04x slower                                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 6.08 sec: 1.04x slower                                                  |
| logging_silent             | 133 ns                                                       | 139 ns: 1.04x slower                                                    |
| generators                 | 37.1 ms                                                      | 38.8 ms: 1.04x slower                                                   |
| fannkuch                   | 451 ms                                                       | 472 ms: 1.05x slower                                                    |
| mdp                        | 3.33 sec                                                     | 3.49 sec: 1.05x slower                                                  |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.87 ms: 1.05x slower                                                   |
| telco                      | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                                   |
| crypto_pyaes               | 82.0 ms                                                      | 86.1 ms: 1.05x slower                                                   |
| dask                       | 370 ms                                                       | 390 ms: 1.05x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.32 ms: 1.05x slower                                                   |
| spectral_norm              | 141 ms                                                       | 149 ms: 1.06x slower                                                    |
| async_generators           | 488 ms                                                       | 517 ms: 1.06x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 622 ms: 1.07x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 71.8 ms: 1.09x slower                                                   |
| raytrace                   | 297 ms                                                       | 324 ms: 1.09x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 212 us: 1.09x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 393 us: 1.10x slower                                                    |
| pyflate                    | 557 ms                                                       | 613 ms: 1.10x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 277 us: 1.10x slower                                                    |
| tornado_http               | 128 ms                                                       | 141 ms: 1.10x slower                                                    |
| scimark_sor                | 159 ms                                                       | 176 ms: 1.10x slower                                                    |
| sqlglot_parse              | 1.42 ms                                                      | 1.57 ms: 1.11x slower                                                   |
| sqlglot_normalize          | 129 ms                                                       | 143 ms: 1.11x slower                                                    |
| go                         | 161 ms                                                       | 178 ms: 1.11x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 1.36 sec: 1.11x slower                                                  |
| sqlglot_optimize           | 62.6 ms                                                      | 69.9 ms: 1.12x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 7.93 ms: 1.13x slower                                                   |
| comprehensions             | 20.5 us                                                      | 23.3 us: 1.14x slower                                                   |
| docutils                   | 3.10 sec                                                     | 3.53 sec: 1.14x slower                                                  |
| deltablue                  | 3.88 ms                                                      | 4.44 ms: 1.15x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 2.00 ms: 1.17x slower                                                   |
| 2to3                       | 305 ms                                                       | 358 ms: 1.17x slower                                                    |
| nqueens                    | 98.9 ms                                                      | 117 ms: 1.19x slower                                                    |
| sympy_expand               | 457 ms                                                       | 542 ms: 1.19x slower                                                    |
| django_template            | 42.3 ms                                                      | 50.2 ms: 1.19x slower                                                   |
| dulwich_log                | 58.5 ms                                                      | 70.0 ms: 1.20x slower                                                   |
| python_startup             | 13.0 ms                                                      | 15.6 ms: 1.20x slower                                                   |
| pprint_pformat             | 1.93 sec                                                     | 2.31 sec: 1.20x slower                                                  |
| pprint_safe_repr           | 933 ms                                                       | 1.12 sec: 1.20x slower                                                  |
| sympy_str                  | 265 ms                                                       | 319 ms: 1.20x slower                                                    |
| sympy_integrate            | 20.9 ms                                                      | 25.6 ms: 1.23x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 179 ms: 1.25x slower                                                    |
| pylint                     | 337 ms                                                       | 424 ms: 1.26x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 8.91 ms: 1.26x slower                                                   |
| genshi_text                | 27.4 ms                                                      | 34.9 ms: 1.27x slower                                                   |
| chaos                      | 68.3 ms                                                      | 87.6 ms: 1.28x slower                                                   |
| scimark_lu                 | 141 ms                                                       | 182 ms: 1.28x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 11.1 ms: 1.29x slower                                                   |
| regex_compile              | 128 ms                                                       | 173 ms: 1.36x slower                                                    |
| genshi_xml                 | 60.4 ms                                                      | 82.5 ms: 1.37x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                            |

Benchmark hidden because not significant (15): gc_traversal, xml_etree_process, regex_effbot, richards_super, xml_etree_parse, pickle_dict, pidigits, mako, logging_simple, nbody, unpickle, thrift, regex_dna, logging_format, create_gc_cycles
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x