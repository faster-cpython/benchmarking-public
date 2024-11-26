# Results vs. base

- fork: faster-cpython
- ref: load_const_return_re
- machine: linux-x86_64
- commit hash: 2a3b1e2
- commit date: 2024-10-23
- overall geometric mean: 1.004x faster
- HPT reliability: 96.22%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                                 | 254 ms: 1.00x faster                                                             |
| docutils       | 2.67 sec                                                               | 2.66 sec: 1.00x faster                                                           |
| html5lib       | 63.7 ms                                                                | 63.4 ms: 1.00x faster                                                            |
| tornado_http   | 90.1 ms                                                                | 91.4 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|--------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_generators   | 439 ms                                                                 | 427 ms: 1.03x faster                                                             |
| asyncio_websockets | 556 ms                                                                 | 553 ms: 1.01x faster                                                             |
| async_tree_io_tg   | 979 ms                                                                 | 977 ms: 1.00x faster                                                             |
| coroutines         | 23.0 ms                                                                | 23.3 ms: 1.01x slower                                                            |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (7): async_tree_memoization, async_tree_none, async_tree_io, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                 | 187 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                     |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.78 ms                                                                | 3.60 ms: 1.05x faster                                                            |
| regex_dna      | 216 ms                                                                 | 214 ms: 1.01x faster                                                             |
| regex_v8       | 25.1 ms                                                                | 25.3 ms: 1.01x slower                                                            |
| regex_compile  | 129 ms                                                                 | 131 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 11.5 ms                                                                | 11.1 ms: 1.04x faster                                                            |
| xml_etree_parse      | 160 ms                                                                 | 156 ms: 1.02x faster                                                             |
| unpickle_pure_python | 221 us                                                                 | 217 us: 1.02x faster                                                             |
| xml_etree_generate   | 86.4 ms                                                                | 87.1 ms: 1.01x slower                                                            |
| pickle_pure_python   | 311 us                                                                 | 315 us: 1.01x slower                                                             |
| tomli_loads          | 2.08 sec                                                               | 2.12 sec: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (3): json_loads, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 11.8 ms                                                                | 11.8 ms: 1.00x slower                                                            |
| python_startup_no_site | 7.04 ms                                                                | 7.05 ms: 1.00x slower                                                            |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako           | 11.5 ms                                                                | 11.4 ms: 1.01x faster                                                            |
| genshi_xml     | 51.3 ms                                                                | 52.5 ms: 1.02x slower                                                            |
| genshi_text    | 22.8 ms                                                                | 23.8 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| logging_silent           | 107 ns                                                                 | 98.3 ns: 1.09x faster                                                            |
| mdp                      | 2.69 sec                                                               | 2.50 sec: 1.07x faster                                                           |
| generators               | 28.6 ms                                                                | 26.8 ms: 1.07x faster                                                            |
| regex_effbot             | 3.78 ms                                                                | 3.60 ms: 1.05x faster                                                            |
| json_dumps               | 11.5 ms                                                                | 11.1 ms: 1.04x faster                                                            |
| scimark_fft              | 378 ms                                                                 | 365 ms: 1.03x faster                                                             |
| pyflate                  | 473 ms                                                                 | 459 ms: 1.03x faster                                                             |
| async_generators         | 439 ms                                                                 | 427 ms: 1.03x faster                                                             |
| crypto_pyaes             | 73.7 ms                                                                | 71.8 ms: 1.03x faster                                                            |
| xml_etree_parse          | 160 ms                                                                 | 156 ms: 1.02x faster                                                             |
| scimark_monte_carlo      | 70.6 ms                                                                | 69.1 ms: 1.02x faster                                                            |
| meteor_contest           | 108 ms                                                                 | 106 ms: 1.02x faster                                                             |
| go                       | 122 ms                                                                 | 120 ms: 1.02x faster                                                             |
| coverage                 | 85.9 ms                                                                | 84.4 ms: 1.02x faster                                                            |
| deepcopy_reduce          | 2.74 us                                                                | 2.69 us: 1.02x faster                                                            |
| bpe_tokeniser            | 4.85 sec                                                               | 4.77 sec: 1.02x faster                                                           |
| unpickle_pure_python     | 221 us                                                                 | 217 us: 1.02x faster                                                             |
| raytrace                 | 274 ms                                                                 | 270 ms: 1.02x faster                                                             |
| richards                 | 46.8 ms                                                                | 46.1 ms: 1.02x faster                                                            |
| spectral_norm            | 116 ms                                                                 | 114 ms: 1.01x faster                                                             |
| deltablue                | 3.30 ms                                                                | 3.26 ms: 1.01x faster                                                            |
| hexiom                   | 6.37 ms                                                                | 6.28 ms: 1.01x faster                                                            |
| mako                     | 11.5 ms                                                                | 11.4 ms: 1.01x faster                                                            |
| nqueens                  | 81.4 ms                                                                | 80.6 ms: 1.01x faster                                                            |
| regex_dna                | 216 ms                                                                 | 214 ms: 1.01x faster                                                             |
| comprehensions           | 16.7 us                                                                | 16.6 us: 1.01x faster                                                            |
| typing_runtime_protocols | 164 us                                                                 | 163 us: 1.01x faster                                                             |
| thrift                   | 778 us                                                                 | 773 us: 1.01x faster                                                             |
| asyncio_websockets       | 556 ms                                                                 | 553 ms: 1.01x faster                                                             |
| sqlglot_normalize        | 107 ms                                                                 | 106 ms: 1.00x faster                                                             |
| html5lib                 | 63.7 ms                                                                | 63.4 ms: 1.00x faster                                                            |
| 2to3                     | 255 ms                                                                 | 254 ms: 1.00x faster                                                             |
| docutils                 | 2.67 sec                                                               | 2.66 sec: 1.00x faster                                                           |
| pathlib                  | 15.9 ms                                                                | 15.8 ms: 1.00x faster                                                            |
| async_tree_io_tg         | 979 ms                                                                 | 977 ms: 1.00x faster                                                             |
| pidigits                 | 188 ms                                                                 | 187 ms: 1.00x faster                                                             |
| python_startup           | 11.8 ms                                                                | 11.8 ms: 1.00x slower                                                            |
| python_startup_no_site   | 7.04 ms                                                                | 7.05 ms: 1.00x slower                                                            |
| create_gc_cycles         | 2.66 ms                                                                | 2.67 ms: 1.00x slower                                                            |
| bench_thread_pool        | 839 us                                                                 | 842 us: 1.00x slower                                                             |
| fannkuch                 | 403 ms                                                                 | 405 ms: 1.00x slower                                                             |
| pprint_pformat           | 1.50 sec                                                               | 1.51 sec: 1.00x slower                                                           |
| bench_mp_pool            | 78.3 ms                                                                | 78.7 ms: 1.00x slower                                                            |
| sympy_integrate          | 19.8 ms                                                                | 19.9 ms: 1.01x slower                                                            |
| regex_v8                 | 25.1 ms                                                                | 25.3 ms: 1.01x slower                                                            |
| dulwich_log              | 63.5 ms                                                                | 64.0 ms: 1.01x slower                                                            |
| xml_etree_generate       | 86.4 ms                                                                | 87.1 ms: 1.01x slower                                                            |
| pycparser                | 1.13 sec                                                               | 1.14 sec: 1.01x slower                                                           |
| pickle_pure_python       | 311 us                                                                 | 315 us: 1.01x slower                                                             |
| json                     | 4.79 ms                                                                | 4.85 ms: 1.01x slower                                                            |
| coroutines               | 23.0 ms                                                                | 23.3 ms: 1.01x slower                                                            |
| tornado_http             | 90.1 ms                                                                | 91.4 ms: 1.01x slower                                                            |
| regex_compile            | 129 ms                                                                 | 131 ms: 1.02x slower                                                             |
| logging_simple           | 5.55 us                                                                | 5.64 us: 1.02x slower                                                            |
| tomli_loads              | 2.08 sec                                                               | 2.12 sec: 1.02x slower                                                           |
| scimark_lu               | 115 ms                                                                 | 117 ms: 1.02x slower                                                             |
| gc_traversal             | 4.38 ms                                                                | 4.47 ms: 1.02x slower                                                            |
| genshi_xml               | 51.3 ms                                                                | 52.5 ms: 1.02x slower                                                            |
| chaos                    | 61.2 ms                                                                | 62.6 ms: 1.02x slower                                                            |
| scimark_sor              | 129 ms                                                                 | 132 ms: 1.03x slower                                                             |
| genshi_text              | 22.8 ms                                                                | 23.8 ms: 1.05x slower                                                            |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                                     |

Benchmark hidden because not significant (28): sphinx, async_tree_memoization, async_tree_none, async_tree_io, sqlglot_parse, async_tree_cpu_io_mixed, float, sqlglot_optimize, scimark_sparse_mat_mult, sympy_str, richards_super, sqlglot_transpile, async_tree_none_tg, pylint, async_tree_cpu_io_mixed_tg, telco, json_loads, deepcopy_memo, sympy_expand, django_template, deepcopy, logging_format, nbody, sympy_sum, pprint_safe_repr, async_tree_memoization_tg, xml_etree_process, xml_etree_iterparse
Ignored benchmarks (2) of results/bm-20241022-3.14.0a1+-759a54d/bm-20241022-linux-x86_64-python-759a54d28ffe7eac8c23-3.14.0a1+-759a54d.json: sqlalchemy_declarative, sqlalchemy_imperative

- Geometric mean (including insignificant results): 1.004x faster
# HPT report

- Reliability score: 96.22% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x