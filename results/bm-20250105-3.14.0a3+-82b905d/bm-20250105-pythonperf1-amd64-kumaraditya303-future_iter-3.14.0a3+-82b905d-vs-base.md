# Results vs. base

- fork: kumaraditya303
- ref: future_iter
- machine: windows-amd64
- commit hash: 82b905d
- commit date: 2025-01-05
- overall geometric mean: 1.011x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 224 ms                                                                      | 227 ms: 1.01x slower                                                       |
| html5lib       | 40.2 ms                                                                     | 39.4 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (2): docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 172 ms                                                                      | 168 ms: 1.02x faster                                                       |
| async_tree_memoization     | 224 ms                                                                      | 219 ms: 1.02x faster                                                       |
| async_tree_io_tg           | 401 ms                                                                      | 397 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed_tg | 347 ms                                                                      | 343 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed    | 350 ms                                                                      | 347 ms: 1.01x faster                                                       |
| async_generators           | 238 ms                                                                      | 237 ms: 1.01x faster                                                       |
| coroutines                 | 13.4 ms                                                                     | 13.5 ms: 1.01x slower                                                      |
| asyncio_websockets         | 310 ms                                                                      | 314 ms: 1.01x slower                                                       |
| Geometric mean             | (ref)                                                                       | 1.01x faster                                                               |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_io, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 53.0 ms                                                                     | 52.4 ms: 1.01x faster                                                      |
| nbody          | 77.0 ms                                                                     | 78.7 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 127 ms                                                                      | 114 ms: 1.11x faster                                                       |
| regex_effbot   | 1.47 ms                                                                     | 1.45 ms: 1.02x faster                                                      |
| regex_compile  | 87.5 ms                                                                     | 89.2 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 57.4 ms                                                                     | 57.7 ms: 1.01x slower                                                      |
| xml_etree_parse      | 87.5 ms                                                                     | 88.2 ms: 1.01x slower                                                      |
| xml_etree_process    | 40.2 ms                                                                     | 41.2 ms: 1.02x slower                                                      |
| pickle_pure_python   | 221 us                                                                      | 226 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 62.7 ms                                                                     | 64.2 ms: 1.02x slower                                                      |
| json_loads           | 14.5 us                                                                     | 15.0 us: 1.04x slower                                                      |
| tomli_loads          | 1.39 sec                                                                    | 1.44 sec: 1.04x slower                                                     |
| unpickle_pure_python | 148 us                                                                      | 154 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-----------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 16.7 ms                                                                     | 16.5 ms: 1.01x faster                                                      |
| genshi_xml      | 34.6 ms                                                                     | 34.8 ms: 1.01x slower                                                      |
| mako            | 6.87 ms                                                                     | 7.05 ms: 1.03x slower                                                      |
| django_template | 24.8 ms                                                                     | 25.6 ms: 1.03x slower                                                      |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250105-pythonperf1-amd64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------------|:---------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna                  | 127 ms                                                                      | 114 ms: 1.11x faster                                                       |
| async_tree_none_tg         | 172 ms                                                                      | 168 ms: 1.02x faster                                                       |
| logging_format             | 6.89 us                                                                     | 6.74 us: 1.02x faster                                                      |
| async_tree_memoization     | 224 ms                                                                      | 219 ms: 1.02x faster                                                       |
| html5lib                   | 40.2 ms                                                                     | 39.4 ms: 1.02x faster                                                      |
| regex_effbot               | 1.47 ms                                                                     | 1.45 ms: 1.02x faster                                                      |
| pathlib                    | 76.6 ms                                                                     | 75.6 ms: 1.01x faster                                                      |
| genshi_text                | 16.7 ms                                                                     | 16.5 ms: 1.01x faster                                                      |
| float                      | 53.0 ms                                                                     | 52.4 ms: 1.01x faster                                                      |
| spectral_norm              | 64.1 ms                                                                     | 63.4 ms: 1.01x faster                                                      |
| logging_simple             | 6.38 us                                                                     | 6.31 us: 1.01x faster                                                      |
| async_tree_io_tg           | 401 ms                                                                      | 397 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed_tg | 347 ms                                                                      | 343 ms: 1.01x faster                                                       |
| raytrace                   | 193 ms                                                                      | 192 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed    | 350 ms                                                                      | 347 ms: 1.01x faster                                                       |
| async_generators           | 238 ms                                                                      | 237 ms: 1.01x faster                                                       |
| chaos                      | 43.5 ms                                                                     | 43.3 ms: 1.01x faster                                                      |
| xml_etree_generate         | 57.4 ms                                                                     | 57.7 ms: 1.01x slower                                                      |
| genshi_xml                 | 34.6 ms                                                                     | 34.8 ms: 1.01x slower                                                      |
| sqlglot_parse              | 889 us                                                                      | 895 us: 1.01x slower                                                       |
| shortest_path              | 349 ms                                                                      | 351 ms: 1.01x slower                                                       |
| coroutines                 | 13.4 ms                                                                     | 13.5 ms: 1.01x slower                                                      |
| sqlglot_transpile          | 1.11 ms                                                                     | 1.12 ms: 1.01x slower                                                      |
| xml_etree_parse            | 87.5 ms                                                                     | 88.2 ms: 1.01x slower                                                      |
| typing_runtime_protocols   | 112 us                                                                      | 113 us: 1.01x slower                                                       |
| gc_traversal               | 1.96 ms                                                                     | 1.98 ms: 1.01x slower                                                      |
| sympy_sum                  | 90.2 ms                                                                     | 91.0 ms: 1.01x slower                                                      |
| deltablue                  | 2.26 ms                                                                     | 2.28 ms: 1.01x slower                                                      |
| meteor_contest             | 77.0 ms                                                                     | 77.7 ms: 1.01x slower                                                      |
| scimark_monte_carlo        | 47.8 ms                                                                     | 48.3 ms: 1.01x slower                                                      |
| sqlglot_optimize           | 35.9 ms                                                                     | 36.3 ms: 1.01x slower                                                      |
| connected_components       | 316 ms                                                                      | 320 ms: 1.01x slower                                                       |
| sympy_integrate            | 13.4 ms                                                                     | 13.5 ms: 1.01x slower                                                      |
| 2to3                       | 224 ms                                                                      | 227 ms: 1.01x slower                                                       |
| sqlglot_normalize          | 196 ms                                                                      | 199 ms: 1.01x slower                                                       |
| asyncio_websockets         | 310 ms                                                                      | 314 ms: 1.01x slower                                                       |
| sympy_str                  | 177 ms                                                                      | 180 ms: 1.01x slower                                                       |
| deepcopy_reduce            | 1.89 us                                                                     | 1.91 us: 1.01x slower                                                      |
| coverage                   | 46.5 ms                                                                     | 47.2 ms: 1.02x slower                                                      |
| sympy_expand               | 305 ms                                                                      | 310 ms: 1.02x slower                                                       |
| regex_compile              | 87.5 ms                                                                     | 89.2 ms: 1.02x slower                                                      |
| deepcopy_memo              | 20.8 us                                                                     | 21.2 us: 1.02x slower                                                      |
| telco                      | 4.82 ms                                                                     | 4.92 ms: 1.02x slower                                                      |
| nbody                      | 77.0 ms                                                                     | 78.7 ms: 1.02x slower                                                      |
| xml_etree_process          | 40.2 ms                                                                     | 41.2 ms: 1.02x slower                                                      |
| scimark_sor                | 90.3 ms                                                                     | 92.5 ms: 1.02x slower                                                      |
| pickle_pure_python         | 221 us                                                                      | 226 us: 1.02x slower                                                       |
| xml_etree_iterparse        | 62.7 ms                                                                     | 64.2 ms: 1.02x slower                                                      |
| deepcopy                   | 184 us                                                                      | 189 us: 1.02x slower                                                       |
| mako                       | 6.87 ms                                                                     | 7.05 ms: 1.03x slower                                                      |
| many_optionals             | 437 us                                                                      | 449 us: 1.03x slower                                                       |
| django_template            | 24.8 ms                                                                     | 25.6 ms: 1.03x slower                                                      |
| mdp                        | 1.43 sec                                                                    | 1.47 sec: 1.03x slower                                                     |
| json                       | 3.01 ms                                                                     | 3.11 ms: 1.03x slower                                                      |
| go                         | 87.2 ms                                                                     | 90.1 ms: 1.03x slower                                                      |
| crypto_pyaes               | 48.2 ms                                                                     | 49.9 ms: 1.03x slower                                                      |
| json_loads                 | 14.5 us                                                                     | 15.0 us: 1.04x slower                                                      |
| tomli_loads                | 1.39 sec                                                                    | 1.44 sec: 1.04x slower                                                     |
| richards_super             | 34.1 ms                                                                     | 35.4 ms: 1.04x slower                                                      |
| pprint_pformat             | 1.07 sec                                                                    | 1.12 sec: 1.04x slower                                                     |
| thrift                     | 524 us                                                                      | 546 us: 1.04x slower                                                       |
| unpickle_pure_python       | 148 us                                                                      | 154 us: 1.04x slower                                                       |
| pprint_safe_repr           | 531 ms                                                                      | 556 ms: 1.05x slower                                                       |
| scimark_fft                | 193 ms                                                                      | 203 ms: 1.05x slower                                                       |
| richards                   | 29.7 ms                                                                     | 31.3 ms: 1.05x slower                                                      |
| fannkuch                   | 266 ms                                                                      | 280 ms: 1.06x slower                                                       |
| comprehensions             | 11.9 us                                                                     | 12.6 us: 1.06x slower                                                      |
| hexiom                     | 4.27 ms                                                                     | 4.54 ms: 1.06x slower                                                      |
| scimark_sparse_mat_mult    | 2.60 ms                                                                     | 2.77 ms: 1.07x slower                                                      |
| nqueens                    | 62.2 ms                                                                     | 66.4 ms: 1.07x slower                                                      |
| scimark_lu                 | 61.5 ms                                                                     | 66.2 ms: 1.08x slower                                                      |
| logging_silent             | 61.6 ns                                                                     | 66.8 ns: 1.08x slower                                                      |
| Geometric mean             | (ref)                                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (23): regex_v8, pycparser, subparsers, pyflate, python_startup, async_tree_memoization_tg, bench_mp_pool, json_dumps, python_startup_no_site, pylint, bpe_tokeniser, mypy2, create_gc_cycles, pidigits, sqlite_synth, sphinx, dulwich_log, docutils, async_tree_io, async_tree_none, k_core, generators, bench_thread_pool

- Geometric mean (including insignificant results): 1.011x slower

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown