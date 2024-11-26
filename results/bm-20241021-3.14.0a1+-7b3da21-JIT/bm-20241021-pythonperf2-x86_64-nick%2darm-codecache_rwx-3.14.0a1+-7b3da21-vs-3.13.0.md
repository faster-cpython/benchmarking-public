# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.008x slower
- HPT reliability: 62.63%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 313 ms: 1.07x slower                                                      |
| docutils       | 2.81 sec                                                     | 3.16 sec: 1.13x slower                                                    |
| html5lib       | 72.9 ms                                                      | 70.7 ms: 1.03x faster                                                     |
| sphinx         | 1.11 sec                                                     | 1.24 sec: 1.12x slower                                                    |
| tornado_http   | 119 ms                                                       | 123 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                        | 1.06x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 373 ms: 1.23x faster                                                      |
| async_tree_memoization     | 447 ms                                                       | 410 ms: 1.09x faster                                                      |
| async_tree_none            | 370 ms                                                       | 342 ms: 1.08x faster                                                      |
| async_tree_none_tg         | 342 ms                                                       | 322 ms: 1.06x faster                                                      |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 576 ms: 1.03x faster                                                      |
| asyncio_websockets         | 395 ms                                                       | 383 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                      |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                     |
| async_tree_io              | 832 ms                                                       | 844 ms: 1.02x slower                                                      |
| async_generators           | 364 ms                                                       | 377 ms: 1.04x slower                                                      |
| async_tree_io_tg           | 823 ms                                                       | 866 ms: 1.05x slower                                                      |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 85.2 ms: 1.08x faster                                                     |
| float          | 81.6 ms                                                      | 78.6 ms: 1.04x faster                                                     |
| pidigits       | 252 ms                                                       | 251 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                        | 1.04x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 241 ms: 1.01x slower                                                      |
| regex_compile  | 143 ms                                                       | 147 ms: 1.03x slower                                                      |
| regex_v8       | 24.9 ms                                                      | 25.7 ms: 1.03x slower                                                     |
| regex_effbot   | 3.51 ms                                                      | 3.68 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                        | 1.03x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.09 sec: 1.17x faster                                                    |
| xml_etree_generate   | 85.2 ms                                                      | 81.3 ms: 1.05x faster                                                     |
| xml_etree_process    | 60.7 ms                                                      | 58.0 ms: 1.05x faster                                                     |
| unpickle_pure_python | 216 us                                                       | 217 us: 1.01x slower                                                      |
| json_loads           | 24.7 us                                                      | 25.0 us: 1.01x slower                                                     |
| xml_etree_iterparse  | 99.8 ms                                                      | 101 ms: 1.01x slower                                                      |
| xml_etree_parse      | 144 ms                                                       | 148 ms: 1.03x slower                                                      |
| json_dumps           | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                     |
| pickle_pure_python   | 322 us                                                       | 344 us: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 14.9 ms: 1.05x faster                                                     |
| python_startup_no_site | 8.93 ms                                                      | 9.00 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                        | 1.02x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.43 ms: 1.09x faster                                                     |
| django_template | 38.9 ms                                                      | 44.0 ms: 1.13x slower                                                     |
| genshi_text     | 27.2 ms                                                      | 32.0 ms: 1.18x slower                                                     |
| genshi_xml      | 58.0 ms                                                      | 70.9 ms: 1.22x slower                                                     |
| Geometric mean  | (ref)                                                        | 1.10x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 29.2 us: 1.33x faster                                                     |
| deepcopy                   | 388 us                                                       | 308 us: 1.26x faster                                                      |
| async_tree_memoization_tg  | 458 ms                                                       | 373 ms: 1.23x faster                                                      |
| scimark_sor                | 125 ms                                                       | 104 ms: 1.20x faster                                                      |
| tomli_loads                | 2.43 sec                                                     | 2.09 sec: 1.17x faster                                                    |
| deepcopy_reduce            | 3.49 us                                                      | 3.03 us: 1.15x faster                                                     |
| telco                      | 8.77 ms                                                      | 7.69 ms: 1.14x faster                                                     |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.10x faster                                                     |
| mako                       | 10.3 ms                                                      | 9.43 ms: 1.09x faster                                                     |
| async_tree_memoization     | 447 ms                                                       | 410 ms: 1.09x faster                                                      |
| go                         | 167 ms                                                       | 154 ms: 1.09x faster                                                      |
| bpe_tokeniser              | 5.09 sec                                                     | 4.68 sec: 1.09x faster                                                    |
| async_tree_none            | 370 ms                                                       | 342 ms: 1.08x faster                                                      |
| nbody                      | 92.1 ms                                                      | 85.2 ms: 1.08x faster                                                     |
| richards                   | 52.5 ms                                                      | 48.8 ms: 1.07x faster                                                     |
| pyflate                    | 493 ms                                                       | 459 ms: 1.07x faster                                                      |
| json                       | 5.62 ms                                                      | 5.25 ms: 1.07x faster                                                     |
| async_tree_none_tg         | 342 ms                                                       | 322 ms: 1.06x faster                                                      |
| logging_silent             | 97.5 ns                                                      | 92.2 ns: 1.06x faster                                                     |
| scimark_fft                | 298 ms                                                       | 283 ms: 1.05x faster                                                      |
| python_startup             | 15.6 ms                                                      | 14.9 ms: 1.05x faster                                                     |
| xml_etree_generate         | 85.2 ms                                                      | 81.3 ms: 1.05x faster                                                     |
| xml_etree_process          | 60.7 ms                                                      | 58.0 ms: 1.05x faster                                                     |
| spectral_norm              | 97.4 ms                                                      | 93.3 ms: 1.04x faster                                                     |
| coverage                   | 84.5 ms                                                      | 81.1 ms: 1.04x faster                                                     |
| pprint_safe_repr           | 835 ms                                                       | 801 ms: 1.04x faster                                                      |
| float                      | 81.6 ms                                                      | 78.6 ms: 1.04x faster                                                     |
| fannkuch                   | 384 ms                                                       | 371 ms: 1.04x faster                                                      |
| richards_super             | 60.2 ms                                                      | 58.2 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 576 ms: 1.03x faster                                                      |
| asyncio_websockets         | 395 ms                                                       | 383 ms: 1.03x faster                                                      |
| pprint_pformat             | 1.70 sec                                                     | 1.65 sec: 1.03x faster                                                    |
| html5lib                   | 72.9 ms                                                      | 70.7 ms: 1.03x faster                                                     |
| dulwich_log                | 65.5 ms                                                      | 63.7 ms: 1.03x faster                                                     |
| deltablue                  | 3.38 ms                                                      | 3.31 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 561 ms: 1.02x faster                                                      |
| thrift                     | 918 us                                                       | 899 us: 1.02x faster                                                      |
| coroutines                 | 21.6 ms                                                      | 21.2 ms: 1.02x faster                                                     |
| scimark_lu                 | 97.4 ms                                                      | 96.2 ms: 1.01x faster                                                     |
| crypto_pyaes               | 73.5 ms                                                      | 73.0 ms: 1.01x faster                                                     |
| pidigits                   | 252 ms                                                       | 251 ms: 1.00x faster                                                      |
| meteor_contest             | 130 ms                                                       | 131 ms: 1.01x slower                                                      |
| unpickle_pure_python       | 216 us                                                       | 217 us: 1.01x slower                                                      |
| python_startup_no_site     | 8.93 ms                                                      | 9.00 ms: 1.01x slower                                                     |
| pycparser                  | 1.28 sec                                                     | 1.29 sec: 1.01x slower                                                    |
| regex_dna                  | 238 ms                                                       | 241 ms: 1.01x slower                                                      |
| json_loads                 | 24.7 us                                                      | 25.0 us: 1.01x slower                                                     |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.26 ms: 1.01x slower                                                     |
| xml_etree_iterparse        | 99.8 ms                                                      | 101 ms: 1.01x slower                                                      |
| async_tree_io              | 832 ms                                                       | 844 ms: 1.02x slower                                                      |
| xml_etree_parse            | 144 ms                                                       | 148 ms: 1.03x slower                                                      |
| regex_compile              | 143 ms                                                       | 147 ms: 1.03x slower                                                      |
| regex_v8                   | 24.9 ms                                                      | 25.7 ms: 1.03x slower                                                     |
| json_dumps                 | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                     |
| async_generators           | 364 ms                                                       | 377 ms: 1.04x slower                                                      |
| tornado_http               | 119 ms                                                       | 123 ms: 1.04x slower                                                      |
| typing_runtime_protocols   | 176 us                                                       | 182 us: 1.04x slower                                                      |
| sympy_expand               | 506 ms                                                       | 529 ms: 1.04x slower                                                      |
| scimark_monte_carlo        | 65.2 ms                                                      | 68.1 ms: 1.04x slower                                                     |
| regex_effbot               | 3.51 ms                                                      | 3.68 ms: 1.05x slower                                                     |
| logging_format             | 6.95 us                                                      | 7.29 us: 1.05x slower                                                     |
| mdp                        | 2.53 sec                                                     | 2.65 sec: 1.05x slower                                                    |
| logging_simple             | 6.28 us                                                      | 6.60 us: 1.05x slower                                                     |
| async_tree_io_tg           | 823 ms                                                       | 866 ms: 1.05x slower                                                      |
| sympy_str                  | 297 ms                                                       | 317 ms: 1.07x slower                                                      |
| 2to3                       | 293 ms                                                       | 313 ms: 1.07x slower                                                      |
| pickle_pure_python         | 322 us                                                       | 344 us: 1.07x slower                                                      |
| create_gc_cycles           | 2.65 ms                                                      | 2.88 ms: 1.09x slower                                                     |
| sqlglot_parse              | 1.37 ms                                                      | 1.49 ms: 1.09x slower                                                     |
| comprehensions             | 17.3 us                                                      | 18.9 us: 1.09x slower                                                     |
| generators                 | 33.9 ms                                                      | 37.3 ms: 1.10x slower                                                     |
| hexiom                     | 6.47 ms                                                      | 7.12 ms: 1.10x slower                                                     |
| sqlglot_transpile          | 1.76 ms                                                      | 1.95 ms: 1.10x slower                                                     |
| nqueens                    | 92.3 ms                                                      | 102 ms: 1.11x slower                                                      |
| sympy_sum                  | 154 ms                                                       | 171 ms: 1.11x slower                                                      |
| sphinx                     | 1.11 sec                                                     | 1.24 sec: 1.12x slower                                                    |
| docutils                   | 2.81 sec                                                     | 3.16 sec: 1.13x slower                                                    |
| sqlglot_normalize          | 119 ms                                                       | 134 ms: 1.13x slower                                                      |
| django_template            | 38.9 ms                                                      | 44.0 ms: 1.13x slower                                                     |
| sympy_integrate            | 23.4 ms                                                      | 26.8 ms: 1.15x slower                                                     |
| sqlglot_optimize           | 58.7 ms                                                      | 68.2 ms: 1.16x slower                                                     |
| chaos                      | 60.6 ms                                                      | 70.8 ms: 1.17x slower                                                     |
| raytrace                   | 267 ms                                                       | 313 ms: 1.17x slower                                                      |
| genshi_text                | 27.2 ms                                                      | 32.0 ms: 1.18x slower                                                     |
| pylint                     | 345 ms                                                       | 407 ms: 1.18x slower                                                      |
| genshi_xml                 | 58.0 ms                                                      | 70.9 ms: 1.22x slower                                                     |
| gc_traversal               | 4.48 ms                                                      | 5.53 ms: 1.24x slower                                                     |
| bench_mp_pool              | 4.82 ms                                                      | 2.82 sec: 584.57x slower                                                  |
| Geometric mean             | (ref)                                                        | 1.08x slower                                                              |

Benchmark hidden because not significant (1): bench_thread_pool
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.008x slower
# HPT report

- Reliability score: 62.63% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x