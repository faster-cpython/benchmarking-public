# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.487x faster
- HPT reliability: 85.96%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 216 ms: 1.01x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.68 sec: 1.10x slower                                                     |
| sphinx         | 617 ms                                                      | 652 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 167 ms: 1.80x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| async_tree_io              | 513 ms                                                      | 393 ms: 1.31x faster                                                       |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 402 ms: 1.24x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 172 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 332 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                       |
| async_generators           | 223 ms                                                      | 246 ms: 1.10x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.11x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.4 ms: 1.17x faster                                                      |
| nbody          | 66.3 ms                                                     | 59.7 ms: 1.11x faster                                                      |
| pidigits       | 146 ms                                                      | 149 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.9 ms: 1.72x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 70.6 ms: 1.14x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.66 ms: 1.02x faster                                                      |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.15 sec: 1.19x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 110 us: 1.18x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 88.0 ms: 1.05x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 52.0 ms: 1.03x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 36.2 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.7 ms: 1.05x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 207 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.0 ms: 1.07x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.6 ms: 1.16x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.43 ms: 1.21x faster                                                      |
| django_template | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pprint_pformat             | 977 ms                                                      | 995 ns: 981684.66x faster                                                  |
| pprint_safe_repr           | 485 ms                                                      | 579 ns: 836315.17x faster                                                  |
| thrift                     | 8.47 ms                                                     | 499 us: 16.98x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 31.8 ms: 2.37x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 167 ms: 1.80x faster                                                       |
| mdp                        | 1.43 sec                                                    | 802 ms: 1.79x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.9 ms: 1.72x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| deepcopy                   | 223 us                                                      | 168 us: 1.33x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 17.7 us: 1.31x faster                                                      |
| async_tree_io              | 513 ms                                                      | 393 ms: 1.31x faster                                                       |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 402 ms: 1.24x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.43 ms: 1.21x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.15 sec: 1.19x faster                                                     |
| unpickle_pure_python       | 130 us                                                      | 110 us: 1.18x faster                                                       |
| float                      | 50.8 ms                                                     | 43.4 ms: 1.17x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 172 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 332 ms: 1.15x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 70.6 ms: 1.14x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.80 us: 1.13x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.35 ms: 1.12x faster                                                      |
| nbody                      | 66.3 ms                                                     | 59.7 ms: 1.11x faster                                                      |
| json                       | 3.30 ms                                                     | 2.97 ms: 1.11x faster                                                      |
| go                         | 84.7 ms                                                     | 76.4 ms: 1.11x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.37 ms: 1.10x faster                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.62 sec: 1.10x faster                                                     |
| scimark_fft                | 175 ms                                                      | 161 ms: 1.09x faster                                                       |
| pyflate                    | 283 ms                                                      | 263 ms: 1.07x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 88.0 ms: 1.05x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 60.8 ms: 1.04x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.64 sec: 1.04x faster                                                     |
| xml_etree_generate         | 53.5 ms                                                     | 52.0 ms: 1.03x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.66 ms: 1.02x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.02x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 75.0 ms: 1.02x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 36.2 ms: 1.01x faster                                                      |
| fannkuch                   | 252 ms                                                      | 250 ms: 1.01x faster                                                       |
| 2to3                       | 215 ms                                                      | 216 ms: 1.01x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 40.4 ms: 1.01x slower                                                      |
| shortest_path              | 355 ms                                                      | 359 ms: 1.01x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 105 us: 1.01x slower                                                       |
| pidigits                   | 146 ms                                                      | 149 ms: 1.01x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.02x slower                                                      |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 46.6 ms: 1.02x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.5 ms: 1.03x slower                                                      |
| connected_components       | 320 ms                                                      | 328 ms: 1.03x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 87.5 ms: 1.03x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.0 ms: 1.03x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 74.3 ms: 1.03x slower                                                      |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| sympy_expand               | 286 ms                                                      | 296 ms: 1.03x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.04x slower                                                      |
| pycparser                  | 695 ms                                                      | 722 ms: 1.04x slower                                                       |
| comprehensions             | 10.4 us                                                     | 10.8 us: 1.04x slower                                                      |
| chaos                      | 37.9 ms                                                     | 39.6 ms: 1.05x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 58.9 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.7 ms: 1.05x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.06 ms: 1.06x slower                                                      |
| sphinx                     | 617 ms                                                      | 652 ms: 1.06x slower                                                       |
| python_startup             | 24.4 ms                                                     | 26.0 ms: 1.07x slower                                                      |
| coverage                   | 45.3 ms                                                     | 48.4 ms: 1.07x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.19 us: 1.07x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.66 us: 1.08x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.34 ms: 1.09x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.68 sec: 1.10x slower                                                     |
| async_generators           | 223 ms                                                      | 246 ms: 1.10x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.17 ms: 1.10x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.11x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 207 us: 1.11x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.19 ms: 1.16x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.6 ms: 1.16x slower                                                      |
| raytrace                   | 153 ms                                                      | 183 ms: 1.19x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                      |
| many_optionals             | 361 us                                                      | 435 us: 1.20x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.7 ms: 1.54x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 316 ns: 5.79x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.45x faster                                                               |

Benchmark hidden because not significant (7): pylint, scimark_monte_carlo, scimark_lu, html5lib, json_dumps, genshi_text, genshi_xml
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-pythonperf1-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.487x faster

# HPT report

- Reliability score: 85.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown