# Results vs. base

- fork: faster-cpython
- ref: specialize_binary_op
- machine: linux-x86_64
- commit hash: 5386b2d
- commit date: 2024-05-29
- overall geometric mean: 1.00x slower
- HPT reliability: 56.05%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 277 ms                                                                | 279 ms: 1.01x slower                                                            |
| html5lib       | 69.2 ms                                                               | 66.9 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_none, async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 72.4 ms                                                               | 71.7 ms: 1.01x faster                                                           |
| pidigits       | 188 ms                                                                | 189 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 24.5 ms                                                               | 24.1 ms: 1.02x faster                                                           |
| regex_compile  | 139 ms                                                                | 137 ms: 1.02x faster                                                            |
| regex_dna      | 231 ms                                                                | 229 ms: 1.01x faster                                                            |
| regex_effbot   | 3.63 ms                                                               | 3.69 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle             | 15.3 us                                                               | 14.7 us: 1.04x faster                                                           |
| pickle_dict          | 36.4 us                                                               | 36.0 us: 1.01x faster                                                           |
| xml_etree_generate   | 82.9 ms                                                               | 82.0 ms: 1.01x faster                                                           |
| unpickle_list        | 5.53 us                                                               | 5.48 us: 1.01x faster                                                           |
| xml_etree_iterparse  | 101 ms                                                                | 100 ms: 1.01x faster                                                            |
| pickle_pure_python   | 302 us                                                                | 300 us: 1.01x faster                                                            |
| unpickle_pure_python | 223 us                                                                | 222 us: 1.00x faster                                                            |
| json_dumps           | 10.4 ms                                                               | 10.4 ms: 1.01x slower                                                           |
| pickle_list          | 5.06 us                                                               | 5.26 us: 1.04x slower                                                           |
| tomli_loads          | 1.96 sec                                                              | 2.09 sec: 1.07x slower                                                          |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (4): xml_etree_parse, json_loads, xml_etree_process, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 11.1 ms                                                               | 11.1 ms: 1.00x faster                                                           |
| python_startup_no_site | 7.61 ms                                                               | 7.59 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 37.4 ms                                                               | 36.1 ms: 1.04x faster                                                           |
| genshi_xml      | 59.0 ms                                                               | 58.2 ms: 1.01x faster                                                           |
| mako            | 10.1 ms                                                               | 10.2 ms: 1.01x slower                                                           |
| genshi_text     | 25.0 ms                                                               | 25.4 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark               | bm-20240529-linux-x86_64-python-1f481fd3275dbc12a88c-3.14.0a0-1f481fd | bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template         | 37.4 ms                                                               | 36.1 ms: 1.04x faster                                                           |
| unpickle                | 15.3 us                                                               | 14.7 us: 1.04x faster                                                           |
| pyflate                 | 464 ms                                                                | 448 ms: 1.04x faster                                                            |
| html5lib                | 69.2 ms                                                               | 66.9 ms: 1.03x faster                                                           |
| coroutines              | 23.2 ms                                                               | 22.5 ms: 1.03x faster                                                           |
| regex_v8                | 24.5 ms                                                               | 24.1 ms: 1.02x faster                                                           |
| regex_compile           | 139 ms                                                                | 137 ms: 1.02x faster                                                            |
| pprint_pformat          | 1.47 sec                                                              | 1.45 sec: 1.02x faster                                                          |
| logging_format          | 6.29 us                                                               | 6.20 us: 1.01x faster                                                           |
| generators              | 30.7 ms                                                               | 30.3 ms: 1.01x faster                                                           |
| crypto_pyaes            | 68.5 ms                                                               | 67.6 ms: 1.01x faster                                                           |
| genshi_xml              | 59.0 ms                                                               | 58.2 ms: 1.01x faster                                                           |
| pickle_dict             | 36.4 us                                                               | 36.0 us: 1.01x faster                                                           |
| sqlglot_normalize       | 115 ms                                                                | 114 ms: 1.01x faster                                                            |
| xml_etree_generate      | 82.9 ms                                                               | 82.0 ms: 1.01x faster                                                           |
| create_gc_cycles        | 1.81 ms                                                               | 1.80 ms: 1.01x faster                                                           |
| chaos                   | 59.5 ms                                                               | 58.9 ms: 1.01x faster                                                           |
| float                   | 72.4 ms                                                               | 71.7 ms: 1.01x faster                                                           |
| regex_dna               | 231 ms                                                                | 229 ms: 1.01x faster                                                            |
| unpickle_list           | 5.53 us                                                               | 5.48 us: 1.01x faster                                                           |
| xml_etree_iterparse     | 101 ms                                                                | 100 ms: 1.01x faster                                                            |
| richards_super          | 48.3 ms                                                               | 47.9 ms: 1.01x faster                                                           |
| pickle_pure_python      | 302 us                                                                | 300 us: 1.01x faster                                                            |
| thrift                  | 823 us                                                                | 817 us: 1.01x faster                                                            |
| logging_simple          | 5.68 us                                                               | 5.65 us: 1.01x faster                                                           |
| unpickle_pure_python    | 223 us                                                                | 222 us: 1.00x faster                                                            |
| python_startup          | 11.1 ms                                                               | 11.1 ms: 1.00x faster                                                           |
| python_startup_no_site  | 7.61 ms                                                               | 7.59 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl         | 1.86 sec                                                              | 1.86 sec: 1.00x faster                                                          |
| pidigits                | 188 ms                                                                | 189 ms: 1.00x slower                                                            |
| 2to3                    | 277 ms                                                                | 279 ms: 1.01x slower                                                            |
| hexiom                  | 6.63 ms                                                               | 6.67 ms: 1.01x slower                                                           |
| json_dumps              | 10.4 ms                                                               | 10.4 ms: 1.01x slower                                                           |
| bench_thread_pool       | 864 us                                                                | 870 us: 1.01x slower                                                            |
| pathlib                 | 16.4 ms                                                               | 16.6 ms: 1.01x slower                                                           |
| go                      | 147 ms                                                                | 148 ms: 1.01x slower                                                            |
| scimark_monte_carlo     | 61.9 ms                                                               | 62.5 ms: 1.01x slower                                                           |
| meteor_contest          | 108 ms                                                                | 109 ms: 1.01x slower                                                            |
| mako                    | 10.1 ms                                                               | 10.2 ms: 1.01x slower                                                           |
| sqlite_synth            | 2.87 us                                                               | 2.90 us: 1.01x slower                                                           |
| logging_silent          | 107 ns                                                                | 108 ns: 1.01x slower                                                            |
| sqlglot_transpile       | 1.65 ms                                                               | 1.67 ms: 1.01x slower                                                           |
| sympy_sum               | 171 ms                                                                | 173 ms: 1.01x slower                                                            |
| sqlglot_parse           | 1.32 ms                                                               | 1.34 ms: 1.01x slower                                                           |
| genshi_text             | 25.0 ms                                                               | 25.4 ms: 1.02x slower                                                           |
| regex_effbot            | 3.63 ms                                                               | 3.69 ms: 1.02x slower                                                           |
| raytrace                | 278 ms                                                                | 284 ms: 1.02x slower                                                            |
| pickle_list             | 5.06 us                                                               | 5.26 us: 1.04x slower                                                           |
| scimark_sor             | 130 ms                                                                | 136 ms: 1.05x slower                                                            |
| scimark_lu              | 122 ms                                                                | 128 ms: 1.05x slower                                                            |
| mdp                     | 2.61 sec                                                              | 2.74 sec: 1.05x slower                                                          |
| gc_traversal            | 3.83 ms                                                               | 4.04 ms: 1.05x slower                                                           |
| tomli_loads             | 1.96 sec                                                              | 2.09 sec: 1.07x slower                                                          |
| scimark_fft             | 312 ms                                                                | 335 ms: 1.07x slower                                                            |
| scimark_sparse_mat_mult | 4.39 ms                                                               | 4.82 ms: 1.10x slower                                                           |
| spectral_norm           | 102 ms                                                                | 118 ms: 1.15x slower                                                            |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (39): async_tree_io_tg, async_tree_none, pprint_safe_repr, xml_etree_parse, async_tree_io, richards, comprehensions, nqueens, async_tree_none_tg, deepcopy, async_generators, telco, sympy_expand, pylint, bench_mp_pool, asyncio_websockets, async_tree_cpu_io_mixed, tornado_http, fannkuch, nbody, sympy_str, json_loads, async_tree_memoization, sqlglot_optimize, xml_etree_process, sympy_integrate, dask, asyncio_tcp, typing_runtime_protocols, pickle, coverage, async_tree_cpu_io_mixed_tg, dulwich_log, json, async_tree_memoization_tg, pycparser, deltablue, deepcopy_reduce, deepcopy_memo
Ignored benchmarks (1) of results/bm-20240529-3.14.0a0-5386b2d-JIT/bm-20240529-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-5386b2d.json: docutils

# HPT report

- Reliability score: 56.05% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x