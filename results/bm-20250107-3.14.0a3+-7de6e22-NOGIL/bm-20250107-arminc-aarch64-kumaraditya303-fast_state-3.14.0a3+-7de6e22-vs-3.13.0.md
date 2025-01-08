# Results vs. 3.13.0

- fork: kumaraditya303
- ref: fast_state
- machine: linux-aarch64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.245x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 463 ms: 1.48x slower                                                   |
| docutils       | 2.96 sec                                                 | 3.74 sec: 1.26x slower                                                 |
| html5lib       | 65.6 ms                                                  | 108 ms: 1.65x slower                                                   |
| sphinx         | 1.20 sec                                                 | 1.47 sec: 1.23x slower                                                 |
| Geometric mean | (ref)                                                    | 1.39x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|---------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg | 663 ms                                                   | 616 ms: 1.08x faster                                                   |
| async_tree_io             | 1.14 sec                                                 | 1.18 sec: 1.03x slower                                                 |
| async_tree_none_tg        | 484 ms                                                   | 505 ms: 1.04x slower                                                   |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 833 ms: 1.06x slower                                                   |
| async_tree_none           | 504 ms                                                   | 540 ms: 1.07x slower                                                   |
| coroutines                | 29.4 ms                                                  | 33.5 ms: 1.14x slower                                                  |
| async_generators          | 500 ms                                                   | 614 ms: 1.23x slower                                                   |
| Geometric mean            | (ref)                                                    | 1.04x slower                                                           |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 118 ms                                                   | 182 ms: 1.54x slower                                                   |
| float          | 95.8 ms                                                  | 154 ms: 1.60x slower                                                   |
| Geometric mean | (ref)                                                    | 1.36x slower                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.15 ms: 1.23x faster                                                  |
| regex_compile  | 134 ms                                                   | 191 ms: 1.43x slower                                                   |
| Geometric mean | (ref)                                                    | 1.05x slower                                                           |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 135 ms: 1.17x faster                                                   |
| xml_etree_parse      | 203 ms                                                   | 186 ms: 1.09x faster                                                   |
| json_loads           | 32.8 us                                                  | 36.0 us: 1.10x slower                                                  |
| xml_etree_generate   | 118 ms                                                   | 143 ms: 1.21x slower                                                   |
| json_dumps           | 14.2 ms                                                  | 18.1 ms: 1.28x slower                                                  |
| tomli_loads          | 2.67 sec                                                 | 3.56 sec: 1.33x slower                                                 |
| xml_etree_process    | 82.1 ms                                                  | 111 ms: 1.35x slower                                                   |
| unpickle_pure_python | 265 us                                                   | 455 us: 1.72x slower                                                   |
| pickle_pure_python   | 374 us                                                   | 702 us: 1.88x slower                                                   |
| Geometric mean       | (ref)                                                    | 1.25x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 20.4 ms: 1.27x slower                                                  |
| python_startup_no_site | 8.79 ms                                                  | 12.5 ms: 1.42x slower                                                  |
| Geometric mean         | (ref)                                                    | 1.34x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 81.2 ms: 1.32x slower                                                  |
| genshi_text     | 28.6 ms                                                  | 40.5 ms: 1.42x slower                                                  |
| django_template | 39.4 ms                                                  | 66.8 ms: 1.70x slower                                                  |
| mako            | 14.0 ms                                                  | 25.2 ms: 1.81x slower                                                  |
| Geometric mean  | (ref)                                                    | 1.55x slower                                                           |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|---------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot              | 5.10 ms                                                  | 4.15 ms: 1.23x faster                                                  |
| xml_etree_iterparse       | 159 ms                                                   | 135 ms: 1.17x faster                                                   |
| gc_traversal              | 5.92 ms                                                  | 5.09 ms: 1.16x faster                                                  |
| create_gc_cycles          | 3.39 ms                                                  | 3.01 ms: 1.13x faster                                                  |
| xml_etree_parse           | 203 ms                                                   | 186 ms: 1.09x faster                                                   |
| deepcopy                  | 479 us                                                   | 443 us: 1.08x faster                                                   |
| async_tree_memoization_tg | 663 ms                                                   | 616 ms: 1.08x faster                                                   |
| sqlite_synth              | 4.08 us                                                  | 3.83 us: 1.07x faster                                                  |
| async_tree_io             | 1.14 sec                                                 | 1.18 sec: 1.03x slower                                                 |
| async_tree_none_tg        | 484 ms                                                   | 505 ms: 1.04x slower                                                   |
| json                      | 5.94 ms                                                  | 6.23 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 833 ms: 1.06x slower                                                   |
| async_tree_none           | 504 ms                                                   | 540 ms: 1.07x slower                                                   |
| deepcopy_memo             | 53.0 us                                                  | 56.9 us: 1.07x slower                                                  |
| scimark_fft               | 463 ms                                                   | 500 ms: 1.08x slower                                                   |
| spectral_norm             | 143 ms                                                   | 156 ms: 1.09x slower                                                   |
| json_loads                | 32.8 us                                                  | 36.0 us: 1.10x slower                                                  |
| k_core                    | 2.99 sec                                                 | 3.28 sec: 1.10x slower                                                 |
| coroutines                | 29.4 ms                                                  | 33.5 ms: 1.14x slower                                                  |
| deepcopy_reduce           | 4.24 us                                                  | 4.90 us: 1.15x slower                                                  |
| mdp                       | 3.45 sec                                                 | 4.03 sec: 1.17x slower                                                 |
| telco                     | 10.5 ms                                                  | 12.3 ms: 1.18x slower                                                  |
| xml_etree_generate        | 118 ms                                                   | 143 ms: 1.21x slower                                                   |
| scimark_sparse_mat_mult   | 6.66 ms                                                  | 8.15 ms: 1.22x slower                                                  |
| sphinx                    | 1.20 sec                                                 | 1.47 sec: 1.23x slower                                                 |
| async_generators          | 500 ms                                                   | 614 ms: 1.23x slower                                                   |
| connected_components      | 547 ms                                                   | 676 ms: 1.24x slower                                                   |
| shortest_path             | 565 ms                                                   | 703 ms: 1.24x slower                                                   |
| docutils                  | 2.96 sec                                                 | 3.74 sec: 1.26x slower                                                 |
| python_startup            | 16.0 ms                                                  | 20.4 ms: 1.27x slower                                                  |
| pycparser                 | 1.34 sec                                                 | 1.71 sec: 1.28x slower                                                 |
| json_dumps                | 14.2 ms                                                  | 18.1 ms: 1.28x slower                                                  |
| pylint                    | 345 ms                                                   | 442 ms: 1.28x slower                                                   |
| nqueens                   | 105 ms                                                   | 136 ms: 1.30x slower                                                   |
| genshi_xml                | 61.6 ms                                                  | 81.2 ms: 1.32x slower                                                  |
| bpe_tokeniser             | 6.02 sec                                                 | 7.94 sec: 1.32x slower                                                 |
| sqlglot_optimize          | 65.2 ms                                                  | 86.6 ms: 1.33x slower                                                  |
| tomli_loads               | 2.67 sec                                                 | 3.56 sec: 1.33x slower                                                 |
| xml_etree_process         | 82.1 ms                                                  | 111 ms: 1.35x slower                                                   |
| sqlglot_normalize         | 131 ms                                                   | 176 ms: 1.35x slower                                                   |
| meteor_contest            | 117 ms                                                   | 160 ms: 1.37x slower                                                   |
| coverage                  | 106 ms                                                   | 145 ms: 1.37x slower                                                   |
| thrift                    | 1.01 ms                                                  | 1.39 ms: 1.37x slower                                                  |
| sympy_sum                 | 151 ms                                                   | 210 ms: 1.39x slower                                                   |
| generators                | 40.3 ms                                                  | 55.9 ms: 1.39x slower                                                  |
| sympy_integrate           | 21.4 ms                                                  | 29.8 ms: 1.39x slower                                                  |
| pprint_pformat            | 1.99 sec                                                 | 2.76 sec: 1.39x slower                                                 |
| pprint_safe_repr          | 962 ms                                                   | 1.34 sec: 1.40x slower                                                 |
| genshi_text               | 28.6 ms                                                  | 40.5 ms: 1.42x slower                                                  |
| python_startup_no_site    | 8.79 ms                                                  | 12.5 ms: 1.42x slower                                                  |
| crypto_pyaes              | 84.9 ms                                                  | 121 ms: 1.42x slower                                                   |
| sympy_expand              | 472 ms                                                   | 674 ms: 1.43x slower                                                   |
| regex_compile             | 134 ms                                                   | 191 ms: 1.43x slower                                                   |
| sympy_str                 | 265 ms                                                   | 381 ms: 1.44x slower                                                   |
| fannkuch                  | 478 ms                                                   | 695 ms: 1.45x slower                                                   |
| typing_runtime_protocols  | 197 us                                                   | 288 us: 1.46x slower                                                   |
| 2to3                      | 313 ms                                                   | 463 ms: 1.48x slower                                                   |
| scimark_lu                | 146 ms                                                   | 221 ms: 1.51x slower                                                   |
| logging_format            | 8.10 us                                                  | 12.3 us: 1.52x slower                                                  |
| logging_simple            | 7.25 us                                                  | 11.1 us: 1.53x slower                                                  |
| nbody                     | 118 ms                                                   | 182 ms: 1.54x slower                                                   |
| bench_thread_pool         | 1.34 ms                                                  | 2.07 ms: 1.55x slower                                                  |
| pyflate                   | 582 ms                                                   | 901 ms: 1.55x slower                                                   |
| sqlalchemy_declarative    | 154 ms                                                   | 241 ms: 1.56x slower                                                   |
| many_optionals            | 626 us                                                   | 999 us: 1.59x slower                                                   |
| float                     | 95.8 ms                                                  | 154 ms: 1.60x slower                                                   |
| sqlalchemy_imperative     | 16.1 ms                                                  | 26.1 ms: 1.62x slower                                                  |
| html5lib                  | 65.6 ms                                                  | 108 ms: 1.65x slower                                                   |
| django_template           | 39.4 ms                                                  | 66.8 ms: 1.70x slower                                                  |
| unpickle_pure_python      | 265 us                                                   | 455 us: 1.72x slower                                                   |
| scimark_monte_carlo       | 87.8 ms                                                  | 151 ms: 1.72x slower                                                   |
| hexiom                    | 7.34 ms                                                  | 12.8 ms: 1.75x slower                                                  |
| scimark_sor               | 164 ms                                                   | 289 ms: 1.76x slower                                                   |
| richards_super            | 60.8 ms                                                  | 109 ms: 1.79x slower                                                   |
| richards                  | 54.5 ms                                                  | 97.7 ms: 1.79x slower                                                  |
| chaos                     | 70.7 ms                                                  | 127 ms: 1.79x slower                                                   |
| mako                      | 14.0 ms                                                  | 25.2 ms: 1.81x slower                                                  |
| comprehensions            | 20.8 us                                                  | 38.1 us: 1.83x slower                                                  |
| pickle_pure_python        | 374 us                                                   | 702 us: 1.88x slower                                                   |
| subparsers                | 20.3 ms                                                  | 38.2 ms: 1.88x slower                                                  |
| logging_silent            | 135 ns                                                   | 255 ns: 1.90x slower                                                   |
| sqlglot_transpile         | 1.84 ms                                                  | 3.64 ms: 1.98x slower                                                  |
| go                        | 164 ms                                                   | 341 ms: 2.08x slower                                                   |
| raytrace                  | 310 ms                                                   | 658 ms: 2.12x slower                                                   |
| sqlglot_parse             | 1.43 ms                                                  | 3.10 ms: 2.16x slower                                                  |
| deltablue                 | 3.97 ms                                                  | 11.0 ms: 2.78x slower                                                  |
| bench_mp_pool             | 8.07 ms                                                  | 61.1 ms: 7.57x slower                                                  |
| Geometric mean            | (ref)                                                    | 1.36x slower                                                           |

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_memoization, pathlib, async_tree_cpu_io_mixed_tg, pidigits, asyncio_websockets, regex_v8, regex_dna
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (2) of results/bm-20250107-3.14.0a3+-7de6e22-NOGIL/bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: dulwich_log, mypy2

- Geometric mean (including insignificant results): 1.245x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.26x
- 95% likely to have a slowdown of 1.25x
- 99% likely to have a slowdown of 1.21x

# Memory
- memory change: 1.22x