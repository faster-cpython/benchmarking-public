# Results vs. 3.13.0

- fork: python
- ref: 0cafa97932c6574734bb
- machine: linux-aarch64
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.248x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 468 ms: 1.50x slower                                                     |
| docutils       | 2.96 sec                                                 | 3.72 sec: 1.25x slower                                                   |
| html5lib       | 65.6 ms                                                  | 111 ms: 1.69x slower                                                     |
| sphinx         | 1.20 sec                                                 | 1.49 sec: 1.24x slower                                                   |
| Geometric mean | (ref)                                                    | 1.41x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg | 663 ms                                                   | 628 ms: 1.06x faster                                                     |
| async_tree_io             | 1.14 sec                                                 | 1.18 sec: 1.04x slower                                                   |
| async_tree_none_tg        | 484 ms                                                   | 510 ms: 1.05x slower                                                     |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 833 ms: 1.06x slower                                                     |
| async_tree_none           | 504 ms                                                   | 536 ms: 1.06x slower                                                     |
| coroutines                | 29.4 ms                                                  | 33.8 ms: 1.15x slower                                                    |
| async_generators          | 500 ms                                                   | 619 ms: 1.24x slower                                                     |
| Geometric mean            | (ref)                                                    | 1.05x slower                                                             |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_io_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 118 ms                                                   | 186 ms: 1.57x slower                                                     |
| float          | 95.8 ms                                                  | 154 ms: 1.60x slower                                                     |
| Geometric mean | (ref)                                                    | 1.37x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.15 ms: 1.23x faster                                                    |
| regex_compile  | 134 ms                                                   | 187 ms: 1.40x slower                                                     |
| Geometric mean | (ref)                                                    | 1.05x slower                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 137 ms: 1.16x faster                                                     |
| xml_etree_parse      | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| json_loads           | 32.8 us                                                  | 37.4 us: 1.14x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 145 ms: 1.22x slower                                                     |
| json_dumps           | 14.2 ms                                                  | 18.4 ms: 1.29x slower                                                    |
| xml_etree_process    | 82.1 ms                                                  | 109 ms: 1.33x slower                                                     |
| tomli_loads          | 2.67 sec                                                 | 3.60 sec: 1.35x slower                                                   |
| unpickle_pure_python | 265 us                                                   | 453 us: 1.71x slower                                                     |
| pickle_pure_python   | 374 us                                                   | 701 us: 1.88x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.26x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 20.4 ms: 1.27x slower                                                    |
| python_startup_no_site | 8.79 ms                                                  | 12.4 ms: 1.41x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.34x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 86.6 ms: 1.41x slower                                                    |
| genshi_text     | 28.6 ms                                                  | 41.3 ms: 1.44x slower                                                    |
| django_template | 39.4 ms                                                  | 65.3 ms: 1.66x slower                                                    |
| mako            | 14.0 ms                                                  | 25.6 ms: 1.83x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.58x slower                                                             |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot              | 5.10 ms                                                  | 4.15 ms: 1.23x faster                                                    |
| create_gc_cycles          | 3.39 ms                                                  | 2.87 ms: 1.18x faster                                                    |
| gc_traversal              | 5.92 ms                                                  | 5.03 ms: 1.18x faster                                                    |
| xml_etree_iterparse       | 159 ms                                                   | 137 ms: 1.16x faster                                                     |
| xml_etree_parse           | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| deepcopy                  | 479 us                                                   | 432 us: 1.11x faster                                                     |
| async_tree_memoization_tg | 663 ms                                                   | 628 ms: 1.06x faster                                                     |
| async_tree_io             | 1.14 sec                                                 | 1.18 sec: 1.04x slower                                                   |
| async_tree_none_tg        | 484 ms                                                   | 510 ms: 1.05x slower                                                     |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 833 ms: 1.06x slower                                                     |
| async_tree_none           | 504 ms                                                   | 536 ms: 1.06x slower                                                     |
| deepcopy_memo             | 53.0 us                                                  | 56.6 us: 1.07x slower                                                    |
| spectral_norm             | 143 ms                                                   | 154 ms: 1.08x slower                                                     |
| scimark_fft               | 463 ms                                                   | 501 ms: 1.08x slower                                                     |
| json                      | 5.94 ms                                                  | 6.54 ms: 1.10x slower                                                    |
| k_core                    | 2.99 sec                                                 | 3.30 sec: 1.10x slower                                                   |
| json_loads                | 32.8 us                                                  | 37.4 us: 1.14x slower                                                    |
| deepcopy_reduce           | 4.24 us                                                  | 4.85 us: 1.14x slower                                                    |
| coroutines                | 29.4 ms                                                  | 33.8 ms: 1.15x slower                                                    |
| mdp                       | 3.45 sec                                                 | 4.01 sec: 1.17x slower                                                   |
| telco                     | 10.5 ms                                                  | 12.4 ms: 1.18x slower                                                    |
| xml_etree_generate        | 118 ms                                                   | 145 ms: 1.22x slower                                                     |
| connected_components      | 547 ms                                                   | 676 ms: 1.24x slower                                                     |
| async_generators          | 500 ms                                                   | 619 ms: 1.24x slower                                                     |
| sphinx                    | 1.20 sec                                                 | 1.49 sec: 1.24x slower                                                   |
| shortest_path             | 565 ms                                                   | 707 ms: 1.25x slower                                                     |
| docutils                  | 2.96 sec                                                 | 3.72 sec: 1.25x slower                                                   |
| pylint                    | 345 ms                                                   | 438 ms: 1.27x slower                                                     |
| python_startup            | 16.0 ms                                                  | 20.4 ms: 1.27x slower                                                    |
| scimark_sparse_mat_mult   | 6.66 ms                                                  | 8.49 ms: 1.27x slower                                                    |
| pycparser                 | 1.34 sec                                                 | 1.73 sec: 1.29x slower                                                   |
| json_dumps                | 14.2 ms                                                  | 18.4 ms: 1.29x slower                                                    |
| nqueens                   | 105 ms                                                   | 136 ms: 1.30x slower                                                     |
| sqlglot_optimize          | 65.2 ms                                                  | 86.0 ms: 1.32x slower                                                    |
| bpe_tokeniser             | 6.02 sec                                                 | 7.94 sec: 1.32x slower                                                   |
| xml_etree_process         | 82.1 ms                                                  | 109 ms: 1.33x slower                                                     |
| sympy_expand              | 472 ms                                                   | 635 ms: 1.34x slower                                                     |
| tomli_loads               | 2.67 sec                                                 | 3.60 sec: 1.35x slower                                                   |
| thrift                    | 1.01 ms                                                  | 1.38 ms: 1.36x slower                                                    |
| coverage                  | 106 ms                                                   | 144 ms: 1.36x slower                                                     |
| sympy_sum                 | 151 ms                                                   | 208 ms: 1.37x slower                                                     |
| sqlglot_normalize         | 131 ms                                                   | 180 ms: 1.38x slower                                                     |
| meteor_contest            | 117 ms                                                   | 161 ms: 1.38x slower                                                     |
| generators                | 40.3 ms                                                  | 56.1 ms: 1.39x slower                                                    |
| pprint_safe_repr          | 962 ms                                                   | 1.34 sec: 1.40x slower                                                   |
| regex_compile             | 134 ms                                                   | 187 ms: 1.40x slower                                                     |
| pprint_pformat            | 1.99 sec                                                 | 2.78 sec: 1.40x slower                                                   |
| sympy_integrate           | 21.4 ms                                                  | 30.1 ms: 1.40x slower                                                    |
| python_startup_no_site    | 8.79 ms                                                  | 12.4 ms: 1.41x slower                                                    |
| genshi_xml                | 61.6 ms                                                  | 86.6 ms: 1.41x slower                                                    |
| crypto_pyaes              | 84.9 ms                                                  | 121 ms: 1.42x slower                                                     |
| genshi_text               | 28.6 ms                                                  | 41.3 ms: 1.44x slower                                                    |
| fannkuch                  | 478 ms                                                   | 692 ms: 1.45x slower                                                     |
| sqlalchemy_declarative    | 154 ms                                                   | 227 ms: 1.48x slower                                                     |
| bench_thread_pool         | 1.34 ms                                                  | 2.00 ms: 1.49x slower                                                    |
| 2to3                      | 313 ms                                                   | 468 ms: 1.50x slower                                                     |
| sympy_str                 | 265 ms                                                   | 399 ms: 1.50x slower                                                     |
| logging_format            | 8.10 us                                                  | 12.3 us: 1.51x slower                                                    |
| typing_runtime_protocols  | 197 us                                                   | 302 us: 1.53x slower                                                     |
| logging_simple            | 7.25 us                                                  | 11.2 us: 1.55x slower                                                    |
| scimark_lu                | 146 ms                                                   | 228 ms: 1.56x slower                                                     |
| pyflate                   | 582 ms                                                   | 911 ms: 1.57x slower                                                     |
| many_optionals            | 626 us                                                   | 983 us: 1.57x slower                                                     |
| nbody                     | 118 ms                                                   | 186 ms: 1.57x slower                                                     |
| sqlalchemy_imperative     | 16.1 ms                                                  | 25.7 ms: 1.59x slower                                                    |
| float                     | 95.8 ms                                                  | 154 ms: 1.60x slower                                                     |
| django_template           | 39.4 ms                                                  | 65.3 ms: 1.66x slower                                                    |
| html5lib                  | 65.6 ms                                                  | 111 ms: 1.69x slower                                                     |
| unpickle_pure_python      | 265 us                                                   | 453 us: 1.71x slower                                                     |
| scimark_sor               | 164 ms                                                   | 285 ms: 1.74x slower                                                     |
| scimark_monte_carlo       | 87.8 ms                                                  | 154 ms: 1.76x slower                                                     |
| richards_super            | 60.8 ms                                                  | 108 ms: 1.78x slower                                                     |
| richards                  | 54.5 ms                                                  | 97.6 ms: 1.79x slower                                                    |
| hexiom                    | 7.34 ms                                                  | 13.4 ms: 1.82x slower                                                    |
| chaos                     | 70.7 ms                                                  | 129 ms: 1.83x slower                                                     |
| mako                      | 14.0 ms                                                  | 25.6 ms: 1.83x slower                                                    |
| comprehensions            | 20.8 us                                                  | 38.5 us: 1.85x slower                                                    |
| subparsers                | 20.3 ms                                                  | 37.9 ms: 1.86x slower                                                    |
| pickle_pure_python        | 374 us                                                   | 701 us: 1.88x slower                                                     |
| logging_silent            | 135 ns                                                   | 261 ns: 1.94x slower                                                     |
| sqlglot_transpile         | 1.84 ms                                                  | 3.73 ms: 2.03x slower                                                    |
| go                        | 164 ms                                                   | 337 ms: 2.05x slower                                                     |
| raytrace                  | 310 ms                                                   | 666 ms: 2.15x slower                                                     |
| sqlglot_parse             | 1.43 ms                                                  | 3.13 ms: 2.18x slower                                                    |
| deltablue                 | 3.97 ms                                                  | 11.1 ms: 2.79x slower                                                    |
| bench_mp_pool             | 8.07 ms                                                  | 62.6 ms: 7.76x slower                                                    |
| Geometric mean            | (ref)                                                    | 1.36x slower                                                             |

Benchmark hidden because not significant (9): sqlite_synth, pathlib, async_tree_memoization, async_tree_io_tg, asyncio_websockets, async_tree_cpu_io_mixed_tg, regex_v8, pidigits, regex_dna
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (2) of results/bm-20250104-3.14.0a3+-0cafa97-NOGIL/bm-20250104-arminc-aarch64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: dulwich_log, mypy2

- Geometric mean (including insignificant results): 1.248x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.26x
- 95% likely to have a slowdown of 1.25x
- 99% likely to have a slowdown of 1.22x

# Memory
- memory change: 1.22x