# Results vs. 3.13.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: windows-amd64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.079x faster
- HPT reliability: 80.49%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 223 ms: 1.03x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.66 sec: 1.09x slower                                                     |
| sphinx         | 617 ms                                                      | 644 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.93x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                       |
| async_tree_none            | 219 ms                                                      | 167 ms: 1.31x faster                                                       |
| async_tree_io              | 513 ms                                                      | 391 ms: 1.31x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 384 ms: 1.29x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.15x faster                                                       |
| async_generators           | 223 ms                                                      | 252 ms: 1.13x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.7 ms: 1.17x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 54.7 ms: 1.21x faster                                                      |
| float          | 50.8 ms                                                     | 44.5 ms: 1.14x faster                                                      |
| pidigits       | 146 ms                                                      | 146 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.9 ms: 1.72x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.61 ms: 1.05x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 79.1 ms: 1.02x faster                                                      |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 107 us: 1.21x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.14 sec: 1.20x faster                                                     |
| xml_etree_parse      | 92.2 ms                                                     | 87.9 ms: 1.05x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 51.1 ms: 1.05x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.6 us: 1.04x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 36.1 ms: 1.01x faster                                                      |
| json_dumps           | 6.19 ms                                                     | 6.28 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 61.7 ms: 1.02x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 204 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.5 ms: 1.04x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.2 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.35 ms: 1.23x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.8 ms: 1.04x slower                                                      |
| genshi_xml      | 33.9 ms                                                     | 36.3 ms: 1.07x slower                                                      |
| django_template | 20.3 ms                                                     | 25.0 ms: 1.23x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 501 us: 16.91x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 30.1 ms: 2.50x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.93x faster                                                       |
| mdp                        | 1.43 sec                                                    | 800 ms: 1.79x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.9 ms: 1.72x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                       |
| async_tree_none            | 219 ms                                                      | 167 ms: 1.31x faster                                                       |
| async_tree_io              | 513 ms                                                      | 391 ms: 1.31x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 384 ms: 1.29x faster                                                       |
| deepcopy                   | 223 us                                                      | 173 us: 1.29x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.7 us: 1.23x faster                                                      |
| mako                       | 6.56 ms                                                     | 5.35 ms: 1.23x faster                                                      |
| nbody                      | 66.3 ms                                                     | 54.7 ms: 1.21x faster                                                      |
| unpickle_pure_python       | 130 us                                                      | 107 us: 1.21x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.14 sec: 1.20x faster                                                     |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.25 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.15x faster                                                       |
| scimark_fft                | 175 ms                                                      | 153 ms: 1.14x faster                                                       |
| float                      | 50.8 ms                                                     | 44.5 ms: 1.14x faster                                                      |
| fannkuch                   | 252 ms                                                      | 220 ms: 1.14x faster                                                       |
| pyflate                    | 283 ms                                                      | 252 ms: 1.12x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.58 sec: 1.11x faster                                                     |
| deepcopy_reduce            | 2.02 us                                                     | 1.83 us: 1.10x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.41 ms: 1.10x faster                                                      |
| go                         | 84.7 ms                                                     | 78.2 ms: 1.08x faster                                                      |
| json                       | 3.30 ms                                                     | 3.05 ms: 1.08x faster                                                      |
| pprint_safe_repr           | 485 ms                                                      | 458 ms: 1.06x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.61 ms: 1.05x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.62 sec: 1.05x faster                                                     |
| xml_etree_parse            | 92.2 ms                                                     | 87.9 ms: 1.05x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 51.1 ms: 1.05x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.6 us: 1.04x faster                                                      |
| pprint_pformat             | 977 ms                                                      | 944 ms: 1.03x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 79.1 ms: 1.02x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.02x faster                                                      |
| meteor_contest             | 72.0 ms                                                     | 70.9 ms: 1.01x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 36.1 ms: 1.01x faster                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 45.4 ms: 1.00x faster                                                      |
| pidigits                   | 146 ms                                                      | 146 ms: 1.00x faster                                                       |
| shortest_path              | 355 ms                                                      | 358 ms: 1.01x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 40.5 ms: 1.01x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 105 us: 1.01x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.28 ms: 1.01x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 61.7 ms: 1.02x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 55.7 ns: 1.02x slower                                                      |
| connected_components       | 320 ms                                                      | 327 ms: 1.02x slower                                                       |
| comprehensions             | 10.4 us                                                     | 10.6 us: 1.02x slower                                                      |
| sympy_str                  | 167 ms                                                      | 171 ms: 1.03x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.7 ms: 1.03x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 87.6 ms: 1.03x slower                                                      |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| 2to3                       | 215 ms                                                      | 223 ms: 1.03x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.8 ms: 1.04x slower                                                      |
| sympy_expand               | 286 ms                                                      | 298 ms: 1.04x slower                                                       |
| sphinx                     | 617 ms                                                      | 644 ms: 1.04x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.5 ms: 1.04x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.4 ms: 1.04x slower                                                      |
| richards_super             | 29.8 ms                                                     | 31.4 ms: 1.06x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 80.6 ms: 1.06x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 67.3 ms: 1.06x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 43.3 ms: 1.06x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 861 us: 1.06x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 59.7 ms: 1.06x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.57 us: 1.06x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.16 us: 1.07x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.31 ms: 1.07x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.12 ms: 1.07x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 36.3 ms: 1.07x slower                                                      |
| generators                 | 19.0 ms                                                     | 20.3 ms: 1.07x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.13 ms: 1.09x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.66 sec: 1.09x slower                                                     |
| chaos                      | 37.9 ms                                                     | 41.3 ms: 1.09x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 204 us: 1.10x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 62.4 ms: 1.10x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 94.4 ms: 1.12x slower                                                      |
| coverage                   | 45.3 ms                                                     | 50.9 ms: 1.12x slower                                                      |
| async_generators           | 223 ms                                                      | 252 ms: 1.13x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.2 ms: 1.13x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.7 ms: 1.17x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.24 ms: 1.18x slower                                                      |
| raytrace                   | 153 ms                                                      | 182 ms: 1.19x slower                                                       |
| django_template            | 20.3 ms                                                     | 25.0 ms: 1.23x slower                                                      |
| many_optionals             | 361 us                                                      | 447 us: 1.24x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 17.2 ms: 1.58x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (3): pylint, pycparser, html5lib
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.079x faster

# HPT report

- Reliability score: 80.49% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown