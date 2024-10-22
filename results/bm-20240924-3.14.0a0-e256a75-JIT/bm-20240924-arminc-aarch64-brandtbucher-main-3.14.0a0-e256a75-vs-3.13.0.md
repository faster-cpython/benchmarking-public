# Results vs. 3.13.0

- fork: brandtbucher
- ref: main
- machine: linux-aarch64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 380 ms: 1.24x slower                                          |
| docutils       | 2.91 sec                                                 | 4.02 sec: 1.38x slower                                        |
| html5lib       | 64.3 ms                                                  | 72.5 ms: 1.13x slower                                         |
| tornado_http   | 131 ms                                                   | 150 ms: 1.15x slower                                          |
| Geometric mean | (ref)                                                    | 1.22x slower                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|---------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_memoization_tg | 649 ms                                                   | 568 ms: 1.14x faster                                          |
| async_tree_none           | 493 ms                                                   | 445 ms: 1.11x faster                                          |
| async_tree_none_tg        | 467 ms                                                   | 432 ms: 1.08x faster                                          |
| async_tree_memoization    | 626 ms                                                   | 588 ms: 1.06x faster                                          |
| asyncio_websockets        | 656 ms                                                   | 663 ms: 1.01x slower                                          |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.22 sec: 1.02x slower                                        |
| async_generators          | 496 ms                                                   | 507 ms: 1.02x slower                                          |
| async_tree_io             | 1.11 sec                                                 | 1.14 sec: 1.04x slower                                        |
| async_tree_io_tg          | 1.09 sec                                                 | 1.19 sec: 1.09x slower                                        |
| asyncio_tcp               | 568 ms                                                   | 623 ms: 1.10x slower                                          |
| Geometric mean            | (ref)                                                    | 1.01x faster                                                  |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 88.5 ms: 1.07x faster                                         |
| Geometric mean | (ref)                                                    | 1.02x faster                                                  |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 30.5 ms: 1.03x faster                                         |
| regex_effbot   | 4.87 ms                                                  | 4.96 ms: 1.02x slower                                         |
| regex_dna      | 246 ms                                                   | 255 ms: 1.04x slower                                          |
| regex_compile  | 128 ms                                                   | 197 ms: 1.54x slower                                          |
| Geometric mean | (ref)                                                    | 1.12x slower                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------|:--------------------------------------------------------:|:-------------------------------------------------------------:|
| unpickle_list        | 6.65 us                                                  | 6.37 us: 1.04x faster                                         |
| unpickle             | 20.2 us                                                  | 19.5 us: 1.03x faster                                         |
| xml_etree_generate   | 113 ms                                                   | 110 ms: 1.03x faster                                          |
| pickle_list          | 5.34 us                                                  | 5.22 us: 1.02x faster                                         |
| xml_etree_iterparse  | 147 ms                                                   | 148 ms: 1.01x slower                                          |
| pickle               | 13.5 us                                                  | 13.8 us: 1.02x slower                                         |
| tomli_loads          | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                        |
| unpickle_pure_python | 254 us                                                   | 266 us: 1.04x slower                                          |
| pickle_pure_python   | 359 us                                                   | 399 us: 1.11x slower                                          |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                  |

Benchmark hidden because not significant (5): xml_etree_parse, pickle_dict, json_dumps, json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:--------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                         |
| django_template | 42.3 ms                                                  | 51.0 ms: 1.21x slower                                         |
| genshi_text     | 27.7 ms                                                  | 34.6 ms: 1.25x slower                                         |
| genshi_xml      | 60.2 ms                                                  | 80.5 ms: 1.34x slower                                         |
| Geometric mean  | (ref)                                                    | 1.19x slower                                                  |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75 |
|---------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------:|
| deepcopy_memo             | 51.0 us                                                  | 37.5 us: 1.36x faster                                         |
| async_tree_memoization_tg | 649 ms                                                   | 568 ms: 1.14x faster                                          |
| deepcopy                  | 451 us                                                   | 398 us: 1.13x faster                                          |
| async_tree_none           | 493 ms                                                   | 445 ms: 1.11x faster                                          |
| async_tree_none_tg        | 467 ms                                                   | 432 ms: 1.08x faster                                          |
| float                     | 94.4 ms                                                  | 88.5 ms: 1.07x faster                                         |
| async_tree_memoization    | 626 ms                                                   | 588 ms: 1.06x faster                                          |
| scimark_sor               | 159 ms                                                   | 151 ms: 1.05x faster                                          |
| unpickle_list             | 6.65 us                                                  | 6.37 us: 1.04x faster                                         |
| deepcopy_reduce           | 4.07 us                                                  | 3.90 us: 1.04x faster                                         |
| unpickle                  | 20.2 us                                                  | 19.5 us: 1.03x faster                                         |
| regex_v8                  | 31.5 ms                                                  | 30.5 ms: 1.03x faster                                         |
| xml_etree_generate        | 113 ms                                                   | 110 ms: 1.03x faster                                          |
| pathlib                   | 22.4 ms                                                  | 21.8 ms: 1.03x faster                                         |
| pickle_list               | 5.34 us                                                  | 5.22 us: 1.02x faster                                         |
| mako                      | 13.3 ms                                                  | 13.1 ms: 1.02x faster                                         |
| xml_etree_iterparse       | 147 ms                                                   | 148 ms: 1.01x slower                                          |
| thrift                    | 946 us                                                   | 953 us: 1.01x slower                                          |
| asyncio_websockets        | 656 ms                                                   | 663 ms: 1.01x slower                                          |
| sqlite_synth              | 3.84 us                                                  | 3.89 us: 1.01x slower                                         |
| regex_effbot              | 4.87 ms                                                  | 4.96 ms: 1.02x slower                                         |
| asyncio_tcp_ssl           | 2.18 sec                                                 | 2.22 sec: 1.02x slower                                        |
| async_generators          | 496 ms                                                   | 507 ms: 1.02x slower                                          |
| pickle                    | 13.5 us                                                  | 13.8 us: 1.02x slower                                         |
| scimark_fft               | 447 ms                                                   | 459 ms: 1.03x slower                                          |
| async_tree_io             | 1.11 sec                                                 | 1.14 sec: 1.04x slower                                        |
| regex_dna                 | 246 ms                                                   | 255 ms: 1.04x slower                                          |
| spectral_norm             | 141 ms                                                   | 146 ms: 1.04x slower                                          |
| mdp                       | 3.36 sec                                                 | 3.49 sec: 1.04x slower                                        |
| tomli_loads               | 2.53 sec                                                 | 2.63 sec: 1.04x slower                                        |
| logging_format            | 7.83 us                                                  | 8.16 us: 1.04x slower                                         |
| scimark_sparse_mat_mult   | 6.58 ms                                                  | 6.86 ms: 1.04x slower                                         |
| coverage                  | 98.5 ms                                                  | 103 ms: 1.04x slower                                          |
| unpickle_pure_python      | 254 us                                                   | 266 us: 1.04x slower                                          |
| logging_simple            | 7.04 us                                                  | 7.49 us: 1.06x slower                                         |
| bench_thread_pool         | 1.28 ms                                                  | 1.36 ms: 1.06x slower                                         |
| scimark_lu                | 139 ms                                                   | 149 ms: 1.07x slower                                          |
| crypto_pyaes              | 82.7 ms                                                  | 89.9 ms: 1.09x slower                                         |
| meteor_contest            | 113 ms                                                   | 124 ms: 1.09x slower                                          |
| async_tree_io_tg          | 1.09 sec                                                 | 1.19 sec: 1.09x slower                                        |
| asyncio_tcp               | 568 ms                                                   | 623 ms: 1.10x slower                                          |
| create_gc_cycles          | 2.12 ms                                                  | 2.33 ms: 1.10x slower                                         |
| telco                     | 9.73 ms                                                  | 10.7 ms: 1.10x slower                                         |
| scimark_monte_carlo       | 83.8 ms                                                  | 93.0 ms: 1.11x slower                                         |
| pickle_pure_python        | 359 us                                                   | 399 us: 1.11x slower                                          |
| typing_runtime_protocols  | 192 us                                                   | 215 us: 1.12x slower                                          |
| html5lib                  | 64.3 ms                                                  | 72.5 ms: 1.13x slower                                         |
| fannkuch                  | 452 ms                                                   | 510 ms: 1.13x slower                                          |
| pyflate                   | 556 ms                                                   | 628 ms: 1.13x slower                                          |
| gc_traversal              | 4.53 ms                                                  | 5.12 ms: 1.13x slower                                         |
| deltablue                 | 3.85 ms                                                  | 4.36 ms: 1.13x slower                                         |
| tornado_http              | 131 ms                                                   | 150 ms: 1.15x slower                                          |
| go                        | 163 ms                                                   | 186 ms: 1.15x slower                                          |
| raytrace                  | 298 ms                                                   | 347 ms: 1.17x slower                                          |
| comprehensions            | 20.4 us                                                  | 24.3 us: 1.19x slower                                         |
| pycparser                 | 1.26 sec                                                 | 1.51 sec: 1.19x slower                                        |
| sqlglot_normalize         | 128 ms                                                   | 154 ms: 1.20x slower                                          |
| django_template           | 42.3 ms                                                  | 51.0 ms: 1.21x slower                                         |
| 2to3                      | 306 ms                                                   | 380 ms: 1.24x slower                                          |
| richards                  | 53.5 ms                                                  | 66.6 ms: 1.25x slower                                         |
| genshi_text               | 27.7 ms                                                  | 34.6 ms: 1.25x slower                                         |
| sqlglot_parse             | 1.38 ms                                                  | 1.75 ms: 1.26x slower                                         |
| richards_super            | 60.3 ms                                                  | 76.3 ms: 1.27x slower                                         |
| sqlglot_optimize          | 62.4 ms                                                  | 79.1 ms: 1.27x slower                                         |
| sqlglot_transpile         | 1.73 ms                                                  | 2.21 ms: 1.28x slower                                         |
| nqueens                   | 98.7 ms                                                  | 127 ms: 1.29x slower                                          |
| chaos                     | 68.8 ms                                                  | 90.8 ms: 1.32x slower                                         |
| genshi_xml                | 60.2 ms                                                  | 80.5 ms: 1.34x slower                                         |
| sympy_expand              | 455 ms                                                   | 613 ms: 1.35x slower                                          |
| sympy_integrate           | 21.0 ms                                                  | 28.4 ms: 1.35x slower                                         |
| pprint_safe_repr          | 926 ms                                                   | 1.26 sec: 1.36x slower                                        |
| pprint_pformat            | 1.90 sec                                                 | 2.61 sec: 1.38x slower                                        |
| docutils                  | 2.91 sec                                                 | 4.02 sec: 1.38x slower                                        |
| pylint                    | 343 ms                                                   | 476 ms: 1.39x slower                                          |
| sympy_str                 | 264 ms                                                   | 366 ms: 1.39x slower                                          |
| hexiom                    | 7.13 ms                                                  | 10.2 ms: 1.43x slower                                         |
| sympy_sum                 | 143 ms                                                   | 209 ms: 1.46x slower                                          |
| generators                | 37.8 ms                                                  | 56.5 ms: 1.49x slower                                         |
| regex_compile             | 128 ms                                                   | 197 ms: 1.54x slower                                          |
| unpack_sequence           | 57.2 ns                                                  | 148 ns: 2.59x slower                                          |
| Geometric mean            | (ref)                                                    | 1.10x slower                                                  |

Benchmark hidden because not significant (16): python_startup, async_tree_cpu_io_mixed, python_startup_no_site, xml_etree_parse, pidigits, pickle_dict, async_tree_cpu_io_mixed_tg, nbody, bpe_tokeniser, json_dumps, coroutines, bench_mp_pool, logging_silent, json_loads, json, xml_etree_process
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240924-3.14.0a0-e256a75-JIT/bm-20240924-arminc-aarch64-brandtbucher-main-3.14.0a0-e256a75.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x