# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-aarch64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.55x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 509 ms: 1.67x slower                                                    |
| docutils       | 2.91 sec                                                 | 3.93 sec: 1.35x slower                                                  |
| html5lib       | 64.3 ms                                                  | 119 ms: 1.85x slower                                                    |
| tornado_http   | 131 ms                                                   | 202 ms: 1.54x slower                                                    |
| Geometric mean | (ref)                                                    | 1.59x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 656 ms                                                   | 672 ms: 1.02x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 692 ms: 1.07x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.47 sec: 1.13x slower                                                  |
| asyncio_tcp                | 568 ms                                                   | 653 ms: 1.15x slower                                                    |
| async_tree_memoization     | 626 ms                                                   | 730 ms: 1.17x slower                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 895 ms: 1.17x slower                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 865 ms: 1.18x slower                                                    |
| async_tree_none_tg         | 467 ms                                                   | 568 ms: 1.22x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.33 sec: 1.22x slower                                                  |
| async_tree_none            | 493 ms                                                   | 623 ms: 1.26x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.40 sec: 1.27x slower                                                  |
| async_generators           | 496 ms                                                   | 658 ms: 1.33x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 39.2 ms: 1.39x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.19x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 204 ms: 2.16x slower                                                    |
| nbody          | 114 ms                                                   | 279 ms: 2.44x slower                                                    |
| Geometric mean | (ref)                                                    | 1.74x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.87 ms                                                  | 4.44 ms: 1.10x faster                                                   |
| regex_dna      | 246 ms                                                   | 257 ms: 1.04x slower                                                    |
| regex_v8       | 31.5 ms                                                  | 33.2 ms: 1.05x slower                                                   |
| regex_compile  | 128 ms                                                   | 244 ms: 1.90x slower                                                    |
| Geometric mean | (ref)                                                    | 1.18x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 188 ms                                                   | 184 ms: 1.02x faster                                                    |
| pickle               | 13.5 us                                                  | 13.3 us: 1.01x faster                                                   |
| pickle_list          | 5.34 us                                                  | 5.30 us: 1.01x faster                                                   |
| pickle_dict          | 38.1 us                                                  | 39.2 us: 1.03x slower                                                   |
| unpickle             | 20.2 us                                                  | 21.4 us: 1.06x slower                                                   |
| xml_etree_iterparse  | 147 ms                                                   | 156 ms: 1.07x slower                                                    |
| unpickle_list        | 6.65 us                                                  | 7.10 us: 1.07x slower                                                   |
| json_loads           | 31.4 us                                                  | 37.3 us: 1.19x slower                                                   |
| json_dumps           | 13.4 ms                                                  | 17.4 ms: 1.30x slower                                                   |
| xml_etree_generate   | 113 ms                                                   | 157 ms: 1.39x slower                                                    |
| xml_etree_process    | 80.1 ms                                                  | 130 ms: 1.62x slower                                                    |
| tomli_loads          | 2.53 sec                                                 | 4.12 sec: 1.63x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 522 us: 2.05x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 751 us: 2.09x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.27x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 18.0 ms: 1.36x slower                                                   |
| python_startup_no_site | 8.75 ms                                                  | 11.9 ms: 1.36x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.36x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.2 ms                                                  | 100 ms: 1.67x slower                                                    |
| genshi_text     | 27.7 ms                                                  | 50.4 ms: 1.82x slower                                                   |
| django_template | 42.3 ms                                                  | 80.7 ms: 1.91x slower                                                   |
| mako            | 13.3 ms                                                  | 28.4 ms: 2.13x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.87x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 2.12 ms                                                  | 1.62 ms: 1.31x faster                                                   |
| gc_traversal               | 4.53 ms                                                  | 3.47 ms: 1.30x faster                                                   |
| regex_effbot               | 4.87 ms                                                  | 4.44 ms: 1.10x faster                                                   |
| xml_etree_parse            | 188 ms                                                   | 184 ms: 1.02x faster                                                    |
| pickle                     | 13.5 us                                                  | 13.3 us: 1.01x faster                                                   |
| pickle_list                | 5.34 us                                                  | 5.30 us: 1.01x faster                                                   |
| asyncio_websockets         | 656 ms                                                   | 672 ms: 1.02x slower                                                    |
| sqlite_synth               | 3.84 us                                                  | 3.94 us: 1.03x slower                                                   |
| pickle_dict                | 38.1 us                                                  | 39.2 us: 1.03x slower                                                   |
| regex_dna                  | 246 ms                                                   | 257 ms: 1.04x slower                                                    |
| regex_v8                   | 31.5 ms                                                  | 33.2 ms: 1.05x slower                                                   |
| unpickle                   | 20.2 us                                                  | 21.4 us: 1.06x slower                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 692 ms: 1.07x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                   | 156 ms: 1.07x slower                                                    |
| unpickle_list              | 6.65 us                                                  | 7.10 us: 1.07x slower                                                   |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.47 sec: 1.13x slower                                                  |
| asyncio_tcp                | 568 ms                                                   | 653 ms: 1.15x slower                                                    |
| async_tree_memoization     | 626 ms                                                   | 730 ms: 1.17x slower                                                    |
| deepcopy                   | 451 us                                                   | 528 us: 1.17x slower                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 895 ms: 1.17x slower                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 865 ms: 1.18x slower                                                    |
| pathlib                    | 22.4 ms                                                  | 26.4 ms: 1.18x slower                                                   |
| json                       | 5.61 ms                                                  | 6.65 ms: 1.18x slower                                                   |
| json_loads                 | 31.4 us                                                  | 37.3 us: 1.19x slower                                                   |
| async_tree_none_tg         | 467 ms                                                   | 568 ms: 1.22x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.33 sec: 1.22x slower                                                  |
| scimark_fft                | 447 ms                                                   | 560 ms: 1.25x slower                                                    |
| async_tree_none            | 493 ms                                                   | 623 ms: 1.26x slower                                                    |
| mdp                        | 3.36 sec                                                 | 4.26 sec: 1.27x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.40 sec: 1.27x slower                                                  |
| telco                      | 9.73 ms                                                  | 12.4 ms: 1.28x slower                                                   |
| json_dumps                 | 13.4 ms                                                  | 17.4 ms: 1.30x slower                                                   |
| coverage                   | 98.5 ms                                                  | 129 ms: 1.31x slower                                                    |
| deepcopy_memo              | 51.0 us                                                  | 67.1 us: 1.31x slower                                                   |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 8.70 ms: 1.32x slower                                                   |
| async_generators           | 496 ms                                                   | 658 ms: 1.33x slower                                                    |
| docutils                   | 2.91 sec                                                 | 3.93 sec: 1.35x slower                                                  |
| python_startup             | 13.3 ms                                                  | 18.0 ms: 1.36x slower                                                   |
| python_startup_no_site     | 8.75 ms                                                  | 11.9 ms: 1.36x slower                                                   |
| xml_etree_generate         | 113 ms                                                   | 157 ms: 1.39x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 39.2 ms: 1.39x slower                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 5.71 us: 1.40x slower                                                   |
| pylint                     | 343 ms                                                   | 498 ms: 1.45x slower                                                    |
| meteor_contest             | 113 ms                                                   | 167 ms: 1.47x slower                                                    |
| nqueens                    | 98.7 ms                                                  | 149 ms: 1.51x slower                                                    |
| generators                 | 37.8 ms                                                  | 57.3 ms: 1.52x slower                                                   |
| tornado_http               | 131 ms                                                   | 202 ms: 1.54x slower                                                    |
| bench_thread_pool          | 1.28 ms                                                  | 1.98 ms: 1.55x slower                                                   |
| bpe_tokeniser              | 5.90 sec                                                 | 9.20 sec: 1.56x slower                                                  |
| spectral_norm              | 141 ms                                                   | 220 ms: 1.56x slower                                                    |
| pycparser                  | 1.26 sec                                                 | 2.01 sec: 1.59x slower                                                  |
| xml_etree_process          | 80.1 ms                                                  | 130 ms: 1.62x slower                                                    |
| tomli_loads                | 2.53 sec                                                 | 4.12 sec: 1.63x slower                                                  |
| fannkuch                   | 452 ms                                                   | 743 ms: 1.64x slower                                                    |
| sympy_integrate            | 21.0 ms                                                  | 34.8 ms: 1.66x slower                                                   |
| crypto_pyaes               | 82.7 ms                                                  | 137 ms: 1.66x slower                                                    |
| genshi_xml                 | 60.2 ms                                                  | 100 ms: 1.67x slower                                                    |
| 2to3                       | 306 ms                                                   | 509 ms: 1.67x slower                                                    |
| typing_runtime_protocols   | 192 us                                                   | 322 us: 1.68x slower                                                    |
| sqlglot_normalize          | 128 ms                                                   | 218 ms: 1.70x slower                                                    |
| thrift                     | 946 us                                                   | 1.62 ms: 1.71x slower                                                   |
| sqlglot_optimize           | 62.4 ms                                                  | 111 ms: 1.78x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.66 sec: 1.79x slower                                                  |
| pprint_pformat             | 1.90 sec                                                 | 3.40 sec: 1.79x slower                                                  |
| pyflate                    | 556 ms                                                   | 1.00 sec: 1.80x slower                                                  |
| genshi_text                | 27.7 ms                                                  | 50.4 ms: 1.82x slower                                                   |
| html5lib                   | 64.3 ms                                                  | 119 ms: 1.85x slower                                                    |
| regex_compile              | 128 ms                                                   | 244 ms: 1.90x slower                                                    |
| sympy_str                  | 264 ms                                                   | 503 ms: 1.91x slower                                                    |
| django_template            | 42.3 ms                                                  | 80.7 ms: 1.91x slower                                                   |
| logging_format             | 7.83 us                                                  | 15.0 us: 1.91x slower                                                   |
| logging_simple             | 7.04 us                                                  | 13.8 us: 1.96x slower                                                   |
| comprehensions             | 20.4 us                                                  | 40.3 us: 1.97x slower                                                   |
| sympy_expand               | 455 ms                                                   | 926 ms: 2.04x slower                                                    |
| unpickle_pure_python       | 254 us                                                   | 522 us: 2.05x slower                                                    |
| scimark_monte_carlo        | 83.8 ms                                                  | 173 ms: 2.06x slower                                                    |
| logging_silent             | 135 ns                                                   | 281 ns: 2.08x slower                                                    |
| pickle_pure_python         | 359 us                                                   | 751 us: 2.09x slower                                                    |
| scimark_sor                | 159 ms                                                   | 336 ms: 2.11x slower                                                    |
| mako                       | 13.3 ms                                                  | 28.4 ms: 2.13x slower                                                   |
| hexiom                     | 7.13 ms                                                  | 15.3 ms: 2.14x slower                                                   |
| sympy_sum                  | 143 ms                                                   | 309 ms: 2.15x slower                                                    |
| float                      | 94.4 ms                                                  | 204 ms: 2.16x slower                                                    |
| richards                   | 53.5 ms                                                  | 118 ms: 2.21x slower                                                    |
| richards_super             | 60.3 ms                                                  | 136 ms: 2.25x slower                                                    |
| chaos                      | 68.8 ms                                                  | 157 ms: 2.28x slower                                                    |
| scimark_lu                 | 139 ms                                                   | 326 ms: 2.34x slower                                                    |
| go                         | 163 ms                                                   | 387 ms: 2.38x slower                                                    |
| nbody                      | 114 ms                                                   | 279 ms: 2.44x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 4.26 ms: 2.46x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 3.68 ms: 2.66x slower                                                   |
| raytrace                   | 298 ms                                                   | 803 ms: 2.70x slower                                                    |
| unpack_sequence            | 57.2 ns                                                  | 182 ns: 3.18x slower                                                    |
| deltablue                  | 3.85 ms                                                  | 12.4 ms: 3.23x slower                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 40.1 ms: 5.50x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.55x slower                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241005-3.14.0a0-16cd6cc-NOGIL/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.47x
- 95% likely to have a slowdown of 1.42x
- 99% likely to have a slowdown of 1.36x

# Memory
- memory change: 1.17x