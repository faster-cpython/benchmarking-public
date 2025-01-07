# Results vs. 3.13.0

- fork: kumaraditya303
- ref: fast_state
- machine: linux-x86_64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.068x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 279 ms: 1.05x faster                                                       |
| docutils       | 2.83 sec                                                     | 2.87 sec: 1.01x slower                                                     |
| html5lib       | 73.5 ms                                                      | 67.2 ms: 1.09x faster                                                      |
| sphinx         | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                     |
| Geometric mean | (ref)                                                        | 1.04x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 318 ms: 1.46x faster                                                       |
| async_tree_io_tg           | 831 ms                                                       | 606 ms: 1.37x faster                                                       |
| async_tree_io              | 843 ms                                                       | 618 ms: 1.36x faster                                                       |
| async_tree_none            | 376 ms                                                       | 282 ms: 1.33x faster                                                       |
| async_tree_none_tg         | 346 ms                                                       | 262 ms: 1.32x faster                                                       |
| async_tree_memoization     | 453 ms                                                       | 345 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 487 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 511 ms: 1.18x faster                                                       |
| async_generators           | 457 ms                                                       | 430 ms: 1.06x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 20.9 ms: 1.03x faster                                                      |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                       |
| Geometric mean             | (ref)                                                        | 1.23x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 81.3 ms                                                      | 72.3 ms: 1.13x faster                                                      |
| nbody          | 89.3 ms                                                      | 86.6 ms: 1.03x faster                                                      |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                      | 3.19 ms: 1.15x faster                                                      |
| regex_dna      | 247 ms                                                       | 231 ms: 1.07x faster                                                       |
| regex_compile  | 143 ms                                                       | 134 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.46 sec                                                     | 2.03 sec: 1.21x faster                                                     |
| xml_etree_parse      | 150 ms                                                       | 137 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 95.1 ms: 1.08x faster                                                      |
| unpickle_pure_python | 217 us                                                       | 206 us: 1.06x faster                                                       |
| xml_etree_generate   | 86.5 ms                                                      | 82.2 ms: 1.05x faster                                                      |
| xml_etree_process    | 61.2 ms                                                      | 58.6 ms: 1.04x faster                                                      |
| json_loads           | 24.7 us                                                      | 24.2 us: 1.02x faster                                                      |
| pickle_pure_python   | 323 us                                                       | 326 us: 1.01x slower                                                       |
| json_dumps           | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 8.96 ms                                                      | 8.98 ms: 1.00x slower                                                      |
| python_startup         | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text    | 26.2 ms                                                      | 24.0 ms: 1.09x faster                                                      |
| genshi_xml     | 57.1 ms                                                      | 54.4 ms: 1.05x faster                                                      |
| mako           | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                        | 1.02x faster                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 466 ms                                                       | 318 ms: 1.46x faster                                                       |
| deepcopy                   | 392 us                                                       | 280 us: 1.40x faster                                                       |
| async_tree_io_tg           | 831 ms                                                       | 606 ms: 1.37x faster                                                       |
| async_tree_io              | 843 ms                                                       | 618 ms: 1.36x faster                                                       |
| async_tree_none            | 376 ms                                                       | 282 ms: 1.33x faster                                                       |
| async_tree_none_tg         | 346 ms                                                       | 262 ms: 1.32x faster                                                       |
| async_tree_memoization     | 453 ms                                                       | 345 ms: 1.31x faster                                                       |
| deepcopy_memo              | 38.6 us                                                      | 29.6 us: 1.30x faster                                                      |
| go                         | 162 ms                                                       | 129 ms: 1.26x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.91 us: 1.22x faster                                                      |
| tomli_loads                | 2.46 sec                                                     | 2.03 sec: 1.21x faster                                                     |
| generators                 | 33.6 ms                                                      | 28.1 ms: 1.20x faster                                                      |
| async_tree_cpu_io_mixed_tg | 581 ms                                                       | 487 ms: 1.20x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                       | 511 ms: 1.18x faster                                                       |
| regex_effbot               | 3.67 ms                                                      | 3.19 ms: 1.15x faster                                                      |
| pyflate                    | 503 ms                                                       | 440 ms: 1.14x faster                                                       |
| richards                   | 52.9 ms                                                      | 46.3 ms: 1.14x faster                                                      |
| richards_super             | 59.6 ms                                                      | 52.3 ms: 1.14x faster                                                      |
| telco                      | 8.79 ms                                                      | 7.75 ms: 1.13x faster                                                      |
| float                      | 81.3 ms                                                      | 72.3 ms: 1.13x faster                                                      |
| json                       | 5.69 ms                                                      | 5.10 ms: 1.11x faster                                                      |
| spectral_norm              | 97.0 ms                                                      | 87.4 ms: 1.11x faster                                                      |
| pathlib                    | 17.5 ms                                                      | 15.9 ms: 1.10x faster                                                      |
| pprint_pformat             | 1.72 sec                                                     | 1.56 sec: 1.10x faster                                                     |
| scimark_fft                | 328 ms                                                       | 298 ms: 1.10x faster                                                       |
| scimark_sor                | 123 ms                                                       | 112 ms: 1.10x faster                                                       |
| xml_etree_parse            | 150 ms                                                       | 137 ms: 1.10x faster                                                       |
| pprint_safe_repr           | 843 ms                                                       | 768 ms: 1.10x faster                                                       |
| html5lib                   | 73.5 ms                                                      | 67.2 ms: 1.09x faster                                                      |
| genshi_text                | 26.2 ms                                                      | 24.0 ms: 1.09x faster                                                      |
| pylint                     | 347 ms                                                       | 318 ms: 1.09x faster                                                       |
| hexiom                     | 6.55 ms                                                      | 6.04 ms: 1.09x faster                                                      |
| xml_etree_iterparse        | 103 ms                                                       | 95.1 ms: 1.08x faster                                                      |
| bpe_tokeniser              | 5.09 sec                                                     | 4.71 sec: 1.08x faster                                                     |
| regex_dna                  | 247 ms                                                       | 231 ms: 1.07x faster                                                       |
| regex_compile              | 143 ms                                                       | 134 ms: 1.07x faster                                                       |
| async_generators           | 457 ms                                                       | 430 ms: 1.06x faster                                                       |
| sqlglot_parse              | 1.40 ms                                                      | 1.32 ms: 1.06x faster                                                      |
| unpickle_pure_python       | 217 us                                                       | 206 us: 1.06x faster                                                       |
| scimark_sparse_mat_mult    | 4.77 ms                                                      | 4.52 ms: 1.06x faster                                                      |
| sqlglot_normalize          | 119 ms                                                       | 113 ms: 1.05x faster                                                       |
| xml_etree_generate         | 86.5 ms                                                      | 82.2 ms: 1.05x faster                                                      |
| 2to3                       | 293 ms                                                       | 279 ms: 1.05x faster                                                       |
| genshi_xml                 | 57.1 ms                                                      | 54.4 ms: 1.05x faster                                                      |
| sqlglot_transpile          | 1.79 ms                                                      | 1.71 ms: 1.04x faster                                                      |
| coverage                   | 80.0 ms                                                      | 76.7 ms: 1.04x faster                                                      |
| xml_etree_process          | 61.2 ms                                                      | 58.6 ms: 1.04x faster                                                      |
| scimark_monte_carlo        | 66.1 ms                                                      | 63.5 ms: 1.04x faster                                                      |
| thrift                     | 901 us                                                       | 866 us: 1.04x faster                                                       |
| connected_components       | 432 ms                                                       | 417 ms: 1.04x faster                                                       |
| sqlglot_optimize           | 59.3 ms                                                      | 57.3 ms: 1.03x faster                                                      |
| shortest_path              | 460 ms                                                       | 445 ms: 1.03x faster                                                       |
| meteor_contest             | 130 ms                                                       | 126 ms: 1.03x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 20.9 ms: 1.03x faster                                                      |
| nbody                      | 89.3 ms                                                      | 86.6 ms: 1.03x faster                                                      |
| mdp                        | 2.54 sec                                                     | 2.46 sec: 1.03x faster                                                     |
| logging_simple             | 6.39 us                                                      | 6.20 us: 1.03x faster                                                      |
| sqlalchemy_declarative     | 148 ms                                                       | 144 ms: 1.03x faster                                                       |
| scimark_lu                 | 98.7 ms                                                      | 95.8 ms: 1.03x faster                                                      |
| dulwich_log                | 68.2 ms                                                      | 66.2 ms: 1.03x faster                                                      |
| k_core                     | 2.17 sec                                                     | 2.11 sec: 1.03x faster                                                     |
| sympy_str                  | 298 ms                                                       | 290 ms: 1.03x faster                                                       |
| sympy_sum                  | 155 ms                                                       | 151 ms: 1.03x faster                                                       |
| sympy_integrate            | 23.6 ms                                                      | 23.0 ms: 1.03x faster                                                      |
| sqlite_synth               | 2.91 us                                                      | 2.83 us: 1.03x faster                                                      |
| sqlalchemy_imperative      | 18.3 ms                                                      | 17.8 ms: 1.02x faster                                                      |
| raytrace                   | 273 ms                                                       | 266 ms: 1.02x faster                                                       |
| fannkuch                   | 363 ms                                                       | 355 ms: 1.02x faster                                                       |
| sphinx                     | 1.12 sec                                                     | 1.10 sec: 1.02x faster                                                     |
| sympy_expand               | 509 ms                                                       | 499 ms: 1.02x faster                                                       |
| json_loads                 | 24.7 us                                                      | 24.2 us: 1.02x faster                                                      |
| pycparser                  | 1.24 sec                                                     | 1.22 sec: 1.02x faster                                                     |
| nqueens                    | 90.7 ms                                                      | 89.5 ms: 1.01x faster                                                      |
| asyncio_websockets         | 388 ms                                                       | 384 ms: 1.01x faster                                                       |
| logging_format             | 6.94 us                                                      | 6.89 us: 1.01x faster                                                      |
| python_startup_no_site     | 8.96 ms                                                      | 8.98 ms: 1.00x slower                                                      |
| python_startup             | 15.9 ms                                                      | 16.0 ms: 1.01x slower                                                      |
| pidigits                   | 252 ms                                                       | 254 ms: 1.01x slower                                                       |
| pickle_pure_python         | 323 us                                                       | 326 us: 1.01x slower                                                       |
| docutils                   | 2.83 sec                                                     | 2.87 sec: 1.01x slower                                                     |
| logging_silent             | 97.9 ns                                                      | 99.4 ns: 1.02x slower                                                      |
| typing_runtime_protocols   | 169 us                                                       | 173 us: 1.02x slower                                                       |
| create_gc_cycles           | 2.68 ms                                                      | 2.75 ms: 1.03x slower                                                      |
| json_dumps                 | 11.1 ms                                                      | 11.5 ms: 1.03x slower                                                      |
| chaos                      | 60.2 ms                                                      | 62.3 ms: 1.03x slower                                                      |
| comprehensions             | 17.0 us                                                      | 17.7 us: 1.04x slower                                                      |
| mako                       | 10.4 ms                                                      | 11.0 ms: 1.06x slower                                                      |
| many_optionals             | 930 us                                                       | 1.02 ms: 1.09x slower                                                      |
| gc_traversal               | 4.74 ms                                                      | 6.15 ms: 1.30x slower                                                      |
| subparsers                 | 17.5 ms                                                      | 22.8 ms: 1.30x slower                                                      |
| bench_mp_pool              | 5.12 ms                                                      | 1.31 sec: 256.54x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                               |

Benchmark hidden because not significant (5): bench_thread_pool, django_template, crypto_pyaes, deltablue, regex_v8
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250107-3.14.0a3+-7de6e22/bm-20250107-pythonperf2-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: mypy2

- Geometric mean (including insignificant results): 1.068x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.02x