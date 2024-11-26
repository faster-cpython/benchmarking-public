# Results vs. 3.10.4

- fork: faster-cpython
- ref: split_load_const
- machine: linux-x86_64
- commit hash: f934559
- commit date: 2024-10-25
- overall geometric mean: 1.412x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                                         |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                                       |
| html5lib       | 88.9 ms                                                | 63.9 ms: 1.39x faster                                                        |
| tornado_http   | 136 ms                                                 | 91.1 ms: 1.50x faster                                                        |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.23x faster                                                         |
| async_tree_io           | 1.77 sec                                               | 838 ms: 2.11x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 413 ms: 2.11x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 571 ms: 1.78x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 94.4 ms: 1.63x faster                                                        |
| float          | 117 ms                                                 | 79.4 ms: 1.47x faster                                                        |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                         |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.13x faster                                                        |
| regex_dna      | 227 ms                                                 | 217 ms: 1.04x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.69 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 313 us: 1.55x faster                                                         |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                         |
| tomli_loads          | 3.14 sec                                               | 2.13 sec: 1.47x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                        |
| json_loads           | 31.2 us                                                | 26.2 us: 1.19x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 85.4 ms: 1.16x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 157 ms: 1.07x faster                                                         |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.8 ms: 1.24x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                        |
| mako            | 16.3 ms                                                | 11.7 ms: 1.40x faster                                                        |
| django_template | 48.2 ms                                                | 34.6 ms: 1.39x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 50.4 ms: 1.31x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 158 us: 3.45x faster                                                         |
| generators               | 80.1 ms                                                | 28.0 ms: 2.86x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.29 ms: 2.41x faster                                                        |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.23x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 838 ms: 2.11x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 413 ms: 2.11x faster                                                         |
| go                       | 240 ms                                                 | 121 ms: 1.99x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 30.6 us: 1.91x faster                                                        |
| chaos                    | 115 ms                                                 | 60.9 ms: 1.90x faster                                                        |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                         |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                                         |
| richards_super           | 94.7 ms                                                | 52.3 ms: 1.81x faster                                                        |
| logging_silent           | 190 ns                                                 | 107 ns: 1.78x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 571 ms: 1.78x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 72.5 ms: 1.76x faster                                                        |
| pylint                   | 551 ms                                                 | 317 ms: 1.74x faster                                                         |
| richards                 | 79.3 ms                                                | 45.8 ms: 1.73x faster                                                        |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.73x faster                                                         |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 70.3 ms: 1.68x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                        |
| hexiom                   | 10.4 ms                                                | 6.29 ms: 1.65x faster                                                        |
| nbody                    | 154 ms                                                 | 94.4 ms: 1.63x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 313 us: 1.55x faster                                                         |
| pyflate                  | 716 ms                                                 | 465 ms: 1.54x faster                                                         |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                         |
| tornado_http             | 136 ms                                                 | 91.1 ms: 1.50x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.58 us: 1.49x faster                                                        |
| float                    | 117 ms                                                 | 79.4 ms: 1.47x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 2.13 sec: 1.47x faster                                                       |
| coroutines               | 35.1 ms                                                | 23.9 ms: 1.47x faster                                                        |
| logging_format           | 9.09 us                                                | 6.23 us: 1.46x faster                                                        |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                         |
| spectral_norm            | 170 ms                                                 | 118 ms: 1.44x faster                                                         |
| genshi_text              | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.41x faster                                                       |
| mako                     | 16.3 ms                                                | 11.7 ms: 1.40x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 730 ms: 1.39x faster                                                         |
| django_template          | 48.2 ms                                                | 34.6 ms: 1.39x faster                                                        |
| html5lib                 | 88.9 ms                                                | 63.9 ms: 1.39x faster                                                        |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.37x faster                                                        |
| thrift                   | 1.07 ms                                                | 782 us: 1.37x faster                                                         |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 127 ms: 1.35x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.35x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.85 ms: 1.33x faster                                                        |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 63.6 ms: 1.33x faster                                                        |
| nqueens                  | 106 ms                                                 | 80.5 ms: 1.32x faster                                                        |
| fannkuch                 | 532 ms                                                 | 405 ms: 1.31x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 50.4 ms: 1.31x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 53.2 ms: 1.30x faster                                                        |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                         |
| scimark_fft              | 466 ms                                                 | 365 ms: 1.28x faster                                                         |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                        |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                                       |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                                         |
| python_startup           | 14.6 ms                                                | 11.8 ms: 1.24x faster                                                        |
| json_loads               | 31.2 us                                                | 26.2 us: 1.19x faster                                                        |
| json                     | 5.69 ms                                                | 4.84 ms: 1.18x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 841 us: 1.17x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 85.4 ms: 1.16x faster                                                        |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.13x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.11x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 157 ms: 1.07x faster                                                         |
| regex_dna                | 227 ms                                                 | 217 ms: 1.04x faster                                                         |
| async_generators         | 444 ms                                                 | 428 ms: 1.04x faster                                                         |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                         |
| regex_effbot             | 3.63 ms                                                | 3.69 ms: 1.02x slower                                                        |
| coverage                 | 79.4 ms                                                | 84.7 ms: 1.07x slower                                                        |
| telco                    | 7.27 ms                                                | 7.94 ms: 1.09x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.71 ms: 1.30x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.68 ms: 1.65x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 78.1 ms: 3.25x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                                 |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241025-3.14.0a1+-f934559/bm-20241025-linux-x86_64-faster%2dcpython-split_load_const-3.14.0a1+-f934559.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.412x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.25x