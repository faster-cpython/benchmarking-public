# Results vs. 3.13.0

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-aarch64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 386 ms: 1.26x slower                                                    |
| docutils       | 2.91 sec                                                 | 4.04 sec: 1.39x slower                                                  |
| html5lib       | 64.3 ms                                                  | 71.9 ms: 1.12x slower                                                   |
| tornado_http   | 131 ms                                                   | 140 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                    | 1.20x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 542 ms: 1.20x faster                                                    |
| async_tree_none            | 493 ms                                                   | 435 ms: 1.13x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 412 ms: 1.13x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 580 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 705 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 751 ms: 1.02x faster                                                    |
| asyncio_websockets         | 656 ms                                                   | 660 ms: 1.01x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 29.1 ms: 1.03x slower                                                   |
| async_generators           | 496 ms                                                   | 511 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.25 sec: 1.03x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| asyncio_tcp                | 568 ms                                                   | 614 ms: 1.08x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 88.3 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.2 ms: 1.04x faster                                                   |
| regex_effbot   | 4.87 ms                                                  | 4.81 ms: 1.01x faster                                                   |
| regex_compile  | 128 ms                                                   | 188 ms: 1.46x slower                                                    |
| Geometric mean | (ref)                                                    | 1.08x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 188 ms                                                   | 189 ms: 1.00x slower                                                    |
| tomli_loads          | 2.53 sec                                                 | 2.61 sec: 1.03x slower                                                  |
| xml_etree_iterparse  | 147 ms                                                   | 151 ms: 1.03x slower                                                    |
| json_loads           | 31.4 us                                                  | 32.5 us: 1.04x slower                                                   |
| unpickle_pure_python | 254 us                                                   | 268 us: 1.05x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 391 us: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.03x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_generate, xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| django_template | 42.3 ms                                                  | 50.8 ms: 1.20x slower                                                   |
| genshi_text     | 27.7 ms                                                  | 34.3 ms: 1.24x slower                                                   |
| genshi_xml      | 60.2 ms                                                  | 82.0 ms: 1.36x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.19x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 51.0 us                                                  | 36.8 us: 1.39x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 542 ms: 1.20x faster                                                    |
| deepcopy                   | 451 us                                                   | 397 us: 1.14x faster                                                    |
| async_tree_none            | 493 ms                                                   | 435 ms: 1.13x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 412 ms: 1.13x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 580 ms: 1.08x faster                                                    |
| float                      | 94.4 ms                                                  | 88.3 ms: 1.07x faster                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 3.81 us: 1.07x faster                                                   |
| scimark_sor                | 159 ms                                                   | 150 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 705 ms: 1.04x faster                                                    |
| regex_v8                   | 31.5 ms                                                  | 30.2 ms: 1.04x faster                                                   |
| pathlib                    | 22.4 ms                                                  | 22.0 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 751 ms: 1.02x faster                                                    |
| python_startup             | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| mako                       | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| regex_effbot               | 4.87 ms                                                  | 4.81 ms: 1.01x faster                                                   |
| coverage                   | 98.5 ms                                                  | 97.7 ms: 1.01x faster                                                   |
| xml_etree_parse            | 188 ms                                                   | 189 ms: 1.00x slower                                                    |
| asyncio_websockets         | 656 ms                                                   | 660 ms: 1.01x slower                                                    |
| scimark_fft                | 447 ms                                                   | 454 ms: 1.02x slower                                                    |
| json                       | 5.61 ms                                                  | 5.71 ms: 1.02x slower                                                   |
| bpe_tokeniser              | 5.90 sec                                                 | 6.02 sec: 1.02x slower                                                  |
| coroutines                 | 28.2 ms                                                  | 29.1 ms: 1.03x slower                                                   |
| async_generators           | 496 ms                                                   | 511 ms: 1.03x slower                                                    |
| tomli_loads                | 2.53 sec                                                 | 2.61 sec: 1.03x slower                                                  |
| xml_etree_iterparse        | 147 ms                                                   | 151 ms: 1.03x slower                                                    |
| mdp                        | 3.36 sec                                                 | 3.47 sec: 1.03x slower                                                  |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.80 ms: 1.03x slower                                                   |
| bench_thread_pool          | 1.28 ms                                                  | 1.32 ms: 1.03x slower                                                   |
| spectral_norm              | 141 ms                                                   | 146 ms: 1.03x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.25 sec: 1.03x slower                                                  |
| json_loads                 | 31.4 us                                                  | 32.5 us: 1.04x slower                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 7.56 ms: 1.04x slower                                                   |
| logging_format             | 7.83 us                                                  | 8.16 us: 1.04x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| telco                      | 9.73 ms                                                  | 10.2 ms: 1.04x slower                                                   |
| thrift                     | 946 us                                                   | 992 us: 1.05x slower                                                    |
| unpickle_pure_python       | 254 us                                                   | 268 us: 1.05x slower                                                    |
| logging_simple             | 7.04 us                                                  | 7.44 us: 1.06x slower                                                   |
| scimark_lu                 | 139 ms                                                   | 147 ms: 1.06x slower                                                    |
| crypto_pyaes               | 82.7 ms                                                  | 88.2 ms: 1.07x slower                                                   |
| tornado_http               | 131 ms                                                   | 140 ms: 1.07x slower                                                    |
| meteor_contest             | 113 ms                                                   | 122 ms: 1.08x slower                                                    |
| asyncio_tcp                | 568 ms                                                   | 614 ms: 1.08x slower                                                    |
| scimark_monte_carlo        | 83.8 ms                                                  | 90.8 ms: 1.08x slower                                                   |
| pickle_pure_python         | 359 us                                                   | 391 us: 1.09x slower                                                    |
| create_gc_cycles           | 2.12 ms                                                  | 2.32 ms: 1.09x slower                                                   |
| typing_runtime_protocols   | 192 us                                                   | 210 us: 1.09x slower                                                    |
| deltablue                  | 3.85 ms                                                  | 4.24 ms: 1.10x slower                                                   |
| raytrace                   | 298 ms                                                   | 328 ms: 1.10x slower                                                    |
| fannkuch                   | 452 ms                                                   | 502 ms: 1.11x slower                                                    |
| html5lib                   | 64.3 ms                                                  | 71.9 ms: 1.12x slower                                                   |
| gc_traversal               | 4.53 ms                                                  | 5.08 ms: 1.12x slower                                                   |
| go                         | 163 ms                                                   | 186 ms: 1.14x slower                                                    |
| pyflate                    | 556 ms                                                   | 643 ms: 1.16x slower                                                    |
| sqlglot_normalize          | 128 ms                                                   | 150 ms: 1.17x slower                                                    |
| pycparser                  | 1.26 sec                                                 | 1.49 sec: 1.18x slower                                                  |
| comprehensions             | 20.4 us                                                  | 24.2 us: 1.19x slower                                                   |
| django_template            | 42.3 ms                                                  | 50.8 ms: 1.20x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.69 ms: 1.22x slower                                                   |
| genshi_text                | 27.7 ms                                                  | 34.3 ms: 1.24x slower                                                   |
| nqueens                    | 98.7 ms                                                  | 123 ms: 1.24x slower                                                    |
| richards_super             | 60.3 ms                                                  | 75.0 ms: 1.24x slower                                                   |
| sqlglot_optimize           | 62.4 ms                                                  | 78.4 ms: 1.26x slower                                                   |
| 2to3                       | 306 ms                                                   | 386 ms: 1.26x slower                                                    |
| richards                   | 53.5 ms                                                  | 68.4 ms: 1.28x slower                                                   |
| sqlglot_transpile          | 1.73 ms                                                  | 2.22 ms: 1.28x slower                                                   |
| chaos                      | 68.8 ms                                                  | 88.9 ms: 1.29x slower                                                   |
| sympy_expand               | 455 ms                                                   | 604 ms: 1.33x slower                                                    |
| genshi_xml                 | 60.2 ms                                                  | 82.0 ms: 1.36x slower                                                   |
| sympy_integrate            | 21.0 ms                                                  | 28.9 ms: 1.38x slower                                                   |
| pylint                     | 343 ms                                                   | 477 ms: 1.39x slower                                                    |
| docutils                   | 2.91 sec                                                 | 4.04 sec: 1.39x slower                                                  |
| sympy_str                  | 264 ms                                                   | 370 ms: 1.40x slower                                                    |
| hexiom                     | 7.13 ms                                                  | 10.0 ms: 1.40x slower                                                   |
| pprint_safe_repr           | 926 ms                                                   | 1.35 sec: 1.45x slower                                                  |
| regex_compile              | 128 ms                                                   | 188 ms: 1.46x slower                                                    |
| pprint_pformat             | 1.90 sec                                                 | 2.79 sec: 1.47x slower                                                  |
| generators                 | 37.8 ms                                                  | 57.2 ms: 1.51x slower                                                   |
| sympy_sum                  | 143 ms                                                   | 218 ms: 1.52x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.09x slower                                                            |

Benchmark hidden because not significant (9): xml_etree_generate, logging_silent, xml_etree_process, pidigits, regex_dna, json_dumps, python_startup_no_site, async_tree_io_tg, nbody
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.11x