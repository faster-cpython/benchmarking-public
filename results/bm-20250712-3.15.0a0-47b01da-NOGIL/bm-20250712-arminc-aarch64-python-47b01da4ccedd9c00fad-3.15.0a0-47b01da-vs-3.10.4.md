# Results vs. 3.10.4

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: linux-aarch64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.140x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.66x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 349 ms: 1.09x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.19 sec: 1.11x faster                                                  |
| html5lib       | 86.5 ms                                                               | 70.2 ms: 1.23x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 875 ms: 2.61x faster                                                    |
| async_tree_none         | 950 ms                                                                | 407 ms: 2.33x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 487 ms: 2.33x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 683 ms: 1.86x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.27x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 95.6 ms: 1.41x faster                                                   |
| pidigits       | 235 ms                                                                | 232 ms: 1.02x faster                                                    |
| nbody          | 166 ms                                                                | 181 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 26.0 ms: 1.24x faster                                                   |
| regex_compile  | 177 ms                                                                | 149 ms: 1.18x faster                                                    |
| regex_dna      | 257 ms                                                                | 237 ms: 1.09x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.94 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 303 us: 1.20x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 450 us: 1.18x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 133 ms: 1.17x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.87 sec: 1.17x faster                                                  |
| xml_etree_parse      | 212 ms                                                                | 183 ms: 1.16x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.8 ms: 1.12x faster                                                   |
| unpickle_list        | 6.99 us                                                               | 6.94 us: 1.01x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 101 ms: 1.02x slower                                                    |
| pickle_list          | 5.24 us                                                               | 5.65 us: 1.08x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 38.4 us: 1.09x slower                                                   |
| xml_etree_generate   | 123 ms                                                                | 140 ms: 1.14x slower                                                    |
| unpickle             | 17.5 us                                                               | 20.4 us: 1.17x slower                                                   |
| json_loads           | 30.9 us                                                               | 36.5 us: 1.18x slower                                                   |
| pickle               | 12.5 us                                                               | 15.7 us: 1.26x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.1 ms: 1.76x slower                                                   |
| python_startup         | 11.2 ms                                                               | 20.0 ms: 1.79x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.78x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 51.3 ms: 1.04x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 75.2 ms: 1.08x slower                                                   |
| mako            | 18.9 ms                                                               | 21.1 ms: 1.12x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.04x slower                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 246 us: 2.69x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 875 ms: 2.61x faster                                                    |
| async_tree_none          | 950 ms                                                                | 407 ms: 2.33x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 487 ms: 2.33x faster                                                    |
| mdp                      | 3.70 sec                                                              | 1.92 sec: 1.92x faster                                                  |
| deltablue                | 8.94 ms                                                               | 4.68 ms: 1.91x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 683 ms: 1.86x faster                                                    |
| go                       | 264 ms                                                                | 153 ms: 1.73x faster                                                    |
| generators               | 68.1 ms                                                               | 39.8 ms: 1.71x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 565 ms: 1.67x faster                                                    |
| logging_silent           | 222 ns                                                                | 143 ns: 1.56x faster                                                    |
| scimark_sor              | 246 ms                                                                | 163 ms: 1.51x faster                                                    |
| chaos                    | 121 ms                                                                | 80.5 ms: 1.50x faster                                                   |
| gc_traversal             | 4.15 ms                                                               | 2.87 ms: 1.45x faster                                                   |
| raytrace                 | 573 ms                                                                | 401 ms: 1.43x faster                                                    |
| float                    | 135 ms                                                                | 95.6 ms: 1.41x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.81 ms: 1.40x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.42 sec: 1.36x faster                                                  |
| comprehensions           | 33.1 us                                                               | 24.6 us: 1.35x faster                                                   |
| pyflate                  | 795 ms                                                                | 592 ms: 1.34x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 46.5 us: 1.33x faster                                                   |
| richards                 | 91.7 ms                                                               | 69.8 ms: 1.31x faster                                                   |
| richards_super           | 107 ms                                                                | 82.0 ms: 1.31x faster                                                   |
| pylint                   | 485 ms                                                                | 374 ms: 1.30x faster                                                    |
| deepcopy                 | 511 us                                                                | 394 us: 1.30x faster                                                    |
| spectral_norm            | 186 ms                                                                | 145 ms: 1.28x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 107 ms: 1.25x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.36 sec: 1.25x faster                                                  |
| regex_v8                 | 32.2 ms                                                               | 26.0 ms: 1.24x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 59.5 ms: 1.24x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 70.2 ms: 1.23x faster                                                   |
| coroutines               | 37.2 ms                                                               | 30.4 ms: 1.22x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 105 ms: 1.22x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.39 us: 1.21x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 303 us: 1.20x faster                                                    |
| scimark_lu               | 227 ms                                                                | 189 ms: 1.20x faster                                                    |
| logging_simple           | 9.78 us                                                               | 8.21 us: 1.19x faster                                                   |
| regex_compile            | 177 ms                                                                | 149 ms: 1.18x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 450 us: 1.18x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 133 ms: 1.17x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.87 sec: 1.17x faster                                                  |
| logging_format           | 10.6 us                                                               | 9.07 us: 1.17x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 183 ms: 1.16x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 23.0 ms: 1.14x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 14.8 ms: 1.12x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.19 sec: 1.11x faster                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 1.05 sec: 1.09x faster                                                  |
| 2to3                     | 381 ms                                                                | 349 ms: 1.09x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.17 sec: 1.09x faster                                                  |
| regex_dna                | 257 ms                                                                | 237 ms: 1.09x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 3.94 ms: 1.08x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 25.0 ms: 1.06x faster                                                   |
| scimark_fft              | 500 ms                                                                | 473 ms: 1.06x faster                                                    |
| thrift                   | 1.26 ms                                                               | 1.19 ms: 1.06x faster                                                   |
| django_template          | 53.3 ms                                                               | 51.3 ms: 1.04x faster                                                   |
| pidigits                 | 235 ms                                                                | 232 ms: 1.02x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.56 ms: 1.01x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.94 us: 1.01x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                                    |
| xml_etree_process        | 99.5 ms                                                               | 101 ms: 1.02x slower                                                    |
| json                     | 5.88 ms                                                               | 6.26 ms: 1.07x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 75.2 ms: 1.08x slower                                                   |
| pickle_list              | 5.24 us                                                               | 5.65 us: 1.08x slower                                                   |
| sympy_expand             | 543 ms                                                                | 586 ms: 1.08x slower                                                    |
| meteor_contest           | 126 ms                                                                | 137 ms: 1.08x slower                                                    |
| nbody                    | 166 ms                                                                | 181 ms: 1.09x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 38.4 us: 1.09x slower                                                   |
| fannkuch                 | 546 ms                                                                | 597 ms: 1.09x slower                                                    |
| mako                     | 18.9 ms                                                               | 21.1 ms: 1.12x slower                                                   |
| async_generators         | 452 ms                                                                | 505 ms: 1.12x slower                                                    |
| xml_etree_generate       | 123 ms                                                                | 140 ms: 1.14x slower                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.81 ms: 1.14x slower                                                   |
| unpickle                 | 17.5 us                                                               | 20.4 us: 1.17x slower                                                   |
| json_loads               | 30.9 us                                                               | 36.5 us: 1.18x slower                                                   |
| pickle                   | 12.5 us                                                               | 15.7 us: 1.26x slower                                                   |
| coverage                 | 83.6 ms                                                               | 142 ms: 1.69x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 12.1 ms: 1.76x slower                                                   |
| python_startup           | 11.2 ms                                                               | 20.0 ms: 1.79x slower                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 65.2 ms: 4.48x slower                                                   |
| telco                    | 8.49 ms                                                               | 190 ms: 22.36x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.10x faster                                                            |

Benchmark hidden because not significant (6): deepcopy_reduce, create_gc_cycles, sympy_sum, genshi_text, sympy_str, nqueens
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.140x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.66x