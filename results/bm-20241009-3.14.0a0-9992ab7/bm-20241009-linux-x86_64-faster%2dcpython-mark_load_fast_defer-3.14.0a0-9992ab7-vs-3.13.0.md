# Results vs. 3.13.0

- fork: faster-cpython
- ref: mark_load_fast_defer
- machine: linux-x86_64
- commit hash: 9992ab7
- commit date: 2024-10-09
- overall geometric mean: 1.036x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 256 ms: 1.04x faster                                                            |
| docutils       | 2.59 sec                                               | 2.66 sec: 1.03x slower                                                          |
| html5lib       | 64.2 ms                                                | 63.2 ms: 1.02x faster                                                           |
| tornado_http   | 92.4 ms                                                | 90.8 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 388 ms: 1.19x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 393 ms: 1.13x faster                                                            |
| async_tree_none            | 351 ms                                                 | 315 ms: 1.11x faster                                                            |
| async_tree_none_tg         | 321 ms                                                 | 300 ms: 1.07x faster                                                            |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 567 ms: 1.02x faster                                                            |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 556 ms: 1.02x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (4): async_generators, coroutines, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 76.6 ms: 1.03x faster                                                           |
| nbody          | 87.0 ms                                                | 84.1 ms: 1.03x faster                                                           |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.3 ms: 1.08x faster                                                           |
| regex_compile  | 132 ms                                                 | 129 ms: 1.03x faster                                                            |
| regex_effbot   | 3.73 ms                                                | 3.63 ms: 1.03x faster                                                           |
| regex_dna      | 218 ms                                                 | 221 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process    | 60.6 ms                                                | 58.2 ms: 1.04x faster                                                           |
| xml_etree_generate   | 86.7 ms                                                | 84.3 ms: 1.03x faster                                                           |
| pickle_pure_python   | 310 us                                                 | 303 us: 1.02x faster                                                            |
| json_dumps           | 10.6 ms                                                | 10.3 ms: 1.02x faster                                                           |
| tomli_loads          | 2.14 sec                                               | 2.11 sec: 1.01x faster                                                          |
| json_loads           | 27.2 us                                                | 26.9 us: 1.01x faster                                                           |
| xml_etree_parse      | 156 ms                                                 | 154 ms: 1.01x faster                                                            |
| unpickle_pure_python | 216 us                                                 | 214 us: 1.01x faster                                                            |
| xml_etree_iterparse  | 101 ms                                                 | 103 ms: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                           |
| python_startup_no_site | 6.96 ms                                                | 6.99 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 21.9 ms: 1.08x faster                                                           |
| genshi_xml      | 50.9 ms                                                | 49.1 ms: 1.04x faster                                                           |
| django_template | 35.2 ms                                                | 34.1 ms: 1.03x faster                                                           |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.72 ms: 1.40x faster                                                           |
| deepcopy                   | 358 us                                                 | 258 us: 1.39x faster                                                            |
| deepcopy_memo              | 39.1 us                                                | 30.5 us: 1.28x faster                                                           |
| deepcopy_reduce            | 3.20 us                                                | 2.64 us: 1.21x faster                                                           |
| go                         | 144 ms                                                 | 120 ms: 1.20x faster                                                            |
| async_tree_memoization_tg  | 464 ms                                                 | 388 ms: 1.19x faster                                                            |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                           |
| async_tree_memoization     | 442 ms                                                 | 393 ms: 1.13x faster                                                            |
| async_tree_none            | 351 ms                                                 | 315 ms: 1.11x faster                                                            |
| json                       | 5.36 ms                                                | 4.87 ms: 1.10x faster                                                           |
| gc_traversal               | 4.37 ms                                                | 4.00 ms: 1.09x faster                                                           |
| regex_v8                   | 26.2 ms                                                | 24.3 ms: 1.08x faster                                                           |
| pathlib                    | 17.5 ms                                                | 16.3 ms: 1.08x faster                                                           |
| genshi_text                | 23.5 ms                                                | 21.9 ms: 1.08x faster                                                           |
| async_tree_none_tg         | 321 ms                                                 | 300 ms: 1.07x faster                                                            |
| mdp                        | 2.72 sec                                               | 2.58 sec: 1.06x faster                                                          |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.05x faster                                                          |
| generators                 | 29.0 ms                                                | 27.6 ms: 1.05x faster                                                           |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.81 ms: 1.05x faster                                                           |
| 2to3                       | 267 ms                                                 | 256 ms: 1.04x faster                                                            |
| xml_etree_process          | 60.6 ms                                                | 58.2 ms: 1.04x faster                                                           |
| crypto_pyaes               | 75.3 ms                                                | 72.3 ms: 1.04x faster                                                           |
| thrift                     | 809 us                                                 | 778 us: 1.04x faster                                                            |
| bench_thread_pool          | 822 us                                                 | 791 us: 1.04x faster                                                            |
| typing_runtime_protocols   | 165 us                                                 | 159 us: 1.04x faster                                                            |
| genshi_xml                 | 50.9 ms                                                | 49.1 ms: 1.04x faster                                                           |
| richards                   | 48.7 ms                                                | 46.9 ms: 1.04x faster                                                           |
| richards_super             | 54.9 ms                                                | 53.0 ms: 1.03x faster                                                           |
| float                      | 79.2 ms                                                | 76.6 ms: 1.03x faster                                                           |
| nbody                      | 87.0 ms                                                | 84.1 ms: 1.03x faster                                                           |
| sympy_str                  | 275 ms                                                 | 266 ms: 1.03x faster                                                            |
| django_template            | 35.2 ms                                                | 34.1 ms: 1.03x faster                                                           |
| xml_etree_generate         | 86.7 ms                                                | 84.3 ms: 1.03x faster                                                           |
| regex_compile              | 132 ms                                                 | 129 ms: 1.03x faster                                                            |
| regex_effbot               | 3.73 ms                                                | 3.63 ms: 1.03x faster                                                           |
| pprint_safe_repr           | 728 ms                                                 | 710 ms: 1.02x faster                                                            |
| pickle_pure_python         | 310 us                                                 | 303 us: 1.02x faster                                                            |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                            |
| json_dumps                 | 10.6 ms                                                | 10.3 ms: 1.02x faster                                                           |
| pprint_pformat             | 1.49 sec                                               | 1.46 sec: 1.02x faster                                                          |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                            |
| sympy_integrate            | 19.9 ms                                                | 19.5 ms: 1.02x faster                                                           |
| pyflate                    | 471 ms                                                 | 462 ms: 1.02x faster                                                            |
| tornado_http               | 92.4 ms                                                | 90.8 ms: 1.02x faster                                                           |
| telco                      | 8.54 ms                                                | 8.40 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 567 ms: 1.02x faster                                                            |
| sympy_expand               | 463 ms                                                 | 456 ms: 1.02x faster                                                            |
| scimark_lu                 | 113 ms                                                 | 111 ms: 1.02x faster                                                            |
| sqlglot_optimize           | 53.7 ms                                                | 52.9 ms: 1.02x faster                                                           |
| html5lib                   | 64.2 ms                                                | 63.2 ms: 1.02x faster                                                           |
| tomli_loads                | 2.14 sec                                               | 2.11 sec: 1.01x faster                                                          |
| logging_simple             | 5.72 us                                                | 5.65 us: 1.01x faster                                                           |
| json_loads                 | 27.2 us                                                | 26.9 us: 1.01x faster                                                           |
| xml_etree_parse            | 156 ms                                                 | 154 ms: 1.01x faster                                                            |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                                            |
| unpickle_pure_python       | 216 us                                                 | 214 us: 1.01x faster                                                            |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                                            |
| raytrace                   | 267 ms                                                 | 266 ms: 1.01x faster                                                            |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| scimark_fft                | 364 ms                                                 | 365 ms: 1.00x slower                                                            |
| comprehensions             | 16.5 us                                                | 16.5 us: 1.00x slower                                                           |
| python_startup_no_site     | 6.96 ms                                                | 6.99 ms: 1.00x slower                                                           |
| dulwich_log                | 64.3 ms                                                | 64.7 ms: 1.01x slower                                                           |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                                           |
| logging_silent             | 102 ns                                                 | 103 ns: 1.01x slower                                                            |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                                            |
| regex_dna                  | 218 ms                                                 | 221 ms: 1.01x slower                                                            |
| scimark_monte_carlo        | 67.4 ms                                                | 68.5 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 556 ms: 1.02x slower                                                            |
| deltablue                  | 3.23 ms                                                | 3.29 ms: 1.02x slower                                                           |
| xml_etree_iterparse        | 101 ms                                                 | 103 ms: 1.02x slower                                                            |
| nqueens                    | 78.4 ms                                                | 80.0 ms: 1.02x slower                                                           |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| docutils                   | 2.59 sec                                               | 2.66 sec: 1.03x slower                                                          |
| chaos                      | 58.1 ms                                                | 59.7 ms: 1.03x slower                                                           |
| coverage                   | 84.0 ms                                                | 87.2 ms: 1.04x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (12): fannkuch, async_generators, logging_format, hexiom, bpe_tokeniser, bench_mp_pool, sqlglot_transpile, coroutines, scimark_sor, async_tree_io_tg, async_tree_io, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241009-3.14.0a0-9992ab7/bm-20241009-linux-x86_64-faster%2dcpython-mark_load_fast_defer-3.14.0a0-9992ab7.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.036x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x