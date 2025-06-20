# Results vs. 3.13.0

- fork: python
- ref: 0f866cbfefd797b4dae2
- machine: windows-amd64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.078x faster
- HPT reliability: 64.84%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                     |
| sphinx         | 617 ms                                                      | 650 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.33x faster                                                       |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.30x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 205 ms: 1.29x faster                                                       |
| async_tree_io              | 513 ms                                                      | 398 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 335 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 345 ms: 1.11x faster                                                       |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.11x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.8 ms: 1.16x faster                                                      |
| nbody          | 66.3 ms                                                     | 58.5 ms: 1.13x faster                                                      |
| pidigits       | 146 ms                                                      | 149 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.56 ms: 1.09x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.3 ms: 1.03x faster                                                      |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.15 sec: 1.19x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 112 us: 1.16x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 51.5 ms: 1.04x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 91.2 ms: 1.01x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 36.3 ms: 1.01x faster                                                      |
| json_dumps           | 6.19 ms                                                     | 6.27 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.4 ms: 1.06x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 204 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.0 ms: 1.07x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.61 ms: 1.17x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| django_template | 20.3 ms                                                     | 23.9 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 494 us: 17.13x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 31.9 ms: 2.36x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 158 ms: 1.90x faster                                                       |
| mdp                        | 1.43 sec                                                    | 806 ms: 1.78x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.1 ms: 1.69x faster                                                      |
| deepcopy                   | 223 us                                                      | 168 us: 1.33x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.33x faster                                                       |
| async_tree_none            | 219 ms                                                      | 169 ms: 1.30x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 205 ms: 1.29x faster                                                       |
| async_tree_io              | 513 ms                                                      | 398 ms: 1.29x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.3 us: 1.26x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.15 sec: 1.19x faster                                                     |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.61 ms: 1.17x faster                                                      |
| float                      | 50.8 ms                                                     | 43.8 ms: 1.16x faster                                                      |
| unpickle_pure_python       | 130 us                                                      | 112 us: 1.16x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.27 ms: 1.15x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 335 ms: 1.14x faster                                                       |
| scimark_fft                | 175 ms                                                      | 154 ms: 1.13x faster                                                       |
| nbody                      | 66.3 ms                                                     | 58.5 ms: 1.13x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.80 us: 1.12x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.37 ms: 1.11x faster                                                      |
| go                         | 84.7 ms                                                     | 76.3 ms: 1.11x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 345 ms: 1.11x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.62 sec: 1.10x faster                                                     |
| regex_effbot               | 1.69 ms                                                     | 1.56 ms: 1.09x faster                                                      |
| pyflate                    | 283 ms                                                      | 261 ms: 1.08x faster                                                       |
| json                       | 3.30 ms                                                     | 3.06 ms: 1.08x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 59.9 ms: 1.06x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 51.5 ms: 1.04x faster                                                      |
| fannkuch                   | 252 ms                                                      | 244 ms: 1.03x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 78.3 ms: 1.03x faster                                                      |
| k_core                     | 1.70 sec                                                    | 1.65 sec: 1.03x faster                                                     |
| sqlite_synth               | 1.59 us                                                     | 1.56 us: 1.02x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 91.2 ms: 1.01x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 75.5 ms: 1.01x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 36.3 ms: 1.01x faster                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.27 ms: 1.01x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| pidigits                   | 146 ms                                                      | 149 ms: 1.02x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 73.2 ms: 1.02x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.6 ms: 1.02x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 41.1 ms: 1.02x slower                                                      |
| connected_components       | 320 ms                                                      | 328 ms: 1.03x slower                                                       |
| chaos                      | 37.9 ms                                                     | 38.9 ms: 1.03x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 106 us: 1.03x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 87.5 ms: 1.03x slower                                                      |
| sympy_str                  | 167 ms                                                      | 172 ms: 1.03x slower                                                       |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 47.1 ms: 1.03x slower                                                      |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.03x slower                                                       |
| sympy_expand               | 286 ms                                                      | 296 ms: 1.04x slower                                                       |
| richards_super             | 29.8 ms                                                     | 30.9 ms: 1.04x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 59.0 ms: 1.04x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.3 ms: 1.04x slower                                                      |
| sphinx                     | 617 ms                                                      | 650 ms: 1.05x slower                                                       |
| comprehensions             | 10.4 us                                                     | 10.9 us: 1.06x slower                                                      |
| coverage                   | 45.3 ms                                                     | 47.9 ms: 1.06x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 59.7 ms: 1.06x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.4 ms: 1.06x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.0 ms: 1.07x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.12 ms: 1.07x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 524 ms: 1.08x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.06 sec: 1.08x slower                                                     |
| docutils                   | 1.53 sec                                                    | 1.66 sec: 1.08x slower                                                     |
| create_gc_cycles           | 1.22 ms                                                     | 1.33 ms: 1.08x slower                                                      |
| async_generators           | 223 ms                                                      | 243 ms: 1.09x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.15 ms: 1.09x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 204 us: 1.09x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.79 us: 1.10x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.35 us: 1.10x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.8 ms: 1.11x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.5 ms: 1.15x slower                                                      |
| raytrace                   | 153 ms                                                      | 178 ms: 1.16x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.21 ms: 1.17x slower                                                      |
| django_template            | 20.3 ms                                                     | 23.9 ms: 1.18x slower                                                      |
| many_optionals             | 361 us                                                      | 446 us: 1.23x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.9 ms: 1.56x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 316 ns: 5.79x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (6): pylint, shortest_path, scimark_monte_carlo, html5lib, pycparser, genshi_xml
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-pythonperf1-amd64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.078x faster

# HPT report

- Reliability score: 64.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown