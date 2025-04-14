# Results vs. 3.13.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.041x faster
- HPT reliability: 96.58%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 264 ms: 1.01x faster                                                   |
| docutils       | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                 |
| html5lib       | 63.4 ms                                                | 62.0 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                   |
| async_tree_io              | 838 ms                                                 | 615 ms: 1.36x faster                                                   |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 476 ms: 1.14x faster                                                   |
| async_generators           | 433 ms                                                 | 418 ms: 1.04x faster                                                   |
| coroutines                 | 22.2 ms                                                | 23.7 ms: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 65.1 ms: 1.21x faster                                                  |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 24.2 ms: 1.11x faster                                                  |
| regex_effbot   | 3.77 ms                                                | 3.55 ms: 1.06x faster                                                  |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                   |
| regex_dna      | 220 ms                                                 | 227 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|---------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads         | 2.12 sec                                               | 1.88 sec: 1.12x faster                                                 |
| xml_etree_parse     | 154 ms                                                 | 140 ms: 1.10x faster                                                   |
| xml_etree_generate  | 86.8 ms                                                | 79.9 ms: 1.09x faster                                                  |
| xml_etree_process   | 60.5 ms                                                | 56.6 ms: 1.07x faster                                                  |
| xml_etree_iterparse | 101 ms                                                 | 97.3 ms: 1.04x faster                                                  |
| pickle_pure_python  | 302 us                                                 | 320 us: 1.06x slower                                                   |
| json_loads          | 27.2 us                                                | 29.7 us: 1.09x slower                                                  |
| json_dumps          | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                  |
| Geometric mean      | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 13.0 ms: 1.03x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 8.15 ms: 1.16x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                  |
| genshi_xml      | 50.5 ms                                                | 49.7 ms: 1.02x faster                                                  |
| django_template | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                  |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 311 ms: 1.49x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 313 ms: 1.39x faster                                                   |
| async_tree_io_tg           | 861 ms                                                 | 620 ms: 1.39x faster                                                   |
| async_tree_io              | 838 ms                                                 | 615 ms: 1.36x faster                                                   |
| deepcopy                   | 354 us                                                 | 261 us: 1.36x faster                                                   |
| async_tree_none            | 350 ms                                                 | 260 ms: 1.35x faster                                                   |
| deepcopy_memo              | 38.4 us                                                | 28.9 us: 1.33x faster                                                  |
| richards                   | 47.5 ms                                                | 36.4 ms: 1.31x faster                                                  |
| richards_super             | 53.7 ms                                                | 41.3 ms: 1.30x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 250 ms: 1.28x faster                                                   |
| float                      | 78.7 ms                                                | 65.1 ms: 1.21x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.73 us: 1.19x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 489 ms: 1.17x faster                                                   |
| scimark_fft                | 367 ms                                                 | 317 ms: 1.16x faster                                                   |
| spectral_norm              | 113 ms                                                 | 98.8 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 476 ms: 1.14x faster                                                   |
| tomli_loads                | 2.12 sec                                               | 1.88 sec: 1.12x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 24.2 ms: 1.11x faster                                                  |
| pylint                     | 312 ms                                                 | 281 ms: 1.11x faster                                                   |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                   |
| xml_etree_generate         | 86.8 ms                                                | 79.9 ms: 1.09x faster                                                  |
| go                         | 141 ms                                                 | 129 ms: 1.09x faster                                                   |
| pyflate                    | 470 ms                                                 | 434 ms: 1.08x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 59.9 ms: 1.08x faster                                                  |
| sqlite_synth               | 2.90 us                                                | 2.70 us: 1.08x faster                                                  |
| xml_etree_process          | 60.5 ms                                                | 56.6 ms: 1.07x faster                                                  |
| genshi_text                | 22.6 ms                                                | 21.2 ms: 1.07x faster                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.71 ms: 1.07x faster                                                  |
| regex_effbot               | 3.77 ms                                                | 3.55 ms: 1.06x faster                                                  |
| gc_traversal               | 4.90 ms                                                | 4.64 ms: 1.06x faster                                                  |
| pathlib                    | 17.4 ms                                                | 16.5 ms: 1.05x faster                                                  |
| deltablue                  | 3.19 ms                                                | 3.05 ms: 1.05x faster                                                  |
| telco                      | 8.40 ms                                                | 8.06 ms: 1.04x faster                                                  |
| logging_silent             | 101 ns                                                 | 97.0 ns: 1.04x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 97.3 ms: 1.04x faster                                                  |
| async_generators           | 433 ms                                                 | 418 ms: 1.04x faster                                                   |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                   |
| mdp                        | 2.54 sec                                               | 2.46 sec: 1.03x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                 |
| html5lib                   | 63.4 ms                                                | 62.0 ms: 1.02x faster                                                  |
| generators                 | 28.8 ms                                                | 28.2 ms: 1.02x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.60 sec: 1.02x faster                                                 |
| thrift                     | 800 us                                                 | 786 us: 1.02x faster                                                   |
| genshi_xml                 | 50.5 ms                                                | 49.7 ms: 1.02x faster                                                  |
| logging_simple             | 5.65 us                                                | 5.56 us: 1.02x faster                                                  |
| logging_format             | 6.23 us                                                | 6.14 us: 1.01x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.19 sec: 1.01x faster                                                 |
| json                       | 5.32 ms                                                | 5.27 ms: 1.01x faster                                                  |
| 2to3                       | 266 ms                                                 | 264 ms: 1.01x faster                                                   |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                   |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                   |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.01x slower                                                   |
| sympy_str                  | 273 ms                                                 | 275 ms: 1.01x slower                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 17.1 ms: 1.01x slower                                                  |
| meteor_contest             | 108 ms                                                 | 110 ms: 1.01x slower                                                   |
| sympy_integrate            | 19.8 ms                                                | 20.1 ms: 1.01x slower                                                  |
| connected_components       | 447 ms                                                 | 453 ms: 1.01x slower                                                   |
| create_gc_cycles           | 2.45 ms                                                | 2.48 ms: 1.01x slower                                                  |
| shortest_path              | 487 ms                                                 | 494 ms: 1.02x slower                                                   |
| django_template            | 31.7 ms                                                | 32.2 ms: 1.02x slower                                                  |
| raytrace                   | 262 ms                                                 | 268 ms: 1.02x slower                                                   |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                   |
| python_startup             | 12.7 ms                                                | 13.0 ms: 1.03x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 68.9 ms: 1.03x slower                                                  |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                  |
| regex_dna                  | 220 ms                                                 | 227 ms: 1.03x slower                                                   |
| chaos                      | 58.0 ms                                                | 60.3 ms: 1.04x slower                                                  |
| nqueens                    | 80.9 ms                                                | 84.1 ms: 1.04x slower                                                  |
| sympy_expand               | 456 ms                                                 | 475 ms: 1.04x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.70 sec: 1.04x slower                                                 |
| pprint_pformat             | 1.48 sec                                               | 1.55 sec: 1.05x slower                                                 |
| coverage                   | 82.8 ms                                                | 87.0 ms: 1.05x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 764 ms: 1.05x slower                                                   |
| fannkuch                   | 394 ms                                                 | 415 ms: 1.06x slower                                                   |
| typing_runtime_protocols   | 160 us                                                 | 169 us: 1.06x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 320 us: 1.06x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.7 ms: 1.07x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 79.9 ms: 1.07x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 880 us: 1.08x slower                                                   |
| json_loads                 | 27.2 us                                                | 29.7 us: 1.09x slower                                                  |
| hexiom                     | 6.08 ms                                                | 6.90 ms: 1.14x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 11.5 ms: 1.14x slower                                                  |
| many_optionals             | 857 us                                                 | 977 us: 1.14x slower                                                   |
| comprehensions             | 16.5 us                                                | 19.0 us: 1.15x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 8.15 ms: 1.16x slower                                                  |
| subparsers                 | 15.5 ms                                                | 21.2 ms: 1.37x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 82.5 ms: 3.44x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (5): sphinx, sqlalchemy_declarative, asyncio_websockets, unpickle_pure_python, nbody
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.041x faster

# HPT report

- Reliability score: 96.58% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x