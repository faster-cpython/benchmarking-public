# Results vs. 3.13.0

- fork: python
- ref: 6eb6c5dbfb528bd07d77
- machine: windows-amd64
- commit hash: 6eb6c5d
- commit date: 2025-06-13
- overall geometric mean: 1.033x slower
- HPT reliability: 99.39%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 223 ms: 1.04x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                     |
| html5lib       | 38.2 ms                                                     | 39.1 ms: 1.02x slower                                                      |
| sphinx         | 617 ms                                                      | 644 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.92x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.32x faster                                                       |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 210 ms: 1.26x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 395 ms: 1.26x faster                                                       |
| async_tree_none            | 219 ms                                                      | 179 ms: 1.23x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 334 ms: 1.14x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                       |
| async_generators           | 223 ms                                                      | 231 ms: 1.04x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.9 ms: 1.13x faster                                                      |
| nbody          | 66.3 ms                                                     | 65.2 ms: 1.02x faster                                                      |
| pidigits       | 146 ms                                                      | 149 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.0 ms: 1.70x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.53 ms: 1.10x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 80.2 ms: 1.01x faster                                                      |
| regex_dna      | 115 ms                                                      | 119 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.2 us: 1.06x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 89.3 ms: 1.03x faster                                                      |
| json_dumps           | 6.19 ms                                                     | 6.26 ms: 1.01x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| unpickle_pure_python | 130 us                                                      | 137 us: 1.06x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 56.7 ms: 1.06x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 39.6 ms: 1.09x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 65.7 ms: 1.09x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 214 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 26.0 ms: 1.07x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.65 ms: 1.01x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                      |
| django_template | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 32.0 ms: 2.35x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.92x faster                                                       |
| mdp                        | 1.43 sec                                                    | 808 ms: 1.77x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.0 ms: 1.70x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 212 ms: 1.32x faster                                                       |
| deepcopy                   | 223 us                                                      | 171 us: 1.31x faster                                                       |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 210 ms: 1.26x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 395 ms: 1.26x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.4 us: 1.25x faster                                                      |
| async_tree_none            | 219 ms                                                      | 179 ms: 1.23x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 334 ms: 1.14x faster                                                       |
| float                      | 50.8 ms                                                     | 44.9 ms: 1.13x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 341 ms: 1.12x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.83 us: 1.11x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.53 ms: 1.10x faster                                                      |
| go                         | 84.7 ms                                                     | 77.5 ms: 1.09x faster                                                      |
| json                       | 3.30 ms                                                     | 3.07 ms: 1.08x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 59.2 ms: 1.07x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.06x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.64 ms: 1.05x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 89.3 ms: 1.03x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.55 ms: 1.02x faster                                                      |
| nbody                      | 66.3 ms                                                     | 65.2 ms: 1.02x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 40.4 ms: 1.01x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 80.2 ms: 1.01x faster                                                      |
| meteor_contest             | 72.0 ms                                                     | 72.7 ms: 1.01x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.26 ms: 1.01x slower                                                      |
| mako                       | 6.56 ms                                                     | 6.65 ms: 1.01x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 15.4 ms: 1.01x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 105 us: 1.01x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.5 ms: 1.02x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.02x slower                                                     |
| pidigits                   | 146 ms                                                      | 149 ms: 1.02x slower                                                       |
| pyflate                    | 283 ms                                                      | 289 ms: 1.02x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.1 ms: 1.02x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 41.1 ms: 1.03x slower                                                      |
| fannkuch                   | 252 ms                                                      | 258 ms: 1.03x slower                                                       |
| shortest_path              | 355 ms                                                      | 365 ms: 1.03x slower                                                       |
| sympy_str                  | 167 ms                                                      | 172 ms: 1.03x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 47.0 ms: 1.03x slower                                                      |
| sympy_expand               | 286 ms                                                      | 295 ms: 1.03x slower                                                       |
| regex_dna                  | 115 ms                                                      | 119 ms: 1.04x slower                                                       |
| async_generators           | 223 ms                                                      | 231 ms: 1.04x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 88.3 ms: 1.04x slower                                                      |
| 2to3                       | 215 ms                                                      | 223 ms: 1.04x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.98 sec: 1.04x slower                                                     |
| pycparser                  | 695 ms                                                      | 724 ms: 1.04x slower                                                       |
| sphinx                     | 617 ms                                                      | 644 ms: 1.04x slower                                                       |
| scimark_fft                | 175 ms                                                      | 182 ms: 1.04x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.9 ms: 1.05x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 59.5 ms: 1.05x slower                                                      |
| connected_components       | 320 ms                                                      | 336 ms: 1.05x slower                                                       |
| chaos                      | 37.9 ms                                                     | 39.9 ms: 1.05x slower                                                      |
| richards                   | 26.3 ms                                                     | 27.7 ms: 1.06x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 137 us: 1.06x slower                                                       |
| richards_super             | 29.8 ms                                                     | 31.5 ms: 1.06x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.0 us: 1.06x slower                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 56.7 ms: 1.06x slower                                                      |
| python_startup             | 24.4 ms                                                     | 26.0 ms: 1.07x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                     |
| create_gc_cycles           | 1.22 ms                                                     | 1.32 ms: 1.08x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.15 ms: 1.08x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 39.6 ms: 1.09x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 65.7 ms: 1.09x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 61.2 ms: 1.09x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.14 ms: 1.09x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.46 us: 1.12x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.91 us: 1.12x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 548 ms: 1.13x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.12 sec: 1.15x slower                                                     |
| pickle_pure_python         | 186 us                                                      | 214 us: 1.15x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.6 ms: 1.17x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.26 ms: 1.19x slower                                                      |
| raytrace                   | 153 ms                                                      | 184 ms: 1.20x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.4 ms: 1.20x slower                                                      |
| many_optionals             | 361 us                                                      | 443 us: 1.23x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 17.0 ms: 1.56x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 321 ns: 5.88x slower                                                       |
| coverage                   | 45.3 ms                                                     | 296 ms: 6.53x slower                                                       |
| thrift                     | 8.47 ms                                                     | 98.3 ms: 11.61x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                               |

Benchmark hidden because not significant (5): pylint, scimark_sor, sqlite_synth, k_core, genshi_xml
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250613-3.15.0a0-6eb6c5d/bm-20250613-pythonperf1-amd64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.033x slower

# HPT report

- Reliability score: 99.39% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown