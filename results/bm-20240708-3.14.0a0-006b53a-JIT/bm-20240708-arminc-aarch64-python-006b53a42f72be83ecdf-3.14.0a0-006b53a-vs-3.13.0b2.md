# Results vs. 3.13.0b2

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: linux-aarch64
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 360 ms: 1.18x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.58 sec: 1.16x slower                                                  |
| html5lib       | 66.1 ms                                                      | 69.6 ms: 1.05x slower                                                   |
| tornado_http   | 128 ms                                                       | 139 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                        | 1.12x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 409 ms: 1.16x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.10 sec: 1.15x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.14x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 538 ms: 1.12x faster                                                    |
| async_tree_none            | 492 ms                                                       | 445 ms: 1.11x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 584 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 734 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 716 ms: 1.07x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.12x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 89.9 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 248 ms: 1.04x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.85 ms: 1.03x faster                                                   |
| regex_v8       | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                                   |
| regex_compile  | 128 ms                                                       | 180 ms: 1.41x slower                                                    |
| Geometric mean | (ref)                                                        | 1.07x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_process    | 80.8 ms                                                      | 79.3 ms: 1.02x faster                                                   |
| xml_etree_generate   | 114 ms                                                       | 112 ms: 1.01x faster                                                    |
| tomli_loads          | 2.57 sec                                                     | 2.61 sec: 1.01x slower                                                  |
| json_dumps           | 13.1 ms                                                      | 13.3 ms: 1.02x slower                                                   |
| json_loads           | 32.1 us                                                      | 32.9 us: 1.02x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 150 ms: 1.03x slower                                                    |
| unpickle_pure_python | 251 us                                                       | 275 us: 1.09x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 411 us: 1.15x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.78 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 50.2 ms: 1.19x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 34.5 ms: 1.26x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 80.2 ms: 1.33x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.19x slower                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 38.4 us: 1.32x faster                                                   |
| deepcopy                   | 448 us                                                       | 372 us: 1.21x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 409 ms: 1.16x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.10 sec: 1.15x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.14x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 538 ms: 1.12x faster                                                    |
| async_tree_none            | 492 ms                                                       | 445 ms: 1.11x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 584 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 734 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 716 ms: 1.07x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 4.90 ms: 1.06x faster                                                   |
| pathlib                    | 22.8 ms                                                      | 21.8 ms: 1.04x faster                                                   |
| regex_dna                  | 259 ms                                                       | 248 ms: 1.04x faster                                                    |
| richards                   | 55.9 ms                                                      | 54.2 ms: 1.03x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.85 ms: 1.03x faster                                                   |
| xml_etree_process          | 80.8 ms                                                      | 79.3 ms: 1.02x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                                   |
| float                      | 91.4 ms                                                      | 89.9 ms: 1.02x faster                                                   |
| richards_super             | 62.3 ms                                                      | 61.3 ms: 1.02x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.01x faster                                                    |
| meteor_contest             | 113 ms                                                       | 115 ms: 1.01x slower                                                    |
| coroutines                 | 29.0 ms                                                      | 29.4 ms: 1.01x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.61 sec: 1.01x slower                                                  |
| logging_format             | 7.82 us                                                      | 7.96 us: 1.02x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.3 ms: 1.02x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 8.78 ms: 1.02x slower                                                   |
| logging_silent             | 133 ns                                                       | 137 ns: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.26 sec: 1.02x slower                                                  |
| coverage                   | 98.4 ms                                                      | 101 ms: 1.02x slower                                                    |
| json_loads                 | 32.1 us                                                      | 32.9 us: 1.02x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 150 ms: 1.03x slower                                                    |
| bpe_tokeniser              | 5.83 sec                                                     | 6.00 sec: 1.03x slower                                                  |
| json                       | 5.64 ms                                                      | 5.82 ms: 1.03x slower                                                   |
| mdp                        | 3.33 sec                                                     | 3.44 sec: 1.03x slower                                                  |
| telco                      | 10.0 ms                                                      | 10.4 ms: 1.03x slower                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 4.19 us: 1.04x slower                                                   |
| scimark_fft                | 445 ms                                                       | 463 ms: 1.04x slower                                                    |
| dask                       | 370 ms                                                       | 387 ms: 1.04x slower                                                    |
| async_generators           | 488 ms                                                       | 512 ms: 1.05x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 69.6 ms: 1.05x slower                                                   |
| generators                 | 37.1 ms                                                      | 39.2 ms: 1.05x slower                                                   |
| fannkuch                   | 451 ms                                                       | 476 ms: 1.06x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 619 ms: 1.06x slower                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.99 ms: 1.07x slower                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.35 ms: 1.07x slower                                                   |
| typing_runtime_protocols   | 193 us                                                       | 208 us: 1.07x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 88.7 ms: 1.08x slower                                                   |
| crypto_pyaes               | 82.0 ms                                                      | 88.5 ms: 1.08x slower                                                   |
| tornado_http               | 128 ms                                                       | 139 ms: 1.08x slower                                                    |
| pyflate                    | 557 ms                                                       | 608 ms: 1.09x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 275 us: 1.09x slower                                                    |
| sqlglot_optimize           | 62.6 ms                                                      | 68.6 ms: 1.09x slower                                                   |
| sqlglot_normalize          | 129 ms                                                       | 142 ms: 1.10x slower                                                    |
| raytrace                   | 297 ms                                                       | 325 ms: 1.10x slower                                                    |
| pycparser                  | 1.22 sec                                                     | 1.34 sec: 1.10x slower                                                  |
| scimark_sor                | 159 ms                                                       | 176 ms: 1.11x slower                                                    |
| sqlglot_parse              | 1.42 ms                                                      | 1.59 ms: 1.12x slower                                                   |
| go                         | 161 ms                                                       | 180 ms: 1.12x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 411 us: 1.15x slower                                                    |
| comprehensions             | 20.5 us                                                      | 23.6 us: 1.15x slower                                                   |
| deltablue                  | 3.88 ms                                                      | 4.47 ms: 1.15x slower                                                   |
| docutils                   | 3.10 sec                                                     | 3.58 sec: 1.16x slower                                                  |
| bench_mp_pool              | 7.03 ms                                                      | 8.18 ms: 1.16x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 116 ms: 1.17x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 2.02 ms: 1.18x slower                                                   |
| 2to3                       | 305 ms                                                       | 360 ms: 1.18x slower                                                    |
| sympy_expand               | 457 ms                                                       | 542 ms: 1.19x slower                                                    |
| django_template            | 42.3 ms                                                      | 50.2 ms: 1.19x slower                                                   |
| dulwich_log                | 58.5 ms                                                      | 69.4 ms: 1.19x slower                                                   |
| pylint                     | 337 ms                                                       | 405 ms: 1.20x slower                                                    |
| pprint_safe_repr           | 933 ms                                                       | 1.14 sec: 1.22x slower                                                  |
| sympy_str                  | 265 ms                                                       | 328 ms: 1.24x slower                                                    |
| pprint_pformat             | 1.93 sec                                                     | 2.39 sec: 1.24x slower                                                  |
| genshi_text                | 27.4 ms                                                      | 34.5 ms: 1.26x slower                                                   |
| sympy_integrate            | 20.9 ms                                                      | 26.4 ms: 1.27x slower                                                   |
| hexiom                     | 7.08 ms                                                      | 9.04 ms: 1.28x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 187 ms: 1.30x slower                                                    |
| scimark_lu                 | 141 ms                                                       | 184 ms: 1.30x slower                                                    |
| chaos                      | 68.3 ms                                                      | 89.6 ms: 1.31x slower                                                   |
| genshi_xml                 | 60.4 ms                                                      | 80.2 ms: 1.33x slower                                                   |
| regex_compile              | 128 ms                                                       | 180 ms: 1.41x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.06x slower                                                            |

Benchmark hidden because not significant (10): logging_simple, pidigits, python_startup, asyncio_websockets, thrift, create_gc_cycles, xml_etree_parse, nbody, mako, spectral_norm
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.08x