# Results vs. 3.13.0

- fork: faster-cpython
- ref: experimental_gc_fix
- machine: linux-x86_64
- commit hash: 615a96e
- commit date: 2024-09-27
- overall geometric mean: 1.035x faster
- HPT reliability: 99.51%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 2.59 sec                                               | 2.58 sec: 1.00x faster                                                         |
| html5lib       | 64.2 ms                                                | 67.9 ms: 1.06x slower                                                          |
| tornado_http   | 92.4 ms                                                | 91.0 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 349 ms: 1.33x faster                                                           |
| async_tree_io_tg           | 857 ms                                                 | 653 ms: 1.31x faster                                                           |
| async_tree_io              | 842 ms                                                 | 654 ms: 1.29x faster                                                           |
| async_tree_memoization     | 442 ms                                                 | 370 ms: 1.20x faster                                                           |
| async_tree_none            | 351 ms                                                 | 301 ms: 1.17x faster                                                           |
| async_tree_none_tg         | 321 ms                                                 | 284 ms: 1.13x faster                                                           |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 536 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 512 ms: 1.07x faster                                                           |
| asyncio_websockets         | 552 ms                                                 | 557 ms: 1.01x slower                                                           |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                          |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.13x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                           |
| nbody          | 87.0 ms                                                | 88.2 ms: 1.01x slower                                                          |
| float          | 79.2 ms                                                | 92.7 ms: 1.17x slower                                                          |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                          |
| regex_compile  | 132 ms                                                 | 128 ms: 1.03x faster                                                           |
| regex_effbot   | 3.73 ms                                                | 3.68 ms: 1.01x faster                                                          |
| regex_dna      | 218 ms                                                 | 224 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                         |
| json_loads           | 27.2 us                                                | 26.9 us: 1.01x faster                                                          |
| json_dumps           | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                          |
| pickle_pure_python   | 310 us                                                 | 308 us: 1.01x faster                                                           |
| unpickle_pure_python | 216 us                                                 | 217 us: 1.01x slower                                                           |
| xml_etree_process    | 60.6 ms                                                | 61.5 ms: 1.01x slower                                                          |
| xml_etree_generate   | 86.7 ms                                                | 88.1 ms: 1.02x slower                                                          |
| xml_etree_parse      | 156 ms                                                 | 163 ms: 1.05x slower                                                           |
| xml_etree_iterparse  | 101 ms                                                 | 129 ms: 1.27x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.17x faster                                                          |
| python_startup_no_site | 6.96 ms                                                | 6.99 ms: 1.00x slower                                                          |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 22.5 ms: 1.05x faster                                                          |
| django_template | 35.2 ms                                                | 34.6 ms: 1.02x faster                                                          |
| genshi_xml      | 50.9 ms                                                | 52.2 ms: 1.03x slower                                                          |
| mako            | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                          |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.70 ms: 1.42x faster                                                          |
| deepcopy                   | 358 us                                                 | 262 us: 1.37x faster                                                           |
| async_tree_memoization_tg  | 464 ms                                                 | 349 ms: 1.33x faster                                                           |
| async_tree_io_tg           | 857 ms                                                 | 653 ms: 1.31x faster                                                           |
| async_tree_io              | 842 ms                                                 | 654 ms: 1.29x faster                                                           |
| deepcopy_memo              | 39.1 us                                                | 30.4 us: 1.28x faster                                                          |
| go                         | 144 ms                                                 | 120 ms: 1.20x faster                                                           |
| async_tree_memoization     | 442 ms                                                 | 370 ms: 1.20x faster                                                           |
| deepcopy_reduce            | 3.20 us                                                | 2.70 us: 1.18x faster                                                          |
| python_startup             | 12.5 ms                                                | 10.6 ms: 1.17x faster                                                          |
| async_tree_none            | 351 ms                                                 | 301 ms: 1.17x faster                                                           |
| async_tree_none_tg         | 321 ms                                                 | 284 ms: 1.13x faster                                                           |
| gc_traversal               | 4.37 ms                                                | 3.89 ms: 1.12x faster                                                          |
| pylint                     | 313 ms                                                 | 279 ms: 1.12x faster                                                           |
| pathlib                    | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                          |
| json                       | 5.36 ms                                                | 4.93 ms: 1.09x faster                                                          |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.65 ms: 1.09x faster                                                          |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 536 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 512 ms: 1.07x faster                                                           |
| regex_v8                   | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                          |
| richards                   | 48.7 ms                                                | 46.1 ms: 1.06x faster                                                          |
| genshi_text                | 23.5 ms                                                | 22.5 ms: 1.05x faster                                                          |
| richards_super             | 54.9 ms                                                | 52.4 ms: 1.05x faster                                                          |
| crypto_pyaes               | 75.3 ms                                                | 72.0 ms: 1.05x faster                                                          |
| thrift                     | 809 us                                                 | 773 us: 1.05x faster                                                           |
| generators                 | 29.0 ms                                                | 27.7 ms: 1.04x faster                                                          |
| typing_runtime_protocols   | 165 us                                                 | 158 us: 1.04x faster                                                           |
| meteor_contest             | 109 ms                                                 | 104 ms: 1.04x faster                                                           |
| regex_compile              | 132 ms                                                 | 128 ms: 1.03x faster                                                           |
| bench_thread_pool          | 822 us                                                 | 797 us: 1.03x faster                                                           |
| tomli_loads                | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                         |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.03x faster                                                           |
| sympy_str                  | 275 ms                                                 | 268 ms: 1.02x faster                                                           |
| scimark_fft                | 364 ms                                                 | 356 ms: 1.02x faster                                                           |
| sympy_integrate            | 19.9 ms                                                | 19.5 ms: 1.02x faster                                                          |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                           |
| telco                      | 8.54 ms                                                | 8.39 ms: 1.02x faster                                                          |
| pyflate                    | 471 ms                                                 | 463 ms: 1.02x faster                                                           |
| logging_format             | 6.40 us                                                | 6.29 us: 1.02x faster                                                          |
| django_template            | 35.2 ms                                                | 34.6 ms: 1.02x faster                                                          |
| fannkuch                   | 404 ms                                                 | 398 ms: 1.02x faster                                                           |
| tornado_http               | 92.4 ms                                                | 91.0 ms: 1.02x faster                                                          |
| regex_effbot               | 3.73 ms                                                | 3.68 ms: 1.01x faster                                                          |
| raytrace                   | 267 ms                                                 | 264 ms: 1.01x faster                                                           |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.01x faster                                                           |
| json_loads                 | 27.2 us                                                | 26.9 us: 1.01x faster                                                          |
| sympy_expand               | 463 ms                                                 | 459 ms: 1.01x faster                                                           |
| json_dumps                 | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                          |
| pickle_pure_python         | 310 us                                                 | 308 us: 1.01x faster                                                           |
| pprint_safe_repr           | 728 ms                                                 | 723 ms: 1.01x faster                                                           |
| logging_simple             | 5.72 us                                                | 5.68 us: 1.01x faster                                                          |
| pprint_pformat             | 1.49 sec                                               | 1.49 sec: 1.01x faster                                                         |
| docutils                   | 2.59 sec                                               | 2.58 sec: 1.00x faster                                                         |
| sqlglot_optimize           | 53.7 ms                                                | 53.9 ms: 1.00x slower                                                          |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                           |
| python_startup_no_site     | 6.96 ms                                                | 6.99 ms: 1.00x slower                                                          |
| unpickle_pure_python       | 216 us                                                 | 217 us: 1.01x slower                                                           |
| asyncio_websockets         | 552 ms                                                 | 557 ms: 1.01x slower                                                           |
| mdp                        | 2.72 sec                                               | 2.75 sec: 1.01x slower                                                         |
| hexiom                     | 6.16 ms                                                | 6.24 ms: 1.01x slower                                                          |
| coverage                   | 84.0 ms                                                | 85.1 ms: 1.01x slower                                                          |
| dulwich_log                | 64.3 ms                                                | 65.2 ms: 1.01x slower                                                          |
| nbody                      | 87.0 ms                                                | 88.2 ms: 1.01x slower                                                          |
| sqlglot_transpile          | 1.58 ms                                                | 1.61 ms: 1.01x slower                                                          |
| xml_etree_process          | 60.6 ms                                                | 61.5 ms: 1.01x slower                                                          |
| chaos                      | 58.1 ms                                                | 59.0 ms: 1.02x slower                                                          |
| xml_etree_generate         | 86.7 ms                                                | 88.1 ms: 1.02x slower                                                          |
| scimark_monte_carlo        | 67.4 ms                                                | 68.6 ms: 1.02x slower                                                          |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                          |
| sqlglot_parse              | 1.27 ms                                                | 1.30 ms: 1.02x slower                                                          |
| pycparser                  | 1.20 sec                                               | 1.22 sec: 1.02x slower                                                         |
| scimark_sor                | 124 ms                                                 | 126 ms: 1.02x slower                                                           |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                          |
| nqueens                    | 78.4 ms                                                | 80.1 ms: 1.02x slower                                                          |
| regex_dna                  | 218 ms                                                 | 224 ms: 1.02x slower                                                           |
| deltablue                  | 3.23 ms                                                | 3.30 ms: 1.02x slower                                                          |
| genshi_xml                 | 50.9 ms                                                | 52.2 ms: 1.03x slower                                                          |
| mako                       | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                          |
| logging_silent             | 102 ns                                                 | 105 ns: 1.03x slower                                                           |
| xml_etree_parse            | 156 ms                                                 | 163 ms: 1.05x slower                                                           |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                                           |
| html5lib                   | 64.2 ms                                                | 67.9 ms: 1.06x slower                                                          |
| bpe_tokeniser              | 4.75 sec                                               | 5.29 sec: 1.12x slower                                                         |
| float                      | 79.2 ms                                                | 92.7 ms: 1.17x slower                                                          |
| xml_etree_iterparse        | 101 ms                                                 | 129 ms: 1.27x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                   |

Benchmark hidden because not significant (3): 2to3, scimark_lu, bench_mp_pool
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240927-3.14.0a0-615a96e/bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-615a96e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.035x faster
# HPT report

- Reliability score: 99.51% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.90x