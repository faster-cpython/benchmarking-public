# Results vs. 3.13.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: windows-amd64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.069x faster
- HPT reliability: 85.98%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 218 ms: 1.01x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.60 sec: 1.05x slower                                                     |
| sphinx         | 617 ms                                                      | 634 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.36x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 202 ms: 1.31x faster                                                       |
| async_tree_io              | 513 ms                                                      | 393 ms: 1.30x faster                                                       |
| async_tree_none            | 219 ms                                                      | 168 ms: 1.30x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 396 ms: 1.25x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 340 ms: 1.13x faster                                                       |
| async_generators           | 223 ms                                                      | 231 ms: 1.04x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 42.9 ms: 1.18x faster                                                      |
| nbody          | 66.3 ms                                                     | 64.2 ms: 1.03x faster                                                      |
| pidigits       | 146 ms                                                      | 145 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.50 ms: 1.13x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.5 ms: 1.03x faster                                                      |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.1 us: 1.07x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 87.8 ms: 1.05x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.35 sec: 1.02x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 132 us: 1.02x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 55.5 ms: 1.04x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 38.4 ms: 1.05x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.7 ms: 1.07x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 206 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.0 ms: 1.06x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| django_template | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 496 us: 17.08x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 30.2 ms: 2.49x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                       |
| mdp                        | 1.43 sec                                                    | 802 ms: 1.79x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.36x faster                                                       |
| deepcopy                   | 223 us                                                      | 169 us: 1.32x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 202 ms: 1.31x faster                                                       |
| async_tree_io              | 513 ms                                                      | 393 ms: 1.30x faster                                                       |
| async_tree_none            | 219 ms                                                      | 168 ms: 1.30x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 396 ms: 1.25x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 19.3 us: 1.20x faster                                                      |
| float                      | 50.8 ms                                                     | 42.9 ms: 1.18x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 329 ms: 1.15x faster                                                       |
| go                         | 84.7 ms                                                     | 74.6 ms: 1.14x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.50 ms: 1.13x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 340 ms: 1.13x faster                                                       |
| json                       | 3.30 ms                                                     | 2.95 ms: 1.12x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.81 us: 1.12x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.48 ms: 1.08x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.1 us: 1.07x faster                                                      |
| pylint                     | 205 ms                                                      | 195 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.48 ms: 1.05x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 87.8 ms: 1.05x faster                                                      |
| nbody                      | 66.3 ms                                                     | 64.2 ms: 1.03x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 78.5 ms: 1.03x faster                                                      |
| typing_runtime_protocols   | 103 us                                                      | 101 us: 1.02x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 74.9 ms: 1.02x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.35 sec: 1.02x faster                                                     |
| pidigits                   | 146 ms                                                      | 145 ms: 1.01x faster                                                       |
| sympy_expand               | 286 ms                                                      | 285 ms: 1.00x faster                                                       |
| dulwich_log                | 40.1 ms                                                     | 40.3 ms: 1.00x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 57.0 ms: 1.00x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 72.4 ms: 1.01x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.2 ms: 1.01x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 86.3 ms: 1.01x slower                                                      |
| 2to3                       | 215 ms                                                      | 218 ms: 1.01x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 492 ms: 1.02x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 55.5 ns: 1.02x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 64.5 ms: 1.02x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.92 sec: 1.02x slower                                                     |
| unpickle_pure_python       | 130 us                                                      | 132 us: 1.02x slower                                                       |
| shortest_path              | 355 ms                                                      | 363 ms: 1.02x slower                                                       |
| pyflate                    | 283 ms                                                      | 290 ms: 1.02x slower                                                       |
| richards                   | 26.3 ms                                                     | 26.9 ms: 1.02x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.5 ms: 1.03x slower                                                      |
| fannkuch                   | 252 ms                                                      | 258 ms: 1.03x slower                                                       |
| sphinx                     | 617 ms                                                      | 634 ms: 1.03x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.01 sec: 1.03x slower                                                     |
| comprehensions             | 10.4 us                                                     | 10.7 us: 1.03x slower                                                      |
| connected_components       | 320 ms                                                      | 331 ms: 1.03x slower                                                       |
| scimark_fft                | 175 ms                                                      | 181 ms: 1.03x slower                                                       |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 47.2 ms: 1.04x slower                                                      |
| async_generators           | 223 ms                                                      | 231 ms: 1.04x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 55.5 ms: 1.04x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.60 sec: 1.05x slower                                                     |
| hexiom                     | 3.84 ms                                                     | 4.03 ms: 1.05x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 38.4 ms: 1.05x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 860 us: 1.06x slower                                                       |
| python_startup             | 24.4 ms                                                     | 26.0 ms: 1.06x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.31 ms: 1.07x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.7 ms: 1.07x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.10 ms: 1.07x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 60.3 ms: 1.07x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.21 us: 1.08x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.71 us: 1.09x slower                                                      |
| chaos                      | 37.9 ms                                                     | 41.3 ms: 1.09x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 206 us: 1.11x slower                                                       |
| coverage                   | 45.3 ms                                                     | 50.4 ms: 1.11x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 93.9 ms: 1.11x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.14 ms: 1.13x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                      |
| raytrace                   | 153 ms                                                      | 180 ms: 1.17x slower                                                       |
| many_optionals             | 361 us                                                      | 432 us: 1.20x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 16.8 ms: 1.55x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (10): html5lib, scimark_monte_carlo, json_dumps, sqlite_synth, sympy_integrate, mako, sympy_str, k_core, pycparser, genshi_xml
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf1-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.069x faster

# HPT report

- Reliability score: 85.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown