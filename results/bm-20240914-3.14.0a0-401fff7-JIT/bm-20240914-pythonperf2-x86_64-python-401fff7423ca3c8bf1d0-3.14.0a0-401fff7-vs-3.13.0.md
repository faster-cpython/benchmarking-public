# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-x86_64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.026x faster
- HPT reliability: 95.41%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 309 ms: 1.06x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.16 sec: 1.13x slower                                                      |
| html5lib       | 72.9 ms                                                      | 71.3 ms: 1.02x faster                                                       |
| tornado_http   | 119 ms                                                       | 121 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 389 ms: 1.18x faster                                                        |
| async_tree_none            | 370 ms                                                       | 319 ms: 1.16x faster                                                        |
| async_tree_memoization     | 447 ms                                                       | 401 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 342 ms                                                       | 309 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 544 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 571 ms: 1.04x faster                                                        |
| async_tree_io              | 832 ms                                                       | 805 ms: 1.03x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.01x slower                                                       |
| async_generators           | 364 ms                                                       | 386 ms: 1.06x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (2): async_tree_io_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 78.7 ms: 1.17x faster                                                       |
| float          | 81.6 ms                                                      | 74.2 ms: 1.10x faster                                                       |
| pidigits       | 252 ms                                                       | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 238 ms                                                       | 237 ms: 1.01x faster                                                        |
| regex_compile  | 143 ms                                                       | 146 ms: 1.02x slower                                                        |
| regex_effbot   | 3.51 ms                                                      | 3.61 ms: 1.03x slower                                                       |
| regex_v8       | 24.9 ms                                                      | 25.8 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.43 sec                                                     | 2.09 sec: 1.17x faster                                                      |
| xml_etree_process    | 60.7 ms                                                      | 55.8 ms: 1.09x faster                                                       |
| xml_etree_generate   | 85.2 ms                                                      | 78.5 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 99.8 ms                                                      | 97.4 ms: 1.03x faster                                                       |
| unpickle_pure_python | 216 us                                                       | 214 us: 1.01x faster                                                        |
| xml_etree_parse      | 144 ms                                                       | 142 ms: 1.01x faster                                                        |
| json_loads           | 24.7 us                                                      | 24.5 us: 1.01x faster                                                       |
| pickle_pure_python   | 322 us                                                       | 326 us: 1.01x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 15.6 ms                                                      | 13.3 ms: 1.17x faster                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.3 ms                                                      | 9.18 ms: 1.12x faster                                                       |
| django_template | 38.9 ms                                                      | 41.6 ms: 1.07x slower                                                       |
| genshi_text     | 27.2 ms                                                      | 29.3 ms: 1.08x slower                                                       |
| genshi_xml      | 58.0 ms                                                      | 66.1 ms: 1.14x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 38.9 us                                                      | 26.5 us: 1.47x faster                                                       |
| create_gc_cycles           | 2.65 ms                                                      | 1.91 ms: 1.39x faster                                                       |
| deepcopy                   | 388 us                                                       | 292 us: 1.33x faster                                                        |
| scimark_sor                | 125 ms                                                       | 103 ms: 1.21x faster                                                        |
| deepcopy_reduce            | 3.49 us                                                      | 2.90 us: 1.20x faster                                                       |
| spectral_norm              | 97.4 ms                                                      | 81.4 ms: 1.20x faster                                                       |
| async_tree_memoization_tg  | 458 ms                                                       | 389 ms: 1.18x faster                                                        |
| richards                   | 52.5 ms                                                      | 44.7 ms: 1.17x faster                                                       |
| python_startup             | 15.6 ms                                                      | 13.3 ms: 1.17x faster                                                       |
| nbody                      | 92.1 ms                                                      | 78.7 ms: 1.17x faster                                                       |
| tomli_loads                | 2.43 sec                                                     | 2.09 sec: 1.17x faster                                                      |
| async_tree_none            | 370 ms                                                       | 319 ms: 1.16x faster                                                        |
| richards_super             | 60.2 ms                                                      | 52.4 ms: 1.15x faster                                                       |
| mako                       | 10.3 ms                                                      | 9.18 ms: 1.12x faster                                                       |
| async_tree_memoization     | 447 ms                                                       | 401 ms: 1.12x faster                                                        |
| go                         | 167 ms                                                       | 150 ms: 1.11x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.7 ms: 1.11x faster                                                       |
| async_tree_none_tg         | 342 ms                                                       | 309 ms: 1.11x faster                                                        |
| float                      | 81.6 ms                                                      | 74.2 ms: 1.10x faster                                                       |
| xml_etree_process          | 60.7 ms                                                      | 55.8 ms: 1.09x faster                                                       |
| xml_etree_generate         | 85.2 ms                                                      | 78.5 ms: 1.09x faster                                                       |
| telco                      | 8.77 ms                                                      | 8.08 ms: 1.09x faster                                                       |
| pyflate                    | 493 ms                                                       | 454 ms: 1.08x faster                                                        |
| json                       | 5.62 ms                                                      | 5.20 ms: 1.08x faster                                                       |
| fannkuch                   | 384 ms                                                       | 358 ms: 1.07x faster                                                        |
| bpe_tokeniser              | 5.09 sec                                                     | 4.76 sec: 1.07x faster                                                      |
| pprint_safe_repr           | 835 ms                                                       | 783 ms: 1.07x faster                                                        |
| coverage                   | 84.5 ms                                                      | 79.4 ms: 1.06x faster                                                       |
| crypto_pyaes               | 73.5 ms                                                      | 69.7 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 544 ms: 1.05x faster                                                        |
| deltablue                  | 3.38 ms                                                      | 3.23 ms: 1.05x faster                                                       |
| pprint_pformat             | 1.70 sec                                                     | 1.63 sec: 1.05x faster                                                      |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 571 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.06 ms: 1.04x faster                                                       |
| thrift                     | 918 us                                                       | 885 us: 1.04x faster                                                        |
| async_tree_io              | 832 ms                                                       | 805 ms: 1.03x faster                                                        |
| scimark_fft                | 298 ms                                                       | 290 ms: 1.03x faster                                                        |
| gc_traversal               | 4.48 ms                                                      | 4.36 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 99.8 ms                                                      | 97.4 ms: 1.03x faster                                                       |
| html5lib                   | 72.9 ms                                                      | 71.3 ms: 1.02x faster                                                       |
| meteor_contest             | 130 ms                                                       | 128 ms: 1.02x faster                                                        |
| dulwich_log                | 65.5 ms                                                      | 64.6 ms: 1.01x faster                                                       |
| unpickle_pure_python       | 216 us                                                       | 214 us: 1.01x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 142 ms: 1.01x faster                                                        |
| json_loads                 | 24.7 us                                                      | 24.5 us: 1.01x faster                                                       |
| pidigits                   | 252 ms                                                       | 250 ms: 1.01x faster                                                        |
| regex_dna                  | 238 ms                                                       | 237 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.01x slower                                                       |
| pickle_pure_python         | 322 us                                                       | 326 us: 1.01x slower                                                        |
| tornado_http               | 119 ms                                                       | 121 ms: 1.01x slower                                                        |
| pycparser                  | 1.28 sec                                                     | 1.30 sec: 1.01x slower                                                      |
| regex_compile              | 143 ms                                                       | 146 ms: 1.02x slower                                                        |
| regex_effbot               | 3.51 ms                                                      | 3.61 ms: 1.03x slower                                                       |
| scimark_monte_carlo        | 65.2 ms                                                      | 67.1 ms: 1.03x slower                                                       |
| mdp                        | 2.53 sec                                                     | 2.61 sec: 1.03x slower                                                      |
| regex_v8                   | 24.9 ms                                                      | 25.8 ms: 1.03x slower                                                       |
| logging_format             | 6.95 us                                                      | 7.20 us: 1.04x slower                                                       |
| sympy_expand               | 506 ms                                                       | 525 ms: 1.04x slower                                                        |
| bench_mp_pool              | 4.82 ms                                                      | 5.00 ms: 1.04x slower                                                       |
| sympy_str                  | 297 ms                                                       | 308 ms: 1.04x slower                                                        |
| logging_simple             | 6.28 us                                                      | 6.53 us: 1.04x slower                                                       |
| logging_silent             | 97.5 ns                                                      | 101 ns: 1.04x slower                                                        |
| nqueens                    | 92.3 ms                                                      | 97.0 ms: 1.05x slower                                                       |
| 2to3                       | 293 ms                                                       | 309 ms: 1.06x slower                                                        |
| comprehensions             | 17.3 us                                                      | 18.3 us: 1.06x slower                                                       |
| typing_runtime_protocols   | 176 us                                                       | 186 us: 1.06x slower                                                        |
| async_generators           | 364 ms                                                       | 386 ms: 1.06x slower                                                        |
| django_template            | 38.9 ms                                                      | 41.6 ms: 1.07x slower                                                       |
| sqlglot_normalize          | 119 ms                                                       | 128 ms: 1.07x slower                                                        |
| hexiom                     | 6.47 ms                                                      | 6.95 ms: 1.07x slower                                                       |
| generators                 | 33.9 ms                                                      | 36.5 ms: 1.08x slower                                                       |
| genshi_text                | 27.2 ms                                                      | 29.3 ms: 1.08x slower                                                       |
| chaos                      | 60.6 ms                                                      | 65.6 ms: 1.08x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 167 ms: 1.08x slower                                                        |
| sqlglot_parse              | 1.37 ms                                                      | 1.48 ms: 1.08x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                      | 1.93 ms: 1.10x slower                                                       |
| sqlglot_optimize           | 58.7 ms                                                      | 65.0 ms: 1.11x slower                                                       |
| sympy_integrate            | 23.4 ms                                                      | 26.3 ms: 1.13x slower                                                       |
| docutils                   | 2.81 sec                                                     | 3.16 sec: 1.13x slower                                                      |
| genshi_xml                 | 58.0 ms                                                      | 66.1 ms: 1.14x slower                                                       |
| raytrace                   | 267 ms                                                       | 313 ms: 1.17x slower                                                        |
| pylint                     | 345 ms                                                       | 408 ms: 1.18x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (6): bench_thread_pool, async_tree_io_tg, json_dumps, python_startup_no_site, scimark_lu, asyncio_websockets
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.026x faster
# HPT report

- Reliability score: 95.41% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x