# Results vs. 3.13.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.206x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x slower
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 339 ms: 1.27x slower                                                  |
| docutils       | 2.58 sec                                               | 3.16 sec: 1.22x slower                                                |
| html5lib       | 63.4 ms                                                | 75.4 ms: 1.19x slower                                                 |
| sphinx         | 1.03 sec                                               | 1.26 sec: 1.22x slower                                                |
| Geometric mean | (ref)                                                  | 1.23x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 861 ms                                                 | 594 ms: 1.45x faster                                                  |
| async_tree_memoization_tg  | 463 ms                                                 | 336 ms: 1.38x faster                                                  |
| async_tree_io              | 838 ms                                                 | 633 ms: 1.32x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 260 ms: 1.23x faster                                                  |
| async_tree_none            | 350 ms                                                 | 299 ms: 1.17x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 375 ms: 1.16x faster                                                  |
| async_generators           | 433 ms                                                 | 452 ms: 1.04x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 567 ms: 1.04x slower                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 610 ms: 1.06x slower                                                  |
| coroutines                 | 22.2 ms                                                | 28.8 ms: 1.30x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 81.1 ms: 1.03x slower                                                 |
| pidigits       | 186 ms                                                 | 203 ms: 1.09x slower                                                  |
| nbody          | 87.7 ms                                                | 151 ms: 1.73x slower                                                  |
| Geometric mean | (ref)                                                  | 1.25x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 2.99 ms: 1.26x faster                                                 |
| regex_dna      | 220 ms                                                 | 192 ms: 1.15x faster                                                  |
| regex_v8       | 26.9 ms                                                | 23.6 ms: 1.14x faster                                                 |
| regex_compile  | 132 ms                                                 | 172 ms: 1.30x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 101 ms                                                 | 108 ms: 1.07x slower                                                  |
| xml_etree_parse      | 154 ms                                                 | 165 ms: 1.07x slower                                                  |
| tomli_loads          | 2.12 sec                                               | 2.63 sec: 1.24x slower                                                |
| json_loads           | 27.2 us                                                | 37.2 us: 1.37x slower                                                 |
| unpickle_pure_python | 213 us                                                 | 296 us: 1.39x slower                                                  |
| pickle_pure_python   | 302 us                                                 | 424 us: 1.40x slower                                                  |
| xml_etree_generate   | 86.8 ms                                                | 125 ms: 1.43x slower                                                  |
| xml_etree_process    | 60.5 ms                                                | 87.5 ms: 1.45x slower                                                 |
| json_dumps           | 10.1 ms                                                | 14.8 ms: 1.46x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.31x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 17.2 ms: 1.36x slower                                                 |
| python_startup_no_site | 7.00 ms                                                | 10.0 ms: 1.43x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.40x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 50.5 ms                                                | 77.5 ms: 1.54x slower                                                 |
| genshi_text     | 22.6 ms                                                | 35.5 ms: 1.57x slower                                                 |
| django_template | 31.7 ms                                                | 53.5 ms: 1.69x slower                                                 |
| mako            | 10.7 ms                                                | 18.9 ms: 1.77x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.64x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal               | 4.90 ms                                                | 2.89 ms: 1.69x faster                                                 |
| mdp                        | 2.54 sec                                               | 1.74 sec: 1.46x faster                                                |
| async_tree_io_tg           | 861 ms                                                 | 594 ms: 1.45x faster                                                  |
| async_tree_memoization_tg  | 463 ms                                                 | 336 ms: 1.38x faster                                                  |
| async_tree_io              | 838 ms                                                 | 633 ms: 1.32x faster                                                  |
| create_gc_cycles           | 2.45 ms                                                | 1.88 ms: 1.30x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 2.99 ms: 1.26x faster                                                 |
| async_tree_none_tg         | 319 ms                                                 | 260 ms: 1.23x faster                                                  |
| async_tree_none            | 350 ms                                                 | 299 ms: 1.17x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 375 ms: 1.16x faster                                                  |
| regex_dna                  | 220 ms                                                 | 192 ms: 1.15x faster                                                  |
| regex_v8                   | 26.9 ms                                                | 23.6 ms: 1.14x faster                                                 |
| go                         | 141 ms                                                 | 139 ms: 1.01x faster                                                  |
| float                      | 78.7 ms                                                | 81.1 ms: 1.03x slower                                                 |
| async_generators           | 433 ms                                                 | 452 ms: 1.04x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 567 ms: 1.04x slower                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 610 ms: 1.06x slower                                                  |
| deepcopy_memo              | 38.4 us                                                | 40.8 us: 1.06x slower                                                 |
| xml_etree_iterparse        | 101 ms                                                 | 108 ms: 1.07x slower                                                  |
| deepcopy                   | 354 us                                                 | 378 us: 1.07x slower                                                  |
| xml_etree_parse            | 154 ms                                                 | 165 ms: 1.07x slower                                                  |
| pycparser                  | 1.20 sec                                               | 1.29 sec: 1.07x slower                                                |
| pidigits                   | 186 ms                                                 | 203 ms: 1.09x slower                                                  |
| k_core                     | 2.37 sec                                               | 2.58 sec: 1.09x slower                                                |
| sqlite_synth               | 2.90 us                                                | 3.21 us: 1.11x slower                                                 |
| dulwich_log                | 64.6 ms                                                | 73.0 ms: 1.13x slower                                                 |
| pathlib                    | 17.4 ms                                                | 19.7 ms: 1.14x slower                                                 |
| pylint                     | 312 ms                                                 | 357 ms: 1.14x slower                                                  |
| pyflate                    | 470 ms                                                 | 550 ms: 1.17x slower                                                  |
| html5lib                   | 63.4 ms                                                | 75.4 ms: 1.19x slower                                                 |
| shortest_path              | 487 ms                                                 | 587 ms: 1.21x slower                                                  |
| spectral_norm              | 113 ms                                                 | 137 ms: 1.21x slower                                                  |
| connected_components       | 447 ms                                                 | 542 ms: 1.21x slower                                                  |
| docutils                   | 2.58 sec                                               | 3.16 sec: 1.22x slower                                                |
| generators                 | 28.8 ms                                                | 35.1 ms: 1.22x slower                                                 |
| sphinx                     | 1.03 sec                                               | 1.26 sec: 1.22x slower                                                |
| tomli_loads                | 2.12 sec                                               | 2.63 sec: 1.24x slower                                                |
| json                       | 5.32 ms                                                | 6.62 ms: 1.24x slower                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 5.90 sec: 1.26x slower                                                |
| meteor_contest             | 108 ms                                                 | 137 ms: 1.26x slower                                                  |
| sympy_integrate            | 19.8 ms                                                | 25.2 ms: 1.27x slower                                                 |
| 2to3                       | 266 ms                                                 | 339 ms: 1.27x slower                                                  |
| scimark_sor                | 122 ms                                                 | 156 ms: 1.28x slower                                                  |
| deepcopy_reduce            | 3.24 us                                                | 4.18 us: 1.29x slower                                                 |
| coroutines                 | 22.2 ms                                                | 28.8 ms: 1.30x slower                                                 |
| hexiom                     | 6.08 ms                                                | 7.90 ms: 1.30x slower                                                 |
| regex_compile              | 132 ms                                                 | 172 ms: 1.30x slower                                                  |
| scimark_fft                | 367 ms                                                 | 479 ms: 1.31x slower                                                  |
| sympy_sum                  | 150 ms                                                 | 199 ms: 1.32x slower                                                  |
| sympy_str                  | 273 ms                                                 | 369 ms: 1.35x slower                                                  |
| python_startup             | 12.7 ms                                                | 17.2 ms: 1.36x slower                                                 |
| json_loads                 | 27.2 us                                                | 37.2 us: 1.37x slower                                                 |
| sympy_expand               | 456 ms                                                 | 630 ms: 1.38x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 296 us: 1.39x slower                                                  |
| comprehensions             | 16.5 us                                                | 22.9 us: 1.39x slower                                                 |
| chaos                      | 58.0 ms                                                | 81.4 ms: 1.40x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 424 us: 1.40x slower                                                  |
| richards                   | 47.5 ms                                                | 66.9 ms: 1.41x slower                                                 |
| scimark_lu                 | 114 ms                                                 | 161 ms: 1.41x slower                                                  |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 7.11 ms: 1.41x slower                                                 |
| deltablue                  | 3.19 ms                                                | 4.56 ms: 1.43x slower                                                 |
| xml_etree_generate         | 86.8 ms                                                | 125 ms: 1.43x slower                                                  |
| python_startup_no_site     | 7.00 ms                                                | 10.0 ms: 1.43x slower                                                 |
| telco                      | 8.40 ms                                                | 12.1 ms: 1.44x slower                                                 |
| nqueens                    | 80.9 ms                                                | 116 ms: 1.44x slower                                                  |
| richards_super             | 53.7 ms                                                | 77.4 ms: 1.44x slower                                                 |
| many_optionals             | 857 us                                                 | 1.24 ms: 1.44x slower                                                 |
| xml_etree_process          | 60.5 ms                                                | 87.5 ms: 1.45x slower                                                 |
| fannkuch                   | 394 ms                                                 | 573 ms: 1.45x slower                                                  |
| json_dumps                 | 10.1 ms                                                | 14.8 ms: 1.46x slower                                                 |
| thrift                     | 800 us                                                 | 1.18 ms: 1.47x slower                                                 |
| raytrace                   | 262 ms                                                 | 387 ms: 1.48x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 238 us: 1.49x slower                                                  |
| scimark_monte_carlo        | 66.8 ms                                                | 99.8 ms: 1.49x slower                                                 |
| crypto_pyaes               | 74.7 ms                                                | 112 ms: 1.50x slower                                                  |
| genshi_xml                 | 50.5 ms                                                | 77.5 ms: 1.54x slower                                                 |
| coverage                   | 82.8 ms                                                | 128 ms: 1.55x slower                                                  |
| genshi_text                | 22.6 ms                                                | 35.5 ms: 1.57x slower                                                 |
| pprint_safe_repr           | 727 ms                                                 | 1.15 sec: 1.59x slower                                                |
| pprint_pformat             | 1.48 sec                                               | 2.38 sec: 1.61x slower                                                |
| logging_simple             | 5.65 us                                                | 9.09 us: 1.61x slower                                                 |
| logging_format             | 6.23 us                                                | 10.2 us: 1.64x slower                                                 |
| django_template            | 31.7 ms                                                | 53.5 ms: 1.69x slower                                                 |
| nbody                      | 87.7 ms                                                | 151 ms: 1.73x slower                                                  |
| mako                       | 10.7 ms                                                | 18.9 ms: 1.77x slower                                                 |
| subparsers                 | 15.5 ms                                                | 33.7 ms: 2.18x slower                                                 |
| bench_thread_pool          | 818 us                                                 | 3.51 ms: 4.29x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 112 ms: 4.67x slower                                                  |
| logging_silent             | 101 ns                                                 | 755 ns: 7.48x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.29x slower                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.206x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.20x
- 95% likely to have a slowdown of 1.19x
- 99% likely to have a slowdown of 1.15x

# Memory
- memory change: 1.29x