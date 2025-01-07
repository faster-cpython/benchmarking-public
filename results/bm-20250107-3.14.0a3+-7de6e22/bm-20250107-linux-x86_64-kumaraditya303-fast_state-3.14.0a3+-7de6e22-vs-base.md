# Results vs. base

- fork: kumaraditya303
- ref: fast_state
- machine: linux-x86_64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.000x faster
- HPT reliability: 89.66%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 255 ms                                                                 | 256 ms: 1.00x slower                                                 |
| docutils       | 2.61 sec                                                               | 2.62 sec: 1.00x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|---------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io             | 611 ms                                                                 | 577 ms: 1.06x faster                                                 |
| async_tree_none           | 264 ms                                                                 | 257 ms: 1.03x faster                                                 |
| async_tree_memoization    | 330 ms                                                                 | 322 ms: 1.02x faster                                                 |
| async_tree_memoization_tg | 302 ms                                                                 | 298 ms: 1.01x faster                                                 |
| async_tree_none_tg        | 243 ms                                                                 | 246 ms: 1.01x slower                                                 |
| Geometric mean            | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (6): coroutines, asyncio_websockets, async_generators, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                 | 187 ms: 1.01x faster                                                 |
| nbody          | 98.6 ms                                                                | 97.2 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                                 | 128 ms: 1.00x faster                                                 |
| regex_effbot   | 3.40 ms                                                                | 3.43 ms: 1.01x slower                                                |
| regex_v8       | 25.7 ms                                                                | 26.4 ms: 1.03x slower                                                |
| regex_dna      | 214 ms                                                                 | 223 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|---------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate  | 86.0 ms                                                                | 84.8 ms: 1.01x faster                                                |
| xml_etree_iterparse | 97.5 ms                                                                | 96.6 ms: 1.01x faster                                                |
| json_loads          | 26.3 us                                                                | 26.4 us: 1.00x slower                                                |
| json_dumps          | 11.3 ms                                                                | 11.5 ms: 1.01x slower                                                |
| tomli_loads         | 1.98 sec                                                               | 2.01 sec: 1.02x slower                                               |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (4): pickle_pure_python, unpickle_pure_python, xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.07 ms                                                                | 7.07 ms: 1.00x slower                                                |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 22.5 ms                                                                | 22.1 ms: 1.02x faster                                                |
| genshi_xml      | 50.3 ms                                                                | 49.8 ms: 1.01x faster                                                |
| django_template | 31.6 ms                                                                | 31.4 ms: 1.01x faster                                                |
| mako            | 11.7 ms                                                                | 11.8 ms: 1.01x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                         |

All benchmarks:
===============

