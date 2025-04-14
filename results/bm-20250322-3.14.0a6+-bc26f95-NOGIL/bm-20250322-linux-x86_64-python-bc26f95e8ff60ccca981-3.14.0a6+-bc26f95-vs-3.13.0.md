# Results vs. 3.13.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.072x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 296 ms: 1.11x slower                                                   |
| docutils       | 2.58 sec                                               | 2.78 sec: 1.07x slower                                                 |
| html5lib       | 63.4 ms                                                | 68.0 ms: 1.07x slower                                                  |
| sphinx         | 1.03 sec                                               | 1.10 sec: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 536 ms: 1.61x faster                                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                                   |
| async_tree_io              | 838 ms                                                 | 577 ms: 1.45x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 238 ms: 1.34x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 352 ms: 1.24x faster                                                   |
| async_tree_none            | 350 ms                                                 | 283 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 459 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 507 ms: 1.13x faster                                                   |
| async_generators           | 433 ms                                                 | 448 ms: 1.03x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 75.5 ms: 1.04x faster                                                  |
| pidigits       | 186 ms                                                 | 181 ms: 1.03x faster                                                   |
| nbody          | 87.7 ms                                                | 134 ms: 1.53x slower                                                   |
| Geometric mean | (ref)                                                  | 1.13x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.9 ms                                                | 21.8 ms: 1.23x faster                                                  |
| regex_effbot   | 3.77 ms                                                | 3.31 ms: 1.14x faster                                                  |
| regex_compile  | 132 ms                                                 | 149 ms: 1.13x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 95.2 ms: 1.06x faster                                                  |
| xml_etree_parse      | 154 ms                                                 | 150 ms: 1.03x faster                                                   |
| xml_etree_generate   | 86.8 ms                                                | 94.4 ms: 1.09x slower                                                  |
| tomli_loads          | 2.12 sec                                               | 2.33 sec: 1.10x slower                                                 |
| xml_etree_process    | 60.5 ms                                                | 66.9 ms: 1.11x slower                                                  |
| pickle_pure_python   | 302 us                                                 | 351 us: 1.16x slower                                                   |
| unpickle_pure_python | 213 us                                                 | 252 us: 1.18x slower                                                   |
| json_loads           | 27.2 us                                                | 33.0 us: 1.22x slower                                                  |
| json_dumps           | 10.1 ms                                                | 12.9 ms: 1.27x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 15.5 ms: 1.23x slower                                                  |
| python_startup_no_site | 7.00 ms                                                | 10.9 ms: 1.56x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.38x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 59.5 ms: 1.18x slower                                                  |
| genshi_text     | 22.6 ms                                                | 28.5 ms: 1.26x slower                                                  |
| django_template | 31.7 ms                                                | 40.1 ms: 1.27x slower                                                  |
| mako            | 10.7 ms                                                | 16.2 ms: 1.51x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.30x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| gc_traversal               | 4.90 ms                                                | 2.17 ms: 2.26x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 536 ms: 1.61x faster                                                   |
| async_tree_memoization_tg  | 463 ms                                                 | 309 ms: 1.50x faster                                                   |
| create_gc_cycles           | 2.45 ms                                                | 1.68 ms: 1.45x faster                                                  |
| async_tree_io              | 838 ms                                                 | 577 ms: 1.45x faster                                                   |
| async_tree_none_tg         | 319 ms                                                 | 238 ms: 1.34x faster                                                   |
| async_tree_memoization     | 437 ms                                                 | 352 ms: 1.24x faster                                                   |
| async_tree_none            | 350 ms                                                 | 283 ms: 1.24x faster                                                   |
| regex_v8                   | 26.9 ms                                                | 21.8 ms: 1.23x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 459 ms: 1.18x faster                                                   |
| deepcopy                   | 354 us                                                 | 308 us: 1.15x faster                                                   |
| regex_effbot               | 3.77 ms                                                | 3.31 ms: 1.14x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 507 ms: 1.13x faster                                                   |
| xml_etree_iterparse        | 101 ms                                                 | 95.2 ms: 1.06x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.13 sec: 1.06x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.75 us: 1.06x faster                                                  |
| float                      | 78.7 ms                                                | 75.5 ms: 1.04x faster                                                  |
| xml_etree_parse            | 154 ms                                                 | 150 ms: 1.03x faster                                                   |
| pidigits                   | 186 ms                                                 | 181 ms: 1.03x faster                                                   |
| dulwich_log                | 64.6 ms                                                | 63.1 ms: 1.02x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 3.20 us: 1.01x faster                                                  |
| pathlib                    | 17.4 ms                                                | 17.3 ms: 1.00x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 38.7 us: 1.01x slower                                                  |
| go                         | 141 ms                                                 | 142 ms: 1.01x slower                                                   |
| k_core                     | 2.37 sec                                               | 2.44 sec: 1.03x slower                                                 |
| async_generators           | 433 ms                                                 | 448 ms: 1.03x slower                                                   |
| spectral_norm              | 113 ms                                                 | 119 ms: 1.05x slower                                                   |
| generators                 | 28.8 ms                                                | 30.3 ms: 1.05x slower                                                  |
| json                       | 5.32 ms                                                | 5.64 ms: 1.06x slower                                                  |
| sphinx                     | 1.03 sec                                               | 1.10 sec: 1.06x slower                                                 |
| pyflate                    | 470 ms                                                 | 504 ms: 1.07x slower                                                   |
| coroutines                 | 22.2 ms                                                | 23.8 ms: 1.07x slower                                                  |
| html5lib                   | 63.4 ms                                                | 68.0 ms: 1.07x slower                                                  |
| docutils                   | 2.58 sec                                               | 2.78 sec: 1.07x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 5.08 sec: 1.08x slower                                                 |
| xml_etree_generate         | 86.8 ms                                                | 94.4 ms: 1.09x slower                                                  |
| tomli_loads                | 2.12 sec                                               | 2.33 sec: 1.10x slower                                                 |
| xml_etree_process          | 60.5 ms                                                | 66.9 ms: 1.11x slower                                                  |
| thrift                     | 800 us                                                 | 886 us: 1.11x slower                                                   |
| telco                      | 8.40 ms                                                | 9.31 ms: 1.11x slower                                                  |
| 2to3                       | 266 ms                                                 | 296 ms: 1.11x slower                                                   |
| richards                   | 47.5 ms                                                | 53.4 ms: 1.12x slower                                                  |
| regex_compile              | 132 ms                                                 | 149 ms: 1.13x slower                                                   |
| mdp                        | 2.54 sec                                               | 2.87 sec: 1.13x slower                                                 |
| scimark_sor                | 122 ms                                                 | 138 ms: 1.13x slower                                                   |
| logging_silent             | 101 ns                                                 | 115 ns: 1.14x slower                                                   |
| scimark_fft                | 367 ms                                                 | 422 ms: 1.15x slower                                                   |
| pprint_safe_repr           | 727 ms                                                 | 837 ms: 1.15x slower                                                   |
| sympy_str                  | 273 ms                                                 | 315 ms: 1.15x slower                                                   |
| sympy_sum                  | 150 ms                                                 | 174 ms: 1.16x slower                                                   |
| pickle_pure_python         | 302 us                                                 | 351 us: 1.16x slower                                                   |
| sympy_integrate            | 19.8 ms                                                | 23.0 ms: 1.16x slower                                                  |
| sympy_expand               | 456 ms                                                 | 530 ms: 1.16x slower                                                   |
| richards_super             | 53.7 ms                                                | 62.6 ms: 1.17x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.73 sec: 1.17x slower                                                 |
| logging_simple             | 5.65 us                                                | 6.65 us: 1.18x slower                                                  |
| genshi_xml                 | 50.5 ms                                                | 59.5 ms: 1.18x slower                                                  |
| shortest_path              | 487 ms                                                 | 574 ms: 1.18x slower                                                   |
| unpickle_pure_python       | 213 us                                                 | 252 us: 1.18x slower                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 159 ms: 1.19x slower                                                   |
| connected_components       | 447 ms                                                 | 537 ms: 1.20x slower                                                   |
| sqlalchemy_imperative      | 16.9 ms                                                | 20.3 ms: 1.20x slower                                                  |
| logging_format             | 6.23 us                                                | 7.50 us: 1.20x slower                                                  |
| meteor_contest             | 108 ms                                                 | 131 ms: 1.20x slower                                                   |
| chaos                      | 58.0 ms                                                | 70.1 ms: 1.21x slower                                                  |
| crypto_pyaes               | 74.7 ms                                                | 90.2 ms: 1.21x slower                                                  |
| json_loads                 | 27.2 us                                                | 33.0 us: 1.22x slower                                                  |
| comprehensions             | 16.5 us                                                | 20.1 us: 1.22x slower                                                  |
| nqueens                    | 80.9 ms                                                | 98.9 ms: 1.22x slower                                                  |
| deltablue                  | 3.19 ms                                                | 3.91 ms: 1.22x slower                                                  |
| python_startup             | 12.7 ms                                                | 15.5 ms: 1.23x slower                                                  |
| many_optionals             | 857 us                                                 | 1.06 ms: 1.24x slower                                                  |
| scimark_lu                 | 114 ms                                                 | 144 ms: 1.26x slower                                                   |
| genshi_text                | 22.6 ms                                                | 28.5 ms: 1.26x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 202 us: 1.26x slower                                                   |
| django_template            | 31.7 ms                                                | 40.1 ms: 1.27x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 12.9 ms: 1.27x slower                                                  |
| hexiom                     | 6.08 ms                                                | 7.76 ms: 1.28x slower                                                  |
| raytrace                   | 262 ms                                                 | 335 ms: 1.28x slower                                                   |
| fannkuch                   | 394 ms                                                 | 511 ms: 1.30x slower                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 6.56 ms: 1.30x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 87.2 ms: 1.31x slower                                                  |
| coverage                   | 82.8 ms                                                | 121 ms: 1.46x slower                                                   |
| mako                       | 10.7 ms                                                | 16.2 ms: 1.51x slower                                                  |
| nbody                      | 87.7 ms                                                | 134 ms: 1.53x slower                                                   |
| subparsers                 | 15.5 ms                                                | 24.1 ms: 1.56x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 10.9 ms: 1.56x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 91.0 ms: 3.79x slower                                                  |
| bench_thread_pool          | 818 us                                                 | 3.26 ms: 3.99x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.11x slower                                                           |

Benchmark hidden because not significant (3): pylint, regex_dna, asyncio_websockets
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95-NOGIL/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.072x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.24x