# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_invalidate_500k
- machine: linux-x86_64
- commit hash: 61a6174
- commit date: 2024-09-25
- overall geometric mean: 1.028x faster
- HPT reliability: 90.51%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 276 ms: 1.03x slower                                                            |
| docutils       | 2.59 sec                                               | 2.93 sec: 1.13x slower                                                          |
| html5lib       | 64.2 ms                                                | 62.0 ms: 1.03x faster                                                           |
| tornado_http   | 92.4 ms                                                | 94.6 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 387 ms: 1.20x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 398 ms: 1.11x faster                                                            |
| async_tree_none           | 351 ms                                                 | 320 ms: 1.10x faster                                                            |
| async_tree_none_tg        | 321 ms                                                 | 309 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 564 ms: 1.02x faster                                                            |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                                            |
| coroutines                | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                           |
| async_tree_io_tg          | 857 ms                                                 | 876 ms: 1.02x slower                                                            |
| async_tree_io             | 842 ms                                                 | 887 ms: 1.05x slower                                                            |
| async_generators          | 436 ms                                                 | 460 ms: 1.06x slower                                                            |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 69.8 ms: 1.13x faster                                                           |
| nbody          | 87.0 ms                                                | 81.4 ms: 1.07x faster                                                           |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.8 ms: 1.06x faster                                                           |
| regex_dna      | 218 ms                                                 | 212 ms: 1.03x faster                                                            |
| regex_effbot   | 3.73 ms                                                | 3.70 ms: 1.01x faster                                                           |
| regex_compile  | 132 ms                                                 | 142 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_generate  | 86.7 ms                                                | 77.3 ms: 1.12x faster                                                           |
| tomli_loads         | 2.14 sec                                               | 1.92 sec: 1.11x faster                                                          |
| xml_etree_process   | 60.6 ms                                                | 54.8 ms: 1.11x faster                                                           |
| json_dumps          | 10.6 ms                                                | 9.81 ms: 1.08x faster                                                           |
| xml_etree_parse     | 156 ms                                                 | 146 ms: 1.07x faster                                                            |
| xml_etree_iterparse | 101 ms                                                 | 98.7 ms: 1.03x faster                                                           |
| pickle_pure_python  | 310 us                                                 | 303 us: 1.03x faster                                                            |
| Geometric mean      | (ref)                                                  | 1.06x faster                                                                    |

