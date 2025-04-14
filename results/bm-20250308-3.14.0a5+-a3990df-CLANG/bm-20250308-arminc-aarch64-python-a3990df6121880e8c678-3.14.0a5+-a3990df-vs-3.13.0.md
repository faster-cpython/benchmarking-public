# Results vs. 3.13.0

- fork: python
- ref: a3990df6121880e8c678
- machine: linux-aarch64
- commit hash: a3990df
- commit date: 2025-03-08
- overall geometric mean: 1.092x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 284 ms: 1.10x faster                                                     |
| docutils       | 2.96 sec                                                 | 2.87 sec: 1.03x faster                                                   |
| html5lib       | 65.6 ms                                                  | 57.3 ms: 1.14x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.08 sec: 1.11x faster                                                   |
| Geometric mean | (ref)                                                    | 1.10x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 453 ms: 1.46x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 454 ms: 1.46x faster                                                     |
| async_tree_none            | 504 ms                                                   | 364 ms: 1.39x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 847 ms: 1.38x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 357 ms: 1.36x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 861 ms: 1.32x faster                                                     |
| async_generators           | 500 ms                                                   | 395 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 703 ms: 1.14x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 712 ms: 1.11x faster                                                     |
| coroutines                 | 29.4 ms                                                  | 27.4 ms: 1.07x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.26x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 84.4 ms: 1.13x faster                                                    |
| nbody          | 118 ms                                                   | 112 ms: 1.06x faster                                                     |
| pidigits       | 238 ms                                                   | 296 ms: 1.24x slower                                                     |
| Geometric mean | (ref)                                                    | 1.01x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.21 ms: 1.21x faster                                                    |
| regex_compile  | 134 ms                                                   | 121 ms: 1.10x faster                                                     |
| regex_dna      | 263 ms                                                   | 245 ms: 1.07x faster                                                     |
| Geometric mean | (ref)                                                    | 1.10x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate  | 118 ms                                                   | 100 ms: 1.18x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.29 sec: 1.16x faster                                                   |
| xml_etree_process   | 82.1 ms                                                  | 72.1 ms: 1.14x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 149 ms: 1.07x faster                                                     |
| Geometric mean      | (ref)                                                    | 1.06x faster                                                             |

