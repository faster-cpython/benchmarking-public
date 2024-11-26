# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: partial_evaluator
- machine: linux-x86_64
- commit hash: a6bc1a0
- commit date: 2024-09-04
- overall geometric mean: 1.028x faster
- HPT reliability: 74.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 276 ms: 1.04x slower                                                         |
| docutils       | 2.59 sec                                               | 2.95 sec: 1.14x slower                                                       |
| html5lib       | 64.2 ms                                                | 62.4 ms: 1.03x faster                                                        |
| tornado_http   | 92.4 ms                                                | 95.0 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg | 464 ms                                                 | 410 ms: 1.13x faster                                                         |
| async_tree_memoization    | 442 ms                                                 | 414 ms: 1.07x faster                                                         |
| async_tree_none           | 351 ms                                                 | 331 ms: 1.06x faster                                                         |
| async_tree_none_tg        | 321 ms                                                 | 316 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 568 ms: 1.02x faster                                                         |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                                         |
| coroutines                | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                        |
| async_generators          | 436 ms                                                 | 459 ms: 1.05x slower                                                         |
| async_tree_io_tg          | 857 ms                                                 | 910 ms: 1.06x slower                                                         |
| async_tree_io             | 842 ms                                                 | 946 ms: 1.12x slower                                                         |
| Geometric mean            | (ref)                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 70.9 ms: 1.12x faster                                                        |
| nbody          | 87.0 ms                                                | 80.0 ms: 1.09x faster                                                        |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                        |
| regex_effbot   | 3.73 ms                                                | 3.58 ms: 1.04x faster                                                        |
| regex_dna      | 218 ms                                                 | 212 ms: 1.03x faster                                                         |
| regex_compile  | 132 ms                                                 | 141 ms: 1.07x slower                                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 77.4 ms: 1.12x faster                                                        |
| tomli_loads          | 2.14 sec                                               | 1.92 sec: 1.11x faster                                                       |
| xml_etree_process    | 60.6 ms                                                | 54.5 ms: 1.11x faster                                                        |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.06x faster                                                         |
| pickle_pure_python   | 310 us                                                 | 300 us: 1.03x faster                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 98.8 ms: 1.02x faster                                                        |
| json_dumps           | 10.6 ms                                                | 10.3 ms: 1.02x faster                                                        |
| unpickle_pure_python | 216 us                                                 | 214 us: 1.01x faster                                                         |
| json_loads           | 27.2 us                                                | 28.6 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                        |
| python_startup_no_site | 6.96 ms                                                | 7.21 ms: 1.04x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.72 ms: 1.14x faster                                                        |
| django_template | 35.2 ms                                                | 35.9 ms: 1.02x slower                                                        |
| genshi_text     | 23.5 ms                                                | 24.6 ms: 1.04x slower                                                        |
| genshi_xml      | 50.9 ms                                                | 56.6 ms: 1.11x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                 |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0 |
|---------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo             | 39.1 us                                                | 27.0 us: 1.45x faster                                                        |
| deepcopy                  | 358 us                                                 | 261 us: 1.37x faster                                                         |
| create_gc_cycles          | 2.41 ms                                                | 1.78 ms: 1.35x faster                                                        |
| richards                  | 48.7 ms                                                | 39.2 ms: 1.24x faster                                                        |
| richards_super            | 54.9 ms                                                | 44.8 ms: 1.23x faster                                                        |
| deepcopy_reduce           | 3.20 us                                                | 2.67 us: 1.20x faster                                                        |
| scimark_fft               | 364 ms                                                 | 309 ms: 1.18x faster                                                         |
| python_startup            | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                        |
| gc_traversal              | 4.37 ms                                                | 3.77 ms: 1.16x faster                                                        |
| scimark_sparse_mat_mult   | 5.04 ms                                                | 4.37 ms: 1.15x faster                                                        |
| crypto_pyaes              | 75.3 ms                                                | 65.7 ms: 1.15x faster                                                        |
| mako                      | 11.1 ms                                                | 9.72 ms: 1.14x faster                                                        |
| async_tree_memoization_tg | 464 ms                                                 | 410 ms: 1.13x faster                                                         |
| spectral_norm             | 115 ms                                                 | 103 ms: 1.12x faster                                                         |
| xml_etree_generate        | 86.7 ms                                                | 77.4 ms: 1.12x faster                                                        |
| float                     | 79.2 ms                                                | 70.9 ms: 1.12x faster                                                        |
| pathlib                   | 17.5 ms                                                | 15.7 ms: 1.12x faster                                                        |
| tomli_loads               | 2.14 sec                                               | 1.92 sec: 1.11x faster                                                       |
| xml_etree_process         | 60.6 ms                                                | 54.5 ms: 1.11x faster                                                        |
| go                        | 144 ms                                                 | 130 ms: 1.11x faster                                                         |
| fannkuch                  | 404 ms                                                 | 371 ms: 1.09x faster                                                         |
| nbody                     | 87.0 ms                                                | 80.0 ms: 1.09x faster                                                        |
| telco                     | 8.54 ms                                                | 7.91 ms: 1.08x faster                                                        |
| mdp                       | 2.72 sec                                               | 2.54 sec: 1.07x faster                                                       |
| scimark_monte_carlo       | 67.4 ms                                                | 63.2 ms: 1.07x faster                                                        |
| async_tree_memoization    | 442 ms                                                 | 414 ms: 1.07x faster                                                         |
| bpe_tokeniser             | 4.75 sec                                               | 4.46 sec: 1.06x faster                                                       |
| xml_etree_parse           | 156 ms                                                 | 146 ms: 1.06x faster                                                         |
| regex_v8                  | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                        |
| async_tree_none           | 351 ms                                                 | 331 ms: 1.06x faster                                                         |
| scimark_sor               | 124 ms                                                 | 118 ms: 1.05x faster                                                         |
| regex_effbot              | 3.73 ms                                                | 3.58 ms: 1.04x faster                                                        |
| logging_format            | 6.40 us                                                | 6.14 us: 1.04x faster                                                        |
| thrift                    | 809 us                                                 | 782 us: 1.04x faster                                                         |
| pickle_pure_python        | 310 us                                                 | 300 us: 1.03x faster                                                         |
| pyflate                   | 471 ms                                                 | 456 ms: 1.03x faster                                                         |
| regex_dna                 | 218 ms                                                 | 212 ms: 1.03x faster                                                         |
| html5lib                  | 64.2 ms                                                | 62.4 ms: 1.03x faster                                                        |
| meteor_contest            | 109 ms                                                 | 106 ms: 1.03x faster                                                         |
| scimark_lu                | 113 ms                                                 | 110 ms: 1.02x faster                                                         |
| xml_etree_iterparse       | 101 ms                                                 | 98.8 ms: 1.02x faster                                                        |
| json_dumps                | 10.6 ms                                                | 10.3 ms: 1.02x faster                                                        |
| logging_simple            | 5.72 us                                                | 5.61 us: 1.02x faster                                                        |
| async_tree_none_tg        | 321 ms                                                 | 316 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed   | 577 ms                                                 | 568 ms: 1.02x faster                                                         |
| deltablue                 | 3.23 ms                                                | 3.18 ms: 1.01x faster                                                        |
| unpickle_pure_python      | 216 us                                                 | 214 us: 1.01x faster                                                         |
| asyncio_websockets        | 552 ms                                                 | 555 ms: 1.01x slower                                                         |
| pidigits                  | 186 ms                                                 | 188 ms: 1.01x slower                                                         |
| typing_runtime_protocols  | 165 us                                                 | 166 us: 1.01x slower                                                         |
| coroutines                | 22.7 ms                                                | 22.9 ms: 1.01x slower                                                        |
| bench_thread_pool         | 822 us                                                 | 831 us: 1.01x slower                                                         |
| pprint_pformat            | 1.49 sec                                               | 1.51 sec: 1.01x slower                                                       |
| pycparser                 | 1.20 sec                                               | 1.22 sec: 1.02x slower                                                       |
| chaos                     | 58.1 ms                                                | 59.1 ms: 1.02x slower                                                        |
| raytrace                  | 267 ms                                                 | 272 ms: 1.02x slower                                                         |
| django_template           | 35.2 ms                                                | 35.9 ms: 1.02x slower                                                        |
| tornado_http              | 92.4 ms                                                | 95.0 ms: 1.03x slower                                                        |
| coverage                  | 84.0 ms                                                | 86.4 ms: 1.03x slower                                                        |
| 2to3                      | 267 ms                                                 | 276 ms: 1.04x slower                                                         |
| python_startup_no_site    | 6.96 ms                                                | 7.21 ms: 1.04x slower                                                        |
| genshi_text               | 23.5 ms                                                | 24.6 ms: 1.04x slower                                                        |
| sqlglot_parse             | 1.27 ms                                                | 1.33 ms: 1.04x slower                                                        |
| sqlglot_normalize         | 108 ms                                                 | 112 ms: 1.05x slower                                                         |
| json_loads                | 27.2 us                                                | 28.6 us: 1.05x slower                                                        |
| async_generators          | 436 ms                                                 | 459 ms: 1.05x slower                                                         |
| sqlglot_transpile         | 1.58 ms                                                | 1.68 ms: 1.06x slower                                                        |
| dulwich_log               | 64.3 ms                                                | 68.4 ms: 1.06x slower                                                        |
| async_tree_io_tg          | 857 ms                                                 | 910 ms: 1.06x slower                                                         |
| regex_compile             | 132 ms                                                 | 141 ms: 1.07x slower                                                         |
| sqlglot_optimize          | 53.7 ms                                                | 57.8 ms: 1.08x slower                                                        |
| nqueens                   | 78.4 ms                                                | 85.3 ms: 1.09x slower                                                        |
| sympy_str                 | 275 ms                                                 | 299 ms: 1.09x slower                                                         |
| sympy_expand              | 463 ms                                                 | 507 ms: 1.09x slower                                                         |
| genshi_xml                | 50.9 ms                                                | 56.6 ms: 1.11x slower                                                        |
| hexiom                    | 6.16 ms                                                | 6.92 ms: 1.12x slower                                                        |
| async_tree_io             | 842 ms                                                 | 946 ms: 1.12x slower                                                         |
| docutils                  | 2.59 sec                                               | 2.95 sec: 1.14x slower                                                       |
| generators                | 29.0 ms                                                | 32.9 ms: 1.14x slower                                                        |
| sympy_integrate           | 19.9 ms                                                | 22.7 ms: 1.14x slower                                                        |
| sympy_sum                 | 150 ms                                                 | 172 ms: 1.15x slower                                                         |
| pylint                    | 313 ms                                                 | 372 ms: 1.19x slower                                                         |
| Geometric mean            | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (6): json, comprehensions, bench_mp_pool, logging_silent, pprint_safe_repr, async_tree_cpu_io_mixed_tg
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240904-3.14.0a0-a6bc1a0-JIT/bm-20240904-linux-x86_64-Fidget%2dSpinner-partial_evaluator-3.14.0a0-a6bc1a0.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.028x faster
# HPT report

- Reliability score: 74.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x