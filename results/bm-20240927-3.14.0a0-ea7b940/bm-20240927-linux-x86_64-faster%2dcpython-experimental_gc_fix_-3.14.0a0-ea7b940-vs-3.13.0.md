# Results vs. 3.13.0

- fork: faster-cpython
- ref: experimental_gc_fix_
- machine: linux-x86_64
- commit hash: ea7b940
- commit date: 2024-09-27
- overall geometric mean: 1.034x faster
- HPT reliability: 98.52%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 268 ms: 1.00x slower                                                            |
| docutils       | 2.59 sec                                               | 2.61 sec: 1.01x slower                                                          |
| html5lib       | 64.2 ms                                                | 68.0 ms: 1.06x slower                                                           |
| tornado_http   | 92.4 ms                                                | 91.1 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 342 ms: 1.36x faster                                                            |
| async_tree_io_tg           | 857 ms                                                 | 656 ms: 1.30x faster                                                            |
| async_tree_io              | 842 ms                                                 | 650 ms: 1.29x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 365 ms: 1.21x faster                                                            |
| async_tree_none            | 351 ms                                                 | 300 ms: 1.17x faster                                                            |
| async_tree_none_tg         | 321 ms                                                 | 278 ms: 1.15x faster                                                            |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 521 ms: 1.11x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 498 ms: 1.10x faster                                                            |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.01x slower                                                           |
| asyncio_websockets         | 552 ms                                                 | 560 ms: 1.01x slower                                                            |
| async_generators           | 436 ms                                                 | 455 ms: 1.05x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| nbody          | 87.0 ms                                                | 89.6 ms: 1.03x slower                                                           |
| float          | 79.2 ms                                                | 94.2 ms: 1.19x slower                                                           |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.3 ms: 1.08x faster                                                           |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                            |
| regex_effbot   | 3.73 ms                                                | 3.77 ms: 1.01x slower                                                           |
| regex_dna      | 218 ms                                                 | 229 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 10.6 ms                                                | 10.3 ms: 1.03x faster                                                           |
| json_loads           | 27.2 us                                                | 26.9 us: 1.01x faster                                                           |
| pickle_pure_python   | 310 us                                                 | 307 us: 1.01x faster                                                            |
| tomli_loads          | 2.14 sec                                               | 2.13 sec: 1.01x faster                                                          |
| xml_etree_generate   | 86.7 ms                                                | 87.9 ms: 1.01x slower                                                           |
| xml_etree_process    | 60.6 ms                                                | 61.9 ms: 1.02x slower                                                           |
| unpickle_pure_python | 216 us                                                 | 221 us: 1.02x slower                                                            |
| xml_etree_parse      | 156 ms                                                 | 163 ms: 1.05x slower                                                            |
| xml_etree_iterparse  | 101 ms                                                 | 134 ms: 1.32x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.04x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.7 ms: 1.17x faster                                                           |
| python_startup_no_site | 6.96 ms                                                | 7.02 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 22.3 ms: 1.05x faster                                                           |
| django_template | 35.2 ms                                                | 34.2 ms: 1.03x faster                                                           |
| mako            | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| genshi_xml      | 50.9 ms                                                | 52.6 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.70 ms: 1.41x faster                                                           |
| deepcopy                   | 358 us                                                 | 262 us: 1.37x faster                                                            |
| async_tree_memoization_tg  | 464 ms                                                 | 342 ms: 1.36x faster                                                            |
| async_tree_io_tg           | 857 ms                                                 | 656 ms: 1.30x faster                                                            |
| async_tree_io              | 842 ms                                                 | 650 ms: 1.29x faster                                                            |
| deepcopy_memo              | 39.1 us                                                | 30.6 us: 1.28x faster                                                           |
| async_tree_memoization     | 442 ms                                                 | 365 ms: 1.21x faster                                                            |
| deepcopy_reduce            | 3.20 us                                                | 2.66 us: 1.20x faster                                                           |
| go                         | 144 ms                                                 | 121 ms: 1.19x faster                                                            |
| async_tree_none            | 351 ms                                                 | 300 ms: 1.17x faster                                                            |
| python_startup             | 12.5 ms                                                | 10.7 ms: 1.17x faster                                                           |
| async_tree_none_tg         | 321 ms                                                 | 278 ms: 1.15x faster                                                            |
| gc_traversal               | 4.37 ms                                                | 3.89 ms: 1.12x faster                                                           |
| pylint                     | 313 ms                                                 | 279 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 521 ms: 1.11x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 498 ms: 1.10x faster                                                            |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.65 ms: 1.08x faster                                                           |
| pathlib                    | 17.5 ms                                                | 16.2 ms: 1.08x faster                                                           |
| json                       | 5.36 ms                                                | 4.96 ms: 1.08x faster                                                           |
| regex_v8                   | 26.2 ms                                                | 24.3 ms: 1.08x faster                                                           |
| genshi_text                | 23.5 ms                                                | 22.3 ms: 1.05x faster                                                           |
| thrift                     | 809 us                                                 | 769 us: 1.05x faster                                                            |
| crypto_pyaes               | 75.3 ms                                                | 71.6 ms: 1.05x faster                                                           |
| generators                 | 29.0 ms                                                | 27.6 ms: 1.05x faster                                                           |
| richards                   | 48.7 ms                                                | 46.5 ms: 1.05x faster                                                           |
| richards_super             | 54.9 ms                                                | 52.7 ms: 1.04x faster                                                           |
| bench_thread_pool          | 822 us                                                 | 793 us: 1.04x faster                                                            |
| django_template            | 35.2 ms                                                | 34.2 ms: 1.03x faster                                                           |
| sympy_str                  | 275 ms                                                 | 267 ms: 1.03x faster                                                            |
| json_dumps                 | 10.6 ms                                                | 10.3 ms: 1.03x faster                                                           |
| telco                      | 8.54 ms                                                | 8.33 ms: 1.03x faster                                                           |
| typing_runtime_protocols   | 165 us                                                 | 161 us: 1.02x faster                                                            |
| scimark_fft                | 364 ms                                                 | 357 ms: 1.02x faster                                                            |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                          |
| sympy_sum                  | 150 ms                                                 | 148 ms: 1.02x faster                                                            |
| sympy_expand               | 463 ms                                                 | 455 ms: 1.02x faster                                                            |
| pprint_pformat             | 1.49 sec                                               | 1.47 sec: 1.02x faster                                                          |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                            |
| sympy_integrate            | 19.9 ms                                                | 19.6 ms: 1.02x faster                                                           |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                            |
| tornado_http               | 92.4 ms                                                | 91.1 ms: 1.01x faster                                                           |
| pprint_safe_repr           | 728 ms                                                 | 718 ms: 1.01x faster                                                            |
| logging_format             | 6.40 us                                                | 6.32 us: 1.01x faster                                                           |
| json_loads                 | 27.2 us                                                | 26.9 us: 1.01x faster                                                           |
| pickle_pure_python         | 310 us                                                 | 307 us: 1.01x faster                                                            |
| logging_simple             | 5.72 us                                                | 5.66 us: 1.01x faster                                                           |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                                            |
| tomli_loads                | 2.14 sec                                               | 2.13 sec: 1.01x faster                                                          |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.00x faster                                                            |
| scimark_lu                 | 113 ms                                                 | 112 ms: 1.00x faster                                                            |
| mdp                        | 2.72 sec                                               | 2.71 sec: 1.00x faster                                                          |
| 2to3                       | 267 ms                                                 | 268 ms: 1.00x slower                                                            |
| dulwich_log                | 64.3 ms                                                | 64.6 ms: 1.00x slower                                                           |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| scimark_monte_carlo        | 67.4 ms                                                | 67.9 ms: 1.01x slower                                                           |
| python_startup_no_site     | 6.96 ms                                                | 7.02 ms: 1.01x slower                                                           |
| docutils                   | 2.59 sec                                               | 2.61 sec: 1.01x slower                                                          |
| regex_effbot               | 3.73 ms                                                | 3.77 ms: 1.01x slower                                                           |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.01x slower                                                           |
| xml_etree_generate         | 86.7 ms                                                | 87.9 ms: 1.01x slower                                                           |
| hexiom                     | 6.16 ms                                                | 6.25 ms: 1.01x slower                                                           |
| asyncio_websockets         | 552 ms                                                 | 560 ms: 1.01x slower                                                            |
| nqueens                    | 78.4 ms                                                | 79.8 ms: 1.02x slower                                                           |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                           |
| pyflate                    | 471 ms                                                 | 480 ms: 1.02x slower                                                            |
| xml_etree_process          | 60.6 ms                                                | 61.9 ms: 1.02x slower                                                           |
| coverage                   | 84.0 ms                                                | 85.8 ms: 1.02x slower                                                           |
| sqlglot_transpile          | 1.58 ms                                                | 1.62 ms: 1.02x slower                                                           |
| sqlglot_parse              | 1.27 ms                                                | 1.30 ms: 1.02x slower                                                           |
| mako                       | 11.1 ms                                                | 11.3 ms: 1.02x slower                                                           |
| unpickle_pure_python       | 216 us                                                 | 221 us: 1.02x slower                                                            |
| logging_silent             | 102 ns                                                 | 104 ns: 1.03x slower                                                            |
| deltablue                  | 3.23 ms                                                | 3.32 ms: 1.03x slower                                                           |
| nbody                      | 87.0 ms                                                | 89.6 ms: 1.03x slower                                                           |
| genshi_xml                 | 50.9 ms                                                | 52.6 ms: 1.03x slower                                                           |
| chaos                      | 58.1 ms                                                | 60.0 ms: 1.03x slower                                                           |
| async_generators           | 436 ms                                                 | 455 ms: 1.05x slower                                                            |
| xml_etree_parse            | 156 ms                                                 | 163 ms: 1.05x slower                                                            |
| regex_dna                  | 218 ms                                                 | 229 ms: 1.05x slower                                                            |
| html5lib                   | 64.2 ms                                                | 68.0 ms: 1.06x slower                                                           |
| bpe_tokeniser              | 4.75 sec                                               | 5.29 sec: 1.12x slower                                                          |
| float                      | 79.2 ms                                                | 94.2 ms: 1.19x slower                                                           |
| xml_etree_iterparse        | 101 ms                                                 | 134 ms: 1.32x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (5): raytrace, fannkuch, bench_mp_pool, sqlglot_optimize, scimark_sor
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240927-3.14.0a0-ea7b940/bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.034x faster
# HPT report

- Reliability score: 98.52% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.90x