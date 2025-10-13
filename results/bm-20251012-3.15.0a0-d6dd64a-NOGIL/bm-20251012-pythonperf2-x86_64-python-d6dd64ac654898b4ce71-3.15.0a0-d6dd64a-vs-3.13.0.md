# Results vs. 3.13.0

- fork: python
- ref: d6dd64ac654898b4ce71
- machine: linux-x86_64
- commit hash: d6dd64a
- commit date: 2025-10-12
- overall geometric mean: 1.042x slower
- HPT reliability: 83.69%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 312 ms: 1.07x slower                                                        |
| docutils       | 2.83 sec                                                     | 2.85 sec: 1.01x slower                                                      |
| html5lib       | 73.5 ms                                                      | 70.5 ms: 1.04x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.15 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 290 ms: 1.61x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 524 ms: 1.59x faster                                                        |
| async_tree_io              | 843 ms                                                       | 552 ms: 1.53x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 229 ms: 1.51x faster                                                        |
| async_tree_none            | 376 ms                                                       | 259 ms: 1.45x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 316 ms: 1.43x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 462 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 491 ms: 1.23x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 376 ms: 1.03x faster                                                        |
| async_generators           | 457 ms                                                       | 470 ms: 1.03x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.8 ms: 1.06x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 71.0 ms: 1.15x faster                                                       |
| pidigits       | 252 ms                                                       | 251 ms: 1.01x faster                                                        |
| nbody          | 89.3 ms                                                      | 125 ms: 1.40x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.3 ms: 1.12x faster                                                       |
| regex_dna      | 247 ms                                                       | 226 ms: 1.09x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.52 ms: 1.04x faster                                                       |
| regex_compile  | 143 ms                                                       | 154 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 88.5 ms: 1.16x faster                                                       |
| tomli_loads          | 2.46 sec                                                     | 2.15 sec: 1.14x faster                                                      |
| xml_etree_parse      | 150 ms                                                       | 137 ms: 1.09x faster                                                        |
| json_dumps           | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                                       |
| unpickle_pure_python | 217 us                                                       | 239 us: 1.10x slower                                                        |
| pickle_pure_python   | 323 us                                                       | 358 us: 1.11x slower                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 97.6 ms: 1.13x slower                                                       |
| json_loads           | 24.7 us                                                      | 28.0 us: 1.13x slower                                                       |
| xml_etree_process    | 61.2 ms                                                      | 69.5 ms: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 19.1 ms: 1.20x slower                                                       |
| python_startup_no_site | 8.96 ms                                                      | 11.7 ms: 1.31x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.25x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.1 ms                                                      | 65.7 ms: 1.15x slower                                                       |
| genshi_text     | 26.2 ms                                                      | 30.3 ms: 1.16x slower                                                       |
| django_template | 36.4 ms                                                      | 42.7 ms: 1.18x slower                                                       |
| mako            | 10.4 ms                                                      | 17.3 ms: 1.67x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.27x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                      | 2.21 ms: 2.14x faster                                                       |
| mdp                        | 2.54 sec                                                     | 1.44 sec: 1.76x faster                                                      |
| async_tree_memoization_tg  | 466 ms                                                       | 290 ms: 1.61x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 524 ms: 1.59x faster                                                        |
| async_tree_io              | 843 ms                                                       | 552 ms: 1.53x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 229 ms: 1.51x faster                                                        |
| async_tree_none            | 376 ms                                                       | 259 ms: 1.45x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 316 ms: 1.43x faster                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.00 ms: 1.34x faster                                                       |
| deepcopy                   | 392 us                                                       | 297 us: 1.32x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 30.0 us: 1.29x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 462 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 491 ms: 1.23x faster                                                        |
| go                         | 162 ms                                                       | 137 ms: 1.18x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 88.5 ms: 1.16x faster                                                       |
| float                      | 81.3 ms                                                      | 71.0 ms: 1.15x faster                                                       |
| tomli_loads                | 2.46 sec                                                     | 2.15 sec: 1.14x faster                                                      |
| pathlib                    | 17.5 ms                                                      | 15.5 ms: 1.13x faster                                                       |
| regex_v8                   | 26.1 ms                                                      | 23.3 ms: 1.12x faster                                                       |
| scimark_sor                | 123 ms                                                       | 110 ms: 1.12x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.63 us: 1.10x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 61.9 ms: 1.10x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 137 ms: 1.09x faster                                                        |
| regex_dna                  | 247 ms                                                       | 226 ms: 1.09x faster                                                        |
| generators                 | 33.6 ms                                                      | 31.0 ms: 1.09x faster                                                       |
| pyflate                    | 503 ms                                                       | 467 ms: 1.08x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.32 us: 1.07x faster                                                       |
| html5lib                   | 73.5 ms                                                      | 70.5 ms: 1.04x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.52 ms: 1.04x faster                                                       |
| scimark_fft                | 328 ms                                                       | 317 ms: 1.03x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 376 ms: 1.03x faster                                                        |
| json                       | 5.69 ms                                                      | 5.51 ms: 1.03x faster                                                       |
| pycparser                  | 1.24 sec                                                     | 1.21 sec: 1.02x faster                                                      |
| hexiom                     | 6.55 ms                                                      | 6.41 ms: 1.02x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 96.1 ns: 1.02x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 5.05 sec: 1.01x faster                                                      |
| pidigits                   | 252 ms                                                       | 251 ms: 1.01x faster                                                        |
| docutils                   | 2.83 sec                                                     | 2.85 sec: 1.01x slower                                                      |
| pprint_safe_repr           | 843 ms                                                       | 858 ms: 1.02x slower                                                        |
| sphinx                     | 1.12 sec                                                     | 1.15 sec: 1.02x slower                                                      |
| spectral_norm              | 97.0 ms                                                      | 99.6 ms: 1.03x slower                                                       |
| async_generators           | 457 ms                                                       | 470 ms: 1.03x slower                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.78 sec: 1.03x slower                                                      |
| json_dumps                 | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                                       |
| deltablue                  | 3.42 ms                                                      | 3.56 ms: 1.04x slower                                                       |
| comprehensions             | 17.0 us                                                      | 17.8 us: 1.04x slower                                                       |
| richards                   | 52.9 ms                                                      | 55.3 ms: 1.04x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 22.8 ms: 1.06x slower                                                       |
| sympy_integrate            | 23.6 ms                                                      | 25.0 ms: 1.06x slower                                                       |
| 2to3                       | 293 ms                                                       | 312 ms: 1.07x slower                                                        |
| logging_simple             | 6.39 us                                                      | 6.81 us: 1.07x slower                                                       |
| richards_super             | 59.6 ms                                                      | 63.9 ms: 1.07x slower                                                       |
| k_core                     | 2.17 sec                                                     | 2.34 sec: 1.08x slower                                                      |
| regex_compile              | 143 ms                                                       | 154 ms: 1.08x slower                                                        |
| sympy_expand               | 509 ms                                                       | 553 ms: 1.08x slower                                                        |
| sympy_str                  | 298 ms                                                       | 325 ms: 1.09x slower                                                        |
| thrift                     | 901 us                                                       | 981 us: 1.09x slower                                                        |
| chaos                      | 60.2 ms                                                      | 65.8 ms: 1.09x slower                                                       |
| logging_format             | 6.94 us                                                      | 7.62 us: 1.10x slower                                                       |
| unpickle_pure_python       | 217 us                                                       | 239 us: 1.10x slower                                                        |
| sympy_sum                  | 155 ms                                                       | 171 ms: 1.10x slower                                                        |
| pickle_pure_python         | 323 us                                                       | 358 us: 1.11x slower                                                        |
| meteor_contest             | 130 ms                                                       | 144 ms: 1.11x slower                                                        |
| connected_components       | 432 ms                                                       | 481 ms: 1.11x slower                                                        |
| shortest_path              | 460 ms                                                       | 512 ms: 1.11x slower                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 97.6 ms: 1.13x slower                                                       |
| json_loads                 | 24.7 us                                                      | 28.0 us: 1.13x slower                                                       |
| xml_etree_process          | 61.2 ms                                                      | 69.5 ms: 1.14x slower                                                       |
| genshi_xml                 | 57.1 ms                                                      | 65.7 ms: 1.15x slower                                                       |
| scimark_lu                 | 98.7 ms                                                      | 114 ms: 1.15x slower                                                        |
| genshi_text                | 26.2 ms                                                      | 30.3 ms: 1.16x slower                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 77.4 ms: 1.17x slower                                                       |
| django_template            | 36.4 ms                                                      | 42.7 ms: 1.18x slower                                                       |
| nqueens                    | 90.7 ms                                                      | 107 ms: 1.18x slower                                                        |
| raytrace                   | 273 ms                                                       | 321 ms: 1.18x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.63 ms: 1.18x slower                                                       |
| python_startup             | 15.9 ms                                                      | 19.1 ms: 1.20x slower                                                       |
| typing_runtime_protocols   | 169 us                                                       | 207 us: 1.22x slower                                                        |
| bench_mp_pool              | 5.12 ms                                                      | 6.32 ms: 1.23x slower                                                       |
| fannkuch                   | 363 ms                                                       | 450 ms: 1.24x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 93.5 ms: 1.28x slower                                                       |
| python_startup_no_site     | 8.96 ms                                                      | 11.7 ms: 1.31x slower                                                       |
| nbody                      | 89.3 ms                                                      | 125 ms: 1.40x slower                                                        |
| many_optionals             | 930 us                                                       | 1.30 ms: 1.40x slower                                                       |
| bench_thread_pool          | 942 us                                                       | 1.36 ms: 1.45x slower                                                       |
| coverage                   | 80.0 ms                                                      | 120 ms: 1.50x slower                                                        |
| mako                       | 10.4 ms                                                      | 17.3 ms: 1.67x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 50.4 ms: 2.88x slower                                                       |
| telco                      | 8.79 ms                                                      | 167 ms: 19.01x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (1): pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251012-3.15.0a0-d6dd64a-NOGIL/bm-20251012-pythonperf2-x86_64-python-d6dd64ac654898b4ce71-3.15.0a0-d6dd64a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.042x slower

# HPT report

- Reliability score: 83.69% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.32x