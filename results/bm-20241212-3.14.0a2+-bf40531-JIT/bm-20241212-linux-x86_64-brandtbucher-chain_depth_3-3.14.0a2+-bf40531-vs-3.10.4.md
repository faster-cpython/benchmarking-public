# Results vs. 3.10.4

- fork: brandtbucher
- ref: chain_depth_3
- machine: linux-x86_64
- commit hash: bf40531
- commit date: 2024-12-12
- overall geometric mean: 1.435x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.36x faster                                                  |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                |
| html5lib       | 88.9 ms                                                | 64.5 ms: 1.38x faster                                                 |
| Geometric mean | (ref)                                                  | 1.32x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 621 ms: 2.85x faster                                                  |
| async_tree_none         | 728 ms                                                 | 271 ms: 2.69x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 339 ms: 2.56x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 505 ms: 2.01x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.51x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.0 ms: 1.89x faster                                                 |
| float          | 117 ms                                                 | 75.6 ms: 1.55x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.44x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.48x faster                                                  |
| regex_v8       | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.47 ms: 1.04x faster                                                 |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 194 us: 1.70x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                |
| pickle_pure_python   | 484 us                                                 | 317 us: 1.53x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 54.5 ms: 1.45x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 77.3 ms: 1.29x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 137 ms: 1.22x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 95.0 ms: 1.22x faster                                                 |
| json_loads           | 31.2 us                                                | 26.2 us: 1.19x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.38x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.99 ms: 1.63x faster                                                 |
| django_template | 48.2 ms                                                | 33.8 ms: 1.42x faster                                                 |
| genshi_text     | 31.8 ms                                                | 24.4 ms: 1.31x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 58.9 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 621 ms: 2.85x faster                                                  |
| async_tree_none          | 728 ms                                                 | 271 ms: 2.69x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 339 ms: 2.56x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.17 ms: 2.50x faster                                                 |
| richards_super           | 94.7 ms                                                | 42.6 ms: 2.22x faster                                                 |
| generators               | 80.1 ms                                                | 36.1 ms: 2.22x faster                                                 |
| richards                 | 79.3 ms                                                | 36.7 ms: 2.16x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 505 ms: 2.01x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 2.00x faster                                                 |
| chaos                    | 115 ms                                                 | 58.8 ms: 1.96x faster                                                 |
| pylint                   | 551 ms                                                 | 288 ms: 1.91x faster                                                  |
| nbody                    | 154 ms                                                 | 81.0 ms: 1.89x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 68.1 ms: 1.88x faster                                                 |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.87x faster                                                  |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 64.1 ms: 1.84x faster                                                 |
| go                       | 240 ms                                                 | 131 ms: 1.83x faster                                                  |
| raytrace                 | 507 ms                                                 | 283 ms: 1.79x faster                                                  |
| deepcopy                 | 479 us                                                 | 271 us: 1.77x faster                                                  |
| djangocms                | 38.4 us                                                | 22.1 us: 1.74x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 194 us: 1.70x faster                                                  |
| comprehensions           | 28.8 us                                                | 17.2 us: 1.67x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.66x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                |
| mako                     | 16.3 ms                                                | 9.99 ms: 1.63x faster                                                 |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.61x faster                                                  |
| pyflate                  | 716 ms                                                 | 448 ms: 1.60x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                 |
| float                    | 117 ms                                                 | 75.6 ms: 1.55x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 317 us: 1.53x faster                                                  |
| spectral_norm            | 170 ms                                                 | 111 ms: 1.53x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.99 ms: 1.49x faster                                                 |
| regex_compile            | 188 ms                                                 | 128 ms: 1.48x faster                                                  |
| scimark_fft              | 466 ms                                                 | 318 ms: 1.46x faster                                                  |
| logging_format           | 9.09 us                                                | 6.25 us: 1.46x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.72 us: 1.45x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 54.5 ms: 1.45x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                |
| django_template          | 48.2 ms                                                | 33.8 ms: 1.42x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 715 ms: 1.42x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.57 ms: 1.41x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.6 ms: 1.40x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                                |
| fannkuch                 | 532 ms                                                 | 385 ms: 1.38x faster                                                  |
| html5lib                 | 88.9 ms                                                | 64.5 ms: 1.38x faster                                                 |
| thrift                   | 1.07 ms                                                | 778 us: 1.38x faster                                                  |
| 2to3                     | 348 ms                                                 | 257 ms: 1.36x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.33x faster                                                  |
| genshi_text              | 31.8 ms                                                | 24.4 ms: 1.31x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 77.3 ms: 1.29x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                 |
| sympy_sum                | 196 ms                                                 | 156 ms: 1.26x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 20.6 ms: 1.25x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 67.4 ms: 1.25x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 55.4 ms: 1.25x faster                                                 |
| sympy_str                | 346 ms                                                 | 280 ms: 1.23x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 137 ms: 1.22x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 95.0 ms: 1.22x faster                                                 |
| json_loads               | 31.2 us                                                | 26.2 us: 1.19x faster                                                 |
| sympy_expand             | 566 ms                                                 | 477 ms: 1.19x faster                                                  |
| nqueens                  | 106 ms                                                 | 89.5 ms: 1.18x faster                                                 |
| json                     | 5.69 ms                                                | 4.92 ms: 1.16x faster                                                 |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 875 us: 1.13x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 58.9 ms: 1.12x faster                                                 |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.47 ms: 1.04x faster                                                 |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                                  |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                  |
| async_generators         | 444 ms                                                 | 448 ms: 1.01x slower                                                  |
| telco                    | 7.27 ms                                                | 7.53 ms: 1.04x slower                                                 |
| coverage                 | 79.4 ms                                                | 83.3 ms: 1.05x slower                                                 |
| mypy2                    | 894 ms                                                 | 953 ms: 1.07x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.78 ms: 1.32x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                 |
| bench_mp_pool            | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                          |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241212-3.14.0a2+-bf40531-JIT/bm-20241212-linux-x86_64-brandtbucher-chain_depth_3-3.14.0a2+-bf40531.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.435x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.29x