# Results vs. 3.13.0

- fork: faster-cpython
- ref: split_load_const
- machine: linux-x86_64
- commit hash: f934559
- commit date: 2024-10-25
- overall geometric mean: 1.016x faster
- HPT reliability: 93.35%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 255 ms: 1.05x faster                                                         |
| docutils       | 2.59 sec                                               | 2.65 sec: 1.02x slower                                                       |
| html5lib       | 64.2 ms                                                | 63.9 ms: 1.00x faster                                                        |
| tornado_http   | 92.4 ms                                                | 91.1 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 384 ms: 1.21x faster                                                         |
| async_tree_none            | 351 ms                                                 | 326 ms: 1.08x faster                                                         |
| async_tree_memoization     | 442 ms                                                 | 413 ms: 1.07x faster                                                         |
| async_generators           | 436 ms                                                 | 428 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 559 ms: 1.02x slower                                                         |
| coroutines                 | 22.7 ms                                                | 23.9 ms: 1.05x slower                                                        |
| async_tree_io_tg           | 857 ms                                                 | 981 ms: 1.14x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, async_tree_io, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                         |
| nbody          | 87.0 ms                                                | 94.4 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                        |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                         |
| regex_effbot   | 3.73 ms                                                | 3.69 ms: 1.01x faster                                                        |
| regex_dna      | 218 ms                                                 | 217 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_loads           | 27.2 us                                                | 26.2 us: 1.04x faster                                                        |
| xml_etree_process    | 60.6 ms                                                | 59.6 ms: 1.02x faster                                                        |
| xml_etree_generate   | 86.7 ms                                                | 85.4 ms: 1.02x faster                                                        |
| unpickle_pure_python | 216 us                                                 | 217 us: 1.01x slower                                                         |
| pickle_pure_python   | 310 us                                                 | 313 us: 1.01x slower                                                         |
| xml_etree_parse      | 156 ms                                                 | 157 ms: 1.01x slower                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 105 ms: 1.03x slower                                                         |
| json_dumps           | 10.6 ms                                                | 11.3 ms: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.8 ms: 1.06x faster                                                        |
| python_startup_no_site | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 22.2 ms: 1.06x faster                                                        |
| django_template | 35.2 ms                                                | 34.6 ms: 1.02x faster                                                        |
| genshi_xml      | 50.9 ms                                                | 50.4 ms: 1.01x faster                                                        |
| mako            | 11.1 ms                                                | 11.7 ms: 1.05x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 261 us: 1.37x faster                                                         |
| deepcopy_memo              | 39.1 us                                                | 30.6 us: 1.28x faster                                                        |
| async_tree_memoization_tg  | 464 ms                                                 | 384 ms: 1.21x faster                                                         |
| deepcopy_reduce            | 3.20 us                                                | 2.67 us: 1.20x faster                                                        |
| go                         | 144 ms                                                 | 121 ms: 1.19x faster                                                         |
| json                       | 5.36 ms                                                | 4.84 ms: 1.11x faster                                                        |
| pathlib                    | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                        |
| telco                      | 8.54 ms                                                | 7.94 ms: 1.08x faster                                                        |
| async_tree_none            | 351 ms                                                 | 326 ms: 1.08x faster                                                         |
| async_tree_memoization     | 442 ms                                                 | 413 ms: 1.07x faster                                                         |
| regex_v8                   | 26.2 ms                                                | 24.7 ms: 1.06x faster                                                        |
| richards                   | 48.7 ms                                                | 45.8 ms: 1.06x faster                                                        |
| genshi_text                | 23.5 ms                                                | 22.2 ms: 1.06x faster                                                        |
| python_startup             | 12.5 ms                                                | 11.8 ms: 1.06x faster                                                        |
| mdp                        | 2.72 sec                                               | 2.58 sec: 1.06x faster                                                       |
| richards_super             | 54.9 ms                                                | 52.3 ms: 1.05x faster                                                        |
| sqlalchemy_declarative     | 133 ms                                                 | 127 ms: 1.05x faster                                                         |
| 2to3                       | 267 ms                                                 | 255 ms: 1.05x faster                                                         |
| typing_runtime_protocols   | 165 us                                                 | 158 us: 1.04x faster                                                         |
| json_loads                 | 27.2 us                                                | 26.2 us: 1.04x faster                                                        |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.85 ms: 1.04x faster                                                        |
| crypto_pyaes               | 75.3 ms                                                | 72.5 ms: 1.04x faster                                                        |
| thrift                     | 809 us                                                 | 782 us: 1.04x faster                                                         |
| generators                 | 29.0 ms                                                | 28.0 ms: 1.03x faster                                                        |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.03x faster                                                         |
| logging_format             | 6.40 us                                                | 6.23 us: 1.03x faster                                                        |
| logging_simple             | 5.72 us                                                | 5.58 us: 1.03x faster                                                        |
| sympy_str                  | 275 ms                                                 | 268 ms: 1.02x faster                                                         |
| regex_compile              | 132 ms                                                 | 129 ms: 1.02x faster                                                         |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                         |
| xml_etree_process          | 60.6 ms                                                | 59.6 ms: 1.02x faster                                                        |
| pycparser                  | 1.20 sec                                               | 1.18 sec: 1.02x faster                                                       |
| async_generators           | 436 ms                                                 | 428 ms: 1.02x faster                                                         |
| django_template            | 35.2 ms                                                | 34.6 ms: 1.02x faster                                                        |
| sympy_expand               | 463 ms                                                 | 456 ms: 1.02x faster                                                         |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.02x faster                                                         |
| xml_etree_generate         | 86.7 ms                                                | 85.4 ms: 1.02x faster                                                        |
| tornado_http               | 92.4 ms                                                | 91.1 ms: 1.02x faster                                                        |
| pyflate                    | 471 ms                                                 | 465 ms: 1.01x faster                                                         |
| dulwich_log                | 64.3 ms                                                | 63.6 ms: 1.01x faster                                                        |
| sqlglot_optimize           | 53.7 ms                                                | 53.2 ms: 1.01x faster                                                        |
| regex_effbot               | 3.73 ms                                                | 3.69 ms: 1.01x faster                                                        |
| genshi_xml                 | 50.9 ms                                                | 50.4 ms: 1.01x faster                                                        |
| regex_dna                  | 218 ms                                                 | 217 ms: 1.01x faster                                                         |
| sympy_integrate            | 19.9 ms                                                | 19.8 ms: 1.00x faster                                                        |
| html5lib                   | 64.2 ms                                                | 63.9 ms: 1.00x faster                                                        |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                         |
| sqlglot_transpile          | 1.58 ms                                                | 1.59 ms: 1.00x slower                                                        |
| scimark_fft                | 364 ms                                                 | 365 ms: 1.00x slower                                                         |
| bpe_tokeniser              | 4.75 sec                                               | 4.77 sec: 1.01x slower                                                       |
| unpickle_pure_python       | 216 us                                                 | 217 us: 1.01x slower                                                         |
| pickle_pure_python         | 310 us                                                 | 313 us: 1.01x slower                                                         |
| coverage                   | 84.0 ms                                                | 84.7 ms: 1.01x slower                                                        |
| xml_etree_parse            | 156 ms                                                 | 157 ms: 1.01x slower                                                         |
| python_startup_no_site     | 6.96 ms                                                | 7.04 ms: 1.01x slower                                                        |
| comprehensions             | 16.5 us                                                | 16.7 us: 1.01x slower                                                        |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.01x slower                                                        |
| deltablue                  | 3.23 ms                                                | 3.29 ms: 1.02x slower                                                        |
| hexiom                     | 6.16 ms                                                | 6.29 ms: 1.02x slower                                                        |
| scimark_lu                 | 113 ms                                                 | 115 ms: 1.02x slower                                                         |
| docutils                   | 2.59 sec                                               | 2.65 sec: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 559 ms: 1.02x slower                                                         |
| bench_thread_pool          | 822 us                                                 | 841 us: 1.02x slower                                                         |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.02x slower                                                         |
| nqueens                    | 78.4 ms                                                | 80.5 ms: 1.03x slower                                                        |
| raytrace                   | 267 ms                                                 | 274 ms: 1.03x slower                                                         |
| scimark_sor                | 124 ms                                                 | 127 ms: 1.03x slower                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 105 ms: 1.03x slower                                                         |
| scimark_monte_carlo        | 67.4 ms                                                | 70.3 ms: 1.04x slower                                                        |
| logging_silent             | 102 ns                                                 | 107 ns: 1.05x slower                                                         |
| chaos                      | 58.1 ms                                                | 60.9 ms: 1.05x slower                                                        |
| mako                       | 11.1 ms                                                | 11.7 ms: 1.05x slower                                                        |
| coroutines                 | 22.7 ms                                                | 23.9 ms: 1.05x slower                                                        |
| json_dumps                 | 10.6 ms                                                | 11.3 ms: 1.07x slower                                                        |
| gc_traversal               | 4.37 ms                                                | 4.71 ms: 1.08x slower                                                        |
| nbody                      | 87.0 ms                                                | 94.4 ms: 1.09x slower                                                        |
| create_gc_cycles           | 2.41 ms                                                | 2.68 ms: 1.11x slower                                                        |
| async_tree_io_tg           | 857 ms                                                 | 981 ms: 1.14x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 78.1 ms: 3.26x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (12): async_tree_cpu_io_mixed, async_tree_io, tomli_loads, sqlalchemy_imperative, pprint_pformat, pprint_safe_repr, float, fannkuch, asyncio_websockets, async_tree_none_tg, sphinx, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path

- Geometric mean (including insignificant results): 1.016x faster
# HPT report

- Reliability score: 93.35% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x