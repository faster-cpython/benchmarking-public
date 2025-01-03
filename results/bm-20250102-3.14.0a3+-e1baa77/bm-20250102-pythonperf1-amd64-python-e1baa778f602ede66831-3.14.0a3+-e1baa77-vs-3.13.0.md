# Results vs. 3.13.0

- fork: python
- ref: e1baa778f602ede66831
- machine: windows-amd64
- commit hash: e1baa77
- commit date: 2025-01-02
- overall geometric mean: 1.013x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 224 ms: 1.04x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.1 ms: 1.03x slower                                                       |
| sphinx         | 617 ms                                                      | 646 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.35x faster                                                        |
| async_tree_io              | 513 ms                                                      | 408 ms: 1.26x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 398 ms: 1.25x faster                                                        |
| async_tree_none            | 219 ms                                                      | 182 ms: 1.20x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 225 ms: 1.18x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 346 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 352 ms: 1.08x faster                                                        |
| async_generators           | 223 ms                                                      | 232 ms: 1.04x slower                                                        |
| asyncio_websockets         | 300 ms                                                      | 316 ms: 1.05x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.08x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                        |
| float          | 50.8 ms                                                     | 51.8 ms: 1.02x slower                                                       |
| nbody          | 66.3 ms                                                     | 75.9 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.69 ms                                                     | 1.44 ms: 1.18x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 86.4 ms: 1.07x slower                                                       |
| regex_dna      | 115 ms                                                      | 124 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 86.7 ms: 1.06x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.1 ms: 1.03x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 57.0 ms: 1.07x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.70 ms: 1.08x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 40.1 ms: 1.10x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 147 us: 1.13x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 222 us: 1.19x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 23.3 ms: 1.05x faster                                                       |
| python_startup_no_site | 16.9 ms                                                     | 17.3 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 6.77 ms: 1.03x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 35.4 ms: 1.04x slower                                                       |
| genshi_text     | 15.2 ms                                                     | 16.7 ms: 1.10x slower                                                       |
| django_template | 20.3 ms                                                     | 25.3 ms: 1.25x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 524 us: 16.17x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 209 ms: 1.35x faster                                                        |
| async_tree_io              | 513 ms                                                      | 408 ms: 1.26x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 398 ms: 1.25x faster                                                        |
| deepcopy                   | 223 us                                                      | 183 us: 1.22x faster                                                        |
| async_tree_none            | 219 ms                                                      | 182 ms: 1.20x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 225 ms: 1.18x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.44 ms: 1.18x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 171 ms: 1.17x faster                                                        |
| json                       | 3.30 ms                                                     | 2.91 ms: 1.14x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 20.5 us: 1.13x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 346 ms: 1.10x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.87 us: 1.08x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 352 ms: 1.08x faster                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 86.7 ms: 1.06x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                       |
| python_startup             | 24.4 ms                                                     | 23.3 ms: 1.05x faster                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 82.3 ms: 1.02x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.77 ms: 1.02x faster                                                       |
| shortest_path              | 355 ms                                                      | 349 ms: 1.02x faster                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 63.7 ms: 1.00x slower                                                       |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                        |
| float                      | 50.8 ms                                                     | 51.8 ms: 1.02x slower                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.62 us: 1.02x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 17.3 ms: 1.03x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.1 ms: 1.03x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.1 ms: 1.03x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.77 ms: 1.03x slower                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.70 ms: 1.04x slower                                                       |
| async_generators           | 223 ms                                                      | 232 ms: 1.04x slower                                                        |
| 2to3                       | 215 ms                                                      | 224 ms: 1.04x slower                                                        |
| go                         | 84.7 ms                                                     | 88.2 ms: 1.04x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.49 sec: 1.04x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.04x slower                                                      |
| genshi_xml                 | 33.9 ms                                                     | 35.4 ms: 1.04x slower                                                       |
| coverage                   | 45.3 ms                                                     | 47.3 ms: 1.04x slower                                                       |
| sphinx                     | 617 ms                                                      | 646 ms: 1.05x slower                                                        |
| crypto_pyaes               | 45.6 ms                                                     | 47.8 ms: 1.05x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.01 sec: 1.05x slower                                                      |
| pycparser                  | 695 ms                                                      | 732 ms: 1.05x slower                                                        |
| asyncio_websockets         | 300 ms                                                      | 316 ms: 1.05x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 42.4 ms: 1.06x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 90.7 ms: 1.06x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 57.0 ms: 1.07x slower                                                       |
| sympy_expand               | 286 ms                                                      | 305 ms: 1.07x slower                                                        |
| sympy_str                  | 167 ms                                                      | 178 ms: 1.07x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 110 us: 1.07x slower                                                        |
| regex_compile              | 80.7 ms                                                     | 86.4 ms: 1.07x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.65 us: 1.08x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 77.5 ms: 1.08x slower                                                       |
| regex_dna                  | 115 ms                                                      | 124 ms: 1.08x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.25 us: 1.08x slower                                                       |
| json_dumps                 | 6.19 ms                                                     | 6.70 ms: 1.08x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.6 ms: 1.08x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.4 ms: 1.09x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                      |
| scimark_fft                | 175 ms                                                      | 191 ms: 1.09x slower                                                        |
| genshi_text                | 15.2 ms                                                     | 16.7 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 35.7 ms: 1.10x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 40.1 ms: 1.10x slower                                                       |
| fannkuch                   | 252 ms                                                      | 277 ms: 1.10x slower                                                        |
| pprint_pformat             | 977 ms                                                      | 1.08 sec: 1.11x slower                                                      |
| scimark_lu                 | 56.7 ms                                                     | 63.2 ms: 1.12x slower                                                       |
| generators                 | 19.0 ms                                                     | 21.2 ms: 1.12x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 541 ms: 1.12x slower                                                        |
| sqlglot_normalize          | 172 ms                                                      | 193 ms: 1.13x slower                                                        |
| pyflate                    | 283 ms                                                      | 319 ms: 1.13x slower                                                        |
| unpickle_pure_python       | 130 us                                                      | 147 us: 1.13x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 62.4 ns: 1.14x slower                                                       |
| chaos                      | 37.9 ms                                                     | 43.3 ms: 1.14x slower                                                       |
| nbody                      | 66.3 ms                                                     | 75.9 ms: 1.15x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.44 ms: 1.16x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 65.1 ms: 1.16x slower                                                       |
| comprehensions             | 10.4 us                                                     | 12.1 us: 1.17x slower                                                       |
| richards_super             | 29.8 ms                                                     | 34.8 ms: 1.17x slower                                                       |
| richards                   | 26.3 ms                                                     | 30.7 ms: 1.17x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.12 ms: 1.17x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 900 us: 1.18x slower                                                        |
| scimark_monte_carlo        | 40.7 ms                                                     | 48.2 ms: 1.18x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 222 us: 1.19x slower                                                        |
| scimark_sor                | 76.2 ms                                                     | 91.3 ms: 1.20x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.29 ms: 1.21x slower                                                       |
| many_optionals             | 361 us                                                      | 440 us: 1.22x slower                                                        |
| django_template            | 20.3 ms                                                     | 25.3 ms: 1.25x slower                                                       |
| raytrace                   | 153 ms                                                      | 197 ms: 1.28x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 16.0 ms: 1.48x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (7): pylint, k_core, connected_components, pathlib, gc_traversal, bench_thread_pool, regex_v8
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20250102-3.14.0a3+-e1baa77/bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77.json: mypy2

- Geometric mean (including insignificant results): 1.013x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown