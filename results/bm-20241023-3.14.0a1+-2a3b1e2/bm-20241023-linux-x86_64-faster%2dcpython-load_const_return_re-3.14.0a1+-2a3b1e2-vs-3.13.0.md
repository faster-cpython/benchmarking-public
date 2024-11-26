# Results vs. 3.13.0

- fork: faster-cpython
- ref: load_const_return_re
- machine: linux-x86_64
- commit hash: 2a3b1e2
- commit date: 2024-10-23
- overall geometric mean: 1.015x faster
- HPT reliability: 77.78%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 254 ms: 1.05x faster                                                             |
| docutils       | 2.59 sec                                               | 2.66 sec: 1.02x slower                                                           |
| html5lib       | 64.2 ms                                                | 63.4 ms: 1.01x faster                                                            |
| tornado_http   | 92.4 ms                                                | 91.4 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 386 ms: 1.20x faster                                                             |
| async_tree_none            | 351 ms                                                 | 327 ms: 1.07x faster                                                             |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                                             |
| async_generators           | 436 ms                                                 | 427 ms: 1.02x faster                                                             |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 566 ms: 1.02x faster                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 556 ms: 1.02x slower                                                             |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                                            |
| async_tree_io_tg           | 857 ms                                                 | 977 ms: 1.14x slower                                                             |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.01x slower                                                             |
| float          | 79.2 ms                                                | 80.3 ms: 1.01x slower                                                            |
| nbody          | 87.0 ms                                                | 95.8 ms: 1.10x slower                                                            |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.3 ms: 1.04x faster                                                            |
| regex_effbot   | 3.73 ms                                                | 3.60 ms: 1.04x faster                                                            |
| regex_dna      | 218 ms                                                 | 214 ms: 1.02x faster                                                             |
| regex_compile  | 132 ms                                                 | 131 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 27.2 us                                                | 26.2 us: 1.04x faster                                                            |
| tomli_loads          | 2.14 sec                                               | 2.12 sec: 1.01x faster                                                           |
| xml_etree_process    | 60.6 ms                                                | 60.1 ms: 1.01x faster                                                            |
| xml_etree_generate   | 86.7 ms                                                | 87.1 ms: 1.00x slower                                                            |
| unpickle_pure_python | 216 us                                                 | 217 us: 1.01x slower                                                             |
| pickle_pure_python   | 310 us                                                 | 315 us: 1.01x slower                                                             |
| json_dumps           | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                            |
| xml_etree_iterparse  | 101 ms                                                 | 106 ms: 1.05x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.8 ms: 1.06x faster                                                            |
| python_startup_no_site | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 34.8 ms: 1.01x faster                                                            |
| genshi_text     | 23.5 ms                                                | 23.8 ms: 1.01x slower                                                            |
| mako            | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                            |
| genshi_xml      | 50.9 ms                                                | 52.5 ms: 1.03x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 263 us: 1.36x faster                                                             |
| deepcopy_memo              | 39.1 us                                                | 31.1 us: 1.26x faster                                                            |
| async_tree_memoization_tg  | 464 ms                                                 | 386 ms: 1.20x faster                                                             |
| go                         | 144 ms                                                 | 120 ms: 1.20x faster                                                             |
| deepcopy_reduce            | 3.20 us                                                | 2.69 us: 1.19x faster                                                            |
| pathlib                    | 17.5 ms                                                | 15.8 ms: 1.11x faster                                                            |
| json                       | 5.36 ms                                                | 4.85 ms: 1.10x faster                                                            |
| mdp                        | 2.72 sec                                               | 2.50 sec: 1.09x faster                                                           |
| generators                 | 29.0 ms                                                | 26.8 ms: 1.08x faster                                                            |
| async_tree_none            | 351 ms                                                 | 327 ms: 1.07x faster                                                             |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                                             |
| telco                      | 8.54 ms                                                | 8.02 ms: 1.07x faster                                                            |
| python_startup             | 12.5 ms                                                | 11.8 ms: 1.06x faster                                                            |
| richards                   | 48.7 ms                                                | 46.1 ms: 1.06x faster                                                            |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                                           |
| crypto_pyaes               | 75.3 ms                                                | 71.8 ms: 1.05x faster                                                            |
| 2to3                       | 267 ms                                                 | 254 ms: 1.05x faster                                                             |
| thrift                     | 809 us                                                 | 773 us: 1.05x faster                                                             |
| richards_super             | 54.9 ms                                                | 52.7 ms: 1.04x faster                                                            |
| json_loads                 | 27.2 us                                                | 26.2 us: 1.04x faster                                                            |
| regex_v8                   | 26.2 ms                                                | 25.3 ms: 1.04x faster                                                            |
| regex_effbot               | 3.73 ms                                                | 3.60 ms: 1.04x faster                                                            |
| logging_silent             | 102 ns                                                 | 98.3 ns: 1.03x faster                                                            |
| logging_format             | 6.40 us                                                | 6.18 us: 1.03x faster                                                            |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.03x faster                                                             |
| sympy_str                  | 275 ms                                                 | 267 ms: 1.03x faster                                                             |
| pyflate                    | 471 ms                                                 | 459 ms: 1.03x faster                                                             |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                             |
| async_generators           | 436 ms                                                 | 427 ms: 1.02x faster                                                             |
| regex_dna                  | 218 ms                                                 | 214 ms: 1.02x faster                                                             |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 566 ms: 1.02x faster                                                             |
| sympy_expand               | 463 ms                                                 | 456 ms: 1.02x faster                                                             |
| logging_simple             | 5.72 us                                                | 5.64 us: 1.01x faster                                                            |
| typing_runtime_protocols   | 165 us                                                 | 163 us: 1.01x faster                                                             |
| sqlglot_normalize          | 108 ms                                                 | 106 ms: 1.01x faster                                                             |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                             |
| html5lib                   | 64.2 ms                                                | 63.4 ms: 1.01x faster                                                            |
| tornado_http               | 92.4 ms                                                | 91.4 ms: 1.01x faster                                                            |
| tomli_loads                | 2.14 sec                                               | 2.12 sec: 1.01x faster                                                           |
| django_template            | 35.2 ms                                                | 34.8 ms: 1.01x faster                                                            |
| regex_compile              | 132 ms                                                 | 131 ms: 1.01x faster                                                             |
| xml_etree_process          | 60.6 ms                                                | 60.1 ms: 1.01x faster                                                            |
| sqlglot_optimize           | 53.7 ms                                                | 53.3 ms: 1.01x faster                                                            |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.01 ms: 1.01x faster                                                            |
| dulwich_log                | 64.3 ms                                                | 64.0 ms: 1.01x faster                                                            |
| scimark_fft                | 364 ms                                                 | 365 ms: 1.00x slower                                                             |
| coverage                   | 84.0 ms                                                | 84.4 ms: 1.00x slower                                                            |
| xml_etree_generate         | 86.7 ms                                                | 87.1 ms: 1.00x slower                                                            |
| bpe_tokeniser              | 4.75 sec                                               | 4.77 sec: 1.01x slower                                                           |
| pidigits                   | 186 ms                                                 | 187 ms: 1.01x slower                                                             |
| comprehensions             | 16.5 us                                                | 16.6 us: 1.01x slower                                                            |
| unpickle_pure_python       | 216 us                                                 | 217 us: 1.01x slower                                                             |
| sqlglot_transpile          | 1.58 ms                                                | 1.60 ms: 1.01x slower                                                            |
| pprint_pformat             | 1.49 sec                                               | 1.51 sec: 1.01x slower                                                           |
| deltablue                  | 3.23 ms                                                | 3.26 ms: 1.01x slower                                                            |
| raytrace                   | 267 ms                                                 | 270 ms: 1.01x slower                                                             |
| python_startup_no_site     | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                            |
| genshi_text                | 23.5 ms                                                | 23.8 ms: 1.01x slower                                                            |
| pprint_safe_repr           | 728 ms                                                 | 738 ms: 1.01x slower                                                             |
| float                      | 79.2 ms                                                | 80.3 ms: 1.01x slower                                                            |
| pickle_pure_python         | 310 us                                                 | 315 us: 1.01x slower                                                             |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 556 ms: 1.02x slower                                                             |
| sqlglot_parse              | 1.27 ms                                                | 1.30 ms: 1.02x slower                                                            |
| hexiom                     | 6.16 ms                                                | 6.28 ms: 1.02x slower                                                            |
| gc_traversal               | 4.37 ms                                                | 4.47 ms: 1.02x slower                                                            |
| docutils                   | 2.59 sec                                               | 2.66 sec: 1.02x slower                                                           |
| bench_thread_pool          | 822 us                                                 | 842 us: 1.02x slower                                                             |
| scimark_monte_carlo        | 67.4 ms                                                | 69.1 ms: 1.02x slower                                                            |
| coroutines                 | 22.7 ms                                                | 23.3 ms: 1.03x slower                                                            |
| mako                       | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                            |
| nqueens                    | 78.4 ms                                                | 80.6 ms: 1.03x slower                                                            |
| genshi_xml                 | 50.9 ms                                                | 52.5 ms: 1.03x slower                                                            |
| scimark_lu                 | 113 ms                                                 | 117 ms: 1.04x slower                                                             |
| json_dumps                 | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                            |
| xml_etree_iterparse        | 101 ms                                                 | 106 ms: 1.05x slower                                                             |
| scimark_sor                | 124 ms                                                 | 132 ms: 1.07x slower                                                             |
| chaos                      | 58.1 ms                                                | 62.6 ms: 1.08x slower                                                            |
| nbody                      | 87.0 ms                                                | 95.8 ms: 1.10x slower                                                            |
| create_gc_cycles           | 2.41 ms                                                | 2.67 ms: 1.11x slower                                                            |
| async_tree_io_tg           | 857 ms                                                 | 977 ms: 1.14x slower                                                             |
| bench_mp_pool              | 24.0 ms                                                | 78.7 ms: 3.28x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (8): sympy_integrate, fannkuch, asyncio_websockets, async_tree_none_tg, xml_etree_parse, sphinx, async_tree_io, pylint
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.015x faster
# HPT report

- Reliability score: 77.78% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x