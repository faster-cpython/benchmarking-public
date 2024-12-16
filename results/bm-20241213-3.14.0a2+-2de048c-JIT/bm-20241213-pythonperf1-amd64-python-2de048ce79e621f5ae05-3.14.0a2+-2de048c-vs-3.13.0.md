# Results vs. 3.13.0

- fork: python
- ref: 2de048ce79e621f5ae05
- machine: windows-amd64
- commit hash: 2de048c
- commit date: 2024-12-13
- overall geometric mean: 1.026x faster
- HPT reliability: 52.33%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 219 ms: 1.02x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.71 sec: 1.12x slower                                                      |
| html5lib       | 38.2 ms                                                     | 39.2 ms: 1.03x slower                                                       |
| sphinx         | 617 ms                                                      | 677 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                        |
| async_tree_io              | 513 ms                                                      | 395 ms: 1.30x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                                        |
| async_tree_none            | 219 ms                                                      | 181 ms: 1.21x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 220 ms: 1.20x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 350 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 354 ms: 1.07x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 310 ms: 1.03x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| async_generators           | 223 ms                                                      | 255 ms: 1.15x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 52.8 ms: 1.26x faster                                                       |
| float          | 50.8 ms                                                     | 45.3 ms: 1.12x faster                                                       |
| pidigits       | 146 ms                                                      | 148 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.69 ms                                                     | 1.40 ms: 1.21x faster                                                       |
| regex_dna      | 115 ms                                                      | 113 ms: 1.02x faster                                                        |
| regex_compile  | 80.7 ms                                                     | 81.3 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 130 us                                                      | 110 us: 1.18x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.23 sec: 1.11x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 85.0 ms: 1.08x faster                                                       |
| json_loads           | 15.1 us                                                     | 14.2 us: 1.06x faster                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 50.8 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 58.3 ms: 1.04x faster                                                       |
| pickle_pure_python   | 186 us                                                      | 208 us: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 23.3 ms: 1.05x faster                                                       |
| python_startup_no_site | 16.9 ms                                                     | 17.4 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 5.11 ms: 1.28x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 18.8 ms: 1.23x slower                                                       |
| django_template | 20.3 ms                                                     | 27.5 ms: 1.36x slower                                                       |
| genshi_xml      | 33.9 ms                                                     | 48.5 ms: 1.43x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.17x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 537 us: 15.78x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 16.6 us: 1.39x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 216 ms: 1.30x faster                                                        |
| async_tree_io              | 513 ms                                                      | 395 ms: 1.30x faster                                                        |
| spectral_norm              | 63.4 ms                                                     | 49.1 ms: 1.29x faster                                                       |
| mako                       | 6.56 ms                                                     | 5.11 ms: 1.28x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 391 ms: 1.27x faster                                                        |
| nbody                      | 66.3 ms                                                     | 52.8 ms: 1.26x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 61.2 ms: 1.25x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.11 ms: 1.24x faster                                                       |
| async_tree_none            | 219 ms                                                      | 181 ms: 1.21x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.40 ms: 1.21x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 220 ms: 1.20x faster                                                        |
| scimark_fft                | 175 ms                                                      | 146 ms: 1.20x faster                                                        |
| deepcopy                   | 223 us                                                      | 188 us: 1.19x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 169 ms: 1.18x faster                                                        |
| unpickle_pure_python       | 130 us                                                      | 110 us: 1.18x faster                                                        |
| telco                      | 4.85 ms                                                     | 4.22 ms: 1.15x faster                                                       |
| float                      | 50.8 ms                                                     | 45.3 ms: 1.12x faster                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 40.7 ms: 1.12x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 36.4 ms: 1.12x faster                                                       |
| deepcopy_reduce            | 2.02 us                                                     | 1.81 us: 1.12x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.23 sec: 1.11x faster                                                      |
| json                       | 3.30 ms                                                     | 2.97 ms: 1.11x faster                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 2.61 sec: 1.10x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 350 ms: 1.09x faster                                                        |
| xml_etree_parse            | 92.2 ms                                                     | 85.0 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 354 ms: 1.07x faster                                                        |
| k_core                     | 1.70 sec                                                    | 1.59 sec: 1.07x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.2 us: 1.06x faster                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 50.8 ms: 1.05x faster                                                       |
| python_startup             | 24.4 ms                                                     | 23.3 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 58.3 ms: 1.04x faster                                                       |
| shortest_path              | 355 ms                                                      | 345 ms: 1.03x faster                                                        |
| fannkuch                   | 252 ms                                                      | 244 ms: 1.03x faster                                                        |
| connected_components       | 320 ms                                                      | 311 ms: 1.03x faster                                                        |
| pyflate                    | 283 ms                                                      | 276 ms: 1.02x faster                                                        |
| bench_mp_pool              | 84.2 ms                                                     | 82.3 ms: 1.02x faster                                                       |
| scimark_lu                 | 56.7 ms                                                     | 55.5 ms: 1.02x faster                                                       |
| sqlite_synth               | 1.59 us                                                     | 1.55 us: 1.02x faster                                                       |
| regex_dna                  | 115 ms                                                      | 113 ms: 1.02x faster                                                        |
| regex_compile              | 80.7 ms                                                     | 81.3 ms: 1.01x slower                                                       |
| pidigits                   | 146 ms                                                      | 148 ms: 1.01x slower                                                        |
| pprint_safe_repr           | 485 ms                                                      | 489 ms: 1.01x slower                                                        |
| pathlib                    | 75.3 ms                                                     | 76.2 ms: 1.01x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 988 ms: 1.01x slower                                                        |
| 2to3                       | 215 ms                                                      | 219 ms: 1.02x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 40.9 ms: 1.02x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 39.2 ms: 1.03x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 17.4 ms: 1.03x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 310 ms: 1.03x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 74.5 ms: 1.04x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.49 sec: 1.04x slower                                                      |
| coverage                   | 45.3 ms                                                     | 47.1 ms: 1.04x slower                                                       |
| sympy_str                  | 167 ms                                                      | 176 ms: 1.06x slower                                                        |
| go                         | 84.7 ms                                                     | 90.0 ms: 1.06x slower                                                       |
| sympy_expand               | 286 ms                                                      | 304 ms: 1.07x slower                                                        |
| sympy_sum                  | 85.2 ms                                                     | 90.9 ms: 1.07x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.20 us: 1.07x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.66 us: 1.08x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 838 us: 1.10x slower                                                        |
| sphinx                     | 617 ms                                                      | 677 ms: 1.10x slower                                                        |
| sympy_integrate            | 12.3 ms                                                     | 13.6 ms: 1.10x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 114 us: 1.10x slower                                                        |
| docutils                   | 1.53 sec                                                    | 1.71 sec: 1.12x slower                                                      |
| chaos                      | 37.9 ms                                                     | 42.4 ms: 1.12x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 208 us: 1.12x slower                                                        |
| logging_silent             | 54.6 ns                                                     | 61.7 ns: 1.13x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.09 ms: 1.14x slower                                                       |
| comprehensions             | 10.4 us                                                     | 11.9 us: 1.14x slower                                                       |
| async_generators           | 223 ms                                                      | 255 ms: 1.15x slower                                                        |
| nqueens                    | 56.1 ms                                                     | 64.5 ms: 1.15x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 38.0 ms: 1.17x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 207 ms: 1.20x slower                                                        |
| deltablue                  | 1.89 ms                                                     | 2.29 ms: 1.21x slower                                                       |
| genshi_text                | 15.2 ms                                                     | 18.8 ms: 1.23x slower                                                       |
| generators                 | 19.0 ms                                                     | 23.8 ms: 1.25x slower                                                       |
| many_optionals             | 361 us                                                      | 466 us: 1.29x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 4.97 ms: 1.29x slower                                                       |
| richards_super             | 29.8 ms                                                     | 39.1 ms: 1.31x slower                                                       |
| richards                   | 26.3 ms                                                     | 34.7 ms: 1.32x slower                                                       |
| django_template            | 20.3 ms                                                     | 27.5 ms: 1.36x slower                                                       |
| raytrace                   | 153 ms                                                      | 208 ms: 1.36x slower                                                        |
| genshi_xml                 | 33.9 ms                                                     | 48.5 ms: 1.43x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 15.9 ms: 1.47x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (8): regex_v8, create_gc_cycles, xml_etree_process, json_dumps, gc_traversal, pylint, pycparser, bench_thread_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241213-3.14.0a2+-2de048c-JIT/bm-20241213-pythonperf1-amd64-python-2de048ce79e621f5ae05-3.14.0a2+-2de048c.json: mypy2

- Geometric mean (including insignificant results): 1.026x faster

# HPT report

- Reliability score: 52.33% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown