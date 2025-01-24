# Results vs. 3.13.0

- fork: nascheme
- ref: 1b4e8c39e99ce39b39c7
- machine: linux-aarch64
- commit hash: 1b4e8c3
- commit date: 2025-01-22
- overall geometric mean: 1.137x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 382 ms: 1.22x slower                                                       |
| docutils       | 2.96 sec                                                 | 3.38 sec: 1.14x slower                                                     |
| html5lib       | 65.6 ms                                                  | 79.2 ms: 1.21x slower                                                      |
| sphinx         | 1.20 sec                                                 | 1.38 sec: 1.15x slower                                                     |
| Geometric mean | (ref)                                                    | 1.18x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 484 ms: 1.37x faster                                                       |
| async_tree_io_tg           | 1.16 sec                                                 | 917 ms: 1.27x faster                                                       |
| async_tree_none_tg         | 484 ms                                                   | 389 ms: 1.24x faster                                                       |
| async_tree_memoization     | 664 ms                                                   | 545 ms: 1.22x faster                                                       |
| async_tree_io              | 1.14 sec                                                 | 952 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 682 ms: 1.17x faster                                                       |
| async_tree_none            | 504 ms                                                   | 430 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 721 ms: 1.09x faster                                                       |
| async_generators           | 500 ms                                                   | 533 ms: 1.07x slower                                                       |
| coroutines                 | 29.4 ms                                                  | 33.3 ms: 1.13x slower                                                      |
| Geometric mean             | (ref)                                                    | 1.13x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 102 ms: 1.06x slower                                                       |
| nbody          | 118 ms                                                   | 188 ms: 1.59x slower                                                       |
| Geometric mean | (ref)                                                    | 1.18x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.11 ms: 1.24x faster                                                      |
| regex_compile  | 134 ms                                                   | 162 ms: 1.21x slower                                                       |
| Geometric mean | (ref)                                                    | 1.02x faster                                                               |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 32.8 us                                                  | 37.6 us: 1.15x slower                                                      |
| unpickle_pure_python | 265 us                                                   | 315 us: 1.19x slower                                                       |
| json_dumps           | 14.2 ms                                                  | 16.9 ms: 1.19x slower                                                      |
| tomli_loads          | 2.67 sec                                                 | 3.18 sec: 1.19x slower                                                     |
| pickle_pure_python   | 374 us                                                   | 480 us: 1.29x slower                                                       |
| Geometric mean       | (ref)                                                    | 1.20x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 20.4 ms: 1.27x slower                                                      |
| python_startup_no_site | 8.79 ms                                                  | 12.3 ms: 1.39x slower                                                      |
| Geometric mean         | (ref)                                                    | 1.33x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|-----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 77.9 ms: 1.26x slower                                                      |
| genshi_text     | 28.6 ms                                                  | 38.5 ms: 1.35x slower                                                      |
| django_template | 39.4 ms                                                  | 57.2 ms: 1.45x slower                                                      |
| mako            | 14.0 ms                                                  | 23.3 ms: 1.67x slower                                                      |
| Geometric mean  | (ref)                                                    | 1.42x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------------:|
| create_gc_cycles           | 3.39 ms                                                  | 2.29 ms: 1.48x faster                                                      |
| async_tree_memoization_tg  | 663 ms                                                   | 484 ms: 1.37x faster                                                       |
| async_tree_io_tg           | 1.16 sec                                                 | 917 ms: 1.27x faster                                                       |
| async_tree_none_tg         | 484 ms                                                   | 389 ms: 1.24x faster                                                       |
| regex_effbot               | 5.10 ms                                                  | 4.11 ms: 1.24x faster                                                      |
| async_tree_memoization     | 664 ms                                                   | 545 ms: 1.22x faster                                                       |
| async_tree_io              | 1.14 sec                                                 | 952 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 682 ms: 1.17x faster                                                       |
| async_tree_none            | 504 ms                                                   | 430 ms: 1.17x faster                                                       |
| deepcopy                   | 479 us                                                   | 433 us: 1.11x faster                                                       |
| sqlite_synth               | 4.08 us                                                  | 3.71 us: 1.10x faster                                                      |
| gc_traversal               | 5.92 ms                                                  | 5.41 ms: 1.10x faster                                                      |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 721 ms: 1.09x faster                                                       |
| scimark_fft                | 463 ms                                                   | 490 ms: 1.06x slower                                                       |
| float                      | 95.8 ms                                                  | 102 ms: 1.06x slower                                                       |
| async_generators           | 500 ms                                                   | 533 ms: 1.07x slower                                                       |
| json                       | 5.94 ms                                                  | 6.41 ms: 1.08x slower                                                      |
| pycparser                  | 1.34 sec                                                 | 1.46 sec: 1.08x slower                                                     |
| scimark_sor                | 164 ms                                                   | 179 ms: 1.09x slower                                                       |
| generators                 | 40.3 ms                                                  | 44.0 ms: 1.09x slower                                                      |
| deepcopy_reduce            | 4.24 us                                                  | 4.65 us: 1.09x slower                                                      |
| k_core                     | 2.99 sec                                                 | 3.29 sec: 1.10x slower                                                     |
| go                         | 164 ms                                                   | 181 ms: 1.10x slower                                                       |
| telco                      | 10.5 ms                                                  | 11.7 ms: 1.12x slower                                                      |
| mdp                        | 3.45 sec                                                 | 3.87 sec: 1.12x slower                                                     |
| coroutines                 | 29.4 ms                                                  | 33.3 ms: 1.13x slower                                                      |
| pylint                     | 345 ms                                                   | 392 ms: 1.13x slower                                                       |
| docutils                   | 2.96 sec                                                 | 3.38 sec: 1.14x slower                                                     |
| sphinx                     | 1.20 sec                                                 | 1.38 sec: 1.15x slower                                                     |
| json_loads                 | 32.8 us                                                  | 37.6 us: 1.15x slower                                                      |
| pyflate                    | 582 ms                                                   | 674 ms: 1.16x slower                                                       |
| logging_silent             | 135 ns                                                   | 157 ns: 1.17x slower                                                       |
| unpickle_pure_python       | 265 us                                                   | 315 us: 1.19x slower                                                       |
| json_dumps                 | 14.2 ms                                                  | 16.9 ms: 1.19x slower                                                      |
| tomli_loads                | 2.67 sec                                                 | 3.18 sec: 1.19x slower                                                     |
| pprint_pformat             | 1.99 sec                                                 | 2.38 sec: 1.20x slower                                                     |
| pprint_safe_repr           | 962 ms                                                   | 1.15 sec: 1.20x slower                                                     |
| html5lib                   | 65.6 ms                                                  | 79.2 ms: 1.21x slower                                                      |
| regex_compile              | 134 ms                                                   | 162 ms: 1.21x slower                                                       |
| sqlglot_normalize          | 131 ms                                                   | 159 ms: 1.22x slower                                                       |
| sqlglot_optimize           | 65.2 ms                                                  | 79.3 ms: 1.22x slower                                                      |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 8.12 ms: 1.22x slower                                                      |
| 2to3                       | 313 ms                                                   | 382 ms: 1.22x slower                                                       |
| coverage                   | 106 ms                                                   | 129 ms: 1.22x slower                                                       |
| bpe_tokeniser              | 6.02 sec                                                 | 7.36 sec: 1.22x slower                                                     |
| connected_components       | 547 ms                                                   | 676 ms: 1.24x slower                                                       |
| logging_simple             | 7.25 us                                                  | 9.06 us: 1.25x slower                                                      |
| logging_format             | 8.10 us                                                  | 10.2 us: 1.25x slower                                                      |
| shortest_path              | 565 ms                                                   | 710 ms: 1.26x slower                                                       |
| genshi_xml                 | 61.6 ms                                                  | 77.9 ms: 1.26x slower                                                      |
| chaos                      | 70.7 ms                                                  | 89.8 ms: 1.27x slower                                                      |
| python_startup             | 16.0 ms                                                  | 20.4 ms: 1.27x slower                                                      |
| sympy_expand               | 472 ms                                                   | 605 ms: 1.28x slower                                                       |
| nqueens                    | 105 ms                                                   | 134 ms: 1.28x slower                                                       |
| pickle_pure_python         | 374 us                                                   | 480 us: 1.29x slower                                                       |
| thrift                     | 1.01 ms                                                  | 1.30 ms: 1.29x slower                                                      |
| sqlglot_transpile          | 1.84 ms                                                  | 2.41 ms: 1.31x slower                                                      |
| hexiom                     | 7.34 ms                                                  | 9.64 ms: 1.31x slower                                                      |
| meteor_contest             | 117 ms                                                   | 154 ms: 1.31x slower                                                       |
| scimark_lu                 | 146 ms                                                   | 192 ms: 1.32x slower                                                       |
| sympy_sum                  | 151 ms                                                   | 199 ms: 1.32x slower                                                       |
| sqlalchemy_declarative     | 154 ms                                                   | 203 ms: 1.32x slower                                                       |
| scimark_monte_carlo        | 87.8 ms                                                  | 117 ms: 1.33x slower                                                       |
| sympy_integrate            | 21.4 ms                                                  | 28.5 ms: 1.33x slower                                                      |
| genshi_text                | 28.6 ms                                                  | 38.5 ms: 1.35x slower                                                      |
| comprehensions             | 20.8 us                                                  | 28.2 us: 1.35x slower                                                      |
| richards                   | 54.5 ms                                                  | 74.4 ms: 1.36x slower                                                      |
| crypto_pyaes               | 84.9 ms                                                  | 116 ms: 1.37x slower                                                       |
| raytrace                   | 310 ms                                                   | 429 ms: 1.38x slower                                                       |
| sympy_str                  | 265 ms                                                   | 368 ms: 1.39x slower                                                       |
| sqlalchemy_imperative      | 16.1 ms                                                  | 22.4 ms: 1.39x slower                                                      |
| python_startup_no_site     | 8.79 ms                                                  | 12.3 ms: 1.39x slower                                                      |
| sqlglot_parse              | 1.43 ms                                                  | 2.02 ms: 1.41x slower                                                      |
| bench_thread_pool          | 1.34 ms                                                  | 1.89 ms: 1.42x slower                                                      |
| fannkuch                   | 478 ms                                                   | 680 ms: 1.42x slower                                                       |
| typing_runtime_protocols   | 197 us                                                   | 282 us: 1.43x slower                                                       |
| richards_super             | 60.8 ms                                                  | 87.2 ms: 1.43x slower                                                      |
| many_optionals             | 626 us                                                   | 901 us: 1.44x slower                                                       |
| django_template            | 39.4 ms                                                  | 57.2 ms: 1.45x slower                                                      |
| deltablue                  | 3.97 ms                                                  | 6.10 ms: 1.54x slower                                                      |
| nbody                      | 118 ms                                                   | 188 ms: 1.59x slower                                                       |
| subparsers                 | 20.3 ms                                                  | 33.4 ms: 1.64x slower                                                      |
| mako                       | 14.0 ms                                                  | 23.3 ms: 1.67x slower                                                      |
| bench_mp_pool              | 8.07 ms                                                  | 59.2 ms: 7.34x slower                                                      |
| Geometric mean             | (ref)                                                    | 1.19x slower                                                               |

Benchmark hidden because not significant (7): pathlib, regex_dna, pidigits, regex_v8, asyncio_websockets, deepcopy_memo, spectral_norm
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
Ignored benchmarks (1) of results/bm-20250122-3.14.0a4+-1b4e8c3-NOGIL/bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3.json: dulwich_log

- Geometric mean (including insignificant results): 1.137x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 1.23x