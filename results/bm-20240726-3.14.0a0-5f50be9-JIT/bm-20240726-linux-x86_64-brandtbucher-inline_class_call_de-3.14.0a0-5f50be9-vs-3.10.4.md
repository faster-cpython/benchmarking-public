# Results vs. 3.10.4

- fork: brandtbucher
- ref: inline_class_call_de
- machine: linux-x86_64
- commit hash: 5f50be9
- commit date: 2024-07-26
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 272 ms: 1.28x faster                                                        |
| docutils       | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                      |
| html5lib       | 88.9 ms                                                | 64.4 ms: 1.38x faster                                                       |
| tornado_http   | 136 ms                                                 | 92.9 ms: 1.47x faster                                                       |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.23x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 420 ms: 2.07x faster                                                        |
| async_tree_io           | 1.77 sec                                               | 902 ms: 1.96x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 567 ms: 1.79x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 78.9 ms: 1.94x faster                                                       |
| float          | 117 ms                                                 | 71.2 ms: 1.64x faster                                                       |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.49x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.40x faster                                                        |
| regex_v8       | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                       |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.74 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 293 us: 1.65x faster                                                        |
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 56.3 ms: 1.41x faster                                                       |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 79.9 ms: 1.24x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 144 ms: 1.17x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 99.2 ms: 1.16x faster                                                       |
| json_loads           | 31.2 us                                                | 28.0 us: 1.12x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.20 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.81 ms: 1.66x faster                                                       |
| django_template | 48.2 ms                                                | 35.0 ms: 1.37x faster                                                       |
| genshi_text     | 31.8 ms                                                | 25.4 ms: 1.25x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 58.8 ms: 1.12x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.37x faster                                                        |
| generators               | 80.1 ms                                                | 28.7 ms: 2.79x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.50 ms: 2.26x faster                                                       |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.23x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 420 ms: 2.07x faster                                                        |
| richards_super           | 94.7 ms                                                | 46.6 ms: 2.03x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 28.8 us: 2.03x faster                                                       |
| chaos                    | 115 ms                                                 | 57.7 ms: 2.00x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 60.2 ms: 1.96x faster                                                       |
| richards                 | 79.3 ms                                                | 40.4 ms: 1.96x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 902 ms: 1.96x faster                                                        |
| nbody                    | 154 ms                                                 | 78.9 ms: 1.94x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 67.2 ms: 1.90x faster                                                       |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 497 ms: 1.86x faster                                                        |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 567 ms: 1.79x faster                                                        |
| deepcopy                 | 479 us                                                 | 269 us: 1.78x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                       |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                                        |
| go                       | 240 ms                                                 | 144 ms: 1.67x faster                                                        |
| mako                     | 16.3 ms                                                | 9.81 ms: 1.66x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 293 us: 1.65x faster                                                        |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                        |
| float                    | 117 ms                                                 | 71.2 ms: 1.64x faster                                                       |
| pyflate                  | 716 ms                                                 | 438 ms: 1.64x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                       |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.52 ms: 1.59x faster                                                       |
| pylint                   | 551 ms                                                 | 350 ms: 1.58x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                        |
| scimark_fft              | 466 ms                                                 | 307 ms: 1.52x faster                                                        |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.55 us: 1.50x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.81 us: 1.49x faster                                                       |
| logging_format           | 9.09 us                                                | 6.15 us: 1.48x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.40 ms: 1.47x faster                                                       |
| tornado_http             | 136 ms                                                 | 92.9 ms: 1.47x faster                                                       |
| fannkuch                 | 532 ms                                                 | 368 ms: 1.44x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 706 ms: 1.44x faster                                                        |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 56.3 ms: 1.41x faster                                                       |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.41x faster                                                        |
| regex_compile            | 188 ms                                                 | 135 ms: 1.40x faster                                                        |
| html5lib                 | 88.9 ms                                                | 64.4 ms: 1.38x faster                                                       |
| django_template          | 48.2 ms                                                | 35.0 ms: 1.37x faster                                                       |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.37x faster                                                       |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                      |
| thrift                   | 1.07 ms                                                | 798 us: 1.34x faster                                                        |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                       |
| 2to3                     | 348 ms                                                 | 272 ms: 1.28x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                                        |
| genshi_text              | 31.8 ms                                                | 25.4 ms: 1.25x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 79.9 ms: 1.24x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 55.9 ms: 1.24x faster                                                       |
| nqueens                  | 106 ms                                                 | 86.2 ms: 1.23x faster                                                       |
| dask                     | 441 ms                                                 | 365 ms: 1.21x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 827 us: 1.19x faster                                                        |
| sympy_str                | 346 ms                                                 | 295 ms: 1.17x faster                                                        |
| sympy_sum                | 196 ms                                                 | 168 ms: 1.17x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 144 ms: 1.17x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 99.2 ms: 1.16x faster                                                       |
| sympy_integrate          | 25.8 ms                                                | 22.3 ms: 1.16x faster                                                       |
| docutils                 | 3.30 sec                                               | 2.91 sec: 1.13x faster                                                      |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                        |
| sympy_expand             | 566 ms                                                 | 502 ms: 1.13x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 58.8 ms: 1.12x faster                                                       |
| json_loads               | 31.2 us                                                | 28.0 us: 1.12x faster                                                       |
| json                     | 5.69 ms                                                | 5.16 ms: 1.10x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.60 sec: 1.09x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                       |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                        |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.74 ms: 1.03x slower                                                       |
| async_generators         | 444 ms                                                 | 462 ms: 1.04x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 3.87 ms: 1.07x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.77 ms: 1.09x slower                                                       |
| telco                    | 7.27 ms                                                | 7.94 ms: 1.09x slower                                                       |
| coverage                 | 79.4 ms                                                | 92.3 ms: 1.16x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.20 ms: 1.21x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240726-3.14.0a0-5f50be9-JIT/bm-20240726-linux-x86_64-brandtbucher-inline_class_call_de-3.14.0a0-5f50be9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.20x