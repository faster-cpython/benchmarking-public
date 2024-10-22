# Results vs. 3.10.4

- fork: brandtbucher
- ref: binary_op_inplace_ad
- machine: linux-x86_64
- commit hash: 5206d7b
- commit date: 2024-07-17
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 273 ms: 1.28x faster                                                        |
| docutils       | 3.30 sec                                               | 2.86 sec: 1.15x faster                                                      |
| html5lib       | 88.9 ms                                                | 65.0 ms: 1.37x faster                                                       |
| tornado_http   | 136 ms                                                 | 94.2 ms: 1.45x faster                                                       |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 322 ms: 2.26x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 408 ms: 2.13x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 840 ms: 2.10x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 561 ms: 1.81x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.07x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.0 ms: 1.92x faster                                                       |
| float          | 117 ms                                                 | 70.1 ms: 1.67x faster                                                       |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.49x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 136 ms: 1.38x faster                                                        |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                       |
| regex_dna      | 227 ms                                                 | 229 ms: 1.01x slower                                                        |
| regex_effbot   | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 300 us: 1.62x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                        |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 58.2 ms: 1.36x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 81.8 ms: 1.21x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 100 ms: 1.15x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                        |
| json_loads           | 31.2 us                                                | 27.5 us: 1.14x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.81 ms: 1.66x faster                                                       |
| django_template | 48.2 ms                                                | 36.1 ms: 1.33x faster                                                       |
| genshi_text     | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 57.7 ms: 1.14x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 173 us: 3.15x faster                                                        |
| generators               | 80.1 ms                                                | 29.7 ms: 2.70x faster                                                       |
| async_tree_none          | 728 ms                                                 | 322 ms: 2.26x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.66 ms: 2.16x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 408 ms: 2.13x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 840 ms: 2.10x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 28.8 us: 2.03x faster                                                       |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 60.6 ms: 1.95x faster                                                       |
| richards_super           | 94.7 ms                                                | 48.7 ms: 1.95x faster                                                       |
| nbody                    | 154 ms                                                 | 80.0 ms: 1.92x faster                                                       |
| richards                 | 79.3 ms                                                | 42.2 ms: 1.88x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 68.1 ms: 1.88x faster                                                       |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 503 ms: 1.83x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 561 ms: 1.81x faster                                                        |
| logging_silent           | 190 ns                                                 | 106 ns: 1.80x faster                                                        |
| deepcopy                 | 479 us                                                 | 271 us: 1.77x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                       |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                       |
| float                    | 117 ms                                                 | 70.1 ms: 1.67x faster                                                       |
| mako                     | 16.3 ms                                                | 9.81 ms: 1.66x faster                                                       |
| pyflate                  | 716 ms                                                 | 435 ms: 1.65x faster                                                        |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.64x faster                                                        |
| pylint                   | 551 ms                                                 | 338 ms: 1.63x faster                                                        |
| go                       | 240 ms                                                 | 147 ms: 1.63x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.62x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                                       |
| hexiom                   | 10.4 ms                                                | 6.65 ms: 1.56x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                       |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.48 us: 1.52x faster                                                       |
| logging_format           | 9.09 us                                                | 6.04 us: 1.50x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.31 ms: 1.50x faster                                                       |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                                        |
| fannkuch                 | 532 ms                                                 | 360 ms: 1.48x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                      |
| tornado_http             | 136 ms                                                 | 94.2 ms: 1.45x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 710 ms: 1.43x faster                                                        |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                      |
| scimark_lu               | 176 ms                                                 | 123 ms: 1.43x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.39x faster                                                      |
| regex_compile            | 188 ms                                                 | 136 ms: 1.38x faster                                                        |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                       |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                       |
| html5lib                 | 88.9 ms                                                | 65.0 ms: 1.37x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 58.2 ms: 1.36x faster                                                       |
| thrift                   | 1.07 ms                                                | 799 us: 1.34x faster                                                        |
| django_template          | 48.2 ms                                                | 36.1 ms: 1.33x faster                                                       |
| 2to3                     | 348 ms                                                 | 273 ms: 1.28x faster                                                        |
| genshi_text              | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 55.8 ms: 1.24x faster                                                       |
| dulwich_log              | 84.3 ms                                                | 68.1 ms: 1.24x faster                                                       |
| nqueens                  | 106 ms                                                 | 85.9 ms: 1.23x faster                                                       |
| dask                     | 441 ms                                                 | 362 ms: 1.22x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 81.8 ms: 1.21x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 835 us: 1.18x faster                                                        |
| sympy_sum                | 196 ms                                                 | 167 ms: 1.17x faster                                                        |
| sympy_str                | 346 ms                                                 | 295 ms: 1.17x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 22.3 ms: 1.16x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 100 ms: 1.15x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.86 sec: 1.15x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 57.7 ms: 1.14x faster                                                       |
| sympy_expand             | 566 ms                                                 | 498 ms: 1.14x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                       |
| json_loads               | 31.2 us                                                | 27.5 us: 1.14x faster                                                       |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                                      |
| json                     | 5.69 ms                                                | 5.14 ms: 1.11x faster                                                       |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                        |
| regex_dna                | 227 ms                                                 | 229 ms: 1.01x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 3.67 ms: 1.01x slower                                                       |
| async_generators         | 444 ms                                                 | 456 ms: 1.03x slower                                                        |
| regex_effbot             | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                                       |
| telco                    | 7.27 ms                                                | 8.06 ms: 1.11x slower                                                       |
| coverage                 | 79.4 ms                                                | 93.4 ms: 1.18x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240717-3.14.0a0-5206d7b-JIT/bm-20240717-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-5206d7b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.19x