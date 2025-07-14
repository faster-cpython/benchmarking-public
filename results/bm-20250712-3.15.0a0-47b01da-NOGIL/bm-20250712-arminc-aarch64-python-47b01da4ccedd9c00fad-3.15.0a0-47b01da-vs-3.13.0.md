# Results vs. 3.13.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: linux-aarch64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.089x slower
- HPT reliability: 99.95%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 349 ms: 1.12x slower                                                    |
| docutils       | 2.96 sec                                                 | 3.19 sec: 1.08x slower                                                  |
| html5lib       | 65.6 ms                                                  | 70.2 ms: 1.07x slower                                                   |
| sphinx         | 1.20 sec                                                 | 1.27 sec: 1.05x slower                                                  |
| Geometric mean | (ref)                                                    | 1.08x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 459 ms: 1.44x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 854 ms: 1.36x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 487 ms: 1.36x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 875 ms: 1.30x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 378 ms: 1.28x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 643 ms: 1.24x faster                                                    |
| async_tree_none            | 504 ms                                                   | 407 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 683 ms: 1.16x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                            |

Benchmark hidden because not significant (3): asyncio_websockets, async_generators, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 238 ms                                                   | 232 ms: 1.03x faster                                                    |
| nbody          | 118 ms                                                   | 181 ms: 1.53x slower                                                    |
| Geometric mean | (ref)                                                    | 1.14x slower                                                            |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.94 ms: 1.29x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 26.0 ms: 1.25x faster                                                   |
| regex_dna      | 263 ms                                                   | 237 ms: 1.11x faster                                                    |
| regex_compile  | 134 ms                                                   | 149 ms: 1.12x slower                                                    |
| Geometric mean | (ref)                                                    | 1.13x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 133 ms: 1.20x faster                                                    |
| xml_etree_parse      | 203 ms                                                   | 183 ms: 1.11x faster                                                    |
| tomli_loads          | 2.67 sec                                                 | 2.87 sec: 1.08x slower                                                  |
| json_loads           | 32.8 us                                                  | 36.5 us: 1.11x slower                                                   |
| unpickle_pure_python | 265 us                                                   | 303 us: 1.15x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 140 ms: 1.18x slower                                                    |
| pickle_pure_python   | 374 us                                                   | 450 us: 1.20x slower                                                    |
| xml_etree_process    | 82.1 ms                                                  | 101 ms: 1.24x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.07x slower                                                            |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 20.0 ms: 1.25x slower                                                   |
| python_startup_no_site | 8.79 ms                                                  | 12.1 ms: 1.38x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.31x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 75.2 ms: 1.22x slower                                                   |
| genshi_text     | 28.6 ms                                                  | 35.2 ms: 1.23x slower                                                   |
| django_template | 39.4 ms                                                  | 51.3 ms: 1.30x slower                                                   |
| mako            | 14.0 ms                                                  | 21.1 ms: 1.51x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.31x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 5.92 ms                                                  | 2.87 ms: 2.07x faster                                                   |
| mdp                        | 3.45 sec                                                 | 1.92 sec: 1.79x faster                                                  |
| create_gc_cycles           | 3.39 ms                                                  | 2.24 ms: 1.52x faster                                                   |
| async_tree_memoization_tg  | 663 ms                                                   | 459 ms: 1.44x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 854 ms: 1.36x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 487 ms: 1.36x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 875 ms: 1.30x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.94 ms: 1.29x faster                                                   |
| async_tree_none_tg         | 484 ms                                                   | 378 ms: 1.28x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 26.0 ms: 1.25x faster                                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 643 ms: 1.24x faster                                                    |
| async_tree_none            | 504 ms                                                   | 407 ms: 1.24x faster                                                    |
| deepcopy                   | 479 us                                                   | 394 us: 1.22x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.39 us: 1.20x faster                                                   |
| xml_etree_iterparse        | 159 ms                                                   | 133 ms: 1.20x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 683 ms: 1.16x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 46.5 us: 1.14x faster                                                   |
| regex_dna                  | 263 ms                                                   | 237 ms: 1.11x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 183 ms: 1.11x faster                                                    |
| go                         | 164 ms                                                   | 153 ms: 1.07x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 23.0 ms: 1.06x faster                                                   |
| pidigits                   | 238 ms                                                   | 232 ms: 1.03x faster                                                    |
| k_core                     | 2.99 sec                                                 | 3.05 sec: 1.02x slower                                                  |
| deepcopy_reduce            | 4.24 us                                                  | 4.45 us: 1.05x slower                                                   |
| sphinx                     | 1.20 sec                                                 | 1.27 sec: 1.05x slower                                                  |
| json                       | 5.94 ms                                                  | 6.26 ms: 1.06x slower                                                   |
| logging_silent             | 135 ns                                                   | 143 ns: 1.06x slower                                                    |
| hexiom                     | 7.34 ms                                                  | 7.81 ms: 1.06x slower                                                   |
| html5lib                   | 65.6 ms                                                  | 70.2 ms: 1.07x slower                                                   |
| docutils                   | 2.96 sec                                                 | 3.19 sec: 1.08x slower                                                  |
| tomli_loads                | 2.67 sec                                                 | 2.87 sec: 1.08x slower                                                  |
| pylint                     | 345 ms                                                   | 374 ms: 1.08x slower                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.17 sec: 1.09x slower                                                  |
| pprint_safe_repr           | 962 ms                                                   | 1.05 sec: 1.09x slower                                                  |
| json_loads                 | 32.8 us                                                  | 36.5 us: 1.11x slower                                                   |
| 2to3                       | 313 ms                                                   | 349 ms: 1.12x slower                                                    |
| regex_compile              | 134 ms                                                   | 149 ms: 1.12x slower                                                    |
| logging_format             | 8.10 us                                                  | 9.07 us: 1.12x slower                                                   |
| logging_simple             | 7.25 us                                                  | 8.21 us: 1.13x slower                                                   |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.56 ms: 1.14x slower                                                   |
| chaos                      | 70.7 ms                                                  | 80.5 ms: 1.14x slower                                                   |
| unpickle_pure_python       | 265 us                                                   | 303 us: 1.15x slower                                                    |
| nqueens                    | 105 ms                                                   | 121 ms: 1.15x slower                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 6.94 sec: 1.15x slower                                                  |
| sympy_integrate            | 21.4 ms                                                  | 25.0 ms: 1.17x slower                                                   |
| meteor_contest             | 117 ms                                                   | 137 ms: 1.17x slower                                                    |
| connected_components       | 547 ms                                                   | 645 ms: 1.18x slower                                                    |
| deltablue                  | 3.97 ms                                                  | 4.68 ms: 1.18x slower                                                   |
| thrift                     | 1.01 ms                                                  | 1.19 ms: 1.18x slower                                                   |
| comprehensions             | 20.8 us                                                  | 24.6 us: 1.18x slower                                                   |
| xml_etree_generate         | 118 ms                                                   | 140 ms: 1.18x slower                                                    |
| shortest_path              | 565 ms                                                   | 677 ms: 1.20x slower                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 105 ms: 1.20x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 450 us: 1.20x slower                                                    |
| sympy_sum                  | 151 ms                                                   | 183 ms: 1.21x slower                                                    |
| genshi_xml                 | 61.6 ms                                                  | 75.2 ms: 1.22x slower                                                   |
| genshi_text                | 28.6 ms                                                  | 35.2 ms: 1.23x slower                                                   |
| xml_etree_process          | 82.1 ms                                                  | 101 ms: 1.24x slower                                                    |
| sympy_expand               | 472 ms                                                   | 586 ms: 1.24x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 246 us: 1.25x slower                                                    |
| python_startup             | 16.0 ms                                                  | 20.0 ms: 1.25x slower                                                   |
| fannkuch                   | 478 ms                                                   | 597 ms: 1.25x slower                                                    |
| sympy_str                  | 265 ms                                                   | 333 ms: 1.26x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 107 ms: 1.27x slower                                                    |
| richards                   | 54.5 ms                                                  | 69.8 ms: 1.28x slower                                                   |
| scimark_lu                 | 146 ms                                                   | 189 ms: 1.29x slower                                                    |
| raytrace                   | 310 ms                                                   | 401 ms: 1.29x slower                                                    |
| django_template            | 39.4 ms                                                  | 51.3 ms: 1.30x slower                                                   |
| coverage                   | 106 ms                                                   | 142 ms: 1.34x slower                                                    |
| richards_super             | 60.8 ms                                                  | 82.0 ms: 1.35x slower                                                   |
| bench_thread_pool          | 1.34 ms                                                  | 1.81 ms: 1.36x slower                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 12.1 ms: 1.38x slower                                                   |
| many_optionals             | 626 us                                                   | 905 us: 1.44x slower                                                    |
| mako                       | 14.0 ms                                                  | 21.1 ms: 1.51x slower                                                   |
| nbody                      | 118 ms                                                   | 181 ms: 1.53x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 34.0 ms: 1.67x slower                                                   |
| bench_mp_pool              | 8.07 ms                                                  | 65.2 ms: 8.08x slower                                                   |
| telco                      | 10.5 ms                                                  | 190 ms: 18.15x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.11x slower                                                            |

Benchmark hidden because not significant (11): generators, asyncio_websockets, scimark_sor, float, async_generators, pycparser, spectral_norm, pyflate, scimark_fft, coroutines, json_dumps
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.089x slower

# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.29x