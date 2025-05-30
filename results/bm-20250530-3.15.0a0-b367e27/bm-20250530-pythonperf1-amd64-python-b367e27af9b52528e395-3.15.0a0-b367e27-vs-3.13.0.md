# Results vs. 3.13.0

- fork: python
- ref: b367e27af9b52528e395
- machine: windows-amd64
- commit hash: b367e27
- commit date: 2025-05-30
- overall geometric mean: 1.017x slower
- HPT reliability: 88.54%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.61 sec: 1.05x slower                                                     |
| html5lib       | 38.2 ms                                                     | 39.1 ms: 1.02x slower                                                      |
| sphinx         | 617 ms                                                      | 642 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                       |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                       |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 402 ms: 1.24x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 339 ms: 1.13x faster                                                       |
| async_generators           | 223 ms                                                      | 232 ms: 1.04x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.10x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 43.7 ms: 1.16x faster                                                      |
| nbody          | 66.3 ms                                                     | 62.4 ms: 1.06x faster                                                      |
| pidigits       | 146 ms                                                      | 147 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.59 ms: 1.06x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 79.7 ms: 1.01x faster                                                      |
| regex_dna      | 115 ms                                                      | 122 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 87.9 ms: 1.05x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.9 us: 1.02x faster                                                      |
| json_dumps           | 6.19 ms                                                     | 6.11 ms: 1.01x faster                                                      |
| unpickle_pure_python | 130 us                                                      | 133 us: 1.02x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 54.8 ms: 1.02x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 38.1 ms: 1.04x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.5 ms: 1.05x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 209 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 15.2 ms                                                     | 15.0 ms: 1.02x faster                                                      |
| django_template | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 75.3 ms                                                     | 31.6 ms: 2.38x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 159 ms: 1.89x faster                                                       |
| mdp                        | 1.43 sec                                                    | 795 ms: 1.80x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 14.2 ms: 1.68x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 208 ms: 1.35x faster                                                       |
| deepcopy                   | 223 us                                                      | 168 us: 1.33x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 17.7 us: 1.31x faster                                                      |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                       |
| async_tree_none            | 219 ms                                                      | 170 ms: 1.29x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 206 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 402 ms: 1.24x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                       |
| float                      | 50.8 ms                                                     | 43.7 ms: 1.16x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 339 ms: 1.13x faster                                                       |
| go                         | 84.7 ms                                                     | 75.1 ms: 1.13x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 57.7 ms: 1.10x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.84 us: 1.10x faster                                                      |
| json                       | 3.30 ms                                                     | 3.02 ms: 1.09x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.56 ms: 1.06x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.59 ms: 1.06x faster                                                      |
| nbody                      | 66.3 ms                                                     | 62.4 ms: 1.06x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.46 ms: 1.06x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 38.7 ms: 1.05x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 87.9 ms: 1.05x faster                                                      |
| meteor_contest             | 72.0 ms                                                     | 70.5 ms: 1.02x faster                                                      |
| genshi_text                | 15.2 ms                                                     | 15.0 ms: 1.02x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.9 us: 1.02x faster                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.11 ms: 1.01x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 79.7 ms: 1.01x faster                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.2 ms: 1.01x faster                                                      |
| scimark_fft                | 175 ms                                                      | 173 ms: 1.01x faster                                                       |
| sympy_str                  | 167 ms                                                      | 167 ms: 1.00x slower                                                       |
| pidigits                   | 146 ms                                                      | 147 ms: 1.01x slower                                                       |
| sympy_expand               | 286 ms                                                      | 288 ms: 1.01x slower                                                       |
| pyflate                    | 283 ms                                                      | 286 ms: 1.01x slower                                                       |
| generators                 | 19.0 ms                                                     | 19.2 ms: 1.01x slower                                                      |
| shortest_path              | 355 ms                                                      | 362 ms: 1.02x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.93 sec: 1.02x slower                                                     |
| sympy_sum                  | 85.2 ms                                                     | 87.1 ms: 1.02x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 41.0 ms: 1.02x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 39.1 ms: 1.02x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 133 us: 1.02x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 54.8 ms: 1.02x slower                                                      |
| fannkuch                   | 252 ms                                                      | 258 ms: 1.03x slower                                                       |
| comprehensions             | 10.4 us                                                     | 10.6 us: 1.03x slower                                                      |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                       |
| richards                   | 26.3 ms                                                     | 27.1 ms: 1.03x slower                                                      |
| connected_components       | 320 ms                                                      | 330 ms: 1.03x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 47.1 ms: 1.03x slower                                                      |
| chaos                      | 37.9 ms                                                     | 39.3 ms: 1.04x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.9 ms: 1.04x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 3.99 ms: 1.04x slower                                                      |
| sphinx                     | 617 ms                                                      | 642 ms: 1.04x slower                                                       |
| async_generators           | 223 ms                                                      | 232 ms: 1.04x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 38.1 ms: 1.04x slower                                                      |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.5 ms: 1.05x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.61 sec: 1.05x slower                                                     |
| bench_thread_pool          | 810 us                                                      | 854 us: 1.05x slower                                                       |
| regex_dna                  | 115 ms                                                      | 122 ms: 1.06x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                      |
| logging_simple             | 5.77 us                                                     | 6.20 us: 1.07x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.31 ms: 1.07x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.11 ms: 1.07x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.67 us: 1.08x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 61.2 ms: 1.09x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 530 ms: 1.09x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.7 ms: 1.10x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.09 sec: 1.11x slower                                                     |
| bench_mp_pool              | 84.2 ms                                                     | 94.4 ms: 1.12x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 209 us: 1.12x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.3 ms: 1.14x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.18 ms: 1.15x slower                                                      |
| raytrace                   | 153 ms                                                      | 179 ms: 1.17x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                      |
| many_optionals             | 361 us                                                      | 435 us: 1.21x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.9 ms: 1.55x slower                                                      |
| logging_silent             | 54.6 ns                                                     | 321 ns: 5.88x slower                                                       |
| coverage                   | 45.3 ms                                                     | 290 ms: 6.39x slower                                                       |
| thrift                     | 8.47 ms                                                     | 93.6 ms: 11.06x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (10): pylint, genshi_xml, k_core, sqlite_synth, tomli_loads, scimark_lu, mako, scimark_sor, typing_runtime_protocols, pycparser
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250530-3.15.0a0-b367e27/bm-20250530-pythonperf1-amd64-python-b367e27af9b52528e395-3.15.0a0-b367e27.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.017x slower

# HPT report

- Reliability score: 88.54% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown