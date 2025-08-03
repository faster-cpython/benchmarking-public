# Results vs. 3.10.4

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: linux-aarch64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.311x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 301 ms: 1.27x faster                                                    |
| docutils       | 3.53 sec                                                              | 2.94 sec: 1.20x faster                                                  |
| html5lib       | 86.5 ms                                                               | 60.8 ms: 1.42x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 879 ms: 2.60x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 456 ms: 2.48x faster                                                    |
| async_tree_none         | 950 ms                                                                | 383 ms: 2.48x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 654 ms: 1.94x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.36x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 84.7 ms: 1.59x faster                                                   |
| nbody          | 166 ms                                                                | 124 ms: 1.34x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 121 ms: 1.46x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 27.2 ms: 1.18x faster                                                   |
| regex_dna      | 257 ms                                                                | 222 ms: 1.16x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.86 ms: 1.10x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.22x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 261 us: 1.40x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                                  |
| pickle_pure_python   | 529 us                                                                | 396 us: 1.34x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 78.6 ms: 1.27x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.7 ms: 1.21x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 178 ms: 1.19x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 110 ms: 1.12x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.11x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.47 us: 1.08x faster                                                   |
| unpickle             | 17.5 us                                                               | 18.5 us: 1.06x slower                                                   |
| pickle_list          | 5.24 us                                                               | 5.59 us: 1.07x slower                                                   |
| json_loads           | 30.9 us                                                               | 33.1 us: 1.07x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 38.1 us: 1.09x slower                                                   |
| pickle               | 12.5 us                                                               | 15.7 us: 1.26x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.58 ms: 1.25x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                   |
| django_template | 53.3 ms                                                               | 40.2 ms: 1.33x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.4 ms: 1.28x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.7 ms: 1.15x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 195 us: 3.40x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 879 ms: 2.60x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 456 ms: 2.48x faster                                                    |
| async_tree_none          | 950 ms                                                                | 383 ms: 2.48x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.91 ms: 2.29x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.68 sec: 2.20x faster                                                  |
| go                       | 264 ms                                                                | 128 ms: 2.07x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 654 ms: 1.94x faster                                                    |
| generators               | 68.1 ms                                                               | 35.3 ms: 1.93x faster                                                   |
| raytrace                 | 573 ms                                                                | 323 ms: 1.78x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 531 ms: 1.78x faster                                                    |
| chaos                    | 121 ms                                                                | 69.5 ms: 1.74x faster                                                   |
| scimark_sor              | 246 ms                                                                | 142 ms: 1.74x faster                                                    |
| logging_silent           | 222 ns                                                                | 128 ns: 1.74x faster                                                    |
| richards                 | 91.7 ms                                                               | 53.5 ms: 1.71x faster                                                   |
| richards_super           | 107 ms                                                                | 63.2 ms: 1.70x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 36.7 us: 1.68x faster                                                   |
| comprehensions           | 33.1 us                                                               | 19.9 us: 1.66x faster                                                   |
| scimark_lu               | 227 ms                                                                | 142 ms: 1.60x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 84.1 ms: 1.59x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 80.3 ms: 1.59x faster                                                   |
| float                    | 135 ms                                                                | 84.7 ms: 1.59x faster                                                   |
| spectral_norm            | 186 ms                                                                | 118 ms: 1.58x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 6.92 ms: 1.58x faster                                                   |
| deepcopy                 | 511 us                                                                | 329 us: 1.55x faster                                                    |
| pyflate                  | 795 ms                                                                | 515 ms: 1.54x faster                                                    |
| pylint                   | 485 ms                                                                | 321 ms: 1.51x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.18 sec: 1.50x faster                                                  |
| regex_compile            | 177 ms                                                                | 121 ms: 1.46x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 60.8 ms: 1.42x faster                                                   |
| logging_simple           | 9.78 us                                                               | 6.90 us: 1.42x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.56 us: 1.40x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 261 us: 1.40x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                                  |
| mako                     | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 53.9 ms: 1.36x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.24 sec: 1.36x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 396 us: 1.34x faster                                                    |
| nbody                    | 166 ms                                                                | 124 ms: 1.34x faster                                                    |
| django_template          | 53.3 ms                                                               | 40.2 ms: 1.33x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.1 ms: 1.32x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.50 us: 1.31x faster                                                   |
| sympy_sum                | 184 ms                                                                | 142 ms: 1.30x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.82 sec: 1.29x faster                                                  |
| thrift                   | 1.26 ms                                                               | 980 us: 1.29x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.4 ms: 1.28x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 896 ms: 1.28x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 78.6 ms: 1.27x faster                                                   |
| 2to3                     | 381 ms                                                                | 301 ms: 1.27x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.5 ms: 1.26x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.7 ms: 1.21x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.7 ms: 1.21x faster                                                   |
| docutils                 | 3.53 sec                                                              | 2.94 sec: 1.20x faster                                                  |
| sympy_str                | 329 ms                                                                | 274 ms: 1.20x faster                                                    |
| nqueens                  | 117 ms                                                                | 98.2 ms: 1.20x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 178 ms: 1.19x faster                                                    |
| scimark_fft              | 500 ms                                                                | 422 ms: 1.19x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 27.2 ms: 1.18x faster                                                   |
| fannkuch                 | 546 ms                                                                | 462 ms: 1.18x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.36 ms: 1.17x faster                                                   |
| sympy_expand             | 543 ms                                                                | 463 ms: 1.17x faster                                                    |
| regex_dna                | 257 ms                                                                | 222 ms: 1.16x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 60.7 ms: 1.15x faster                                                   |
| meteor_contest           | 126 ms                                                                | 111 ms: 1.14x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 110 ms: 1.12x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.11x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 3.86 ms: 1.10x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.75 us: 1.10x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.05 ms: 1.08x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.47 us: 1.08x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 673 ms: 1.03x slower                                                    |
| unpickle                 | 17.5 us                                                               | 18.5 us: 1.06x slower                                                   |
| pickle_list              | 5.24 us                                                               | 5.59 us: 1.07x slower                                                   |
| json_loads               | 30.9 us                                                               | 33.1 us: 1.07x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 38.1 us: 1.09x slower                                                   |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.58 ms: 1.25x slower                                                   |
| pickle                   | 12.5 us                                                               | 15.7 us: 1.26x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.1 ms: 1.35x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.74 ms: 1.65x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.88 ms: 1.65x slower                                                   |
| telco                    | 8.49 ms                                                               | 164 ms: 19.35x slower                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 2.99 sec: 205.84x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                            |

Benchmark hidden because not significant (3): json, async_generators, pidigits
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.311x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.39x