Benchmark hidden because not significant (2): json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                           |
| python_startup_no_site | 6.96 ms                                                | 7.06 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.74 ms: 1.14x faster                                                           |
| django_template | 35.2 ms                                                | 36.0 ms: 1.02x slower                                                           |
| genshi_text     | 23.5 ms                                                | 24.8 ms: 1.06x slower                                                           |
| genshi_xml      | 50.9 ms                                                | 58.3 ms: 1.14x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174 |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 27.4 us: 1.43x faster                                                           |
| create_gc_cycles          | 2.41 ms                                                | 1.75 ms: 1.38x faster                                                           |
| deepcopy                  | 358 us                                                 | 266 us: 1.35x faster                                                            |
| deepcopy_reduce           | 3.20 us                                                | 2.67 us: 1.20x faster                                                           |
| async_tree_memoization_tg | 464 ms                                                 | 387 ms: 1.20x faster                                                            |
| richards                  | 48.7 ms                                                | 41.1 ms: 1.18x faster                                                           |
| python_startup            | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                           |
| richards_super            | 54.9 ms                                                | 46.9 ms: 1.17x faster                                                           |
| scimark_fft               | 364 ms                                                 | 312 ms: 1.17x faster                                                            |
| gc_traversal              | 4.37 ms                                                | 3.77 ms: 1.16x faster                                                           |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.40 ms: 1.15x faster                                                           |
| mako                      | 11.1 ms                                                | 9.74 ms: 1.14x faster                                                           |
| float                     | 79.2 ms                                                | 69.8 ms: 1.13x faster                                                           |
| xml_etree_generate        | 86.7 ms                                                | 77.3 ms: 1.12x faster                                                           |
| crypto_pyaes              | 75.3 ms                                                | 67.5 ms: 1.12x faster                                                           |
| tomli_loads               | 2.14 sec                                               | 1.92 sec: 1.11x faster                                                          |
| spectral_norm             | 115 ms                                                 | 104 ms: 1.11x faster                                                            |
| async_tree_memoization    | 442 ms                                                 | 398 ms: 1.11x faster                                                            |
| xml_etree_process         | 60.6 ms                                                | 54.8 ms: 1.11x faster                                                           |
| pathlib                   | 17.5 ms                                                | 15.9 ms: 1.10x faster                                                           |
| async_tree_none           | 351 ms                                                 | 320 ms: 1.10x faster                                                            |
| go                        | 144 ms                                                 | 133 ms: 1.08x faster                                                            |
| json_dumps                | 10.6 ms                                                | 9.81 ms: 1.08x faster                                                           |
| fannkuch                  | 404 ms                                                 | 377 ms: 1.07x faster                                                            |
| telco                     | 8.54 ms                                                | 7.96 ms: 1.07x faster                                                           |
| pyflate                   | 471 ms                                                 | 439 ms: 1.07x faster                                                            |
| mdp                       | 2.72 sec                                               | 2.54 sec: 1.07x faster                                                          |
| nbody                     | 87.0 ms                                                | 81.4 ms: 1.07x faster                                                           |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.07x faster                                                            |
| scimark_monte_carlo       | 67.4 ms                                                | 63.2 ms: 1.07x faster                                                           |
| bpe_tokeniser             | 4.75 sec                                               | 4.45 sec: 1.07x faster                                                          |
| regex_v8                  | 26.2 ms                                                | 24.8 ms: 1.06x faster                                                           |
| scimark_sor               | 124 ms                                                 | 117 ms: 1.06x faster                                                            |
| logging_format            | 6.40 us                                                | 6.15 us: 1.04x faster                                                           |
| async_tree_none_tg        | 321 ms                                                 | 309 ms: 1.04x faster                                                            |
| json                      | 5.36 ms                                                | 5.17 ms: 1.04x faster                                                           |
| html5lib                  | 64.2 ms                                                | 62.0 ms: 1.03x faster                                                           |
| regex_dna                 | 218 ms                                                 | 212 ms: 1.03x faster                                                            |
| thrift                    | 809 us                                                 | 788 us: 1.03x faster                                                            |
| xml_etree_iterparse       | 101 ms                                                 | 98.7 ms: 1.03x faster                                                           |
| pickle_pure_python        | 310 us                                                 | 303 us: 1.03x faster                                                            |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 564 ms: 1.02x faster                                                            |
| scimark_lu                | 113 ms                                                 | 111 ms: 1.02x faster                                                            |
| pycparser                 | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                          |
| logging_simple            | 5.72 us                                                | 5.65 us: 1.01x faster                                                           |
| meteor_contest            | 109 ms                                                 | 108 ms: 1.01x faster                                                            |
| deltablue                 | 3.23 ms                                                | 3.20 ms: 1.01x faster                                                           |
| regex_effbot              | 3.73 ms                                                | 3.70 ms: 1.01x faster                                                           |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                                            |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                                            |
| coroutines                | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                           |
| logging_silent            | 102 ns                                                 | 103 ns: 1.01x slower                                                            |
| python_startup_no_site    | 6.96 ms                                                | 7.06 ms: 1.01x slower                                                           |
| coverage                  | 84.0 ms                                                | 85.4 ms: 1.02x slower                                                           |
| chaos                     | 58.1 ms                                                | 59.1 ms: 1.02x slower                                                           |
| pprint_safe_repr          | 728 ms                                                 | 744 ms: 1.02x slower                                                            |
| async_tree_io_tg          | 857 ms                                                 | 876 ms: 1.02x slower                                                            |
| tornado_http              | 92.4 ms                                                | 94.6 ms: 1.02x slower                                                           |
| django_template           | 35.2 ms                                                | 36.0 ms: 1.02x slower                                                           |
| bench_thread_pool         | 822 us                                                 | 844 us: 1.03x slower                                                            |
| comprehensions            | 16.5 us                                                | 17.0 us: 1.03x slower                                                           |
| 2to3                      | 267 ms                                                 | 276 ms: 1.03x slower                                                            |
| raytrace                  | 267 ms                                                 | 276 ms: 1.04x slower                                                            |
| sqlglot_normalize         | 108 ms                                                 | 112 ms: 1.04x slower                                                            |
| pprint_pformat            | 1.49 sec                                               | 1.56 sec: 1.04x slower                                                          |
| sqlglot_parse             | 1.27 ms                                                | 1.33 ms: 1.05x slower                                                           |
| async_tree_io             | 842 ms                                                 | 887 ms: 1.05x slower                                                            |
| genshi_text               | 23.5 ms                                                | 24.8 ms: 1.06x slower                                                           |
| async_generators          | 436 ms                                                 | 460 ms: 1.06x slower                                                            |
| sqlglot_transpile         | 1.58 ms                                                | 1.69 ms: 1.07x slower                                                           |
| dulwich_log               | 64.3 ms                                                | 68.6 ms: 1.07x slower                                                           |
| regex_compile             | 132 ms                                                 | 142 ms: 1.08x slower                                                            |
| sqlglot_optimize          | 53.7 ms                                                | 58.4 ms: 1.09x slower                                                           |
| sympy_str                 | 275 ms                                                 | 300 ms: 1.09x slower                                                            |
| sympy_expand              | 463 ms                                                 | 506 ms: 1.09x slower                                                            |
| nqueens                   | 78.4 ms                                                | 88.5 ms: 1.13x slower                                                           |
| docutils                  | 2.59 sec                                               | 2.93 sec: 1.13x slower                                                          |
| hexiom                    | 6.16 ms                                                | 6.97 ms: 1.13x slower                                                           |
| genshi_xml                | 50.9 ms                                                | 58.3 ms: 1.14x slower                                                           |
| sympy_integrate           | 19.9 ms                                                | 22.9 ms: 1.15x slower                                                           |
| sympy_sum                 | 150 ms                                                 | 174 ms: 1.15x slower                                                            |
| generators                | 29.0 ms                                                | 34.9 ms: 1.20x slower                                                           |
| pylint                    | 313 ms                                                 | 381 ms: 1.22x slower                                                            |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (5): typing_runtime_protocols, json_loads, bench_mp_pool, unpickle_pure_python, async_tree_cpu_io_mixed_tg
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240925-3.14.0a0-61a6174-JIT/bm-20240925-linux-x86_64-savannahostrowski-jit_invalidate_500k-3.14.0a0-61a6174.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.028x faster
# HPT report

- Reliability score: 90.51% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.97x