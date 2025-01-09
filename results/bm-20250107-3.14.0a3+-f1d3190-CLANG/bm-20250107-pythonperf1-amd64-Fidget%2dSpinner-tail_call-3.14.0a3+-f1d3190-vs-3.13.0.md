# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: tail_call
- machine: windows-amd64
- commit hash: f1d3190
- commit date: 2025-01-07
- overall geometric mean: 1.042x faster
- HPT reliability: 66.44%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 225 ms: 1.04x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.71 sec: 1.11x slower                                                     |
| html5lib       | 38.2 ms                                                     | 36.6 ms: 1.04x faster                                                      |
| sphinx         | 617 ms                                                      | 666 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                       | 1.05x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io              | 513 ms                                                      | 363 ms: 1.41x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 203 ms: 1.39x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 364 ms: 1.37x faster                                                       |
| async_tree_none            | 219 ms                                                      | 161 ms: 1.36x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 203 ms: 1.30x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 154 ms: 1.30x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 365 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 369 ms: 1.03x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 12.3 ms: 1.02x faster                                                      |
| async_generators           | 223 ms                                                      | 233 ms: 1.05x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 326 ms: 1.09x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 66.3 ms                                                     | 55.8 ms: 1.19x faster                                                      |
| float          | 50.8 ms                                                     | 45.8 ms: 1.11x faster                                                      |
| pidigits       | 146 ms                                                      | 155 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 80.7 ms                                                     | 77.2 ms: 1.05x faster                                                      |
| regex_effbot   | 1.69 ms                                                     | 1.99 ms: 1.17x slower                                                      |
| regex_dna      | 115 ms                                                      | 139 ms: 1.21x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.15 sec: 1.19x faster                                                     |
| unpickle_pure_python | 130 us                                                      | 126 us: 1.03x faster                                                       |
| pickle_pure_python   | 186 us                                                      | 189 us: 1.02x slower                                                       |
| xml_etree_parse      | 92.2 ms                                                     | 97.9 ms: 1.06x slower                                                      |
| xml_etree_iterparse  | 60.5 ms                                                     | 65.6 ms: 1.08x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 40.9 ms: 1.12x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 61.4 ms: 1.15x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 7.33 ms: 1.18x slower                                                      |
| json_loads           | 15.1 us                                                     | 19.8 us: 1.31x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.5 ms: 1.04x slower                                                      |
| python_startup_no_site | 16.9 ms                                                     | 18.9 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 30.5 ms: 1.11x faster                                                      |
| genshi_text     | 15.2 ms                                                     | 13.8 ms: 1.10x faster                                                      |
| mako            | 6.56 ms                                                     | 7.19 ms: 1.10x slower                                                      |
| django_template | 20.3 ms                                                     | 23.3 ms: 1.15x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf1-amd64-Fidget%2dSpinner-tail_call-3.14.0a3+-f1d3190 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 568 us: 14.90x faster                                                      |
| async_tree_io              | 513 ms                                                      | 363 ms: 1.41x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 203 ms: 1.39x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 16.8 us: 1.38x faster                                                      |
| deepcopy                   | 223 us                                                      | 163 us: 1.37x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 364 ms: 1.37x faster                                                       |
| async_tree_none            | 219 ms                                                      | 161 ms: 1.36x faster                                                       |
| go                         | 84.7 ms                                                     | 64.8 ms: 1.31x faster                                                      |
| async_tree_memoization     | 265 ms                                                      | 203 ms: 1.30x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 154 ms: 1.30x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 60.3 ms: 1.26x faster                                                      |
| generators                 | 19.0 ms                                                     | 15.1 ms: 1.26x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.15 sec: 1.19x faster                                                     |
| nbody                      | 66.3 ms                                                     | 55.8 ms: 1.19x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.73 us: 1.17x faster                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 35.0 ms: 1.16x faster                                                      |
| spectral_norm              | 63.4 ms                                                     | 56.4 ms: 1.13x faster                                                      |
| genshi_xml                 | 33.9 ms                                                     | 30.5 ms: 1.11x faster                                                      |
| float                      | 50.8 ms                                                     | 45.8 ms: 1.11x faster                                                      |
| deltablue                  | 1.89 ms                                                     | 1.71 ms: 1.10x faster                                                      |
| hexiom                     | 3.84 ms                                                     | 3.48 ms: 1.10x faster                                                      |
| genshi_text                | 15.2 ms                                                     | 13.8 ms: 1.10x faster                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.42 ms: 1.07x faster                                                      |
| scimark_fft                | 175 ms                                                      | 164 ms: 1.07x faster                                                       |
| logging_silent             | 54.6 ns                                                     | 51.3 ns: 1.06x faster                                                      |
| scimark_lu                 | 56.7 ms                                                     | 53.4 ms: 1.06x faster                                                      |
| fannkuch                   | 252 ms                                                      | 237 ms: 1.06x faster                                                       |
| sqlglot_parse              | 764 us                                                      | 726 us: 1.05x faster                                                       |
| pylint                     | 205 ms                                                      | 196 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 365 ms: 1.05x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 77.2 ms: 1.05x faster                                                      |
| html5lib                   | 38.2 ms                                                     | 36.6 ms: 1.04x faster                                                      |
| richards                   | 26.3 ms                                                     | 25.3 ms: 1.04x faster                                                      |
| richards_super             | 29.8 ms                                                     | 28.8 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 369 ms: 1.03x faster                                                       |
| unpickle_pure_python       | 130 us                                                      | 126 us: 1.03x faster                                                       |
| pprint_safe_repr           | 485 ms                                                      | 472 ms: 1.03x faster                                                       |
| pprint_pformat             | 977 ms                                                      | 952 ms: 1.03x faster                                                       |
| shortest_path              | 355 ms                                                      | 348 ms: 1.02x faster                                                       |
| coroutines                 | 12.5 ms                                                     | 12.3 ms: 1.02x faster                                                      |
| dulwich_log                | 40.1 ms                                                     | 39.9 ms: 1.01x faster                                                      |
| meteor_contest             | 72.0 ms                                                     | 71.6 ms: 1.01x faster                                                      |
| sqlglot_transpile          | 953 us                                                      | 961 us: 1.01x slower                                                       |
| logging_simple             | 5.77 us                                                     | 5.84 us: 1.01x slower                                                      |
| connected_components       | 320 ms                                                      | 324 ms: 1.01x slower                                                       |
| sympy_str                  | 167 ms                                                      | 169 ms: 1.01x slower                                                       |
| telco                      | 4.85 ms                                                     | 4.92 ms: 1.02x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 189 us: 1.02x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 87.0 ms: 1.02x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 57.4 ms: 1.02x slower                                                      |
| logging_format             | 6.18 us                                                     | 6.33 us: 1.02x slower                                                      |
| sympy_expand               | 286 ms                                                      | 293 ms: 1.03x slower                                                       |
| bench_thread_pool          | 810 us                                                      | 840 us: 1.04x slower                                                       |
| typing_runtime_protocols   | 103 us                                                      | 107 us: 1.04x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.9 ms: 1.04x slower                                                      |
| sqlglot_optimize           | 32.5 ms                                                     | 33.9 ms: 1.04x slower                                                      |
| python_startup             | 24.4 ms                                                     | 25.5 ms: 1.04x slower                                                      |
| 2to3                       | 215 ms                                                      | 225 ms: 1.04x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 47.7 ms: 1.05x slower                                                      |
| comprehensions             | 10.4 us                                                     | 10.8 us: 1.05x slower                                                      |
| async_generators           | 223 ms                                                      | 233 ms: 1.05x slower                                                       |
| raytrace                   | 153 ms                                                      | 162 ms: 1.05x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.03 sec: 1.05x slower                                                     |
| sqlglot_normalize          | 172 ms                                                      | 181 ms: 1.06x slower                                                       |
| pidigits                   | 146 ms                                                      | 155 ms: 1.06x slower                                                       |
| pathlib                    | 75.3 ms                                                     | 79.5 ms: 1.06x slower                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 97.9 ms: 1.06x slower                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.69 us: 1.07x slower                                                      |
| sphinx                     | 617 ms                                                      | 666 ms: 1.08x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 65.6 ms: 1.08x slower                                                      |
| asyncio_websockets         | 300 ms                                                      | 326 ms: 1.09x slower                                                       |
| json                       | 3.30 ms                                                     | 3.58 ms: 1.09x slower                                                      |
| mako                       | 6.56 ms                                                     | 7.19 ms: 1.10x slower                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 93.3 ms: 1.11x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.71 sec: 1.11x slower                                                     |
| coverage                   | 45.3 ms                                                     | 50.5 ms: 1.11x slower                                                      |
| python_startup_no_site     | 16.9 ms                                                     | 18.9 ms: 1.12x slower                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.37 ms: 1.12x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 40.9 ms: 1.12x slower                                                      |
| mdp                        | 1.43 sec                                                    | 1.62 sec: 1.13x slower                                                     |
| xml_etree_generate         | 53.5 ms                                                     | 61.4 ms: 1.15x slower                                                      |
| django_template            | 20.3 ms                                                     | 23.3 ms: 1.15x slower                                                      |
| regex_effbot               | 1.69 ms                                                     | 1.99 ms: 1.17x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 7.33 ms: 1.18x slower                                                      |
| many_optionals             | 361 us                                                      | 436 us: 1.21x slower                                                       |
| regex_dna                  | 115 ms                                                      | 139 ms: 1.21x slower                                                       |
| json_loads                 | 15.1 us                                                     | 19.8 us: 1.31x slower                                                      |
| gc_traversal               | 1.96 ms                                                     | 2.85 ms: 1.45x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 15.8 ms: 1.46x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (5): pycparser, pyflate, k_core, regex_v8, chaos
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 66.44% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown