# Results vs. 3.13.0

- fork: python
- ref: 719e5c3f7111bcda5eee
- machine: windows-amd64
- commit hash: 719e5c3
- commit date: 2025-08-19
- overall geometric mean: 1.081x faster
- HPT reliability: 91.01%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 221 ms: 1.03x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.68 sec: 1.10x slower                                                     |
| html5lib       | 38.2 ms                                                     | 39.3 ms: 1.03x slower                                                      |
| sphinx         | 617 ms                                                      | 639 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.93x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.33x faster                                                       |
| async_tree_io              | 513 ms                                                      | 389 ms: 1.32x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 386 ms: 1.29x faster                                                       |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.27x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.15x faster                                                       |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.13x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 53.4 ms: 1.24x faster                                                      |
| float          | 50.8 ms                                                     | 43.5 ms: 1.17x faster                                                      |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 15.5 ms: 1.54x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.55 ms: 1.09x faster                                                      |
| regex_compile  | 80.7 ms                                                     | 78.4 ms: 1.03x faster                                                      |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.11 sec: 1.24x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 106 us: 1.23x faster                                                       |
| json_dumps           | 6.19 ms                                                     | 5.40 ms: 1.15x faster                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 50.7 ms: 1.05x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 88.0 ms: 1.05x faster                                                      |
| xml_etree_process    | 36.5 ms                                                     | 35.2 ms: 1.04x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.7 us: 1.03x faster                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 63.2 ms: 1.04x slower                                                      |
| pickle_pure_python   | 186 us                                                      | 205 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.41 ms: 1.21x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| genshi_xml      | 33.9 ms                                                     | 35.2 ms: 1.04x slower                                                      |
| django_template | 20.3 ms                                                     | 24.3 ms: 1.20x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 501 us: 16.89x faster                                                      |
| pathlib                    | 75.3 ms                                                     | 29.1 ms: 2.58x faster                                                      |
| asyncio_websockets         | 300 ms                                                      | 156 ms: 1.93x faster                                                       |
| mdp                        | 1.43 sec                                                    | 811 ms: 1.76x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 15.5 ms: 1.54x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.33x faster                                                       |
| deepcopy                   | 223 us                                                      | 169 us: 1.32x faster                                                       |
| async_tree_io              | 513 ms                                                      | 389 ms: 1.32x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 204 ms: 1.30x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 386 ms: 1.29x faster                                                       |
| async_tree_none            | 219 ms                                                      | 172 ms: 1.27x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 18.2 us: 1.27x faster                                                      |
| nbody                      | 66.3 ms                                                     | 53.4 ms: 1.24x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.11 sec: 1.24x faster                                                     |
| unpickle_pure_python       | 130 us                                                      | 106 us: 1.23x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.41 ms: 1.21x faster                                                      |
| async_tree_none_tg         | 200 ms                                                      | 167 ms: 1.20x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.06 ms: 1.19x faster                                                      |
| fannkuch                   | 252 ms                                                      | 214 ms: 1.18x faster                                                       |
| float                      | 50.8 ms                                                     | 43.5 ms: 1.17x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 330 ms: 1.15x faster                                                       |
| pprint_safe_repr           | 485 ms                                                      | 423 ms: 1.15x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 334 ms: 1.15x faster                                                       |
| json_dumps                 | 6.19 ms                                                     | 5.40 ms: 1.15x faster                                                      |
| scimark_fft                | 175 ms                                                      | 153 ms: 1.14x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.28 ms: 1.14x faster                                                      |
| bpe_tokeniser              | 2.87 sec                                                    | 2.52 sec: 1.14x faster                                                     |
| pprint_pformat             | 977 ms                                                      | 865 ms: 1.13x faster                                                       |
| go                         | 84.7 ms                                                     | 76.0 ms: 1.11x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.84 us: 1.10x faster                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.55 ms: 1.09x faster                                                      |
| pyflate                    | 283 ms                                                      | 264 ms: 1.07x faster                                                       |
| k_core                     | 1.70 sec                                                    | 1.61 sec: 1.06x faster                                                     |
| json                       | 3.30 ms                                                     | 3.13 ms: 1.06x faster                                                      |
| xml_etree_generate         | 53.5 ms                                                     | 50.7 ms: 1.05x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.0 ms: 1.05x faster                                                      |
| xml_etree_process          | 36.5 ms                                                     | 35.2 ms: 1.04x faster                                                      |
| regex_compile              | 80.7 ms                                                     | 78.4 ms: 1.03x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.7 us: 1.03x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.7 ms: 1.03x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.55 us: 1.02x faster                                                      |
| meteor_contest             | 72.0 ms                                                     | 70.5 ms: 1.02x faster                                                      |
| logging_silent             | 54.6 ns                                                     | 53.8 ns: 1.01x faster                                                      |
| shortest_path              | 355 ms                                                      | 353 ms: 1.01x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 76.5 ms: 1.00x slower                                                      |
| dulwich_log                | 40.1 ms                                                     | 40.5 ms: 1.01x slower                                                      |
| connected_components       | 320 ms                                                      | 323 ms: 1.01x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 15.5 ms: 1.02x slower                                                      |
| richards                   | 26.3 ms                                                     | 26.8 ms: 1.02x slower                                                      |
| spectral_norm              | 63.4 ms                                                     | 64.9 ms: 1.02x slower                                                      |
| richards_super             | 29.8 ms                                                     | 30.5 ms: 1.02x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 12.7 ms: 1.03x slower                                                      |
| comprehensions             | 10.4 us                                                     | 10.7 us: 1.03x slower                                                      |
| sympy_str                  | 167 ms                                                      | 172 ms: 1.03x slower                                                       |
| 2to3                       | 215 ms                                                      | 221 ms: 1.03x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.3 ms: 1.03x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 87.7 ms: 1.03x slower                                                      |
| logging_simple             | 5.77 us                                                     | 5.95 us: 1.03x slower                                                      |
| generators                 | 19.0 ms                                                     | 19.6 ms: 1.03x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.38 us: 1.03x slower                                                      |
| sympy_expand               | 286 ms                                                      | 295 ms: 1.03x slower                                                       |
| sphinx                     | 617 ms                                                      | 639 ms: 1.04x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 35.2 ms: 1.04x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.00 ms: 1.04x slower                                                      |
| regex_dna                  | 115 ms                                                      | 120 ms: 1.04x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 63.2 ms: 1.04x slower                                                      |
| pycparser                  | 695 ms                                                      | 727 ms: 1.05x slower                                                       |
| python_startup             | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.30 ms: 1.06x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 60.1 ms: 1.06x slower                                                      |
| chaos                      | 37.9 ms                                                     | 40.6 ms: 1.07x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.12 ms: 1.08x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 61.0 ms: 1.09x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.68 sec: 1.10x slower                                                     |
| async_generators           | 223 ms                                                      | 245 ms: 1.10x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 205 us: 1.10x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 14.2 ms: 1.13x slower                                                      |
| coverage                   | 45.3 ms                                                     | 51.9 ms: 1.15x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.19 ms: 1.16x slower                                                      |
| raytrace                   | 153 ms                                                      | 181 ms: 1.18x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.3 ms: 1.20x slower                                                      |
| many_optionals             | 361 us                                                      | 578 us: 1.60x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 31.2 ms: 2.87x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                               |

Benchmark hidden because not significant (4): pylint, pidigits, crypto_pyaes, typing_runtime_protocols
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250819-3.15.0a0-719e5c3-JIT/bm-20250819-pythonperf1-amd64-python-719e5c3f7111bcda5eee-3.15.0a0-719e5c3.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.081x faster

# HPT report

- Reliability score: 91.01% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown