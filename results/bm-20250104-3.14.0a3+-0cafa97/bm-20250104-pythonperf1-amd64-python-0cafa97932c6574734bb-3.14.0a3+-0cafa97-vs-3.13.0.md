# Results vs. 3.13.0

- fork: python
- ref: 0cafa97932c6574734bb
- machine: windows-amd64
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.007x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 224 ms: 1.04x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.4 ms: 1.03x slower                                                       |
| sphinx         | 617 ms                                                      | 645 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                        |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 396 ms: 1.26x faster                                                        |
| async_tree_none            | 219 ms                                                      | 179 ms: 1.22x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 222 ms: 1.19x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 345 ms: 1.10x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 315 ms: 1.05x slower                                                        |
| async_generators           | 223 ms                                                      | 237 ms: 1.07x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                        |
| float          | 50.8 ms                                                     | 52.1 ms: 1.02x slower                                                       |
| nbody          | 66.3 ms                                                     | 75.3 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.69 ms                                                     | 1.46 ms: 1.16x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 86.5 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.1 us: 1.07x faster                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 88.8 ms: 1.04x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.5 ms: 1.03x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 56.4 ms: 1.05x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.57 ms: 1.06x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 39.6 ms: 1.09x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 145 us: 1.11x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 220 us: 1.18x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 23.6 ms: 1.04x faster                                                       |
| python_startup_no_site | 16.9 ms                                                     | 17.3 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.69 ms: 1.02x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 36.2 ms: 1.07x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 17.5 ms: 1.15x slower                                                       |
| django_template | 20.3 ms                                                     | 25.5 ms: 1.26x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.12x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 533 us: 15.89x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                        |
| async_tree_io              | 513 ms                                                      | 397 ms: 1.29x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 396 ms: 1.26x faster                                                        |
| async_tree_none            | 219 ms                                                      | 179 ms: 1.22x faster                                                        |
| deepcopy                   | 223 us                                                      | 185 us: 1.21x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 222 ms: 1.19x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 170 ms: 1.18x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 19.8 us: 1.17x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.46 ms: 1.16x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.12x faster                                                        |
| json                       | 3.30 ms                                                     | 2.98 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 345 ms: 1.10x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.88 us: 1.08x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.1 us: 1.07x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 88.8 ms: 1.04x faster                                                       |
| python_startup             | 24.4 ms                                                     | 23.6 ms: 1.04x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 82.3 ms: 1.02x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 62.2 ms: 1.02x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.76 ms: 1.02x faster                                                       |
| create_gc_cycles           | 1.22 ms                                                     | 1.20 ms: 1.02x faster                                                       |
| shortest_path              | 355 ms                                                      | 351 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.59 ms: 1.00x faster                                                       |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                        |
| coverage                   | 45.3 ms                                                     | 45.8 ms: 1.01x slower                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.61 us: 1.01x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.39 sec: 1.01x slower                                                      |
| mdp                        | 1.43 sec                                                    | 1.46 sec: 1.02x slower                                                      |
| mako                       | 6.56 ms                                                     | 6.69 ms: 1.02x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 17.3 ms: 1.02x slower                                                       |
| float                      | 50.8 ms                                                     | 52.1 ms: 1.02x slower                                                       |
| go                         | 84.7 ms                                                     | 87.1 ms: 1.03x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.4 ms: 1.03x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.5 ms: 1.03x slower                                                       |
| 2to3                       | 215 ms                                                      | 224 ms: 1.04x slower                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 3.00 sec: 1.05x slower                                                      |
| sphinx                     | 617 ms                                                      | 645 ms: 1.05x slower                                                        |
| pycparser                  | 695 ms                                                      | 727 ms: 1.05x slower                                                        |
| asyncio_websockets         | 300 ms                                                      | 315 ms: 1.05x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 42.1 ms: 1.05x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 56.4 ms: 1.05x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 48.1 ms: 1.05x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 89.9 ms: 1.06x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.57 ms: 1.06x slower                                                       |
| sympy_str                  | 167 ms                                                      | 178 ms: 1.06x slower                                                        |
| async_generators           | 223 ms                                                      | 237 ms: 1.07x slower                                                        |
| scimark_lu                 | 56.7 ms                                                     | 60.5 ms: 1.07x slower                                                       |
| genshi_xml                 | 33.9 ms                                                     | 36.2 ms: 1.07x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 76.9 ms: 1.07x slower                                                       |
| sympy_expand               | 286 ms                                                      | 306 ms: 1.07x slower                                                        |
| regex_compile              | 80.7 ms                                                     | 86.5 ms: 1.07x slower                                                       |
| fannkuch                   | 252 ms                                                      | 270 ms: 1.07x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.4 ms: 1.07x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.65 sec: 1.08x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 39.6 ms: 1.09x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.07 sec: 1.09x slower                                                      |
| pprint_safe_repr           | 485 ms                                                      | 531 ms: 1.10x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 113 us: 1.10x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.36 us: 1.10x slower                                                       |
| scimark_fft                | 175 ms                                                      | 193 ms: 1.10x slower                                                        |
| sqlglot_optimize           | 32.5 ms                                                     | 35.9 ms: 1.10x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.86 us: 1.11x slower                                                       |
| unpickle_pure_python       | 130 us                                                      | 145 us: 1.11x slower                                                        |
| generators                 | 19.0 ms                                                     | 21.2 ms: 1.12x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 45.8 ms: 1.12x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 61.6 ns: 1.13x slower                                                       |
| scimark_sor                | 76.2 ms                                                     | 86.1 ms: 1.13x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.34 ms: 1.13x slower                                                       |
| pyflate                    | 283 ms                                                      | 321 ms: 1.13x slower                                                        |
| nqueens                    | 56.1 ms                                                     | 63.7 ms: 1.13x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 195 ms: 1.14x slower                                                        |
| chaos                      | 37.9 ms                                                     | 43.0 ms: 1.14x slower                                                       |
| nbody                      | 66.3 ms                                                     | 75.3 ms: 1.14x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.8 us: 1.14x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 17.5 ms: 1.15x slower                                                       |
| richards                   | 26.3 ms                                                     | 30.4 ms: 1.16x slower                                                       |
| richards_super             | 29.8 ms                                                     | 34.5 ms: 1.16x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.11 ms: 1.17x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 895 us: 1.17x slower                                                        |
| pickle_pure_python         | 186 us                                                      | 220 us: 1.18x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.25 ms: 1.19x slower                                                       |
| many_optionals             | 361 us                                                      | 443 us: 1.23x slower                                                        |
| raytrace                   | 153 ms                                                      | 190 ms: 1.24x slower                                                        |
| django_template            | 20.3 ms                                                     | 25.5 ms: 1.26x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.0 ms: 1.47x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (8): regex_v8, pylint, k_core, connected_components, gc_traversal, pathlib, regex_dna, bench_thread_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20250104-3.14.0a3+-0cafa97/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: mypy2

- Geometric mean (including insignificant results): 1.007x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown