# Results vs. 3.13.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.085x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 299 ms: 1.13x slower                                                  |
| docutils       | 2.58 sec                                               | 2.93 sec: 1.13x slower                                                |
| html5lib       | 63.4 ms                                                | 66.7 ms: 1.05x slower                                                 |
| sphinx         | 1.03 sec                                               | 1.14 sec: 1.11x slower                                                |
| Geometric mean | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 353 ms: 1.31x faster                                                  |
| async_tree_io              | 838 ms                                                 | 662 ms: 1.27x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 348 ms: 1.26x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 691 ms: 1.25x faster                                                  |
| async_tree_none            | 350 ms                                                 | 290 ms: 1.21x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 278 ms: 1.15x faster                                                  |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                  |
| async_generators           | 433 ms                                                 | 438 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 597 ms: 1.04x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 586 ms: 1.08x slower                                                  |
| coroutines                 | 22.2 ms                                                | 27.6 ms: 1.24x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 69.8 ms: 1.13x faster                                                 |
| pidigits       | 186 ms                                                 | 207 ms: 1.11x slower                                                  |
| nbody          | 87.7 ms                                                | 97.8 ms: 1.12x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.06 ms: 1.23x faster                                                 |
| regex_dna      | 220 ms                                                 | 198 ms: 1.11x faster                                                  |
| regex_v8       | 26.9 ms                                                | 24.7 ms: 1.09x faster                                                 |
| regex_compile  | 132 ms                                                 | 145 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.12 sec                                               | 2.08 sec: 1.02x faster                                                |
| xml_etree_parse      | 154 ms                                                 | 159 ms: 1.03x slower                                                  |
| unpickle_pure_python | 213 us                                                 | 234 us: 1.10x slower                                                  |
| xml_etree_iterparse  | 101 ms                                                 | 111 ms: 1.10x slower                                                  |
| xml_etree_process    | 60.5 ms                                                | 68.6 ms: 1.14x slower                                                 |
| xml_etree_generate   | 86.8 ms                                                | 101 ms: 1.16x slower                                                  |
| json_loads           | 27.2 us                                                | 33.5 us: 1.23x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 378 us: 1.25x slower                                                  |
| json_dumps           | 10.1 ms                                                | 13.6 ms: 1.34x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.14x slower                                                          |

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
| genshi_text     | 22.6 ms                                                | 25.8 ms: 1.14x slower                                                 |
| genshi_xml      | 50.5 ms                                                | 58.7 ms: 1.16x slower                                                 |
| mako            | 10.7 ms                                                | 13.3 ms: 1.24x slower                                                 |
| django_template | 31.7 ms                                                | 40.9 ms: 1.29x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.21x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.49 sec: 1.71x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 353 ms: 1.31x faster                                                  |
| async_tree_io              | 838 ms                                                 | 662 ms: 1.27x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 348 ms: 1.26x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 691 ms: 1.25x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.06 ms: 1.23x faster                                                 |
| richards                   | 47.5 ms                                                | 39.1 ms: 1.21x faster                                                 |
| async_tree_none            | 350 ms                                                 | 290 ms: 1.21x faster                                                  |
| richards_super             | 53.7 ms                                                | 45.9 ms: 1.17x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 278 ms: 1.15x faster                                                  |
| float                      | 78.7 ms                                                | 69.8 ms: 1.13x faster                                                 |
| deepcopy                   | 354 us                                                 | 318 us: 1.11x faster                                                  |
| regex_dna                  | 220 ms                                                 | 198 ms: 1.11x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 35.1 us: 1.09x faster                                                 |
| go                         | 141 ms                                                 | 129 ms: 1.09x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 24.7 ms: 1.09x faster                                                 |
| spectral_norm              | 113 ms                                                 | 104 ms: 1.09x faster                                                  |
| scimark_fft                | 367 ms                                                 | 341 ms: 1.08x faster                                                  |
| pyflate                    | 470 ms                                                 | 458 ms: 1.02x faster                                                  |
| tomli_loads                | 2.12 sec                                               | 2.08 sec: 1.02x faster                                                |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                  |
| async_generators           | 433 ms                                                 | 438 ms: 1.01x slower                                                  |
| dulwich_log                | 64.6 ms                                                | 65.5 ms: 1.01x slower                                                 |
| xml_etree_parse            | 154 ms                                                 | 159 ms: 1.03x slower                                                  |
| python_startup             | 12.7 ms                                                | 13.2 ms: 1.04x slower                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 597 ms: 1.04x slower                                                  |
| pathlib                    | 17.4 ms                                                | 18.2 ms: 1.05x slower                                                 |
| deepcopy_reduce            | 3.24 us                                                | 3.39 us: 1.05x slower                                                 |
| shortest_path              | 487 ms                                                 | 511 ms: 1.05x slower                                                  |
| sqlite_synth               | 2.90 us                                                | 3.05 us: 1.05x slower                                                 |
| connected_components       | 447 ms                                                 | 470 ms: 1.05x slower                                                  |
| html5lib                   | 63.4 ms                                                | 66.7 ms: 1.05x slower                                                 |
| python_startup_no_site     | 7.00 ms                                                | 7.40 ms: 1.06x slower                                                 |
| gc_traversal               | 4.90 ms                                                | 5.19 ms: 1.06x slower                                                 |
| meteor_contest             | 108 ms                                                 | 116 ms: 1.07x slower                                                  |
| pycparser                  | 1.20 sec                                               | 1.28 sec: 1.07x slower                                                |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.38 ms: 1.07x slower                                                 |
| deltablue                  | 3.19 ms                                                | 3.44 ms: 1.08x slower                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 586 ms: 1.08x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.64 ms: 1.08x slower                                                 |
| sympy_integrate            | 19.8 ms                                                | 21.6 ms: 1.09x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 5.11 sec: 1.09x slower                                                |
| unpickle_pure_python       | 213 us                                                 | 234 us: 1.10x slower                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 111 ms: 1.10x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 73.5 ms: 1.10x slower                                                 |
| regex_compile              | 132 ms                                                 | 145 ms: 1.10x slower                                                  |
| sphinx                     | 1.03 sec                                               | 1.14 sec: 1.11x slower                                                |
| pidigits                   | 186 ms                                                 | 207 ms: 1.11x slower                                                  |
| djangocms                  | 22.3 us                                                | 24.8 us: 1.11x slower                                                 |
| nbody                      | 87.7 ms                                                | 97.8 ms: 1.12x slower                                                 |
| scimark_sor                | 122 ms                                                 | 136 ms: 1.12x slower                                                  |
| 2to3                       | 266 ms                                                 | 299 ms: 1.13x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 170 ms: 1.13x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.93 sec: 1.13x slower                                                |
| xml_etree_process          | 60.5 ms                                                | 68.6 ms: 1.14x slower                                                 |
| genshi_text                | 22.6 ms                                                | 25.8 ms: 1.14x slower                                                 |
| telco                      | 8.40 ms                                                | 9.58 ms: 1.14x slower                                                 |
| hexiom                     | 6.08 ms                                                | 6.94 ms: 1.14x slower                                                 |
| json                       | 5.32 ms                                                | 6.09 ms: 1.14x slower                                                 |
| crypto_pyaes               | 74.7 ms                                                | 85.9 ms: 1.15x slower                                                 |
| sympy_str                  | 273 ms                                                 | 317 ms: 1.16x slower                                                  |
| genshi_xml                 | 50.5 ms                                                | 58.7 ms: 1.16x slower                                                 |
| xml_etree_generate         | 86.8 ms                                                | 101 ms: 1.16x slower                                                  |
| fannkuch                   | 394 ms                                                 | 465 ms: 1.18x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 966 us: 1.18x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 136 ms: 1.19x slower                                                  |
| thrift                     | 800 us                                                 | 961 us: 1.20x slower                                                  |
| chaos                      | 58.0 ms                                                | 69.9 ms: 1.21x slower                                                 |
| sympy_expand               | 456 ms                                                 | 552 ms: 1.21x slower                                                  |
| comprehensions             | 16.5 us                                                | 20.0 us: 1.21x slower                                                 |
| raytrace                   | 262 ms                                                 | 321 ms: 1.23x slower                                                  |
| generators                 | 28.8 ms                                                | 35.4 ms: 1.23x slower                                                 |
| json_loads                 | 27.2 us                                                | 33.5 us: 1.23x slower                                                 |
| coverage                   | 82.8 ms                                                | 103 ms: 1.24x slower                                                  |
| coroutines                 | 22.2 ms                                                | 27.6 ms: 1.24x slower                                                 |
| mako                       | 10.7 ms                                                | 13.3 ms: 1.24x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 378 us: 1.25x slower                                                  |
| nqueens                    | 80.9 ms                                                | 102 ms: 1.26x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 205 us: 1.28x slower                                                  |
| django_template            | 31.7 ms                                                | 40.9 ms: 1.29x slower                                                 |
| many_optionals             | 857 us                                                 | 1.11 ms: 1.29x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 13.6 ms: 1.34x slower                                                 |
| logging_simple             | 5.65 us                                                | 7.66 us: 1.36x slower                                                 |
| logging_format             | 6.23 us                                                | 8.58 us: 1.38x slower                                                 |
| pprint_pformat             | 1.48 sec                                               | 2.10 sec: 1.42x slower                                                |
| pprint_safe_repr           | 727 ms                                                 | 1.03 sec: 1.42x slower                                                |
| subparsers                 | 15.5 ms                                                | 28.7 ms: 1.86x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 105 ms: 4.38x slower                                                  |
| logging_silent             | 101 ns                                                 | 633 ns: 6.27x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.11x slower                                                          |

Benchmark hidden because not significant (2): pylint, k_core
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.085x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.07x