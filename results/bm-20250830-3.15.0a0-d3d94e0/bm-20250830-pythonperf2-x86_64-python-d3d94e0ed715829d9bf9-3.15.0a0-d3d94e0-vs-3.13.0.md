# Results vs. 3.13.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: linux-x86_64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.042x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 281 ms: 1.04x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.87 sec: 1.02x slower                                                      |
| html5lib       | 73.5 ms                                                      | 67.3 ms: 1.09x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.08 sec: 1.04x faster                                                      |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 330 ms: 1.41x faster                                                        |
| async_tree_none            | 376 ms                                                       | 268 ms: 1.40x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 325 ms: 1.39x faster                                                        |
| async_tree_io              | 843 ms                                                       | 614 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 626 ms: 1.33x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 269 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 498 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 507 ms: 1.15x faster                                                        |
| async_generators           | 457 ms                                                       | 421 ms: 1.08x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.0 ms: 1.02x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.23x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 68.5 ms: 1.19x faster                                                       |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                        |
| nbody          | 89.3 ms                                                      | 93.2 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.4 ms: 1.12x faster                                                       |
| regex_dna      | 247 ms                                                       | 226 ms: 1.09x faster                                                        |
| regex_compile  | 143 ms                                                       | 132 ms: 1.08x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.56 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.99 sec: 1.24x faster                                                      |
| xml_etree_parse      | 150 ms                                                       | 137 ms: 1.10x faster                                                        |
| json_dumps           | 11.1 ms                                                      | 10.2 ms: 1.09x faster                                                       |
| xml_etree_process    | 61.2 ms                                                      | 57.5 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 96.8 ms: 1.06x faster                                                       |
| unpickle_pure_python | 217 us                                                       | 206 us: 1.06x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 82.5 ms: 1.05x faster                                                       |
| pickle_pure_python   | 323 us                                                       | 325 us: 1.01x slower                                                        |
| json_loads           | 24.7 us                                                      | 25.2 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.80 ms: 1.02x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 22.7 ms: 1.16x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 52.9 ms: 1.08x faster                                                       |
| django_template | 36.4 ms                                                      | 34.7 ms: 1.05x faster                                                       |
| mako            | 10.4 ms                                                      | 10.7 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.27 sec: 1.99x faster                                                      |
| deepcopy                   | 392 us                                                       | 276 us: 1.42x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 330 ms: 1.41x faster                                                        |
| async_tree_none            | 376 ms                                                       | 268 ms: 1.40x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 27.7 us: 1.40x faster                                                       |
| async_tree_memoization     | 453 ms                                                       | 325 ms: 1.39x faster                                                        |
| go                         | 162 ms                                                       | 117 ms: 1.39x faster                                                        |
| async_tree_io              | 843 ms                                                       | 614 ms: 1.37x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 626 ms: 1.33x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 269 ms: 1.29x faster                                                        |
| pyflate                    | 503 ms                                                       | 406 ms: 1.24x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 1.99 sec: 1.24x faster                                                      |
| scimark_sor                | 123 ms                                                       | 101 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 498 ms: 1.21x faster                                                        |
| richards                   | 52.9 ms                                                      | 44.1 ms: 1.20x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.98 us: 1.19x faster                                                       |
| float                      | 81.3 ms                                                      | 68.5 ms: 1.19x faster                                                       |
| richards_super             | 59.6 ms                                                      | 50.6 ms: 1.18x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 58.5 ms: 1.17x faster                                                       |
| genshi_text                | 26.2 ms                                                      | 22.7 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 507 ms: 1.15x faster                                                        |
| generators                 | 33.6 ms                                                      | 29.9 ms: 1.13x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 5.84 ms: 1.12x faster                                                       |
| regex_v8                   | 26.1 ms                                                      | 23.4 ms: 1.12x faster                                                       |
| spectral_norm              | 97.0 ms                                                      | 87.4 ms: 1.11x faster                                                       |
| scimark_monte_carlo        | 66.1 ms                                                      | 59.6 ms: 1.11x faster                                                       |
| thrift                     | 901 us                                                       | 820 us: 1.10x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.57 sec: 1.10x faster                                                      |
| xml_etree_parse            | 150 ms                                                       | 137 ms: 1.10x faster                                                        |
| logging_simple             | 6.39 us                                                      | 5.84 us: 1.10x faster                                                       |
| regex_dna                  | 247 ms                                                       | 226 ms: 1.09x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.36 us: 1.09x faster                                                       |
| html5lib                   | 73.5 ms                                                      | 67.3 ms: 1.09x faster                                                       |
| pylint                     | 347 ms                                                       | 318 ms: 1.09x faster                                                        |
| json_dumps                 | 11.1 ms                                                      | 10.2 ms: 1.09x faster                                                       |
| pprint_safe_repr           | 843 ms                                                       | 773 ms: 1.09x faster                                                        |
| async_generators           | 457 ms                                                       | 421 ms: 1.08x faster                                                        |
| regex_compile              | 143 ms                                                       | 132 ms: 1.08x faster                                                        |
| sympy_integrate            | 23.6 ms                                                      | 21.8 ms: 1.08x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.71 sec: 1.08x faster                                                      |
| deltablue                  | 3.42 ms                                                      | 3.16 ms: 1.08x faster                                                       |
| genshi_xml                 | 57.1 ms                                                      | 52.9 ms: 1.08x faster                                                       |
| meteor_contest             | 130 ms                                                       | 121 ms: 1.07x faster                                                        |
| scimark_fft                | 328 ms                                                       | 305 ms: 1.07x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 57.5 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 96.8 ms: 1.06x faster                                                       |
| json                       | 5.69 ms                                                      | 5.36 ms: 1.06x faster                                                       |
| comprehensions             | 17.0 us                                                      | 16.1 us: 1.06x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 16.6 ms: 1.06x faster                                                       |
| unpickle_pure_python       | 217 us                                                       | 206 us: 1.06x faster                                                        |
| logging_silent             | 97.9 ns                                                      | 92.8 ns: 1.05x faster                                                       |
| scimark_lu                 | 98.7 ms                                                      | 93.7 ms: 1.05x faster                                                       |
| sympy_str                  | 298 ms                                                       | 283 ms: 1.05x faster                                                        |
| django_template            | 36.4 ms                                                      | 34.7 ms: 1.05x faster                                                       |
| sympy_expand               | 509 ms                                                       | 486 ms: 1.05x faster                                                        |
| xml_etree_generate         | 86.5 ms                                                      | 82.5 ms: 1.05x faster                                                       |
| python_startup             | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| 2to3                       | 293 ms                                                       | 281 ms: 1.04x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.09 sec: 1.04x faster                                                      |
| chaos                      | 60.2 ms                                                      | 58.1 ms: 1.04x faster                                                       |
| sphinx                     | 1.12 sec                                                     | 1.08 sec: 1.04x faster                                                      |
| sympy_sum                  | 155 ms                                                       | 150 ms: 1.03x faster                                                        |
| regex_effbot               | 3.67 ms                                                      | 3.56 ms: 1.03x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.84 us: 1.02x faster                                                       |
| connected_components       | 432 ms                                                       | 423 ms: 1.02x faster                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 8.80 ms: 1.02x faster                                                       |
| shortest_path              | 460 ms                                                       | 454 ms: 1.01x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 385 ms: 1.01x faster                                                        |
| fannkuch                   | 363 ms                                                       | 361 ms: 1.01x faster                                                        |
| pickle_pure_python         | 323 us                                                       | 325 us: 1.01x slower                                                        |
| pycparser                  | 1.24 sec                                                     | 1.26 sec: 1.01x slower                                                      |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                        |
| raytrace                   | 273 ms                                                       | 276 ms: 1.01x slower                                                        |
| docutils                   | 2.83 sec                                                     | 2.87 sec: 1.02x slower                                                      |
| nqueens                    | 90.7 ms                                                      | 92.1 ms: 1.02x slower                                                       |
| bench_thread_pool          | 942 us                                                       | 959 us: 1.02x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.0 ms: 1.02x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.2 us: 1.02x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 74.8 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.92 ms: 1.03x slower                                                       |
| coverage                   | 80.0 ms                                                      | 82.7 ms: 1.03x slower                                                       |
| mako                       | 10.4 ms                                                      | 10.7 ms: 1.04x slower                                                       |
| nbody                      | 89.3 ms                                                      | 93.2 ms: 1.04x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.93 ms: 1.09x slower                                                       |
| many_optionals             | 930 us                                                       | 1.21 ms: 1.30x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 6.43 ms: 1.36x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 42.4 ms: 2.43x slower                                                       |
| telco                      | 8.79 ms                                                      | 157 ms: 17.91x slower                                                       |
| bench_mp_pool              | 5.12 ms                                                      | 1.50 sec: 292.37x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (2): djangocms, typing_runtime_protocols
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.10x