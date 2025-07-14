# Results vs. 3.13.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: windows-amd64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.064x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 229 ms: 1.07x slower                                                       |
| docutils       | 1.53 sec                                                    | 2.87 sec: 1.87x slower                                                     |
| html5lib       | 38.2 ms                                                     | 41.0 ms: 1.07x slower                                                      |
| sphinx         | 617 ms                                                      | 692 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                       | 1.24x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 140 ms: 2.15x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 331 ms: 1.50x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 192 ms: 1.46x faster                                                       |
| async_tree_io              | 513 ms                                                      | 354 ms: 1.45x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 147 ms: 1.36x faster                                                       |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.27x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 211 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 309 ms: 1.24x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| async_generators           | 223 ms                                                      | 267 ms: 1.20x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 15.1 ms: 1.21x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.28x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.9 ms: 1.11x faster                                                      |
| pidigits       | 146 ms                                                      | 137 ms: 1.07x faster                                                       |
| nbody          | 66.3 ms                                                     | 84.0 ms: 1.27x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.5 ms: 1.76x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.58 ms: 1.07x faster                                                      |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 94.7 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 60.5 ms                                                     | 59.2 ms: 1.02x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 91.0 ms: 1.01x faster                                                      |
| json_loads           | 15.1 us                                                     | 15.7 us: 1.04x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 6.70 ms: 1.08x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 62.4 ms: 1.17x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 44.7 ms: 1.22x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 160 us: 1.23x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 237 us: 1.27x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 2.69 sec: 1.96x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.19x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.6 ms: 1.05x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 39.3 ms: 1.16x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 19.0 ms: 1.25x slower                                                      |
| django_template | 20.3 ms                                                     | 27.5 ms: 1.36x slower                                                      |
| mako            | 6.56 ms                                                     | 9.84 ms: 1.50x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.31x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 581 us: 14.56x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 30.6 ms: 2.46x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 140 ms: 2.15x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.5 ms: 1.76x faster                                                      |
| gc_traversal               | 1.96 ms                                                     | 1.15 ms: 1.71x faster                                                      |
| async_tree_io_tg           | 497 ms                                                      | 331 ms: 1.50x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 192 ms: 1.46x faster                                                       |
| async_tree_io              | 513 ms                                                      | 354 ms: 1.45x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 147 ms: 1.36x faster                                                       |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.27x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 211 ms: 1.25x faster                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 977 us: 1.25x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 309 ms: 1.24x faster                                                       |
| mdp                        | 1.43 sec                                                    | 1.17 sec: 1.23x faster                                                     |
| sqlite_synth               | 1.59 us                                                     | 1.33 us: 1.19x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| deepcopy                   | 223 us                                                      | 199 us: 1.12x faster                                                       |
| float                      | 50.8 ms                                                     | 45.9 ms: 1.11x faster                                                      |
| deepcopy_memo              | 23.1 us                                                     | 20.9 us: 1.10x faster                                                      |
| json                       | 3.30 ms                                                     | 3.05 ms: 1.08x faster                                                      |
| pidigits                   | 146 ms                                                      | 137 ms: 1.07x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.58 ms: 1.07x faster                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 78.9 ms: 1.07x faster                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 59.2 ms: 1.02x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 91.0 ms: 1.01x faster                                                      |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                       |
| json_loads                 | 15.1 us                                                     | 15.7 us: 1.04x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.6 ms: 1.05x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 42.1 ms: 1.05x slower                                                      |
| pylint                     | 205 ms                                                      | 216 ms: 1.05x slower                                                       |
| pycparser                  | 695 ms                                                      | 731 ms: 1.05x slower                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 2.13 us: 1.05x slower                                                      |
| 2to3                       | 215 ms                                                      | 229 ms: 1.07x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 41.0 ms: 1.07x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.70 ms: 1.08x slower                                                      |
| go                         | 84.7 ms                                                     | 92.5 ms: 1.09x slower                                                      |
| sphinx                     | 617 ms                                                      | 692 ms: 1.12x slower                                                       |
| sympy_expand               | 286 ms                                                      | 324 ms: 1.13x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 62.0 ns: 1.14x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 14.2 ms: 1.15x slower                                                      |
| telco                      | 4.85 ms                                                     | 5.59 ms: 1.15x slower                                                      |
| pyflate                    | 283 ms                                                      | 327 ms: 1.15x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 39.3 ms: 1.16x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 99.0 ms: 1.16x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 62.4 ms: 1.17x slower                                                      |
| sympy_str                  | 167 ms                                                      | 195 ms: 1.17x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 568 ms: 1.17x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 94.7 ms: 1.17x slower                                                      |
| comprehensions             | 10.4 us                                                     | 12.2 us: 1.18x slower                                                      |
| generators                 | 19.0 ms                                                     | 22.4 ms: 1.18x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 3.11 ms: 1.19x slower                                                      |
| logging_format             | 6.18 us                                                     | 7.38 us: 1.19x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.91 us: 1.20x slower                                                      |
| async_generators           | 223 ms                                                      | 267 ms: 1.20x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 91.6 ms: 1.20x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 76.3 ms: 1.20x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 68.3 ms: 1.21x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.63 ms: 1.21x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 15.1 ms: 1.21x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 87.3 ms: 1.21x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 44.7 ms: 1.22x slower                                                      |
| fannkuch                   | 252 ms                                                      | 309 ms: 1.23x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 160 us: 1.23x slower                                                       |
| chaos                      | 37.9 ms                                                     | 47.0 ms: 1.24x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 19.0 ms: 1.25x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 129 us: 1.25x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 57.7 ms: 1.26x slower                                                      |
| nbody                      | 66.3 ms                                                     | 84.0 ms: 1.27x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 237 us: 1.27x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 72.1 ms: 1.28x slower                                                      |
| scimark_fft                | 175 ms                                                      | 226 ms: 1.29x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.50 ms: 1.32x slower                                                      |
| richards                   | 26.3 ms                                                     | 34.8 ms: 1.33x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 54.1 ms: 1.33x slower                                                      |
| many_optionals             | 361 us                                                      | 488 us: 1.35x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 1.10 ms: 1.35x slower                                                      |
| django_template            | 20.3 ms                                                     | 27.5 ms: 1.36x slower                                                      |
| richards_super             | 29.8 ms                                                     | 41.1 ms: 1.38x slower                                                      |
| raytrace                   | 153 ms                                                      | 213 ms: 1.39x slower                                                       |
| coverage                   | 45.3 ms                                                     | 66.9 ms: 1.48x slower                                                      |
| mako                       | 6.56 ms                                                     | 9.84 ms: 1.50x slower                                                      |
| k_core                     | 1.70 sec                                                    | 2.66 sec: 1.57x slower                                                     |
| pprint_pformat             | 977 ms                                                      | 1.70 sec: 1.74x slower                                                     |
| subparsers                 | 10.9 ms                                                     | 19.4 ms: 1.79x slower                                                      |
| shortest_path              | 355 ms                                                      | 640 ms: 1.80x slower                                                       |
| docutils                   | 1.53 sec                                                    | 2.87 sec: 1.87x slower                                                     |
| bpe_tokeniser              | 2.87 sec                                                    | 5.52 sec: 1.92x slower                                                     |
| connected_components       | 320 ms                                                      | 615 ms: 1.92x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 2.69 sec: 1.96x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.07x slower                                                               |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.064x slower

# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown