# Results vs. 3.13.0

- fork: python
- ref: 52caaef6d01a94962576
- machine: linux-aarch64
- commit hash: 52caaef
- commit date: 2024-08-24
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 379 ms: 1.24x slower                                                    |
| docutils       | 2.91 sec                                                 | 4.10 sec: 1.41x slower                                                  |
| html5lib       | 64.3 ms                                                  | 72.5 ms: 1.13x slower                                                   |
| tornado_http   | 131 ms                                                   | 149 ms: 1.13x slower                                                    |
| Geometric mean | (ref)                                                    | 1.22x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 553 ms: 1.17x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 425 ms: 1.10x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 574 ms: 1.09x faster                                                    |
| async_tree_none            | 493 ms                                                   | 457 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 714 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 742 ms: 1.03x faster                                                    |
| asyncio_websockets         | 656 ms                                                   | 662 ms: 1.01x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 28.5 ms: 1.01x slower                                                   |
| async_generators           | 496 ms                                                   | 511 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.29 sec: 1.05x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.16 sec: 1.06x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.19 sec: 1.08x slower                                                  |
| asyncio_tcp                | 568 ms                                                   | 638 ms: 1.12x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 88.4 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                                   |
| regex_dna      | 246 ms                                                   | 255 ms: 1.04x slower                                                    |
| regex_compile  | 128 ms                                                   | 190 ms: 1.48x slower                                                    |
| Geometric mean | (ref)                                                    | 1.10x slower                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_loads           | 31.4 us                                                  | 32.6 us: 1.04x slower                                                   |
| tomli_loads          | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 266 us: 1.05x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 382 us: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.02x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_generate, json_dumps, xml_etree_iterparse, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                                   |
| django_template | 42.3 ms                                                  | 51.1 ms: 1.21x slower                                                   |
| genshi_text     | 27.7 ms                                                  | 34.4 ms: 1.24x slower                                                   |
| genshi_xml      | 60.2 ms                                                  | 82.0 ms: 1.36x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.19x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 51.0 us                                                  | 37.3 us: 1.37x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 553 ms: 1.17x faster                                                    |
| deepcopy                   | 451 us                                                   | 396 us: 1.14x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 425 ms: 1.10x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 574 ms: 1.09x faster                                                    |
| async_tree_none            | 493 ms                                                   | 457 ms: 1.08x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.78 us: 1.07x faster                                                   |
| float                      | 94.4 ms                                                  | 88.4 ms: 1.07x faster                                                   |
| regex_v8                   | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 714 ms: 1.03x faster                                                    |
| scimark_sor                | 159 ms                                                   | 154 ms: 1.03x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 742 ms: 1.03x faster                                                    |
| python_startup             | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                   |
| pathlib                    | 22.4 ms                                                  | 21.9 ms: 1.03x faster                                                   |
| mako                       | 13.3 ms                                                  | 13.2 ms: 1.01x faster                                                   |
| asyncio_websockets         | 656 ms                                                   | 662 ms: 1.01x slower                                                    |
| thrift                     | 946 us                                                   | 955 us: 1.01x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 28.5 ms: 1.01x slower                                                   |
| bpe_tokeniser              | 5.90 sec                                                 | 5.97 sec: 1.01x slower                                                  |
| scimark_fft                | 447 ms                                                   | 459 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.76 ms: 1.03x slower                                                   |
| json                       | 5.61 ms                                                  | 5.78 ms: 1.03x slower                                                   |
| async_generators           | 496 ms                                                   | 511 ms: 1.03x slower                                                    |
| mdp                        | 3.36 sec                                                 | 3.48 sec: 1.03x slower                                                  |
| regex_dna                  | 246 ms                                                   | 255 ms: 1.04x slower                                                    |
| bench_mp_pool              | 7.30 ms                                                  | 7.56 ms: 1.04x slower                                                   |
| bench_thread_pool          | 1.28 ms                                                  | 1.32 ms: 1.04x slower                                                   |
| json_loads                 | 31.4 us                                                  | 32.6 us: 1.04x slower                                                   |
| spectral_norm              | 141 ms                                                   | 147 ms: 1.04x slower                                                    |
| tomli_loads                | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| unpickle_pure_python       | 254 us                                                   | 266 us: 1.05x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.29 sec: 1.05x slower                                                  |
| logging_format             | 7.83 us                                                  | 8.24 us: 1.05x slower                                                   |
| logging_simple             | 7.04 us                                                  | 7.47 us: 1.06x slower                                                   |
| pickle_pure_python         | 359 us                                                   | 382 us: 1.06x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.16 sec: 1.06x slower                                                  |
| scimark_lu                 | 139 ms                                                   | 149 ms: 1.07x slower                                                    |
| crypto_pyaes               | 82.7 ms                                                  | 89.0 ms: 1.08x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.19 sec: 1.08x slower                                                  |
| meteor_contest             | 113 ms                                                   | 124 ms: 1.09x slower                                                    |
| gc_traversal               | 4.53 ms                                                  | 4.93 ms: 1.09x slower                                                   |
| typing_runtime_protocols   | 192 us                                                   | 209 us: 1.09x slower                                                    |
| telco                      | 9.73 ms                                                  | 10.7 ms: 1.10x slower                                                   |
| create_gc_cycles           | 2.12 ms                                                  | 2.33 ms: 1.10x slower                                                   |
| scimark_monte_carlo        | 83.8 ms                                                  | 92.1 ms: 1.10x slower                                                   |
| fannkuch                   | 452 ms                                                   | 502 ms: 1.11x slower                                                    |
| pyflate                    | 556 ms                                                   | 622 ms: 1.12x slower                                                    |
| asyncio_tcp                | 568 ms                                                   | 638 ms: 1.12x slower                                                    |
| deltablue                  | 3.85 ms                                                  | 4.34 ms: 1.13x slower                                                   |
| html5lib                   | 64.3 ms                                                  | 72.5 ms: 1.13x slower                                                   |
| tornado_http               | 131 ms                                                   | 149 ms: 1.13x slower                                                    |
| sqlglot_normalize          | 128 ms                                                   | 152 ms: 1.18x slower                                                    |
| raytrace                   | 298 ms                                                   | 353 ms: 1.19x slower                                                    |
| comprehensions             | 20.4 us                                                  | 24.6 us: 1.21x slower                                                   |
| django_template            | 42.3 ms                                                  | 51.1 ms: 1.21x slower                                                   |
| pycparser                  | 1.26 sec                                                 | 1.53 sec: 1.21x slower                                                  |
| 2to3                       | 306 ms                                                   | 379 ms: 1.24x slower                                                    |
| genshi_text                | 27.7 ms                                                  | 34.4 ms: 1.24x slower                                                   |
| sqlglot_optimize           | 62.4 ms                                                  | 77.7 ms: 1.25x slower                                                   |
| nqueens                    | 98.7 ms                                                  | 124 ms: 1.26x slower                                                    |
| richards                   | 53.5 ms                                                  | 67.5 ms: 1.26x slower                                                   |
| sqlglot_transpile          | 1.73 ms                                                  | 2.19 ms: 1.26x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.76 ms: 1.28x slower                                                   |
| richards_super             | 60.3 ms                                                  | 77.3 ms: 1.28x slower                                                   |
| chaos                      | 68.8 ms                                                  | 90.9 ms: 1.32x slower                                                   |
| sympy_expand               | 455 ms                                                   | 603 ms: 1.33x slower                                                    |
| genshi_xml                 | 60.2 ms                                                  | 82.0 ms: 1.36x slower                                                   |
| sympy_str                  | 264 ms                                                   | 361 ms: 1.37x slower                                                    |
| sympy_integrate            | 21.0 ms                                                  | 29.0 ms: 1.38x slower                                                   |
| pprint_safe_repr           | 926 ms                                                   | 1.28 sec: 1.38x slower                                                  |
| go                         | 163 ms                                                   | 226 ms: 1.39x slower                                                    |
| pprint_pformat             | 1.90 sec                                                 | 2.65 sec: 1.40x slower                                                  |
| pylint                     | 343 ms                                                   | 480 ms: 1.40x slower                                                    |
| docutils                   | 2.91 sec                                                 | 4.10 sec: 1.41x slower                                                  |
| hexiom                     | 7.13 ms                                                  | 10.2 ms: 1.43x slower                                                   |
| sympy_sum                  | 143 ms                                                   | 211 ms: 1.47x slower                                                    |
| regex_compile              | 128 ms                                                   | 190 ms: 1.48x slower                                                    |
| generators                 | 37.8 ms                                                  | 57.6 ms: 1.52x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.10x slower                                                            |

Benchmark hidden because not significant (11): xml_etree_generate, json_dumps, pidigits, coverage, xml_etree_iterparse, nbody, logging_silent, xml_etree_parse, regex_effbot, python_startup_no_site, xml_etree_process
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.11x