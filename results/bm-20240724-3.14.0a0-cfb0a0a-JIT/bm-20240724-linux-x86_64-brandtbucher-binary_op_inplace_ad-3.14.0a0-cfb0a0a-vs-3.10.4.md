# Results vs. 3.10.4

- fork: brandtbucher
- ref: binary_op_inplace_ad
- machine: linux-x86_64
- commit hash: cfb0a0a
- commit date: 2024-07-24
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 273 ms: 1.28x faster                                                        |
| docutils       | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                      |
| html5lib       | 88.9 ms                                                | 64.6 ms: 1.38x faster                                                       |
| tornado_http   | 136 ms                                                 | 95.4 ms: 1.43x faster                                                       |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.24x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 418 ms: 2.08x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 901 ms: 1.96x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 565 ms: 1.80x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.8 ms: 1.92x faster                                                       |
| float          | 117 ms                                                 | 70.1 ms: 1.67x faster                                                       |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.49x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.41x faster                                                        |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                       |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 299 us: 1.62x faster                                                        |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 56.7 ms: 1.40x faster                                                       |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 81.0 ms: 1.23x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 98.9 ms: 1.17x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.15x faster                                                        |
| json_loads           | 31.2 us                                                | 28.1 us: 1.11x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.21 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.80 ms: 1.67x faster                                                       |
| django_template | 48.2 ms                                                | 35.8 ms: 1.35x faster                                                       |
| genshi_text     | 31.8 ms                                                | 24.6 ms: 1.29x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 58.0 ms: 1.14x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.21x faster                                                        |
| generators               | 80.1 ms                                                | 28.9 ms: 2.77x faster                                                       |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.24x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.60 ms: 2.20x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 418 ms: 2.08x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 28.4 us: 2.06x faster                                                       |
| richards_super           | 94.7 ms                                                | 46.7 ms: 2.03x faster                                                       |
| chaos                    | 115 ms                                                 | 58.2 ms: 1.98x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 60.1 ms: 1.97x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 901 ms: 1.96x faster                                                        |
| richards                 | 79.3 ms                                                | 40.8 ms: 1.94x faster                                                       |
| nbody                    | 154 ms                                                 | 79.8 ms: 1.92x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 67.4 ms: 1.90x faster                                                       |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 504 ms: 1.83x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 565 ms: 1.80x faster                                                        |
| logging_silent           | 190 ns                                                 | 107 ns: 1.78x faster                                                        |
| deepcopy                 | 479 us                                                 | 271 us: 1.77x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.76x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.69x faster                                                       |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                        |
| float                    | 117 ms                                                 | 70.1 ms: 1.67x faster                                                       |
| scimark_sor              | 220 ms                                                 | 132 ms: 1.67x faster                                                        |
| mako                     | 16.3 ms                                                | 9.80 ms: 1.67x faster                                                       |
| pyflate                  | 716 ms                                                 | 432 ms: 1.66x faster                                                        |
| go                       | 240 ms                                                 | 147 ms: 1.64x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.63x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 299 us: 1.62x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                                       |
| hexiom                   | 10.4 ms                                                | 6.55 ms: 1.59x faster                                                       |
| pylint                   | 551 ms                                                 | 353 ms: 1.56x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.22 ms: 1.53x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                                       |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                       |
| scimark_fft              | 466 ms                                                 | 309 ms: 1.51x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                                       |
| logging_format           | 9.09 us                                                | 6.24 us: 1.46x faster                                                       |
| fannkuch                 | 532 ms                                                 | 365 ms: 1.46x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 712 ms: 1.43x faster                                                        |
| tornado_http             | 136 ms                                                 | 95.4 ms: 1.43x faster                                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                      |
| regex_compile            | 188 ms                                                 | 134 ms: 1.41x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 56.7 ms: 1.40x faster                                                       |
| scimark_lu               | 176 ms                                                 | 128 ms: 1.38x faster                                                        |
| html5lib                 | 88.9 ms                                                | 64.6 ms: 1.38x faster                                                       |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                       |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                      |
| django_template          | 48.2 ms                                                | 35.8 ms: 1.35x faster                                                       |
| thrift                   | 1.07 ms                                                | 800 us: 1.34x faster                                                        |
| genshi_text              | 31.8 ms                                                | 24.6 ms: 1.29x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.28x faster                                                        |
| 2to3                     | 348 ms                                                 | 273 ms: 1.28x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 56.0 ms: 1.24x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 81.0 ms: 1.23x faster                                                       |
| nqueens                  | 106 ms                                                 | 87.1 ms: 1.22x faster                                                       |
| dask                     | 441 ms                                                 | 365 ms: 1.21x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 831 us: 1.19x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 71.2 ms: 1.18x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 98.9 ms: 1.17x faster                                                       |
| sympy_integrate          | 25.8 ms                                                | 22.3 ms: 1.16x faster                                                       |
| sympy_str                | 346 ms                                                 | 299 ms: 1.16x faster                                                        |
| meteor_contest           | 120 ms                                                 | 104 ms: 1.15x faster                                                        |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.15x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 58.0 ms: 1.14x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                      |
| sympy_expand             | 566 ms                                                 | 506 ms: 1.12x faster                                                        |
| json_loads               | 31.2 us                                                | 28.1 us: 1.11x faster                                                       |
| json                     | 5.69 ms                                                | 5.15 ms: 1.11x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                       |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                        |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                                        |
| gc_traversal             | 3.62 ms                                                | 3.68 ms: 1.02x slower                                                       |
| async_generators         | 444 ms                                                 | 453 ms: 1.02x slower                                                        |
| regex_effbot             | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                       |
| telco                    | 7.27 ms                                                | 7.87 ms: 1.08x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.08x slower                                                       |
| coverage                 | 79.4 ms                                                | 92.1 ms: 1.16x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.21 ms: 1.21x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240724-3.14.0a0-cfb0a0a-JIT/bm-20240724-linux-x86_64-brandtbucher-binary_op_inplace_ad-3.14.0a0-cfb0a0a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.20x