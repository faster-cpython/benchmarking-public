# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-x86_64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.300x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 437 ms: 1.49x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.44 sec: 1.22x slower                                                      |
| html5lib       | 72.9 ms                                                      | 107 ms: 1.47x slower                                                        |
| tornado_http   | 119 ms                                                       | 169 ms: 1.42x slower                                                        |
| Geometric mean | (ref)                                                        | 1.40x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_websockets         | 395 ms                                                       | 385 ms: 1.03x faster                                                        |
| async_tree_memoization_tg  | 458 ms                                                       | 484 ms: 1.06x slower                                                        |
| async_tree_none_tg         | 342 ms                                                       | 373 ms: 1.09x slower                                                        |
| async_tree_io_tg           | 823 ms                                                       | 909 ms: 1.10x slower                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 645 ms: 1.12x slower                                                        |
| async_tree_none            | 370 ms                                                       | 421 ms: 1.14x slower                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 686 ms: 1.15x slower                                                        |
| async_tree_io              | 832 ms                                                       | 963 ms: 1.16x slower                                                        |
| async_tree_memoization     | 447 ms                                                       | 524 ms: 1.17x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 29.2 ms: 1.36x slower                                                       |
| async_generators           | 364 ms                                                       | 501 ms: 1.38x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 252 ms                                                       | 250 ms: 1.01x faster                                                        |
| float          | 81.6 ms                                                      | 145 ms: 1.77x slower                                                        |
| nbody          | 92.1 ms                                                      | 195 ms: 2.12x slower                                                        |
| Geometric mean | (ref)                                                        | 1.55x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.54 ms: 1.01x slower                                                       |
| regex_dna      | 238 ms                                                       | 241 ms: 1.01x slower                                                        |
| regex_v8       | 24.9 ms                                                      | 27.3 ms: 1.09x slower                                                       |
| regex_compile  | 143 ms                                                       | 231 ms: 1.62x slower                                                        |
| Geometric mean | (ref)                                                        | 1.16x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 144 ms                                                       | 137 ms: 1.05x faster                                                        |
| xml_etree_iterparse  | 99.8 ms                                                      | 110 ms: 1.11x slower                                                        |
| json_loads           | 24.7 us                                                      | 29.5 us: 1.19x slower                                                       |
| json_dumps           | 10.8 ms                                                      | 14.2 ms: 1.32x slower                                                       |
| xml_etree_generate   | 85.2 ms                                                      | 118 ms: 1.38x slower                                                        |
| tomli_loads          | 2.43 sec                                                     | 3.38 sec: 1.39x slower                                                      |
| xml_etree_process    | 60.7 ms                                                      | 96.7 ms: 1.59x slower                                                       |
| pickle_pure_python   | 322 us                                                       | 593 us: 1.84x slower                                                        |
| unpickle_pure_python | 216 us                                                       | 417 us: 1.93x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.38x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 17.4 ms: 1.11x slower                                                       |
| python_startup_no_site | 8.93 ms                                                      | 12.0 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.22x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.0 ms                                                      | 83.9 ms: 1.45x slower                                                       |
| genshi_text     | 27.2 ms                                                      | 43.6 ms: 1.60x slower                                                       |
| django_template | 38.9 ms                                                      | 68.9 ms: 1.77x slower                                                       |
| mako            | 10.3 ms                                                      | 21.9 ms: 2.12x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.72x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| create_gc_cycles           | 2.65 ms                                                      | 1.67 ms: 1.59x faster                                                       |
| gc_traversal               | 4.48 ms                                                      | 2.99 ms: 1.50x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 137 ms: 1.05x faster                                                        |
| asyncio_websockets         | 395 ms                                                       | 385 ms: 1.03x faster                                                        |
| pidigits                   | 252 ms                                                       | 250 ms: 1.01x faster                                                        |
| regex_effbot               | 3.51 ms                                                      | 3.54 ms: 1.01x slower                                                       |
| regex_dna                  | 238 ms                                                       | 241 ms: 1.01x slower                                                        |
| bench_mp_pool              | 4.82 ms                                                      | 5.06 ms: 1.05x slower                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 484 ms: 1.06x slower                                                        |
| async_tree_none_tg         | 342 ms                                                       | 373 ms: 1.09x slower                                                        |
| regex_v8                   | 24.9 ms                                                      | 27.3 ms: 1.09x slower                                                       |
| json                       | 5.62 ms                                                      | 6.19 ms: 1.10x slower                                                       |
| async_tree_io_tg           | 823 ms                                                       | 909 ms: 1.10x slower                                                        |
| xml_etree_iterparse        | 99.8 ms                                                      | 110 ms: 1.11x slower                                                        |
| python_startup             | 15.6 ms                                                      | 17.4 ms: 1.11x slower                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 645 ms: 1.12x slower                                                        |
| async_tree_none            | 370 ms                                                       | 421 ms: 1.14x slower                                                        |
| pathlib                    | 17.4 ms                                                      | 19.9 ms: 1.15x slower                                                       |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 686 ms: 1.15x slower                                                        |
| async_tree_io              | 832 ms                                                       | 963 ms: 1.16x slower                                                        |
| deepcopy                   | 388 us                                                       | 455 us: 1.17x slower                                                        |
| async_tree_memoization     | 447 ms                                                       | 524 ms: 1.17x slower                                                        |
| json_loads                 | 24.7 us                                                      | 29.5 us: 1.19x slower                                                       |
| telco                      | 8.77 ms                                                      | 10.6 ms: 1.21x slower                                                       |
| generators                 | 33.9 ms                                                      | 41.3 ms: 1.22x slower                                                       |
| docutils                   | 2.81 sec                                                     | 3.44 sec: 1.22x slower                                                      |
| pylint                     | 345 ms                                                       | 441 ms: 1.28x slower                                                        |
| mdp                        | 2.53 sec                                                     | 3.24 sec: 1.28x slower                                                      |
| coverage                   | 84.5 ms                                                      | 109 ms: 1.29x slower                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 6.68 sec: 1.31x slower                                                      |
| json_dumps                 | 10.8 ms                                                      | 14.2 ms: 1.32x slower                                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.57 ms: 1.32x slower                                                       |
| meteor_contest             | 130 ms                                                       | 172 ms: 1.32x slower                                                        |
| scimark_fft                | 298 ms                                                       | 399 ms: 1.34x slower                                                        |
| python_startup_no_site     | 8.93 ms                                                      | 12.0 ms: 1.34x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 29.2 ms: 1.36x slower                                                       |
| sympy_integrate            | 23.4 ms                                                      | 32.1 ms: 1.37x slower                                                       |
| deepcopy_memo              | 38.9 us                                                      | 53.4 us: 1.37x slower                                                       |
| async_generators           | 364 ms                                                       | 501 ms: 1.38x slower                                                        |
| dulwich_log                | 65.5 ms                                                      | 90.5 ms: 1.38x slower                                                       |
| pycparser                  | 1.28 sec                                                     | 1.77 sec: 1.38x slower                                                      |
| xml_etree_generate         | 85.2 ms                                                      | 118 ms: 1.38x slower                                                        |
| deepcopy_reduce            | 3.49 us                                                      | 4.83 us: 1.38x slower                                                       |
| tomli_loads                | 2.43 sec                                                     | 3.38 sec: 1.39x slower                                                      |
| tornado_http               | 119 ms                                                       | 169 ms: 1.42x slower                                                        |
| nqueens                    | 92.3 ms                                                      | 132 ms: 1.43x slower                                                        |
| genshi_xml                 | 58.0 ms                                                      | 83.9 ms: 1.45x slower                                                       |
| html5lib                   | 72.9 ms                                                      | 107 ms: 1.47x slower                                                        |
| fannkuch                   | 384 ms                                                       | 571 ms: 1.49x slower                                                        |
| thrift                     | 918 us                                                       | 1.37 ms: 1.49x slower                                                       |
| 2to3                       | 293 ms                                                       | 437 ms: 1.49x slower                                                        |
| sympy_str                  | 297 ms                                                       | 455 ms: 1.53x slower                                                        |
| pyflate                    | 493 ms                                                       | 771 ms: 1.57x slower                                                        |
| richards                   | 52.5 ms                                                      | 83.2 ms: 1.59x slower                                                       |
| typing_runtime_protocols   | 176 us                                                       | 279 us: 1.59x slower                                                        |
| xml_etree_process          | 60.7 ms                                                      | 96.7 ms: 1.59x slower                                                       |
| genshi_text                | 27.2 ms                                                      | 43.6 ms: 1.60x slower                                                       |
| sqlglot_normalize          | 119 ms                                                       | 192 ms: 1.61x slower                                                        |
| regex_compile              | 143 ms                                                       | 231 ms: 1.62x slower                                                        |
| crypto_pyaes               | 73.5 ms                                                      | 120 ms: 1.63x slower                                                        |
| sympy_expand               | 506 ms                                                       | 827 ms: 1.63x slower                                                        |
| sqlglot_optimize           | 58.7 ms                                                      | 95.9 ms: 1.64x slower                                                       |
| richards_super             | 60.2 ms                                                      | 101 ms: 1.68x slower                                                        |
| sympy_sum                  | 154 ms                                                       | 264 ms: 1.72x slower                                                        |
| comprehensions             | 17.3 us                                                      | 29.7 us: 1.72x slower                                                       |
| pprint_safe_repr           | 835 ms                                                       | 1.44 sec: 1.73x slower                                                      |
| go                         | 167 ms                                                       | 291 ms: 1.74x slower                                                        |
| spectral_norm              | 97.4 ms                                                      | 170 ms: 1.75x slower                                                        |
| pprint_pformat             | 1.70 sec                                                     | 2.99 sec: 1.76x slower                                                      |
| django_template            | 38.9 ms                                                      | 68.9 ms: 1.77x slower                                                       |
| float                      | 81.6 ms                                                      | 145 ms: 1.77x slower                                                        |
| logging_format             | 6.95 us                                                      | 12.5 us: 1.79x slower                                                       |
| hexiom                     | 6.47 ms                                                      | 11.9 ms: 1.83x slower                                                       |
| pickle_pure_python         | 322 us                                                       | 593 us: 1.84x slower                                                        |
| logging_simple             | 6.28 us                                                      | 11.6 us: 1.85x slower                                                       |
| bench_thread_pool          | 929 us                                                       | 1.73 ms: 1.86x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                      | 3.39 ms: 1.93x slower                                                       |
| unpickle_pure_python       | 216 us                                                       | 417 us: 1.93x slower                                                        |
| logging_silent             | 97.5 ns                                                      | 191 ns: 1.96x slower                                                        |
| scimark_sor                | 125 ms                                                       | 250 ms: 2.00x slower                                                        |
| scimark_monte_carlo        | 65.2 ms                                                      | 134 ms: 2.05x slower                                                        |
| chaos                      | 60.6 ms                                                      | 125 ms: 2.06x slower                                                        |
| sqlglot_parse              | 1.37 ms                                                      | 2.87 ms: 2.10x slower                                                       |
| nbody                      | 92.1 ms                                                      | 195 ms: 2.12x slower                                                        |
| mako                       | 10.3 ms                                                      | 21.9 ms: 2.12x slower                                                       |
| raytrace                   | 267 ms                                                       | 611 ms: 2.28x slower                                                        |
| scimark_lu                 | 97.4 ms                                                      | 237 ms: 2.43x slower                                                        |
| deltablue                  | 3.38 ms                                                      | 8.35 ms: 2.47x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.43x slower                                                                |
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240831-3.14.0a0-34ddb64-NOGIL/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.300x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.34x
- 95% likely to have a slowdown of 1.33x
- 99% likely to have a slowdown of 1.31x

# Memory
- memory change: 1.06x