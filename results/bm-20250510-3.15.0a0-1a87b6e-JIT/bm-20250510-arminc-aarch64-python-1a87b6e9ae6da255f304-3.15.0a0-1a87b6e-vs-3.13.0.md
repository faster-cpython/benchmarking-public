# Results vs. 3.13.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-aarch64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.045x slower
- HPT reliability: 84.48%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.09 sec: 1.04x slower                                                  |
| html5lib       | 65.6 ms                                                  | 61.0 ms: 1.08x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.17 sec: 1.02x faster                                                  |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 483 ms: 1.37x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 483 ms: 1.37x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 915 ms: 1.25x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 389 ms: 1.24x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 945 ms: 1.23x faster                                                    |
| async_tree_none            | 504 ms                                                   | 412 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 676 ms: 1.18x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 677 ms: 1.17x faster                                                    |
| async_generators           | 500 ms                                                   | 473 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.18x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 84.4 ms: 1.13x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.83 ms: 1.33x faster                                                   |
| regex_dna      | 263 ms                                                   | 232 ms: 1.13x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 28.9 ms: 1.12x faster                                                   |
| regex_compile  | 134 ms                                                   | 122 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                    | 1.17x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.37 sec: 1.13x faster                                                  |
| xml_etree_iterparse | 159 ms                                                   | 144 ms: 1.10x faster                                                    |
| xml_etree_parse     | 203 ms                                                   | 185 ms: 1.09x faster                                                    |
| xml_etree_generate  | 118 ms                                                   | 111 ms: 1.07x faster                                                    |
| xml_etree_process   | 82.1 ms                                                  | 78.8 ms: 1.04x faster                                                   |
| pickle_pure_python  | 374 us                                                   | 394 us: 1.05x slower                                                    |
| json_loads          | 32.8 us                                                  | 35.3 us: 1.07x slower                                                   |
| Geometric mean      | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): unpickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 27.1 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (3): mako, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.05x faster                                                  |
| deepcopy                   | 479 us                                                   | 338 us: 1.42x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 37.5 us: 1.41x faster                                                   |
| async_tree_memoization     | 664 ms                                                   | 483 ms: 1.37x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 483 ms: 1.37x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.83 ms: 1.33x faster                                                   |
| async_tree_io              | 1.14 sec                                                 | 915 ms: 1.25x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 389 ms: 1.24x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 945 ms: 1.23x faster                                                    |
| async_tree_none            | 504 ms                                                   | 412 ms: 1.22x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.56 us: 1.19x faster                                                   |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 676 ms: 1.18x faster                                                    |
| richards_super             | 60.8 ms                                                  | 51.9 ms: 1.17x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 677 ms: 1.17x faster                                                    |
| richards                   | 54.5 ms                                                  | 46.9 ms: 1.16x faster                                                   |
| telco                      | 10.5 ms                                                  | 9.18 ms: 1.14x faster                                                   |
| float                      | 95.8 ms                                                  | 84.4 ms: 1.13x faster                                                   |
| regex_dna                  | 263 ms                                                   | 232 ms: 1.13x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.37 sec: 1.13x faster                                                  |
| regex_v8                   | 32.5 ms                                                  | 28.9 ms: 1.12x faster                                                   |
| scimark_sor                | 164 ms                                                   | 146 ms: 1.12x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.40 sec: 1.11x faster                                                  |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.10x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 185 ms: 1.09x faster                                                    |
| regex_compile              | 134 ms                                                   | 122 ms: 1.09x faster                                                    |
| scimark_fft                | 463 ms                                                   | 426 ms: 1.09x faster                                                    |
| generators                 | 40.3 ms                                                  | 37.3 ms: 1.08x faster                                                   |
| pylint                     | 345 ms                                                   | 320 ms: 1.08x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 61.0 ms: 1.08x faster                                                   |
| spectral_norm              | 143 ms                                                   | 134 ms: 1.07x faster                                                    |
| xml_etree_generate         | 118 ms                                                   | 111 ms: 1.07x faster                                                    |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                   |
| pathlib                    | 24.3 ms                                                  | 23.0 ms: 1.06x faster                                                   |
| async_generators           | 500 ms                                                   | 473 ms: 1.06x faster                                                    |
| genshi_text                | 28.6 ms                                                  | 27.1 ms: 1.05x faster                                                   |
| sqlite_synth               | 4.08 us                                                  | 3.87 us: 1.05x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.84 sec: 1.05x faster                                                  |
| xml_etree_process          | 82.1 ms                                                  | 78.8 ms: 1.04x faster                                                   |
| pyflate                    | 582 ms                                                   | 567 ms: 1.03x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.17 sec: 1.02x faster                                                  |
| connected_components       | 547 ms                                                   | 566 ms: 1.04x slower                                                    |
| logging_format             | 8.10 us                                                  | 8.41 us: 1.04x slower                                                   |
| sympy_str                  | 265 ms                                                   | 275 ms: 1.04x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.09 sec: 1.04x slower                                                  |
| shortest_path              | 565 ms                                                   | 589 ms: 1.04x slower                                                    |
| fannkuch                   | 478 ms                                                   | 499 ms: 1.04x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 394 us: 1.05x slower                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.03 ms: 1.06x slower                                                   |
| raytrace                   | 310 ms                                                   | 330 ms: 1.06x slower                                                    |
| hexiom                     | 7.34 ms                                                  | 7.82 ms: 1.06x slower                                                   |
| logging_simple             | 7.25 us                                                  | 7.74 us: 1.07x slower                                                   |
| meteor_contest             | 117 ms                                                   | 125 ms: 1.07x slower                                                    |
| json_loads                 | 32.8 us                                                  | 35.3 us: 1.07x slower                                                   |
| typing_runtime_protocols   | 197 us                                                   | 214 us: 1.09x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.71 ms: 1.09x slower                                                   |
| crypto_pyaes               | 84.9 ms                                                  | 93.7 ms: 1.10x slower                                                   |
| comprehensions             | 20.8 us                                                  | 23.6 us: 1.13x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.75 ms: 1.14x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 1.14 sec: 1.19x slower                                                  |
| pprint_pformat             | 1.99 sec                                                 | 2.37 sec: 1.19x slower                                                  |
| subparsers                 | 20.3 ms                                                  | 28.4 ms: 1.39x slower                                                   |
| many_optionals             | 626 us                                                   | 908 us: 1.45x slower                                                    |
| logging_silent             | 135 ns                                                   | 629 ns: 4.67x slower                                                    |
| coverage                   | 106 ms                                                   | 545 ms: 5.15x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 1.40 sec: 173.03x slower                                                |
| thrift                     | 1.01 ms                                                  | 194 ms: 191.49x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.12x slower                                                            |

Benchmark hidden because not significant (23): scimark_monte_carlo, deltablue, sympy_sum, python_startup_no_site, sympy_integrate, mako, unpickle_pure_python, asyncio_websockets, pidigits, chaos, 2to3, nbody, json_dumps, scimark_lu, pycparser, go, genshi_xml, django_template, coroutines, sympy_expand, bench_thread_pool, nqueens, json
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.045x slower

# HPT report

- Reliability score: 84.48% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x