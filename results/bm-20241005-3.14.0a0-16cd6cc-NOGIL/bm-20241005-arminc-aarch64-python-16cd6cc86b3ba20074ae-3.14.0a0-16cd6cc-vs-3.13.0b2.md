# Results vs. 3.13.0b2

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-aarch64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.52x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 509 ms: 1.67x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.93 sec: 1.27x slower                                                  |
| html5lib       | 66.1 ms                                                      | 119 ms: 1.80x slower                                                    |
| tornado_http   | 128 ms                                                       | 202 ms: 1.58x slower                                                    |
| Geometric mean | (ref)                                                        | 1.57x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.33 sec: 1.05x slower                                                  |
| async_tree_memoization     | 645 ms                                                       | 730 ms: 1.13x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 895 ms: 1.13x slower                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 865 ms: 1.13x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 692 ms: 1.14x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.40 sec: 1.15x slower                                                  |
| async_tree_none_tg         | 476 ms                                                       | 568 ms: 1.19x slower                                                    |
| async_tree_none            | 492 ms                                                       | 623 ms: 1.27x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 204 ms: 2.23x slower                                                    |
| nbody          | 114 ms                                                       | 279 ms: 2.44x slower                                                    |
| Geometric mean | (ref)                                                        | 1.76x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.98 ms                                                      | 4.44 ms: 1.12x faster                                                   |
| regex_v8       | 31.1 ms                                                      | 33.2 ms: 1.07x slower                                                   |
| regex_compile  | 128 ms                                                       | 244 ms: 1.91x slower                                                    |
| Geometric mean | (ref)                                                        | 1.16x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 191 ms                                                       | 184 ms: 1.04x faster                                                    |
| pickle_list          | 5.27 us                                                      | 5.30 us: 1.00x slower                                                   |
| pickle_dict          | 37.6 us                                                      | 39.2 us: 1.04x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 156 ms: 1.07x slower                                                    |
| unpickle             | 19.8 us                                                      | 21.4 us: 1.08x slower                                                   |
| unpickle_list        | 6.52 us                                                      | 7.10 us: 1.09x slower                                                   |
| json_loads           | 32.1 us                                                      | 37.3 us: 1.16x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 17.4 ms: 1.33x slower                                                   |
| xml_etree_generate   | 114 ms                                                       | 157 ms: 1.38x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 4.12 sec: 1.60x slower                                                  |
| xml_etree_process    | 80.8 ms                                                      | 130 ms: 1.60x slower                                                    |
| unpickle_pure_python | 251 us                                                       | 522 us: 2.08x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 751 us: 2.09x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.27x slower                                                            |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 11.9 ms: 1.39x slower                                                   |
| python_startup         | 13.0 ms                                                      | 18.0 ms: 1.39x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.39x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.4 ms                                                      | 100 ms: 1.66x slower                                                    |
| genshi_text     | 27.4 ms                                                      | 50.4 ms: 1.84x slower                                                   |
| django_template | 42.3 ms                                                      | 80.7 ms: 1.91x slower                                                   |
| mako            | 13.2 ms                                                      | 28.4 ms: 2.16x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.88x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 5.17 ms                                                      | 3.47 ms: 1.49x faster                                                   |
| create_gc_cycles           | 2.33 ms                                                      | 1.62 ms: 1.44x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.44 ms: 1.12x faster                                                   |
| xml_etree_parse            | 191 ms                                                       | 184 ms: 1.04x faster                                                    |
| pickle_list                | 5.27 us                                                      | 5.30 us: 1.00x slower                                                   |
| sqlite_synth               | 3.90 us                                                      | 3.94 us: 1.01x slower                                                   |
| asyncio_websockets         | 657 ms                                                       | 672 ms: 1.02x slower                                                    |
| pickle_dict                | 37.6 us                                                      | 39.2 us: 1.04x slower                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.33 sec: 1.05x slower                                                  |
| xml_etree_iterparse        | 147 ms                                                       | 156 ms: 1.07x slower                                                    |
| regex_v8                   | 31.1 ms                                                      | 33.2 ms: 1.07x slower                                                   |
| unpickle                   | 19.8 us                                                      | 21.4 us: 1.08x slower                                                   |
| unpickle_list              | 6.52 us                                                      | 7.10 us: 1.09x slower                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.47 sec: 1.12x slower                                                  |
| asyncio_tcp                | 584 ms                                                       | 653 ms: 1.12x slower                                                    |
| async_tree_memoization     | 645 ms                                                       | 730 ms: 1.13x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 895 ms: 1.13x slower                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 865 ms: 1.13x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 692 ms: 1.14x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.40 sec: 1.15x slower                                                  |
| pathlib                    | 22.8 ms                                                      | 26.4 ms: 1.16x slower                                                   |
| json_loads                 | 32.1 us                                                      | 37.3 us: 1.16x slower                                                   |
| json                       | 5.64 ms                                                      | 6.65 ms: 1.18x slower                                                   |
| deepcopy                   | 448 us                                                       | 528 us: 1.18x slower                                                    |
| async_tree_none_tg         | 476 ms                                                       | 568 ms: 1.19x slower                                                    |
| telco                      | 10.0 ms                                                      | 12.4 ms: 1.24x slower                                                   |
| scimark_fft                | 445 ms                                                       | 560 ms: 1.26x slower                                                    |
| async_tree_none            | 492 ms                                                       | 623 ms: 1.27x slower                                                    |
| docutils                   | 3.10 sec                                                     | 3.93 sec: 1.27x slower                                                  |
| mdp                        | 3.33 sec                                                     | 4.26 sec: 1.28x slower                                                  |
| coverage                   | 98.4 ms                                                      | 129 ms: 1.31x slower                                                    |
| deepcopy_memo              | 50.8 us                                                      | 67.1 us: 1.32x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 17.4 ms: 1.33x slower                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 8.70 ms: 1.33x slower                                                   |
| async_generators           | 488 ms                                                       | 658 ms: 1.35x slower                                                    |
| coroutines                 | 29.0 ms                                                      | 39.2 ms: 1.35x slower                                                   |
| xml_etree_generate         | 114 ms                                                       | 157 ms: 1.38x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 11.9 ms: 1.39x slower                                                   |
| python_startup             | 13.0 ms                                                      | 18.0 ms: 1.39x slower                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 5.71 us: 1.41x slower                                                   |
| meteor_contest             | 113 ms                                                       | 167 ms: 1.47x slower                                                    |
| pylint                     | 337 ms                                                       | 498 ms: 1.48x slower                                                    |
| nqueens                    | 98.9 ms                                                      | 149 ms: 1.51x slower                                                    |
| generators                 | 37.1 ms                                                      | 57.3 ms: 1.54x slower                                                   |
| spectral_norm              | 141 ms                                                       | 220 ms: 1.56x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.98 ms: 1.57x slower                                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 9.20 sec: 1.58x slower                                                  |
| tornado_http               | 128 ms                                                       | 202 ms: 1.58x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 4.12 sec: 1.60x slower                                                  |
| xml_etree_process          | 80.8 ms                                                      | 130 ms: 1.60x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 2.01 sec: 1.64x slower                                                  |
| fannkuch                   | 451 ms                                                       | 743 ms: 1.65x slower                                                    |
| dulwich_log                | 58.5 ms                                                      | 96.8 ms: 1.65x slower                                                   |
| genshi_xml                 | 60.4 ms                                                      | 100 ms: 1.66x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 322 us: 1.66x slower                                                    |
| sympy_integrate            | 20.9 ms                                                      | 34.8 ms: 1.67x slower                                                   |
| 2to3                       | 305 ms                                                       | 509 ms: 1.67x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 137 ms: 1.67x slower                                                    |
| thrift                     | 962 us                                                       | 1.62 ms: 1.68x slower                                                   |
| sqlglot_normalize          | 129 ms                                                       | 218 ms: 1.69x slower                                                    |
| pprint_pformat             | 1.93 sec                                                     | 3.40 sec: 1.76x slower                                                  |
| sqlglot_optimize           | 62.6 ms                                                      | 111 ms: 1.78x slower                                                    |
| pprint_safe_repr           | 933 ms                                                       | 1.66 sec: 1.78x slower                                                  |
| pyflate                    | 557 ms                                                       | 1.00 sec: 1.80x slower                                                  |
| html5lib                   | 66.1 ms                                                      | 119 ms: 1.80x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 50.4 ms: 1.84x slower                                                   |
| sympy_str                  | 265 ms                                                       | 503 ms: 1.89x slower                                                    |
| django_template            | 42.3 ms                                                      | 80.7 ms: 1.91x slower                                                   |
| regex_compile              | 128 ms                                                       | 244 ms: 1.91x slower                                                    |
| logging_format             | 7.82 us                                                      | 15.0 us: 1.91x slower                                                   |
| logging_simple             | 7.21 us                                                      | 13.8 us: 1.92x slower                                                   |
| comprehensions             | 20.5 us                                                      | 40.3 us: 1.96x slower                                                   |
| sympy_expand               | 457 ms                                                       | 926 ms: 2.02x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 522 us: 2.08x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 751 us: 2.09x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 173 ms: 2.10x slower                                                    |
| logging_silent             | 133 ns                                                       | 281 ns: 2.10x slower                                                    |
| scimark_sor                | 159 ms                                                       | 336 ms: 2.11x slower                                                    |
| richards                   | 55.9 ms                                                      | 118 ms: 2.12x slower                                                    |
| sympy_sum                  | 144 ms                                                       | 309 ms: 2.15x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 15.3 ms: 2.16x slower                                                   |
| mako                       | 13.2 ms                                                      | 28.4 ms: 2.16x slower                                                   |
| richards_super             | 62.3 ms                                                      | 136 ms: 2.18x slower                                                    |
| float                      | 91.4 ms                                                      | 204 ms: 2.23x slower                                                    |
| chaos                      | 68.3 ms                                                      | 157 ms: 2.30x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 326 ms: 2.31x slower                                                    |
| go                         | 161 ms                                                       | 387 ms: 2.41x slower                                                    |
| nbody                      | 114 ms                                                       | 279 ms: 2.44x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 4.26 ms: 2.49x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 3.68 ms: 2.58x slower                                                   |
| raytrace                   | 297 ms                                                       | 803 ms: 2.71x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 12.4 ms: 3.20x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 40.1 ms: 5.71x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.52x slower                                                            |

Benchmark hidden because not significant (3): regex_dna, pickle, pidigits
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241005-3.14.0a0-16cd6cc-NOGIL/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.43x
- 95% likely to have a slowdown of 1.38x
- 99% likely to have a slowdown of 1.33x

# Memory
- memory change: 1.16x