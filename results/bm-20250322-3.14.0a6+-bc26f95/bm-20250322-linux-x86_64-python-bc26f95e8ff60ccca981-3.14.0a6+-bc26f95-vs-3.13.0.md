# Results vs. 3.13.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.043x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 256 ms: 1.04x faster                                                   |
| docutils       | 2.58 sec                                               | 2.60 sec: 1.01x slower                                                 |
| html5lib       | 63.4 ms                                                | 62.8 ms: 1.01x faster                                                  |
| sphinx         | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                   |
| async_tree_io              | 838 ms                                                 | 613 ms: 1.37x faster                                                   |
| async_tree_none            | 350 ms                                                 | 258 ms: 1.36x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 482 ms: 1.19x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 468 ms: 1.16x faster                                                   |
| async_generators           | 433 ms                                                 | 395 ms: 1.10x faster                                                   |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 71.9 ms: 1.09x faster                                                  |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| nbody          | 87.7 ms                                                | 99.0 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.10 ms: 1.22x faster                                                  |
| regex_v8       | 26.9 ms                                                | 23.6 ms: 1.14x faster                                                  |
| regex_compile  | 132 ms                                                 | 126 ms: 1.05x faster                                                   |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 141 ms: 1.09x faster                                                   |
| tomli_loads          | 2.12 sec                                               | 1.95 sec: 1.09x faster                                                 |
| xml_etree_iterparse  | 101 ms                                                 | 98.4 ms: 1.03x faster                                                  |
| xml_etree_process    | 60.5 ms                                                | 59.1 ms: 1.02x faster                                                  |
| xml_etree_generate   | 86.8 ms                                                | 85.6 ms: 1.01x faster                                                  |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                   |
| pickle_pure_python   | 302 us                                                 | 315 us: 1.04x slower                                                   |
| json_loads           | 27.2 us                                                | 29.8 us: 1.10x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 8.17 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 49.0 ms: 1.03x faster                                                  |
| django_template | 31.7 ms                                                | 31.3 ms: 1.01x faster                                                  |
| mako            | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 615 ms: 1.40x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 314 ms: 1.39x faster                                                   |
| async_tree_io              | 838 ms                                                 | 613 ms: 1.37x faster                                                   |
| deepcopy                   | 354 us                                                 | 260 us: 1.37x faster                                                   |
| async_tree_none            | 350 ms                                                 | 258 ms: 1.36x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 29.6 us: 1.30x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 249 ms: 1.28x faster                                                   |
| go                         | 141 ms                                                 | 113 ms: 1.25x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.10 ms: 1.22x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.68 us: 1.21x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 482 ms: 1.19x faster                                                   |
| spectral_norm              | 113 ms                                                 | 96.4 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 468 ms: 1.16x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 23.6 ms: 1.14x faster                                                  |
| pylint                     | 312 ms                                                 | 277 ms: 1.13x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 58.3 ms: 1.11x faster                                                  |
| async_generators           | 433 ms                                                 | 395 ms: 1.10x faster                                                   |
| float                      | 78.7 ms                                                | 71.9 ms: 1.09x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 141 ms: 1.09x faster                                                   |
| tomli_loads                | 2.12 sec                                               | 1.95 sec: 1.09x faster                                                 |
| richards                   | 47.5 ms                                                | 43.9 ms: 1.08x faster                                                  |
| logging_silent             | 101 ns                                                 | 93.7 ns: 1.08x faster                                                  |
| richards_super             | 53.7 ms                                                | 49.9 ms: 1.08x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                 |
| genshi_text                | 22.6 ms                                                | 21.3 ms: 1.06x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.75 ms: 1.06x faster                                                  |
| telco                      | 8.40 ms                                                | 7.94 ms: 1.06x faster                                                  |
| pyflate                    | 470 ms                                                 | 447 ms: 1.05x faster                                                   |
| regex_compile              | 132 ms                                                 | 126 ms: 1.05x faster                                                   |
| sqlite_synth               | 2.90 us                                                | 2.77 us: 1.05x faster                                                  |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.04x faster                                                   |
| scimark_fft                | 367 ms                                                 | 352 ms: 1.04x faster                                                   |
| regex_dna                  | 220 ms                                                 | 212 ms: 1.04x faster                                                   |
| 2to3                       | 266 ms                                                 | 256 ms: 1.04x faster                                                   |
| k_core                     | 2.37 sec                                               | 2.29 sec: 1.03x faster                                                 |
| deltablue                  | 3.19 ms                                                | 3.09 ms: 1.03x faster                                                  |
| thrift                     | 800 us                                                 | 775 us: 1.03x faster                                                   |
| genshi_xml                 | 50.5 ms                                                | 49.0 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 98.4 ms: 1.03x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.9 ms: 1.03x faster                                                  |
| mdp                        | 2.54 sec                                               | 2.48 sec: 1.02x faster                                                 |
| xml_etree_process          | 60.5 ms                                                | 59.1 ms: 1.02x faster                                                  |
| sympy_str                  | 273 ms                                                 | 267 ms: 1.02x faster                                                   |
| logging_simple             | 5.65 us                                                | 5.53 us: 1.02x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.4 ms: 1.02x faster                                                  |
| sqlalchemy_declarative     | 133 ms                                                 | 130 ms: 1.02x faster                                                   |
| sphinx                     | 1.03 sec                                               | 1.01 sec: 1.02x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                   |
| gc_traversal               | 4.90 ms                                                | 4.82 ms: 1.02x faster                                                  |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.62 sec: 1.01x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 85.6 ms: 1.01x faster                                                  |
| django_template            | 31.7 ms                                                | 31.3 ms: 1.01x faster                                                  |
| html5lib                   | 63.4 ms                                                | 62.8 ms: 1.01x faster                                                  |
| logging_format             | 6.23 us                                                | 6.18 us: 1.01x faster                                                  |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| pprint_safe_repr           | 727 ms                                                 | 730 ms: 1.01x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.60 sec: 1.01x slower                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 67.5 ms: 1.01x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.50 sec: 1.01x slower                                                 |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                                  |
| chaos                      | 58.0 ms                                                | 58.8 ms: 1.01x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 75.7 ms: 1.01x slower                                                  |
| raytrace                   | 262 ms                                                 | 266 ms: 1.02x slower                                                   |
| scimark_lu                 | 114 ms                                                 | 116 ms: 1.02x slower                                                   |
| typing_runtime_protocols   | 160 us                                                 | 163 us: 1.02x slower                                                   |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.21 ms: 1.02x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                   |
| nqueens                    | 80.9 ms                                                | 83.6 ms: 1.03x slower                                                  |
| shortest_path              | 487 ms                                                 | 503 ms: 1.03x slower                                                   |
| python_startup             | 12.7 ms                                                | 13.1 ms: 1.03x slower                                                  |
| connected_components       | 447 ms                                                 | 464 ms: 1.04x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 315 us: 1.04x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 869 us: 1.06x slower                                                   |
| mako                       | 10.7 ms                                                | 11.4 ms: 1.07x slower                                                  |
| fannkuch                   | 394 ms                                                 | 422 ms: 1.07x slower                                                   |
| json_loads                 | 27.2 us                                                | 29.8 us: 1.10x slower                                                  |
| many_optionals             | 857 us                                                 | 947 us: 1.10x slower                                                   |
| coverage                   | 82.8 ms                                                | 91.6 ms: 1.11x slower                                                  |
| nbody                      | 87.7 ms                                                | 99.0 ms: 1.13x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 8.17 ms: 1.17x slower                                                  |
| subparsers                 | 15.5 ms                                                | 20.9 ms: 1.35x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 82.8 ms: 3.45x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (5): meteor_contest, generators, sympy_expand, asyncio_websockets, json
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.04x