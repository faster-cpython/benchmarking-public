# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_compact
- machine: linux-aarch64
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 366 ms: 1.20x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.56 sec: 1.15x slower                                                  |
| html5lib       | 66.1 ms                                                      | 71.1 ms: 1.08x slower                                                   |
| tornado_http   | 128 ms                                                       | 138 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                        | 1.13x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.20 sec: 1.06x faster                                                  |
| async_tree_none            | 492 ms                                                       | 505 ms: 1.03x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 813 ms: 1.03x slower                                                    |
| async_tree_memoization     | 645 ms                                                       | 664 ms: 1.03x slower                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 793 ms: 1.04x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 88.2 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                                   |
| regex_effbot   | 4.98 ms                                                      | 4.90 ms: 1.02x faster                                                   |
| regex_compile  | 128 ms                                                       | 171 ms: 1.34x slower                                                    |
| Geometric mean | (ref)                                                        | 1.06x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle             | 19.8 us                                                      | 19.5 us: 1.01x faster                                                   |
| pickle_list          | 5.27 us                                                      | 5.24 us: 1.01x faster                                                   |
| json_dumps           | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.61 sec: 1.01x slower                                                  |
| json_loads           | 32.1 us                                                      | 32.6 us: 1.01x slower                                                   |
| pickle               | 13.4 us                                                      | 13.6 us: 1.02x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 150 ms: 1.02x slower                                                    |
| unpickle_list        | 6.52 us                                                      | 6.73 us: 1.03x slower                                                   |
| pickle_pure_python   | 359 us                                                       | 392 us: 1.09x slower                                                    |
| unpickle_pure_python | 251 us                                                       | 278 us: 1.11x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, pickle_dict, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 15.5 ms: 1.19x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 11.1 ms: 1.29x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.24x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 50.2 ms: 1.19x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 33.8 ms: 1.23x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 78.6 ms: 1.30x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.17x slower                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 38.7 us: 1.31x faster                                                   |
| deepcopy                   | 448 us                                                       | 373 us: 1.20x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.20 sec: 1.06x faster                                                  |
| gc_traversal               | 5.17 ms                                                      | 4.92 ms: 1.05x faster                                                   |
| float                      | 91.4 ms                                                      | 88.2 ms: 1.04x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                                   |
| pathlib                    | 22.8 ms                                                      | 22.2 ms: 1.03x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.90 ms: 1.02x faster                                                   |
| sqlite_synth               | 3.90 us                                                      | 3.85 us: 1.01x faster                                                   |
| unpickle                   | 19.8 us                                                      | 19.5 us: 1.01x faster                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.19 sec: 1.01x faster                                                  |
| pickle_list                | 5.27 us                                                      | 5.24 us: 1.01x faster                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 4.08 us: 1.01x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.61 sec: 1.01x slower                                                  |
| json_loads                 | 32.1 us                                                      | 32.6 us: 1.01x slower                                                   |
| meteor_contest             | 113 ms                                                       | 115 ms: 1.02x slower                                                    |
| pickle                     | 13.4 us                                                      | 13.6 us: 1.02x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 150 ms: 1.02x slower                                                    |
| scimark_fft                | 445 ms                                                       | 456 ms: 1.02x slower                                                    |
| json                       | 5.64 ms                                                      | 5.79 ms: 1.03x slower                                                   |
| async_tree_none            | 492 ms                                                       | 505 ms: 1.03x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 813 ms: 1.03x slower                                                    |
| async_tree_memoization     | 645 ms                                                       | 664 ms: 1.03x slower                                                    |
| bpe_tokeniser              | 5.83 sec                                                     | 6.00 sec: 1.03x slower                                                  |
| unpickle_list              | 6.52 us                                                      | 6.73 us: 1.03x slower                                                   |
| logging_silent             | 133 ns                                                       | 138 ns: 1.03x slower                                                    |
| mdp                        | 3.33 sec                                                     | 3.45 sec: 1.04x slower                                                  |
| fannkuch                   | 451 ms                                                       | 469 ms: 1.04x slower                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 793 ms: 1.04x slower                                                    |
| telco                      | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                                   |
| async_generators           | 488 ms                                                       | 510 ms: 1.04x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.31 ms: 1.04x slower                                                   |
| scimark_monte_carlo        | 82.3 ms                                                      | 86.1 ms: 1.05x slower                                                   |
| crypto_pyaes               | 82.0 ms                                                      | 85.9 ms: 1.05x slower                                                   |
| generators                 | 37.1 ms                                                      | 39.2 ms: 1.05x slower                                                   |
| dask                       | 370 ms                                                       | 392 ms: 1.06x slower                                                    |
| spectral_norm              | 141 ms                                                       | 150 ms: 1.06x slower                                                    |
| coverage                   | 98.4 ms                                                      | 105 ms: 1.06x slower                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 7.50 ms: 1.07x slower                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 7.04 ms: 1.07x slower                                                   |
| html5lib                   | 66.1 ms                                                      | 71.1 ms: 1.08x slower                                                   |
| tornado_http               | 128 ms                                                       | 138 ms: 1.08x slower                                                    |
| raytrace                   | 297 ms                                                       | 321 ms: 1.08x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 211 us: 1.09x slower                                                    |
| scimark_sor                | 159 ms                                                       | 174 ms: 1.09x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 392 us: 1.09x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 1.34 sec: 1.10x slower                                                  |
| go                         | 161 ms                                                       | 176 ms: 1.10x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 142 ms: 1.10x slower                                                    |
| pyflate                    | 557 ms                                                       | 614 ms: 1.10x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 278 us: 1.11x slower                                                    |
| sqlglot_parse              | 1.42 ms                                                      | 1.58 ms: 1.11x slower                                                   |
| sqlglot_optimize           | 62.6 ms                                                      | 69.8 ms: 1.11x slower                                                   |
| comprehensions             | 20.5 us                                                      | 23.0 us: 1.12x slower                                                   |
| deltablue                  | 3.88 ms                                                      | 4.43 ms: 1.14x slower                                                   |
| docutils                   | 3.10 sec                                                     | 3.56 sec: 1.15x slower                                                  |
| nqueens                    | 98.9 ms                                                      | 116 ms: 1.17x slower                                                    |
| dulwich_log                | 58.5 ms                                                      | 68.8 ms: 1.18x slower                                                   |
| sympy_expand               | 457 ms                                                       | 538 ms: 1.18x slower                                                    |
| django_template            | 42.3 ms                                                      | 50.2 ms: 1.19x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 2.03 ms: 1.19x slower                                                   |
| pprint_safe_repr           | 933 ms                                                       | 1.11 sec: 1.19x slower                                                  |
| python_startup             | 13.0 ms                                                      | 15.5 ms: 1.19x slower                                                   |
| pprint_pformat             | 1.93 sec                                                     | 2.31 sec: 1.20x slower                                                  |
| 2to3                       | 305 ms                                                       | 366 ms: 1.20x slower                                                    |
| sympy_str                  | 265 ms                                                       | 323 ms: 1.22x slower                                                    |
| pylint                     | 337 ms                                                       | 414 ms: 1.23x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 33.8 ms: 1.23x slower                                                   |
| sympy_integrate            | 20.9 ms                                                      | 25.8 ms: 1.24x slower                                                   |
| chaos                      | 68.3 ms                                                      | 85.6 ms: 1.25x slower                                                   |
| hexiom                     | 7.08 ms                                                      | 8.94 ms: 1.26x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 182 ms: 1.27x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 11.1 ms: 1.29x slower                                                   |
| scimark_lu                 | 141 ms                                                       | 184 ms: 1.30x slower                                                    |
| genshi_xml                 | 60.4 ms                                                      | 78.6 ms: 1.30x slower                                                   |
| regex_compile              | 128 ms                                                       | 171 ms: 1.34x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                            |

Benchmark hidden because not significant (20): xml_etree_parse, asyncio_tcp, richards, logging_format, async_tree_none_tg, logging_simple, coroutines, xml_etree_process, regex_dna, thrift, mako, pidigits, nbody, richards_super, pickle_dict, asyncio_websockets, async_tree_io, async_tree_memoization_tg, create_gc_cycles, xml_etree_generate
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.10x