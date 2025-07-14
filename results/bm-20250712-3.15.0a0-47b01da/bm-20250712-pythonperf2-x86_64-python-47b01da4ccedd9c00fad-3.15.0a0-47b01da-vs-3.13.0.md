# Results vs. 3.13.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: linux-x86_64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.039x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 281 ms: 1.04x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.86 sec: 1.01x slower                                                      |
| html5lib       | 73.5 ms                                                      | 65.5 ms: 1.12x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 333 ms: 1.40x faster                                                        |
| async_tree_none            | 376 ms                                                       | 273 ms: 1.38x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 332 ms: 1.36x faster                                                        |
| async_tree_io              | 843 ms                                                       | 630 ms: 1.34x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 638 ms: 1.30x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 272 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 505 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                        |
| async_generators           | 457 ms                                                       | 422 ms: 1.08x faster                                                        |
| asyncio_websockets         | 388 ms                                                       | 382 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 70.8 ms: 1.15x faster                                                       |
| pidigits       | 252 ms                                                       | 256 ms: 1.02x slower                                                        |
| nbody          | 89.3 ms                                                      | 93.0 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.1 ms                                                      | 23.3 ms: 1.12x faster                                                       |
| regex_dna      | 247 ms                                                       | 229 ms: 1.08x faster                                                        |
| regex_compile  | 143 ms                                                       | 133 ms: 1.07x faster                                                        |
| regex_effbot   | 3.67 ms                                                      | 3.56 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.02 sec: 1.22x faster                                                      |
| xml_etree_parse      | 150 ms                                                       | 139 ms: 1.08x faster                                                        |
| xml_etree_generate   | 86.5 ms                                                      | 81.9 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 97.4 ms: 1.06x faster                                                       |
| unpickle_pure_python | 217 us                                                       | 206 us: 1.05x faster                                                        |
| xml_etree_process    | 61.2 ms                                                      | 59.3 ms: 1.03x faster                                                       |
| json_dumps           | 11.1 ms                                                      | 11.3 ms: 1.01x slower                                                       |
| pickle_pure_python   | 323 us                                                       | 333 us: 1.03x slower                                                        |
| json_loads           | 24.7 us                                                      | 25.6 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| python_startup_no_site | 8.96 ms                                                      | 8.83 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.2 ms: 1.13x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 52.8 ms: 1.08x faster                                                       |
| django_template | 36.4 ms                                                      | 35.3 ms: 1.03x faster                                                       |
| mako            | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.05x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                                     | 1.27 sec: 1.99x faster                                                      |
| deepcopy                   | 392 us                                                       | 276 us: 1.42x faster                                                        |
| async_tree_memoization_tg  | 466 ms                                                       | 333 ms: 1.40x faster                                                        |
| async_tree_none            | 376 ms                                                       | 273 ms: 1.38x faster                                                        |
| go                         | 162 ms                                                       | 119 ms: 1.37x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 332 ms: 1.36x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 28.8 us: 1.34x faster                                                       |
| async_tree_io              | 843 ms                                                       | 630 ms: 1.34x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 638 ms: 1.30x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 272 ms: 1.27x faster                                                        |
| tomli_loads                | 2.46 sec                                                     | 2.02 sec: 1.22x faster                                                      |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 505 ms: 1.20x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.97 us: 1.19x faster                                                       |
| pyflate                    | 503 ms                                                       | 427 ms: 1.18x faster                                                        |
| scimark_sor                | 123 ms                                                       | 105 ms: 1.17x faster                                                        |
| dulwich_log                | 68.2 ms                                                      | 58.5 ms: 1.16x faster                                                       |
| richards                   | 52.9 ms                                                      | 45.6 ms: 1.16x faster                                                       |
| float                      | 81.3 ms                                                      | 70.8 ms: 1.15x faster                                                       |
| richards_super             | 59.6 ms                                                      | 51.8 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 510 ms: 1.14x faster                                                        |
| generators                 | 33.6 ms                                                      | 29.5 ms: 1.14x faster                                                       |
| genshi_text                | 26.2 ms                                                      | 23.2 ms: 1.13x faster                                                       |
| regex_v8                   | 26.1 ms                                                      | 23.3 ms: 1.12x faster                                                       |
| html5lib                   | 73.5 ms                                                      | 65.5 ms: 1.12x faster                                                       |
| spectral_norm              | 97.0 ms                                                      | 86.8 ms: 1.12x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 5.91 ms: 1.11x faster                                                       |
| pylint                     | 347 ms                                                       | 319 ms: 1.09x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.58 sec: 1.09x faster                                                      |
| pprint_safe_repr           | 843 ms                                                       | 775 ms: 1.09x faster                                                        |
| meteor_contest             | 130 ms                                                       | 120 ms: 1.08x faster                                                        |
| async_generators           | 457 ms                                                       | 422 ms: 1.08x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 52.8 ms: 1.08x faster                                                       |
| regex_dna                  | 247 ms                                                       | 229 ms: 1.08x faster                                                        |
| xml_etree_parse            | 150 ms                                                       | 139 ms: 1.08x faster                                                        |
| sympy_integrate            | 23.6 ms                                                      | 21.9 ms: 1.08x faster                                                       |
| logging_simple             | 6.39 us                                                      | 5.94 us: 1.08x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.73 sec: 1.08x faster                                                      |
| regex_compile              | 143 ms                                                       | 133 ms: 1.07x faster                                                        |
| scimark_monte_carlo        | 66.1 ms                                                      | 61.8 ms: 1.07x faster                                                       |
| deltablue                  | 3.42 ms                                                      | 3.20 ms: 1.07x faster                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 81.9 ms: 1.06x faster                                                       |
| json                       | 5.69 ms                                                      | 5.38 ms: 1.06x faster                                                       |
| logging_format             | 6.94 us                                                      | 6.57 us: 1.06x faster                                                       |
| scimark_fft                | 328 ms                                                       | 311 ms: 1.06x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                       | 97.4 ms: 1.06x faster                                                       |
| unpickle_pure_python       | 217 us                                                       | 206 us: 1.05x faster                                                        |
| thrift                     | 901 us                                                       | 856 us: 1.05x faster                                                        |
| sympy_str                  | 298 ms                                                       | 284 ms: 1.05x faster                                                        |
| sympy_expand               | 509 ms                                                       | 486 ms: 1.05x faster                                                        |
| 2to3                       | 293 ms                                                       | 281 ms: 1.04x faster                                                        |
| comprehensions             | 17.0 us                                                      | 16.4 us: 1.04x faster                                                       |
| logging_silent             | 97.9 ns                                                      | 94.1 ns: 1.04x faster                                                       |
| python_startup             | 15.9 ms                                                      | 15.3 ms: 1.04x faster                                                       |
| k_core                     | 2.17 sec                                                     | 2.09 sec: 1.04x faster                                                      |
| sympy_sum                  | 155 ms                                                       | 149 ms: 1.04x faster                                                        |
| xml_etree_process          | 61.2 ms                                                      | 59.3 ms: 1.03x faster                                                       |
| django_template            | 36.4 ms                                                      | 35.3 ms: 1.03x faster                                                       |
| sphinx                     | 1.12 sec                                                     | 1.09 sec: 1.03x faster                                                      |
| regex_effbot               | 3.67 ms                                                      | 3.56 ms: 1.03x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 17.1 ms: 1.03x faster                                                       |
| sqlite_synth               | 2.91 us                                                      | 2.84 us: 1.02x faster                                                       |
| scimark_lu                 | 98.7 ms                                                      | 96.6 ms: 1.02x faster                                                       |
| connected_components       | 432 ms                                                       | 423 ms: 1.02x faster                                                        |
| chaos                      | 60.2 ms                                                      | 59.0 ms: 1.02x faster                                                       |
| shortest_path              | 460 ms                                                       | 451 ms: 1.02x faster                                                        |
| pycparser                  | 1.24 sec                                                     | 1.22 sec: 1.02x faster                                                      |
| asyncio_websockets         | 388 ms                                                       | 382 ms: 1.02x faster                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 8.83 ms: 1.01x faster                                                       |
| fannkuch                   | 363 ms                                                       | 360 ms: 1.01x faster                                                        |
| typing_runtime_protocols   | 169 us                                                       | 167 us: 1.01x faster                                                        |
| nqueens                    | 90.7 ms                                                      | 91.1 ms: 1.00x slower                                                       |
| docutils                   | 2.83 sec                                                     | 2.86 sec: 1.01x slower                                                      |
| json_dumps                 | 11.1 ms                                                      | 11.3 ms: 1.01x slower                                                       |
| pidigits                   | 252 ms                                                       | 256 ms: 1.02x slower                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.86 ms: 1.02x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 333 us: 1.03x slower                                                        |
| bench_thread_pool          | 942 us                                                       | 974 us: 1.03x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.3 ms: 1.03x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 76.1 ms: 1.04x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.6 us: 1.04x slower                                                       |
| nbody                      | 89.3 ms                                                      | 93.0 ms: 1.04x slower                                                       |
| mako                       | 10.4 ms                                                      | 10.8 ms: 1.04x slower                                                       |
| raytrace                   | 273 ms                                                       | 284 ms: 1.04x slower                                                        |
| coverage                   | 80.0 ms                                                      | 84.4 ms: 1.06x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.93 ms: 1.09x slower                                                       |
| many_optionals             | 930 us                                                       | 1.02 ms: 1.10x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 6.47 ms: 1.37x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 25.0 ms: 1.43x slower                                                       |
| telco                      | 8.79 ms                                                      | 161 ms: 18.28x slower                                                       |
| bench_mp_pool              | 5.12 ms                                                      | 1.55 sec: 302.06x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (1): djangocms
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.10x