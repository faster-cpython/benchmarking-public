# Results vs. 3.13.0

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: linux-aarch64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.254x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 471 ms: 1.50x slower                                                     |
| docutils       | 2.96 sec                                                 | 3.71 sec: 1.25x slower                                                   |
| html5lib       | 65.6 ms                                                  | 110 ms: 1.68x slower                                                     |
| sphinx         | 1.20 sec                                                 | 1.51 sec: 1.26x slower                                                   |
| Geometric mean | (ref)                                                    | 1.41x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg | 663 ms                                                   | 635 ms: 1.04x faster                                                     |
| async_tree_io             | 1.14 sec                                                 | 1.21 sec: 1.06x slower                                                   |
| async_tree_none_tg        | 484 ms                                                   | 519 ms: 1.07x slower                                                     |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 850 ms: 1.08x slower                                                     |
| async_tree_none           | 504 ms                                                   | 543 ms: 1.08x slower                                                     |
| coroutines                | 29.4 ms                                                  | 34.4 ms: 1.17x slower                                                    |
| async_generators          | 500 ms                                                   | 621 ms: 1.24x slower                                                     |
| Geometric mean            | (ref)                                                    | 1.06x slower                                                             |

Benchmark hidden because not significant (4): async_tree_memoization, asyncio_websockets, async_tree_io_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 118 ms                                                   | 191 ms: 1.61x slower                                                     |
| float          | 95.8 ms                                                  | 162 ms: 1.69x slower                                                     |
| Geometric mean | (ref)                                                    | 1.40x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.13 ms: 1.24x faster                                                    |
| regex_compile  | 134 ms                                                   | 195 ms: 1.46x slower                                                     |
| Geometric mean | (ref)                                                    | 1.05x slower                                                             |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 203 ms                                                   | 180 ms: 1.13x faster                                                     |
| xml_etree_iterparse  | 159 ms                                                   | 142 ms: 1.12x faster                                                     |
| json_loads           | 32.8 us                                                  | 37.3 us: 1.14x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 143 ms: 1.21x slower                                                     |
| json_dumps           | 14.2 ms                                                  | 18.6 ms: 1.31x slower                                                    |
| tomli_loads          | 2.67 sec                                                 | 3.58 sec: 1.34x slower                                                   |
| xml_etree_process    | 82.1 ms                                                  | 111 ms: 1.35x slower                                                     |
| unpickle_pure_python | 265 us                                                   | 467 us: 1.76x slower                                                     |
| pickle_pure_python   | 374 us                                                   | 701 us: 1.88x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.27x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 20.6 ms: 1.29x slower                                                    |
| python_startup_no_site | 8.79 ms                                                  | 12.4 ms: 1.41x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.34x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 85.3 ms: 1.39x slower                                                    |
| genshi_text     | 28.6 ms                                                  | 40.4 ms: 1.41x slower                                                    |
| django_template | 39.4 ms                                                  | 65.9 ms: 1.67x slower                                                    |
| mako            | 14.0 ms                                                  | 25.2 ms: 1.80x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.56x slower                                                             |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot              | 5.10 ms                                                  | 4.13 ms: 1.24x faster                                                    |
| gc_traversal              | 5.92 ms                                                  | 5.02 ms: 1.18x faster                                                    |
| create_gc_cycles          | 3.39 ms                                                  | 2.92 ms: 1.16x faster                                                    |
| xml_etree_parse           | 203 ms                                                   | 180 ms: 1.13x faster                                                     |
| xml_etree_iterparse       | 159 ms                                                   | 142 ms: 1.12x faster                                                     |
| deepcopy                  | 479 us                                                   | 437 us: 1.10x faster                                                     |
| sqlite_synth              | 4.08 us                                                  | 3.80 us: 1.07x faster                                                    |
| async_tree_memoization_tg | 663 ms                                                   | 635 ms: 1.04x faster                                                     |
| async_tree_io             | 1.14 sec                                                 | 1.21 sec: 1.06x slower                                                   |
| async_tree_none_tg        | 484 ms                                                   | 519 ms: 1.07x slower                                                     |
| json                      | 5.94 ms                                                  | 6.37 ms: 1.07x slower                                                    |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 850 ms: 1.08x slower                                                     |
| async_tree_none           | 504 ms                                                   | 543 ms: 1.08x slower                                                     |
| deepcopy_memo             | 53.0 us                                                  | 57.4 us: 1.08x slower                                                    |
| scimark_fft               | 463 ms                                                   | 509 ms: 1.10x slower                                                     |
| k_core                    | 2.99 sec                                                 | 3.30 sec: 1.10x slower                                                   |
| json_loads                | 32.8 us                                                  | 37.3 us: 1.14x slower                                                    |
| deepcopy_reduce           | 4.24 us                                                  | 4.87 us: 1.15x slower                                                    |
| spectral_norm             | 143 ms                                                   | 165 ms: 1.15x slower                                                     |
| coroutines                | 29.4 ms                                                  | 34.4 ms: 1.17x slower                                                    |
| mdp                       | 3.45 sec                                                 | 4.05 sec: 1.18x slower                                                   |
| telco                     | 10.5 ms                                                  | 12.4 ms: 1.18x slower                                                    |
| xml_etree_generate        | 118 ms                                                   | 143 ms: 1.21x slower                                                     |
| async_generators          | 500 ms                                                   | 621 ms: 1.24x slower                                                     |
| scimark_sparse_mat_mult   | 6.66 ms                                                  | 8.32 ms: 1.25x slower                                                    |
| docutils                  | 2.96 sec                                                 | 3.71 sec: 1.25x slower                                                   |
| connected_components      | 547 ms                                                   | 685 ms: 1.25x slower                                                     |
| shortest_path             | 565 ms                                                   | 708 ms: 1.25x slower                                                     |
| sphinx                    | 1.20 sec                                                 | 1.51 sec: 1.26x slower                                                   |
| pycparser                 | 1.34 sec                                                 | 1.71 sec: 1.28x slower                                                   |
| python_startup            | 16.0 ms                                                  | 20.6 ms: 1.29x slower                                                    |
| pylint                    | 345 ms                                                   | 446 ms: 1.29x slower                                                     |
| json_dumps                | 14.2 ms                                                  | 18.6 ms: 1.31x slower                                                    |
| nqueens                   | 105 ms                                                   | 138 ms: 1.32x slower                                                     |
| sqlglot_optimize          | 65.2 ms                                                  | 86.3 ms: 1.32x slower                                                    |
| bpe_tokeniser             | 6.02 sec                                                 | 7.99 sec: 1.33x slower                                                   |
| sqlglot_normalize         | 131 ms                                                   | 176 ms: 1.34x slower                                                     |
| tomli_loads               | 2.67 sec                                                 | 3.58 sec: 1.34x slower                                                   |
| coverage                  | 106 ms                                                   | 143 ms: 1.35x slower                                                     |
| xml_etree_process         | 82.1 ms                                                  | 111 ms: 1.35x slower                                                     |
| sympy_sum                 | 151 ms                                                   | 206 ms: 1.36x slower                                                     |
| genshi_xml                | 61.6 ms                                                  | 85.3 ms: 1.39x slower                                                    |
| thrift                    | 1.01 ms                                                  | 1.41 ms: 1.39x slower                                                    |
| meteor_contest            | 117 ms                                                   | 163 ms: 1.40x slower                                                     |
| python_startup_no_site    | 8.79 ms                                                  | 12.4 ms: 1.41x slower                                                    |
| genshi_text               | 28.6 ms                                                  | 40.4 ms: 1.41x slower                                                    |
| generators                | 40.3 ms                                                  | 57.3 ms: 1.42x slower                                                    |
| sympy_integrate           | 21.4 ms                                                  | 30.5 ms: 1.42x slower                                                    |
| crypto_pyaes              | 84.9 ms                                                  | 122 ms: 1.44x slower                                                     |
| pprint_pformat            | 1.99 sec                                                 | 2.89 sec: 1.45x slower                                                   |
| sympy_expand              | 472 ms                                                   | 687 ms: 1.45x slower                                                     |
| pprint_safe_repr          | 962 ms                                                   | 1.40 sec: 1.46x slower                                                   |
| regex_compile             | 134 ms                                                   | 195 ms: 1.46x slower                                                     |
| typing_runtime_protocols  | 197 us                                                   | 290 us: 1.47x slower                                                     |
| fannkuch                  | 478 ms                                                   | 703 ms: 1.47x slower                                                     |
| 2to3                      | 313 ms                                                   | 471 ms: 1.50x slower                                                     |
| scimark_lu                | 146 ms                                                   | 220 ms: 1.51x slower                                                     |
| sympy_str                 | 265 ms                                                   | 400 ms: 1.51x slower                                                     |
| bench_thread_pool         | 1.34 ms                                                  | 2.02 ms: 1.51x slower                                                    |
| logging_format            | 8.10 us                                                  | 12.3 us: 1.52x slower                                                    |
| sqlalchemy_declarative    | 154 ms                                                   | 235 ms: 1.53x slower                                                     |
| logging_simple            | 7.25 us                                                  | 11.3 us: 1.56x slower                                                    |
| pyflate                   | 582 ms                                                   | 921 ms: 1.58x slower                                                     |
| nbody                     | 118 ms                                                   | 191 ms: 1.61x slower                                                     |
| many_optionals            | 626 us                                                   | 1.01 ms: 1.62x slower                                                    |
| sqlalchemy_imperative     | 16.1 ms                                                  | 26.7 ms: 1.65x slower                                                    |
| django_template           | 39.4 ms                                                  | 65.9 ms: 1.67x slower                                                    |
| html5lib                  | 65.6 ms                                                  | 110 ms: 1.68x slower                                                     |
| float                     | 95.8 ms                                                  | 162 ms: 1.69x slower                                                     |
| scimark_sor               | 164 ms                                                   | 288 ms: 1.75x slower                                                     |
| unpickle_pure_python      | 265 us                                                   | 467 us: 1.76x slower                                                     |
| scimark_monte_carlo       | 87.8 ms                                                  | 155 ms: 1.76x slower                                                     |
| richards_super            | 60.8 ms                                                  | 109 ms: 1.79x slower                                                     |
| richards                  | 54.5 ms                                                  | 98.2 ms: 1.80x slower                                                    |
| mako                      | 14.0 ms                                                  | 25.2 ms: 1.80x slower                                                    |
| hexiom                    | 7.34 ms                                                  | 13.4 ms: 1.82x slower                                                    |
| chaos                     | 70.7 ms                                                  | 129 ms: 1.83x slower                                                     |
| subparsers                | 20.3 ms                                                  | 38.0 ms: 1.87x slower                                                    |
| pickle_pure_python        | 374 us                                                   | 701 us: 1.88x slower                                                     |
| sqlglot_transpile         | 1.84 ms                                                  | 3.49 ms: 1.90x slower                                                    |
| comprehensions            | 20.8 us                                                  | 40.3 us: 1.94x slower                                                    |
| logging_silent            | 135 ns                                                   | 265 ns: 1.97x slower                                                     |
| go                        | 164 ms                                                   | 341 ms: 2.07x slower                                                     |
| raytrace                  | 310 ms                                                   | 664 ms: 2.14x slower                                                     |
| sqlglot_parse             | 1.43 ms                                                  | 3.11 ms: 2.17x slower                                                    |
| deltablue                 | 3.97 ms                                                  | 11.1 ms: 2.81x slower                                                    |
| bench_mp_pool             | 8.07 ms                                                  | 63.2 ms: 7.84x slower                                                    |
| Geometric mean            | (ref)                                                    | 1.38x slower                                                             |

Benchmark hidden because not significant (8): pidigits, async_tree_memoization, asyncio_websockets, async_tree_io_tg, regex_dna, regex_v8, async_tree_cpu_io_mixed_tg, pathlib
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (2) of results/bm-20241228-3.14.0a3+-f9a5a3a-NOGIL/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: dulwich_log, mypy2

- Geometric mean (including insignificant results): 1.254x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.26x
- 95% likely to have a slowdown of 1.25x
- 99% likely to have a slowdown of 1.21x

# Memory
- memory change: 1.21x