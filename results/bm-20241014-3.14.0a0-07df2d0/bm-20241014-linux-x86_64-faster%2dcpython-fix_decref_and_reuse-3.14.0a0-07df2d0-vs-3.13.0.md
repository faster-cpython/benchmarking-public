# Results vs. 3.13.0

- fork: faster-cpython
- ref: fix_decref_and_reuse
- machine: linux-x86_64
- commit hash: 07df2d0
- commit date: 2024-10-14
- overall geometric mean: 1.023x faster
- HPT reliability: 96.92%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 255 ms: 1.05x faster                                                            |
| docutils       | 2.59 sec                                               | 2.62 sec: 1.01x slower                                                          |
| html5lib       | 64.2 ms                                                | 62.1 ms: 1.03x faster                                                           |
| tornado_http   | 92.4 ms                                                | 90.4 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|--------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_websockets | 552 ms                                                 | 555 ms: 1.01x slower                                                            |
| coroutines         | 22.7 ms                                                | 23.4 ms: 1.03x slower                                                           |
| Geometric mean     | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 78.3 ms: 1.01x faster                                                           |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| nbody          | 87.0 ms                                                | 94.2 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.0 ms: 1.05x faster                                                           |
| regex_effbot   | 3.73 ms                                                | 3.63 ms: 1.03x faster                                                           |
| regex_compile  | 132 ms                                                 | 129 ms: 1.02x faster                                                            |
| regex_dna      | 218 ms                                                 | 221 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 27.2 us                                                | 26.8 us: 1.02x faster                                                           |
| xml_etree_process    | 60.6 ms                                                | 59.8 ms: 1.01x faster                                                           |
| xml_etree_generate   | 86.7 ms                                                | 86.3 ms: 1.00x faster                                                           |
| pickle_pure_python   | 310 us                                                 | 313 us: 1.01x slower                                                            |
| unpickle_pure_python | 216 us                                                 | 222 us: 1.03x slower                                                            |
| xml_etree_iterparse  | 101 ms                                                 | 105 ms: 1.04x slower                                                            |
| json_dumps           | 10.6 ms                                                | 11.2 ms: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): tomli_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                           |
| python_startup_no_site | 6.96 ms                                                | 7.02 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 34.1 ms: 1.03x faster                                                           |
| genshi_text     | 23.5 ms                                                | 23.0 ms: 1.02x faster                                                           |
| genshi_xml      | 50.9 ms                                                | 51.9 ms: 1.02x slower                                                           |
| mako            | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                 | 358 us                                                 | 261 us: 1.38x faster                                                            |
| create_gc_cycles         | 2.41 ms                                                | 1.78 ms: 1.35x faster                                                           |
| deepcopy_memo            | 39.1 us                                                | 31.2 us: 1.25x faster                                                           |
| deepcopy_reduce          | 3.20 us                                                | 2.68 us: 1.20x faster                                                           |
| python_startup           | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                           |
| go                       | 144 ms                                                 | 122 ms: 1.18x faster                                                            |
| gc_traversal             | 4.37 ms                                                | 3.89 ms: 1.12x faster                                                           |
| pathlib                  | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                           |
| mdp                      | 2.72 sec                                               | 2.53 sec: 1.07x faster                                                          |
| telco                    | 8.54 ms                                                | 8.00 ms: 1.07x faster                                                           |
| pycparser                | 1.20 sec                                               | 1.13 sec: 1.07x faster                                                          |
| scimark_sparse_mat_mult  | 5.04 ms                                                | 4.76 ms: 1.06x faster                                                           |
| json                     | 5.36 ms                                                | 5.09 ms: 1.05x faster                                                           |
| regex_v8                 | 26.2 ms                                                | 25.0 ms: 1.05x faster                                                           |
| 2to3                     | 267 ms                                                 | 255 ms: 1.05x faster                                                            |
| thrift                   | 809 us                                                 | 779 us: 1.04x faster                                                            |
| generators               | 29.0 ms                                                | 28.0 ms: 1.04x faster                                                           |
| richards_super           | 54.9 ms                                                | 53.0 ms: 1.03x faster                                                           |
| html5lib                 | 64.2 ms                                                | 62.1 ms: 1.03x faster                                                           |
| typing_runtime_protocols | 165 us                                                 | 160 us: 1.03x faster                                                            |
| django_template          | 35.2 ms                                                | 34.1 ms: 1.03x faster                                                           |
| richards                 | 48.7 ms                                                | 47.3 ms: 1.03x faster                                                           |
| regex_effbot             | 3.73 ms                                                | 3.63 ms: 1.03x faster                                                           |
| sympy_str                | 275 ms                                                 | 268 ms: 1.03x faster                                                            |
| sympy_sum                | 150 ms                                                 | 147 ms: 1.03x faster                                                            |
| genshi_text              | 23.5 ms                                                | 23.0 ms: 1.02x faster                                                           |
| meteor_contest           | 109 ms                                                 | 106 ms: 1.02x faster                                                            |
| regex_compile            | 132 ms                                                 | 129 ms: 1.02x faster                                                            |
| tornado_http             | 92.4 ms                                                | 90.4 ms: 1.02x faster                                                           |
| logging_format           | 6.40 us                                                | 6.26 us: 1.02x faster                                                           |
| pyflate                  | 471 ms                                                 | 462 ms: 1.02x faster                                                            |
| sympy_expand             | 463 ms                                                 | 455 ms: 1.02x faster                                                            |
| logging_simple           | 5.72 us                                                | 5.62 us: 1.02x faster                                                           |
| crypto_pyaes             | 75.3 ms                                                | 74.1 ms: 1.02x faster                                                           |
| json_loads               | 27.2 us                                                | 26.8 us: 1.02x faster                                                           |
| xml_etree_process        | 60.6 ms                                                | 59.8 ms: 1.01x faster                                                           |
| float                    | 79.2 ms                                                | 78.3 ms: 1.01x faster                                                           |
| spectral_norm            | 115 ms                                                 | 114 ms: 1.01x faster                                                            |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.01x faster                                                            |
| sqlglot_optimize         | 53.7 ms                                                | 53.4 ms: 1.01x faster                                                           |
| bpe_tokeniser            | 4.75 sec                                               | 4.71 sec: 1.01x faster                                                          |
| xml_etree_generate       | 86.7 ms                                                | 86.3 ms: 1.00x faster                                                           |
| sympy_integrate          | 19.9 ms                                                | 19.8 ms: 1.00x faster                                                           |
| dulwich_log              | 64.3 ms                                                | 64.2 ms: 1.00x faster                                                           |
| asyncio_websockets       | 552 ms                                                 | 555 ms: 1.01x slower                                                            |
| sqlglot_transpile        | 1.58 ms                                                | 1.59 ms: 1.01x slower                                                           |
| pickle_pure_python       | 310 us                                                 | 313 us: 1.01x slower                                                            |
| scimark_fft              | 364 ms                                                 | 367 ms: 1.01x slower                                                            |
| docutils                 | 2.59 sec                                               | 2.62 sec: 1.01x slower                                                          |
| pidigits                 | 186 ms                                                 | 188 ms: 1.01x slower                                                            |
| python_startup_no_site   | 6.96 ms                                                | 7.02 ms: 1.01x slower                                                           |
| regex_dna                | 218 ms                                                 | 221 ms: 1.01x slower                                                            |
| coverage                 | 84.0 ms                                                | 85.0 ms: 1.01x slower                                                           |
| raytrace                 | 267 ms                                                 | 271 ms: 1.01x slower                                                            |
| sqlglot_parse            | 1.27 ms                                                | 1.29 ms: 1.02x slower                                                           |
| fannkuch                 | 404 ms                                                 | 411 ms: 1.02x slower                                                            |
| comprehensions           | 16.5 us                                                | 16.8 us: 1.02x slower                                                           |
| genshi_xml               | 50.9 ms                                                | 51.9 ms: 1.02x slower                                                           |
| bench_thread_pool        | 822 us                                                 | 838 us: 1.02x slower                                                            |
| scimark_lu               | 113 ms                                                 | 116 ms: 1.03x slower                                                            |
| deltablue                | 3.23 ms                                                | 3.31 ms: 1.03x slower                                                           |
| scimark_sor              | 124 ms                                                 | 127 ms: 1.03x slower                                                            |
| unpickle_pure_python     | 216 us                                                 | 222 us: 1.03x slower                                                            |
| mako                     | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                           |
| coroutines               | 22.7 ms                                                | 23.4 ms: 1.03x slower                                                           |
| scimark_monte_carlo      | 67.4 ms                                                | 69.7 ms: 1.03x slower                                                           |
| hexiom                   | 6.16 ms                                                | 6.38 ms: 1.04x slower                                                           |
| xml_etree_iterparse      | 101 ms                                                 | 105 ms: 1.04x slower                                                            |
| nqueens                  | 78.4 ms                                                | 81.4 ms: 1.04x slower                                                           |
| chaos                    | 58.1 ms                                                | 61.0 ms: 1.05x slower                                                           |
| json_dumps               | 10.6 ms                                                | 11.2 ms: 1.06x slower                                                           |
| logging_silent           | 102 ns                                                 | 109 ns: 1.07x slower                                                            |
| nbody                    | 87.0 ms                                                | 94.2 ms: 1.08x slower                                                           |
| bench_mp_pool            | 24.0 ms                                                | 56.2 ms: 2.34x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (6): tomli_loads, pprint_pformat, pprint_safe_repr, async_generators, xml_etree_parse, pylint
Ignored benchmarks (17) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241014-3.14.0a0-07df2d0/bm-20241014-linux-x86_64-faster%2dcpython-fix_decref_and_reuse-3.14.0a0-07df2d0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.023x faster
# HPT report

- Reliability score: 96.92% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x