# Results vs. 3.13.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: linux-aarch64
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.285x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 472 ms: 1.51x slower                                                     |
| docutils       | 2.96 sec                                                 | 3.83 sec: 1.29x slower                                                   |
| html5lib       | 65.6 ms                                                  | 117 ms: 1.78x slower                                                     |
| sphinx         | 1.20 sec                                                 | 1.51 sec: 1.25x slower                                                   |
| Geometric mean | (ref)                                                    | 1.44x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 687 ms: 1.04x slower                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 869 ms: 1.09x slower                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 1.29 sec: 1.10x slower                                                   |
| async_tree_memoization     | 664 ms                                                   | 735 ms: 1.11x slower                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 895 ms: 1.13x slower                                                     |
| async_tree_io              | 1.14 sec                                                 | 1.30 sec: 1.14x slower                                                   |
| coroutines                 | 29.4 ms                                                  | 33.8 ms: 1.15x slower                                                    |
| async_tree_none            | 504 ms                                                   | 587 ms: 1.16x slower                                                     |
| async_tree_none_tg         | 484 ms                                                   | 575 ms: 1.19x slower                                                     |
| async_generators           | 500 ms                                                   | 635 ms: 1.27x slower                                                     |
| Geometric mean             | (ref)                                                    | 1.13x slower                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 118 ms                                                   | 193 ms: 1.63x slower                                                     |
| float          | 95.8 ms                                                  | 194 ms: 2.03x slower                                                     |
| Geometric mean | (ref)                                                    | 1.49x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.31 ms: 1.18x faster                                                    |
| regex_compile  | 134 ms                                                   | 201 ms: 1.51x slower                                                     |
| Geometric mean | (ref)                                                    | 1.08x slower                                                             |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 138 ms: 1.15x faster                                                     |
| xml_etree_parse      | 203 ms                                                   | 183 ms: 1.10x faster                                                     |
| json_loads           | 32.8 us                                                  | 36.8 us: 1.12x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 144 ms: 1.22x slower                                                     |
| json_dumps           | 14.2 ms                                                  | 18.8 ms: 1.32x slower                                                    |
| tomli_loads          | 2.67 sec                                                 | 3.59 sec: 1.35x slower                                                   |
| xml_etree_process    | 82.1 ms                                                  | 113 ms: 1.38x slower                                                     |
| unpickle_pure_python | 265 us                                                   | 460 us: 1.74x slower                                                     |
| pickle_pure_python   | 374 us                                                   | 702 us: 1.88x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.27x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 21.5 ms: 1.34x slower                                                    |
| python_startup_no_site | 8.79 ms                                                  | 12.7 ms: 1.44x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.39x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 85.6 ms: 1.39x slower                                                    |
| genshi_text     | 28.6 ms                                                  | 42.4 ms: 1.48x slower                                                    |
| django_template | 39.4 ms                                                  | 66.9 ms: 1.70x slower                                                    |
| mako            | 14.0 ms                                                  | 25.7 ms: 1.84x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.59x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot               | 5.10 ms                                                  | 4.31 ms: 1.18x faster                                                    |
| gc_traversal               | 5.92 ms                                                  | 5.03 ms: 1.18x faster                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 2.95 ms: 1.15x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 138 ms: 1.15x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 183 ms: 1.10x faster                                                     |
| deepcopy                   | 479 us                                                   | 444 us: 1.08x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 687 ms: 1.04x slower                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 869 ms: 1.09x slower                                                     |
| k_core                     | 2.99 sec                                                 | 3.27 sec: 1.09x slower                                                   |
| scimark_fft                | 463 ms                                                   | 507 ms: 1.09x slower                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 1.29 sec: 1.10x slower                                                   |
| json                       | 5.94 ms                                                  | 6.57 ms: 1.11x slower                                                    |
| async_tree_memoization     | 664 ms                                                   | 735 ms: 1.11x slower                                                     |
| spectral_norm              | 143 ms                                                   | 160 ms: 1.11x slower                                                     |
| deepcopy_memo              | 53.0 us                                                  | 59.2 us: 1.12x slower                                                    |
| json_loads                 | 32.8 us                                                  | 36.8 us: 1.12x slower                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 895 ms: 1.13x slower                                                     |
| async_tree_io              | 1.14 sec                                                 | 1.30 sec: 1.14x slower                                                   |
| coroutines                 | 29.4 ms                                                  | 33.8 ms: 1.15x slower                                                    |
| telco                      | 10.5 ms                                                  | 12.1 ms: 1.15x slower                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 4.94 us: 1.16x slower                                                    |
| async_tree_none            | 504 ms                                                   | 587 ms: 1.16x slower                                                     |
| mdp                        | 3.45 sec                                                 | 4.09 sec: 1.19x slower                                                   |
| async_tree_none_tg         | 484 ms                                                   | 575 ms: 1.19x slower                                                     |
| xml_etree_generate         | 118 ms                                                   | 144 ms: 1.22x slower                                                     |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 8.17 ms: 1.23x slower                                                    |
| connected_components       | 547 ms                                                   | 685 ms: 1.25x slower                                                     |
| sphinx                     | 1.20 sec                                                 | 1.51 sec: 1.25x slower                                                   |
| async_generators           | 500 ms                                                   | 635 ms: 1.27x slower                                                     |
| shortest_path              | 565 ms                                                   | 723 ms: 1.28x slower                                                     |
| docutils                   | 2.96 sec                                                 | 3.83 sec: 1.29x slower                                                   |
| nqueens                    | 105 ms                                                   | 137 ms: 1.31x slower                                                     |
| json_dumps                 | 14.2 ms                                                  | 18.8 ms: 1.32x slower                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 8.01 sec: 1.33x slower                                                   |
| python_startup             | 16.0 ms                                                  | 21.5 ms: 1.34x slower                                                    |
| pylint                     | 345 ms                                                   | 463 ms: 1.34x slower                                                     |
| tomli_loads                | 2.67 sec                                                 | 3.59 sec: 1.35x slower                                                   |
| meteor_contest             | 117 ms                                                   | 158 ms: 1.35x slower                                                     |
| sqlglot_optimize           | 65.2 ms                                                  | 89.1 ms: 1.37x slower                                                    |
| xml_etree_process          | 82.1 ms                                                  | 113 ms: 1.38x slower                                                     |
| genshi_xml                 | 61.6 ms                                                  | 85.6 ms: 1.39x slower                                                    |
| coverage                   | 106 ms                                                   | 147 ms: 1.40x slower                                                     |
| generators                 | 40.3 ms                                                  | 56.6 ms: 1.40x slower                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.84 sec: 1.43x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 1.38 sec: 1.43x slower                                                   |
| sqlglot_normalize          | 131 ms                                                   | 189 ms: 1.44x slower                                                     |
| python_startup_no_site     | 8.79 ms                                                  | 12.7 ms: 1.44x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 123 ms: 1.45x slower                                                     |
| pycparser                  | 1.34 sec                                                 | 1.95 sec: 1.45x slower                                                   |
| fannkuch                   | 478 ms                                                   | 698 ms: 1.46x slower                                                     |
| genshi_text                | 28.6 ms                                                  | 42.4 ms: 1.48x slower                                                    |
| regex_compile              | 134 ms                                                   | 201 ms: 1.51x slower                                                     |
| 2to3                       | 313 ms                                                   | 472 ms: 1.51x slower                                                     |
| bench_thread_pool          | 1.34 ms                                                  | 2.03 ms: 1.52x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 305 us: 1.55x slower                                                     |
| sympy_integrate            | 21.4 ms                                                  | 33.2 ms: 1.55x slower                                                    |
| thrift                     | 1.01 ms                                                  | 1.61 ms: 1.59x slower                                                    |
| pyflate                    | 582 ms                                                   | 925 ms: 1.59x slower                                                     |
| sqlalchemy_declarative     | 154 ms                                                   | 248 ms: 1.62x slower                                                     |
| nbody                      | 118 ms                                                   | 193 ms: 1.63x slower                                                     |
| logging_format             | 8.10 us                                                  | 13.3 us: 1.65x slower                                                    |
| logging_simple             | 7.25 us                                                  | 12.0 us: 1.65x slower                                                    |
| many_optionals             | 626 us                                                   | 1.04 ms: 1.66x slower                                                    |
| django_template            | 39.4 ms                                                  | 66.9 ms: 1.70x slower                                                    |
| unpickle_pure_python       | 265 us                                                   | 460 us: 1.74x slower                                                     |
| sympy_str                  | 265 ms                                                   | 465 ms: 1.75x slower                                                     |
| sqlalchemy_imperative      | 16.1 ms                                                  | 28.4 ms: 1.77x slower                                                    |
| html5lib                   | 65.6 ms                                                  | 117 ms: 1.78x slower                                                     |
| scimark_lu                 | 146 ms                                                   | 268 ms: 1.83x slower                                                     |
| mako                       | 14.0 ms                                                  | 25.7 ms: 1.84x slower                                                    |
| sympy_expand               | 472 ms                                                   | 873 ms: 1.85x slower                                                     |
| hexiom                     | 7.34 ms                                                  | 13.7 ms: 1.86x slower                                                    |
| comprehensions             | 20.8 us                                                  | 38.9 us: 1.87x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 702 us: 1.88x slower                                                     |
| scimark_monte_carlo        | 87.8 ms                                                  | 166 ms: 1.89x slower                                                     |
| scimark_sor                | 164 ms                                                   | 313 ms: 1.91x slower                                                     |
| sympy_sum                  | 151 ms                                                   | 293 ms: 1.94x slower                                                     |
| richards_super             | 60.8 ms                                                  | 121 ms: 1.98x slower                                                     |
| chaos                      | 70.7 ms                                                  | 142 ms: 2.00x slower                                                     |
| logging_silent             | 135 ns                                                   | 270 ns: 2.01x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 40.9 ms: 2.01x slower                                                    |
| float                      | 95.8 ms                                                  | 194 ms: 2.03x slower                                                     |
| richards                   | 54.5 ms                                                  | 115 ms: 2.12x slower                                                     |
| sqlglot_transpile          | 1.84 ms                                                  | 3.97 ms: 2.16x slower                                                    |
| go                         | 164 ms                                                   | 378 ms: 2.30x slower                                                     |
| sqlglot_parse              | 1.43 ms                                                  | 3.34 ms: 2.33x slower                                                    |
| raytrace                   | 310 ms                                                   | 739 ms: 2.38x slower                                                     |
| deltablue                  | 3.97 ms                                                  | 12.2 ms: 3.09x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 62.8 ms: 7.79x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.44x slower                                                             |

Benchmark hidden because not significant (6): sqlite_synth, pidigits, pathlib, asyncio_websockets, regex_dna, regex_v8
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (2) of results/bm-20241214-3.14.0a2+-0ac40ac-NOGIL/bm-20241214-arminc-aarch64-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: dulwich_log, mypy2

- Geometric mean (including insignificant results): 1.285x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.30x
- 95% likely to have a slowdown of 1.28x
- 99% likely to have a slowdown of 1.25x

# Memory
- memory change: 1.22x