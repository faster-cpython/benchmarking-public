# Results vs. 3.13.0

- fork: python
- ref: 48d0d0dd9733eae4935f
- machine: linux-x86_64
- commit hash: 48d0d0d
- commit date: 2025-09-26
- overall geometric mean: 1.049x slower
- HPT reliability: 91.35%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 312 ms: 1.07x slower                                                        |
| docutils       | 2.83 sec                                                     | 2.89 sec: 1.02x slower                                                      |
| html5lib       | 73.5 ms                                                      | 70.4 ms: 1.04x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.15 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 291 ms: 1.60x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 523 ms: 1.59x faster                                                        |
| async_tree_io              | 843 ms                                                       | 555 ms: 1.52x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 230 ms: 1.50x faster                                                        |
| async_tree_none            | 376 ms                                                       | 261 ms: 1.44x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 320 ms: 1.42x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 465 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 494 ms: 1.22x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 371 ms: 1.05x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                       |
| async_generators           | 457 ms                                                       | 480 ms: 1.05x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 71.8 ms: 1.13x faster                                                       |
| pidigits       | 252 ms                                                       | 251 ms: 1.01x faster                                                        |
| nbody          | 89.3 ms                                                      | 126 ms: 1.41x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.6 ms: 1.11x faster                                                       |
| regex_dna      | 247 ms                                                       | 231 ms: 1.07x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.57 ms: 1.03x faster                                                       |
| regex_compile  | 143 ms                                                       | 154 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 88.3 ms: 1.16x faster                                                       |
| tomli_loads          | 2.46 sec                                                     | 2.15 sec: 1.15x faster                                                      |
| xml_etree_parse      | 150 ms                                                       | 136 ms: 1.10x faster                                                        |
| json_dumps           | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                                       |
| unpickle_pure_python | 217 us                                                       | 241 us: 1.11x slower                                                        |
| json_loads           | 24.7 us                                                      | 27.6 us: 1.12x slower                                                       |
| pickle_pure_python   | 323 us                                                       | 364 us: 1.13x slower                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 99.0 ms: 1.14x slower                                                       |
| xml_etree_process    | 61.2 ms                                                      | 70.8 ms: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 19.2 ms: 1.21x slower                                                       |
| python_startup_no_site | 8.96 ms                                                      | 11.8 ms: 1.31x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 29.9 ms: 1.14x slower                                                       |
| genshi_xml      | 57.1 ms                                                      | 66.5 ms: 1.17x slower                                                       |
| django_template | 36.4 ms                                                      | 43.2 ms: 1.19x slower                                                       |
| mako            | 10.4 ms                                                      | 17.3 ms: 1.67x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.28x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                      | 2.19 ms: 2.17x faster                                                       |
| mdp                        | 2.54 sec                                                     | 1.45 sec: 1.75x faster                                                      |
| async_tree_memoization_tg  | 466 ms                                                       | 291 ms: 1.60x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 523 ms: 1.59x faster                                                        |
| async_tree_io              | 843 ms                                                       | 555 ms: 1.52x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 230 ms: 1.50x faster                                                        |
| async_tree_none            | 376 ms                                                       | 261 ms: 1.44x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 320 ms: 1.42x faster                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 1.94 ms: 1.38x faster                                                       |
| deepcopy                   | 392 us                                                       | 300 us: 1.31x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 30.6 us: 1.26x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 465 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 494 ms: 1.22x faster                                                        |
| go                         | 162 ms                                                       | 139 ms: 1.17x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 88.3 ms: 1.16x faster                                                       |
| tomli_loads                | 2.46 sec                                                     | 2.15 sec: 1.15x faster                                                      |
| float                      | 81.3 ms                                                      | 71.8 ms: 1.13x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 15.5 ms: 1.13x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 61.3 ms: 1.11x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.62 us: 1.11x faster                                                       |
| regex_v8                   | 26.1 ms                                                      | 23.6 ms: 1.11x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 136 ms: 1.10x faster                                                        |
| regex_dna                  | 247 ms                                                       | 231 ms: 1.07x faster                                                        |
| scimark_sor                | 123 ms                                                       | 116 ms: 1.06x faster                                                        |
| pyflate                    | 503 ms                                                       | 474 ms: 1.06x faster                                                        |
| json                       | 5.69 ms                                                      | 5.37 ms: 1.06x faster                                                       |
| generators                 | 33.6 ms                                                      | 31.8 ms: 1.06x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 3.37 us: 1.05x faster                                                       |
| asyncio_websockets         | 388 ms                                                       | 371 ms: 1.05x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 70.4 ms: 1.04x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.57 ms: 1.03x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 5.03 sec: 1.01x faster                                                      |
| pidigits                   | 252 ms                                                       | 251 ms: 1.01x faster                                                        |
| hexiom                     | 6.55 ms                                                      | 6.52 ms: 1.01x faster                                                       |
| pycparser                  | 1.24 sec                                                     | 1.24 sec: 1.00x faster                                                      |
| sphinx                     | 1.12 sec                                                     | 1.15 sec: 1.02x slower                                                      |
| docutils                   | 2.83 sec                                                     | 2.89 sec: 1.02x slower                                                      |
| json_dumps                 | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                                       |
| spectral_norm              | 97.0 ms                                                      | 101 ms: 1.04x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                       |
| async_generators           | 457 ms                                                       | 480 ms: 1.05x slower                                                        |
| richards                   | 52.9 ms                                                      | 55.8 ms: 1.05x slower                                                       |
| deltablue                  | 3.42 ms                                                      | 3.60 ms: 1.05x slower                                                       |
| pprint_safe_repr           | 843 ms                                                       | 894 ms: 1.06x slower                                                        |
| sympy_integrate            | 23.6 ms                                                      | 25.0 ms: 1.06x slower                                                       |
| 2to3                       | 293 ms                                                       | 312 ms: 1.07x slower                                                        |
| comprehensions             | 17.0 us                                                      | 18.3 us: 1.07x slower                                                       |
| k_core                     | 2.17 sec                                                     | 2.33 sec: 1.07x slower                                                      |
| pprint_pformat             | 1.72 sec                                                     | 1.85 sec: 1.08x slower                                                      |
| regex_compile              | 143 ms                                                       | 154 ms: 1.08x slower                                                        |
| richards_super             | 59.6 ms                                                      | 64.3 ms: 1.08x slower                                                       |
| sympy_expand               | 509 ms                                                       | 552 ms: 1.08x slower                                                        |
| logging_simple             | 6.39 us                                                      | 6.97 us: 1.09x slower                                                       |
| sympy_str                  | 298 ms                                                       | 325 ms: 1.09x slower                                                        |
| sympy_sum                  | 155 ms                                                       | 170 ms: 1.10x slower                                                        |
| thrift                     | 901 us                                                       | 990 us: 1.10x slower                                                        |
| chaos                      | 60.2 ms                                                      | 66.4 ms: 1.10x slower                                                       |
| unpickle_pure_python       | 217 us                                                       | 241 us: 1.11x slower                                                        |
| shortest_path              | 460 ms                                                       | 514 ms: 1.12x slower                                                        |
| connected_components       | 432 ms                                                       | 483 ms: 1.12x slower                                                        |
| json_loads                 | 24.7 us                                                      | 27.6 us: 1.12x slower                                                       |
| meteor_contest             | 130 ms                                                       | 145 ms: 1.12x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 364 us: 1.13x slower                                                        |
| logging_format             | 6.94 us                                                      | 7.82 us: 1.13x slower                                                       |
| genshi_text                | 26.2 ms                                                      | 29.9 ms: 1.14x slower                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 99.0 ms: 1.14x slower                                                       |
| xml_etree_process          | 61.2 ms                                                      | 70.8 ms: 1.16x slower                                                       |
| nqueens                    | 90.7 ms                                                      | 105 ms: 1.16x slower                                                        |
| genshi_xml                 | 57.1 ms                                                      | 66.5 ms: 1.17x slower                                                       |
| raytrace                   | 273 ms                                                       | 319 ms: 1.17x slower                                                        |
| scimark_lu                 | 98.7 ms                                                      | 116 ms: 1.18x slower                                                        |
| django_template            | 36.4 ms                                                      | 43.2 ms: 1.19x slower                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.72 ms: 1.20x slower                                                       |
| python_startup             | 15.9 ms                                                      | 19.2 ms: 1.21x slower                                                       |
| bench_mp_pool              | 5.12 ms                                                      | 6.32 ms: 1.23x slower                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 81.7 ms: 1.24x slower                                                       |
| typing_runtime_protocols   | 169 us                                                       | 209 us: 1.24x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 91.7 ms: 1.25x slower                                                       |
| fannkuch                   | 363 ms                                                       | 456 ms: 1.26x slower                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 11.8 ms: 1.31x slower                                                       |
| many_optionals             | 930 us                                                       | 1.30 ms: 1.39x slower                                                       |
| nbody                      | 89.3 ms                                                      | 126 ms: 1.41x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 1.37 ms: 1.45x slower                                                       |
| coverage                   | 80.0 ms                                                      | 120 ms: 1.50x slower                                                        |
| mako                       | 10.4 ms                                                      | 17.3 ms: 1.67x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 49.5 ms: 2.83x slower                                                       |
| telco                      | 8.79 ms                                                      | 172 ms: 19.60x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                |

Benchmark hidden because not significant (3): pylint, scimark_fft, logging_silent
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250926-3.15.0a0-48d0d0d-NOGIL/bm-20250926-pythonperf2-x86_64-python-48d0d0dd9733eae4935f-3.15.0a0-48d0d0d.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.049x slower

# HPT report

- Reliability score: 91.35% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.32x