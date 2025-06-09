# Results vs. 3.10.4

- fork: python
- ref: aac22ea212849f8fffee
- machine: linux-aarch64
- commit hash: aac22ea
- commit date: 2025-06-08
- overall geometric mean: 1.225x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 300 ms: 1.27x faster                                                    |
| docutils       | 3.53 sec                                                              | 2.91 sec: 1.21x faster                                                  |
| html5lib       | 86.5 ms                                                               | 61.1 ms: 1.42x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 870 ms: 2.63x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 468 ms: 2.42x faster                                                    |
| async_tree_none         | 950 ms                                                                | 392 ms: 2.42x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 661 ms: 1.93x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.33x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 86.3 ms: 1.56x faster                                                   |
| nbody          | 166 ms                                                                | 120 ms: 1.38x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 122 ms: 1.45x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 27.6 ms: 1.17x faster                                                   |
| regex_dna      | 257 ms                                                                | 232 ms: 1.11x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 3.84 ms: 1.11x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 264 us: 1.39x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.47 sec: 1.36x faster                                                  |
| pickle_pure_python   | 529 us                                                                | 392 us: 1.35x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 80.0 ms: 1.24x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.8 ms: 1.21x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 180 ms: 1.18x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.3 us: 1.04x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.64 ms: 1.26x slower                                                   |
| python_startup         | 11.2 ms                                                               | 15.3 ms: 1.36x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.31x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.8 ms: 1.38x faster                                                   |
| django_template | 53.3 ms                                                               | 39.7 ms: 1.34x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 28.1 ms: 1.25x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 62.3 ms: 1.12x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 195 us: 3.40x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 870 ms: 2.63x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 468 ms: 2.42x faster                                                    |
| async_tree_none          | 950 ms                                                                | 392 ms: 2.42x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.91 ms: 2.29x faster                                                   |
| mdp                      | 3.70 sec                                                              | 1.67 sec: 2.21x faster                                                  |
| go                       | 264 ms                                                                | 127 ms: 2.08x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 661 ms: 1.93x faster                                                    |
| richards_super           | 107 ms                                                                | 58.2 ms: 1.84x faster                                                   |
| generators               | 68.1 ms                                                               | 37.6 ms: 1.81x faster                                                   |
| chaos                    | 121 ms                                                                | 68.1 ms: 1.78x faster                                                   |
| richards                 | 91.7 ms                                                               | 51.6 ms: 1.78x faster                                                   |
| raytrace                 | 573 ms                                                                | 326 ms: 1.76x faster                                                    |
| scimark_sor              | 246 ms                                                                | 146 ms: 1.68x faster                                                    |
| comprehensions           | 33.1 us                                                               | 20.2 us: 1.64x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 37.6 us: 1.64x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 84.4 ms: 1.59x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 81.2 ms: 1.57x faster                                                   |
| deepcopy                 | 511 us                                                                | 325 us: 1.57x faster                                                    |
| float                    | 135 ms                                                                | 86.3 ms: 1.56x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.01 ms: 1.56x faster                                                   |
| pylint                   | 485 ms                                                                | 315 ms: 1.54x faster                                                    |
| scimark_lu               | 227 ms                                                                | 152 ms: 1.49x faster                                                    |
| pyflate                  | 795 ms                                                                | 545 ms: 1.46x faster                                                    |
| regex_compile            | 177 ms                                                                | 122 ms: 1.45x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 61.1 ms: 1.42x faster                                                   |
| spectral_norm            | 186 ms                                                                | 132 ms: 1.41x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 52.0 ms: 1.41x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 264 us: 1.39x faster                                                    |
| nbody                    | 166 ms                                                                | 120 ms: 1.38x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.8 ms: 1.38x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.47 sec: 1.36x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 392 us: 1.35x faster                                                    |
| django_template          | 53.3 ms                                                               | 39.7 ms: 1.34x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.28 sec: 1.33x faster                                                  |
| sympy_integrate          | 26.5 ms                                                               | 20.2 ms: 1.32x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.58 us: 1.29x faster                                                   |
| 2to3                     | 381 ms                                                                | 300 ms: 1.27x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.5 ms: 1.26x faster                                                   |
| logging_format           | 10.6 us                                                               | 8.46 us: 1.25x faster                                                   |
| sympy_sum                | 184 ms                                                                | 147 ms: 1.25x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 28.1 ms: 1.25x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.84 us: 1.25x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 80.0 ms: 1.24x faster                                                   |
| sympy_str                | 329 ms                                                                | 265 ms: 1.24x faster                                                    |
| docutils                 | 3.53 sec                                                              | 2.91 sec: 1.21x faster                                                  |
| json_dumps               | 16.7 ms                                                               | 13.8 ms: 1.21x faster                                                   |
| nqueens                  | 117 ms                                                                | 99.7 ms: 1.18x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 180 ms: 1.18x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.5 ms: 1.17x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 27.6 ms: 1.17x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.03 sec: 1.16x faster                                                  |
| fannkuch                 | 546 ms                                                                | 471 ms: 1.16x faster                                                    |
| sympy_expand             | 543 ms                                                                | 468 ms: 1.16x faster                                                    |
| scimark_fft              | 500 ms                                                                | 434 ms: 1.15x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 999 ms: 1.15x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 62.3 ms: 1.12x faster                                                   |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.11x faster                                                    |
| regex_dna                | 257 ms                                                                | 232 ms: 1.11x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 3.84 ms: 1.11x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.91 ms: 1.10x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.93 us: 1.05x faster                                                   |
| json                     | 5.88 ms                                                               | 5.71 ms: 1.03x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 669 ms: 1.02x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.3 us: 1.04x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.27 ms: 1.09x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.64 ms: 1.26x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.3 ms: 1.36x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.82 ms: 1.64x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.72 ms: 1.64x slower                                                   |
| logging_silent           | 222 ns                                                                | 618 ns: 2.78x slower                                                    |
| coverage                 | 83.6 ms                                                               | 569 ms: 6.81x slower                                                    |
| thrift                   | 1.26 ms                                                               | 197 ms: 156.06x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                            |

Benchmark hidden because not significant (2): async_generators, pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250608-3.15.0a0-aac22ea/bm-20250608-arminc-aarch64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.225x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.35x