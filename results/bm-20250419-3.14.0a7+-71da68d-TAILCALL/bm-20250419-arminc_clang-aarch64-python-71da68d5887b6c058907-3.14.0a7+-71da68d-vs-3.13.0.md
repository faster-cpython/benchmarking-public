# Results vs. 3.13.0

- fork: python
- ref: 71da68d5887b6c058907
- machine: linux-aarch64
- commit hash: 71da68d
- commit date: 2025-04-19
- overall geometric mean: 1.075x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 289 ms: 1.08x faster                                                     |
| docutils       | 2.96 sec                                                 | 2.90 sec: 1.02x faster                                                   |
| html5lib       | 65.6 ms                                                  | 58.6 ms: 1.12x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.11 sec: 1.08x faster                                                   |
| Geometric mean | (ref)                                                    | 1.08x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 452 ms: 1.46x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 455 ms: 1.46x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 871 ms: 1.34x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 861 ms: 1.32x faster                                                     |
| async_tree_none            | 504 ms                                                   | 381 ms: 1.32x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 368 ms: 1.32x faster                                                     |
| async_generators           | 500 ms                                                   | 416 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 704 ms: 1.14x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 727 ms: 1.09x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 84.0 ms: 1.14x faster                                                    |
| nbody          | 118 ms                                                   | 126 ms: 1.07x slower                                                     |
| pidigits       | 238 ms                                                   | 291 ms: 1.22x slower                                                     |
| Geometric mean | (ref)                                                    | 1.04x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.02 ms: 1.27x faster                                                    |
| regex_dna      | 263 ms                                                   | 232 ms: 1.13x faster                                                     |
| regex_compile  | 134 ms                                                   | 123 ms: 1.09x faster                                                     |
| regex_v8       | 32.5 ms                                                  | 30.3 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                    | 1.14x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate  | 118 ms                                                   | 104 ms: 1.14x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.35 sec: 1.13x faster                                                   |
| xml_etree_process   | 82.1 ms                                                  | 74.9 ms: 1.10x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 150 ms: 1.06x faster                                                     |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (5): unpickle_pure_python, pickle_pure_python, json_dumps, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.09x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.1 ms: 1.09x faster                                                    |
| genshi_xml     | 61.6 ms                                                  | 58.6 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.61 sec: 2.15x faster                                                   |
| deepcopy                   | 479 us                                                   | 308 us: 1.55x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 35.6 us: 1.49x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 452 ms: 1.46x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 455 ms: 1.46x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 871 ms: 1.34x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 861 ms: 1.32x faster                                                     |
| async_tree_none            | 504 ms                                                   | 381 ms: 1.32x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 368 ms: 1.32x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.27 us: 1.30x faster                                                    |
| go                         | 164 ms                                                   | 129 ms: 1.28x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.02 ms: 1.27x faster                                                    |
| spectral_norm              | 143 ms                                                   | 119 ms: 1.21x faster                                                     |
| async_generators           | 500 ms                                                   | 416 ms: 1.20x faster                                                     |
| logging_silent             | 135 ns                                                   | 114 ns: 1.18x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 21.2 ms: 1.15x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.23 sec: 1.15x faster                                                   |
| generators                 | 40.3 ms                                                  | 35.2 ms: 1.14x faster                                                    |
| scimark_sor                | 164 ms                                                   | 144 ms: 1.14x faster                                                     |
| float                      | 95.8 ms                                                  | 84.0 ms: 1.14x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.18 ms: 1.14x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 704 ms: 1.14x faster                                                     |
| xml_etree_generate         | 118 ms                                                   | 104 ms: 1.14x faster                                                     |
| tomli_loads                | 2.67 sec                                                 | 2.35 sec: 1.13x faster                                                   |
| regex_dna                  | 263 ms                                                   | 232 ms: 1.13x faster                                                     |
| html5lib                   | 65.6 ms                                                  | 58.6 ms: 1.12x faster                                                    |
| richards                   | 54.5 ms                                                  | 48.7 ms: 1.12x faster                                                    |
| pylint                     | 345 ms                                                   | 310 ms: 1.12x faster                                                     |
| sympy_sum                  | 151 ms                                                   | 136 ms: 1.11x faster                                                     |
| sympy_integrate            | 21.4 ms                                                  | 19.4 ms: 1.11x faster                                                    |
| pyflate                    | 582 ms                                                   | 527 ms: 1.10x faster                                                     |
| scimark_fft                | 463 ms                                                   | 422 ms: 1.10x faster                                                     |
| pycparser                  | 1.34 sec                                                 | 1.23 sec: 1.10x faster                                                   |
| xml_etree_process          | 82.1 ms                                                  | 74.9 ms: 1.10x faster                                                    |
| genshi_text                | 28.6 ms                                                  | 26.1 ms: 1.09x faster                                                    |
| regex_compile              | 134 ms                                                   | 123 ms: 1.09x faster                                                     |
| chaos                      | 70.7 ms                                                  | 65.1 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 727 ms: 1.09x faster                                                     |
| 2to3                       | 313 ms                                                   | 289 ms: 1.08x faster                                                     |
| sphinx                     | 1.20 sec                                                 | 1.11 sec: 1.08x faster                                                   |
| regex_v8                   | 32.5 ms                                                  | 30.3 ms: 1.07x faster                                                    |
| logging_format             | 8.10 us                                                  | 7.56 us: 1.07x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.79 sec: 1.07x faster                                                   |
| richards_super             | 60.8 ms                                                  | 56.8 ms: 1.07x faster                                                    |
| nqueens                    | 105 ms                                                   | 98.2 ms: 1.07x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 150 ms: 1.06x faster                                                     |
| hexiom                     | 7.34 ms                                                  | 6.94 ms: 1.06x faster                                                    |
| pprint_pformat             | 1.99 sec                                                 | 1.88 sec: 1.06x faster                                                   |
| pprint_safe_repr           | 962 ms                                                   | 913 ms: 1.05x faster                                                     |
| genshi_xml                 | 61.6 ms                                                  | 58.6 ms: 1.05x faster                                                    |
| sqlalchemy_declarative     | 154 ms                                                   | 146 ms: 1.05x faster                                                     |
| sympy_expand               | 472 ms                                                   | 451 ms: 1.05x faster                                                     |
| typing_runtime_protocols   | 197 us                                                   | 188 us: 1.05x faster                                                     |
| sqlite_synth               | 4.08 us                                                  | 3.90 us: 1.05x faster                                                    |
| comprehensions             | 20.8 us                                                  | 20.0 us: 1.04x faster                                                    |
| sympy_str                  | 265 ms                                                   | 257 ms: 1.03x faster                                                     |
| docutils                   | 2.96 sec                                                 | 2.90 sec: 1.02x faster                                                   |
| shortest_path              | 565 ms                                                   | 578 ms: 1.02x slower                                                     |
| connected_components       | 547 ms                                                   | 569 ms: 1.04x slower                                                     |
| nbody                      | 118 ms                                                   | 126 ms: 1.07x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.73 ms: 1.10x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.64 ms: 1.12x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| pidigits                   | 238 ms                                                   | 291 ms: 1.22x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 25.8 ms: 1.27x slower                                                    |
| many_optionals             | 626 us                                                   | 829 us: 1.32x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 1.85 sec: 229.32x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (23): scimark_monte_carlo, logging_simple, unpickle_pure_python, deltablue, coroutines, pickle_pure_python, json, bench_thread_pool, django_template, scimark_lu, meteor_contest, asyncio_websockets, crypto_pyaes, scimark_sparse_mat_mult, mako, sqlalchemy_imperative, coverage, python_startup, json_dumps, json_loads, xml_etree_parse, raytrace, fannkuch
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (13) of results/bm-20250419-3.14.0a7+-71da68d-CLANG/bm-20250419-arminc-aarch64-python-71da68d5887b6c058907-3.14.0a7+-71da68d.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.075x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.07x