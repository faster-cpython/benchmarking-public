# Results vs. 3.13.0

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: linux-aarch64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 367 ms: 1.20x slower                                                    |
| docutils       | 2.91 sec                                                 | 3.67 sec: 1.26x slower                                                  |
| html5lib       | 64.3 ms                                                  | 70.6 ms: 1.10x slower                                                   |
| tornado_http   | 131 ms                                                   | 139 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                    | 1.15x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 538 ms: 1.21x faster                                                    |
| async_tree_none            | 493 ms                                                   | 435 ms: 1.13x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 413 ms: 1.13x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 574 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 696 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 744 ms: 1.03x faster                                                    |
| asyncio_websockets         | 656 ms                                                   | 662 ms: 1.01x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 28.5 ms: 1.01x slower                                                   |
| async_tree_io_tg           | 1.09 sec                                                 | 1.11 sec: 1.02x slower                                                  |
| async_generators           | 496 ms                                                   | 506 ms: 1.02x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.27 sec: 1.04x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.18 sec: 1.07x slower                                                  |
| asyncio_tcp                | 568 ms                                                   | 641 ms: 1.13x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 91.3 ms: 1.03x faster                                                   |
| nbody          | 114 ms                                                   | 117 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.8 ms: 1.02x faster                                                   |
| regex_dna      | 246 ms                                                   | 251 ms: 1.02x slower                                                    |
| regex_compile  | 128 ms                                                   | 174 ms: 1.35x slower                                                    |
| Geometric mean | (ref)                                                    | 1.08x slower                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_loads           | 31.4 us                                                  | 32.7 us: 1.04x slower                                                   |
| tomli_loads          | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 275 us: 1.08x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 396 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.03x slower                                                            |

