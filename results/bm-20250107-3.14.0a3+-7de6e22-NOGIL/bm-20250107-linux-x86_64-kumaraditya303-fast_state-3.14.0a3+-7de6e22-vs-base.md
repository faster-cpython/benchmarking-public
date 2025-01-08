# Results vs. base

- fork: kumaraditya303
- ref: fast_state
- machine: linux-x86_64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.002x faster
- HPT reliability: 99.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                                 | 345 ms: 1.01x faster                                                 |
| docutils       | 2.97 sec                                                               | 2.99 sec: 1.00x slower                                               |
| html5lib       | 87.4 ms                                                                | 85.7 ms: 1.02x faster                                                |
| sphinx         | 1.16 sec                                                               | 1.17 sec: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io              | 743 ms                                                                 | 726 ms: 1.02x faster                                                 |
| async_tree_memoization     | 439 ms                                                                 | 430 ms: 1.02x faster                                                 |
| async_tree_io_tg           | 688 ms                                                                 | 675 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed    | 590 ms                                                                 | 580 ms: 1.02x faster                                                 |
| coroutines                 | 27.2 ms                                                                | 26.8 ms: 1.02x faster                                                |
| async_tree_none            | 344 ms                                                                 | 339 ms: 1.02x faster                                                 |
| async_tree_none_tg         | 297 ms                                                                 | 292 ms: 1.01x faster                                                 |
| async_tree_memoization_tg  | 390 ms                                                                 | 385 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed_tg | 536 ms                                                                 | 529 ms: 1.01x faster                                                 |
| async_generators           | 496 ms                                                                 | 501 ms: 1.01x slower                                                 |
| Geometric mean             | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 108 ms                                                                 | 105 ms: 1.02x faster                                                 |
| pidigits       | 181 ms                                                                 | 181 ms: 1.00x faster                                                 |
| nbody          | 131 ms                                                                 | 136 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 164 ms                                                                 | 162 ms: 1.01x faster                                                 |
| regex_v8       | 25.1 ms                                                                | 25.2 ms: 1.01x slower                                                |
| regex_effbot   | 3.48 ms                                                                | 3.59 ms: 1.03x slower                                                |
| regex_dna      | 222 ms                                                                 | 231 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|---------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps          | 13.1 ms                                                                | 13.0 ms: 1.01x faster                                                |
| xml_etree_iterparse | 96.4 ms                                                                | 95.7 ms: 1.01x faster                                                |
| xml_etree_process   | 72.6 ms                                                                | 72.3 ms: 1.01x faster                                                |
| pickle_pure_python  | 479 us                                                                 | 482 us: 1.01x slower                                                 |
| xml_etree_parse     | 147 ms                                                                 | 148 ms: 1.01x slower                                                 |
| json_loads          | 29.5 us                                                                | 30.3 us: 1.02x slower                                                |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (3): xml_etree_generate, unpickle_pure_python, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 15.5 ms                                                                | 15.5 ms: 1.00x faster                                                |
| python_startup_no_site | 9.61 ms                                                                | 9.59 ms: 1.00x faster                                                |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text    | 30.8 ms                                                                | 30.4 ms: 1.01x faster                                                |
| mako           | 18.1 ms                                                                | 18.2 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mdp                        | 2.99 sec                                                               | 2.86 sec: 1.05x faster                                               |
| pyflate                    | 666 ms                                                                 | 651 ms: 1.02x faster                                                 |
| async_tree_io              | 743 ms                                                                 | 726 ms: 1.02x faster                                                 |
| deepcopy_memo              | 41.2 us                                                                | 40.3 us: 1.02x faster                                                |
| raytrace                   | 474 ms                                                                 | 465 ms: 1.02x faster                                                 |
| generators                 | 36.6 ms                                                                | 35.9 ms: 1.02x faster                                                |
| async_tree_memoization     | 439 ms                                                                 | 430 ms: 1.02x faster                                                 |
| html5lib                   | 87.4 ms                                                                | 85.7 ms: 1.02x faster                                                |
| go                         | 223 ms                                                                 | 218 ms: 1.02x faster                                                 |
| async_tree_io_tg           | 688 ms                                                                 | 675 ms: 1.02x faster                                                 |
| float                      | 108 ms                                                                 | 105 ms: 1.02x faster                                                 |
| deepcopy_reduce            | 3.38 us                                                                | 3.32 us: 1.02x faster                                                |
| async_tree_cpu_io_mixed    | 590 ms                                                                 | 580 ms: 1.02x faster                                                 |
| coroutines                 | 27.2 ms                                                                | 26.8 ms: 1.02x faster                                                |
| async_tree_none            | 344 ms                                                                 | 339 ms: 1.02x faster                                                 |
| richards                   | 64.0 ms                                                                | 63.1 ms: 1.02x faster                                                |
| richards_super             | 71.4 ms                                                                | 70.3 ms: 1.02x faster                                                |
| async_tree_none_tg         | 297 ms                                                                 | 292 ms: 1.01x faster                                                 |
| async_tree_memoization_tg  | 390 ms                                                                 | 385 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed_tg | 536 ms                                                                 | 529 ms: 1.01x faster                                                 |
| genshi_text                | 30.8 ms                                                                | 30.4 ms: 1.01x faster                                                |
| subparsers                 | 26.8 ms                                                                | 26.5 ms: 1.01x faster                                                |
| meteor_contest             | 133 ms                                                                 | 131 ms: 1.01x faster                                                 |
| deltablue                  | 7.13 ms                                                                | 7.05 ms: 1.01x faster                                                |
| fannkuch                   | 531 ms                                                                 | 526 ms: 1.01x faster                                                 |
| json_dumps                 | 13.1 ms                                                                | 13.0 ms: 1.01x faster                                                |
| regex_compile              | 164 ms                                                                 | 162 ms: 1.01x faster                                                 |
| k_core                     | 2.49 sec                                                               | 2.47 sec: 1.01x faster                                               |
| chaos                      | 93.4 ms                                                                | 92.7 ms: 1.01x faster                                                |
| sqlalchemy_declarative     | 182 ms                                                                 | 180 ms: 1.01x faster                                                 |
| 2to3                       | 348 ms                                                                 | 345 ms: 1.01x faster                                                 |
| xml_etree_iterparse        | 96.4 ms                                                                | 95.7 ms: 1.01x faster                                                |
| logging_format             | 8.87 us                                                                | 8.81 us: 1.01x faster                                                |
| dulwich_log                | 75.9 ms                                                                | 75.5 ms: 1.01x faster                                                |
| connected_components       | 540 ms                                                                 | 537 ms: 1.01x faster                                                 |
| xml_etree_process          | 72.6 ms                                                                | 72.3 ms: 1.01x faster                                                |
| sympy_sum                  | 184 ms                                                                 | 183 ms: 1.00x faster                                                 |
| bench_mp_pool              | 95.4 ms                                                                | 95.0 ms: 1.00x faster                                                |
| create_gc_cycles           | 2.34 ms                                                                | 2.33 ms: 1.00x faster                                                |
| sympy_str                  | 335 ms                                                                 | 333 ms: 1.00x faster                                                 |
| shortest_path              | 580 ms                                                                 | 578 ms: 1.00x faster                                                 |
| python_startup             | 15.5 ms                                                                | 15.5 ms: 1.00x faster                                                |
| hexiom                     | 9.53 ms                                                                | 9.50 ms: 1.00x faster                                                |
| python_startup_no_site     | 9.61 ms                                                                | 9.59 ms: 1.00x faster                                                |
| crypto_pyaes               | 92.5 ms                                                                | 92.3 ms: 1.00x faster                                                |
| pidigits                   | 181 ms                                                                 | 181 ms: 1.00x faster                                                 |
| comprehensions             | 25.3 us                                                                | 25.4 us: 1.00x slower                                                |
| bpe_tokeniser              | 5.29 sec                                                               | 5.30 sec: 1.00x slower                                               |
| docutils                   | 2.97 sec                                                               | 2.99 sec: 1.00x slower                                               |
| deepcopy                   | 317 us                                                                 | 319 us: 1.01x slower                                                 |
| pickle_pure_python         | 479 us                                                                 | 482 us: 1.01x slower                                                 |
| mako                       | 18.1 ms                                                                | 18.2 ms: 1.01x slower                                                |
| regex_v8                   | 25.1 ms                                                                | 25.2 ms: 1.01x slower                                                |
| sphinx                     | 1.16 sec                                                               | 1.17 sec: 1.01x slower                                               |
| scimark_lu                 | 153 ms                                                                 | 154 ms: 1.01x slower                                                 |
| xml_etree_parse            | 147 ms                                                                 | 148 ms: 1.01x slower                                                 |
| scimark_fft                | 414 ms                                                                 | 417 ms: 1.01x slower                                                 |
| pycparser                  | 1.36 sec                                                               | 1.37 sec: 1.01x slower                                               |
| sqlite_synth               | 2.80 us                                                                | 2.83 us: 1.01x slower                                                |
| async_generators           | 496 ms                                                                 | 501 ms: 1.01x slower                                                 |
| json                       | 5.26 ms                                                                | 5.31 ms: 1.01x slower                                                |
| sqlglot_parse              | 2.18 ms                                                                | 2.21 ms: 1.01x slower                                                |
| spectral_norm              | 125 ms                                                                 | 127 ms: 1.01x slower                                                 |
| scimark_sparse_mat_mult    | 6.03 ms                                                                | 6.14 ms: 1.02x slower                                                |
| logging_silent             | 173 ns                                                                 | 176 ns: 1.02x slower                                                 |
| gc_traversal               | 3.67 ms                                                                | 3.75 ms: 1.02x slower                                                |
| json_loads                 | 29.5 us                                                                | 30.3 us: 1.02x slower                                                |
| regex_effbot               | 3.48 ms                                                                | 3.59 ms: 1.03x slower                                                |
| nbody                      | 131 ms                                                                 | 136 ms: 1.04x slower                                                 |
| regex_dna                  | 222 ms                                                                 | 231 ms: 1.04x slower                                                 |
| scimark_sor                | 215 ms                                                                 | 223 ms: 1.04x slower                                                 |
| Geometric mean             | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (26): pathlib, django_template, asyncio_websockets, sympy_expand, pprint_safe_repr, sympy_integrate, pprint_pformat, thrift, xml_etree_generate, many_optionals, sqlglot_normalize, unpickle_pure_python, telco, bench_thread_pool, tomli_loads, mypy2, sqlglot_optimize, scimark_monte_carlo, nqueens, genshi_xml, pylint, logging_simple, typing_runtime_protocols, sqlglot_transpile, coverage, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 99.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x