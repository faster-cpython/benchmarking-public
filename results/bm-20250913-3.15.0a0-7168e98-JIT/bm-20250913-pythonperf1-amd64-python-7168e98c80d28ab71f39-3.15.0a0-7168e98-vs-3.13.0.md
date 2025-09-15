# Results vs. 3.13.0

- fork: python
- ref: 7168e98c80d28ab71f39
- machine: windows-amd64
- commit hash: 7168e98
- commit date: 2025-09-13
- overall geometric mean: 1.108x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 1.53 sec                                                    | 1.60 sec: 1.05x slower                                                     |
| html5lib       | 38.2 ms                                                     | 36.7 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.86x faster                                                       |
| async_tree_io              | 513 ms                                                      | 382 ms: 1.34x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 378 ms: 1.32x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 202 ms: 1.31x faster                                                       |
| async_tree_none            | 219 ms                                                      | 168 ms: 1.30x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 165 ms: 1.21x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 332 ms: 1.15x faster                                                       |
| async_generators           | 223 ms                                                      | 251 ms: 1.13x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 55.5 ms: 1.19x faster                                                      |
| float          | 50.8 ms                                                     | 43.7 ms: 1.16x faster                                                      |
| pidigits       | 146 ms                                                      | 147 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.56 ms: 1.09x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 76.8 ms: 1.05x faster                                                      |
| regex_dna      | 115 ms                                                      | 118 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.08 sec: 1.27x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 105 us: 1.24x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 5.51 ms: 1.12x faster                                                      |
| json_loads           | 15.1 us                                                     | 13.8 us: 1.10x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 84.7 ms: 1.09x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 50.2 ms: 1.07x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 35.8 ms: 1.02x faster                                                      |
| pickle_pure_python   | 186 us                                                      | 198 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.0 ms: 1.03x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 18.6 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.25 ms: 1.25x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.3 ms: 1.01x slower                                                      |
| django_template | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 510 us: 16.61x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 28.9 ms: 2.61x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 162 ms: 1.86x faster                                                       |
| mdp                        | 1.43 sec                                                    | 791 ms: 1.81x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                      |
| deepcopy                   | 223 us                                                      | 164 us: 1.37x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 16.9 us: 1.36x faster                                                      |
| async_tree_io              | 513 ms                                                      | 382 ms: 1.34x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 378 ms: 1.32x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 202 ms: 1.31x faster                                                       |
| async_tree_none            | 219 ms                                                      | 168 ms: 1.30x faster                                                       |
| telco                      | 4.85 ms                                                     | 3.80 ms: 1.28x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.08 sec: 1.27x faster                                                     |
| mako                       | 6.56 ms                                                     | 5.25 ms: 1.25x faster                                                      |
| unpickle_pure_python       | 130 us                                                      | 105 us: 1.24x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 165 ms: 1.21x faster                                                       |
| nbody                      | 66.3 ms                                                     | 55.5 ms: 1.19x faster                                                      |
| scimark_fft                | 175 ms                                                      | 147 ms: 1.19x faster                                                       |
| fannkuch                   | 252 ms                                                      | 212 ms: 1.19x faster                                                       |
| richards                   | 26.3 ms                                                     | 22.3 ms: 1.18x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.23 ms: 1.17x faster                                                      |
| json                       | 3.30 ms                                                     | 2.83 ms: 1.17x faster                                                      |
| float                      | 50.8 ms                                                     | 43.7 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 332 ms: 1.15x faster                                                       |
| pprint_safe_repr           | 485 ms                                                      | 422 ms: 1.15x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.50 sec: 1.15x faster                                                     |
| deepcopy_reduce            | 2.02 us                                                     | 1.77 us: 1.14x faster                                                      |
| go                         | 84.7 ms                                                     | 74.3 ms: 1.14x faster                                                      |
| pprint_pformat             | 977 ms                                                      | 867 ms: 1.13x faster                                                       |
| richards_super             | 29.8 ms                                                     | 26.5 ms: 1.12x faster                                                      |
| json_dumps                 | 6.19 ms                                                     | 5.51 ms: 1.12x faster                                                      |
| pyflate                    | 283 ms                                                      | 252 ms: 1.12x faster                                                       |
| json_loads                 | 15.1 us                                                     | 13.8 us: 1.10x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 84.7 ms: 1.09x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.56 ms: 1.09x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.58 sec: 1.08x faster                                                     |
| scimark_monte_carlo        | 40.7 ms                                                     | 38.1 ms: 1.07x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 50.2 ms: 1.07x faster                                                      |
| pylint                     | 205 ms                                                      | 194 ms: 1.06x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 76.8 ms: 1.05x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.51 us: 1.05x faster                                                      |
| html5lib                   | 38.2 ms                                                     | 36.7 ms: 1.04x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 61.2 ms: 1.04x faster                                                      |
| typing_runtime_protocols   | 103 us                                                      | 100 us: 1.03x faster                                                       |
| logging_silent             | 54.6 ns                                                     | 53.2 ns: 1.03x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 74.4 ms: 1.02x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 35.8 ms: 1.02x faster                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 44.7 ms: 1.02x faster                                                      |
| shortest_path              | 355 ms                                                      | 349 ms: 1.02x faster                                                       |
| meteor_contest             | 72.0 ms                                                     | 71.4 ms: 1.01x faster                                                      |
| connected_components       | 320 ms                                                      | 318 ms: 1.01x faster                                                       |
| genshi_text                | 15.2 ms                                                     | 15.3 ms: 1.01x slower                                                      |
| pidigits                   | 146 ms                                                      | 147 ms: 1.01x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.4 ms: 1.01x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.2 ms: 1.01x slower                                                      |
| comprehensions             | 10.4 us                                                     | 10.5 us: 1.01x slower                                                      |
| regex_dna                  | 115 ms                                                      | 118 ms: 1.02x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.25 ms: 1.02x slower                                                      |
| sympy_expand               | 286 ms                                                      | 292 ms: 1.02x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.0 ms: 1.03x slower                                                      |
| logging_simple             | 5.77 us                                                     | 5.97 us: 1.03x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.41 us: 1.04x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 88.0 ms: 1.04x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.02 ms: 1.05x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.60 sec: 1.05x slower                                                     |
| nqueens                    | 56.1 ms                                                     | 58.8 ms: 1.05x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.06 ms: 1.05x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 860 us: 1.06x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 198 us: 1.06x slower                                                       |
| chaos                      | 37.9 ms                                                     | 40.7 ms: 1.07x slower                                                      |
| coverage                   | 45.3 ms                                                     | 49.3 ms: 1.09x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 18.6 ms: 1.10x slower                                                      |
| async_generators           | 223 ms                                                      | 251 ms: 1.13x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.15 ms: 1.14x slower                                                      |
| raytrace                   | 153 ms                                                      | 174 ms: 1.14x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                      |
| django_template            | 20.3 ms                                                     | 24.0 ms: 1.18x slower                                                      |
| many_optionals             | 361 us                                                      | 563 us: 1.56x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 29.8 ms: 2.75x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.10x faster                                                               |

Benchmark hidden because not significant (9): pycparser, dulwich_log, 2to3, sympy_str, scimark_lu, sympy_sum, genshi_xml, xml_etree_iterparse, sphinx
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250913-3.15.0a0-7168e98-JIT/bm-20250913-pythonperf1-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown