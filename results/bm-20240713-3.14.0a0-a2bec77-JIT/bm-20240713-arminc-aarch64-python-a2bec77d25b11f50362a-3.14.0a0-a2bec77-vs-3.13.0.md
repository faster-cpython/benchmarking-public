# Results vs. 3.13.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-aarch64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 361 ms: 1.18x slower                                                    |
| docutils       | 2.91 sec                                                 | 3.55 sec: 1.22x slower                                                  |
| html5lib       | 64.3 ms                                                  | 69.9 ms: 1.09x slower                                                   |
| tornado_http   | 131 ms                                                   | 142 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                    | 1.14x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 542 ms: 1.20x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 414 ms: 1.13x faster                                                    |
| async_tree_none            | 493 ms                                                   | 451 ms: 1.09x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 590 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 739 ms: 1.03x faster                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.07 sec: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 720 ms: 1.02x faster                                                    |
| asyncio_websockets         | 656 ms                                                   | 660 ms: 1.01x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.11 sec: 1.02x slower                                                  |
| async_generators           | 496 ms                                                   | 505 ms: 1.02x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 28.9 ms: 1.02x slower                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.26 sec: 1.04x slower                                                  |
| asyncio_tcp                | 568 ms                                                   | 625 ms: 1.10x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 90.6 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                                   |
| regex_effbot   | 4.87 ms                                                  | 4.94 ms: 1.01x slower                                                   |
| regex_dna      | 246 ms                                                   | 259 ms: 1.05x slower                                                    |
| regex_compile  | 128 ms                                                   | 178 ms: 1.38x slower                                                    |
| Geometric mean | (ref)                                                    | 1.09x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                  | 13.2 ms: 1.01x faster                                                   |
| tomli_loads          | 2.53 sec                                                 | 2.64 sec: 1.05x slower                                                  |
| json_loads           | 31.4 us                                                  | 32.9 us: 1.05x slower                                                   |
| unpickle_pure_python | 254 us                                                   | 274 us: 1.08x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 415 us: 1.15x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.03x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_process, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| python_startup_no_site | 8.75 ms                                                  | 8.94 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.00x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.1 ms: 1.01x faster                                                   |
| django_template | 42.3 ms                                                  | 50.9 ms: 1.21x slower                                                   |
| genshi_text     | 27.7 ms                                                  | 34.4 ms: 1.24x slower                                                   |
| genshi_xml      | 60.2 ms                                                  | 80.5 ms: 1.34x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.19x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 51.0 us                                                  | 38.0 us: 1.34x faster                                                   |
| deepcopy                   | 451 us                                                   | 372 us: 1.21x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 542 ms: 1.20x faster                                                    |
| async_tree_none_tg         | 467 ms                                                   | 414 ms: 1.13x faster                                                    |
| async_tree_none            | 493 ms                                                   | 451 ms: 1.09x faster                                                    |
| async_tree_memoization     | 626 ms                                                   | 590 ms: 1.06x faster                                                    |
| float                      | 94.4 ms                                                  | 90.6 ms: 1.04x faster                                                   |
| regex_v8                   | 31.5 ms                                                  | 30.3 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 739 ms: 1.03x faster                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.07 sec: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 720 ms: 1.02x faster                                                    |
| pathlib                    | 22.4 ms                                                  | 22.0 ms: 1.02x faster                                                   |
| python_startup             | 13.3 ms                                                  | 13.0 ms: 1.02x faster                                                   |
| json_dumps                 | 13.4 ms                                                  | 13.2 ms: 1.01x faster                                                   |
| mako                       | 13.3 ms                                                  | 13.1 ms: 1.01x faster                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 4.03 us: 1.01x faster                                                   |
| asyncio_websockets         | 656 ms                                                   | 660 ms: 1.01x slower                                                    |
| regex_effbot               | 4.87 ms                                                  | 4.94 ms: 1.01x slower                                                   |
| richards                   | 53.5 ms                                                  | 54.3 ms: 1.02x slower                                                   |
| richards_super             | 60.3 ms                                                  | 61.4 ms: 1.02x slower                                                   |
| bpe_tokeniser              | 5.90 sec                                                 | 6.00 sec: 1.02x slower                                                  |
| async_tree_io_tg           | 1.09 sec                                                 | 1.11 sec: 1.02x slower                                                  |
| async_generators           | 496 ms                                                   | 505 ms: 1.02x slower                                                    |
| logging_simple             | 7.04 us                                                  | 7.17 us: 1.02x slower                                                   |
| python_startup_no_site     | 8.75 ms                                                  | 8.94 ms: 1.02x slower                                                   |
| generators                 | 37.8 ms                                                  | 38.6 ms: 1.02x slower                                                   |
| meteor_contest             | 113 ms                                                   | 116 ms: 1.02x slower                                                    |
| spectral_norm              | 141 ms                                                   | 144 ms: 1.02x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 28.9 ms: 1.02x slower                                                   |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.76 ms: 1.03x slower                                                   |
| coverage                   | 98.5 ms                                                  | 101 ms: 1.03x slower                                                    |
| thrift                     | 946 us                                                   | 974 us: 1.03x slower                                                    |
| mdp                        | 3.36 sec                                                 | 3.47 sec: 1.03x slower                                                  |
| scimark_fft                | 447 ms                                                   | 463 ms: 1.04x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.26 sec: 1.04x slower                                                  |
| fannkuch                   | 452 ms                                                   | 470 ms: 1.04x slower                                                    |
| bench_thread_pool          | 1.28 ms                                                  | 1.33 ms: 1.04x slower                                                   |
| tomli_loads                | 2.53 sec                                                 | 2.64 sec: 1.05x slower                                                  |
| json_loads                 | 31.4 us                                                  | 32.9 us: 1.05x slower                                                   |
| regex_dna                  | 246 ms                                                   | 259 ms: 1.05x slower                                                    |
| crypto_pyaes               | 82.7 ms                                                  | 87.0 ms: 1.05x slower                                                   |
| json                       | 5.61 ms                                                  | 5.92 ms: 1.05x slower                                                   |
| telco                      | 9.73 ms                                                  | 10.4 ms: 1.07x slower                                                   |
| scimark_monte_carlo        | 83.8 ms                                                  | 89.9 ms: 1.07x slower                                                   |
| unpickle_pure_python       | 254 us                                                   | 274 us: 1.08x slower                                                    |
| pycparser                  | 1.26 sec                                                 | 1.36 sec: 1.08x slower                                                  |
| tornado_http               | 131 ms                                                   | 142 ms: 1.08x slower                                                    |
| pyflate                    | 556 ms                                                   | 603 ms: 1.08x slower                                                    |
| typing_runtime_protocols   | 192 us                                                   | 209 us: 1.09x slower                                                    |
| html5lib                   | 64.3 ms                                                  | 69.9 ms: 1.09x slower                                                   |
| raytrace                   | 298 ms                                                   | 325 ms: 1.09x slower                                                    |
| asyncio_tcp                | 568 ms                                                   | 625 ms: 1.10x slower                                                    |
| gc_traversal               | 4.53 ms                                                  | 5.02 ms: 1.11x slower                                                   |
| sqlglot_optimize           | 62.4 ms                                                  | 69.1 ms: 1.11x slower                                                   |
| go                         | 163 ms                                                   | 181 ms: 1.11x slower                                                    |
| dask                       | 350 ms                                                   | 391 ms: 1.11x slower                                                    |
| scimark_sor                | 159 ms                                                   | 178 ms: 1.12x slower                                                    |
| sqlglot_normalize          | 128 ms                                                   | 144 ms: 1.12x slower                                                    |
| create_gc_cycles           | 2.12 ms                                                  | 2.39 ms: 1.13x slower                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 8.27 ms: 1.13x slower                                                   |
| comprehensions             | 20.4 us                                                  | 23.4 us: 1.15x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.59 ms: 1.15x slower                                                   |
| deltablue                  | 3.85 ms                                                  | 4.45 ms: 1.15x slower                                                   |
| pickle_pure_python         | 359 us                                                   | 415 us: 1.15x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 2.02 ms: 1.17x slower                                                   |
| 2to3                       | 306 ms                                                   | 361 ms: 1.18x slower                                                    |
| sympy_expand               | 455 ms                                                   | 541 ms: 1.19x slower                                                    |
| nqueens                    | 98.7 ms                                                  | 118 ms: 1.19x slower                                                    |
| pylint                     | 343 ms                                                   | 413 ms: 1.20x slower                                                    |
| django_template            | 42.3 ms                                                  | 50.9 ms: 1.21x slower                                                   |
| pprint_safe_repr           | 926 ms                                                   | 1.13 sec: 1.22x slower                                                  |
| docutils                   | 2.91 sec                                                 | 3.55 sec: 1.22x slower                                                  |
| sympy_str                  | 264 ms                                                   | 324 ms: 1.23x slower                                                    |
| pprint_pformat             | 1.90 sec                                                 | 2.34 sec: 1.23x slower                                                  |
| genshi_text                | 27.7 ms                                                  | 34.4 ms: 1.24x slower                                                   |
| sympy_integrate            | 21.0 ms                                                  | 26.2 ms: 1.25x slower                                                   |
| hexiom                     | 7.13 ms                                                  | 9.03 ms: 1.27x slower                                                   |
| sympy_sum                  | 143 ms                                                   | 185 ms: 1.29x slower                                                    |
| scimark_lu                 | 139 ms                                                   | 183 ms: 1.31x slower                                                    |
| chaos                      | 68.8 ms                                                  | 90.9 ms: 1.32x slower                                                   |
| genshi_xml                 | 60.2 ms                                                  | 80.5 ms: 1.34x slower                                                   |
| regex_compile              | 128 ms                                                   | 178 ms: 1.38x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.07x slower                                                            |

Benchmark hidden because not significant (8): xml_etree_generate, xml_etree_process, xml_etree_parse, nbody, pidigits, logging_silent, logging_format, xml_etree_iterparse
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240713-3.14.0a0-a2bec77-JIT/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.09x