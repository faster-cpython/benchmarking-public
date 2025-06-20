# Results vs. 3.13.0

- fork: python
- ref: 7cc89496922b7edb033e
- machine: windows-amd64
- commit hash: 7cc8949
- commit date: 2025-06-19
- overall geometric mean: 1.049x faster
- HPT reliability: 99.07%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 223 ms: 1.03x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                     |
| sphinx         | 617 ms                                                      | 640 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.92x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 215 ms: 1.31x faster                                                       |
| async_tree_io              | 513 ms                                                      | 400 ms: 1.28x faster                                                       |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 211 ms: 1.26x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 397 ms: 1.25x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                       |
| async_generators           | 223 ms                                                      | 230 ms: 1.03x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.9 ms: 1.13x faster                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.53 ms: 1.11x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 81.2 ms: 1.01x slower                                                      |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 88.8 ms: 1.04x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 137 us: 1.05x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                     |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.6 ms: 1.07x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 57.1 ms: 1.07x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 39.8 ms: 1.09x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 215 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.0 ms: 1.07x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                      |
| mako            | 6.56 ms                                                     | 6.86 ms: 1.04x slower                                                      |
| django_template | 20.3 ms                                                     | 24.3 ms: 1.20x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 501 us: 16.90x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 31.6 ms: 2.38x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.92x faster                                                       |
| mdp                        | 1.43 sec                                                    | 814 ms: 1.76x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 215 ms: 1.31x faster                                                       |
| deepcopy                   | 223 us                                                      | 174 us: 1.29x faster                                                       |
| async_tree_io              | 513 ms                                                      | 400 ms: 1.28x faster                                                       |
| async_tree_none            | 219 ms                                                      | 174 ms: 1.26x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 211 ms: 1.26x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 397 ms: 1.25x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 20.0 us: 1.15x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 331 ms: 1.15x faster                                                       |
| float                      | 50.8 ms                                                     | 44.9 ms: 1.13x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 342 ms: 1.12x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.53 ms: 1.11x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.83 us: 1.10x faster                                                      |
| go                         | 84.7 ms                                                     | 77.4 ms: 1.09x faster                                                      |
| json                       | 3.30 ms                                                     | 3.04 ms: 1.09x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.62 ms: 1.05x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.8 ms: 1.04x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.51 ms: 1.04x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.7 ms: 1.03x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 62.4 ms: 1.02x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 81.2 ms: 1.01x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 104 us: 1.01x slower                                                       |
| sympy_expand               | 286 ms                                                      | 289 ms: 1.01x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.01x slower                                                      |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 73.5 ms: 1.02x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.4 ms: 1.02x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 41.1 ms: 1.02x slower                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.95 sec: 1.03x slower                                                     |
| scimark_sor                | 76.2 ms                                                     | 78.4 ms: 1.03x slower                                                      |
| shortest_path              | 355 ms                                                      | 366 ms: 1.03x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 87.9 ms: 1.03x slower                                                      |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| scimark_fft                | 175 ms                                                      | 181 ms: 1.03x slower                                                       |
| async_generators           | 223 ms                                                      | 230 ms: 1.03x slower                                                       |
| 2to3                       | 215 ms                                                      | 223 ms: 1.03x slower                                                       |
| sphinx                     | 617 ms                                                      | 640 ms: 1.04x slower                                                       |
| fannkuch                   | 252 ms                                                      | 261 ms: 1.04x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 59.0 ms: 1.04x slower                                                      |
| richards_super             | 29.8 ms                                                     | 31.0 ms: 1.04x slower                                                      |
| pyflate                    | 283 ms                                                      | 296 ms: 1.04x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.86 ms: 1.04x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.4 ms: 1.04x slower                                                      |
| connected_components       | 320 ms                                                      | 335 ms: 1.05x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 137 us: 1.05x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                     |
| crypto_pyaes               | 45.6 ms                                                     | 48.3 ms: 1.06x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.63 sec: 1.06x slower                                                     |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.6 ms: 1.07x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.0 ms: 1.07x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 57.1 ms: 1.07x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.1 us: 1.07x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.13 ms: 1.08x slower                                                      |
| coverage                   | 45.3 ms                                                     | 49.0 ms: 1.08x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.33 ms: 1.09x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 39.8 ms: 1.09x slower                                                      |
| chaos                      | 37.9 ms                                                     | 41.4 ms: 1.09x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.16 ms: 1.10x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 62.1 ms: 1.11x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.90 us: 1.12x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.46 us: 1.12x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 555 ms: 1.14x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.4 ms: 1.15x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.13 sec: 1.15x slower                                                     |
| pickle_pure_python         | 186 us                                                      | 215 us: 1.16x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.24 ms: 1.19x slower                                                      |
| raytrace                   | 153 ms                                                      | 184 ms: 1.20x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.3 ms: 1.20x slower                                                      |
| many_optionals             | 361 us                                                      | 439 us: 1.22x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 17.1 ms: 1.57x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 327 ns: 5.98x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (9): pylint, pidigits, nbody, sqlite_synth, html5lib, json_dumps, k_core, pycparser, genshi_xml
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250619-3.15.0a0-7cc8949/bm-20250619-pythonperf1-amd64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.049x faster

# HPT report

- Reliability score: 99.07% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown