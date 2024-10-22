# Results vs. 3.13.0

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: linux-aarch64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.56x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.41x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 518 ms: 1.69x slower                                                    |
| docutils       | 2.91 sec                                                 | 4.10 sec: 1.41x slower                                                  |
| html5lib       | 64.3 ms                                                  | 121 ms: 1.88x slower                                                    |
| tornado_http   | 131 ms                                                   | 207 ms: 1.57x slower                                                    |
| Geometric mean | (ref)                                                    | 1.63x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 656 ms                                                   | 672 ms: 1.02x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 699 ms: 1.08x slower                                                    |
| async_tree_memoization     | 626 ms                                                   | 739 ms: 1.18x slower                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 871 ms: 1.18x slower                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 914 ms: 1.20x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.62 sec: 1.20x slower                                                  |
| asyncio_tcp                | 568 ms                                                   | 683 ms: 1.20x slower                                                    |
| async_tree_none_tg         | 467 ms                                                   | 572 ms: 1.22x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.36 sec: 1.25x slower                                                  |
| async_tree_none            | 493 ms                                                   | 625 ms: 1.27x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.41 sec: 1.28x slower                                                  |
| async_generators           | 496 ms                                                   | 653 ms: 1.32x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 40.9 ms: 1.45x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.21x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 207 ms: 2.20x slower                                                    |
| nbody          | 114 ms                                                   | 281 ms: 2.46x slower                                                    |
| Geometric mean | (ref)                                                    | 1.76x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.87 ms                                                  | 4.48 ms: 1.09x faster                                                   |
| regex_v8       | 31.5 ms                                                  | 33.0 ms: 1.05x slower                                                   |
| regex_dna      | 246 ms                                                   | 261 ms: 1.06x slower                                                    |
| regex_compile  | 128 ms                                                   | 259 ms: 2.02x slower                                                    |
| Geometric mean | (ref)                                                    | 1.20x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 188 ms                                                   | 184 ms: 1.02x faster                                                    |
| pickle               | 13.5 us                                                  | 13.3 us: 1.01x faster                                                   |
| pickle_dict          | 38.1 us                                                  | 38.8 us: 1.02x slower                                                   |
| unpickle_list        | 6.65 us                                                  | 6.99 us: 1.05x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                   | 157 ms: 1.07x slower                                                    |
| unpickle             | 20.2 us                                                  | 21.7 us: 1.08x slower                                                   |
| json_loads           | 31.4 us                                                  | 39.3 us: 1.25x slower                                                   |
| json_dumps           | 13.4 ms                                                  | 17.9 ms: 1.34x slower                                                   |
| xml_etree_generate   | 113 ms                                                   | 163 ms: 1.44x slower                                                    |
| xml_etree_process    | 80.1 ms                                                  | 130 ms: 1.63x slower                                                    |
| tomli_loads          | 2.53 sec                                                 | 4.19 sec: 1.66x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 542 us: 2.13x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 777 us: 2.16x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.29x slower                                                            |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 18.2 ms: 1.37x slower                                                   |
| python_startup_no_site | 8.75 ms                                                  | 12.2 ms: 1.40x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.38x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.2 ms                                                  | 104 ms: 1.73x slower                                                    |
| genshi_text     | 27.7 ms                                                  | 53.3 ms: 1.93x slower                                                   |
| django_template | 42.3 ms                                                  | 83.4 ms: 1.97x slower                                                   |
| mako            | 13.3 ms                                                  | 28.9 ms: 2.17x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.94x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 4.53 ms                                                  | 3.45 ms: 1.31x faster                                                   |
| create_gc_cycles           | 2.12 ms                                                  | 1.62 ms: 1.31x faster                                                   |
| regex_effbot               | 4.87 ms                                                  | 4.48 ms: 1.09x faster                                                   |
| xml_etree_parse            | 188 ms                                                   | 184 ms: 1.02x faster                                                    |
| pickle                     | 13.5 us                                                  | 13.3 us: 1.01x faster                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 7.20 ms: 1.01x faster                                                   |
| pickle_dict                | 38.1 us                                                  | 38.8 us: 1.02x slower                                                   |
| asyncio_websockets         | 656 ms                                                   | 672 ms: 1.02x slower                                                    |
| regex_v8                   | 31.5 ms                                                  | 33.0 ms: 1.05x slower                                                   |
| unpickle_list              | 6.65 us                                                  | 6.99 us: 1.05x slower                                                   |
| regex_dna                  | 246 ms                                                   | 261 ms: 1.06x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                   | 157 ms: 1.07x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 699 ms: 1.08x slower                                                    |
| unpickle                   | 20.2 us                                                  | 21.7 us: 1.08x slower                                                   |
| sqlite_synth               | 3.84 us                                                  | 4.17 us: 1.08x slower                                                   |
| async_tree_memoization     | 626 ms                                                   | 739 ms: 1.18x slower                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 871 ms: 1.18x slower                                                    |
| pathlib                    | 22.4 ms                                                  | 26.8 ms: 1.19x slower                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 914 ms: 1.20x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.62 sec: 1.20x slower                                                  |
| asyncio_tcp                | 568 ms                                                   | 683 ms: 1.20x slower                                                    |
| async_tree_none_tg         | 467 ms                                                   | 572 ms: 1.22x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.36 sec: 1.25x slower                                                  |
| json_loads                 | 31.4 us                                                  | 39.3 us: 1.25x slower                                                   |
| json                       | 5.61 ms                                                  | 7.03 ms: 1.25x slower                                                   |
| deepcopy                   | 451 us                                                   | 571 us: 1.26x slower                                                    |
| async_tree_none            | 493 ms                                                   | 625 ms: 1.27x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.41 sec: 1.28x slower                                                  |
| scimark_fft                | 447 ms                                                   | 573 ms: 1.28x slower                                                    |
| mdp                        | 3.36 sec                                                 | 4.32 sec: 1.29x slower                                                  |
| telco                      | 9.73 ms                                                  | 12.8 ms: 1.31x slower                                                   |
| async_generators           | 496 ms                                                   | 653 ms: 1.32x slower                                                    |
| json_dumps                 | 13.4 ms                                                  | 17.9 ms: 1.34x slower                                                   |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 8.82 ms: 1.34x slower                                                   |
| python_startup             | 13.3 ms                                                  | 18.2 ms: 1.37x slower                                                   |
| coverage                   | 98.5 ms                                                  | 136 ms: 1.38x slower                                                    |
| python_startup_no_site     | 8.75 ms                                                  | 12.2 ms: 1.40x slower                                                   |
| docutils                   | 2.91 sec                                                 | 4.10 sec: 1.41x slower                                                  |
| deepcopy_memo              | 51.0 us                                                  | 72.1 us: 1.41x slower                                                   |
| xml_etree_generate         | 113 ms                                                   | 163 ms: 1.44x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 40.9 ms: 1.45x slower                                                   |
| meteor_contest             | 113 ms                                                   | 167 ms: 1.47x slower                                                    |
| pylint                     | 343 ms                                                   | 511 ms: 1.49x slower                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 6.14 us: 1.51x slower                                                   |
| generators                 | 37.8 ms                                                  | 57.7 ms: 1.52x slower                                                   |
| nqueens                    | 98.7 ms                                                  | 152 ms: 1.55x slower                                                    |
| tornado_http               | 131 ms                                                   | 207 ms: 1.57x slower                                                    |
| pycparser                  | 1.26 sec                                                 | 2.02 sec: 1.60x slower                                                  |
| spectral_norm              | 141 ms                                                   | 226 ms: 1.60x slower                                                    |
| bpe_tokeniser              | 5.90 sec                                                 | 9.48 sec: 1.61x slower                                                  |
| xml_etree_process          | 80.1 ms                                                  | 130 ms: 1.63x slower                                                    |
| fannkuch                   | 452 ms                                                   | 738 ms: 1.63x slower                                                    |
| crypto_pyaes               | 82.7 ms                                                  | 137 ms: 1.65x slower                                                    |
| sympy_integrate            | 21.0 ms                                                  | 34.7 ms: 1.65x slower                                                   |
| tomli_loads                | 2.53 sec                                                 | 4.19 sec: 1.66x slower                                                  |
| bench_thread_pool          | 1.28 ms                                                  | 2.13 ms: 1.67x slower                                                   |
| 2to3                       | 306 ms                                                   | 518 ms: 1.69x slower                                                    |
| genshi_xml                 | 60.2 ms                                                  | 104 ms: 1.73x slower                                                    |
| typing_runtime_protocols   | 192 us                                                   | 336 us: 1.75x slower                                                    |
| thrift                     | 946 us                                                   | 1.69 ms: 1.78x slower                                                   |
| pyflate                    | 556 ms                                                   | 1.02 sec: 1.84x slower                                                  |
| sqlglot_normalize          | 128 ms                                                   | 237 ms: 1.84x slower                                                    |
| html5lib                   | 64.3 ms                                                  | 121 ms: 1.88x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.76 sec: 1.90x slower                                                  |
| sqlglot_optimize           | 62.4 ms                                                  | 119 ms: 1.90x slower                                                    |
| pprint_pformat             | 1.90 sec                                                 | 3.64 sec: 1.92x slower                                                  |
| genshi_text                | 27.7 ms                                                  | 53.3 ms: 1.93x slower                                                   |
| sympy_str                  | 264 ms                                                   | 514 ms: 1.95x slower                                                    |
| django_template            | 42.3 ms                                                  | 83.4 ms: 1.97x slower                                                   |
| comprehensions             | 20.4 us                                                  | 40.9 us: 2.01x slower                                                   |
| regex_compile              | 128 ms                                                   | 259 ms: 2.02x slower                                                    |
| logging_format             | 7.83 us                                                  | 15.9 us: 2.03x slower                                                   |
| logging_simple             | 7.04 us                                                  | 14.6 us: 2.08x slower                                                   |
| scimark_monte_carlo        | 83.8 ms                                                  | 176 ms: 2.10x slower                                                    |
| logging_silent             | 135 ns                                                   | 284 ns: 2.10x slower                                                    |
| sympy_expand               | 455 ms                                                   | 961 ms: 2.11x slower                                                    |
| unpickle_pure_python       | 254 us                                                   | 542 us: 2.13x slower                                                    |
| scimark_sor                | 159 ms                                                   | 341 ms: 2.14x slower                                                    |
| pickle_pure_python         | 359 us                                                   | 777 us: 2.16x slower                                                    |
| mako                       | 13.3 ms                                                  | 28.9 ms: 2.17x slower                                                   |
| richards                   | 53.5 ms                                                  | 117 ms: 2.18x slower                                                    |
| float                      | 94.4 ms                                                  | 207 ms: 2.20x slower                                                    |
| sympy_sum                  | 143 ms                                                   | 318 ms: 2.21x slower                                                    |
| hexiom                     | 7.13 ms                                                  | 15.9 ms: 2.23x slower                                                   |
| chaos                      | 68.8 ms                                                  | 160 ms: 2.32x slower                                                    |
| richards_super             | 60.3 ms                                                  | 143 ms: 2.36x slower                                                    |
| nbody                      | 114 ms                                                   | 281 ms: 2.46x slower                                                    |
| go                         | 163 ms                                                   | 404 ms: 2.49x slower                                                    |
| scimark_lu                 | 139 ms                                                   | 350 ms: 2.51x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 4.45 ms: 2.57x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 3.67 ms: 2.66x slower                                                   |
| raytrace                   | 298 ms                                                   | 815 ms: 2.74x slower                                                    |
| unpack_sequence            | 57.2 ns                                                  | 182 ns: 3.19x slower                                                    |
| deltablue                  | 3.85 ms                                                  | 12.7 ms: 3.30x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.56x slower                                                            |

Benchmark hidden because not significant (2): pidigits, pickle_list
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240907-3.14.0a0-11fa119-NOGIL/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.49x
- 95% likely to have a slowdown of 1.45x
- 99% likely to have a slowdown of 1.41x

# Memory
- memory change: 1.17x