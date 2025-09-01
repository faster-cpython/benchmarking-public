# Results vs. 3.13.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: linux-x86_64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.048x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 285 ms: 1.03x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| html5lib       | 73.5 ms                                                      | 66.4 ms: 1.11x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                        |
| async_tree_none            | 376 ms                                                       | 270 ms: 1.39x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 325 ms: 1.39x faster                                                        |
| async_tree_io              | 843 ms                                                       | 611 ms: 1.38x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 622 ms: 1.34x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 268 ms: 1.29x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 498 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 504 ms: 1.15x faster                                                        |
| async_generators           | 457 ms                                                       | 437 ms: 1.04x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 381 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.22x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 63.1 ms: 1.29x faster                                                       |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                        |
| nbody          | 89.3 ms                                                      | 104 ms: 1.16x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                       | 224 ms: 1.10x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 23.9 ms: 1.09x faster                                                       |
| regex_compile  | 143 ms                                                       | 132 ms: 1.08x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.53 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 1.90 sec: 1.30x faster                                                      |
| xml_etree_process    | 61.2 ms                                                      | 54.9 ms: 1.11x faster                                                       |
| unpickle_pure_python | 217 us                                                       | 195 us: 1.11x faster                                                        |
| json_dumps           | 11.1 ms                                                      | 10.1 ms: 1.11x faster                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 79.6 ms: 1.09x faster                                                       |
| xml_etree_parse      | 150 ms                                                       | 140 ms: 1.07x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 98.3 ms: 1.05x faster                                                       |
| pickle_pure_python   | 323 us                                                       | 326 us: 1.01x slower                                                        |
| json_loads           | 24.7 us                                                      | 25.1 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.83 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 22.9 ms: 1.15x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 53.8 ms: 1.06x faster                                                       |
| mako            | 10.4 ms                                                      | 9.89 ms: 1.05x faster                                                       |
| django_template | 36.4 ms                                                      | 35.1 ms: 1.04x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.29 sec: 1.97x faster                                                      |
| richards                   | 52.9 ms                                                      | 34.0 ms: 1.56x faster                                                       |
| richards_super             | 59.6 ms                                                      | 38.5 ms: 1.55x faster                                                       |
| deepcopy                   | 392 us                                                       | 276 us: 1.42x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 331 ms: 1.41x faster                                                        |
| async_tree_none            | 376 ms                                                       | 270 ms: 1.39x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 325 ms: 1.39x faster                                                        |
| async_tree_io              | 843 ms                                                       | 611 ms: 1.38x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 28.5 us: 1.36x faster                                                       |
| async_tree_io_tg           | 831 ms                                                       | 622 ms: 1.34x faster                                                        |
| go                         | 162 ms                                                       | 125 ms: 1.30x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 1.90 sec: 1.30x faster                                                      |
| async_tree_none_tg         | 346 ms                                                       | 268 ms: 1.29x faster                                                        |
| float                      | 81.3 ms                                                      | 63.1 ms: 1.29x faster                                                       |
| pyflate                    | 503 ms                                                       | 402 ms: 1.25x faster                                                        |
| spectral_norm              | 97.0 ms                                                      | 77.6 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 498 ms: 1.21x faster                                                        |
| deltablue                  | 3.42 ms                                                      | 2.84 ms: 1.20x faster                                                       |
| scimark_sor                | 123 ms                                                       | 102 ms: 1.20x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.02 us: 1.17x faster                                                       |
| generators                 | 33.6 ms                                                      | 28.8 ms: 1.17x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 58.9 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 504 ms: 1.15x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.50 sec: 1.15x faster                                                      |
| genshi_text                | 26.2 ms                                                      | 22.9 ms: 1.15x faster                                                       |
| pprint_safe_repr           | 843 ms                                                       | 741 ms: 1.14x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.56 sec: 1.12x faster                                                      |
| xml_etree_process          | 61.2 ms                                                      | 54.9 ms: 1.11x faster                                                       |
| unpickle_pure_python       | 217 us                                                       | 195 us: 1.11x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 66.4 ms: 1.11x faster                                                       |
| json_dumps                 | 11.1 ms                                                      | 10.1 ms: 1.11x faster                                                       |
| regex_dna                  | 247 ms                                                       | 224 ms: 1.10x faster                                                        |
| scimark_fft                | 328 ms                                                       | 298 ms: 1.10x faster                                                        |
| thrift                     | 901 us                                                       | 822 us: 1.10x faster                                                        |
| regex_v8                   | 26.1 ms                                                      | 23.9 ms: 1.09x faster                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 79.6 ms: 1.09x faster                                                       |
| regex_compile              | 143 ms                                                       | 132 ms: 1.08x faster                                                        |
| hexiom                     | 6.55 ms                                                      | 6.09 ms: 1.08x faster                                                       |
| k_core                     | 2.17 sec                                                     | 2.02 sec: 1.08x faster                                                      |
| xml_etree_parse            | 150 ms                                                       | 140 ms: 1.07x faster                                                        |
| logging_simple             | 6.39 us                                                      | 5.96 us: 1.07x faster                                                       |
| pylint                     | 347 ms                                                       | 325 ms: 1.07x faster                                                        |
| logging_format             | 6.94 us                                                      | 6.52 us: 1.06x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 92.2 ns: 1.06x faster                                                       |
| genshi_xml                 | 57.1 ms                                                      | 53.8 ms: 1.06x faster                                                       |
| sympy_integrate            | 23.6 ms                                                      | 22.2 ms: 1.06x faster                                                       |
| meteor_contest             | 130 ms                                                       | 122 ms: 1.06x faster                                                        |
| connected_components       | 432 ms                                                       | 410 ms: 1.05x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 93.7 ms: 1.05x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 16.7 ms: 1.05x faster                                                       |
| mako                       | 10.4 ms                                                      | 9.89 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 98.3 ms: 1.05x faster                                                       |
| async_generators           | 457 ms                                                       | 437 ms: 1.04x faster                                                        |
| json                       | 5.69 ms                                                      | 5.46 ms: 1.04x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.53 ms: 1.04x faster                                                       |
| pycparser                  | 1.24 sec                                                     | 1.20 sec: 1.04x faster                                                      |
| python_startup             | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| django_template            | 36.4 ms                                                      | 35.1 ms: 1.04x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.81 us: 1.04x faster                                                       |
| sympy_str                  | 298 ms                                                       | 289 ms: 1.03x faster                                                        |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| sympy_sum                  | 155 ms                                                       | 150 ms: 1.03x faster                                                        |
| shortest_path              | 460 ms                                                       | 447 ms: 1.03x faster                                                        |
| sympy_expand               | 509 ms                                                       | 495 ms: 1.03x faster                                                        |
| 2to3                       | 293 ms                                                       | 285 ms: 1.03x faster                                                        |
| chaos                      | 60.2 ms                                                      | 58.7 ms: 1.02x faster                                                       |
| asyncio_websockets         | 388 ms                                                       | 381 ms: 1.02x faster                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 8.83 ms: 1.01x faster                                                       |
| pickle_pure_python         | 323 us                                                       | 326 us: 1.01x slower                                                        |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                        |
| nqueens                    | 90.7 ms                                                      | 91.9 ms: 1.01x slower                                                       |
| coverage                   | 80.0 ms                                                      | 81.3 ms: 1.02x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.1 us: 1.02x slower                                                       |
| bench_thread_pool          | 942 us                                                       | 962 us: 1.02x slower                                                        |
| comprehensions             | 17.0 us                                                      | 17.4 us: 1.02x slower                                                       |
| docutils                   | 2.83 sec                                                     | 2.90 sec: 1.03x slower                                                      |
| fannkuch                   | 363 ms                                                       | 379 ms: 1.04x slower                                                        |
| raytrace                   | 273 ms                                                       | 285 ms: 1.04x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 76.8 ms: 1.05x slower                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 5.04 ms: 1.05x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.84 ms: 1.06x slower                                                       |
| nbody                      | 89.3 ms                                                      | 104 ms: 1.16x slower                                                        |
| many_optionals             | 930 us                                                       | 1.22 ms: 1.31x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 6.46 ms: 1.36x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 43.0 ms: 2.46x slower                                                       |
| telco                      | 8.79 ms                                                      | 159 ms: 18.13x slower                                                       |
| bench_mp_pool              | 5.12 ms                                                      | 1.28 sec: 249.43x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (3): djangocms, typing_runtime_protocols, scimark_monte_carlo
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-pythonperf2-x86_64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.12x