# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: partial_evaluator_un
- machine: linux-x86_64
- commit hash: aaab6a6
- commit date: 2024-09-20
- overall geometric mean: 1.028x faster
- HPT reliability: 84.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.49x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 276 ms: 1.04x slower                                                            |
| docutils       | 2.59 sec                                               | 2.97 sec: 1.14x slower                                                          |
| html5lib       | 64.2 ms                                                | 65.1 ms: 1.01x slower                                                           |
| tornado_http   | 92.4 ms                                                | 95.1 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 389 ms: 1.19x faster                                                            |
| async_tree_memoization     | 442 ms                                                 | 403 ms: 1.10x faster                                                            |
| async_tree_none            | 351 ms                                                 | 320 ms: 1.10x faster                                                            |
| async_tree_none_tg         | 321 ms                                                 | 309 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 569 ms: 1.01x faster                                                            |
| coroutines                 | 22.7 ms                                                | 22.5 ms: 1.01x faster                                                           |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 552 ms: 1.01x slower                                                            |
| async_tree_io_tg           | 857 ms                                                 | 877 ms: 1.02x slower                                                            |
| async_tree_io              | 842 ms                                                 | 862 ms: 1.02x slower                                                            |
| async_generators           | 436 ms                                                 | 456 ms: 1.05x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 69.4 ms: 1.14x faster                                                           |
| nbody          | 87.0 ms                                                | 81.1 ms: 1.07x faster                                                           |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.3 ms: 1.08x faster                                                           |
| regex_dna      | 218 ms                                                 | 226 ms: 1.03x slower                                                            |
| regex_effbot   | 3.73 ms                                                | 3.92 ms: 1.05x slower                                                           |
| regex_compile  | 132 ms                                                 | 142 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_generate  | 86.7 ms                                                | 76.7 ms: 1.13x faster                                                           |
| xml_etree_process   | 60.6 ms                                                | 53.7 ms: 1.13x faster                                                           |
| tomli_loads         | 2.14 sec                                               | 1.95 sec: 1.10x faster                                                          |
| xml_etree_parse     | 156 ms                                                 | 146 ms: 1.06x faster                                                            |
| json_dumps          | 10.6 ms                                                | 10.1 ms: 1.04x faster                                                           |
| xml_etree_iterparse | 101 ms                                                 | 98.1 ms: 1.03x faster                                                           |
| json_loads          | 27.2 us                                                | 26.6 us: 1.02x faster                                                           |
| pickle_pure_python  | 310 us                                                 | 309 us: 1.01x faster                                                            |
| Geometric mean      | (ref)                                                  | 1.06x faster                                                                    |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                           |
| python_startup_no_site | 6.96 ms                                                | 7.12 ms: 1.02x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.92 ms: 1.12x faster                                                           |
| django_template | 35.2 ms                                                | 36.2 ms: 1.03x slower                                                           |
| genshi_text     | 23.5 ms                                                | 24.6 ms: 1.05x slower                                                           |
| genshi_xml      | 50.9 ms                                                | 58.1 ms: 1.14x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 26.9 us: 1.45x faster                                                           |
| deepcopy                   | 358 us                                                 | 260 us: 1.38x faster                                                            |
| create_gc_cycles           | 2.41 ms                                                | 1.75 ms: 1.37x faster                                                           |
| richards                   | 48.7 ms                                                | 39.6 ms: 1.23x faster                                                           |
| deepcopy_reduce            | 3.20 us                                                | 2.63 us: 1.22x faster                                                           |
| richards_super             | 54.9 ms                                                | 45.7 ms: 1.20x faster                                                           |
| async_tree_memoization_tg  | 464 ms                                                 | 389 ms: 1.19x faster                                                            |
| python_startup             | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                           |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.37 ms: 1.15x faster                                                           |
| float                      | 79.2 ms                                                | 69.4 ms: 1.14x faster                                                           |
| scimark_fft                | 364 ms                                                 | 320 ms: 1.14x faster                                                            |
| crypto_pyaes               | 75.3 ms                                                | 66.4 ms: 1.13x faster                                                           |
| xml_etree_generate         | 86.7 ms                                                | 76.7 ms: 1.13x faster                                                           |
| xml_etree_process          | 60.6 ms                                                | 53.7 ms: 1.13x faster                                                           |
| mako                       | 11.1 ms                                                | 9.92 ms: 1.12x faster                                                           |
| gc_traversal               | 4.37 ms                                                | 3.91 ms: 1.12x faster                                                           |
| pathlib                    | 17.5 ms                                                | 15.8 ms: 1.11x faster                                                           |
| async_tree_memoization     | 442 ms                                                 | 403 ms: 1.10x faster                                                            |
| tomli_loads                | 2.14 sec                                               | 1.95 sec: 1.10x faster                                                          |
| async_tree_none            | 351 ms                                                 | 320 ms: 1.10x faster                                                            |
| go                         | 144 ms                                                 | 132 ms: 1.09x faster                                                            |
| telco                      | 8.54 ms                                                | 7.88 ms: 1.08x faster                                                           |
| spectral_norm              | 115 ms                                                 | 107 ms: 1.08x faster                                                            |
| regex_v8                   | 26.2 ms                                                | 24.3 ms: 1.08x faster                                                           |
| json                       | 5.36 ms                                                | 4.97 ms: 1.08x faster                                                           |
| fannkuch                   | 404 ms                                                 | 375 ms: 1.08x faster                                                            |
| nbody                      | 87.0 ms                                                | 81.1 ms: 1.07x faster                                                           |
| mdp                        | 2.72 sec                                               | 2.54 sec: 1.07x faster                                                          |
| bpe_tokeniser              | 4.75 sec                                               | 4.46 sec: 1.07x faster                                                          |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.06x faster                                                            |
| scimark_monte_carlo        | 67.4 ms                                                | 64.2 ms: 1.05x faster                                                           |
| logging_format             | 6.40 us                                                | 6.11 us: 1.05x faster                                                           |
| json_dumps                 | 10.6 ms                                                | 10.1 ms: 1.04x faster                                                           |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                                          |
| scimark_sor                | 124 ms                                                 | 119 ms: 1.04x faster                                                            |
| async_tree_none_tg         | 321 ms                                                 | 309 ms: 1.04x faster                                                            |
| xml_etree_iterparse        | 101 ms                                                 | 98.1 ms: 1.03x faster                                                           |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.03x faster                                                            |
| scimark_lu                 | 113 ms                                                 | 110 ms: 1.03x faster                                                            |
| json_loads                 | 27.2 us                                                | 26.6 us: 1.02x faster                                                           |
| thrift                     | 809 us                                                 | 792 us: 1.02x faster                                                            |
| logging_simple             | 5.72 us                                                | 5.62 us: 1.02x faster                                                           |
| pyflate                    | 471 ms                                                 | 464 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 569 ms: 1.01x faster                                                            |
| coroutines                 | 22.7 ms                                                | 22.5 ms: 1.01x faster                                                           |
| pickle_pure_python         | 310 us                                                 | 309 us: 1.01x faster                                                            |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                            |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                            |
| comprehensions             | 16.5 us                                                | 16.6 us: 1.01x slower                                                           |
| logging_silent             | 102 ns                                                 | 103 ns: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 552 ms: 1.01x slower                                                            |
| html5lib                   | 64.2 ms                                                | 65.1 ms: 1.01x slower                                                           |
| bench_thread_pool          | 822 us                                                 | 835 us: 1.02x slower                                                            |
| python_startup_no_site     | 6.96 ms                                                | 7.12 ms: 1.02x slower                                                           |
| async_tree_io_tg           | 857 ms                                                 | 877 ms: 1.02x slower                                                            |
| async_tree_io              | 842 ms                                                 | 862 ms: 1.02x slower                                                            |
| raytrace                   | 267 ms                                                 | 274 ms: 1.03x slower                                                            |
| tornado_http               | 92.4 ms                                                | 95.1 ms: 1.03x slower                                                           |
| pprint_pformat             | 1.49 sec                                               | 1.54 sec: 1.03x slower                                                          |
| django_template            | 35.2 ms                                                | 36.2 ms: 1.03x slower                                                           |
| regex_dna                  | 218 ms                                                 | 226 ms: 1.03x slower                                                            |
| 2to3                       | 267 ms                                                 | 276 ms: 1.04x slower                                                            |
| pprint_safe_repr           | 728 ms                                                 | 754 ms: 1.04x slower                                                            |
| dulwich_log                | 64.3 ms                                                | 67.2 ms: 1.04x slower                                                           |
| genshi_text                | 23.5 ms                                                | 24.6 ms: 1.05x slower                                                           |
| async_generators           | 436 ms                                                 | 456 ms: 1.05x slower                                                            |
| regex_effbot               | 3.73 ms                                                | 3.92 ms: 1.05x slower                                                           |
| sqlglot_normalize          | 108 ms                                                 | 113 ms: 1.05x slower                                                            |
| sqlglot_parse              | 1.27 ms                                                | 1.35 ms: 1.06x slower                                                           |
| regex_compile              | 132 ms                                                 | 142 ms: 1.07x slower                                                            |
| sqlglot_transpile          | 1.58 ms                                                | 1.71 ms: 1.08x slower                                                           |
| sympy_str                  | 275 ms                                                 | 298 ms: 1.09x slower                                                            |
| sqlglot_optimize           | 53.7 ms                                                | 58.4 ms: 1.09x slower                                                           |
| sympy_expand               | 463 ms                                                 | 505 ms: 1.09x slower                                                            |
| nqueens                    | 78.4 ms                                                | 85.7 ms: 1.09x slower                                                           |
| hexiom                     | 6.16 ms                                                | 6.86 ms: 1.11x slower                                                           |
| generators                 | 29.0 ms                                                | 33.0 ms: 1.14x slower                                                           |
| genshi_xml                 | 50.9 ms                                                | 58.1 ms: 1.14x slower                                                           |
| docutils                   | 2.59 sec                                               | 2.97 sec: 1.14x slower                                                          |
| sympy_sum                  | 150 ms                                                 | 173 ms: 1.15x slower                                                            |
| sympy_integrate            | 19.9 ms                                                | 22.8 ms: 1.15x slower                                                           |
| pylint                     | 313 ms                                                 | 373 ms: 1.19x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (6): typing_runtime_protocols, unpickle_pure_python, bench_mp_pool, deltablue, coverage, chaos
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240920-3.14.0a0-aaab6a6-JIT/bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.028x faster
# HPT report

- Reliability score: 84.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.49x