| Benchmark                 | bm-20250105-linux-x86_64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-linux-x86_64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|---------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mdp                       | 2.71 sec                                                               | 2.53 sec: 1.07x faster                                               |
| async_tree_io             | 611 ms                                                                 | 577 ms: 1.06x faster                                                 |
| async_tree_none           | 264 ms                                                                 | 257 ms: 1.03x faster                                                 |
| coverage                  | 84.6 ms                                                                | 82.7 ms: 1.02x faster                                                |
| async_tree_memoization    | 330 ms                                                                 | 322 ms: 1.02x faster                                                 |
| crypto_pyaes              | 71.8 ms                                                                | 70.4 ms: 1.02x faster                                                |
| scimark_fft               | 351 ms                                                                 | 345 ms: 1.02x faster                                                 |
| genshi_text               | 22.5 ms                                                                | 22.1 ms: 1.02x faster                                                |
| spectral_norm             | 105 ms                                                                 | 103 ms: 1.02x faster                                                 |
| deepcopy_reduce           | 2.66 us                                                                | 2.62 us: 1.01x faster                                                |
| async_tree_memoization_tg | 302 ms                                                                 | 298 ms: 1.01x faster                                                 |
| pidigits                  | 189 ms                                                                 | 187 ms: 1.01x faster                                                 |
| nbody                     | 98.6 ms                                                                | 97.2 ms: 1.01x faster                                                |
| xml_etree_generate        | 86.0 ms                                                                | 84.8 ms: 1.01x faster                                                |
| sqlalchemy_imperative     | 16.6 ms                                                                | 16.5 ms: 1.01x faster                                                |
| genshi_xml                | 50.3 ms                                                                | 49.8 ms: 1.01x faster                                                |
| xml_etree_iterparse       | 97.5 ms                                                                | 96.6 ms: 1.01x faster                                                |
| subparsers                | 20.8 ms                                                                | 20.6 ms: 1.01x faster                                                |
| sqlglot_transpile         | 1.60 ms                                                                | 1.59 ms: 1.01x faster                                                |
| scimark_monte_carlo       | 68.7 ms                                                                | 68.2 ms: 1.01x faster                                                |
| django_template           | 31.6 ms                                                                | 31.4 ms: 1.01x faster                                                |
| logging_format            | 6.26 us                                                                | 6.22 us: 1.01x faster                                                |
| pprint_safe_repr          | 728 ms                                                                 | 724 ms: 1.01x faster                                                 |
| many_optionals            | 948 us                                                                 | 942 us: 1.01x faster                                                 |
| scimark_sparse_mat_mult   | 4.83 ms                                                                | 4.81 ms: 1.01x faster                                                |
| sqlglot_normalize         | 104 ms                                                                 | 104 ms: 1.01x faster                                                 |
| sqlglot_parse             | 1.27 ms                                                                | 1.27 ms: 1.00x faster                                                |
| deepcopy                  | 260 us                                                                 | 259 us: 1.00x faster                                                 |
| sympy_integrate           | 20.0 ms                                                                | 19.9 ms: 1.00x faster                                                |
| regex_compile             | 128 ms                                                                 | 128 ms: 1.00x faster                                                 |
| sqlalchemy_declarative    | 129 ms                                                                 | 129 ms: 1.00x faster                                                 |
| sqlglot_optimize          | 52.7 ms                                                                | 52.6 ms: 1.00x faster                                                |
| python_startup_no_site    | 7.07 ms                                                                | 7.07 ms: 1.00x slower                                                |
| pyflate                   | 457 ms                                                                 | 458 ms: 1.00x slower                                                 |
| bpe_tokeniser             | 4.51 sec                                                               | 4.53 sec: 1.00x slower                                               |
| 2to3                      | 255 ms                                                                 | 256 ms: 1.00x slower                                                 |
| docutils                  | 2.61 sec                                                               | 2.62 sec: 1.00x slower                                               |
| json_loads                | 26.3 us                                                                | 26.4 us: 1.00x slower                                                |
| regex_effbot              | 3.40 ms                                                                | 3.43 ms: 1.01x slower                                                |
| meteor_contest            | 108 ms                                                                 | 108 ms: 1.01x slower                                                 |
| sympy_sum                 | 147 ms                                                                 | 149 ms: 1.01x slower                                                 |
| mako                      | 11.7 ms                                                                | 11.8 ms: 1.01x slower                                                |
| comprehensions            | 17.3 us                                                                | 17.4 us: 1.01x slower                                                |
| fannkuch                  | 401 ms                                                                 | 404 ms: 1.01x slower                                                 |
| raytrace                  | 271 ms                                                                 | 274 ms: 1.01x slower                                                 |
| generators                | 28.2 ms                                                                | 28.4 ms: 1.01x slower                                                |
| chaos                     | 60.2 ms                                                                | 60.7 ms: 1.01x slower                                                |
| create_gc_cycles          | 2.44 ms                                                                | 2.46 ms: 1.01x slower                                                |
| json_dumps                | 11.3 ms                                                                | 11.5 ms: 1.01x slower                                                |
| scimark_lu                | 117 ms                                                                 | 118 ms: 1.01x slower                                                 |
| sqlite_synth              | 2.81 us                                                                | 2.85 us: 1.01x slower                                                |
| async_tree_none_tg        | 243 ms                                                                 | 246 ms: 1.01x slower                                                 |
| deltablue                 | 3.25 ms                                                                | 3.30 ms: 1.02x slower                                                |
| hexiom                    | 6.21 ms                                                                | 6.31 ms: 1.02x slower                                                |
| tomli_loads               | 1.98 sec                                                               | 2.01 sec: 1.02x slower                                               |
| go                        | 117 ms                                                                 | 119 ms: 1.02x slower                                                 |
| json                      | 4.88 ms                                                                | 4.97 ms: 1.02x slower                                                |
| regex_v8                  | 25.7 ms                                                                | 26.4 ms: 1.03x slower                                                |
| nqueens                   | 79.8 ms                                                                | 82.0 ms: 1.03x slower                                                |
| logging_silent            | 104 ns                                                                 | 107 ns: 1.03x slower                                                 |
| gc_traversal              | 4.78 ms                                                                | 4.93 ms: 1.03x slower                                                |
| regex_dna                 | 214 ms                                                                 | 223 ms: 1.04x slower                                                 |
| pycparser                 | 1.13 sec                                                               | 1.18 sec: 1.04x slower                                               |
| Geometric mean            | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (34): html5lib, logging_simple, coroutines, bench_mp_pool, telco, richards_super, float, pickle_pure_python, asyncio_websockets, typing_runtime_protocols, unpickle_pure_python, dulwich_log, async_generators, python_startup, pylint, async_tree_cpu_io_mixed_tg, bench_thread_pool, thrift, scimark_sor, richards, mypy2, async_tree_io_tg, deepcopy_memo, pprint_pformat, xml_etree_process, sympy_expand, sympy_str, pathlib, xml_etree_parse, connected_components, async_tree_cpu_io_mixed, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 89.66% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x