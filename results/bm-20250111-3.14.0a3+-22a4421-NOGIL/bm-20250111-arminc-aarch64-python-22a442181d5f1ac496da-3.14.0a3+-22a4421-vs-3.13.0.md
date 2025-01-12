# Results vs. 3.13.0

- fork: python
- ref: 22a442181d5f1ac496da
- machine: linux-aarch64
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.238x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 458 ms: 1.46x slower                                                     |
| docutils       | 2.96 sec                                                 | 3.68 sec: 1.24x slower                                                   |
| html5lib       | 65.6 ms                                                  | 110 ms: 1.68x slower                                                     |
| sphinx         | 1.20 sec                                                 | 1.49 sec: 1.24x slower                                                   |
| Geometric mean | (ref)                                                    | 1.39x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg | 663 ms                                                   | 631 ms: 1.05x faster                                                     |
| async_tree_io             | 1.14 sec                                                 | 1.20 sec: 1.05x slower                                                   |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 840 ms: 1.06x slower                                                     |
| async_tree_none_tg        | 484 ms                                                   | 518 ms: 1.07x slower                                                     |
| async_tree_none           | 504 ms                                                   | 543 ms: 1.08x slower                                                     |
| coroutines                | 29.4 ms                                                  | 32.6 ms: 1.11x slower                                                    |
| async_generators          | 500 ms                                                   | 606 ms: 1.21x slower                                                     |
| Geometric mean            | (ref)                                                    | 1.05x slower                                                             |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 118 ms                                                   | 185 ms: 1.56x slower                                                     |
| float          | 95.8 ms                                                  | 150 ms: 1.56x slower                                                     |
| Geometric mean | (ref)                                                    | 1.35x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.07 ms: 1.25x faster                                                    |
| regex_compile  | 134 ms                                                   | 186 ms: 1.40x slower                                                     |
| Geometric mean | (ref)                                                    | 1.05x slower                                                             |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 136 ms: 1.17x faster                                                     |
| xml_etree_parse      | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| json_loads           | 32.8 us                                                  | 36.4 us: 1.11x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 143 ms: 1.21x slower                                                     |
| tomli_loads          | 2.67 sec                                                 | 3.34 sec: 1.25x slower                                                   |
| json_dumps           | 14.2 ms                                                  | 18.4 ms: 1.30x slower                                                    |
| xml_etree_process    | 82.1 ms                                                  | 111 ms: 1.35x slower                                                     |
| unpickle_pure_python | 265 us                                                   | 440 us: 1.66x slower                                                     |
| pickle_pure_python   | 374 us                                                   | 661 us: 1.77x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.23x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 20.4 ms: 1.27x slower                                                    |
| python_startup_no_site | 8.79 ms                                                  | 12.3 ms: 1.40x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.33x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 81.1 ms: 1.32x slower                                                    |
| genshi_text     | 28.6 ms                                                  | 39.7 ms: 1.39x slower                                                    |
| django_template | 39.4 ms                                                  | 64.2 ms: 1.63x slower                                                    |
| mako            | 14.0 ms                                                  | 25.2 ms: 1.80x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.52x slower                                                             |

All benchmarks:
===============

