# Results vs. 3.13.0b2

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-aarch64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 382 ms: 1.25x slower                                                    |
| docutils       | 3.10 sec                                                     | 3.93 sec: 1.27x slower                                                  |
| html5lib       | 66.1 ms                                                      | 70.5 ms: 1.07x slower                                                   |
| tornado_http   | 128 ms                                                       | 151 ms: 1.18x slower                                                    |
| Geometric mean | (ref)                                                        | 1.19x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 645 ms                                                       | 571 ms: 1.13x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 430 ms: 1.11x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.16 sec: 1.10x faster                                                  |
| async_tree_none            | 492 ms                                                       | 451 ms: 1.09x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 558 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 743 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 720 ms: 1.06x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.19 sec: 1.03x faster                                                  |
| Geometric mean             | (ref)                                                        | 1.08x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 88.0 ms: 1.04x faster                                                   |
| nbody          | 114 ms                                                       | 116 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 246 ms: 1.05x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 30.3 ms: 1.03x faster                                                   |
| regex_effbot   | 4.98 ms                                                      | 4.87 ms: 1.02x faster                                                   |
| regex_compile  | 128 ms                                                       | 194 ms: 1.51x slower                                                    |
| Geometric mean | (ref)                                                        | 1.08x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_process    | 80.8 ms                                                      | 79.4 ms: 1.02x faster                                                   |
| xml_etree_iterparse  | 147 ms                                                       | 149 ms: 1.02x slower                                                    |
| json_loads           | 32.1 us                                                      | 32.7 us: 1.02x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| json_dumps           | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| unpickle_pure_python | 251 us                                                       | 266 us: 1.06x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 382 us: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.3 ms: 1.03x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.96 ms: 1.04x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.03x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.2 ms                                                      | 13.1 ms: 1.00x faster                                                   |
| django_template | 42.3 ms                                                      | 51.0 ms: 1.21x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 34.4 ms: 1.26x slower                                                   |
| genshi_xml      | 60.4 ms                                                      | 81.1 ms: 1.34x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.19x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 37.4 us: 1.36x faster                                                   |
| async_tree_memoization     | 645 ms                                                       | 571 ms: 1.13x faster                                                    |
| deepcopy                   | 448 us                                                       | 400 us: 1.12x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 430 ms: 1.11x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.16 sec: 1.10x faster                                                  |
| async_tree_none            | 492 ms                                                       | 451 ms: 1.09x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 558 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 743 ms: 1.06x faster                                                    |
| scimark_sor                | 159 ms                                                       | 150 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 720 ms: 1.06x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.83 us: 1.05x faster                                                   |
| regex_dna                  | 259 ms                                                       | 246 ms: 1.05x faster                                                    |
| pathlib                    | 22.8 ms                                                      | 21.8 ms: 1.04x faster                                                   |
| float                      | 91.4 ms                                                      | 88.0 ms: 1.04x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 5.00 ms: 1.04x faster                                                   |
| async_tree_io              | 1.22 sec                                                     | 1.19 sec: 1.03x faster                                                  |
| regex_v8                   | 31.1 ms                                                      | 30.3 ms: 1.03x faster                                                   |
| coroutines                 | 29.0 ms                                                      | 28.3 ms: 1.02x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.87 ms: 1.02x faster                                                   |
| xml_etree_process          | 80.8 ms                                                      | 79.4 ms: 1.02x faster                                                   |
| mako                       | 13.2 ms                                                      | 13.1 ms: 1.00x faster                                                   |
| asyncio_websockets         | 657 ms                                                       | 663 ms: 1.01x slower                                                    |
| coverage                   | 98.4 ms                                                      | 99.6 ms: 1.01x slower                                                   |
| nbody                      | 114 ms                                                       | 116 ms: 1.02x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                       | 149 ms: 1.02x slower                                                    |
| json_loads                 | 32.1 us                                                      | 32.7 us: 1.02x slower                                                   |
| json                       | 5.64 ms                                                      | 5.76 ms: 1.02x slower                                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 5.96 sec: 1.02x slower                                                  |
| tomli_loads                | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| python_startup             | 13.0 ms                                                      | 13.3 ms: 1.03x slower                                                   |
| logging_simple             | 7.21 us                                                      | 7.41 us: 1.03x slower                                                   |
| logging_silent             | 133 ns                                                       | 137 ns: 1.03x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| telco                      | 10.0 ms                                                      | 10.4 ms: 1.03x slower                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.29 sec: 1.04x slower                                                  |
| mdp                        | 3.33 sec                                                     | 3.45 sec: 1.04x slower                                                  |
| spectral_norm              | 141 ms                                                       | 146 ms: 1.04x slower                                                    |
| async_generators           | 488 ms                                                       | 507 ms: 1.04x slower                                                    |
| logging_format             | 7.82 us                                                      | 8.13 us: 1.04x slower                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.81 ms: 1.04x slower                                                   |
| scimark_fft                | 445 ms                                                       | 463 ms: 1.04x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 8.96 ms: 1.04x slower                                                   |
| scimark_lu                 | 141 ms                                                       | 149 ms: 1.06x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 266 us: 1.06x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.33 ms: 1.06x slower                                                   |
| pickle_pure_python         | 359 us                                                       | 382 us: 1.06x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 70.5 ms: 1.07x slower                                                   |
| typing_runtime_protocols   | 193 us                                                       | 207 us: 1.07x slower                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 7.59 ms: 1.08x slower                                                   |
| meteor_contest             | 113 ms                                                       | 123 ms: 1.09x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 635 ms: 1.09x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 89.4 ms: 1.09x slower                                                   |
| deltablue                  | 3.88 ms                                                      | 4.34 ms: 1.12x slower                                                   |
| scimark_monte_carlo        | 82.3 ms                                                      | 92.2 ms: 1.12x slower                                                   |
| fannkuch                   | 451 ms                                                       | 511 ms: 1.13x slower                                                    |
| pyflate                    | 557 ms                                                       | 630 ms: 1.13x slower                                                    |
| go                         | 161 ms                                                       | 188 ms: 1.17x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 151 ms: 1.17x slower                                                    |
| tornado_http               | 128 ms                                                       | 151 ms: 1.18x slower                                                    |
| raytrace                   | 297 ms                                                       | 353 ms: 1.19x slower                                                    |
| django_template            | 42.3 ms                                                      | 51.0 ms: 1.21x slower                                                   |
| richards                   | 55.9 ms                                                      | 67.9 ms: 1.21x slower                                                   |
| comprehensions             | 20.5 us                                                      | 25.0 us: 1.22x slower                                                   |
| richards_super             | 62.3 ms                                                      | 76.3 ms: 1.22x slower                                                   |
| sqlglot_parse              | 1.42 ms                                                      | 1.77 ms: 1.24x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 1.52 sec: 1.24x slower                                                  |
| 2to3                       | 305 ms                                                       | 382 ms: 1.25x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 34.4 ms: 1.26x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 125 ms: 1.26x slower                                                    |
| docutils                   | 3.10 sec                                                     | 3.93 sec: 1.27x slower                                                  |
| sqlglot_optimize           | 62.6 ms                                                      | 79.4 ms: 1.27x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 2.19 ms: 1.28x slower                                                   |
| chaos                      | 68.3 ms                                                      | 91.5 ms: 1.34x slower                                                   |
| genshi_xml                 | 60.4 ms                                                      | 81.1 ms: 1.34x slower                                                   |
| sympy_expand               | 457 ms                                                       | 619 ms: 1.35x slower                                                    |
| pprint_pformat             | 1.93 sec                                                     | 2.64 sec: 1.37x slower                                                  |
| sympy_str                  | 265 ms                                                       | 364 ms: 1.37x slower                                                    |
| pprint_safe_repr           | 933 ms                                                       | 1.28 sec: 1.37x slower                                                  |
| sympy_integrate            | 20.9 ms                                                      | 29.2 ms: 1.40x slower                                                   |
| pylint                     | 337 ms                                                       | 489 ms: 1.45x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 10.3 ms: 1.45x slower                                                   |
| dulwich_log                | 58.5 ms                                                      | 85.3 ms: 1.46x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 215 ms: 1.50x slower                                                    |
| regex_compile              | 128 ms                                                       | 194 ms: 1.51x slower                                                    |
| generators                 | 37.1 ms                                                      | 56.9 ms: 1.53x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.10x slower                                                            |

Benchmark hidden because not significant (5): thrift, pidigits, xml_etree_generate, create_gc_cycles, xml_etree_parse
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.10x