# Results vs. 3.13.0

- fork: kumaraditya303
- ref: future_iter
- machine: windows-amd64
- commit hash: 82b905d
- commit date: 2025-01-05
- overall geometric mean: 1.023x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 227 ms: 1.05x slower                                                       |
| docutils       | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                     |
| html5lib       | 38.2 ms                                                     | 39.4 ms: 1.03x slower                                                      |
| sphinx         | 617 ms                                                      | 650 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| async_tree_io              | 513 ms                                                      | 405 ms: 1.27x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 397 ms: 1.25x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 219 ms: 1.21x faster                                                       |
| async_tree_none            | 219 ms                                                      | 182 ms: 1.20x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 347 ms: 1.09x faster                                                       |
| asyncio_websockets         | 300 ms                                                      | 314 ms: 1.05x slower                                                       |
| async_generators           | 223 ms                                                      | 237 ms: 1.06x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 52.4 ms: 1.03x slower                                                      |
| nbody          | 66.3 ms                                                     | 78.7 ms: 1.19x slower                                                      |
| Geometric mean | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                      |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 89.2 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 92.2 ms                                                     | 88.2 ms: 1.04x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                     |
| xml_etree_iterparse  | 60.5 ms                                                     | 64.2 ms: 1.06x slower                                                      |
| xml_etree_generate   | 53.5 ms                                                     | 57.7 ms: 1.08x slower                                                      |
| json_dumps           | 6.19 ms                                                     | 6.68 ms: 1.08x slower                                                      |
| xml_etree_process    | 36.5 ms                                                     | 41.2 ms: 1.13x slower                                                      |
| unpickle_pure_python | 130 us                                                      | 154 us: 1.19x slower                                                       |
| pickle_pure_python   | 186 us                                                      | 226 us: 1.22x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 23.0 ms: 1.06x faster                                                      |
| python_startup_no_site | 16.9 ms                                                     | 17.2 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.56 ms                                                     | 7.05 ms: 1.07x slower                                                      |
| genshi_text     | 15.2 ms                                                     | 16.5 ms: 1.08x slower                                                      |
| django_template | 20.3 ms                                                     | 25.6 ms: 1.26x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                               |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 546 us: 15.50x faster                                                      |
| async_tree_memoization_tg  | 281 ms                                                      | 210 ms: 1.34x faster                                                       |
| async_tree_io              | 513 ms                                                      | 405 ms: 1.27x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 397 ms: 1.25x faster                                                       |
| async_tree_memoization     | 265 ms                                                      | 219 ms: 1.21x faster                                                       |
| async_tree_none            | 219 ms                                                      | 182 ms: 1.20x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                       |
| deepcopy                   | 223 us                                                      | 189 us: 1.19x faster                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.45 ms: 1.17x faster                                                      |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 343 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 347 ms: 1.09x faster                                                       |
| deepcopy_memo              | 23.1 us                                                     | 21.2 us: 1.09x faster                                                      |
| json                       | 3.30 ms                                                     | 3.11 ms: 1.06x faster                                                      |
| python_startup             | 24.4 ms                                                     | 23.0 ms: 1.06x faster                                                      |
| deepcopy_reduce            | 2.02 us                                                     | 1.91 us: 1.06x faster                                                      |
| xml_etree_parse            | 92.2 ms                                                     | 88.2 ms: 1.04x faster                                                      |
| bench_mp_pool              | 84.2 ms                                                     | 82.4 ms: 1.02x faster                                                      |
| create_gc_cycles           | 1.22 ms                                                     | 1.21 ms: 1.01x faster                                                      |
| shortest_path              | 355 ms                                                      | 351 ms: 1.01x faster                                                       |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 17.2 ms: 1.01x slower                                                      |
| telco                      | 4.85 ms                                                     | 4.92 ms: 1.01x slower                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.61 us: 1.02x slower                                                      |
| mdp                        | 1.43 sec                                                    | 1.47 sec: 1.03x slower                                                     |
| float                      | 50.8 ms                                                     | 52.4 ms: 1.03x slower                                                      |
| html5lib                   | 38.2 ms                                                     | 39.4 ms: 1.03x slower                                                      |
| coverage                   | 45.3 ms                                                     | 47.2 ms: 1.04x slower                                                      |
| asyncio_websockets         | 300 ms                                                      | 314 ms: 1.05x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.02 sec: 1.05x slower                                                     |
| sphinx                     | 617 ms                                                      | 650 ms: 1.05x slower                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                     |
| 2to3                       | 215 ms                                                      | 227 ms: 1.05x slower                                                       |
| pycparser                  | 695 ms                                                      | 733 ms: 1.05x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 64.2 ms: 1.06x slower                                                      |
| go                         | 84.7 ms                                                     | 90.1 ms: 1.06x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.77 ms: 1.06x slower                                                      |
| async_generators           | 223 ms                                                      | 237 ms: 1.06x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 42.8 ms: 1.07x slower                                                      |
| sympy_sum                  | 85.2 ms                                                     | 91.0 ms: 1.07x slower                                                      |
| mako                       | 6.56 ms                                                     | 7.05 ms: 1.07x slower                                                      |
| sympy_str                  | 167 ms                                                      | 180 ms: 1.08x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 57.7 ms: 1.08x slower                                                      |
| coroutines                 | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                      |
| json_dumps                 | 6.19 ms                                                     | 6.68 ms: 1.08x slower                                                      |
| meteor_contest             | 72.0 ms                                                     | 77.7 ms: 1.08x slower                                                      |
| genshi_text                | 15.2 ms                                                     | 16.5 ms: 1.08x slower                                                      |
| sympy_expand               | 286 ms                                                      | 310 ms: 1.09x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.74 us: 1.09x slower                                                      |
| docutils                   | 1.53 sec                                                    | 1.67 sec: 1.09x slower                                                     |
| logging_simple             | 5.77 us                                                     | 6.31 us: 1.09x slower                                                      |
| crypto_pyaes               | 45.6 ms                                                     | 49.9 ms: 1.09x slower                                                      |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.10x slower                                                      |
| typing_runtime_protocols   | 103 us                                                      | 113 us: 1.10x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 89.2 ms: 1.11x slower                                                      |
| fannkuch                   | 252 ms                                                      | 280 ms: 1.11x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 36.3 ms: 1.12x slower                                                      |
| generators                 | 19.0 ms                                                     | 21.3 ms: 1.12x slower                                                      |
| xml_etree_process          | 36.5 ms                                                     | 41.2 ms: 1.13x slower                                                      |
| pyflate                    | 283 ms                                                      | 323 ms: 1.14x slower                                                       |
| chaos                      | 37.9 ms                                                     | 43.3 ms: 1.14x slower                                                      |
| pprint_pformat             | 977 ms                                                      | 1.12 sec: 1.14x slower                                                     |
| pprint_safe_repr           | 485 ms                                                      | 556 ms: 1.15x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 199 ms: 1.16x slower                                                       |
| scimark_fft                | 175 ms                                                      | 203 ms: 1.16x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 66.2 ms: 1.17x slower                                                      |
| sqlglot_parse              | 764 us                                                      | 895 us: 1.17x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.12 ms: 1.17x slower                                                      |
| hexiom                     | 3.84 ms                                                     | 4.54 ms: 1.18x slower                                                      |
| nqueens                    | 56.1 ms                                                     | 66.4 ms: 1.18x slower                                                      |
| scimark_monte_carlo        | 40.7 ms                                                     | 48.3 ms: 1.19x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 154 us: 1.19x slower                                                       |
| nbody                      | 66.3 ms                                                     | 78.7 ms: 1.19x slower                                                      |
| richards_super             | 29.8 ms                                                     | 35.4 ms: 1.19x slower                                                      |
| richards                   | 26.3 ms                                                     | 31.3 ms: 1.19x slower                                                      |
| deltablue                  | 1.89 ms                                                     | 2.28 ms: 1.20x slower                                                      |
| scimark_sor                | 76.2 ms                                                     | 92.5 ms: 1.21x slower                                                      |
| comprehensions             | 10.4 us                                                     | 12.6 us: 1.21x slower                                                      |
| pickle_pure_python         | 186 us                                                      | 226 us: 1.22x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 66.8 ns: 1.22x slower                                                      |
| many_optionals             | 361 us                                                      | 449 us: 1.24x slower                                                       |
| raytrace                   | 153 ms                                                      | 192 ms: 1.25x slower                                                       |
| django_template            | 20.3 ms                                                     | 25.6 ms: 1.26x slower                                                      |
| subparsers                 | 10.9 ms                                                     | 16.1 ms: 1.48x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (11): regex_v8, pylint, k_core, json_loads, spectral_norm, pidigits, connected_components, pathlib, gc_traversal, bench_thread_pool, genshi_xml
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20250105-3.14.0a3+-82b905d/bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d.json: mypy2

- Geometric mean (including insignificant results): 1.023x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown