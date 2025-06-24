# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_hot
- machine: windows-amd64
- commit hash: a987be7
- commit date: 2025-06-23
- overall geometric mean: 1.085x faster
- HPT reliability: 71.29%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 219 ms: 1.02x slower                                                   |
| docutils       | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                 |
| sphinx         | 617 ms                                                      | 640 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                       | 1.04x slower                                                           |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                   |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                   |
| async_tree_io              | 513 ms                                                      | 393 ms: 1.30x faster                                                   |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.30x faster                                                   |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                   |
| async_tree_io_tg           | 497 ms                                                      | 392 ms: 1.27x faster                                                   |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                   |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.12x faster                                                   |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                   |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                  |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 55.3 ms: 1.20x faster                                                  |
| float          | 50.8 ms                                                     | 44.7 ms: 1.14x faster                                                  |
| pidigits       | 146 ms                                                      | 149 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                       | 1.10x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.9 ms: 1.71x faster                                                  |
| regex_effbot   | 1.69 ms                                                     | 1.59 ms: 1.06x faster                                                  |
| regex_compile  | 80.7 ms                                                     | 78.3 ms: 1.03x faster                                                  |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                       | 1.16x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.15 sec: 1.20x faster                                                 |
| unpickle_pure_python | 130 us                                                      | 109 us: 1.19x faster                                                   |
| xml_etree_generate   | 53.5 ms                                                     | 50.3 ms: 1.06x faster                                                  |
| json_loads           | 15.1 us                                                     | 14.3 us: 1.05x faster                                                  |
| xml_etree_parse      | 92.2 ms                                                     | 88.3 ms: 1.04x faster                                                  |
| xml_etree_process    | 36.5 ms                                                     | 35.5 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.0 ms: 1.04x slower                                                  |
| pickle_pure_python   | 186 us                                                      | 202 us: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                           |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.0 ms: 1.07x slower                                                  |
| python_startup_no_site | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                  |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.40 ms: 1.22x faster                                                  |
| django_template | 20.3 ms                                                     | 24.1 ms: 1.19x slower                                                  |
| Geometric mean  | (ref)                                                       | 1.00x faster                                                           |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 497 us: 17.04x faster                                                  |
| pathlib                    | 75.3 ms                                                     | 31.8 ms: 2.37x faster                                                  |
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                   |
| mdp                        | 1.43 sec                                                    | 807 ms: 1.77x faster                                                   |
| regex_v8                   | 23.8 ms                                                     | 13.9 ms: 1.71x faster                                                  |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                   |
| deepcopy                   | 223 us                                                      | 170 us: 1.31x faster                                                   |
| async_tree_io              | 513 ms                                                      | 393 ms: 1.30x faster                                                   |
| deepcopy_memo              | 23.1 us                                                     | 17.8 us: 1.30x faster                                                  |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.30x faster                                                   |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                   |
| async_tree_io_tg           | 497 ms                                                      | 392 ms: 1.27x faster                                                   |
| mako                       | 6.56 ms                                                     | 5.40 ms: 1.22x faster                                                  |
| nbody                      | 66.3 ms                                                     | 55.3 ms: 1.20x faster                                                  |
| tomli_loads                | 1.37 sec                                                    | 1.15 sec: 1.20x faster                                                 |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                   |
| unpickle_pure_python       | 130 us                                                      | 109 us: 1.19x faster                                                   |
| fannkuch                   | 252 ms                                                      | 215 ms: 1.17x faster                                                   |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.23 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                   |
| telco                      | 4.85 ms                                                     | 4.27 ms: 1.14x faster                                                  |
| float                      | 50.8 ms                                                     | 44.7 ms: 1.14x faster                                                  |
| deepcopy_reduce            | 2.02 us                                                     | 1.78 us: 1.13x faster                                                  |
| go                         | 84.7 ms                                                     | 75.5 ms: 1.12x faster                                                  |
| scimark_fft                | 175 ms                                                      | 157 ms: 1.12x faster                                                   |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.12x faster                                                   |
| bpe_tokeniser              | 2.87 sec                                                    | 2.60 sec: 1.11x faster                                                 |
| pyflate                    | 283 ms                                                      | 256 ms: 1.10x faster                                                   |
| json                       | 3.30 ms                                                     | 3.01 ms: 1.10x faster                                                  |
| regex_effbot               | 1.69 ms                                                     | 1.59 ms: 1.06x faster                                                  |
| xml_etree_generate         | 53.5 ms                                                     | 50.3 ms: 1.06x faster                                                  |
| spectral_norm              | 63.4 ms                                                     | 59.9 ms: 1.06x faster                                                  |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.05x faster                                                  |
| k_core                     | 1.70 sec                                                    | 1.63 sec: 1.04x faster                                                 |
| xml_etree_parse            | 92.2 ms                                                     | 88.3 ms: 1.04x faster                                                  |
| regex_compile              | 80.7 ms                                                     | 78.3 ms: 1.03x faster                                                  |
| xml_etree_process          | 36.5 ms                                                     | 35.5 ms: 1.03x faster                                                  |
| sqlite_synth               | 1.59 us                                                     | 1.55 us: 1.02x faster                                                  |
| scimark_sor                | 76.2 ms                                                     | 75.9 ms: 1.00x faster                                                  |
| crypto_pyaes               | 45.6 ms                                                     | 45.9 ms: 1.01x slower                                                  |
| scimark_monte_carlo        | 40.7 ms                                                     | 41.2 ms: 1.01x slower                                                  |
| pidigits                   | 146 ms                                                      | 149 ms: 1.02x slower                                                   |
| shortest_path              | 355 ms                                                      | 362 ms: 1.02x slower                                                   |
| dulwich_log                | 40.1 ms                                                     | 40.9 ms: 1.02x slower                                                  |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                   |
| 2to3                       | 215 ms                                                      | 219 ms: 1.02x slower                                                   |
| sympy_sum                  | 85.2 ms                                                     | 87.1 ms: 1.02x slower                                                  |
| typing_runtime_protocols   | 103 us                                                      | 106 us: 1.02x slower                                                   |
| connected_components       | 320 ms                                                      | 327 ms: 1.02x slower                                                   |
| sympy_integrate            | 12.3 ms                                                     | 12.6 ms: 1.02x slower                                                  |
| richards_super             | 29.8 ms                                                     | 30.5 ms: 1.03x slower                                                  |
| richards                   | 26.3 ms                                                     | 26.9 ms: 1.03x slower                                                  |
| comprehensions             | 10.4 us                                                     | 10.6 us: 1.03x slower                                                  |
| sympy_expand               | 286 ms                                                      | 294 ms: 1.03x slower                                                   |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.03x slower                                                   |
| pprint_pformat             | 977 ms                                                      | 1.01 sec: 1.04x slower                                                 |
| sphinx                     | 617 ms                                                      | 640 ms: 1.04x slower                                                   |
| generators                 | 19.0 ms                                                     | 19.7 ms: 1.04x slower                                                  |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.0 ms: 1.04x slower                                                  |
| hexiom                     | 3.84 ms                                                     | 4.05 ms: 1.05x slower                                                  |
| pprint_safe_repr           | 485 ms                                                      | 512 ms: 1.06x slower                                                   |
| python_startup             | 24.4 ms                                                     | 26.0 ms: 1.07x slower                                                  |
| coverage                   | 45.3 ms                                                     | 48.3 ms: 1.07x slower                                                  |
| logging_format             | 6.18 us                                                     | 6.59 us: 1.07x slower                                                  |
| chaos                      | 37.9 ms                                                     | 40.4 ms: 1.07x slower                                                  |
| nqueens                    | 56.1 ms                                                     | 60.1 ms: 1.07x slower                                                  |
| logging_simple             | 5.77 us                                                     | 6.21 us: 1.08x slower                                                  |
| gc_traversal               | 1.96 ms                                                     | 2.12 ms: 1.08x slower                                                  |
| docutils                   | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                 |
| pickle_pure_python         | 186 us                                                      | 202 us: 1.08x slower                                                   |
| create_gc_cycles           | 1.22 ms                                                     | 1.33 ms: 1.08x slower                                                  |
| scimark_lu                 | 56.7 ms                                                     | 62.8 ms: 1.11x slower                                                  |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                   |
| coroutines                 | 12.5 ms                                                     | 14.0 ms: 1.12x slower                                                  |
| python_startup_no_site     | 16.9 ms                                                     | 19.2 ms: 1.14x slower                                                  |
| deltablue                  | 1.89 ms                                                     | 2.22 ms: 1.17x slower                                                  |
| raytrace                   | 153 ms                                                      | 182 ms: 1.19x slower                                                   |
| django_template            | 20.3 ms                                                     | 24.1 ms: 1.19x slower                                                  |
| many_optionals             | 361 us                                                      | 449 us: 1.24x slower                                                   |
| subparsers                 | 10.9 ms                                                     | 17.2 ms: 1.59x slower                                                  |
| logging_silent             | 54.6 ns                                                     | 316 ns: 5.78x slower                                                   |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                           |

Benchmark hidden because not significant (7): pylint, json_dumps, meteor_contest, genshi_text, pycparser, genshi_xml, html5lib
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250623-3.15.0a0-a987be7-JIT/bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.085x faster

# HPT report

- Reliability score: 71.29% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown