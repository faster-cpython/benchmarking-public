# Results vs. 3.13.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: linux-x86_64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.043x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 287 ms: 1.02x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                      |
| html5lib       | 73.5 ms                                                      | 66.8 ms: 1.10x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 329 ms: 1.42x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 326 ms: 1.39x faster                                                        |
| async_tree_io              | 843 ms                                                       | 624 ms: 1.35x faster                                                        |
| async_tree_none            | 376 ms                                                       | 280 ms: 1.34x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 635 ms: 1.31x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 268 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 499 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 504 ms: 1.15x faster                                                        |
| async_generators           | 457 ms                                                       | 442 ms: 1.03x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.7 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 65.4 ms: 1.24x faster                                                       |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                        |
| nbody          | 89.3 ms                                                      | 101 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                       | 222 ms: 1.11x faster                                                        |
| regex_compile  | 143 ms                                                       | 133 ms: 1.07x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 24.4 ms: 1.07x faster                                                       |
| regex_effbot   | 3.67 ms                                                      | 3.84 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.91 sec: 1.29x faster                                                      |
| unpickle_pure_python | 217 us                                                       | 192 us: 1.13x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 55.1 ms: 1.11x faster                                                       |
| json_dumps           | 11.1 ms                                                      | 10.2 ms: 1.09x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 138 ms: 1.09x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 79.4 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 97.2 ms: 1.06x faster                                                       |
| json_loads           | 24.7 us                                                      | 25.3 us: 1.03x slower                                                       |
| pickle_pure_python   | 323 us                                                       | 332 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.83 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.2 ms: 1.13x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 54.1 ms: 1.05x faster                                                       |
| mako            | 10.4 ms                                                      | 9.86 ms: 1.05x faster                                                       |
| django_template | 36.4 ms                                                      | 34.9 ms: 1.04x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.29 sec: 1.97x faster                                                      |
| richards                   | 52.9 ms                                                      | 33.9 ms: 1.56x faster                                                       |
| richards_super             | 59.6 ms                                                      | 40.0 ms: 1.49x faster                                                       |
| async_tree_memoization_tg  | 466 ms                                                       | 329 ms: 1.42x faster                                                        |
| deepcopy                   | 392 us                                                       | 279 us: 1.41x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 27.5 us: 1.40x faster                                                       |
| async_tree_memoization     | 453 ms                                                       | 326 ms: 1.39x faster                                                        |
| async_tree_io              | 843 ms                                                       | 624 ms: 1.35x faster                                                        |
| async_tree_none            | 376 ms                                                       | 280 ms: 1.34x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 635 ms: 1.31x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 268 ms: 1.29x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 1.91 sec: 1.29x faster                                                      |
| go                         | 162 ms                                                       | 126 ms: 1.29x faster                                                        |
| float                      | 81.3 ms                                                      | 65.4 ms: 1.24x faster                                                       |
| pyflate                    | 503 ms                                                       | 405 ms: 1.24x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 78.6 ms: 1.23x faster                                                       |
| scimark_sor                | 123 ms                                                       | 102 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 499 ms: 1.21x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 2.84 ms: 1.20x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.99 us: 1.18x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 504 ms: 1.15x faster                                                        |
| pprint_safe_repr           | 843 ms                                                       | 733 ms: 1.15x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 59.5 ms: 1.15x faster                                                       |
| pprint_pformat             | 1.72 sec                                                     | 1.50 sec: 1.14x faster                                                      |
| unpickle_pure_python       | 217 us                                                       | 192 us: 1.13x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 23.2 ms: 1.13x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.51 sec: 1.13x faster                                                      |
| regex_dna                  | 247 ms                                                       | 222 ms: 1.11x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 55.1 ms: 1.11x faster                                                       |
| html5lib                   | 73.5 ms                                                      | 66.8 ms: 1.10x faster                                                       |
| json_dumps                 | 11.1 ms                                                      | 10.2 ms: 1.09x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 138 ms: 1.09x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 79.4 ms: 1.09x faster                                                       |
| logging_simple             | 6.39 us                                                      | 5.93 us: 1.08x faster                                                       |
| thrift                     | 901 us                                                       | 836 us: 1.08x faster                                                        |
| pylint                     | 347 ms                                                       | 322 ms: 1.08x faster                                                        |
| regex_compile              | 143 ms                                                       | 133 ms: 1.07x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.02 sec: 1.07x faster                                                      |
| scimark_fft                | 328 ms                                                       | 306 ms: 1.07x faster                                                        |
| meteor_contest             | 130 ms                                                       | 121 ms: 1.07x faster                                                        |
| regex_v8                   | 26.1 ms                                                      | 24.4 ms: 1.07x faster                                                       |
| logging_format             | 6.94 us                                                      | 6.49 us: 1.07x faster                                                       |
| generators                 | 33.6 ms                                                      | 31.5 ms: 1.07x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 91.8 ns: 1.07x faster                                                       |
| connected_components       | 432 ms                                                       | 407 ms: 1.06x faster                                                        |
| hexiom                     | 6.55 ms                                                      | 6.17 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 97.2 ms: 1.06x faster                                                       |
| genshi_xml                 | 57.1 ms                                                      | 54.1 ms: 1.05x faster                                                       |
| sympy_integrate            | 23.6 ms                                                      | 22.4 ms: 1.05x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 16.7 ms: 1.05x faster                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 62.8 ms: 1.05x faster                                                       |
| mako                       | 10.4 ms                                                      | 9.86 ms: 1.05x faster                                                       |
| json                       | 5.69 ms                                                      | 5.45 ms: 1.04x faster                                                       |
| django_template            | 36.4 ms                                                      | 34.9 ms: 1.04x faster                                                       |
| shortest_path              | 460 ms                                                       | 442 ms: 1.04x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 95.1 ms: 1.04x faster                                                       |
| python_startup             | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| async_generators           | 457 ms                                                       | 442 ms: 1.03x faster                                                        |
| sqlite_synth               | 2.91 us                                                      | 2.83 us: 1.03x faster                                                       |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.02x faster                                                        |
| sympy_str                  | 298 ms                                                       | 292 ms: 1.02x faster                                                        |
| 2to3                       | 293 ms                                                       | 287 ms: 1.02x faster                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 8.83 ms: 1.01x faster                                                       |
| chaos                      | 60.2 ms                                                      | 59.4 ms: 1.01x faster                                                       |
| sympy_expand               | 509 ms                                                       | 503 ms: 1.01x faster                                                        |
| pycparser                  | 1.24 sec                                                     | 1.23 sec: 1.01x faster                                                      |
| fannkuch                   | 363 ms                                                       | 364 ms: 1.00x slower                                                        |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                        |
| comprehensions             | 17.0 us                                                      | 17.4 us: 1.02x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.3 us: 1.03x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 332 us: 1.03x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.91 sec: 1.03x slower                                                      |
| nqueens                    | 90.7 ms                                                      | 93.5 ms: 1.03x slower                                                       |
| raytrace                   | 273 ms                                                       | 281 ms: 1.03x slower                                                        |
| coverage                   | 80.0 ms                                                      | 82.7 ms: 1.03x slower                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.99 ms: 1.04x slower                                                       |
| bench_thread_pool          | 942 us                                                       | 984 us: 1.04x slower                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.84 ms: 1.05x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 22.7 ms: 1.05x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 78.4 ms: 1.07x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.92 ms: 1.09x slower                                                       |
| nbody                      | 89.3 ms                                                      | 101 ms: 1.13x slower                                                        |
| many_optionals             | 930 us                                                       | 1.22 ms: 1.31x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 6.55 ms: 1.38x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 42.7 ms: 2.44x slower                                                       |
| telco                      | 8.79 ms                                                      | 160 ms: 18.15x slower                                                       |
| bench_mp_pool              | 5.12 ms                                                      | 1.61 sec: 313.96x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (3): asyncio_websockets, djangocms, typing_runtime_protocols
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.043x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.12x