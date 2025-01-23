# Results vs. 3.13.0

- fork: mdboom
- ref: aa_test_2025_2
- machine: linux-aarch64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.137x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 383 ms: 1.22x slower                                               |
| docutils       | 2.96 sec                                                 | 3.41 sec: 1.15x slower                                             |
| html5lib       | 65.6 ms                                                  | 78.8 ms: 1.20x slower                                              |
| sphinx         | 1.20 sec                                                 | 1.38 sec: 1.15x slower                                             |
| Geometric mean | (ref)                                                    | 1.18x slower                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 495 ms: 1.34x faster                                               |
| async_tree_io_tg           | 1.16 sec                                                 | 926 ms: 1.26x faster                                               |
| async_tree_memoization     | 664 ms                                                   | 531 ms: 1.25x faster                                               |
| async_tree_none_tg         | 484 ms                                                   | 398 ms: 1.22x faster                                               |
| async_tree_io              | 1.14 sec                                                 | 954 ms: 1.19x faster                                               |
| async_tree_none            | 504 ms                                                   | 428 ms: 1.18x faster                                               |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 686 ms: 1.17x faster                                               |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 722 ms: 1.09x faster                                               |
| async_generators           | 500 ms                                                   | 537 ms: 1.07x slower                                               |
| coroutines                 | 29.4 ms                                                  | 32.8 ms: 1.12x slower                                              |
| Geometric mean             | (ref)                                                    | 1.13x faster                                                       |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 107 ms: 1.12x slower                                               |
| nbody          | 118 ms                                                   | 189 ms: 1.60x slower                                               |
| Geometric mean | (ref)                                                    | 1.21x slower                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.18 ms: 1.22x faster                                              |
| regex_compile  | 134 ms                                                   | 164 ms: 1.23x slower                                               |
| Geometric mean | (ref)                                                    | 1.01x slower                                                       |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 132 ms: 1.20x faster                                               |
| xml_etree_parse      | 203 ms                                                   | 187 ms: 1.09x faster                                               |
| json_loads           | 32.8 us                                                  | 37.0 us: 1.13x slower                                              |
| xml_etree_generate   | 118 ms                                                   | 141 ms: 1.19x slower                                               |
| json_dumps           | 14.2 ms                                                  | 17.1 ms: 1.21x slower                                              |
| tomli_loads          | 2.67 sec                                                 | 3.26 sec: 1.22x slower                                             |
| unpickle_pure_python | 265 us                                                   | 341 us: 1.29x slower                                               |
| xml_etree_process    | 82.1 ms                                                  | 108 ms: 1.32x slower                                               |
| pickle_pure_python   | 374 us                                                   | 499 us: 1.33x slower                                               |
| Geometric mean       | (ref)                                                    | 1.15x slower                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 20.1 ms: 1.25x slower                                              |
| python_startup_no_site | 8.79 ms                                                  | 12.1 ms: 1.38x slower                                              |
| Geometric mean         | (ref)                                                    | 1.31x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 80.5 ms: 1.31x slower                                              |
| genshi_text     | 28.6 ms                                                  | 38.4 ms: 1.34x slower                                              |
| django_template | 39.4 ms                                                  | 57.3 ms: 1.45x slower                                              |
| mako            | 14.0 ms                                                  | 23.0 ms: 1.65x slower                                              |
| Geometric mean  | (ref)                                                    | 1.43x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------:|
| create_gc_cycles           | 3.39 ms                                                  | 2.17 ms: 1.56x faster                                              |
| async_tree_memoization_tg  | 663 ms                                                   | 495 ms: 1.34x faster                                               |
| async_tree_io_tg           | 1.16 sec                                                 | 926 ms: 1.26x faster                                               |
| async_tree_memoization     | 664 ms                                                   | 531 ms: 1.25x faster                                               |
| regex_effbot               | 5.10 ms                                                  | 4.18 ms: 1.22x faster                                              |
| async_tree_none_tg         | 484 ms                                                   | 398 ms: 1.22x faster                                               |
| xml_etree_iterparse        | 159 ms                                                   | 132 ms: 1.20x faster                                               |
| async_tree_io              | 1.14 sec                                                 | 954 ms: 1.19x faster                                               |
| async_tree_none            | 504 ms                                                   | 428 ms: 1.18x faster                                               |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 686 ms: 1.17x faster                                               |
| sqlite_synth               | 4.08 us                                                  | 3.60 us: 1.13x faster                                              |
| deepcopy                   | 479 us                                                   | 426 us: 1.12x faster                                               |
| gc_traversal               | 5.92 ms                                                  | 5.36 ms: 1.10x faster                                              |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 722 ms: 1.09x faster                                               |
| xml_etree_parse            | 203 ms                                                   | 187 ms: 1.09x faster                                               |
| k_core                     | 2.99 sec                                                 | 3.20 sec: 1.07x slower                                             |
| scimark_fft                | 463 ms                                                   | 495 ms: 1.07x slower                                               |
| async_generators           | 500 ms                                                   | 537 ms: 1.07x slower                                               |
| json                       | 5.94 ms                                                  | 6.44 ms: 1.08x slower                                              |
| scimark_sor                | 164 ms                                                   | 179 ms: 1.09x slower                                               |
| pycparser                  | 1.34 sec                                                 | 1.47 sec: 1.09x slower                                             |
| go                         | 164 ms                                                   | 181 ms: 1.10x slower                                               |
| generators                 | 40.3 ms                                                  | 44.7 ms: 1.11x slower                                              |
| coroutines                 | 29.4 ms                                                  | 32.8 ms: 1.12x slower                                              |
| float                      | 95.8 ms                                                  | 107 ms: 1.12x slower                                               |
| deepcopy_reduce            | 4.24 us                                                  | 4.77 us: 1.12x slower                                              |
| mdp                        | 3.45 sec                                                 | 3.87 sec: 1.12x slower                                             |
| json_loads                 | 32.8 us                                                  | 37.0 us: 1.13x slower                                              |
| pylint                     | 345 ms                                                   | 389 ms: 1.13x slower                                               |
| telco                      | 10.5 ms                                                  | 11.8 ms: 1.13x slower                                              |
| pyflate                    | 582 ms                                                   | 665 ms: 1.14x slower                                               |
| docutils                   | 2.96 sec                                                 | 3.41 sec: 1.15x slower                                             |
| sphinx                     | 1.20 sec                                                 | 1.38 sec: 1.15x slower                                             |
| logging_silent             | 135 ns                                                   | 157 ns: 1.16x slower                                               |
| xml_etree_generate         | 118 ms                                                   | 141 ms: 1.19x slower                                               |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.95 ms: 1.19x slower                                              |
| sqlglot_optimize           | 65.2 ms                                                  | 77.8 ms: 1.19x slower                                              |
| sqlglot_normalize          | 131 ms                                                   | 156 ms: 1.19x slower                                               |
| html5lib                   | 65.6 ms                                                  | 78.8 ms: 1.20x slower                                              |
| connected_components       | 547 ms                                                   | 657 ms: 1.20x slower                                               |
| json_dumps                 | 14.2 ms                                                  | 17.1 ms: 1.21x slower                                              |
| pprint_pformat             | 1.99 sec                                                 | 2.41 sec: 1.21x slower                                             |
| pprint_safe_repr           | 962 ms                                                   | 1.17 sec: 1.21x slower                                             |
| tomli_loads                | 2.67 sec                                                 | 3.26 sec: 1.22x slower                                             |
| coverage                   | 106 ms                                                   | 129 ms: 1.22x slower                                               |
| 2to3                       | 313 ms                                                   | 383 ms: 1.22x slower                                               |
| shortest_path              | 565 ms                                                   | 691 ms: 1.22x slower                                               |
| regex_compile              | 134 ms                                                   | 164 ms: 1.23x slower                                               |
| bpe_tokeniser              | 6.02 sec                                                 | 7.44 sec: 1.24x slower                                             |
| logging_format             | 8.10 us                                                  | 10.1 us: 1.24x slower                                              |
| thrift                     | 1.01 ms                                                  | 1.26 ms: 1.24x slower                                              |
| python_startup             | 16.0 ms                                                  | 20.1 ms: 1.25x slower                                              |
| sympy_sum                  | 151 ms                                                   | 190 ms: 1.26x slower                                               |
| logging_simple             | 7.25 us                                                  | 9.22 us: 1.27x slower                                              |
| chaos                      | 70.7 ms                                                  | 90.1 ms: 1.27x slower                                              |
| scimark_monte_carlo        | 87.8 ms                                                  | 112 ms: 1.27x slower                                               |
| unpickle_pure_python       | 265 us                                                   | 341 us: 1.29x slower                                               |
| nqueens                    | 105 ms                                                   | 135 ms: 1.29x slower                                               |
| scimark_lu                 | 146 ms                                                   | 189 ms: 1.30x slower                                               |
| crypto_pyaes               | 84.9 ms                                                  | 111 ms: 1.31x slower                                               |
| genshi_xml                 | 61.6 ms                                                  | 80.5 ms: 1.31x slower                                              |
| sympy_expand               | 472 ms                                                   | 617 ms: 1.31x slower                                               |
| hexiom                     | 7.34 ms                                                  | 9.66 ms: 1.32x slower                                              |
| xml_etree_process          | 82.1 ms                                                  | 108 ms: 1.32x slower                                               |
| pickle_pure_python         | 374 us                                                   | 499 us: 1.33x slower                                               |
| genshi_text                | 28.6 ms                                                  | 38.4 ms: 1.34x slower                                              |
| meteor_contest             | 117 ms                                                   | 158 ms: 1.35x slower                                               |
| sqlalchemy_declarative     | 154 ms                                                   | 208 ms: 1.35x slower                                               |
| sympy_integrate            | 21.4 ms                                                  | 29.2 ms: 1.36x slower                                              |
| raytrace                   | 310 ms                                                   | 425 ms: 1.37x slower                                               |
| sqlglot_transpile          | 1.84 ms                                                  | 2.52 ms: 1.37x slower                                              |
| comprehensions             | 20.8 us                                                  | 28.6 us: 1.37x slower                                              |
| python_startup_no_site     | 8.79 ms                                                  | 12.1 ms: 1.38x slower                                              |
| sympy_str                  | 265 ms                                                   | 370 ms: 1.40x slower                                               |
| richards_super             | 60.8 ms                                                  | 85.0 ms: 1.40x slower                                              |
| sqlglot_parse              | 1.43 ms                                                  | 2.02 ms: 1.41x slower                                              |
| richards                   | 54.5 ms                                                  | 77.1 ms: 1.41x slower                                              |
| fannkuch                   | 478 ms                                                   | 677 ms: 1.42x slower                                               |
| bench_thread_pool          | 1.34 ms                                                  | 1.91 ms: 1.43x slower                                              |
| django_template            | 39.4 ms                                                  | 57.3 ms: 1.45x slower                                              |
| sqlalchemy_imperative      | 16.1 ms                                                  | 23.9 ms: 1.48x slower                                              |
| many_optionals             | 626 us                                                   | 940 us: 1.50x slower                                               |
| typing_runtime_protocols   | 197 us                                                   | 305 us: 1.55x slower                                               |
| deltablue                  | 3.97 ms                                                  | 6.16 ms: 1.55x slower                                              |
| nbody                      | 118 ms                                                   | 189 ms: 1.60x slower                                               |
| mako                       | 14.0 ms                                                  | 23.0 ms: 1.65x slower                                              |
| subparsers                 | 20.3 ms                                                  | 33.8 ms: 1.66x slower                                              |
| bench_mp_pool              | 8.07 ms                                                  | 59.7 ms: 7.40x slower                                              |
| Geometric mean             | (ref)                                                    | 1.19x slower                                                       |

Benchmark hidden because not significant (7): pathlib, regex_v8, pidigits, deepcopy_memo, asyncio_websockets, regex_dna, spectral_norm
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250123-3.14.0a4+-8ffb2c1-NOGIL/bm-20250123-arminc-aarch64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1.json: dulwich_log

- Geometric mean (including insignificant results): 1.137x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 1.22x