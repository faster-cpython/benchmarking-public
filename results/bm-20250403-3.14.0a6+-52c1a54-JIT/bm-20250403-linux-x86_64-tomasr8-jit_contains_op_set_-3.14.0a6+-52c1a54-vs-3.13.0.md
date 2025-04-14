# Results vs. 3.13.0

- fork: tomasr8
- ref: jit_contains_op_set_
- machine: linux-x86_64
- commit hash: 52c1a54
- commit date: 2025-04-03
- overall geometric mean: 1.057x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 253 ms: 1.05x faster                                                    |
| docutils       | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                  |
| html5lib       | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                            |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                    |
| async_tree_memoization     | 437 ms                                                 | 311 ms: 1.40x faster                                                    |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                    |
| async_tree_io              | 838 ms                                                 | 608 ms: 1.38x faster                                                    |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 477 ms: 1.20x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                                    |
| async_generators           | 433 ms                                                 | 417 ms: 1.04x faster                                                    |
| coroutines                 | 22.2 ms                                                | 24.3 ms: 1.09x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 64.8 ms: 1.21x faster                                                   |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| nbody          | 87.7 ms                                                | 89.2 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.36 ms: 1.12x faster                                                   |
| regex_v8       | 26.9 ms                                                | 24.0 ms: 1.12x faster                                                   |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                    |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|---------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.12 sec                                               | 1.85 sec: 1.15x faster                                                  |
| xml_etree_parse     | 154 ms                                                 | 140 ms: 1.10x faster                                                    |
| xml_etree_process   | 60.5 ms                                                | 55.4 ms: 1.09x faster                                                   |
| xml_etree_generate  | 86.8 ms                                                | 79.6 ms: 1.09x faster                                                   |
| xml_etree_iterparse | 101 ms                                                 | 97.2 ms: 1.04x faster                                                   |
| pickle_pure_python  | 302 us                                                 | 324 us: 1.07x slower                                                    |
| json_loads          | 27.2 us                                                | 29.6 us: 1.09x slower                                                   |
| json_dumps          | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                   |
| Geometric mean      | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                   |
| python_startup_no_site | 7.00 ms                                                | 8.20 ms: 1.17x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                   |
| genshi_xml      | 50.5 ms                                                | 48.8 ms: 1.03x faster                                                   |
| django_template | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                   |
| mako            | 10.7 ms                                                | 10.9 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.21 sec: 2.10x faster                                                  |
| async_tree_memoization_tg  | 463 ms                                                 | 317 ms: 1.46x faster                                                    |
| deepcopy                   | 354 us                                                 | 250 us: 1.42x faster                                                    |
| async_tree_memoization     | 437 ms                                                 | 311 ms: 1.40x faster                                                    |
| async_tree_io_tg           | 861 ms                                                 | 614 ms: 1.40x faster                                                    |
| async_tree_io              | 838 ms                                                 | 608 ms: 1.38x faster                                                    |
| deepcopy_memo              | 38.4 us                                                | 28.6 us: 1.34x faster                                                   |
| async_tree_none            | 350 ms                                                 | 262 ms: 1.34x faster                                                    |
| async_tree_none_tg         | 319 ms                                                 | 251 ms: 1.27x faster                                                    |
| richards                   | 47.5 ms                                                | 38.4 ms: 1.24x faster                                                   |
| deepcopy_reduce            | 3.24 us                                                | 2.64 us: 1.23x faster                                                   |
| float                      | 78.7 ms                                                | 64.8 ms: 1.21x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 477 ms: 1.20x faster                                                    |
| scimark_fft                | 367 ms                                                 | 307 ms: 1.20x faster                                                    |
| richards_super             | 53.7 ms                                                | 45.3 ms: 1.19x faster                                                   |
| go                         | 141 ms                                                 | 122 ms: 1.15x faster                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 474 ms: 1.15x faster                                                    |
| tomli_loads                | 2.12 sec                                               | 1.85 sec: 1.15x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.36 ms: 1.12x faster                                                   |
| spectral_norm              | 113 ms                                                 | 101 ms: 1.12x faster                                                    |
| regex_v8                   | 26.9 ms                                                | 24.0 ms: 1.12x faster                                                   |
| pylint                     | 312 ms                                                 | 280 ms: 1.11x faster                                                    |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                    |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.58 ms: 1.10x faster                                                   |
| xml_etree_process          | 60.5 ms                                                | 55.4 ms: 1.09x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 79.6 ms: 1.09x faster                                                   |
| pyflate                    | 470 ms                                                 | 432 ms: 1.09x faster                                                    |
| telco                      | 8.40 ms                                                | 7.82 ms: 1.07x faster                                                   |
| genshi_text                | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 60.8 ms: 1.06x faster                                                   |
| sqlite_synth               | 2.90 us                                                | 2.74 us: 1.06x faster                                                   |
| deltablue                  | 3.19 ms                                                | 3.02 ms: 1.06x faster                                                   |
| scimark_sor                | 122 ms                                                 | 116 ms: 1.05x faster                                                    |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                    |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                                  |
| 2to3                       | 266 ms                                                 | 253 ms: 1.05x faster                                                    |
| bpe_tokeniser              | 4.69 sec                                               | 4.48 sec: 1.05x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 97.2 ms: 1.04x faster                                                   |
| async_generators           | 433 ms                                                 | 417 ms: 1.04x faster                                                    |
| logging_silent             | 101 ns                                                 | 97.5 ns: 1.04x faster                                                   |
| genshi_xml                 | 50.5 ms                                                | 48.8 ms: 1.03x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                  |
| gc_traversal               | 4.90 ms                                                | 4.76 ms: 1.03x faster                                                   |
| html5lib                   | 63.4 ms                                                | 61.9 ms: 1.02x faster                                                   |
| chaos                      | 58.0 ms                                                | 56.9 ms: 1.02x faster                                                   |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                    |
| pathlib                    | 17.4 ms                                                | 17.1 ms: 1.02x faster                                                   |
| sympy_integrate            | 19.8 ms                                                | 19.6 ms: 1.01x faster                                                   |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| create_gc_cycles           | 2.45 ms                                                | 2.44 ms: 1.00x faster                                                   |
| crypto_pyaes               | 74.7 ms                                                | 75.2 ms: 1.01x slower                                                   |
| django_template            | 31.7 ms                                                | 31.9 ms: 1.01x slower                                                   |
| logging_simple             | 5.65 us                                                | 5.71 us: 1.01x slower                                                   |
| connected_components       | 447 ms                                                 | 452 ms: 1.01x slower                                                    |
| pprint_safe_repr           | 727 ms                                                 | 735 ms: 1.01x slower                                                    |
| logging_format             | 6.23 us                                                | 6.33 us: 1.02x slower                                                   |
| nbody                      | 87.7 ms                                                | 89.2 ms: 1.02x slower                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                   |
| mako                       | 10.7 ms                                                | 10.9 ms: 1.02x slower                                                   |
| typing_runtime_protocols   | 160 us                                                 | 164 us: 1.03x slower                                                    |
| pprint_pformat             | 1.48 sec                                               | 1.52 sec: 1.03x slower                                                  |
| nqueens                    | 80.9 ms                                                | 83.2 ms: 1.03x slower                                                   |
| generators                 | 28.8 ms                                                | 29.6 ms: 1.03x slower                                                   |
| sympy_expand               | 456 ms                                                 | 472 ms: 1.03x slower                                                    |
| docutils                   | 2.58 sec                                               | 2.67 sec: 1.03x slower                                                  |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                   |
| fannkuch                   | 394 ms                                                 | 414 ms: 1.05x slower                                                    |
| coverage                   | 82.8 ms                                                | 88.4 ms: 1.07x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 324 us: 1.07x slower                                                    |
| bench_thread_pool          | 818 us                                                 | 885 us: 1.08x slower                                                    |
| json_loads                 | 27.2 us                                                | 29.6 us: 1.09x slower                                                   |
| coroutines                 | 22.2 ms                                                | 24.3 ms: 1.09x slower                                                   |
| many_optionals             | 857 us                                                 | 946 us: 1.10x slower                                                    |
| hexiom                     | 6.08 ms                                                | 6.71 ms: 1.10x slower                                                   |
| comprehensions             | 16.5 us                                                | 18.3 us: 1.11x slower                                                   |
| json_dumps                 | 10.1 ms                                                | 11.6 ms: 1.15x slower                                                   |
| python_startup_no_site     | 7.00 ms                                                | 8.20 ms: 1.17x slower                                                   |
| subparsers                 | 15.5 ms                                                | 21.0 ms: 1.36x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 82.3 ms: 3.43x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                            |

Benchmark hidden because not significant (12): sphinx, scimark_monte_carlo, sympy_str, json, shortest_path, meteor_contest, unpickle_pure_python, raytrace, asyncio_websockets, sqlalchemy_declarative, sympy_sum, scimark_lu
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250403-3.14.0a6+-52c1a54-JIT/bm-20250403-linux-x86_64-tomasr8-jit_contains_op_set_-3.14.0a6+-52c1a54.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.057x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x