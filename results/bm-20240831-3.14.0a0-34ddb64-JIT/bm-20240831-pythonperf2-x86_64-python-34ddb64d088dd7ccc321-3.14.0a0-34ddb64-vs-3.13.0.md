# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-x86_64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.023x faster
- HPT reliability: 94.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 310 ms: 1.06x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.16 sec: 1.13x slower                                                      |
| html5lib       | 72.9 ms                                                      | 68.9 ms: 1.06x faster                                                       |
| tornado_http   | 119 ms                                                       | 121 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 396 ms: 1.16x faster                                                        |
| async_tree_none            | 370 ms                                                       | 330 ms: 1.12x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 401 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 315 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 567 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 556 ms: 1.03x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.03x slower                                                       |
| async_generators           | 364 ms                                                       | 382 ms: 1.05x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (3): async_tree_io_tg, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.6 ms                                                      | 75.7 ms: 1.08x faster                                                       |
| nbody          | 92.1 ms                                                      | 89.1 ms: 1.03x faster                                                       |
| pidigits       | 252 ms                                                       | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.33 ms: 1.06x faster                                                       |
| regex_dna      | 238 ms                                                       | 234 ms: 1.02x faster                                                        |
| regex_compile  | 143 ms                                                       | 147 ms: 1.03x slower                                                        |
| regex_v8       | 24.9 ms                                                      | 25.9 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.15 sec: 1.13x faster                                                      |
| xml_etree_process    | 60.7 ms                                                      | 55.3 ms: 1.10x faster                                                       |
| xml_etree_generate   | 85.2 ms                                                      | 79.0 ms: 1.08x faster                                                       |
| unpickle_pure_python | 216 us                                                       | 212 us: 1.02x faster                                                        |
| json_dumps           | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                                       |
| xml_etree_iterparse  | 99.8 ms                                                      | 98.6 ms: 1.01x faster                                                       |
| pickle_pure_python   | 322 us                                                       | 320 us: 1.01x faster                                                        |
| json_loads           | 24.7 us                                                      | 25.1 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| python_startup_no_site | 8.93 ms                                                      | 9.09 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.23 ms: 1.12x faster                                                       |
| genshi_xml      | 58.0 ms                                                      | 61.3 ms: 1.06x slower                                                       |
| genshi_text     | 27.2 ms                                                      | 29.4 ms: 1.08x slower                                                       |
| django_template | 38.9 ms                                                      | 42.4 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 26.7 us: 1.46x faster                                                       |
| create_gc_cycles           | 2.65 ms                                                      | 1.91 ms: 1.39x faster                                                       |
| deepcopy                   | 388 us                                                       | 303 us: 1.28x faster                                                        |
| richards                   | 52.5 ms                                                      | 43.7 ms: 1.20x faster                                                       |
| richards_super             | 60.2 ms                                                      | 50.3 ms: 1.20x faster                                                       |
| spectral_norm              | 97.4 ms                                                      | 81.4 ms: 1.20x faster                                                       |
| scimark_sor                | 125 ms                                                       | 105 ms: 1.19x faster                                                        |
| deepcopy_reduce            | 3.49 us                                                      | 2.94 us: 1.19x faster                                                       |
| python_startup             | 15.6 ms                                                      | 13.4 ms: 1.17x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 396 ms: 1.16x faster                                                        |
| tomli_loads                | 2.43 sec                                                     | 2.15 sec: 1.13x faster                                                      |
| async_tree_none            | 370 ms                                                       | 330 ms: 1.12x faster                                                        |
| mako                       | 10.3 ms                                                      | 9.23 ms: 1.12x faster                                                       |
| async_tree_memoization     | 447 ms                                                       | 401 ms: 1.12x faster                                                        |
| xml_etree_process          | 60.7 ms                                                      | 55.3 ms: 1.10x faster                                                       |
| fannkuch                   | 384 ms                                                       | 350 ms: 1.10x faster                                                        |
| go                         | 167 ms                                                       | 152 ms: 1.10x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.09x faster                                                       |
| async_tree_none_tg         | 342 ms                                                       | 315 ms: 1.08x faster                                                        |
| telco                      | 8.77 ms                                                      | 8.11 ms: 1.08x faster                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 79.0 ms: 1.08x faster                                                       |
| bpe_tokeniser              | 5.09 sec                                                     | 4.73 sec: 1.08x faster                                                      |
| float                      | 81.6 ms                                                      | 75.7 ms: 1.08x faster                                                       |
| pprint_safe_repr           | 835 ms                                                       | 780 ms: 1.07x faster                                                        |
| coverage                   | 84.5 ms                                                      | 79.2 ms: 1.07x faster                                                       |
| deltablue                  | 3.38 ms                                                      | 3.18 ms: 1.06x faster                                                       |
| html5lib                   | 72.9 ms                                                      | 68.9 ms: 1.06x faster                                                       |
| regex_effbot               | 3.51 ms                                                      | 3.33 ms: 1.06x faster                                                       |
| crypto_pyaes               | 73.5 ms                                                      | 69.7 ms: 1.05x faster                                                       |
| pyflate                    | 493 ms                                                       | 468 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 567 ms: 1.05x faster                                                        |
| json                       | 5.62 ms                                                      | 5.37 ms: 1.05x faster                                                       |
| pprint_pformat             | 1.70 sec                                                     | 1.63 sec: 1.04x faster                                                      |
| nbody                      | 92.1 ms                                                      | 89.1 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 556 ms: 1.03x faster                                                        |
| thrift                     | 918 us                                                       | 894 us: 1.03x faster                                                        |
| scimark_fft                | 298 ms                                                       | 291 ms: 1.02x faster                                                        |
| gc_traversal               | 4.48 ms                                                      | 4.38 ms: 1.02x faster                                                       |
| pycparser                  | 1.28 sec                                                     | 1.25 sec: 1.02x faster                                                      |
| regex_dna                  | 238 ms                                                       | 234 ms: 1.02x faster                                                        |
| meteor_contest             | 130 ms                                                       | 128 ms: 1.02x faster                                                        |
| unpickle_pure_python       | 216 us                                                       | 212 us: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.14 ms: 1.02x faster                                                       |
| json_dumps                 | 10.8 ms                                                      | 10.7 ms: 1.01x faster                                                       |
| xml_etree_iterparse        | 99.8 ms                                                      | 98.6 ms: 1.01x faster                                                       |
| pidigits                   | 252 ms                                                       | 250 ms: 1.01x faster                                                        |
| scimark_lu                 | 97.4 ms                                                      | 96.7 ms: 1.01x faster                                                       |
| pickle_pure_python         | 322 us                                                       | 320 us: 1.01x faster                                                        |
| logging_format             | 6.95 us                                                      | 7.00 us: 1.01x slower                                                       |
| logging_simple             | 6.28 us                                                      | 6.36 us: 1.01x slower                                                       |
| json_loads                 | 24.7 us                                                      | 25.1 us: 1.01x slower                                                       |
| tornado_http               | 119 ms                                                       | 121 ms: 1.02x slower                                                        |
| python_startup_no_site     | 8.93 ms                                                      | 9.09 ms: 1.02x slower                                                       |
| mdp                        | 2.53 sec                                                     | 2.59 sec: 1.02x slower                                                      |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.03x slower                                                       |
| logging_silent             | 97.5 ns                                                      | 100 ns: 1.03x slower                                                        |
| regex_compile              | 143 ms                                                       | 147 ms: 1.03x slower                                                        |
| typing_runtime_protocols   | 176 us                                                       | 182 us: 1.04x slower                                                        |
| regex_v8                   | 24.9 ms                                                      | 25.9 ms: 1.04x slower                                                       |
| sympy_expand               | 506 ms                                                       | 528 ms: 1.04x slower                                                        |
| sympy_str                  | 297 ms                                                       | 311 ms: 1.05x slower                                                        |
| async_generators           | 364 ms                                                       | 382 ms: 1.05x slower                                                        |
| scimark_monte_carlo        | 65.2 ms                                                      | 68.6 ms: 1.05x slower                                                       |
| genshi_xml                 | 58.0 ms                                                      | 61.3 ms: 1.06x slower                                                       |
| 2to3                       | 293 ms                                                       | 310 ms: 1.06x slower                                                        |
| nqueens                    | 92.3 ms                                                      | 98.2 ms: 1.06x slower                                                       |
| comprehensions             | 17.3 us                                                      | 18.5 us: 1.07x slower                                                       |
| bench_mp_pool              | 4.82 ms                                                      | 5.20 ms: 1.08x slower                                                       |
| genshi_text                | 27.2 ms                                                      | 29.4 ms: 1.08x slower                                                       |
| hexiom                     | 6.47 ms                                                      | 7.00 ms: 1.08x slower                                                       |
| sqlglot_normalize          | 119 ms                                                       | 130 ms: 1.09x slower                                                        |
| django_template            | 38.9 ms                                                      | 42.4 ms: 1.09x slower                                                       |
| sqlglot_parse              | 1.37 ms                                                      | 1.50 ms: 1.10x slower                                                       |
| generators                 | 33.9 ms                                                      | 37.2 ms: 1.10x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                      | 1.94 ms: 1.10x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 170 ms: 1.10x slower                                                        |
| chaos                      | 60.6 ms                                                      | 67.6 ms: 1.12x slower                                                       |
| sqlglot_optimize           | 58.7 ms                                                      | 65.6 ms: 1.12x slower                                                       |
| docutils                   | 2.81 sec                                                     | 3.16 sec: 1.13x slower                                                      |
| sympy_integrate            | 23.4 ms                                                      | 26.4 ms: 1.13x slower                                                       |
| raytrace                   | 267 ms                                                       | 309 ms: 1.15x slower                                                        |
| pylint                     | 345 ms                                                       | 409 ms: 1.19x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (6): async_tree_io_tg, bench_thread_pool, xml_etree_parse, asyncio_websockets, dulwich_log, async_tree_io
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.023x faster
# HPT report

- Reliability score: 94.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x