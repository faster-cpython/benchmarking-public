# Results vs. 3.13.0

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: linux-aarch64
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.259x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 477 ms: 1.53x slower                                                     |
| docutils       | 2.96 sec                                                 | 3.78 sec: 1.27x slower                                                   |
| html5lib       | 65.6 ms                                                  | 109 ms: 1.66x slower                                                     |
| sphinx         | 1.20 sec                                                 | 1.47 sec: 1.22x slower                                                   |
| Geometric mean | (ref)                                                    | 1.41x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg | 663 ms                                                   | 638 ms: 1.04x faster                                                     |
| async_tree_io             | 1.14 sec                                                 | 1.21 sec: 1.06x slower                                                   |
| async_tree_none           | 504 ms                                                   | 542 ms: 1.08x slower                                                     |
| async_tree_none_tg        | 484 ms                                                   | 523 ms: 1.08x slower                                                     |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 852 ms: 1.08x slower                                                     |
| coroutines                | 29.4 ms                                                  | 34.6 ms: 1.18x slower                                                    |
| async_generators          | 500 ms                                                   | 606 ms: 1.21x slower                                                     |
| Geometric mean            | (ref)                                                    | 1.06x slower                                                             |

Benchmark hidden because not significant (4): async_tree_io_tg, asyncio_websockets, async_tree_memoization, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 118 ms                                                   | 188 ms: 1.59x slower                                                     |
| float          | 95.8 ms                                                  | 159 ms: 1.66x slower                                                     |
| Geometric mean | (ref)                                                    | 1.40x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.12 ms: 1.24x faster                                                    |
| regex_compile  | 134 ms                                                   | 191 ms: 1.43x slower                                                     |
| Geometric mean | (ref)                                                    | 1.05x slower                                                             |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 135 ms: 1.18x faster                                                     |
| xml_etree_parse      | 203 ms                                                   | 178 ms: 1.14x faster                                                     |
| json_loads           | 32.8 us                                                  | 37.4 us: 1.14x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 143 ms: 1.21x slower                                                     |
| json_dumps           | 14.2 ms                                                  | 18.2 ms: 1.28x slower                                                    |
| tomli_loads          | 2.67 sec                                                 | 3.57 sec: 1.34x slower                                                   |
| xml_etree_process    | 82.1 ms                                                  | 111 ms: 1.36x slower                                                     |
| unpickle_pure_python | 265 us                                                   | 472 us: 1.78x slower                                                     |
| pickle_pure_python   | 374 us                                                   | 692 us: 1.85x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.26x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 21.4 ms: 1.33x slower                                                    |
| python_startup_no_site | 8.79 ms                                                  | 12.5 ms: 1.43x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.38x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 83.9 ms: 1.36x slower                                                    |
| genshi_text     | 28.6 ms                                                  | 42.2 ms: 1.48x slower                                                    |
| django_template | 39.4 ms                                                  | 67.4 ms: 1.71x slower                                                    |
| mako            | 14.0 ms                                                  | 25.6 ms: 1.83x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.58x slower                                                             |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot              | 5.10 ms                                                  | 4.12 ms: 1.24x faster                                                    |
| gc_traversal              | 5.92 ms                                                  | 5.03 ms: 1.18x faster                                                    |
| xml_etree_iterparse       | 159 ms                                                   | 135 ms: 1.18x faster                                                     |
| create_gc_cycles          | 3.39 ms                                                  | 2.90 ms: 1.17x faster                                                    |
| xml_etree_parse           | 203 ms                                                   | 178 ms: 1.14x faster                                                     |
| deepcopy                  | 479 us                                                   | 435 us: 1.10x faster                                                     |
| sqlite_synth              | 4.08 us                                                  | 3.85 us: 1.06x faster                                                    |
| async_tree_memoization_tg | 663 ms                                                   | 638 ms: 1.04x faster                                                     |
| async_tree_io             | 1.14 sec                                                 | 1.21 sec: 1.06x slower                                                   |
| async_tree_none           | 504 ms                                                   | 542 ms: 1.08x slower                                                     |
| async_tree_none_tg        | 484 ms                                                   | 523 ms: 1.08x slower                                                     |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 852 ms: 1.08x slower                                                     |
| deepcopy_memo             | 53.0 us                                                  | 57.8 us: 1.09x slower                                                    |
| spectral_norm             | 143 ms                                                   | 157 ms: 1.09x slower                                                     |
| k_core                    | 2.99 sec                                                 | 3.31 sec: 1.11x slower                                                   |
| scimark_fft               | 463 ms                                                   | 517 ms: 1.12x slower                                                     |
| deepcopy_reduce           | 4.24 us                                                  | 4.81 us: 1.13x slower                                                    |
| json_loads                | 32.8 us                                                  | 37.4 us: 1.14x slower                                                    |
| json                      | 5.94 ms                                                  | 6.85 ms: 1.15x slower                                                    |
| telco                     | 10.5 ms                                                  | 12.1 ms: 1.16x slower                                                    |
| mdp                       | 3.45 sec                                                 | 4.05 sec: 1.18x slower                                                   |
| coroutines                | 29.4 ms                                                  | 34.6 ms: 1.18x slower                                                    |
| async_generators          | 500 ms                                                   | 606 ms: 1.21x slower                                                     |
| xml_etree_generate        | 118 ms                                                   | 143 ms: 1.21x slower                                                     |
| sphinx                    | 1.20 sec                                                 | 1.47 sec: 1.22x slower                                                   |
| scimark_sparse_mat_mult   | 6.66 ms                                                  | 8.38 ms: 1.26x slower                                                    |
| connected_components      | 547 ms                                                   | 693 ms: 1.27x slower                                                     |
| docutils                  | 2.96 sec                                                 | 3.78 sec: 1.27x slower                                                   |
| shortest_path             | 565 ms                                                   | 724 ms: 1.28x slower                                                     |
| json_dumps                | 14.2 ms                                                  | 18.2 ms: 1.28x slower                                                    |
| nqueens                   | 105 ms                                                   | 135 ms: 1.29x slower                                                     |
| pycparser                 | 1.34 sec                                                 | 1.74 sec: 1.29x slower                                                   |
| pylint                    | 345 ms                                                   | 446 ms: 1.29x slower                                                     |
| bpe_tokeniser             | 6.02 sec                                                 | 7.99 sec: 1.33x slower                                                   |
| python_startup            | 16.0 ms                                                  | 21.4 ms: 1.33x slower                                                    |
| thrift                    | 1.01 ms                                                  | 1.35 ms: 1.33x slower                                                    |
| tomli_loads               | 2.67 sec                                                 | 3.57 sec: 1.34x slower                                                   |
| sqlglot_optimize          | 65.2 ms                                                  | 87.9 ms: 1.35x slower                                                    |
| xml_etree_process         | 82.1 ms                                                  | 111 ms: 1.36x slower                                                     |
| meteor_contest            | 117 ms                                                   | 159 ms: 1.36x slower                                                     |
| coverage                  | 106 ms                                                   | 144 ms: 1.36x slower                                                     |
| genshi_xml                | 61.6 ms                                                  | 83.9 ms: 1.36x slower                                                    |
| sqlglot_normalize         | 131 ms                                                   | 179 ms: 1.36x slower                                                     |
| python_startup_no_site    | 8.79 ms                                                  | 12.5 ms: 1.43x slower                                                    |
| regex_compile             | 134 ms                                                   | 191 ms: 1.43x slower                                                     |
| crypto_pyaes              | 84.9 ms                                                  | 122 ms: 1.44x slower                                                     |
| generators                | 40.3 ms                                                  | 58.1 ms: 1.44x slower                                                    |
| typing_runtime_protocols  | 197 us                                                   | 284 us: 1.44x slower                                                     |
| pprint_safe_repr          | 962 ms                                                   | 1.39 sec: 1.45x slower                                                   |
| pprint_pformat            | 1.99 sec                                                 | 2.87 sec: 1.45x slower                                                   |
| fannkuch                  | 478 ms                                                   | 698 ms: 1.46x slower                                                     |
| bench_thread_pool         | 1.34 ms                                                  | 1.97 ms: 1.48x slower                                                    |
| genshi_text               | 28.6 ms                                                  | 42.2 ms: 1.48x slower                                                    |
| scimark_lu                | 146 ms                                                   | 218 ms: 1.49x slower                                                     |
| sympy_integrate           | 21.4 ms                                                  | 32.7 ms: 1.52x slower                                                    |
| 2to3                      | 313 ms                                                   | 477 ms: 1.53x slower                                                     |
| pyflate                   | 582 ms                                                   | 894 ms: 1.54x slower                                                     |
| logging_format            | 8.10 us                                                  | 12.5 us: 1.54x slower                                                    |
| logging_simple            | 7.25 us                                                  | 11.5 us: 1.58x slower                                                    |
| nbody                     | 118 ms                                                   | 188 ms: 1.59x slower                                                     |
| sqlalchemy_declarative    | 154 ms                                                   | 248 ms: 1.61x slower                                                     |
| many_optionals            | 626 us                                                   | 1.02 ms: 1.62x slower                                                    |
| sqlalchemy_imperative     | 16.1 ms                                                  | 26.5 ms: 1.65x slower                                                    |
| float                     | 95.8 ms                                                  | 159 ms: 1.66x slower                                                     |
| html5lib                  | 65.6 ms                                                  | 109 ms: 1.66x slower                                                     |
| django_template           | 39.4 ms                                                  | 67.4 ms: 1.71x slower                                                    |
| scimark_sor               | 164 ms                                                   | 283 ms: 1.73x slower                                                     |
| scimark_monte_carlo       | 87.8 ms                                                  | 154 ms: 1.75x slower                                                     |
| richards                  | 54.5 ms                                                  | 96.0 ms: 1.76x slower                                                    |
| sympy_str                 | 265 ms                                                   | 468 ms: 1.77x slower                                                     |
| hexiom                    | 7.34 ms                                                  | 13.0 ms: 1.77x slower                                                    |
| unpickle_pure_python      | 265 us                                                   | 472 us: 1.78x slower                                                     |
| richards_super            | 60.8 ms                                                  | 109 ms: 1.79x slower                                                     |
| chaos                     | 70.7 ms                                                  | 129 ms: 1.83x slower                                                     |
| mako                      | 14.0 ms                                                  | 25.6 ms: 1.83x slower                                                    |
| sympy_expand              | 472 ms                                                   | 870 ms: 1.84x slower                                                     |
| subparsers                | 20.3 ms                                                  | 37.6 ms: 1.85x slower                                                    |
| pickle_pure_python        | 374 us                                                   | 692 us: 1.85x slower                                                     |
| comprehensions            | 20.8 us                                                  | 38.8 us: 1.86x slower                                                    |
| sqlglot_transpile         | 1.84 ms                                                  | 3.52 ms: 1.91x slower                                                    |
| logging_silent            | 135 ns                                                   | 258 ns: 1.92x slower                                                     |
| sympy_sum                 | 151 ms                                                   | 290 ms: 1.92x slower                                                     |
| go                        | 164 ms                                                   | 336 ms: 2.05x slower                                                     |
| raytrace                  | 310 ms                                                   | 663 ms: 2.14x slower                                                     |
| sqlglot_parse             | 1.43 ms                                                  | 3.12 ms: 2.17x slower                                                    |
| deltablue                 | 3.97 ms                                                  | 11.0 ms: 2.77x slower                                                    |
| bench_mp_pool             | 8.07 ms                                                  | 64.1 ms: 7.95x slower                                                    |
| Geometric mean            | (ref)                                                    | 1.38x slower                                                             |

Benchmark hidden because not significant (8): pathlib, regex_dna, async_tree_io_tg, asyncio_websockets, async_tree_memoization, async_tree_cpu_io_mixed_tg, pidigits, regex_v8
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (2) of results/bm-20241220-3.14.0a3+-2a66dd3-NOGIL/bm-20241220-arminc-aarch64-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: dulwich_log, mypy2

- Geometric mean (including insignificant results): 1.259x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.28x
- 95% likely to have a slowdown of 1.28x
- 99% likely to have a slowdown of 1.22x

# Memory
- memory change: 1.21x