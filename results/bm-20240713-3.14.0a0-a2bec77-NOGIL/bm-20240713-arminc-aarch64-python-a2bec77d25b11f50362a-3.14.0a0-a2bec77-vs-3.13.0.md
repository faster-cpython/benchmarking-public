# Results vs. 3.13.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-aarch64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.58x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 517 ms: 1.69x slower                                                    |
| docutils       | 2.91 sec                                                 | 4.10 sec: 1.41x slower                                                  |
| html5lib       | 64.3 ms                                                  | 121 ms: 1.88x slower                                                    |
| tornado_http   | 131 ms                                                   | 202 ms: 1.53x slower                                                    |
| Geometric mean | (ref)                                                    | 1.62x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 656 ms                                                   | 671 ms: 1.02x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 702 ms: 1.08x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.47 sec: 1.13x slower                                                  |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 869 ms: 1.18x slower                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 910 ms: 1.19x slower                                                    |
| async_tree_memoization     | 626 ms                                                   | 748 ms: 1.19x slower                                                    |
| asyncio_tcp                | 568 ms                                                   | 684 ms: 1.20x slower                                                    |
| async_tree_none_tg         | 467 ms                                                   | 566 ms: 1.21x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.35 sec: 1.23x slower                                                  |
| async_tree_none            | 493 ms                                                   | 611 ms: 1.24x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.40 sec: 1.26x slower                                                  |
| async_generators           | 496 ms                                                   | 678 ms: 1.37x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 39.2 ms: 1.39x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.20x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 210 ms: 2.22x slower                                                    |
| nbody          | 114 ms                                                   | 289 ms: 2.53x slower                                                    |
| Geometric mean | (ref)                                                    | 1.78x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.87 ms                                                  | 4.30 ms: 1.13x faster                                                   |
| regex_dna      | 246 ms                                                   | 245 ms: 1.01x faster                                                    |
| regex_v8       | 31.5 ms                                                  | 32.5 ms: 1.03x slower                                                   |
| regex_compile  | 128 ms                                                   | 256 ms: 1.99x slower                                                    |
| Geometric mean | (ref)                                                    | 1.16x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 188 ms                                                   | 182 ms: 1.03x faster                                                    |
| xml_etree_iterparse  | 147 ms                                                   | 156 ms: 1.07x slower                                                    |
| json_loads           | 31.4 us                                                  | 38.7 us: 1.23x slower                                                   |
| json_dumps           | 13.4 ms                                                  | 17.6 ms: 1.32x slower                                                   |
| xml_etree_generate   | 113 ms                                                   | 160 ms: 1.41x slower                                                    |
| xml_etree_process    | 80.1 ms                                                  | 129 ms: 1.62x slower                                                    |
| tomli_loads          | 2.53 sec                                                 | 4.20 sec: 1.66x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 542 us: 2.13x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 774 us: 2.16x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.46x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 17.6 ms: 1.33x slower                                                   |
| python_startup_no_site | 8.75 ms                                                  | 11.7 ms: 1.34x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.33x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.2 ms                                                  | 104 ms: 1.72x slower                                                    |
| genshi_text     | 27.7 ms                                                  | 53.2 ms: 1.92x slower                                                   |
| django_template | 42.3 ms                                                  | 83.2 ms: 1.97x slower                                                   |
| mako            | 13.3 ms                                                  | 28.8 ms: 2.16x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.94x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 2.12 ms                                                  | 1.58 ms: 1.34x faster                                                   |
| gc_traversal               | 4.53 ms                                                  | 3.42 ms: 1.32x faster                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 6.25 ms: 1.17x faster                                                   |
| regex_effbot               | 4.87 ms                                                  | 4.30 ms: 1.13x faster                                                   |
| xml_etree_parse            | 188 ms                                                   | 182 ms: 1.03x faster                                                    |
| regex_dna                  | 246 ms                                                   | 245 ms: 1.01x faster                                                    |
| asyncio_websockets         | 656 ms                                                   | 671 ms: 1.02x slower                                                    |
| regex_v8                   | 31.5 ms                                                  | 32.5 ms: 1.03x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                   | 156 ms: 1.07x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 702 ms: 1.08x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.47 sec: 1.13x slower                                                  |
| pathlib                    | 22.4 ms                                                  | 26.3 ms: 1.17x slower                                                   |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 869 ms: 1.18x slower                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 910 ms: 1.19x slower                                                    |
| async_tree_memoization     | 626 ms                                                   | 748 ms: 1.19x slower                                                    |
| asyncio_tcp                | 568 ms                                                   | 684 ms: 1.20x slower                                                    |
| async_tree_none_tg         | 467 ms                                                   | 566 ms: 1.21x slower                                                    |
| telco                      | 9.73 ms                                                  | 11.8 ms: 1.21x slower                                                   |
| json_loads                 | 31.4 us                                                  | 38.7 us: 1.23x slower                                                   |
| async_tree_io_tg           | 1.09 sec                                                 | 1.35 sec: 1.23x slower                                                  |
| deepcopy                   | 451 us                                                   | 559 us: 1.24x slower                                                    |
| async_tree_none            | 493 ms                                                   | 611 ms: 1.24x slower                                                    |
| json                       | 5.61 ms                                                  | 7.01 ms: 1.25x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.40 sec: 1.26x slower                                                  |
| mdp                        | 3.36 sec                                                 | 4.37 sec: 1.30x slower                                                  |
| json_dumps                 | 13.4 ms                                                  | 17.6 ms: 1.32x slower                                                   |
| python_startup             | 13.3 ms                                                  | 17.6 ms: 1.33x slower                                                   |
| python_startup_no_site     | 8.75 ms                                                  | 11.7 ms: 1.34x slower                                                   |
| scimark_fft                | 447 ms                                                   | 601 ms: 1.34x slower                                                    |
| coverage                   | 98.5 ms                                                  | 134 ms: 1.36x slower                                                    |
| async_generators           | 496 ms                                                   | 678 ms: 1.37x slower                                                    |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 9.05 ms: 1.37x slower                                                   |
| coroutines                 | 28.2 ms                                                  | 39.2 ms: 1.39x slower                                                   |
| deepcopy_memo              | 51.0 us                                                  | 72.0 us: 1.41x slower                                                   |
| docutils                   | 2.91 sec                                                 | 4.10 sec: 1.41x slower                                                  |
| xml_etree_generate         | 113 ms                                                   | 160 ms: 1.41x slower                                                    |
| pylint                     | 343 ms                                                   | 504 ms: 1.47x slower                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 6.02 us: 1.48x slower                                                   |
| bench_thread_pool          | 1.28 ms                                                  | 1.91 ms: 1.49x slower                                                   |
| nqueens                    | 98.7 ms                                                  | 151 ms: 1.53x slower                                                    |
| meteor_contest             | 113 ms                                                   | 174 ms: 1.53x slower                                                    |
| tornado_http               | 131 ms                                                   | 202 ms: 1.53x slower                                                    |
| generators                 | 37.8 ms                                                  | 58.4 ms: 1.54x slower                                                   |
| bpe_tokeniser              | 5.90 sec                                                 | 9.48 sec: 1.61x slower                                                  |
| xml_etree_process          | 80.1 ms                                                  | 129 ms: 1.62x slower                                                    |
| pycparser                  | 1.26 sec                                                 | 2.06 sec: 1.63x slower                                                  |
| fannkuch                   | 452 ms                                                   | 750 ms: 1.66x slower                                                    |
| tomli_loads                | 2.53 sec                                                 | 4.20 sec: 1.66x slower                                                  |
| sympy_integrate            | 21.0 ms                                                  | 35.0 ms: 1.67x slower                                                   |
| spectral_norm              | 141 ms                                                   | 237 ms: 1.68x slower                                                    |
| crypto_pyaes               | 82.7 ms                                                  | 140 ms: 1.69x slower                                                    |
| 2to3                       | 306 ms                                                   | 517 ms: 1.69x slower                                                    |
| genshi_xml                 | 60.2 ms                                                  | 104 ms: 1.72x slower                                                    |
| typing_runtime_protocols   | 192 us                                                   | 331 us: 1.72x slower                                                    |
| thrift                     | 946 us                                                   | 1.67 ms: 1.76x slower                                                   |
| sqlglot_normalize          | 128 ms                                                   | 230 ms: 1.80x slower                                                    |
| pyflate                    | 556 ms                                                   | 1.02 sec: 1.83x slower                                                  |
| sqlglot_optimize           | 62.4 ms                                                  | 116 ms: 1.85x slower                                                    |
| html5lib                   | 64.3 ms                                                  | 121 ms: 1.88x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.77 sec: 1.91x slower                                                  |
| pprint_pformat             | 1.90 sec                                                 | 3.64 sec: 1.92x slower                                                  |
| genshi_text                | 27.7 ms                                                  | 53.2 ms: 1.92x slower                                                   |
| sympy_str                  | 264 ms                                                   | 519 ms: 1.97x slower                                                    |
| django_template            | 42.3 ms                                                  | 83.2 ms: 1.97x slower                                                   |
| regex_compile              | 128 ms                                                   | 256 ms: 1.99x slower                                                    |
| comprehensions             | 20.4 us                                                  | 40.7 us: 1.99x slower                                                   |
| logging_format             | 7.83 us                                                  | 15.6 us: 2.00x slower                                                   |
| logging_simple             | 7.04 us                                                  | 14.6 us: 2.07x slower                                                   |
| scimark_monte_carlo        | 83.8 ms                                                  | 175 ms: 2.09x slower                                                    |
| sympy_expand               | 455 ms                                                   | 956 ms: 2.10x slower                                                    |
| logging_silent             | 135 ns                                                   | 287 ns: 2.12x slower                                                    |
| unpickle_pure_python       | 254 us                                                   | 542 us: 2.13x slower                                                    |
| pickle_pure_python         | 359 us                                                   | 774 us: 2.16x slower                                                    |
| scimark_sor                | 159 ms                                                   | 343 ms: 2.16x slower                                                    |
| mako                       | 13.3 ms                                                  | 28.8 ms: 2.16x slower                                                   |
| hexiom                     | 7.13 ms                                                  | 15.6 ms: 2.19x slower                                                   |
| sympy_sum                  | 143 ms                                                   | 318 ms: 2.22x slower                                                    |
| float                      | 94.4 ms                                                  | 210 ms: 2.22x slower                                                    |
| chaos                      | 68.8 ms                                                  | 161 ms: 2.34x slower                                                    |
| richards                   | 53.5 ms                                                  | 127 ms: 2.38x slower                                                    |
| richards_super             | 60.3 ms                                                  | 145 ms: 2.41x slower                                                    |
| nbody                      | 114 ms                                                   | 289 ms: 2.53x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 4.38 ms: 2.53x slower                                                   |
| scimark_lu                 | 139 ms                                                   | 355 ms: 2.55x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 3.78 ms: 2.73x slower                                                   |
| go                         | 163 ms                                                   | 448 ms: 2.76x slower                                                    |
| raytrace                   | 298 ms                                                   | 825 ms: 2.77x slower                                                    |
| deltablue                  | 3.85 ms                                                  | 12.9 ms: 3.34x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.58x slower                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240713-3.14.0a0-a2bec77-NOGIL/bm-20240713-arminc-aarch64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.50x
- 95% likely to have a slowdown of 1.46x
- 99% likely to have a slowdown of 1.40x

# Memory
- memory change: 1.16x