# Results vs. 3.13.0

- fork: faster-cpython
- ref: immortal_ref_count_s
- machine: linux-x86_64
- commit hash: e179c31
- commit date: 2024-09-20
- overall geometric mean: 1.038x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 255 ms: 1.05x faster                                                            |
| docutils       | 2.59 sec                                               | 2.65 sec: 1.02x slower                                                          |
| html5lib       | 64.2 ms                                                | 62.2 ms: 1.03x faster                                                           |
| tornado_http   | 92.4 ms                                                | 89.8 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 385 ms: 1.20x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 391 ms: 1.13x faster                                                            |
| async_tree_none            | 351 ms                                                 | 310 ms: 1.13x faster                                                            |
| async_tree_none_tg         | 321 ms                                                 | 297 ms: 1.08x faster                                                            |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 563 ms: 1.02x faster                                                            |
| async_generators           | 436 ms                                                 | 432 ms: 1.01x faster                                                            |
| asyncio_websockets         | 552 ms                                                 | 557 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 554 ms: 1.01x slower                                                            |
| coroutines                 | 22.7 ms                                                | 23.4 ms: 1.03x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (2): async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 76.6 ms: 1.03x faster                                                           |
| nbody          | 87.0 ms                                                | 89.9 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                           |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                            |
| regex_effbot   | 3.73 ms                                                | 3.68 ms: 1.01x faster                                                           |
| regex_dna      | 218 ms                                                 | 225 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 10.6 ms                                                | 10.1 ms: 1.04x faster                                                           |
| xml_etree_process    | 60.6 ms                                                | 58.7 ms: 1.03x faster                                                           |
| xml_etree_generate   | 86.7 ms                                                | 84.8 ms: 1.02x faster                                                           |
| pickle_pure_python   | 310 us                                                 | 304 us: 1.02x faster                                                            |
| tomli_loads          | 2.14 sec                                               | 2.10 sec: 1.02x faster                                                          |
| json_loads           | 27.2 us                                                | 26.8 us: 1.01x faster                                                           |
| xml_etree_parse      | 156 ms                                                 | 154 ms: 1.01x faster                                                            |
| unpickle_pure_python | 216 us                                                 | 214 us: 1.01x faster                                                            |
| xml_etree_iterparse  | 101 ms                                                 | 105 ms: 1.03x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                           |
| python_startup_no_site | 6.96 ms                                                | 7.00 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 21.9 ms: 1.07x faster                                                           |
| genshi_xml      | 50.9 ms                                                | 49.2 ms: 1.03x faster                                                           |
| django_template | 35.2 ms                                                | 34.5 ms: 1.02x faster                                                           |
| mako            | 11.1 ms                                                | 11.4 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 256 us: 1.40x faster                                                            |
| create_gc_cycles           | 2.41 ms                                                | 1.73 ms: 1.39x faster                                                           |
| deepcopy_memo              | 39.1 us                                                | 30.4 us: 1.29x faster                                                           |
| gc_traversal               | 4.37 ms                                                | 3.55 ms: 1.23x faster                                                           |
| async_tree_memoization_tg  | 464 ms                                                 | 385 ms: 1.20x faster                                                            |
| deepcopy_reduce            | 3.20 us                                                | 2.67 us: 1.20x faster                                                           |
| go                         | 144 ms                                                 | 120 ms: 1.20x faster                                                            |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                           |
| async_tree_memoization     | 442 ms                                                 | 391 ms: 1.13x faster                                                            |
| async_tree_none            | 351 ms                                                 | 310 ms: 1.13x faster                                                            |
| json                       | 5.36 ms                                                | 4.86 ms: 1.10x faster                                                           |
| pathlib                    | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                           |
| async_tree_none_tg         | 321 ms                                                 | 297 ms: 1.08x faster                                                            |
| genshi_text                | 23.5 ms                                                | 21.9 ms: 1.07x faster                                                           |
| regex_v8                   | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                           |
| thrift                     | 809 us                                                 | 763 us: 1.06x faster                                                            |
| crypto_pyaes               | 75.3 ms                                                | 71.0 ms: 1.06x faster                                                           |
| typing_runtime_protocols   | 165 us                                                 | 157 us: 1.05x faster                                                            |
| richards_super             | 54.9 ms                                                | 52.3 ms: 1.05x faster                                                           |
| richards                   | 48.7 ms                                                | 46.5 ms: 1.05x faster                                                           |
| 2to3                       | 267 ms                                                 | 255 ms: 1.05x faster                                                            |
| json_dumps                 | 10.6 ms                                                | 10.1 ms: 1.04x faster                                                           |
| bench_thread_pool          | 822 us                                                 | 791 us: 1.04x faster                                                            |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                            |
| generators                 | 29.0 ms                                                | 27.9 ms: 1.04x faster                                                           |
| genshi_xml                 | 50.9 ms                                                | 49.2 ms: 1.03x faster                                                           |
| float                      | 79.2 ms                                                | 76.6 ms: 1.03x faster                                                           |
| logging_format             | 6.40 us                                                | 6.19 us: 1.03x faster                                                           |
| xml_etree_process          | 60.6 ms                                                | 58.7 ms: 1.03x faster                                                           |
| html5lib                   | 64.2 ms                                                | 62.2 ms: 1.03x faster                                                           |
| pycparser                  | 1.20 sec                                               | 1.17 sec: 1.03x faster                                                          |
| tornado_http               | 92.4 ms                                                | 89.8 ms: 1.03x faster                                                           |
| sympy_sum                  | 150 ms                                                 | 146 ms: 1.03x faster                                                            |
| sympy_str                  | 275 ms                                                 | 268 ms: 1.03x faster                                                            |
| pprint_safe_repr           | 728 ms                                                 | 710 ms: 1.03x faster                                                            |
| pprint_pformat             | 1.49 sec                                               | 1.46 sec: 1.02x faster                                                          |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 563 ms: 1.02x faster                                                            |
| xml_etree_generate         | 86.7 ms                                                | 84.8 ms: 1.02x faster                                                           |
| logging_simple             | 5.72 us                                                | 5.59 us: 1.02x faster                                                           |
| pickle_pure_python         | 310 us                                                 | 304 us: 1.02x faster                                                            |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                            |
| sympy_integrate            | 19.9 ms                                                | 19.5 ms: 1.02x faster                                                           |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                            |
| tomli_loads                | 2.14 sec                                               | 2.10 sec: 1.02x faster                                                          |
| django_template            | 35.2 ms                                                | 34.5 ms: 1.02x faster                                                           |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.02x faster                                                            |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.96 ms: 1.02x faster                                                           |
| sqlglot_optimize           | 53.7 ms                                                | 52.9 ms: 1.02x faster                                                           |
| sympy_expand               | 463 ms                                                 | 456 ms: 1.02x faster                                                            |
| json_loads                 | 27.2 us                                                | 26.8 us: 1.01x faster                                                           |
| regex_effbot               | 3.73 ms                                                | 3.68 ms: 1.01x faster                                                           |
| xml_etree_parse            | 156 ms                                                 | 154 ms: 1.01x faster                                                            |
| mdp                        | 2.72 sec                                               | 2.69 sec: 1.01x faster                                                          |
| async_generators           | 436 ms                                                 | 432 ms: 1.01x faster                                                            |
| raytrace                   | 267 ms                                                 | 265 ms: 1.01x faster                                                            |
| pyflate                    | 471 ms                                                 | 468 ms: 1.01x faster                                                            |
| unpickle_pure_python       | 216 us                                                 | 214 us: 1.01x faster                                                            |
| bpe_tokeniser              | 4.75 sec                                               | 4.77 sec: 1.00x slower                                                          |
| python_startup_no_site     | 6.96 ms                                                | 7.00 ms: 1.01x slower                                                           |
| nqueens                    | 78.4 ms                                                | 78.9 ms: 1.01x slower                                                           |
| hexiom                     | 6.16 ms                                                | 6.20 ms: 1.01x slower                                                           |
| scimark_fft                | 364 ms                                                 | 367 ms: 1.01x slower                                                            |
| asyncio_websockets         | 552 ms                                                 | 557 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 554 ms: 1.01x slower                                                            |
| chaos                      | 58.1 ms                                                | 59.0 ms: 1.02x slower                                                           |
| deltablue                  | 3.23 ms                                                | 3.28 ms: 1.02x slower                                                           |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                            |
| docutils                   | 2.59 sec                                               | 2.65 sec: 1.02x slower                                                          |
| mako                       | 11.1 ms                                                | 11.4 ms: 1.02x slower                                                           |
| regex_dna                  | 218 ms                                                 | 225 ms: 1.03x slower                                                            |
| coroutines                 | 22.7 ms                                                | 23.4 ms: 1.03x slower                                                           |
| coverage                   | 84.0 ms                                                | 86.8 ms: 1.03x slower                                                           |
| nbody                      | 87.0 ms                                                | 89.9 ms: 1.03x slower                                                           |
| xml_etree_iterparse        | 101 ms                                                 | 105 ms: 1.03x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (14): telco, scimark_lu, sqlglot_transpile, fannkuch, dulwich_log, pidigits, bench_mp_pool, scimark_sor, comprehensions, sqlglot_parse, scimark_monte_carlo, async_tree_io_tg, async_tree_io, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240920-3.14.0a0-e179c31/bm-20240920-linux-x86_64-faster%2dcpython-immortal_ref_count_s-3.14.0a0-e179c31.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.038x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x