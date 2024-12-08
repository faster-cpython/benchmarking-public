# Results vs. 3.13.0

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: linux-aarch64
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.287x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 468 ms: 1.50x slower                                                     |
| docutils       | 2.96 sec                                                 | 3.77 sec: 1.27x slower                                                   |
| html5lib       | 65.6 ms                                                  | 118 ms: 1.79x slower                                                     |
| sphinx         | 1.20 sec                                                 | 1.52 sec: 1.27x slower                                                   |
| Geometric mean | (ref)                                                    | 1.44x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 693 ms: 1.05x slower                                                     |
| async_tree_memoization     | 664 ms                                                   | 708 ms: 1.07x slower                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 874 ms: 1.09x slower                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 1.30 sec: 1.11x slower                                                   |
| coroutines                 | 29.4 ms                                                  | 33.4 ms: 1.14x slower                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 900 ms: 1.14x slower                                                     |
| async_tree_io              | 1.14 sec                                                 | 1.31 sec: 1.15x slower                                                   |
| async_tree_none            | 504 ms                                                   | 592 ms: 1.17x slower                                                     |
| async_tree_none_tg         | 484 ms                                                   | 578 ms: 1.19x slower                                                     |
| async_generators           | 500 ms                                                   | 637 ms: 1.27x slower                                                     |
| Geometric mean             | (ref)                                                    | 1.13x slower                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 118 ms                                                   | 183 ms: 1.55x slower                                                     |
| float          | 95.8 ms                                                  | 198 ms: 2.07x slower                                                     |
| Geometric mean | (ref)                                                    | 1.46x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.99 ms: 1.28x faster                                                    |
| regex_compile  | 134 ms                                                   | 203 ms: 1.52x slower                                                     |
| Geometric mean | (ref)                                                    | 1.06x slower                                                             |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 141 ms: 1.12x faster                                                     |
| xml_etree_parse      | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| json_loads           | 32.8 us                                                  | 37.1 us: 1.13x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 144 ms: 1.22x slower                                                     |
| json_dumps           | 14.2 ms                                                  | 19.3 ms: 1.36x slower                                                    |
| tomli_loads          | 2.67 sec                                                 | 3.69 sec: 1.38x slower                                                   |
| xml_etree_process    | 82.1 ms                                                  | 116 ms: 1.41x slower                                                     |
| unpickle_pure_python | 265 us                                                   | 459 us: 1.73x slower                                                     |
| pickle_pure_python   | 374 us                                                   | 668 us: 1.79x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.28x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 21.6 ms: 1.34x slower                                                    |
| python_startup_no_site | 8.79 ms                                                  | 12.8 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.40x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 84.5 ms: 1.37x slower                                                    |
| genshi_text     | 28.6 ms                                                  | 43.3 ms: 1.52x slower                                                    |
| django_template | 39.4 ms                                                  | 68.5 ms: 1.74x slower                                                    |
| mako            | 14.0 ms                                                  | 26.3 ms: 1.88x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.61x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot               | 5.10 ms                                                  | 3.99 ms: 1.28x faster                                                    |
| gc_traversal               | 5.92 ms                                                  | 5.06 ms: 1.17x faster                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 2.94 ms: 1.15x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 141 ms: 1.12x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| deepcopy                   | 479 us                                                   | 449 us: 1.07x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 693 ms: 1.05x slower                                                     |
| async_tree_memoization     | 664 ms                                                   | 708 ms: 1.07x slower                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 874 ms: 1.09x slower                                                     |
| pathlib                    | 24.3 ms                                                  | 26.6 ms: 1.09x slower                                                    |
| json                       | 5.94 ms                                                  | 6.55 ms: 1.10x slower                                                    |
| deepcopy_memo              | 53.0 us                                                  | 58.8 us: 1.11x slower                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 1.30 sec: 1.11x slower                                                   |
| json_loads                 | 32.8 us                                                  | 37.1 us: 1.13x slower                                                    |
| telco                      | 10.5 ms                                                  | 11.8 ms: 1.13x slower                                                    |
| coroutines                 | 29.4 ms                                                  | 33.4 ms: 1.14x slower                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 900 ms: 1.14x slower                                                     |
| k_core                     | 2.99 sec                                                 | 3.42 sec: 1.14x slower                                                   |
| async_tree_io              | 1.14 sec                                                 | 1.31 sec: 1.15x slower                                                   |
| scimark_fft                | 463 ms                                                   | 536 ms: 1.16x slower                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 4.94 us: 1.16x slower                                                    |
| spectral_norm              | 143 ms                                                   | 168 ms: 1.17x slower                                                     |
| async_tree_none            | 504 ms                                                   | 592 ms: 1.17x slower                                                     |
| mdp                        | 3.45 sec                                                 | 4.10 sec: 1.19x slower                                                   |
| async_tree_none_tg         | 484 ms                                                   | 578 ms: 1.19x slower                                                     |
| xml_etree_generate         | 118 ms                                                   | 144 ms: 1.22x slower                                                     |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 8.23 ms: 1.24x slower                                                    |
| connected_components       | 547 ms                                                   | 678 ms: 1.24x slower                                                     |
| shortest_path              | 565 ms                                                   | 711 ms: 1.26x slower                                                     |
| sphinx                     | 1.20 sec                                                 | 1.52 sec: 1.27x slower                                                   |
| docutils                   | 2.96 sec                                                 | 3.77 sec: 1.27x slower                                                   |
| async_generators           | 500 ms                                                   | 637 ms: 1.27x slower                                                     |
| coverage                   | 106 ms                                                   | 136 ms: 1.29x slower                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 7.87 sec: 1.31x slower                                                   |
| nqueens                    | 105 ms                                                   | 138 ms: 1.32x slower                                                     |
| python_startup             | 16.0 ms                                                  | 21.6 ms: 1.34x slower                                                    |
| meteor_contest             | 117 ms                                                   | 158 ms: 1.35x slower                                                     |
| json_dumps                 | 14.2 ms                                                  | 19.3 ms: 1.36x slower                                                    |
| sqlglot_normalize          | 131 ms                                                   | 179 ms: 1.37x slower                                                     |
| genshi_xml                 | 61.6 ms                                                  | 84.5 ms: 1.37x slower                                                    |
| tomli_loads                | 2.67 sec                                                 | 3.69 sec: 1.38x slower                                                   |
| pylint                     | 345 ms                                                   | 480 ms: 1.39x slower                                                     |
| crypto_pyaes               | 84.9 ms                                                  | 118 ms: 1.40x slower                                                     |
| generators                 | 40.3 ms                                                  | 56.4 ms: 1.40x slower                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.80 sec: 1.41x slower                                                   |
| sqlglot_optimize           | 65.2 ms                                                  | 92.2 ms: 1.41x slower                                                    |
| xml_etree_process          | 82.1 ms                                                  | 116 ms: 1.41x slower                                                     |
| pprint_safe_repr           | 962 ms                                                   | 1.36 sec: 1.41x slower                                                   |
| pycparser                  | 1.34 sec                                                 | 1.91 sec: 1.42x slower                                                   |
| typing_runtime_protocols   | 197 us                                                   | 284 us: 1.44x slower                                                     |
| fannkuch                   | 478 ms                                                   | 690 ms: 1.44x slower                                                     |
| python_startup_no_site     | 8.79 ms                                                  | 12.8 ms: 1.45x slower                                                    |
| 2to3                       | 313 ms                                                   | 468 ms: 1.50x slower                                                     |
| bench_thread_pool          | 1.34 ms                                                  | 2.00 ms: 1.50x slower                                                    |
| genshi_text                | 28.6 ms                                                  | 43.3 ms: 1.52x slower                                                    |
| sympy_integrate            | 21.4 ms                                                  | 32.6 ms: 1.52x slower                                                    |
| regex_compile              | 134 ms                                                   | 203 ms: 1.52x slower                                                     |
| nbody                      | 118 ms                                                   | 183 ms: 1.55x slower                                                     |
| thrift                     | 1.01 ms                                                  | 1.60 ms: 1.58x slower                                                    |
| pyflate                    | 582 ms                                                   | 927 ms: 1.59x slower                                                     |
| many_optionals             | 626 us                                                   | 1.03 ms: 1.64x slower                                                    |
| sympy_str                  | 265 ms                                                   | 458 ms: 1.73x slower                                                     |
| logging_format             | 8.10 us                                                  | 14.0 us: 1.73x slower                                                    |
| unpickle_pure_python       | 265 us                                                   | 459 us: 1.73x slower                                                     |
| django_template            | 39.4 ms                                                  | 68.5 ms: 1.74x slower                                                    |
| hexiom                     | 7.34 ms                                                  | 12.8 ms: 1.75x slower                                                    |
| sqlalchemy_declarative     | 154 ms                                                   | 271 ms: 1.76x slower                                                     |
| pickle_pure_python         | 374 us                                                   | 668 us: 1.79x slower                                                     |
| html5lib                   | 65.6 ms                                                  | 118 ms: 1.79x slower                                                     |
| sqlalchemy_imperative      | 16.1 ms                                                  | 29.1 ms: 1.81x slower                                                    |
| logging_simple             | 7.25 us                                                  | 13.1 us: 1.81x slower                                                    |
| sympy_expand               | 472 ms                                                   | 859 ms: 1.82x slower                                                     |
| scimark_lu                 | 146 ms                                                   | 271 ms: 1.85x slower                                                     |
| comprehensions             | 20.8 us                                                  | 38.7 us: 1.86x slower                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 164 ms: 1.87x slower                                                     |
| mako                       | 14.0 ms                                                  | 26.3 ms: 1.88x slower                                                    |
| sympy_sum                  | 151 ms                                                   | 287 ms: 1.90x slower                                                     |
| scimark_sor                | 164 ms                                                   | 314 ms: 1.92x slower                                                     |
| chaos                      | 70.7 ms                                                  | 136 ms: 1.92x slower                                                     |
| richards                   | 54.5 ms                                                  | 106 ms: 1.94x slower                                                     |
| richards_super             | 60.8 ms                                                  | 119 ms: 1.96x slower                                                     |
| logging_silent             | 135 ns                                                   | 265 ns: 1.97x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 40.8 ms: 2.00x slower                                                    |
| float                      | 95.8 ms                                                  | 198 ms: 2.07x slower                                                     |
| sqlglot_transpile          | 1.84 ms                                                  | 3.96 ms: 2.15x slower                                                    |
| go                         | 164 ms                                                   | 373 ms: 2.27x slower                                                     |
| sqlglot_parse              | 1.43 ms                                                  | 3.38 ms: 2.36x slower                                                    |
| raytrace                   | 310 ms                                                   | 736 ms: 2.37x slower                                                     |
| deltablue                  | 3.97 ms                                                  | 11.8 ms: 2.98x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 66.8 ms: 8.28x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.43x slower                                                             |

Benchmark hidden because not significant (5): pidigits, regex_dna, sqlite_synth, asyncio_websockets, regex_v8
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241207-3.14.0a2+-79b7cab-NOGIL/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json: dulwich_log

- Geometric mean (including insignificant results): 1.287x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.29x
- 95% likely to have a slowdown of 1.28x
- 99% likely to have a slowdown of 1.25x

# Memory
- memory change: 1.22x