Benchmark hidden because not significant (5): unpickle_pure_python, json_dumps, pickle_pure_python, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.1 ms: 1.15x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.07x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 26.3 ms: 1.08x faster                                                    |
| genshi_xml      | 61.6 ms                                                  | 57.2 ms: 1.08x faster                                                    |
| django_template | 39.4 ms                                                  | 37.2 ms: 1.06x faster                                                    |
| mako            | 14.0 ms                                                  | 13.4 ms: 1.04x faster                                                    |
| Geometric mean  | (ref)                                                    | 1.06x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 292 us: 1.64x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 34.6 us: 1.53x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 453 ms: 1.46x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 454 ms: 1.46x faster                                                     |
| spectral_norm              | 143 ms                                                   | 102 ms: 1.40x faster                                                     |
| async_tree_none            | 504 ms                                                   | 364 ms: 1.39x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 847 ms: 1.38x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 357 ms: 1.36x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 861 ms: 1.32x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.26 us: 1.30x faster                                                    |
| scimark_fft                | 463 ms                                                   | 363 ms: 1.27x faster                                                     |
| async_generators           | 500 ms                                                   | 395 ms: 1.27x faster                                                     |
| go                         | 164 ms                                                   | 131 ms: 1.25x faster                                                     |
| scimark_sor                | 164 ms                                                   | 135 ms: 1.22x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.21 ms: 1.21x faster                                                    |
| logging_silent             | 135 ns                                                   | 114 ns: 1.18x faster                                                     |
| xml_etree_generate         | 118 ms                                                   | 100 ms: 1.18x faster                                                     |
| scimark_monte_carlo        | 87.8 ms                                                  | 75.2 ms: 1.17x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.29 sec: 1.16x faster                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 5.19 sec: 1.16x faster                                                   |
| coverage                   | 106 ms                                                   | 91.3 ms: 1.16x faster                                                    |
| pylint                     | 345 ms                                                   | 299 ms: 1.16x faster                                                     |
| pyflate                    | 582 ms                                                   | 506 ms: 1.15x faster                                                     |
| html5lib                   | 65.6 ms                                                  | 57.3 ms: 1.14x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 21.3 ms: 1.14x faster                                                    |
| generators                 | 40.3 ms                                                  | 35.4 ms: 1.14x faster                                                    |
| xml_etree_process          | 82.1 ms                                                  | 72.1 ms: 1.14x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 703 ms: 1.14x faster                                                     |
| richards                   | 54.5 ms                                                  | 48.0 ms: 1.14x faster                                                    |
| float                      | 95.8 ms                                                  | 84.4 ms: 1.13x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.24 ms: 1.13x faster                                                    |
| typing_runtime_protocols   | 197 us                                                   | 174 us: 1.13x faster                                                     |
| richards_super             | 60.8 ms                                                  | 53.9 ms: 1.13x faster                                                    |
| sqlglot_transpile          | 1.84 ms                                                  | 1.64 ms: 1.12x faster                                                    |
| logging_format             | 8.10 us                                                  | 7.26 us: 1.12x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.08 sec: 1.11x faster                                                   |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 5.98 ms: 1.11x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.21 sec: 1.11x faster                                                   |
| comprehensions             | 20.8 us                                                  | 18.8 us: 1.11x faster                                                    |
| sqlglot_normalize          | 131 ms                                                   | 118 ms: 1.11x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 712 ms: 1.11x faster                                                     |
| chaos                      | 70.7 ms                                                  | 63.9 ms: 1.11x faster                                                    |
| scimark_lu                 | 146 ms                                                   | 132 ms: 1.10x faster                                                     |
| logging_simple             | 7.25 us                                                  | 6.58 us: 1.10x faster                                                    |
| 2to3                       | 313 ms                                                   | 284 ms: 1.10x faster                                                     |
| regex_compile              | 134 ms                                                   | 121 ms: 1.10x faster                                                     |
| sqlalchemy_declarative     | 154 ms                                                   | 140 ms: 1.10x faster                                                     |
| thrift                     | 1.01 ms                                                  | 918 us: 1.10x faster                                                     |
| sqlglot_optimize           | 65.2 ms                                                  | 59.4 ms: 1.10x faster                                                    |
| sqlalchemy_imperative      | 16.1 ms                                                  | 14.7 ms: 1.10x faster                                                    |
| mdp                        | 3.45 sec                                                 | 3.16 sec: 1.09x faster                                                   |
| sqlite_synth               | 4.08 us                                                  | 3.74 us: 1.09x faster                                                    |
| sympy_integrate            | 21.4 ms                                                  | 19.7 ms: 1.09x faster                                                    |
| nqueens                    | 105 ms                                                   | 96.5 ms: 1.09x faster                                                    |
| sympy_sum                  | 151 ms                                                   | 139 ms: 1.09x faster                                                     |
| genshi_text                | 28.6 ms                                                  | 26.3 ms: 1.08x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.76 sec: 1.08x faster                                                   |
| pprint_pformat             | 1.99 sec                                                 | 1.84 sec: 1.08x faster                                                   |
| genshi_xml                 | 61.6 ms                                                  | 57.2 ms: 1.08x faster                                                    |
| coroutines                 | 29.4 ms                                                  | 27.4 ms: 1.07x faster                                                    |
| regex_dna                  | 263 ms                                                   | 245 ms: 1.07x faster                                                     |
| sqlglot_parse              | 1.43 ms                                                  | 1.34 ms: 1.07x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 149 ms: 1.07x faster                                                     |
| pprint_safe_repr           | 962 ms                                                   | 903 ms: 1.06x faster                                                     |
| sympy_expand               | 472 ms                                                   | 444 ms: 1.06x faster                                                     |
| hexiom                     | 7.34 ms                                                  | 6.90 ms: 1.06x faster                                                    |
| nbody                      | 118 ms                                                   | 112 ms: 1.06x faster                                                     |
| django_template            | 39.4 ms                                                  | 37.2 ms: 1.06x faster                                                    |
| bench_thread_pool          | 1.34 ms                                                  | 1.27 ms: 1.05x faster                                                    |
| deltablue                  | 3.97 ms                                                  | 3.78 ms: 1.05x faster                                                    |
| meteor_contest             | 117 ms                                                   | 113 ms: 1.04x faster                                                     |
| mako                       | 14.0 ms                                                  | 13.4 ms: 1.04x faster                                                    |
| sympy_str                  | 265 ms                                                   | 255 ms: 1.04x faster                                                     |
| docutils                   | 2.96 sec                                                 | 2.87 sec: 1.03x faster                                                   |
| connected_components       | 547 ms                                                   | 531 ms: 1.03x faster                                                     |
| shortest_path              | 565 ms                                                   | 550 ms: 1.03x faster                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.61 ms: 1.07x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.62 ms: 1.12x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 10.1 ms: 1.15x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 25.0 ms: 1.23x slower                                                    |
| pidigits                   | 238 ms                                                   | 296 ms: 1.24x slower                                                     |
| many_optionals             | 626 us                                                   | 814 us: 1.30x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 5.87 sec: 727.15x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (12): json, unpickle_pure_python, raytrace, asyncio_websockets, json_dumps, crypto_pyaes, fannkuch, regex_v8, python_startup, pickle_pure_python, json_loads, xml_etree_parse
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250308-3.14.0a5+-a3990df-CLANG/bm-20250308-arminc-aarch64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.092x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.06x