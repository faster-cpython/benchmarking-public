# Results vs. 3.10.4

- fork: brandtbucher
- ref: chain_depth_5
- machine: linux-x86_64
- commit hash: dc27e14
- commit date: 2024-12-12
- overall geometric mean: 1.425x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                  |
| docutils       | 3.30 sec                                               | 2.71 sec: 1.22x faster                                                |
| html5lib       | 88.9 ms                                                | 65.2 ms: 1.36x faster                                                 |
| Geometric mean | (ref)                                                  | 1.31x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 617 ms: 2.87x faster                                                  |
| async_tree_none         | 728 ms                                                 | 271 ms: 2.68x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 340 ms: 2.56x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 496 ms: 2.05x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.52x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.5 ms: 1.91x faster                                                 |
| float          | 117 ms                                                 | 76.0 ms: 1.54x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.44x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.9 ms: 1.11x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.39 ms: 1.07x faster                                                 |
| regex_dna      | 227 ms                                                 | 215 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 195 us: 1.70x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                |
| pickle_pure_python   | 484 us                                                 | 315 us: 1.54x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 55.4 ms: 1.43x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 78.0 ms: 1.27x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.22x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 95.2 ms: 1.21x faster                                                 |
| json_loads           | 31.2 us                                                | 26.1 us: 1.20x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.37x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.14x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.03 ms: 1.18x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.3 ms: 1.58x faster                                                 |
| django_template | 48.2 ms                                                | 33.9 ms: 1.42x faster                                                 |
| genshi_text     | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 57.7 ms: 1.14x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 617 ms: 2.87x faster                                                  |
| async_tree_none          | 728 ms                                                 | 271 ms: 2.68x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 340 ms: 2.56x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                                 |
| generators               | 80.1 ms                                                | 36.3 ms: 2.21x faster                                                 |
| richards_super           | 94.7 ms                                                | 43.1 ms: 2.20x faster                                                 |
| richards                 | 79.3 ms                                                | 37.6 ms: 2.11x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 496 ms: 2.05x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.1 us: 2.01x faster                                                 |
| chaos                    | 115 ms                                                 | 60.2 ms: 1.92x faster                                                 |
| nbody                    | 154 ms                                                 | 80.5 ms: 1.91x faster                                                 |
| pylint                   | 551 ms                                                 | 290 ms: 1.90x faster                                                  |
| logging_silent           | 190 ns                                                 | 101 ns: 1.87x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 68.5 ms: 1.87x faster                                                 |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 64.3 ms: 1.84x faster                                                 |
| go                       | 240 ms                                                 | 133 ms: 1.80x faster                                                  |
| raytrace                 | 507 ms                                                 | 284 ms: 1.78x faster                                                  |
| deepcopy                 | 479 us                                                 | 272 us: 1.76x faster                                                  |
| djangocms                | 38.4 us                                                | 22.3 us: 1.73x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 195 us: 1.70x faster                                                  |
| comprehensions           | 28.8 us                                                | 17.4 us: 1.65x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                |
| mako                     | 16.3 ms                                                | 10.3 ms: 1.58x faster                                                 |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.58x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                                 |
| pyflate                  | 716 ms                                                 | 460 ms: 1.56x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.54x faster                                                 |
| float                    | 117 ms                                                 | 76.0 ms: 1.54x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 315 us: 1.54x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                                 |
| spectral_norm            | 170 ms                                                 | 112 ms: 1.51x faster                                                  |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                  |
| hexiom                   | 10.4 ms                                                | 7.10 ms: 1.46x faster                                                 |
| logging_format           | 9.09 us                                                | 6.24 us: 1.46x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.74 us: 1.45x faster                                                 |
| scimark_fft              | 466 ms                                                 | 325 ms: 1.43x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 55.4 ms: 1.43x faster                                                 |
| django_template          | 48.2 ms                                                | 33.9 ms: 1.42x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 725 ms: 1.40x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                 |
| fannkuch                 | 532 ms                                                 | 388 ms: 1.37x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                |
| thrift                   | 1.07 ms                                                | 783 us: 1.37x faster                                                  |
| html5lib                 | 88.9 ms                                                | 65.2 ms: 1.36x faster                                                 |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.85 ms: 1.33x faster                                                 |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                                  |
| genshi_text              | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.29x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 78.0 ms: 1.27x faster                                                 |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                 |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.26x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 55.5 ms: 1.25x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 67.7 ms: 1.25x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 20.8 ms: 1.24x faster                                                 |
| sympy_str                | 346 ms                                                 | 283 ms: 1.22x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.22x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.71 sec: 1.22x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 95.2 ms: 1.21x faster                                                 |
| json_loads               | 31.2 us                                                | 26.1 us: 1.20x faster                                                 |
| json                     | 5.69 ms                                                | 4.80 ms: 1.19x faster                                                 |
| sympy_expand             | 566 ms                                                 | 478 ms: 1.18x faster                                                  |
| nqueens                  | 106 ms                                                 | 90.3 ms: 1.17x faster                                                 |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.14x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 57.7 ms: 1.14x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 878 us: 1.12x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.9 ms: 1.11x faster                                                 |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.39 ms: 1.07x faster                                                 |
| regex_dna                | 227 ms                                                 | 215 ms: 1.05x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.76 sec: 1.03x faster                                                |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| async_generators         | 444 ms                                                 | 455 ms: 1.03x slower                                                  |
| telco                    | 7.27 ms                                                | 7.64 ms: 1.05x slower                                                 |
| mypy2                    | 894 ms                                                 | 960 ms: 1.07x slower                                                  |
| coverage                 | 79.4 ms                                                | 86.5 ms: 1.09x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.03 ms: 1.18x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.80 ms: 1.32x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                 |
| bench_mp_pool            | 24.0 ms                                                | 80.8 ms: 3.36x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                          |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241212-3.14.0a2+-dc27e14-JIT/bm-20241212-linux-x86_64-brandtbucher-chain_depth_5-3.14.0a2+-dc27e14.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.425x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.29x