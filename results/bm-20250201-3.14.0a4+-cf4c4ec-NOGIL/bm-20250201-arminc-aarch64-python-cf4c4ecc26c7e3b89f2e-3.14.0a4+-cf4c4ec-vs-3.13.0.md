# Results vs. 3.13.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: linux-aarch64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.120x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 379 ms: 1.21x slower                                                     |
| docutils       | 2.96 sec                                                 | 3.38 sec: 1.14x slower                                                   |
| html5lib       | 65.6 ms                                                  | 75.6 ms: 1.15x slower                                                    |
| sphinx         | 1.20 sec                                                 | 1.37 sec: 1.14x slower                                                   |
| Geometric mean | (ref)                                                    | 1.16x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 503 ms: 1.32x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 933 ms: 1.25x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 549 ms: 1.21x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 966 ms: 1.18x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 414 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 695 ms: 1.15x faster                                                     |
| async_tree_none            | 504 ms                                                   | 443 ms: 1.14x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 722 ms: 1.09x faster                                                     |
| async_generators           | 500 ms                                                   | 542 ms: 1.08x slower                                                     |
| Geometric mean             | (ref)                                                    | 1.12x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 103 ms: 1.08x slower                                                     |
| nbody          | 118 ms                                                   | 188 ms: 1.59x slower                                                     |
| Geometric mean | (ref)                                                    | 1.19x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.05 ms: 1.26x faster                                                    |
| regex_compile  | 134 ms                                                   | 158 ms: 1.18x slower                                                     |
| Geometric mean | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 130 ms: 1.22x faster                                                     |
| xml_etree_parse      | 203 ms                                                   | 184 ms: 1.10x faster                                                     |
| unpickle_pure_python | 265 us                                                   | 308 us: 1.17x slower                                                     |
| json_loads           | 32.8 us                                                  | 38.3 us: 1.17x slower                                                    |
| tomli_loads          | 2.67 sec                                                 | 3.20 sec: 1.20x slower                                                   |
| json_dumps           | 14.2 ms                                                  | 17.1 ms: 1.20x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 143 ms: 1.21x slower                                                     |
| xml_etree_process    | 82.1 ms                                                  | 103 ms: 1.26x slower                                                     |
| pickle_pure_python   | 374 us                                                   | 484 us: 1.29x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.12x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 20.0 ms: 1.25x slower                                                    |
| python_startup_no_site | 8.79 ms                                                  | 12.2 ms: 1.39x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.32x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 78.9 ms: 1.28x slower                                                    |
| genshi_text     | 28.6 ms                                                  | 37.1 ms: 1.30x slower                                                    |
| django_template | 39.4 ms                                                  | 55.2 ms: 1.40x slower                                                    |
| mako            | 14.0 ms                                                  | 23.5 ms: 1.68x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.41x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| gc_traversal               | 5.92 ms                                                  | 2.70 ms: 2.20x faster                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 2.16 ms: 1.57x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 503 ms: 1.32x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.05 ms: 1.26x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 933 ms: 1.25x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 130 ms: 1.22x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 549 ms: 1.21x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 966 ms: 1.18x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 414 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 695 ms: 1.15x faster                                                     |
| deepcopy                   | 479 us                                                   | 421 us: 1.14x faster                                                     |
| async_tree_none            | 504 ms                                                   | 443 ms: 1.14x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 184 ms: 1.10x faster                                                     |
| sqlite_synth               | 4.08 us                                                  | 3.71 us: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 722 ms: 1.09x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 22.8 ms: 1.07x faster                                                    |
| scimark_fft                | 463 ms                                                   | 487 ms: 1.05x slower                                                     |
| k_core                     | 2.99 sec                                                 | 3.18 sec: 1.06x slower                                                   |
| pycparser                  | 1.34 sec                                                 | 1.43 sec: 1.07x slower                                                   |
| float                      | 95.8 ms                                                  | 103 ms: 1.08x slower                                                     |
| async_generators           | 500 ms                                                   | 542 ms: 1.08x slower                                                     |
| telco                      | 10.5 ms                                                  | 11.4 ms: 1.09x slower                                                    |
| go                         | 164 ms                                                   | 180 ms: 1.09x slower                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 4.67 us: 1.10x slower                                                    |
| scimark_sor                | 164 ms                                                   | 182 ms: 1.11x slower                                                     |
| json                       | 5.94 ms                                                  | 6.59 ms: 1.11x slower                                                    |
| pylint                     | 345 ms                                                   | 385 ms: 1.12x slower                                                     |
| mdp                        | 3.45 sec                                                 | 3.86 sec: 1.12x slower                                                   |
| pyflate                    | 582 ms                                                   | 655 ms: 1.13x slower                                                     |
| sphinx                     | 1.20 sec                                                 | 1.37 sec: 1.14x slower                                                   |
| docutils                   | 2.96 sec                                                 | 3.38 sec: 1.14x slower                                                   |
| html5lib                   | 65.6 ms                                                  | 75.6 ms: 1.15x slower                                                    |
| logging_silent             | 135 ns                                                   | 156 ns: 1.16x slower                                                     |
| unpickle_pure_python       | 265 us                                                   | 308 us: 1.17x slower                                                     |
| json_loads                 | 32.8 us                                                  | 38.3 us: 1.17x slower                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.85 ms: 1.18x slower                                                    |
| regex_compile              | 134 ms                                                   | 158 ms: 1.18x slower                                                     |
| sqlglot_normalize          | 131 ms                                                   | 156 ms: 1.19x slower                                                     |
| sqlglot_optimize           | 65.2 ms                                                  | 77.7 ms: 1.19x slower                                                    |
| tomli_loads                | 2.67 sec                                                 | 3.20 sec: 1.20x slower                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.38 sec: 1.20x slower                                                   |
| json_dumps                 | 14.2 ms                                                  | 17.1 ms: 1.20x slower                                                    |
| connected_components       | 547 ms                                                   | 658 ms: 1.20x slower                                                     |
| xml_etree_generate         | 118 ms                                                   | 143 ms: 1.21x slower                                                     |
| pprint_safe_repr           | 962 ms                                                   | 1.16 sec: 1.21x slower                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 7.28 sec: 1.21x slower                                                   |
| 2to3                       | 313 ms                                                   | 379 ms: 1.21x slower                                                     |
| shortest_path              | 565 ms                                                   | 691 ms: 1.22x slower                                                     |
| logging_format             | 8.10 us                                                  | 9.96 us: 1.23x slower                                                    |
| thrift                     | 1.01 ms                                                  | 1.24 ms: 1.23x slower                                                    |
| logging_simple             | 7.25 us                                                  | 8.99 us: 1.24x slower                                                    |
| python_startup             | 16.0 ms                                                  | 20.0 ms: 1.25x slower                                                    |
| chaos                      | 70.7 ms                                                  | 88.7 ms: 1.25x slower                                                    |
| xml_etree_process          | 82.1 ms                                                  | 103 ms: 1.26x slower                                                     |
| scimark_monte_carlo        | 87.8 ms                                                  | 112 ms: 1.27x slower                                                     |
| hexiom                     | 7.34 ms                                                  | 9.41 ms: 1.28x slower                                                    |
| genshi_xml                 | 61.6 ms                                                  | 78.9 ms: 1.28x slower                                                    |
| comprehensions             | 20.8 us                                                  | 26.7 us: 1.28x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 484 us: 1.29x slower                                                     |
| sqlglot_transpile          | 1.84 ms                                                  | 2.38 ms: 1.30x slower                                                    |
| meteor_contest             | 117 ms                                                   | 152 ms: 1.30x slower                                                     |
| genshi_text                | 28.6 ms                                                  | 37.1 ms: 1.30x slower                                                    |
| sympy_expand               | 472 ms                                                   | 614 ms: 1.30x slower                                                     |
| sympy_sum                  | 151 ms                                                   | 197 ms: 1.30x slower                                                     |
| sqlalchemy_declarative     | 154 ms                                                   | 201 ms: 1.30x slower                                                     |
| coverage                   | 106 ms                                                   | 140 ms: 1.32x slower                                                     |
| nqueens                    | 105 ms                                                   | 139 ms: 1.33x slower                                                     |
| scimark_lu                 | 146 ms                                                   | 195 ms: 1.33x slower                                                     |
| raytrace                   | 310 ms                                                   | 415 ms: 1.34x slower                                                     |
| crypto_pyaes               | 84.9 ms                                                  | 115 ms: 1.35x slower                                                     |
| sympy_integrate            | 21.4 ms                                                  | 29.2 ms: 1.36x slower                                                    |
| richards                   | 54.5 ms                                                  | 75.1 ms: 1.38x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 12.2 ms: 1.39x slower                                                    |
| sympy_str                  | 265 ms                                                   | 368 ms: 1.39x slower                                                     |
| sqlalchemy_imperative      | 16.1 ms                                                  | 22.4 ms: 1.39x slower                                                    |
| sqlglot_parse              | 1.43 ms                                                  | 2.00 ms: 1.40x slower                                                    |
| django_template            | 39.4 ms                                                  | 55.2 ms: 1.40x slower                                                    |
| fannkuch                   | 478 ms                                                   | 672 ms: 1.41x slower                                                     |
| bench_thread_pool          | 1.34 ms                                                  | 1.88 ms: 1.41x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 282 us: 1.43x slower                                                     |
| richards_super             | 60.8 ms                                                  | 88.4 ms: 1.45x slower                                                    |
| many_optionals             | 626 us                                                   | 944 us: 1.51x slower                                                     |
| deltablue                  | 3.97 ms                                                  | 6.17 ms: 1.56x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 32.2 ms: 1.59x slower                                                    |
| nbody                      | 118 ms                                                   | 188 ms: 1.59x slower                                                     |
| mako                       | 14.0 ms                                                  | 23.5 ms: 1.68x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 54.9 ms: 6.80x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.16x slower                                                             |

Benchmark hidden because not significant (8): regex_v8, pidigits, deepcopy_memo, regex_dna, spectral_norm, asyncio_websockets, coroutines, generators
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250201-3.14.0a4+-cf4c4ec-NOGIL/bm-20250201-arminc-aarch64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.120x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.12x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.23x