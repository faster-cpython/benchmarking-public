# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_binary_op_swa
- machine: linux-x86_64
- commit hash: 18313ac
- commit date: 2024-12-10
- overall geometric mean: 1.425x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.35x faster                                                         |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                       |
| html5lib       | 88.9 ms                                                | 64.5 ms: 1.38x faster                                                        |
| Geometric mean | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 618 ms: 2.86x faster                                                         |
| async_tree_none         | 728 ms                                                 | 268 ms: 2.71x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 337 ms: 2.58x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 492 ms: 2.07x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.54x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 93.2 ms: 1.65x faster                                                        |
| float          | 117 ms                                                 | 76.7 ms: 1.53x faster                                                        |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.25 ms: 1.12x faster                                                        |
| regex_v8       | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                        |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                  | 1.18x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 194 us: 1.71x faster                                                         |
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.52x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 55.0 ms: 1.44x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 81.1 ms: 1.23x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 95.8 ms: 1.21x faster                                                        |
| json_loads           | 31.2 us                                                | 26.1 us: 1.20x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                        |
| django_template | 48.2 ms                                                | 33.3 ms: 1.45x faster                                                        |
| genshi_text     | 31.8 ms                                                | 24.1 ms: 1.32x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 58.6 ms: 1.13x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.27x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 618 ms: 2.86x faster                                                         |
| async_tree_none          | 728 ms                                                 | 268 ms: 2.71x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 337 ms: 2.58x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.16 ms: 2.51x faster                                                        |
| generators               | 80.1 ms                                                | 36.2 ms: 2.21x faster                                                        |
| richards_super           | 94.7 ms                                                | 43.6 ms: 2.17x faster                                                        |
| richards                 | 79.3 ms                                                | 36.9 ms: 2.15x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 492 ms: 2.07x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                                        |
| logging_silent           | 190 ns                                                 | 99.1 ns: 1.91x faster                                                        |
| pylint                   | 551 ms                                                 | 290 ms: 1.90x faster                                                         |
| chaos                    | 115 ms                                                 | 62.3 ms: 1.85x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 69.3 ms: 1.84x faster                                                        |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.82x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 65.8 ms: 1.80x faster                                                        |
| go                       | 240 ms                                                 | 135 ms: 1.78x faster                                                         |
| deepcopy                 | 479 us                                                 | 270 us: 1.77x faster                                                         |
| djangocms                | 38.4 us                                                | 22.1 us: 1.74x faster                                                        |
| raytrace                 | 507 ms                                                 | 294 ms: 1.72x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 194 us: 1.71x faster                                                         |
| comprehensions           | 28.8 us                                                | 17.3 us: 1.66x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.65x faster                                                        |
| nbody                    | 154 ms                                                 | 93.2 ms: 1.65x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                       |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                        |
| pyflate                  | 716 ms                                                 | 455 ms: 1.57x faster                                                         |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                         |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                        |
| float                    | 117 ms                                                 | 76.7 ms: 1.53x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.52x faster                                                         |
| hexiom                   | 10.4 ms                                                | 7.00 ms: 1.48x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                                        |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                         |
| logging_format           | 9.09 us                                                | 6.21 us: 1.46x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                       |
| django_template          | 48.2 ms                                                | 33.3 ms: 1.45x faster                                                        |
| spectral_norm            | 170 ms                                                 | 118 ms: 1.44x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 55.0 ms: 1.44x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 709 ms: 1.44x faster                                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.6 ms: 1.40x faster                                                        |
| scimark_fft              | 466 ms                                                 | 336 ms: 1.39x faster                                                         |
| thrift                   | 1.07 ms                                                | 775 us: 1.38x faster                                                         |
| html5lib                 | 88.9 ms                                                | 64.5 ms: 1.38x faster                                                        |
| fannkuch                 | 532 ms                                                 | 388 ms: 1.37x faster                                                         |
| 2to3                     | 348 ms                                                 | 257 ms: 1.35x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.33x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.33x faster                                                       |
| genshi_text              | 31.8 ms                                                | 24.1 ms: 1.32x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.29x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.09 ms: 1.27x faster                                                        |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                        |
| sympy_sum                | 196 ms                                                 | 156 ms: 1.26x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 67.1 ms: 1.26x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 55.4 ms: 1.25x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 20.7 ms: 1.25x faster                                                        |
| sympy_str                | 346 ms                                                 | 281 ms: 1.23x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 81.1 ms: 1.23x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 95.8 ms: 1.21x faster                                                        |
| json_loads               | 31.2 us                                                | 26.1 us: 1.20x faster                                                        |
| json                     | 5.69 ms                                                | 4.79 ms: 1.19x faster                                                        |
| sympy_expand             | 566 ms                                                 | 476 ms: 1.19x faster                                                         |
| nqueens                  | 106 ms                                                 | 91.1 ms: 1.16x faster                                                        |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 873 us: 1.13x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 58.6 ms: 1.13x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.25 ms: 1.12x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.10x faster                                                       |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                                        |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                         |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                         |
| async_generators         | 444 ms                                                 | 446 ms: 1.01x slower                                                         |
| telco                    | 7.27 ms                                                | 7.59 ms: 1.05x slower                                                        |
| mypy2                    | 894 ms                                                 | 954 ms: 1.07x slower                                                         |
| coverage                 | 79.4 ms                                                | 85.7 ms: 1.08x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.60 ms: 1.27x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.44 ms: 1.51x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                                 |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241210-3.14.0a2+-18313ac-JIT/bm-20241210-linux-x86_64-brandtbucher-justin_binary_op_swa-3.14.0a2+-18313ac.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.425x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.29x