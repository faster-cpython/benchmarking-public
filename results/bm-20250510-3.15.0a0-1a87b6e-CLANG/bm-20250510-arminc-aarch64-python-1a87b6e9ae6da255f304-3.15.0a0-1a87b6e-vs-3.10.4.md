# Results vs. 3.10.4

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-aarch64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.227x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 301 ms: 1.27x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.02 sec: 1.17x faster                                                  |
| html5lib       | 86.5 ms                                                               | 60.2 ms: 1.44x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 863 ms: 2.65x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 455 ms: 2.49x faster                                                    |
| async_tree_none         | 950 ms                                                                | 383 ms: 2.48x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 721 ms: 1.77x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.32x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 86.3 ms: 1.56x faster                                                   |
| nbody          | 166 ms                                                                | 129 ms: 1.29x faster                                                    |
| pidigits       | 235 ms                                                                | 292 ms: 1.24x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.18x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 120 ms: 1.48x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.6 ms: 1.05x faster                                                   |
| regex_dna      | 257 ms                                                                | 247 ms: 1.04x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.64 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 255 us: 1.43x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.43 sec: 1.38x faster                                                  |
| pickle_pure_python   | 529 us                                                                | 385 us: 1.38x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 76.1 ms: 1.31x faster                                                   |
| unpickle_list        | 6.99 us                                                               | 5.79 us: 1.21x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 14.8 ms: 1.13x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 110 ms: 1.12x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.06x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 205 ms: 1.03x faster                                                    |
| unpickle             | 17.5 us                                                               | 17.0 us: 1.03x faster                                                   |
| pickle_dict          | 35.1 us                                                               | 36.5 us: 1.04x slower                                                   |
| pickle_list          | 5.24 us                                                               | 5.55 us: 1.06x slower                                                   |
| json_loads           | 30.9 us                                                               | 34.2 us: 1.10x slower                                                   |
| pickle               | 12.5 us                                                               | 15.1 us: 1.21x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.74 ms: 1.27x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 39.0 ms: 1.37x faster                                                   |
| mako            | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 26.7 ms: 1.32x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 61.1 ms: 1.14x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.29x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 193 us: 3.42x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 863 ms: 2.65x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 455 ms: 2.49x faster                                                    |
| async_tree_none          | 950 ms                                                                | 383 ms: 2.48x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.76 ms: 2.38x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.66 sec: 2.23x faster                                                  |
| go                       | 264 ms                                                                | 130 ms: 2.04x faster                                                    |
| generators               | 68.1 ms                                                               | 35.2 ms: 1.93x faster                                                   |
| richards_super           | 107 ms                                                                | 55.6 ms: 1.93x faster                                                   |
| richards                 | 91.7 ms                                                               | 49.0 ms: 1.87x faster                                                   |
| raytrace                 | 573 ms                                                                | 320 ms: 1.79x faster                                                    |
| chaos                    | 121 ms                                                                | 68.1 ms: 1.78x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 721 ms: 1.77x faster                                                    |
| scimark_sor              | 246 ms                                                                | 142 ms: 1.73x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 35.7 us: 1.73x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 558 ms: 1.69x faster                                                    |
| scimark_lu               | 227 ms                                                                | 137 ms: 1.66x faster                                                    |
| comprehensions           | 33.1 us                                                               | 20.3 us: 1.63x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 78.7 ms: 1.62x faster                                                   |
| deepcopy                 | 511 us                                                                | 318 us: 1.61x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 84.2 ms: 1.59x faster                                                   |
| float                    | 135 ms                                                                | 86.3 ms: 1.56x faster                                                   |
| pylint                   | 485 ms                                                                | 315 ms: 1.54x faster                                                    |
| spectral_norm            | 186 ms                                                                | 121 ms: 1.54x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.13 ms: 1.53x faster                                                   |
| pyflate                  | 795 ms                                                                | 523 ms: 1.52x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.49x faster                                                  |
| regex_compile            | 177 ms                                                                | 120 ms: 1.48x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 60.2 ms: 1.44x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 255 us: 1.43x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 53.2 ms: 1.38x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.43 sec: 1.38x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 385 us: 1.38x faster                                                    |
| django_template          | 53.3 ms                                                               | 39.0 ms: 1.37x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.36 us: 1.37x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.25 sec: 1.35x faster                                                  |
| mako                     | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 19.9 ms: 1.33x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 26.7 ms: 1.32x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.47 us: 1.31x faster                                                   |
| logging_format           | 10.6 us                                                               | 8.10 us: 1.31x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 76.1 ms: 1.31x faster                                                   |
| nbody                    | 166 ms                                                                | 129 ms: 1.29x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.8 ms: 1.29x faster                                                   |
| sympy_sum                | 184 ms                                                                | 143 ms: 1.28x faster                                                    |
| 2to3                     | 381 ms                                                                | 301 ms: 1.27x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.88 sec: 1.26x faster                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 926 ms: 1.24x faster                                                    |
| scimark_fft              | 500 ms                                                                | 407 ms: 1.23x faster                                                    |
| sympy_str                | 329 ms                                                                | 267 ms: 1.23x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.6 ms: 1.22x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 5.79 us: 1.21x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.32 ms: 1.20x faster                                                   |
| sympy_expand             | 543 ms                                                                | 458 ms: 1.18x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.02 sec: 1.17x faster                                                  |
| nqueens                  | 117 ms                                                                | 101 ms: 1.16x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 61.1 ms: 1.14x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 14.8 ms: 1.13x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.77 ms: 1.13x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 110 ms: 1.12x faster                                                    |
| fannkuch                 | 546 ms                                                                | 487 ms: 1.12x faster                                                    |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.09x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.88 us: 1.06x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.06x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.6 ms: 1.05x faster                                                   |
| async_generators         | 452 ms                                                                | 432 ms: 1.05x faster                                                    |
| regex_dna                | 257 ms                                                                | 247 ms: 1.04x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 205 ms: 1.03x faster                                                    |
| unpickle                 | 17.5 us                                                               | 17.0 us: 1.03x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 666 ms: 1.01x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 36.5 us: 1.04x slower                                                   |
| pickle_list              | 5.24 us                                                               | 5.55 us: 1.06x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.64 ms: 1.09x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.36 ms: 1.10x slower                                                   |
| json_loads               | 30.9 us                                                               | 34.2 us: 1.10x slower                                                   |
| pickle                   | 12.5 us                                                               | 15.1 us: 1.21x slower                                                   |
| pidigits                 | 235 ms                                                                | 292 ms: 1.24x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.74 ms: 1.27x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.73 ms: 1.62x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.85 ms: 1.70x slower                                                   |
| logging_silent           | 222 ns                                                                | 631 ns: 2.84x slower                                                    |
| coverage                 | 83.6 ms                                                               | 534 ms: 6.39x slower                                                    |
| thrift                   | 1.26 ms                                                               | 192 ms: 152.04x slower                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 3.51 sec: 241.18x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.12x faster                                                            |

Benchmark hidden because not significant (1): json
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.227x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.41x