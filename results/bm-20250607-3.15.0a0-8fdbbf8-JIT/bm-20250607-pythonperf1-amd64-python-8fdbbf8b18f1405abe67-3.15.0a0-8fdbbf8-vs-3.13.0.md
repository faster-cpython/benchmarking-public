# Results vs. 3.13.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: windows-amd64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.076x faster
- HPT reliability: 63.23%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                     |
| sphinx         | 617 ms                                                      | 646 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.89x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                       |
| async_tree_io              | 513 ms                                                      | 395 ms: 1.30x faster                                                       |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 393 ms: 1.26x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                       |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.5 ms: 1.14x faster                                                      |
| nbody          | 66.3 ms                                                     | 59.5 ms: 1.11x faster                                                      |
| pidigits       | 146 ms                                                      | 149 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 13.6 ms: 1.75x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.55 ms: 1.09x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.2 ms: 1.03x faster                                                      |
| regex_dna      | 115 ms                                                      | 116 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.16 sec: 1.19x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 112 us: 1.16x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 87.0 ms: 1.06x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 50.8 ms: 1.05x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 36.7 ms: 1.01x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 6.38 ms: 1.03x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.8 ms: 1.05x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 204 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.2 ms: 1.07x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.54 ms: 1.18x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.6 ms: 1.03x slower                                                      |
| django_template | 20.3 ms                                                     | 23.9 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 492 us: 17.20x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 32.0 ms: 2.35x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.89x faster                                                       |
| mdp                        | 1.43 sec                                                    | 809 ms: 1.77x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 13.6 ms: 1.75x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.34x faster                                                       |
| deepcopy                   | 223 us                                                      | 171 us: 1.31x faster                                                       |
| async_tree_io              | 513 ms                                                      | 395 ms: 1.30x faster                                                       |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 393 ms: 1.26x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.8 us: 1.23x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.16 sec: 1.19x faster                                                     |
| mako                       | 6.56 ms                                                     | 5.54 ms: 1.18x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 112 us: 1.16x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| float                      | 50.8 ms                                                     | 44.5 ms: 1.14x faster                                                      |
| go                         | 84.7 ms                                                     | 75.7 ms: 1.12x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                       |
| nbody                      | 66.3 ms                                                     | 59.5 ms: 1.11x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.36 ms: 1.11x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.82 us: 1.11x faster                                                      |
| scimark_fft                | 175 ms                                                      | 158 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.37 ms: 1.10x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.55 ms: 1.09x faster                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.63 sec: 1.09x faster                                                     |
| json                       | 3.30 ms                                                     | 3.06 ms: 1.08x faster                                                      |
| pyflate                    | 283 ms                                                      | 264 ms: 1.07x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 87.0 ms: 1.06x faster                                                      |
| fannkuch                   | 252 ms                                                      | 238 ms: 1.06x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 50.8 ms: 1.05x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 60.3 ms: 1.05x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.64 sec: 1.04x faster                                                     |
| regex_compile              | 80.7 ms                                                     | 78.2 ms: 1.03x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.7 ms: 1.03x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 74.8 ms: 1.02x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 36.7 ms: 1.01x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 104 us: 1.01x slower                                                       |
| regex_dna                  | 115 ms                                                      | 116 ms: 1.01x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 72.8 ms: 1.01x slower                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.61 us: 1.01x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 40.7 ms: 1.02x slower                                                      |
| shortest_path              | 355 ms                                                      | 361 ms: 1.02x slower                                                       |
| pidigits                   | 146 ms                                                      | 149 ms: 1.02x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.6 ms: 1.02x slower                                                      |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 46.7 ms: 1.02x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 87.3 ms: 1.02x slower                                                      |
| sympy_expand               | 286 ms                                                      | 293 ms: 1.03x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.6 ms: 1.03x slower                                                      |
| connected_components       | 320 ms                                                      | 329 ms: 1.03x slower                                                       |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.38 ms: 1.03x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.7 ms: 1.03x slower                                                      |
| comprehensions             | 10.4 us                                                     | 10.7 us: 1.03x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.2 ms: 1.03x slower                                                      |
| chaos                      | 37.9 ms                                                     | 39.2 ms: 1.04x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.7 ms: 1.04x slower                                                      |
| sphinx                     | 617 ms                                                      | 646 ms: 1.05x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.8 ms: 1.05x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 60.3 ms: 1.06x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.2 ms: 1.07x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 60.3 ms: 1.07x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 521 ms: 1.07x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.26 us: 1.08x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.17 ms: 1.09x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                     |
| logging_format             | 6.18 us                                                     | 6.76 us: 1.09x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 204 us: 1.10x slower                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.35 ms: 1.10x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.07 sec: 1.10x slower                                                     |
| async_generators           | 223 ms                                                      | 247 ms: 1.11x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.19 ms: 1.12x slower                                                      |
| coverage                   | 45.3 ms                                                     | 50.7 ms: 1.12x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 14.1 ms: 1.13x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| raytrace                   | 153 ms                                                      | 180 ms: 1.17x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.22 ms: 1.17x slower                                                      |
| django_template            | 20.3 ms                                                     | 23.9 ms: 1.18x slower                                                      |
| many_optionals             | 361 us                                                      | 449 us: 1.24x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 17.0 ms: 1.57x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 325 ns: 5.95x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (4): pylint, html5lib, genshi_xml, pycparser
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-pythonperf1-amd64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.076x faster

# HPT report

- Reliability score: 63.23% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown