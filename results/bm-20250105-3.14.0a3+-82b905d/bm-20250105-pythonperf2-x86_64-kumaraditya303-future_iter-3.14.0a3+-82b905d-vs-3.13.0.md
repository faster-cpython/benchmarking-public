# Results vs. 3.13.0

- fork: kumaraditya303
- ref: future_iter
- machine: linux-x86_64
- commit hash: 82b905d
- commit date: 2025-01-05
- overall geometric mean: 1.064x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 280 ms: 1.04x faster                                                        |
| docutils       | 2.83 sec                                                     | 2.87 sec: 1.02x slower                                                      |
| html5lib       | 73.5 ms                                                      | 66.8 ms: 1.10x faster                                                       |
| sphinx         | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                      |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 320 ms: 1.46x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 604 ms: 1.38x faster                                                        |
| async_tree_io              | 843 ms                                                       | 618 ms: 1.36x faster                                                        |
| async_tree_none            | 376 ms                                                       | 282 ms: 1.34x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 262 ms: 1.32x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 346 ms: 1.31x faster                                                        |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 489 ms: 1.19x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 512 ms: 1.18x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 20.6 ms: 1.05x faster                                                       |
| async_generators           | 457 ms                                                       | 437 ms: 1.05x faster                                                        |
| Geometric mean             | (ref)                                                        | 1.23x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 71.8 ms: 1.13x faster                                                       |
| nbody          | 89.3 ms                                                      | 86.2 ms: 1.04x faster                                                       |
| pidigits       | 252 ms                                                       | 255 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.25 ms: 1.13x faster                                                       |
| regex_compile  | 143 ms                                                       | 134 ms: 1.06x faster                                                        |
| regex_dna      | 247 ms                                                       | 245 ms: 1.01x faster                                                        |
| regex_v8       | 26.1 ms                                                      | 26.8 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                                      |
| xml_etree_parse      | 150 ms                                                       | 134 ms: 1.12x faster                                                        |
| unpickle_pure_python | 217 us                                                       | 201 us: 1.08x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                       | 95.4 ms: 1.08x faster                                                       |
| xml_etree_process    | 61.2 ms                                                      | 58.7 ms: 1.04x faster                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 83.2 ms: 1.04x faster                                                       |
| pickle_pure_python   | 323 us                                                       | 326 us: 1.01x slower                                                        |
| json_dumps           | 11.1 ms                                                      | 11.4 ms: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 9.02 ms: 1.01x slower                                                       |
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.2 ms                                                      | 23.9 ms: 1.10x faster                                                       |
| genshi_xml      | 57.1 ms                                                      | 52.5 ms: 1.09x faster                                                       |
| django_template | 36.4 ms                                                      | 35.1 ms: 1.03x faster                                                       |
| mako            | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.04x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 320 ms: 1.46x faster                                                        |
| deepcopy                   | 392 us                                                       | 282 us: 1.39x faster                                                        |
| async_tree_io_tg           | 831 ms                                                       | 604 ms: 1.38x faster                                                        |
| async_tree_io              | 843 ms                                                       | 618 ms: 1.36x faster                                                        |
| async_tree_none            | 376 ms                                                       | 282 ms: 1.34x faster                                                        |
| async_tree_none_tg         | 346 ms                                                       | 262 ms: 1.32x faster                                                        |
| async_tree_memoization     | 453 ms                                                       | 346 ms: 1.31x faster                                                        |
| go                         | 162 ms                                                       | 126 ms: 1.28x faster                                                        |
| deepcopy_memo              | 38.6 us                                                      | 30.7 us: 1.26x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.91 us: 1.22x faster                                                       |
| tomli_loads                | 2.46 sec                                                     | 2.05 sec: 1.20x faster                                                      |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 489 ms: 1.19x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 512 ms: 1.18x faster                                                        |
| generators                 | 33.6 ms                                                      | 28.6 ms: 1.18x faster                                                       |
| richards_super             | 59.6 ms                                                      | 52.2 ms: 1.14x faster                                                       |
| richards                   | 52.9 ms                                                      | 46.6 ms: 1.14x faster                                                       |
| float                      | 81.3 ms                                                      | 71.8 ms: 1.13x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.25 ms: 1.13x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 134 ms: 1.12x faster                                                        |
| json                       | 5.69 ms                                                      | 5.07 ms: 1.12x faster                                                       |
| telco                      | 8.79 ms                                                      | 7.84 ms: 1.12x faster                                                       |
| pyflate                    | 503 ms                                                       | 451 ms: 1.12x faster                                                        |
| scimark_sor                | 123 ms                                                       | 110 ms: 1.12x faster                                                        |
| pprint_pformat             | 1.72 sec                                                     | 1.55 sec: 1.11x faster                                                      |
| spectral_norm              | 97.0 ms                                                      | 87.7 ms: 1.11x faster                                                       |
| pathlib                    | 17.5 ms                                                      | 15.9 ms: 1.10x faster                                                       |
| pylint                     | 347 ms                                                       | 315 ms: 1.10x faster                                                        |
| html5lib                   | 73.5 ms                                                      | 66.8 ms: 1.10x faster                                                       |
| pprint_safe_repr           | 843 ms                                                       | 767 ms: 1.10x faster                                                        |
| genshi_text                | 26.2 ms                                                      | 23.9 ms: 1.10x faster                                                       |
| genshi_xml                 | 57.1 ms                                                      | 52.5 ms: 1.09x faster                                                       |
| scimark_fft                | 328 ms                                                       | 302 ms: 1.09x faster                                                        |
| unpickle_pure_python       | 217 us                                                       | 201 us: 1.08x faster                                                        |
| hexiom                     | 6.55 ms                                                      | 6.08 ms: 1.08x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                       | 95.4 ms: 1.08x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.76 sec: 1.07x faster                                                      |
| regex_compile              | 143 ms                                                       | 134 ms: 1.06x faster                                                        |
| sqlglot_parse              | 1.40 ms                                                      | 1.32 ms: 1.06x faster                                                       |
| thrift                     | 901 us                                                       | 854 us: 1.05x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 20.6 ms: 1.05x faster                                                       |
| sqlglot_normalize          | 119 ms                                                       | 114 ms: 1.05x faster                                                        |
| async_generators           | 457 ms                                                       | 437 ms: 1.05x faster                                                        |
| 2to3                       | 293 ms                                                       | 280 ms: 1.04x faster                                                        |
| sqlglot_transpile          | 1.79 ms                                                      | 1.72 ms: 1.04x faster                                                       |
| xml_etree_process          | 61.2 ms                                                      | 58.7 ms: 1.04x faster                                                       |
| shortest_path              | 460 ms                                                       | 442 ms: 1.04x faster                                                        |
| scimark_lu                 | 98.7 ms                                                      | 94.8 ms: 1.04x faster                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 83.2 ms: 1.04x faster                                                       |
| sqlalchemy_declarative     | 148 ms                                                       | 143 ms: 1.04x faster                                                        |
| k_core                     | 2.17 sec                                                     | 2.09 sec: 1.04x faster                                                      |
| scimark_monte_carlo        | 66.1 ms                                                      | 63.8 ms: 1.04x faster                                                       |
| nbody                      | 89.3 ms                                                      | 86.2 ms: 1.04x faster                                                       |
| django_template            | 36.4 ms                                                      | 35.1 ms: 1.03x faster                                                       |
| coverage                   | 80.0 ms                                                      | 77.3 ms: 1.03x faster                                                       |
| connected_components       | 432 ms                                                       | 419 ms: 1.03x faster                                                        |
| sympy_integrate            | 23.6 ms                                                      | 22.8 ms: 1.03x faster                                                       |
| sqlglot_optimize           | 59.3 ms                                                      | 57.5 ms: 1.03x faster                                                       |
| sympy_sum                  | 155 ms                                                       | 150 ms: 1.03x faster                                                        |
| sympy_str                  | 298 ms                                                       | 290 ms: 1.03x faster                                                        |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.64 ms: 1.03x faster                                                       |
| dulwich_log                | 68.2 ms                                                      | 66.3 ms: 1.03x faster                                                       |
| mdp                        | 2.54 sec                                                     | 2.48 sec: 1.02x faster                                                      |
| sqlite_synth               | 2.91 us                                                      | 2.84 us: 1.02x faster                                                       |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.9 ms: 1.02x faster                                                       |
| sympy_expand               | 509 ms                                                       | 499 ms: 1.02x faster                                                        |
| sphinx                     | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                      |
| raytrace                   | 273 ms                                                       | 268 ms: 1.02x faster                                                        |
| meteor_contest             | 130 ms                                                       | 127 ms: 1.02x faster                                                        |
| pycparser                  | 1.24 sec                                                     | 1.23 sec: 1.01x faster                                                      |
| deltablue                  | 3.42 ms                                                      | 3.39 ms: 1.01x faster                                                       |
| regex_dna                  | 247 ms                                                       | 245 ms: 1.01x faster                                                        |
| python_startup_no_site     | 8.96 ms                                                      | 9.02 ms: 1.01x slower                                                       |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                       |
| crypto_pyaes               | 73.3 ms                                                      | 73.9 ms: 1.01x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 326 us: 1.01x slower                                                        |
| pidigits                   | 252 ms                                                       | 255 ms: 1.01x slower                                                        |
| typing_runtime_protocols   | 169 us                                                       | 171 us: 1.01x slower                                                        |
| chaos                      | 60.2 ms                                                      | 60.9 ms: 1.01x slower                                                       |
| docutils                   | 2.83 sec                                                     | 2.87 sec: 1.02x slower                                                      |
| json_dumps                 | 11.1 ms                                                      | 11.4 ms: 1.02x slower                                                       |
| regex_v8                   | 26.1 ms                                                      | 26.8 ms: 1.02x slower                                                       |
| fannkuch                   | 363 ms                                                       | 373 ms: 1.03x slower                                                        |
| create_gc_cycles           | 2.68 ms                                                      | 2.79 ms: 1.04x slower                                                       |
| comprehensions             | 17.0 us                                                      | 17.7 us: 1.04x slower                                                       |
| mako                       | 10.4 ms                                                      | 10.9 ms: 1.05x slower                                                       |
| many_optionals             | 930 us                                                       | 1.01 ms: 1.09x slower                                                       |
| subparsers                 | 17.5 ms                                                      | 22.7 ms: 1.30x slower                                                       |
| gc_traversal               | 4.74 ms                                                      | 6.63 ms: 1.40x slower                                                       |
| bench_mp_pool              | 5.12 ms                                                      | 891 ms: 173.90x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (7): bench_thread_pool, asyncio_websockets, logging_simple, json_loads, logging_format, nqueens, logging_silent
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250105-3.14.0a3+-82b905d/bm-20250105-pythonperf2-x86_64-kumaraditya303-future_iter-3.14.0a3+-82b905d.json: mypy2

- Geometric mean (including insignificant results): 1.064x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.02x