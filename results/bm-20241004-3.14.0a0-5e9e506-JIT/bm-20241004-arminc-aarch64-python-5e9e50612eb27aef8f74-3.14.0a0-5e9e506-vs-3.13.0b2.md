# Results vs. 3.13.0b2

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: linux-aarch64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.15x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 385 ms: 1.26x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.72 sec: 1.20x slower                                                  |
| html5lib       | 66.1 ms                                                      | 71.9 ms: 1.09x slower                                                   |
| tornado_http   | 128 ms                                                       | 145 ms: 1.13x slower                                                    |
| Geometric mean | (ref)                                                        | 1.17x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 424 ms: 1.12x faster                                                    |
| async_tree_none            | 492 ms                                                       | 444 ms: 1.11x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 588 ms: 1.10x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.09x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 561 ms: 1.08x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 763 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 743 ms: 1.03x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.08x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 111 ms: 1.02x faster                                                    |
| float          | 91.4 ms                                                      | 89.8 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 253 ms: 1.02x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.91 ms: 1.01x faster                                                   |
| regex_v8       | 31.1 ms                                                      | 31.4 ms: 1.01x slower                                                   |
| regex_compile  | 128 ms                                                       | 185 ms: 1.44x slower                                                    |
| Geometric mean | (ref)                                                        | 1.09x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_loads           | 32.1 us                                                      | 31.1 us: 1.03x faster                                                   |
| unpickle             | 19.8 us                                                      | 19.2 us: 1.03x faster                                                   |
| unpickle_list        | 6.52 us                                                      | 6.33 us: 1.03x faster                                                   |
| pickle_list          | 5.27 us                                                      | 5.21 us: 1.01x faster                                                   |
| xml_etree_generate   | 114 ms                                                       | 113 ms: 1.01x faster                                                    |
| xml_etree_iterparse  | 147 ms                                                       | 148 ms: 1.01x slower                                                    |
| pickle               | 13.4 us                                                      | 13.7 us: 1.02x slower                                                   |
| xml_etree_process    | 80.8 ms                                                      | 82.5 ms: 1.02x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| unpickle_pure_python | 251 us                                                       | 264 us: 1.05x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 397 us: 1.11x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_parse, json_dumps, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.73 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 13.0 ms: 1.01x faster                                                   |
| django_template | 42.3 ms                                                      | 51.0 ms: 1.21x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 34.9 ms: 1.27x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 84.1 ms: 1.39x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.21x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 38.3 us: 1.33x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 424 ms: 1.12x faster                                                    |
| deepcopy                   | 448 us                                                       | 402 us: 1.11x faster                                                    |
| async_tree_none            | 492 ms                                                       | 444 ms: 1.11x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 588 ms: 1.10x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.09x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 561 ms: 1.08x faster                                                    |
| telco                      | 10.0 ms                                                      | 9.41 ms: 1.07x faster                                                   |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                                  |
| scimark_sor                | 159 ms                                                       | 152 ms: 1.05x faster                                                    |
| pathlib                    | 22.8 ms                                                      | 21.9 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 763 ms: 1.04x faster                                                    |
| json_loads                 | 32.1 us                                                      | 31.1 us: 1.03x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 5.02 ms: 1.03x faster                                                   |
| sqlite_synth               | 3.90 us                                                      | 3.78 us: 1.03x faster                                                   |
| unpickle                   | 19.8 us                                                      | 19.2 us: 1.03x faster                                                   |
| unpickle_list              | 6.52 us                                                      | 6.33 us: 1.03x faster                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 743 ms: 1.03x faster                                                    |
| json                       | 5.64 ms                                                      | 5.50 ms: 1.03x faster                                                   |
| nbody                      | 114 ms                                                       | 111 ms: 1.02x faster                                                    |
| create_gc_cycles           | 2.33 ms                                                      | 2.28 ms: 1.02x faster                                                   |
| regex_dna                  | 259 ms                                                       | 253 ms: 1.02x faster                                                    |
| logging_silent             | 133 ns                                                       | 131 ns: 1.02x faster                                                    |
| float                      | 91.4 ms                                                      | 89.8 ms: 1.02x faster                                                   |
| coroutines                 | 29.0 ms                                                      | 28.6 ms: 1.01x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.91 ms: 1.01x faster                                                   |
| pickle_list                | 5.27 us                                                      | 5.21 us: 1.01x faster                                                   |
| mako                       | 13.2 ms                                                      | 13.0 ms: 1.01x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 113 ms: 1.01x faster                                                    |
| coverage                   | 98.4 ms                                                      | 97.8 ms: 1.01x faster                                                   |
| asyncio_websockets         | 657 ms                                                       | 663 ms: 1.01x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                       | 148 ms: 1.01x slower                                                    |
| scimark_fft                | 445 ms                                                       | 449 ms: 1.01x slower                                                    |
| regex_v8                   | 31.1 ms                                                      | 31.4 ms: 1.01x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 8.73 ms: 1.02x slower                                                   |
| pickle                     | 13.4 us                                                      | 13.7 us: 1.02x slower                                                   |
| xml_etree_process          | 80.8 ms                                                      | 82.5 ms: 1.02x slower                                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 5.99 sec: 1.03x slower                                                  |
| tomli_loads                | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.29 sec: 1.04x slower                                                  |
| async_generators           | 488 ms                                                       | 507 ms: 1.04x slower                                                    |
| spectral_norm              | 141 ms                                                       | 147 ms: 1.04x slower                                                    |
| logging_simple             | 7.21 us                                                      | 7.51 us: 1.04x slower                                                   |
| mdp                        | 3.33 sec                                                     | 3.48 sec: 1.04x slower                                                  |
| unpickle_pure_python       | 251 us                                                       | 264 us: 1.05x slower                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.91 ms: 1.05x slower                                                   |
| logging_format             | 7.82 us                                                      | 8.27 us: 1.06x slower                                                   |
| scimark_lu                 | 141 ms                                                       | 150 ms: 1.06x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 628 ms: 1.08x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 208 us: 1.08x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 71.9 ms: 1.09x slower                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.37 ms: 1.09x slower                                                   |
| scimark_monte_carlo        | 82.3 ms                                                      | 89.9 ms: 1.09x slower                                                   |
| meteor_contest             | 113 ms                                                       | 124 ms: 1.09x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 90.1 ms: 1.10x slower                                                   |
| pickle_pure_python         | 359 us                                                       | 397 us: 1.11x slower                                                    |
| fannkuch                   | 451 ms                                                       | 505 ms: 1.12x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 4.35 ms: 1.12x slower                                                   |
| tornado_http               | 128 ms                                                       | 145 ms: 1.13x slower                                                    |
| pyflate                    | 557 ms                                                       | 638 ms: 1.15x slower                                                    |
| richards                   | 55.9 ms                                                      | 64.1 ms: 1.15x slower                                                   |
| richards_super             | 62.3 ms                                                      | 71.8 ms: 1.15x slower                                                   |
| go                         | 161 ms                                                       | 186 ms: 1.16x slower                                                    |
| raytrace                   | 297 ms                                                       | 349 ms: 1.18x slower                                                    |
| comprehensions             | 20.5 us                                                      | 24.5 us: 1.19x slower                                                   |
| docutils                   | 3.10 sec                                                     | 3.72 sec: 1.20x slower                                                  |
| sqlglot_parse              | 1.42 ms                                                      | 1.71 ms: 1.20x slower                                                   |
| sqlglot_normalize          | 129 ms                                                       | 156 ms: 1.20x slower                                                    |
| django_template            | 42.3 ms                                                      | 51.0 ms: 1.21x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 1.49 sec: 1.22x slower                                                  |
| 2to3                       | 305 ms                                                       | 385 ms: 1.26x slower                                                    |
| nqueens                    | 98.9 ms                                                      | 125 ms: 1.26x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 34.9 ms: 1.27x slower                                                   |
| sympy_expand               | 457 ms                                                       | 587 ms: 1.28x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 2.20 ms: 1.29x slower                                                   |
| chaos                      | 68.3 ms                                                      | 88.8 ms: 1.30x slower                                                   |
| sqlglot_optimize           | 62.6 ms                                                      | 82.1 ms: 1.31x slower                                                   |
| pprint_safe_repr           | 933 ms                                                       | 1.25 sec: 1.34x slower                                                  |
| pprint_pformat             | 1.93 sec                                                     | 2.61 sec: 1.35x slower                                                  |
| sympy_str                  | 265 ms                                                       | 363 ms: 1.37x slower                                                    |
| dulwich_log                | 58.5 ms                                                      | 80.8 ms: 1.38x slower                                                   |
| genshi_xml                 | 60.4 ms                                                      | 84.1 ms: 1.39x slower                                                   |
| sympy_integrate            | 20.9 ms                                                      | 29.2 ms: 1.40x slower                                                   |
| hexiom                     | 7.08 ms                                                      | 10.1 ms: 1.42x slower                                                   |
| regex_compile              | 128 ms                                                       | 185 ms: 1.44x slower                                                    |
| pylint                     | 337 ms                                                       | 487 ms: 1.45x slower                                                    |
| sympy_sum                  | 144 ms                                                       | 215 ms: 1.50x slower                                                    |
| generators                 | 37.1 ms                                                      | 59.5 ms: 1.60x slower                                                   |
| bench_mp_pool              | 7.03 ms                                                      | 2.04 sec: 290.62x slower                                                |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                            |

Benchmark hidden because not significant (7): xml_etree_parse, deepcopy_reduce, pidigits, python_startup, json_dumps, pickle_dict, thrift
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.06x