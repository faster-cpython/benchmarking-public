# Results vs. 3.13.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.180x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 364 ms: 1.24x slower                                                        |
| docutils       | 2.83 sec                                                     | 3.27 sec: 1.16x slower                                                      |
| html5lib       | 73.5 ms                                                      | 75.3 ms: 1.02x slower                                                       |
| sphinx         | 1.12 sec                                                     | 1.32 sec: 1.18x slower                                                      |
| Geometric mean | (ref)                                                        | 1.15x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 607 ms: 1.37x faster                                                        |
| async_tree_io              | 843 ms                                                       | 639 ms: 1.32x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 263 ms: 1.32x faster                                                        |
| async_tree_none            | 376 ms                                                       | 293 ms: 1.28x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 357 ms: 1.27x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 377 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 616 ms: 1.06x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 645 ms: 1.07x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 24.5 ms: 1.14x slower                                                       |
| async_generators           | 457 ms                                                       | 536 ms: 1.17x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 80.0 ms: 1.02x faster                                                       |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                        |
| nbody          | 89.3 ms                                                      | 135 ms: 1.52x slower                                                        |
| Geometric mean | (ref)                                                        | 1.14x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.44 ms: 1.07x faster                                                       |
| regex_dna      | 247 ms                                                       | 249 ms: 1.01x slower                                                        |
| regex_v8       | 26.1 ms                                                      | 26.8 ms: 1.02x slower                                                       |
| regex_compile  | 143 ms                                                       | 176 ms: 1.24x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 109 ms: 1.06x slower                                                        |
| tomli_loads          | 2.46 sec                                                     | 2.71 sec: 1.10x slower                                                      |
| xml_etree_parse      | 150 ms                                                       | 169 ms: 1.12x slower                                                        |
| unpickle_pure_python | 217 us                                                       | 295 us: 1.36x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 448 us: 1.39x slower                                                        |
| json_dumps           | 11.1 ms                                                      | 15.5 ms: 1.39x slower                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 124 ms: 1.44x slower                                                        |
| json_loads           | 24.7 us                                                      | 35.6 us: 1.44x slower                                                       |
| xml_etree_process    | 61.2 ms                                                      | 88.3 ms: 1.44x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.30x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 21.2 ms: 1.34x slower                                                       |
| python_startup_no_site | 8.96 ms                                                      | 12.6 ms: 1.40x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.37x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 76.6 ms: 1.34x slower                                                       |
| genshi_text     | 26.2 ms                                                      | 36.5 ms: 1.39x slower                                                       |
| django_template | 36.4 ms                                                      | 51.9 ms: 1.43x slower                                                       |
| mako            | 10.4 ms                                                      | 19.7 ms: 1.90x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.50x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                      | 3.02 ms: 1.57x faster                                                       |
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                        |
| mdp                        | 2.54 sec                                                     | 1.81 sec: 1.40x faster                                                      |
| async_tree_io_tg           | 831 ms                                                       | 607 ms: 1.37x faster                                                        |
| async_tree_io              | 843 ms                                                       | 639 ms: 1.32x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 263 ms: 1.32x faster                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.06 ms: 1.30x faster                                                       |
| async_tree_none            | 376 ms                                                       | 293 ms: 1.28x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 357 ms: 1.27x faster                                                        |
| go                         | 162 ms                                                       | 151 ms: 1.08x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.44 ms: 1.07x faster                                                       |
| deepcopy                   | 392 us                                                       | 374 us: 1.05x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 377 ms: 1.03x faster                                                        |
| float                      | 81.3 ms                                                      | 80.0 ms: 1.02x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 67.9 ms: 1.00x faster                                                       |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                        |
| deepcopy_memo              | 38.6 us                                                      | 38.9 us: 1.01x slower                                                       |
| regex_dna                  | 247 ms                                                       | 249 ms: 1.01x slower                                                        |
| html5lib                   | 73.5 ms                                                      | 75.3 ms: 1.02x slower                                                       |
| regex_v8                   | 26.1 ms                                                      | 26.8 ms: 1.02x slower                                                       |
| pyflate                    | 503 ms                                                       | 522 ms: 1.04x slower                                                        |
| sqlite_synth               | 2.91 us                                                      | 3.08 us: 1.06x slower                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 616 ms: 1.06x slower                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 109 ms: 1.06x slower                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 645 ms: 1.07x slower                                                        |
| generators                 | 33.6 ms                                                      | 35.9 ms: 1.07x slower                                                       |
| tomli_loads                | 2.46 sec                                                     | 2.71 sec: 1.10x slower                                                      |
| pycparser                  | 1.24 sec                                                     | 1.38 sec: 1.11x slower                                                      |
| k_core                     | 2.17 sec                                                     | 2.42 sec: 1.11x slower                                                      |
| xml_etree_parse            | 150 ms                                                       | 169 ms: 1.12x slower                                                        |
| pylint                     | 347 ms                                                       | 394 ms: 1.14x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 24.5 ms: 1.14x slower                                                       |
| connected_components       | 432 ms                                                       | 497 ms: 1.15x slower                                                        |
| hexiom                     | 6.55 ms                                                      | 7.53 ms: 1.15x slower                                                       |
| pathlib                    | 17.5 ms                                                      | 20.3 ms: 1.16x slower                                                       |
| docutils                   | 2.83 sec                                                     | 3.27 sec: 1.16x slower                                                      |
| shortest_path              | 460 ms                                                       | 536 ms: 1.16x slower                                                        |
| async_generators           | 457 ms                                                       | 536 ms: 1.17x slower                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 4.17 us: 1.18x slower                                                       |
| sympy_integrate            | 23.6 ms                                                      | 27.8 ms: 1.18x slower                                                       |
| sphinx                     | 1.12 sec                                                     | 1.32 sec: 1.18x slower                                                      |
| deltablue                  | 3.42 ms                                                      | 4.04 ms: 1.18x slower                                                       |
| json                       | 5.69 ms                                                      | 6.76 ms: 1.19x slower                                                       |
| scimark_sor                | 123 ms                                                       | 147 ms: 1.19x slower                                                        |
| meteor_contest             | 130 ms                                                       | 155 ms: 1.19x slower                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 6.27 sec: 1.23x slower                                                      |
| regex_compile              | 143 ms                                                       | 176 ms: 1.24x slower                                                        |
| richards                   | 52.9 ms                                                      | 65.8 ms: 1.24x slower                                                       |
| 2to3                       | 293 ms                                                       | 364 ms: 1.24x slower                                                        |
| sympy_sum                  | 155 ms                                                       | 198 ms: 1.28x slower                                                        |
| sympy_str                  | 298 ms                                                       | 387 ms: 1.30x slower                                                        |
| richards_super             | 59.6 ms                                                      | 77.6 ms: 1.30x slower                                                       |
| sympy_expand               | 509 ms                                                       | 664 ms: 1.30x slower                                                        |
| many_optionals             | 930 us                                                       | 1.23 ms: 1.32x slower                                                       |
| python_startup             | 15.9 ms                                                      | 21.2 ms: 1.34x slower                                                       |
| genshi_xml                 | 57.1 ms                                                      | 76.6 ms: 1.34x slower                                                       |
| logging_simple             | 6.39 us                                                      | 8.62 us: 1.35x slower                                                       |
| thrift                     | 901 us                                                       | 1.22 ms: 1.35x slower                                                       |
| chaos                      | 60.2 ms                                                      | 81.5 ms: 1.35x slower                                                       |
| nqueens                    | 90.7 ms                                                      | 123 ms: 1.36x slower                                                        |
| scimark_fft                | 328 ms                                                       | 445 ms: 1.36x slower                                                        |
| unpickle_pure_python       | 217 us                                                       | 295 us: 1.36x slower                                                        |
| telco                      | 8.79 ms                                                      | 12.0 ms: 1.36x slower                                                       |
| logging_format             | 6.94 us                                                      | 9.59 us: 1.38x slower                                                       |
| comprehensions             | 17.0 us                                                      | 23.6 us: 1.38x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 448 us: 1.39x slower                                                        |
| genshi_text                | 26.2 ms                                                      | 36.5 ms: 1.39x slower                                                       |
| json_dumps                 | 11.1 ms                                                      | 15.5 ms: 1.39x slower                                                       |
| python_startup_no_site     | 8.96 ms                                                      | 12.6 ms: 1.40x slower                                                       |
| spectral_norm              | 97.0 ms                                                      | 138 ms: 1.42x slower                                                        |
| raytrace                   | 273 ms                                                       | 389 ms: 1.43x slower                                                        |
| django_template            | 36.4 ms                                                      | 51.9 ms: 1.43x slower                                                       |
| pprint_safe_repr           | 843 ms                                                       | 1.20 sec: 1.43x slower                                                      |
| xml_etree_generate         | 86.5 ms                                                      | 124 ms: 1.44x slower                                                        |
| pprint_pformat             | 1.72 sec                                                     | 2.48 sec: 1.44x slower                                                      |
| json_loads                 | 24.7 us                                                      | 35.6 us: 1.44x slower                                                       |
| xml_etree_process          | 61.2 ms                                                      | 88.3 ms: 1.44x slower                                                       |
| scimark_lu                 | 98.7 ms                                                      | 142 ms: 1.44x slower                                                        |
| fannkuch                   | 363 ms                                                       | 544 ms: 1.50x slower                                                        |
| nbody                      | 89.3 ms                                                      | 135 ms: 1.52x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 257 us: 1.52x slower                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 100 ms: 1.52x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 117 ms: 1.59x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 1.50 ms: 1.59x slower                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 7.78 ms: 1.63x slower                                                       |
| coverage                   | 80.0 ms                                                      | 135 ms: 1.69x slower                                                        |
| subparsers                 | 17.5 ms                                                      | 32.0 ms: 1.83x slower                                                       |
| mako                       | 10.4 ms                                                      | 19.7 ms: 1.90x slower                                                       |
| logging_silent             | 97.9 ns                                                      | 780 ns: 7.97x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 61.7 ms: 12.05x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.24x slower                                                                |
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.180x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.15x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: 1.34x