Benchmark hidden because not significant (5): json_dumps, xml_etree_process, xml_etree_generate, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                   |
| genshi_text     | 27.7 ms                                                  | 32.9 ms: 1.19x slower                                                   |
| genshi_xml      | 60.2 ms                                                  | 72.7 ms: 1.21x slower                                                   |
| django_template | 42.3 ms                                                  | 52.1 ms: 1.23x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.14x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240802-arminc-aarch64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 51.0 us                                                  | 38.4 us: 1.33x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 538 ms: 1.21x faster                                                    |
| deepcopy                   | 451 us                                                   | 376 us: 1.20x faster                                                    |
| async_tree_none            | 493 ms                                                   | 435 ms: 1.13x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 413 ms: 1.13x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 574 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 696 ms: 1.06x faster                                                    |
| scimark_sor                | 159 ms                                                   | 152 ms: 1.04x faster                                                    |
| mako                       | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                   |
| float                      | 94.4 ms                                                  | 91.3 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 744 ms: 1.03x faster                                                    |
| regex_v8                   | 31.5 ms                                                  | 30.8 ms: 1.02x faster                                                   |
| pathlib                    | 22.4 ms                                                  | 22.2 ms: 1.01x faster                                                   |
| bpe_tokeniser              | 5.90 sec                                                 | 5.84 sec: 1.01x faster                                                  |
| asyncio_websockets         | 656 ms                                                   | 662 ms: 1.01x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 28.5 ms: 1.01x slower                                                   |
| regex_dna                  | 246 ms                                                   | 251 ms: 1.02x slower                                                    |
| spectral_norm              | 141 ms                                                   | 144 ms: 1.02x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.11 sec: 1.02x slower                                                  |
| bench_thread_pool          | 1.28 ms                                                  | 1.30 ms: 1.02x slower                                                   |
| async_generators           | 496 ms                                                   | 506 ms: 1.02x slower                                                    |
| logging_format             | 7.83 us                                                  | 8.00 us: 1.02x slower                                                   |
| nbody                      | 114 ms                                                   | 117 ms: 1.02x slower                                                    |
| richards                   | 53.5 ms                                                  | 54.9 ms: 1.02x slower                                                   |
| richards_super             | 60.3 ms                                                  | 62.1 ms: 1.03x slower                                                   |
| mdp                        | 3.36 sec                                                 | 3.47 sec: 1.03x slower                                                  |
| thrift                     | 946 us                                                   | 979 us: 1.04x slower                                                    |
| json                       | 5.61 ms                                                  | 5.81 ms: 1.04x slower                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 4.22 us: 1.04x slower                                                   |
| json_loads                 | 31.4 us                                                  | 32.7 us: 1.04x slower                                                   |
| tomli_loads                | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                                  |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.27 sec: 1.04x slower                                                  |
| logging_simple             | 7.04 us                                                  | 7.35 us: 1.04x slower                                                   |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.90 ms: 1.05x slower                                                   |
| telco                      | 9.73 ms                                                  | 10.3 ms: 1.06x slower                                                   |
| meteor_contest             | 113 ms                                                   | 120 ms: 1.06x slower                                                    |
| tornado_http               | 131 ms                                                   | 139 ms: 1.06x slower                                                    |
| scimark_monte_carlo        | 83.8 ms                                                  | 89.1 ms: 1.06x slower                                                   |
| scimark_lu                 | 139 ms                                                   | 148 ms: 1.06x slower                                                    |
| scimark_fft                | 447 ms                                                   | 476 ms: 1.06x slower                                                    |
| fannkuch                   | 452 ms                                                   | 481 ms: 1.06x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.18 sec: 1.07x slower                                                  |
| unpickle_pure_python       | 254 us                                                   | 275 us: 1.08x slower                                                    |
| gc_traversal               | 4.53 ms                                                  | 4.91 ms: 1.08x slower                                                   |
| crypto_pyaes               | 82.7 ms                                                  | 90.2 ms: 1.09x slower                                                   |
| html5lib                   | 64.3 ms                                                  | 70.6 ms: 1.10x slower                                                   |
| pyflate                    | 556 ms                                                   | 612 ms: 1.10x slower                                                    |
| pickle_pure_python         | 359 us                                                   | 396 us: 1.10x slower                                                    |
| create_gc_cycles           | 2.12 ms                                                  | 2.35 ms: 1.11x slower                                                   |
| typing_runtime_protocols   | 192 us                                                   | 213 us: 1.11x slower                                                    |
| raytrace                   | 298 ms                                                   | 332 ms: 1.11x slower                                                    |
| dask                       | 350 ms                                                   | 391 ms: 1.12x slower                                                    |
| go                         | 163 ms                                                   | 182 ms: 1.12x slower                                                    |
| bench_mp_pool              | 7.30 ms                                                  | 8.23 ms: 1.13x slower                                                   |
| asyncio_tcp                | 568 ms                                                   | 641 ms: 1.13x slower                                                    |
| sqlglot_normalize          | 128 ms                                                   | 147 ms: 1.14x slower                                                    |
| deltablue                  | 3.85 ms                                                  | 4.44 ms: 1.15x slower                                                   |
| sqlglot_optimize           | 62.4 ms                                                  | 72.5 ms: 1.16x slower                                                   |
| pycparser                  | 1.26 sec                                                 | 1.47 sec: 1.16x slower                                                  |
| comprehensions             | 20.4 us                                                  | 24.1 us: 1.18x slower                                                   |
| genshi_text                | 27.7 ms                                                  | 32.9 ms: 1.19x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.65 ms: 1.20x slower                                                   |
| 2to3                       | 306 ms                                                   | 367 ms: 1.20x slower                                                    |
| genshi_xml                 | 60.2 ms                                                  | 72.7 ms: 1.21x slower                                                   |
| sqlglot_transpile          | 1.73 ms                                                  | 2.11 ms: 1.22x slower                                                   |
| django_template            | 42.3 ms                                                  | 52.1 ms: 1.23x slower                                                   |
| nqueens                    | 98.7 ms                                                  | 123 ms: 1.25x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.16 sec: 1.25x slower                                                  |
| pylint                     | 343 ms                                                   | 429 ms: 1.25x slower                                                    |
| pprint_pformat             | 1.90 sec                                                 | 2.39 sec: 1.26x slower                                                  |
| docutils                   | 2.91 sec                                                 | 3.67 sec: 1.26x slower                                                  |
| chaos                      | 68.8 ms                                                  | 87.7 ms: 1.27x slower                                                   |
| hexiom                     | 7.13 ms                                                  | 9.24 ms: 1.30x slower                                                   |
| sympy_expand               | 455 ms                                                   | 589 ms: 1.30x slower                                                    |
| sympy_integrate            | 21.0 ms                                                  | 27.5 ms: 1.31x slower                                                   |
| sympy_str                  | 264 ms                                                   | 350 ms: 1.33x slower                                                    |
| regex_compile              | 128 ms                                                   | 174 ms: 1.35x slower                                                    |
| sympy_sum                  | 143 ms                                                   | 201 ms: 1.40x slower                                                    |
| generators                 | 37.8 ms                                                  | 57.3 ms: 1.51x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.08x slower                                                            |

Benchmark hidden because not significant (11): logging_silent, python_startup, json_dumps, coverage, xml_etree_process, pidigits, regex_effbot, xml_etree_generate, python_startup_no_site, xml_etree_parse, xml_etree_iterparse
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.10x