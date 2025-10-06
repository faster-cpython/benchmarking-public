# Results vs. 3.13.0

- fork: python
- ref: 880c9526f91960b9cba5
- machine: windows-amd64
- commit hash: 880c952
- commit date: 2025-10-04
- overall geometric mean: 1.071x faster
- HPT reliability: 78.81%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 213 ms: 1.01x faster                                                       |
| docutils       | 1.53 sec                                                    | 1.58 sec: 1.03x slower                                                     |
| html5lib       | 38.2 ms                                                     | 37.0 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.36x faster                                                       |
| async_tree_io              | 513 ms                                                      | 384 ms: 1.33x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 201 ms: 1.31x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 379 ms: 1.31x faster                                                       |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 165 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 324 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 333 ms: 1.15x faster                                                       |
| async_generators           | 223 ms                                                      | 228 ms: 1.02x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.12x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.24x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.7 ms: 1.16x faster                                                      |
| nbody          | 66.3 ms                                                     | 64.4 ms: 1.03x faster                                                      |
| pidigits       | 146 ms                                                      | 147 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.6 ms: 1.63x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.48 ms: 1.14x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.8 ms: 1.02x faster                                                      |
| regex_dna      | 115 ms                                                      | 119 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 6.19 ms                                                     | 5.42 ms: 1.14x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.2 us: 1.06x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 87.9 ms: 1.05x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                     |
| xml_etree_iterparse  | 60.5 ms                                                     | 61.9 ms: 1.02x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 133 us: 1.02x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 55.5 ms: 1.04x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 38.6 ms: 1.06x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 206 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.5 ms: 1.05x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                                      |
| django_template | 20.3 ms                                                     | 24.3 ms: 1.20x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 498 us: 16.99x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 29.8 ms: 2.53x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                       |
| mdp                        | 1.43 sec                                                    | 786 ms: 1.82x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.6 ms: 1.63x faster                                                      |
| deepcopy_memo              | 23.1 us                                                     | 16.8 us: 1.37x faster                                                      |
| deepcopy                   | 223 us                                                      | 164 us: 1.36x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 207 ms: 1.36x faster                                                       |
| async_tree_io              | 513 ms                                                      | 384 ms: 1.33x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 201 ms: 1.31x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 379 ms: 1.31x faster                                                       |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 165 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 324 ms: 1.17x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.14 ms: 1.17x faster                                                      |
| float                      | 50.8 ms                                                     | 43.7 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 333 ms: 1.15x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.42 ms: 1.14x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.48 ms: 1.14x faster                                                      |
| json                       | 3.30 ms                                                     | 2.90 ms: 1.14x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.81 us: 1.12x faster                                                      |
| go                         | 84.7 ms                                                     | 75.7 ms: 1.12x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.39 ms: 1.09x faster                                                      |
| pylint                     | 205 ms                                                      | 190 ms: 1.08x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.06x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 87.9 ms: 1.05x faster                                                      |
| scimark_fft                | 175 ms                                                      | 168 ms: 1.04x faster                                                       |
| dulwich_log                | 40.1 ms                                                     | 38.8 ms: 1.03x faster                                                      |
| html5lib                   | 38.2 ms                                                     | 37.0 ms: 1.03x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.5 ms: 1.03x faster                                                      |
| nbody                      | 66.3 ms                                                     | 64.4 ms: 1.03x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 78.8 ms: 1.02x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.02x faster                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.1 ms: 1.02x faster                                                      |
| scimark_lu                 | 56.7 ms                                                     | 56.0 ms: 1.01x faster                                                      |
| typing_runtime_protocols   | 103 us                                                      | 102 us: 1.01x faster                                                       |
| sympy_expand               | 286 ms                                                      | 283 ms: 1.01x faster                                                       |
| pyflate                    | 283 ms                                                      | 280 ms: 1.01x faster                                                       |
| genshi_text                | 15.2 ms                                                     | 15.1 ms: 1.01x faster                                                      |
| 2to3                       | 215 ms                                                      | 213 ms: 1.01x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.36 sec: 1.01x faster                                                     |
| sympy_str                  | 167 ms                                                      | 166 ms: 1.01x faster                                                       |
| shortest_path              | 355 ms                                                      | 353 ms: 1.01x faster                                                       |
| pidigits                   | 146 ms                                                      | 147 ms: 1.01x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.1 ms: 1.01x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 77.2 ms: 1.01x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 491 ms: 1.01x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 55.6 ns: 1.02x slower                                                      |
| richards                   | 26.3 ms                                                     | 26.8 ms: 1.02x slower                                                      |
| connected_components       | 320 ms                                                      | 327 ms: 1.02x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 61.9 ms: 1.02x slower                                                      |
| async_generators           | 223 ms                                                      | 228 ms: 1.02x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 133 us: 1.02x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.00 sec: 1.02x slower                                                     |
| meteor_contest             | 72.0 ms                                                     | 74.0 ms: 1.03x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.96 sec: 1.03x slower                                                     |
| richards_super             | 29.8 ms                                                     | 30.7 ms: 1.03x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.58 sec: 1.03x slower                                                     |
| comprehensions             | 10.4 us                                                     | 10.7 us: 1.04x slower                                                      |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.04x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.27 ms: 1.04x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 55.5 ms: 1.04x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 65.9 ms: 1.04x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 47.4 ms: 1.04x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.02 us: 1.04x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.44 us: 1.04x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.5 ms: 1.05x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 88.1 ms: 1.05x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.02 ms: 1.05x slower                                                      |
| fannkuch                   | 252 ms                                                      | 264 ms: 1.05x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 38.6 ms: 1.06x slower                                                      |
| chaos                      | 37.9 ms                                                     | 40.9 ms: 1.08x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 61.8 ms: 1.10x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 206 us: 1.11x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.12x slower                                                      |
| coverage                   | 45.3 ms                                                     | 50.6 ms: 1.12x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.0 ms: 1.12x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.21 ms: 1.12x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.18 ms: 1.15x slower                                                      |
| raytrace                   | 153 ms                                                      | 180 ms: 1.17x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.3 ms: 1.20x slower                                                      |
| many_optionals             | 361 us                                                      | 563 us: 1.56x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 30.5 ms: 2.81x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (7): k_core, sympy_sum, genshi_xml, pycparser, sphinx, mako, bench_thread_pool
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251004-3.15.0a0-880c952/bm-20251004-pythonperf1-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.071x faster

# HPT report

- Reliability score: 78.81% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown