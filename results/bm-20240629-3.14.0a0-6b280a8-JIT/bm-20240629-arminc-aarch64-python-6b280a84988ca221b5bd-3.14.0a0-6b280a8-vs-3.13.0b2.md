# Results vs. 3.13.0b2

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: linux-aarch64
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 360 ms: 1.18x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.53 sec: 1.14x slower                                                  |
| html5lib       | 66.1 ms                                                      | 71.9 ms: 1.09x slower                                                   |
| tornado_http   | 128 ms                                                       | 137 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                        | 1.12x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 403 ms: 1.18x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.10 sec: 1.16x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.14x faster                                                  |
| async_tree_memoization     | 645 ms                                                       | 569 ms: 1.13x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 534 ms: 1.13x faster                                                    |
| async_tree_none            | 492 ms                                                       | 443 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 731 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 714 ms: 1.07x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.13x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 89.4 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 251 ms: 1.03x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.87 ms: 1.02x faster                                                   |
| regex_compile  | 128 ms                                                       | 173 ms: 1.35x slower                                                    |
| Geometric mean | (ref)                                                        | 1.06x slower                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_process    | 80.8 ms                                                      | 79.0 ms: 1.02x faster                                                   |
| xml_etree_generate   | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| tomli_loads          | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                  |
| xml_etree_iterparse  | 147 ms                                                       | 150 ms: 1.02x slower                                                    |
| json_dumps           | 13.1 ms                                                      | 13.4 ms: 1.03x slower                                                   |
| json_loads           | 32.1 us                                                      | 33.4 us: 1.04x slower                                                   |
| unpickle_pure_python | 251 us                                                       | 278 us: 1.11x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 397 us: 1.11x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 15.6 ms: 1.20x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 11.0 ms: 1.28x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.24x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 50.8 ms: 1.20x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 33.6 ms: 1.22x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 80.1 ms: 1.33x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.18x slower                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 38.9 us: 1.30x faster                                                   |
| deepcopy                   | 448 us                                                       | 375 us: 1.20x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 403 ms: 1.18x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.10 sec: 1.16x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.14x faster                                                  |
| async_tree_memoization     | 645 ms                                                       | 569 ms: 1.13x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 534 ms: 1.13x faster                                                    |
| async_tree_none            | 492 ms                                                       | 443 ms: 1.11x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 731 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 714 ms: 1.07x faster                                                    |
| regex_dna                  | 259 ms                                                       | 251 ms: 1.03x faster                                                    |
| pathlib                    | 22.8 ms                                                      | 22.1 ms: 1.03x faster                                                   |
| xml_etree_process          | 80.8 ms                                                      | 79.0 ms: 1.02x faster                                                   |
| float                      | 91.4 ms                                                      | 89.4 ms: 1.02x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.87 ms: 1.02x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 5.15 ms: 1.01x faster                                                   |
| logging_format             | 7.82 us                                                      | 7.90 us: 1.01x slower                                                   |
| coverage                   | 98.4 ms                                                      | 100 ms: 1.02x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                  |
| xml_etree_iterparse        | 147 ms                                                       | 150 ms: 1.02x slower                                                    |
| meteor_contest             | 113 ms                                                       | 116 ms: 1.02x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.4 ms: 1.03x slower                                                   |
| coroutines                 | 29.0 ms                                                      | 29.8 ms: 1.03x slower                                                   |
| telco                      | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                   |
| logging_silent             | 133 ns                                                       | 138 ns: 1.03x slower                                                    |
| scimark_fft                | 445 ms                                                       | 461 ms: 1.04x slower                                                    |
| bpe_tokeniser              | 5.83 sec                                                     | 6.04 sec: 1.04x slower                                                  |
| mdp                        | 3.33 sec                                                     | 3.46 sec: 1.04x slower                                                  |
| json_loads                 | 32.1 us                                                      | 33.4 us: 1.04x slower                                                   |
| spectral_norm              | 141 ms                                                       | 147 ms: 1.04x slower                                                    |
| json                       | 5.64 ms                                                      | 5.88 ms: 1.04x slower                                                   |
| async_generators           | 488 ms                                                       | 510 ms: 1.04x slower                                                    |
| dask                       | 370 ms                                                       | 387 ms: 1.05x slower                                                    |
| fannkuch                   | 451 ms                                                       | 472 ms: 1.05x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.32 ms: 1.05x slower                                                   |
| crypto_pyaes               | 82.0 ms                                                      | 86.3 ms: 1.05x slower                                                   |
| generators                 | 37.1 ms                                                      | 39.3 ms: 1.06x slower                                                   |
| scimark_monte_carlo        | 82.3 ms                                                      | 87.5 ms: 1.06x slower                                                   |
| asyncio_tcp                | 584 ms                                                       | 623 ms: 1.07x slower                                                    |
| tornado_http               | 128 ms                                                       | 137 ms: 1.07x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 207 us: 1.07x slower                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 7.03 ms: 1.07x slower                                                   |
| html5lib                   | 66.1 ms                                                      | 71.9 ms: 1.09x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 1.34 sec: 1.10x slower                                                  |
| raytrace                   | 297 ms                                                       | 325 ms: 1.10x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 142 ms: 1.10x slower                                                    |
| scimark_sor                | 159 ms                                                       | 176 ms: 1.10x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 278 us: 1.11x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 397 us: 1.11x slower                                                    |
| sqlglot_parse              | 1.42 ms                                                      | 1.58 ms: 1.11x slower                                                   |
| pyflate                    | 557 ms                                                       | 618 ms: 1.11x slower                                                    |
| go                         | 161 ms                                                       | 179 ms: 1.11x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 70.1 ms: 1.12x slower                                                   |
| docutils                   | 3.10 sec                                                     | 3.53 sec: 1.14x slower                                                  |
| comprehensions             | 20.5 us                                                      | 23.4 us: 1.14x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 1.99 ms: 1.16x slower                                                   |
| sympy_expand               | 457 ms                                                       | 534 ms: 1.17x slower                                                    |
| nqueens                    | 98.9 ms                                                      | 116 ms: 1.18x slower                                                    |
| 2to3                       | 305 ms                                                       | 360 ms: 1.18x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 4.61 ms: 1.19x slower                                                   |
| sympy_str                  | 265 ms                                                       | 316 ms: 1.19x slower                                                    |
| django_template            | 42.3 ms                                                      | 50.8 ms: 1.20x slower                                                   |
| python_startup             | 13.0 ms                                                      | 15.6 ms: 1.20x slower                                                   |
| sympy_integrate            | 20.9 ms                                                      | 25.3 ms: 1.21x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 8.57 ms: 1.22x slower                                                   |
| pprint_safe_repr           | 933 ms                                                       | 1.14 sec: 1.22x slower                                                  |
| pylint                     | 337 ms                                                       | 412 ms: 1.22x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 33.6 ms: 1.22x slower                                                   |
| pprint_pformat             | 1.93 sec                                                     | 2.38 sec: 1.23x slower                                                  |
| dulwich_log                | 58.5 ms                                                      | 73.1 ms: 1.25x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 180 ms: 1.25x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 8.99 ms: 1.27x slower                                                   |
| chaos                      | 68.3 ms                                                      | 87.0 ms: 1.27x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 11.0 ms: 1.28x slower                                                   |
| scimark_lu                 | 141 ms                                                       | 183 ms: 1.29x slower                                                    |
| genshi_xml                 | 60.4 ms                                                      | 80.1 ms: 1.33x slower                                                   |
| regex_compile              | 128 ms                                                       | 173 ms: 1.35x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                            |

Benchmark hidden because not significant (13): regex_v8, richards, richards_super, xml_etree_parse, asyncio_tcp_ssl, thrift, mako, pidigits, asyncio_websockets, nbody, create_gc_cycles, deepcopy_reduce, logging_simple
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.10x