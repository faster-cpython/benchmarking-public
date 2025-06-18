# Results vs. 3.13.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.092x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 292 ms: 1.10x slower                                                  |
| docutils       | 2.58 sec                                               | 2.85 sec: 1.10x slower                                                |
| html5lib       | 63.4 ms                                                | 64.8 ms: 1.02x slower                                                 |
| sphinx         | 1.03 sec                                               | 1.13 sec: 1.09x slower                                                |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 346 ms: 1.34x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 676 ms: 1.27x faster                                                  |
| async_tree_io              | 838 ms                                                 | 663 ms: 1.26x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 347 ms: 1.26x faster                                                  |
| async_tree_none            | 350 ms                                                 | 289 ms: 1.21x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 276 ms: 1.16x faster                                                  |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                                  |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 602 ms: 1.05x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 593 ms: 1.09x slower                                                  |
| coroutines                 | 22.2 ms                                                | 26.8 ms: 1.21x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 75.3 ms: 1.05x faster                                                 |
| pidigits       | 186 ms                                                 | 205 ms: 1.10x slower                                                  |
| nbody          | 87.7 ms                                                | 106 ms: 1.21x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 2.93 ms: 1.29x faster                                                 |
| regex_dna      | 220 ms                                                 | 197 ms: 1.12x faster                                                  |
| regex_v8       | 26.9 ms                                                | 24.2 ms: 1.11x faster                                                 |
| regex_compile  | 132 ms                                                 | 144 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 2.22 sec: 1.05x slower                                                |
| xml_etree_parse      | 154 ms                                                 | 162 ms: 1.05x slower                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 112 ms: 1.10x slower                                                  |
| unpickle_pure_python | 213 us                                                 | 259 us: 1.21x slower                                                  |
| xml_etree_process    | 60.5 ms                                                | 74.4 ms: 1.23x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 374 us: 1.24x slower                                                  |
| xml_etree_generate   | 86.8 ms                                                | 108 ms: 1.25x slower                                                  |
| json_loads           | 27.2 us                                                | 34.0 us: 1.25x slower                                                 |
| json_dumps           | 10.1 ms                                                | 13.4 ms: 1.33x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.19x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                 |
| python_startup_no_site | 7.00 ms                                                | 7.40 ms: 1.06x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 57.2 ms: 1.13x slower                                                 |
| genshi_text     | 22.6 ms                                                | 25.7 ms: 1.14x slower                                                 |
| mako            | 10.7 ms                                                | 13.6 ms: 1.27x slower                                                 |
| django_template | 31.7 ms                                                | 40.8 ms: 1.29x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.21x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.47 sec: 1.73x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 346 ms: 1.34x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 2.93 ms: 1.29x faster                                                 |
| async_tree_io_tg           | 861 ms                                                 | 676 ms: 1.27x faster                                                  |
| async_tree_io              | 838 ms                                                 | 663 ms: 1.26x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 347 ms: 1.26x faster                                                  |
| async_tree_none            | 350 ms                                                 | 289 ms: 1.21x faster                                                  |
| go                         | 141 ms                                                 | 119 ms: 1.18x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 276 ms: 1.16x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 34.1 us: 1.13x faster                                                 |
| deepcopy                   | 354 us                                                 | 315 us: 1.12x faster                                                  |
| regex_dna                  | 220 ms                                                 | 197 ms: 1.12x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 24.2 ms: 1.11x faster                                                 |
| async_generators           | 433 ms                                                 | 413 ms: 1.05x faster                                                  |
| float                      | 78.7 ms                                                | 75.3 ms: 1.05x faster                                                 |
| dulwich_log                | 64.6 ms                                                | 63.8 ms: 1.01x faster                                                 |
| pyflate                    | 470 ms                                                 | 465 ms: 1.01x faster                                                  |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                  |
| html5lib                   | 63.4 ms                                                | 64.8 ms: 1.02x slower                                                 |
| deepcopy_reduce            | 3.24 us                                                | 3.32 us: 1.03x slower                                                 |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                 |
| gc_traversal               | 4.90 ms                                                | 5.14 ms: 1.05x slower                                                 |
| tomli_loads                | 2.12 sec                                               | 2.22 sec: 1.05x slower                                                |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 602 ms: 1.05x slower                                                  |
| pycparser                  | 1.20 sec                                               | 1.26 sec: 1.05x slower                                                |
| xml_etree_parse            | 154 ms                                                 | 162 ms: 1.05x slower                                                  |
| sympy_integrate            | 19.8 ms                                                | 20.9 ms: 1.06x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                | 7.40 ms: 1.06x slower                                                 |
| pathlib                    | 17.4 ms                                                | 18.4 ms: 1.06x slower                                                 |
| meteor_contest             | 108 ms                                                 | 116 ms: 1.07x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.63 ms: 1.08x slower                                                 |
| regex_compile              | 132 ms                                                 | 144 ms: 1.09x slower                                                  |
| sphinx                     | 1.03 sec                                               | 1.13 sec: 1.09x slower                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 593 ms: 1.09x slower                                                  |
| shortest_path              | 487 ms                                                 | 532 ms: 1.09x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.65 ms: 1.09x slower                                                 |
| djangocms                  | 22.3 us                                                | 24.4 us: 1.09x slower                                                 |
| connected_components       | 447 ms                                                 | 490 ms: 1.10x slower                                                  |
| sqlite_synth               | 2.90 us                                                | 3.18 us: 1.10x slower                                                 |
| pidigits                   | 186 ms                                                 | 205 ms: 1.10x slower                                                  |
| 2to3                       | 266 ms                                                 | 292 ms: 1.10x slower                                                  |
| scimark_sor                | 122 ms                                                 | 134 ms: 1.10x slower                                                  |
| scimark_fft                | 367 ms                                                 | 403 ms: 1.10x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.85 sec: 1.10x slower                                                |
| sympy_sum                  | 150 ms                                                 | 166 ms: 1.10x slower                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 112 ms: 1.10x slower                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.61 ms: 1.11x slower                                                 |
| sympy_str                  | 273 ms                                                 | 308 ms: 1.13x slower                                                  |
| genshi_xml                 | 50.5 ms                                                | 57.2 ms: 1.13x slower                                                 |
| telco                      | 8.40 ms                                                | 9.52 ms: 1.13x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 5.32 sec: 1.13x slower                                                |
| genshi_text                | 22.6 ms                                                | 25.7 ms: 1.14x slower                                                 |
| richards                   | 47.5 ms                                                | 54.3 ms: 1.14x slower                                                 |
| json                       | 5.32 ms                                                | 6.08 ms: 1.14x slower                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 76.4 ms: 1.14x slower                                                 |
| generators                 | 28.8 ms                                                | 33.0 ms: 1.15x slower                                                 |
| crypto_pyaes               | 74.7 ms                                                | 85.6 ms: 1.15x slower                                                 |
| richards_super             | 53.7 ms                                                | 62.2 ms: 1.16x slower                                                 |
| scimark_lu                 | 114 ms                                                 | 133 ms: 1.16x slower                                                  |
| comprehensions             | 16.5 us                                                | 19.3 us: 1.17x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 958 us: 1.17x slower                                                  |
| sympy_expand               | 456 ms                                                 | 541 ms: 1.19x slower                                                  |
| chaos                      | 58.0 ms                                                | 68.8 ms: 1.19x slower                                                 |
| thrift                     | 800 us                                                 | 956 us: 1.20x slower                                                  |
| deltablue                  | 3.19 ms                                                | 3.86 ms: 1.21x slower                                                 |
| coroutines                 | 22.2 ms                                                | 26.8 ms: 1.21x slower                                                 |
| nbody                      | 87.7 ms                                                | 106 ms: 1.21x slower                                                  |
| nqueens                    | 80.9 ms                                                | 98.2 ms: 1.21x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 259 us: 1.21x slower                                                  |
| fannkuch                   | 394 ms                                                 | 479 ms: 1.22x slower                                                  |
| raytrace                   | 262 ms                                                 | 320 ms: 1.23x slower                                                  |
| xml_etree_process          | 60.5 ms                                                | 74.4 ms: 1.23x slower                                                 |
| coverage                   | 82.8 ms                                                | 102 ms: 1.23x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 198 us: 1.23x slower                                                  |
| pickle_pure_python         | 302 us                                                 | 374 us: 1.24x slower                                                  |
| xml_etree_generate         | 86.8 ms                                                | 108 ms: 1.25x slower                                                  |
| json_loads                 | 27.2 us                                                | 34.0 us: 1.25x slower                                                 |
| many_optionals             | 857 us                                                 | 1.08 ms: 1.25x slower                                                 |
| mako                       | 10.7 ms                                                | 13.6 ms: 1.27x slower                                                 |
| django_template            | 31.7 ms                                                | 40.8 ms: 1.29x slower                                                 |
| logging_simple             | 5.65 us                                                | 7.47 us: 1.32x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 13.4 ms: 1.33x slower                                                 |
| logging_format             | 6.23 us                                                | 8.43 us: 1.35x slower                                                 |
| pprint_pformat             | 1.48 sec                                               | 2.01 sec: 1.36x slower                                                |
| pprint_safe_repr           | 727 ms                                                 | 993 ms: 1.37x slower                                                  |
| subparsers                 | 15.5 ms                                                | 28.1 ms: 1.82x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 105 ms: 4.40x slower                                                  |
| logging_silent             | 101 ns                                                 | 623 ns: 6.17x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.12x slower                                                          |

Benchmark hidden because not significant (3): pylint, spectral_norm, k_core
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.092x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 1.05x