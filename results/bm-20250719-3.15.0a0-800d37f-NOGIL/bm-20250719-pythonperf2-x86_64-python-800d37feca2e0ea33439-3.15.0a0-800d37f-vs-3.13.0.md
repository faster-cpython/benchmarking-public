# Results vs. 3.13.0

- fork: python
- ref: 800d37feca2e0ea33439
- machine: linux-x86_64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.050x slower
- HPT reliability: 96.93%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 319 ms: 1.09x slower                                                        |
| docutils       | 2.83 sec                                                     | 2.92 sec: 1.03x slower                                                      |
| html5lib       | 73.5 ms                                                      | 70.5 ms: 1.04x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.15 sec: 1.03x slower                                                      |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 295 ms: 1.58x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 529 ms: 1.57x faster                                                        |
| async_tree_io              | 843 ms                                                       | 560 ms: 1.51x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 232 ms: 1.49x faster                                                        |
| async_tree_none            | 376 ms                                                       | 264 ms: 1.43x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 323 ms: 1.40x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 465 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 495 ms: 1.22x faster                                                        |
| async_generators           | 457 ms                                                       | 475 ms: 1.04x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.8 ms: 1.06x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.28x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 71.7 ms: 1.13x faster                                                       |
| pidigits       | 252 ms                                                       | 251 ms: 1.00x faster                                                        |
| nbody          | 89.3 ms                                                      | 127 ms: 1.42x slower                                                        |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.8 ms: 1.10x faster                                                       |
| regex_effbot   | 3.67 ms                                                      | 3.46 ms: 1.06x faster                                                       |
| regex_compile  | 143 ms                                                       | 154 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 88.3 ms: 1.16x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.11x faster                                                        |
| tomli_loads          | 2.46 sec                                                     | 2.31 sec: 1.07x faster                                                      |
| json_dumps           | 11.1 ms                                                      | 12.0 ms: 1.08x slower                                                       |
| unpickle_pure_python | 217 us                                                       | 239 us: 1.10x slower                                                        |
| json_loads           | 24.7 us                                                      | 28.0 us: 1.14x slower                                                       |
| pickle_pure_python   | 323 us                                                       | 368 us: 1.14x slower                                                        |
| xml_etree_process    | 61.2 ms                                                      | 70.2 ms: 1.15x slower                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 99.4 ms: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 19.5 ms: 1.23x slower                                                       |
| python_startup_no_site | 8.96 ms                                                      | 11.6 ms: 1.30x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 30.1 ms: 1.15x slower                                                       |
| genshi_xml      | 57.1 ms                                                      | 66.8 ms: 1.17x slower                                                       |
| django_template | 36.4 ms                                                      | 43.1 ms: 1.19x slower                                                       |
| mako            | 10.4 ms                                                      | 17.2 ms: 1.66x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.28x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                      | 2.26 ms: 2.10x faster                                                       |
| mdp                        | 2.54 sec                                                     | 1.45 sec: 1.75x faster                                                      |
| async_tree_memoization_tg  | 466 ms                                                       | 295 ms: 1.58x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 529 ms: 1.57x faster                                                        |
| async_tree_io              | 843 ms                                                       | 560 ms: 1.51x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 232 ms: 1.49x faster                                                        |
| async_tree_none            | 376 ms                                                       | 264 ms: 1.43x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 323 ms: 1.40x faster                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 1.97 ms: 1.36x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 465 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 495 ms: 1.22x faster                                                        |
| deepcopy                   | 392 us                                                       | 321 us: 1.22x faster                                                        |
| go                         | 162 ms                                                       | 138 ms: 1.18x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 88.3 ms: 1.16x faster                                                       |
| deepcopy_memo              | 38.6 us                                                      | 33.9 us: 1.14x faster                                                       |
| float                      | 81.3 ms                                                      | 71.7 ms: 1.13x faster                                                       |
| generators                 | 33.6 ms                                                      | 30.3 ms: 1.11x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.11x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 61.6 ms: 1.11x faster                                                       |
| regex_v8                   | 26.1 ms                                                      | 23.8 ms: 1.10x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.66 us: 1.09x faster                                                       |
| tomli_loads                | 2.46 sec                                                     | 2.31 sec: 1.07x faster                                                      |
| pyflate                    | 503 ms                                                       | 474 ms: 1.06x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.46 ms: 1.06x faster                                                       |
| scimark_sor                | 123 ms                                                       | 117 ms: 1.05x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 70.5 ms: 1.04x faster                                                       |
| json                       | 5.69 ms                                                      | 5.50 ms: 1.03x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 17.1 ms: 1.02x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 96.8 ns: 1.01x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 3.51 us: 1.01x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 5.05 sec: 1.01x faster                                                      |
| pidigits                   | 252 ms                                                       | 251 ms: 1.00x faster                                                        |
| hexiom                     | 6.55 ms                                                      | 6.53 ms: 1.00x faster                                                       |
| pycparser                  | 1.24 sec                                                     | 1.27 sec: 1.03x slower                                                      |
| sphinx                     | 1.12 sec                                                     | 1.15 sec: 1.03x slower                                                      |
| richards                   | 52.9 ms                                                      | 54.7 ms: 1.03x slower                                                       |
| docutils                   | 2.83 sec                                                     | 2.92 sec: 1.03x slower                                                      |
| async_generators           | 457 ms                                                       | 475 ms: 1.04x slower                                                        |
| pprint_safe_repr           | 843 ms                                                       | 884 ms: 1.05x slower                                                        |
| spectral_norm              | 97.0 ms                                                      | 102 ms: 1.05x slower                                                        |
| comprehensions             | 17.0 us                                                      | 18.0 us: 1.06x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 22.8 ms: 1.06x slower                                                       |
| pprint_pformat             | 1.72 sec                                                     | 1.82 sec: 1.06x slower                                                      |
| richards_super             | 59.6 ms                                                      | 63.2 ms: 1.06x slower                                                       |
| sympy_integrate            | 23.6 ms                                                      | 25.2 ms: 1.07x slower                                                       |
| deltablue                  | 3.42 ms                                                      | 3.65 ms: 1.07x slower                                                       |
| k_core                     | 2.17 sec                                                     | 2.32 sec: 1.07x slower                                                      |
| regex_compile              | 143 ms                                                       | 154 ms: 1.08x slower                                                        |
| json_dumps                 | 11.1 ms                                                      | 12.0 ms: 1.08x slower                                                       |
| sympy_expand               | 509 ms                                                       | 551 ms: 1.08x slower                                                        |
| logging_simple             | 6.39 us                                                      | 6.94 us: 1.09x slower                                                       |
| scimark_fft                | 328 ms                                                       | 357 ms: 1.09x slower                                                        |
| 2to3                       | 293 ms                                                       | 319 ms: 1.09x slower                                                        |
| sympy_str                  | 298 ms                                                       | 326 ms: 1.09x slower                                                        |
| unpickle_pure_python       | 217 us                                                       | 239 us: 1.10x slower                                                        |
| chaos                      | 60.2 ms                                                      | 66.3 ms: 1.10x slower                                                       |
| meteor_contest             | 130 ms                                                       | 144 ms: 1.11x slower                                                        |
| sympy_sum                  | 155 ms                                                       | 172 ms: 1.11x slower                                                        |
| thrift                     | 901 us                                                       | 1.00 ms: 1.11x slower                                                       |
| logging_format             | 6.94 us                                                      | 7.78 us: 1.12x slower                                                       |
| shortest_path              | 460 ms                                                       | 518 ms: 1.13x slower                                                        |
| connected_components       | 432 ms                                                       | 490 ms: 1.13x slower                                                        |
| json_loads                 | 24.7 us                                                      | 28.0 us: 1.14x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 368 us: 1.14x slower                                                        |
| xml_etree_process          | 61.2 ms                                                      | 70.2 ms: 1.15x slower                                                       |
| genshi_text                | 26.2 ms                                                      | 30.1 ms: 1.15x slower                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 99.4 ms: 1.15x slower                                                       |
| nqueens                    | 90.7 ms                                                      | 105 ms: 1.16x slower                                                        |
| genshi_xml                 | 57.1 ms                                                      | 66.8 ms: 1.17x slower                                                       |
| raytrace                   | 273 ms                                                       | 322 ms: 1.18x slower                                                        |
| django_template            | 36.4 ms                                                      | 43.1 ms: 1.19x slower                                                       |
| scimark_lu                 | 98.7 ms                                                      | 117 ms: 1.19x slower                                                        |
| many_optionals             | 930 us                                                       | 1.11 ms: 1.19x slower                                                       |
| python_startup             | 15.9 ms                                                      | 19.5 ms: 1.23x slower                                                       |
| typing_runtime_protocols   | 169 us                                                       | 208 us: 1.23x slower                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 81.8 ms: 1.24x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 92.6 ms: 1.26x slower                                                       |
| fannkuch                   | 363 ms                                                       | 460 ms: 1.27x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 11.6 ms: 1.30x slower                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 6.25 ms: 1.31x slower                                                       |
| nbody                      | 89.3 ms                                                      | 127 ms: 1.42x slower                                                        |
| coverage                   | 80.0 ms                                                      | 116 ms: 1.45x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 1.42 ms: 1.51x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 27.3 ms: 1.56x slower                                                       |
| mako                       | 10.4 ms                                                      | 17.2 ms: 1.66x slower                                                       |
| bench_mp_pool              | 5.12 ms                                                      | 57.3 ms: 11.19x slower                                                      |
| telco                      | 8.79 ms                                                      | 175 ms: 19.96x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                |

Benchmark hidden because not significant (3): regex_dna, asyncio_websockets, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250719-3.15.0a0-800d37f-NOGIL/bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.050x slower

# HPT report

- Reliability score: 96.93% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.31x