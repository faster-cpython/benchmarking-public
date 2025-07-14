# Results vs. 3.13.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: linux-x86_64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.053x slower
- HPT reliability: 97.10%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 320 ms: 1.09x slower                                                        |
| docutils       | 2.83 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| html5lib       | 73.5 ms                                                      | 71.3 ms: 1.03x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.15 sec: 1.02x slower                                                      |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 831 ms                                                       | 538 ms: 1.55x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 302 ms: 1.54x faster                                                        |
| async_tree_io              | 843 ms                                                       | 569 ms: 1.48x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 237 ms: 1.46x faster                                                        |
| async_tree_none            | 376 ms                                                       | 269 ms: 1.40x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 330 ms: 1.37x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 473 ms: 1.23x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 504 ms: 1.20x faster                                                        |
| async_generators           | 457 ms                                                       | 465 ms: 1.02x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.27x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 71.6 ms: 1.14x faster                                                       |
| pidigits       | 252 ms                                                       | 249 ms: 1.01x faster                                                        |
| nbody          | 89.3 ms                                                      | 130 ms: 1.45x slower                                                        |
| Geometric mean | (ref)                                                        | 1.08x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 22.7 ms: 1.15x faster                                                       |
| regex_dna      | 247 ms                                                       | 223 ms: 1.11x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.40 ms: 1.08x faster                                                       |
| regex_compile  | 143 ms                                                       | 154 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 88.4 ms: 1.16x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 138 ms: 1.09x faster                                                        |
| tomli_loads          | 2.46 sec                                                     | 2.31 sec: 1.07x faster                                                      |
| json_dumps           | 11.1 ms                                                      | 12.1 ms: 1.09x slower                                                       |
| unpickle_pure_python | 217 us                                                       | 237 us: 1.09x slower                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 97.7 ms: 1.13x slower                                                       |
| pickle_pure_python   | 323 us                                                       | 369 us: 1.14x slower                                                        |
| json_loads           | 24.7 us                                                      | 28.2 us: 1.14x slower                                                       |
| xml_etree_process    | 61.2 ms                                                      | 70.2 ms: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.05x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 19.7 ms: 1.24x slower                                                       |
| python_startup_no_site | 8.96 ms                                                      | 11.8 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.28x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 30.4 ms: 1.16x slower                                                       |
| genshi_xml      | 57.1 ms                                                      | 66.8 ms: 1.17x slower                                                       |
| django_template | 36.4 ms                                                      | 44.3 ms: 1.22x slower                                                       |
| mako            | 10.4 ms                                                      | 17.5 ms: 1.69x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.29x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| gc_traversal               | 4.74 ms                                                      | 2.24 ms: 2.12x faster                                                       |
| mdp                        | 2.54 sec                                                     | 1.46 sec: 1.74x faster                                                      |
| async_tree_io_tg           | 831 ms                                                       | 538 ms: 1.55x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 302 ms: 1.54x faster                                                        |
| async_tree_io              | 843 ms                                                       | 569 ms: 1.48x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 237 ms: 1.46x faster                                                        |
| async_tree_none            | 376 ms                                                       | 269 ms: 1.40x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 330 ms: 1.37x faster                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 1.97 ms: 1.36x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 473 ms: 1.23x faster                                                        |
| deepcopy                   | 392 us                                                       | 325 us: 1.21x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 504 ms: 1.20x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 88.4 ms: 1.16x faster                                                       |
| go                         | 162 ms                                                       | 140 ms: 1.16x faster                                                        |
| regex_v8                   | 26.1 ms                                                      | 22.7 ms: 1.15x faster                                                       |
| float                      | 81.3 ms                                                      | 71.6 ms: 1.14x faster                                                       |
| deepcopy_memo              | 38.6 us                                                      | 34.5 us: 1.12x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.60 us: 1.12x faster                                                       |
| regex_dna                  | 247 ms                                                       | 223 ms: 1.11x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 61.6 ms: 1.11x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 138 ms: 1.09x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.40 ms: 1.08x faster                                                       |
| tomli_loads                | 2.46 sec                                                     | 2.31 sec: 1.07x faster                                                      |
| generators                 | 33.6 ms                                                      | 31.5 ms: 1.07x faster                                                       |
| pyflate                    | 503 ms                                                       | 475 ms: 1.06x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 71.3 ms: 1.03x faster                                                       |
| scimark_sor                | 123 ms                                                       | 120 ms: 1.03x faster                                                        |
| json                       | 5.69 ms                                                      | 5.56 ms: 1.02x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 17.2 ms: 1.02x faster                                                       |
| pidigits                   | 252 ms                                                       | 249 ms: 1.01x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 5.08 sec: 1.00x faster                                                      |
| logging_silent             | 97.9 ns                                                      | 99.5 ns: 1.02x slower                                                       |
| hexiom                     | 6.55 ms                                                      | 6.66 ms: 1.02x slower                                                       |
| async_generators           | 457 ms                                                       | 465 ms: 1.02x slower                                                        |
| sphinx                     | 1.12 sec                                                     | 1.15 sec: 1.02x slower                                                      |
| pycparser                  | 1.24 sec                                                     | 1.27 sec: 1.02x slower                                                      |
| docutils                   | 2.83 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| pprint_safe_repr           | 843 ms                                                       | 882 ms: 1.05x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                       |
| pprint_pformat             | 1.72 sec                                                     | 1.82 sec: 1.06x slower                                                      |
| spectral_norm              | 97.0 ms                                                      | 103 ms: 1.07x slower                                                        |
| comprehensions             | 17.0 us                                                      | 18.2 us: 1.07x slower                                                       |
| richards                   | 52.9 ms                                                      | 56.6 ms: 1.07x slower                                                       |
| k_core                     | 2.17 sec                                                     | 2.33 sec: 1.07x slower                                                      |
| sympy_integrate            | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                       |
| logging_simple             | 6.39 us                                                      | 6.89 us: 1.08x slower                                                       |
| regex_compile              | 143 ms                                                       | 154 ms: 1.08x slower                                                        |
| richards_super             | 59.6 ms                                                      | 64.6 ms: 1.08x slower                                                       |
| json_dumps                 | 11.1 ms                                                      | 12.1 ms: 1.09x slower                                                       |
| deltablue                  | 3.42 ms                                                      | 3.72 ms: 1.09x slower                                                       |
| unpickle_pure_python       | 217 us                                                       | 237 us: 1.09x slower                                                        |
| 2to3                       | 293 ms                                                       | 320 ms: 1.09x slower                                                        |
| thrift                     | 901 us                                                       | 984 us: 1.09x slower                                                        |
| scimark_fft                | 328 ms                                                       | 358 ms: 1.09x slower                                                        |
| sympy_expand               | 509 ms                                                       | 561 ms: 1.10x slower                                                        |
| sympy_str                  | 298 ms                                                       | 329 ms: 1.10x slower                                                        |
| chaos                      | 60.2 ms                                                      | 66.7 ms: 1.11x slower                                                       |
| logging_format             | 6.94 us                                                      | 7.70 us: 1.11x slower                                                       |
| sympy_sum                  | 155 ms                                                       | 172 ms: 1.11x slower                                                        |
| shortest_path              | 460 ms                                                       | 516 ms: 1.12x slower                                                        |
| meteor_contest             | 130 ms                                                       | 145 ms: 1.12x slower                                                        |
| connected_components       | 432 ms                                                       | 486 ms: 1.12x slower                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 97.7 ms: 1.13x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 369 us: 1.14x slower                                                        |
| json_loads                 | 24.7 us                                                      | 28.2 us: 1.14x slower                                                       |
| xml_etree_process          | 61.2 ms                                                      | 70.2 ms: 1.15x slower                                                       |
| genshi_text                | 26.2 ms                                                      | 30.4 ms: 1.16x slower                                                       |
| genshi_xml                 | 57.1 ms                                                      | 66.8 ms: 1.17x slower                                                       |
| raytrace                   | 273 ms                                                       | 323 ms: 1.18x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 108 ms: 1.19x slower                                                        |
| many_optionals             | 930 us                                                       | 1.11 ms: 1.20x slower                                                       |
| scimark_lu                 | 98.7 ms                                                      | 118 ms: 1.20x slower                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 79.3 ms: 1.20x slower                                                       |
| django_template            | 36.4 ms                                                      | 44.3 ms: 1.22x slower                                                       |
| typing_runtime_protocols   | 169 us                                                       | 207 us: 1.23x slower                                                        |
| python_startup             | 15.9 ms                                                      | 19.7 ms: 1.24x slower                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.91 ms: 1.24x slower                                                       |
| fannkuch                   | 363 ms                                                       | 450 ms: 1.24x slower                                                        |
| crypto_pyaes               | 73.3 ms                                                      | 93.7 ms: 1.28x slower                                                       |
| python_startup_no_site     | 8.96 ms                                                      | 11.8 ms: 1.32x slower                                                       |
| nbody                      | 89.3 ms                                                      | 130 ms: 1.45x slower                                                        |
| coverage                   | 80.0 ms                                                      | 117 ms: 1.46x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 1.41 ms: 1.50x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 27.5 ms: 1.58x slower                                                       |
| mako                       | 10.4 ms                                                      | 17.5 ms: 1.69x slower                                                       |
| bench_mp_pool              | 5.12 ms                                                      | 56.9 ms: 11.11x slower                                                      |
| telco                      | 8.79 ms                                                      | 175 ms: 19.88x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                                |

Benchmark hidden because not significant (3): deepcopy_reduce, asyncio_websockets, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.053x slower

# HPT report

- Reliability score: 97.10% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.31x