| Benchmark                 | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|---------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot              | 5.10 ms                                                  | 4.07 ms: 1.25x faster                                                    |
| gc_traversal              | 5.92 ms                                                  | 5.03 ms: 1.18x faster                                                    |
| create_gc_cycles          | 3.39 ms                                                  | 2.89 ms: 1.18x faster                                                    |
| xml_etree_iterparse       | 159 ms                                                   | 136 ms: 1.17x faster                                                     |
| xml_etree_parse           | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| deepcopy                  | 479 us                                                   | 446 us: 1.07x faster                                                     |
| sqlite_synth              | 4.08 us                                                  | 3.83 us: 1.07x faster                                                    |
| async_tree_memoization_tg | 663 ms                                                   | 631 ms: 1.05x faster                                                     |
| spectral_norm             | 143 ms                                                   | 150 ms: 1.05x slower                                                     |
| async_tree_io             | 1.14 sec                                                 | 1.20 sec: 1.05x slower                                                   |
| async_tree_cpu_io_mixed   | 789 ms                                                   | 840 ms: 1.06x slower                                                     |
| scimark_fft               | 463 ms                                                   | 493 ms: 1.06x slower                                                     |
| async_tree_none_tg        | 484 ms                                                   | 518 ms: 1.07x slower                                                     |
| json                      | 5.94 ms                                                  | 6.38 ms: 1.07x slower                                                    |
| async_tree_none           | 504 ms                                                   | 543 ms: 1.08x slower                                                     |
| k_core                    | 2.99 sec                                                 | 3.27 sec: 1.09x slower                                                   |
| coroutines                | 29.4 ms                                                  | 32.6 ms: 1.11x slower                                                    |
| json_loads                | 32.8 us                                                  | 36.4 us: 1.11x slower                                                    |
| deepcopy_memo             | 53.0 us                                                  | 59.2 us: 1.12x slower                                                    |
| deepcopy_reduce           | 4.24 us                                                  | 4.81 us: 1.13x slower                                                    |
| mdp                       | 3.45 sec                                                 | 4.00 sec: 1.16x slower                                                   |
| xml_etree_generate        | 118 ms                                                   | 143 ms: 1.21x slower                                                     |
| async_generators          | 500 ms                                                   | 606 ms: 1.21x slower                                                     |
| connected_components      | 547 ms                                                   | 671 ms: 1.23x slower                                                     |
| scimark_sparse_mat_mult   | 6.66 ms                                                  | 8.22 ms: 1.24x slower                                                    |
| docutils                  | 2.96 sec                                                 | 3.68 sec: 1.24x slower                                                   |
| sphinx                    | 1.20 sec                                                 | 1.49 sec: 1.24x slower                                                   |
| tomli_loads               | 2.67 sec                                                 | 3.34 sec: 1.25x slower                                                   |
| pycparser                 | 1.34 sec                                                 | 1.68 sec: 1.25x slower                                                   |
| shortest_path             | 565 ms                                                   | 716 ms: 1.27x slower                                                     |
| telco                     | 10.5 ms                                                  | 13.3 ms: 1.27x slower                                                    |
| python_startup            | 16.0 ms                                                  | 20.4 ms: 1.27x slower                                                    |
| nqueens                   | 105 ms                                                   | 134 ms: 1.28x slower                                                     |
| pylint                    | 345 ms                                                   | 443 ms: 1.28x slower                                                     |
| json_dumps                | 14.2 ms                                                  | 18.4 ms: 1.30x slower                                                    |
| bpe_tokeniser             | 6.02 sec                                                 | 7.86 sec: 1.31x slower                                                   |
| coverage                  | 106 ms                                                   | 139 ms: 1.31x slower                                                     |
| thrift                    | 1.01 ms                                                  | 1.33 ms: 1.32x slower                                                    |
| genshi_xml                | 61.6 ms                                                  | 81.1 ms: 1.32x slower                                                    |
| sqlglot_optimize          | 65.2 ms                                                  | 87.1 ms: 1.34x slower                                                    |
| xml_etree_process         | 82.1 ms                                                  | 111 ms: 1.35x slower                                                     |
| meteor_contest            | 117 ms                                                   | 158 ms: 1.35x slower                                                     |
| pprint_safe_repr          | 962 ms                                                   | 1.32 sec: 1.37x slower                                                   |
| pprint_pformat            | 1.99 sec                                                 | 2.73 sec: 1.37x slower                                                   |
| generators                | 40.3 ms                                                  | 55.4 ms: 1.37x slower                                                    |
| sqlglot_normalize         | 131 ms                                                   | 181 ms: 1.39x slower                                                     |
| genshi_text               | 28.6 ms                                                  | 39.7 ms: 1.39x slower                                                    |
| sympy_sum                 | 151 ms                                                   | 210 ms: 1.39x slower                                                     |
| regex_compile             | 134 ms                                                   | 186 ms: 1.40x slower                                                     |
| python_startup_no_site    | 8.79 ms                                                  | 12.3 ms: 1.40x slower                                                    |
| typing_runtime_protocols  | 197 us                                                   | 276 us: 1.40x slower                                                     |
| sympy_integrate           | 21.4 ms                                                  | 30.1 ms: 1.40x slower                                                    |
| crypto_pyaes              | 84.9 ms                                                  | 119 ms: 1.41x slower                                                     |
| sympy_expand              | 472 ms                                                   | 665 ms: 1.41x slower                                                     |
| fannkuch                  | 478 ms                                                   | 674 ms: 1.41x slower                                                     |
| logging_format            | 8.10 us                                                  | 11.8 us: 1.46x slower                                                    |
| 2to3                      | 313 ms                                                   | 458 ms: 1.46x slower                                                     |
| pyflate                   | 582 ms                                                   | 866 ms: 1.49x slower                                                     |
| logging_simple            | 7.25 us                                                  | 10.8 us: 1.49x slower                                                    |
| bench_thread_pool         | 1.34 ms                                                  | 2.00 ms: 1.50x slower                                                    |
| sqlalchemy_declarative    | 154 ms                                                   | 231 ms: 1.50x slower                                                     |
| sympy_str                 | 265 ms                                                   | 401 ms: 1.51x slower                                                     |
| scimark_lu                | 146 ms                                                   | 223 ms: 1.52x slower                                                     |
| many_optionals            | 626 us                                                   | 975 us: 1.56x slower                                                     |
| nbody                     | 118 ms                                                   | 185 ms: 1.56x slower                                                     |
| float                     | 95.8 ms                                                  | 150 ms: 1.56x slower                                                     |
| scimark_sor               | 164 ms                                                   | 258 ms: 1.57x slower                                                     |
| django_template           | 39.4 ms                                                  | 64.2 ms: 1.63x slower                                                    |
| scimark_monte_carlo       | 87.8 ms                                                  | 143 ms: 1.63x slower                                                     |
| sqlalchemy_imperative     | 16.1 ms                                                  | 26.7 ms: 1.66x slower                                                    |
| unpickle_pure_python      | 265 us                                                   | 440 us: 1.66x slower                                                     |
| hexiom                    | 7.34 ms                                                  | 12.2 ms: 1.67x slower                                                    |
| html5lib                  | 65.6 ms                                                  | 110 ms: 1.68x slower                                                     |
| richards                  | 54.5 ms                                                  | 93.4 ms: 1.71x slower                                                    |
| richards_super            | 60.8 ms                                                  | 106 ms: 1.74x slower                                                     |
| pickle_pure_python        | 374 us                                                   | 661 us: 1.77x slower                                                     |
| chaos                     | 70.7 ms                                                  | 126 ms: 1.79x slower                                                     |
| mako                      | 14.0 ms                                                  | 25.2 ms: 1.80x slower                                                    |
| comprehensions            | 20.8 us                                                  | 38.0 us: 1.83x slower                                                    |
| subparsers                | 20.3 ms                                                  | 37.8 ms: 1.86x slower                                                    |
| sqlglot_transpile         | 1.84 ms                                                  | 3.49 ms: 1.90x slower                                                    |
| logging_silent            | 135 ns                                                   | 269 ns: 2.00x slower                                                     |
| go                        | 164 ms                                                   | 332 ms: 2.02x slower                                                     |
| raytrace                  | 310 ms                                                   | 655 ms: 2.11x slower                                                     |
| sqlglot_parse             | 1.43 ms                                                  | 3.16 ms: 2.21x slower                                                    |
| deltablue                 | 3.97 ms                                                  | 10.8 ms: 2.71x slower                                                    |
| bench_mp_pool             | 8.07 ms                                                  | 61.3 ms: 7.60x slower                                                    |
| Geometric mean            | (ref)                                                    | 1.35x slower                                                             |

Benchmark hidden because not significant (8): pathlib, regex_dna, async_tree_io_tg, pidigits, async_tree_memoization, async_tree_cpu_io_mixed_tg, asyncio_websockets, regex_v8
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250111-3.14.0a3+-22a4421-NOGIL/bm-20250111-arminc-aarch64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.238x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.25x
- 95% likely to have a slowdown of 1.24x
- 99% likely to have a slowdown of 1.21x

# Memory
- memory change: 1.22x