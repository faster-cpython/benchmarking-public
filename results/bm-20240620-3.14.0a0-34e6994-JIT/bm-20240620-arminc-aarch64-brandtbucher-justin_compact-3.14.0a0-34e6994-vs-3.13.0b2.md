# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_compact
- machine: linux-aarch64
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 370 ms: 1.21x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.58 sec: 1.16x slower                                                  |
| html5lib       | 66.1 ms                                                      | 71.2 ms: 1.08x slower                                                   |
| tornado_http   | 128 ms                                                       | 147 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                        | 1.15x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.21 sec: 1.05x faster                                                  |
| async_tree_none            | 492 ms                                                       | 500 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 795 ms: 1.04x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 88.2 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 248 ms: 1.04x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.85 ms: 1.03x faster                                                   |
| regex_v8       | 31.1 ms                                                      | 30.4 ms: 1.02x faster                                                   |
| regex_compile  | 128 ms                                                       | 175 ms: 1.37x slower                                                    |
| Geometric mean | (ref)                                                        | 1.06x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_process    | 80.8 ms                                                      | 79.1 ms: 1.02x faster                                                   |
| unpickle             | 19.8 us                                                      | 19.5 us: 1.01x faster                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 148 ms: 1.01x slower                                                    |
| json_dumps           | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| unpickle_list        | 6.52 us                                                      | 6.65 us: 1.02x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                  |
| json_loads           | 32.1 us                                                      | 33.2 us: 1.03x slower                                                   |
| pickle               | 13.4 us                                                      | 13.8 us: 1.03x slower                                                   |
| pickle_pure_python   | 359 us                                                       | 395 us: 1.10x slower                                                    |
| unpickle_pure_python | 251 us                                                       | 279 us: 1.11x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_parse, pickle_dict, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 15.8 ms: 1.21x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 11.2 ms: 1.30x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 49.0 ms: 1.16x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 33.5 ms: 1.22x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 79.0 ms: 1.31x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.17x slower                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240620-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 38.5 us: 1.32x faster                                                   |
| deepcopy                   | 448 us                                                       | 378 us: 1.19x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.21 sec: 1.05x faster                                                  |
| regex_dna                  | 259 ms                                                       | 248 ms: 1.04x faster                                                    |
| float                      | 91.4 ms                                                      | 88.2 ms: 1.04x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 5.01 ms: 1.03x faster                                                   |
| pathlib                    | 22.8 ms                                                      | 22.1 ms: 1.03x faster                                                   |
| sqlite_synth               | 3.90 us                                                      | 3.80 us: 1.03x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.85 ms: 1.03x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.4 ms: 1.02x faster                                                   |
| xml_etree_process          | 80.8 ms                                                      | 79.1 ms: 1.02x faster                                                   |
| richards                   | 55.9 ms                                                      | 54.8 ms: 1.02x faster                                                   |
| unpickle                   | 19.8 us                                                      | 19.5 us: 1.01x faster                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 148 ms: 1.01x slower                                                    |
| async_tree_none            | 492 ms                                                       | 500 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.25 sec: 1.02x slower                                                  |
| json_dumps                 | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| unpickle_list              | 6.52 us                                                      | 6.65 us: 1.02x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                  |
| scimark_fft                | 445 ms                                                       | 456 ms: 1.02x slower                                                    |
| logging_silent             | 133 ns                                                       | 138 ns: 1.03x slower                                                    |
| coverage                   | 98.4 ms                                                      | 102 ms: 1.03x slower                                                    |
| json_loads                 | 32.1 us                                                      | 33.2 us: 1.03x slower                                                   |
| mdp                        | 3.33 sec                                                     | 3.44 sec: 1.03x slower                                                  |
| pickle                     | 13.4 us                                                      | 13.8 us: 1.03x slower                                                   |
| scimark_monte_carlo        | 82.3 ms                                                      | 85.1 ms: 1.03x slower                                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 6.03 sec: 1.03x slower                                                  |
| fannkuch                   | 451 ms                                                       | 468 ms: 1.04x slower                                                    |
| async_generators           | 488 ms                                                       | 507 ms: 1.04x slower                                                    |
| spectral_norm              | 141 ms                                                       | 147 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 795 ms: 1.04x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 85.5 ms: 1.04x slower                                                   |
| generators                 | 37.1 ms                                                      | 38.8 ms: 1.04x slower                                                   |
| asyncio_tcp                | 584 ms                                                       | 611 ms: 1.05x slower                                                    |
| meteor_contest             | 113 ms                                                       | 119 ms: 1.05x slower                                                    |
| json                       | 5.64 ms                                                      | 5.91 ms: 1.05x slower                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.89 ms: 1.05x slower                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.33 ms: 1.05x slower                                                   |
| pyflate                    | 557 ms                                                       | 592 ms: 1.06x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 206 us: 1.07x slower                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 7.50 ms: 1.07x slower                                                   |
| dask                       | 370 ms                                                       | 396 ms: 1.07x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 71.2 ms: 1.08x slower                                                   |
| scimark_sor                | 159 ms                                                       | 174 ms: 1.09x slower                                                    |
| raytrace                   | 297 ms                                                       | 324 ms: 1.09x slower                                                    |
| go                         | 161 ms                                                       | 176 ms: 1.10x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 395 us: 1.10x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 143 ms: 1.10x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 279 us: 1.11x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 1.36 sec: 1.11x slower                                                  |
| sqlglot_parse              | 1.42 ms                                                      | 1.59 ms: 1.12x slower                                                   |
| sqlglot_optimize           | 62.6 ms                                                      | 70.0 ms: 1.12x slower                                                   |
| comprehensions             | 20.5 us                                                      | 23.0 us: 1.12x slower                                                   |
| deltablue                  | 3.88 ms                                                      | 4.41 ms: 1.14x slower                                                   |
| tornado_http               | 128 ms                                                       | 147 ms: 1.15x slower                                                    |
| docutils                   | 3.10 sec                                                     | 3.58 sec: 1.16x slower                                                  |
| django_template            | 42.3 ms                                                      | 49.0 ms: 1.16x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 2.01 ms: 1.17x slower                                                   |
| pprint_safe_repr           | 933 ms                                                       | 1.10 sec: 1.18x slower                                                  |
| pprint_pformat             | 1.93 sec                                                     | 2.30 sec: 1.19x slower                                                  |
| sympy_expand               | 457 ms                                                       | 550 ms: 1.20x slower                                                    |
| 2to3                       | 305 ms                                                       | 370 ms: 1.21x slower                                                    |
| python_startup             | 13.0 ms                                                      | 15.8 ms: 1.21x slower                                                   |
| genshi_text                | 27.4 ms                                                      | 33.5 ms: 1.22x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 122 ms: 1.23x slower                                                    |
| pylint                     | 337 ms                                                       | 418 ms: 1.24x slower                                                    |
| sympy_str                  | 265 ms                                                       | 332 ms: 1.25x slower                                                    |
| sympy_integrate            | 20.9 ms                                                      | 26.2 ms: 1.26x slower                                                   |
| chaos                      | 68.3 ms                                                      | 86.7 ms: 1.27x slower                                                   |
| hexiom                     | 7.08 ms                                                      | 9.00 ms: 1.27x slower                                                   |
| scimark_lu                 | 141 ms                                                       | 181 ms: 1.28x slower                                                    |
| dulwich_log                | 58.5 ms                                                      | 76.2 ms: 1.30x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 11.2 ms: 1.30x slower                                                   |
| genshi_xml                 | 60.4 ms                                                      | 79.0 ms: 1.31x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 188 ms: 1.31x slower                                                    |
| regex_compile              | 128 ms                                                       | 175 ms: 1.37x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.07x slower                                                            |

Benchmark hidden because not significant (21): richards_super, xml_etree_generate, xml_etree_parse, telco, thrift, pickle_dict, create_gc_cycles, deepcopy_reduce, async_tree_none_tg, mako, async_tree_memoization_tg, pidigits, coroutines, pickle_list, asyncio_websockets, logging_simple, logging_format, async_tree_cpu_io_mixed, nbody, async_tree_io, async_tree_memoization
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.10x