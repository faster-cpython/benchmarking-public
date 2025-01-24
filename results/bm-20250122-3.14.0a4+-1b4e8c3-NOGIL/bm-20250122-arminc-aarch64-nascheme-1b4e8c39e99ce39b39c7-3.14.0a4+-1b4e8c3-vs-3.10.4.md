# Results vs. 3.10.4

- fork: nascheme
- ref: 1b4e8c39e99ce39b39c7
- machine: linux-aarch64
- commit hash: 1b4e8c3
- commit date: 2025-01-22
- overall geometric mean: 1.093x faster
- HPT reliability: 99.83%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.57x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 3.53 sec                                                              | 3.38 sec: 1.04x faster                                                     |
| html5lib       | 86.5 ms                                                               | 79.2 ms: 1.09x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                               |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 952 ms: 2.40x faster                                                       |
| async_tree_none         | 950 ms                                                                | 430 ms: 2.21x faster                                                       |
| async_tree_memoization  | 1.13 sec                                                              | 545 ms: 2.08x faster                                                       |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 721 ms: 1.76x faster                                                       |
| Geometric mean          | (ref)                                                                 | 2.10x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 102 ms: 1.32x faster                                                       |
| nbody          | 166 ms                                                                | 188 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 162 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                               |

Benchmark hidden because not significant (3): regex_effbot, regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 315 us: 1.16x faster                                                       |
| pickle_pure_python   | 529 us                                                                | 480 us: 1.10x faster                                                       |
| tomli_loads          | 3.36 sec                                                              | 3.18 sec: 1.06x faster                                                     |
| json_loads           | 30.9 us                                                               | 37.6 us: 1.22x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.02x faster                                                               |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.3 ms: 1.78x slower                                                      |
| python_startup         | 11.2 ms                                                               | 20.4 ms: 1.83x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.80x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 57.2 ms: 1.07x slower                                                      |
| genshi_text     | 35.2 ms                                                               | 38.5 ms: 1.09x slower                                                      |
| genshi_xml      | 69.8 ms                                                               | 77.9 ms: 1.11x slower                                                      |
| mako            | 18.9 ms                                                               | 23.3 ms: 1.23x slower                                                      |
| Geometric mean  | (ref)                                                                 | 1.13x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io            | 2.28 sec                                                              | 952 ms: 2.40x faster                                                       |
| typing_runtime_protocols | 661 us                                                                | 282 us: 2.34x faster                                                       |
| async_tree_none          | 950 ms                                                                | 430 ms: 2.21x faster                                                       |
| async_tree_memoization   | 1.13 sec                                                              | 545 ms: 2.08x faster                                                       |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 721 ms: 1.76x faster                                                       |
| generators               | 68.1 ms                                                               | 44.0 ms: 1.55x faster                                                      |
| deltablue                | 8.94 ms                                                               | 6.10 ms: 1.47x faster                                                      |
| go                       | 264 ms                                                                | 181 ms: 1.46x faster                                                       |
| logging_silent           | 222 ns                                                                | 157 ns: 1.41x faster                                                       |
| scimark_sor              | 246 ms                                                                | 179 ms: 1.38x faster                                                       |
| chaos                    | 121 ms                                                                | 89.8 ms: 1.35x faster                                                      |
| raytrace                 | 573 ms                                                                | 429 ms: 1.34x faster                                                       |
| float                    | 135 ms                                                                | 102 ms: 1.32x faster                                                       |
| spectral_norm            | 186 ms                                                                | 148 ms: 1.26x faster                                                       |
| pylint                   | 485 ms                                                                | 392 ms: 1.24x faster                                                       |
| richards                 | 91.7 ms                                                               | 74.4 ms: 1.23x faster                                                      |
| richards_super           | 107 ms                                                                | 87.2 ms: 1.23x faster                                                      |
| sqlglot_parse            | 2.40 ms                                                               | 2.02 ms: 1.19x faster                                                      |
| scimark_lu               | 227 ms                                                                | 192 ms: 1.18x faster                                                       |
| pyflate                  | 795 ms                                                                | 674 ms: 1.18x faster                                                       |
| deepcopy                 | 511 us                                                                | 433 us: 1.18x faster                                                       |
| sqlglot_transpile        | 2.84 ms                                                               | 2.41 ms: 1.18x faster                                                      |
| comprehensions           | 33.1 us                                                               | 28.2 us: 1.17x faster                                                      |
| unpickle_pure_python     | 366 us                                                                | 315 us: 1.16x faster                                                       |
| pycparser                | 1.69 sec                                                              | 1.46 sec: 1.16x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 116 ms: 1.16x faster                                                       |
| deepcopy_memo            | 61.7 us                                                               | 54.1 us: 1.14x faster                                                      |
| pathlib                  | 26.3 ms                                                               | 23.2 ms: 1.14x faster                                                      |
| hexiom                   | 10.9 ms                                                               | 9.64 ms: 1.13x faster                                                      |
| coroutines               | 37.2 ms                                                               | 33.3 ms: 1.12x faster                                                      |
| sqlite_synth             | 4.12 us                                                               | 3.71 us: 1.11x faster                                                      |
| pickle_pure_python       | 529 us                                                                | 480 us: 1.10x faster                                                       |
| scimark_monte_carlo      | 128 ms                                                                | 117 ms: 1.10x faster                                                       |
| html5lib                 | 86.5 ms                                                               | 79.2 ms: 1.09x faster                                                      |
| regex_compile            | 177 ms                                                                | 162 ms: 1.09x faster                                                       |
| logging_simple           | 9.78 us                                                               | 9.06 us: 1.08x faster                                                      |
| tomli_loads              | 3.36 sec                                                              | 3.18 sec: 1.06x faster                                                     |
| logging_format           | 10.6 us                                                               | 10.2 us: 1.04x faster                                                      |
| docutils                 | 3.53 sec                                                              | 3.38 sec: 1.04x faster                                                     |
| asyncio_websockets       | 657 ms                                                                | 686 ms: 1.04x slower                                                       |
| mdp                      | 3.70 sec                                                              | 3.87 sec: 1.05x slower                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 79.3 ms: 1.05x slower                                                      |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.12 ms: 1.06x slower                                                      |
| django_template          | 53.3 ms                                                               | 57.2 ms: 1.07x slower                                                      |
| sympy_integrate          | 26.5 ms                                                               | 28.5 ms: 1.07x slower                                                      |
| sympy_sum                | 184 ms                                                                | 199 ms: 1.08x slower                                                       |
| sqlalchemy_imperative    | 20.5 ms                                                               | 22.4 ms: 1.09x slower                                                      |
| json                     | 5.88 ms                                                               | 6.41 ms: 1.09x slower                                                      |
| genshi_text              | 35.2 ms                                                               | 38.5 ms: 1.09x slower                                                      |
| genshi_xml               | 69.8 ms                                                               | 77.9 ms: 1.11x slower                                                      |
| sympy_expand             | 543 ms                                                                | 605 ms: 1.11x slower                                                       |
| sympy_str                | 329 ms                                                                | 368 ms: 1.12x slower                                                       |
| nbody                    | 166 ms                                                                | 188 ms: 1.13x slower                                                       |
| nqueens                  | 117 ms                                                                | 134 ms: 1.14x slower                                                       |
| async_generators         | 452 ms                                                                | 533 ms: 1.18x slower                                                       |
| bench_thread_pool        | 1.59 ms                                                               | 1.89 ms: 1.19x slower                                                      |
| json_loads               | 30.9 us                                                               | 37.6 us: 1.22x slower                                                      |
| meteor_contest           | 126 ms                                                                | 154 ms: 1.22x slower                                                       |
| mako                     | 18.9 ms                                                               | 23.3 ms: 1.23x slower                                                      |
| fannkuch                 | 546 ms                                                                | 680 ms: 1.25x slower                                                       |
| gc_traversal             | 4.15 ms                                                               | 5.41 ms: 1.30x slower                                                      |
| telco                    | 8.49 ms                                                               | 11.7 ms: 1.38x slower                                                      |
| coverage                 | 83.6 ms                                                               | 129 ms: 1.55x slower                                                       |
| python_startup_no_site   | 6.89 ms                                                               | 12.3 ms: 1.78x slower                                                      |
| python_startup           | 11.2 ms                                                               | 20.4 ms: 1.83x slower                                                      |
| bench_mp_pool            | 14.5 ms                                                               | 59.2 ms: 4.08x slower                                                      |
| Geometric mean           | (ref)                                                                 | 1.05x faster                                                               |

Benchmark hidden because not significant (15): regex_effbot, scimark_fft, pidigits, regex_v8, regex_dna, dulwich_log, 2to3, pprint_safe_repr, pprint_pformat, deepcopy_reduce, json_dumps, create_gc_cycles, sqlglot_normalize, sqlalchemy_declarative, thrift
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list, xml_etree_generate, xml_etree_iterparse, xml_etree_parse, xml_etree_process
Ignored benchmarks (11) of results/bm-20250122-3.14.0a4+-1b4e8c3-NOGIL/bm-20250122-arminc-aarch64-nascheme-1b4e8c39e99ce39b39c7-3.14.0a4+-1b4e8c3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.093x faster

# HPT report

- Reliability score: 99.83% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.57x