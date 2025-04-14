# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_stackrefs_single
- machine: linux-aarch64
- commit hash: 916faf4
- commit date: 2025-03-07
- overall geometric mean: 1.290x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 311 ms: 1.23x faster                                                               |
| docutils       | 3.53 sec                                                              | 3.06 sec: 1.15x faster                                                             |
| html5lib       | 86.5 ms                                                               | 66.4 ms: 1.30x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 933 ms: 2.45x faster                                                               |
| async_tree_none         | 950 ms                                                                | 394 ms: 2.41x faster                                                               |
| async_tree_memoization  | 1.13 sec                                                              | 486 ms: 2.33x faster                                                               |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 695 ms: 1.83x faster                                                               |
| Geometric mean          | (ref)                                                                 | 2.24x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 91.7 ms: 1.47x faster                                                              |
| nbody          | 166 ms                                                                | 128 ms: 1.29x faster                                                               |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 133 ms: 1.32x faster                                                               |
| regex_effbot   | 4.25 ms                                                               | 4.04 ms: 1.05x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                                       |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 405 us: 1.31x faster                                                               |
| tomli_loads          | 3.36 sec                                                              | 2.58 sec: 1.30x faster                                                             |
| unpickle_pure_python | 366 us                                                                | 284 us: 1.29x faster                                                               |
| xml_etree_process    | 99.5 ms                                                               | 83.9 ms: 1.19x faster                                                              |
| json_dumps           | 16.7 ms                                                               | 14.6 ms: 1.14x faster                                                              |
| xml_etree_parse      | 212 ms                                                                | 189 ms: 1.12x faster                                                               |
| xml_etree_iterparse  | 156 ms                                                                | 147 ms: 1.06x faster                                                               |
| json_loads           | 30.9 us                                                               | 34.5 us: 1.12x slower                                                              |
| Geometric mean       | (ref)                                                                 | 1.14x faster                                                                       |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.10 ms: 1.32x slower                                                              |
| python_startup         | 11.2 ms                                                               | 16.5 ms: 1.48x slower                                                              |
| Geometric mean         | (ref)                                                                 | 1.40x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 40.8 ms: 1.31x faster                                                              |
| mako            | 18.9 ms                                                               | 14.9 ms: 1.27x faster                                                              |
| genshi_text     | 35.2 ms                                                               | 28.6 ms: 1.23x faster                                                              |
| genshi_xml      | 69.8 ms                                                               | 63.4 ms: 1.10x faster                                                              |
| Geometric mean  | (ref)                                                                 | 1.23x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 203 us: 3.25x faster                                                               |
| async_tree_io            | 2.28 sec                                                              | 933 ms: 2.45x faster                                                               |
| async_tree_none          | 950 ms                                                                | 394 ms: 2.41x faster                                                               |
| async_tree_memoization   | 1.13 sec                                                              | 486 ms: 2.33x faster                                                               |
| deltablue                | 8.94 ms                                                               | 4.21 ms: 2.12x faster                                                              |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 695 ms: 1.83x faster                                                               |
| generators               | 68.1 ms                                                               | 37.4 ms: 1.82x faster                                                              |
| go                       | 264 ms                                                                | 147 ms: 1.80x faster                                                               |
| raytrace                 | 573 ms                                                                | 329 ms: 1.74x faster                                                               |
| richards_super           | 107 ms                                                                | 63.1 ms: 1.70x faster                                                              |
| richards                 | 91.7 ms                                                               | 54.8 ms: 1.67x faster                                                              |
| chaos                    | 121 ms                                                                | 73.7 ms: 1.64x faster                                                              |
| logging_silent           | 222 ns                                                                | 138 ns: 1.61x faster                                                               |
| sqlglot_parse            | 2.40 ms                                                               | 1.52 ms: 1.58x faster                                                              |
| sqlglot_transpile        | 2.84 ms                                                               | 1.85 ms: 1.53x faster                                                              |
| deepcopy_memo            | 61.7 us                                                               | 40.4 us: 1.53x faster                                                              |
| scimark_sor              | 246 ms                                                                | 162 ms: 1.51x faster                                                               |
| spectral_norm            | 186 ms                                                                | 125 ms: 1.49x faster                                                               |
| pylint                   | 485 ms                                                                | 326 ms: 1.49x faster                                                               |
| comprehensions           | 33.1 us                                                               | 22.4 us: 1.48x faster                                                              |
| deepcopy                 | 511 us                                                                | 347 us: 1.47x faster                                                               |
| float                    | 135 ms                                                                | 91.7 ms: 1.47x faster                                                              |
| scimark_monte_carlo      | 128 ms                                                                | 88.0 ms: 1.45x faster                                                              |
| scimark_lu               | 227 ms                                                                | 157 ms: 1.44x faster                                                               |
| crypto_pyaes             | 134 ms                                                                | 93.4 ms: 1.43x faster                                                              |
| hexiom                   | 10.9 ms                                                               | 7.68 ms: 1.42x faster                                                              |
| regex_compile            | 177 ms                                                                | 133 ms: 1.32x faster                                                               |
| logging_format           | 10.6 us                                                               | 8.03 us: 1.32x faster                                                              |
| pyflate                  | 795 ms                                                                | 607 ms: 1.31x faster                                                               |
| pickle_pure_python       | 529 us                                                                | 405 us: 1.31x faster                                                               |
| django_template          | 53.3 ms                                                               | 40.8 ms: 1.31x faster                                                              |
| html5lib                 | 86.5 ms                                                               | 66.4 ms: 1.30x faster                                                              |
| tomli_loads              | 3.36 sec                                                              | 2.58 sec: 1.30x faster                                                             |
| sqlalchemy_declarative   | 197 ms                                                                | 152 ms: 1.30x faster                                                               |
| nbody                    | 166 ms                                                                | 128 ms: 1.29x faster                                                               |
| unpickle_pure_python     | 366 us                                                                | 284 us: 1.29x faster                                                               |
| logging_simple           | 9.78 us                                                               | 7.64 us: 1.28x faster                                                              |
| sympy_sum                | 184 ms                                                                | 144 ms: 1.28x faster                                                               |
| mako                     | 18.9 ms                                                               | 14.9 ms: 1.27x faster                                                              |
| deepcopy_reduce          | 4.60 us                                                               | 3.62 us: 1.27x faster                                                              |
| pycparser                | 1.69 sec                                                              | 1.33 sec: 1.27x faster                                                             |
| thrift                   | 1.26 ms                                                               | 995 us: 1.27x faster                                                               |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.6 ms: 1.24x faster                                                              |
| genshi_text              | 35.2 ms                                                               | 28.6 ms: 1.23x faster                                                              |
| 2to3                     | 381 ms                                                                | 311 ms: 1.23x faster                                                               |
| coroutines               | 37.2 ms                                                               | 30.9 ms: 1.20x faster                                                              |
| sqlglot_optimize         | 75.4 ms                                                               | 63.2 ms: 1.19x faster                                                              |
| sympy_integrate          | 26.5 ms                                                               | 22.3 ms: 1.19x faster                                                              |
| sqlglot_normalize        | 156 ms                                                                | 131 ms: 1.19x faster                                                               |
| xml_etree_process        | 99.5 ms                                                               | 83.9 ms: 1.19x faster                                                              |
| sympy_str                | 329 ms                                                                | 278 ms: 1.18x faster                                                               |
| dulwich_log              | 73.5 ms                                                               | 63.1 ms: 1.16x faster                                                              |
| docutils                 | 3.53 sec                                                              | 3.06 sec: 1.15x faster                                                             |
| pprint_pformat           | 2.36 sec                                                              | 2.05 sec: 1.15x faster                                                             |
| bench_thread_pool        | 1.59 ms                                                               | 1.38 ms: 1.15x faster                                                              |
| scimark_fft              | 500 ms                                                                | 435 ms: 1.15x faster                                                               |
| sympy_expand             | 543 ms                                                                | 474 ms: 1.14x faster                                                               |
| json_dumps               | 16.7 ms                                                               | 14.6 ms: 1.14x faster                                                              |
| pprint_safe_repr         | 1.15 sec                                                              | 1.00 sec: 1.14x faster                                                             |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.69 ms: 1.14x faster                                                              |
| pathlib                  | 26.3 ms                                                               | 23.2 ms: 1.14x faster                                                              |
| xml_etree_parse          | 212 ms                                                                | 189 ms: 1.12x faster                                                               |
| genshi_xml               | 69.8 ms                                                               | 63.4 ms: 1.10x faster                                                              |
| nqueens                  | 117 ms                                                                | 107 ms: 1.10x faster                                                               |
| mdp                      | 3.70 sec                                                              | 3.43 sec: 1.08x faster                                                             |
| xml_etree_iterparse      | 156 ms                                                                | 147 ms: 1.06x faster                                                               |
| regex_effbot             | 4.25 ms                                                               | 4.04 ms: 1.05x faster                                                              |
| fannkuch                 | 546 ms                                                                | 528 ms: 1.03x faster                                                               |
| async_generators         | 452 ms                                                                | 467 ms: 1.03x slower                                                               |
| asyncio_websockets       | 657 ms                                                                | 678 ms: 1.03x slower                                                               |
| json_loads               | 30.9 us                                                               | 34.5 us: 1.12x slower                                                              |
| telco                    | 8.49 ms                                                               | 9.79 ms: 1.15x slower                                                              |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                                               |
| python_startup_no_site   | 6.89 ms                                                               | 9.10 ms: 1.32x slower                                                              |
| python_startup           | 11.2 ms                                                               | 16.5 ms: 1.48x slower                                                              |
| create_gc_cycles         | 2.26 ms                                                               | 3.60 ms: 1.59x slower                                                              |
| gc_traversal             | 4.15 ms                                                               | 7.13 ms: 1.72x slower                                                              |
| bench_mp_pool            | 14.5 ms                                                               | 4.66 sec: 320.45x slower                                                           |
| Geometric mean           | (ref)                                                                 | 1.18x faster                                                                       |

Benchmark hidden because not significant (7): meteor_contest, xml_etree_generate, pidigits, regex_dna, sqlite_synth, regex_v8, json
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250307-3.14.0a5+-916faf4/bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.290x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.30x