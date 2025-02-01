# Results vs. 3.10.4

- fork: eendebakpt
- ref: binaryops_shift
- machine: linux-x86_64
- commit hash: 1895d69
- commit date: 2025-01-31
- overall geometric mean: 1.453x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 253 ms: 1.38x faster                                                  |
| docutils       | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                |
| html5lib       | 88.9 ms                                                | 60.2 ms: 1.48x faster                                                 |
| Geometric mean | (ref)                                                  | 1.37x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 619 ms: 2.86x faster                                                  |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.77x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 323 ms: 2.69x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 495 ms: 2.05x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.57x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 71.1 ms: 1.65x faster                                                 |
| nbody          | 154 ms                                                 | 94.4 ms: 1.63x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.40x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                                  |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.10x faster                                                 |
| regex_effbot   | 3.63 ms                                                | 3.34 ms: 1.09x faster                                                 |
| regex_dna      | 227 ms                                                 | 209 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.59x faster                                                |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 58.4 ms: 1.35x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                  |
| json_dumps           | 14.2 ms                                                | 12.0 ms: 1.19x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 97.4 ms: 1.18x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 83.9 ms: 1.18x faster                                                 |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.7 ms: 1.52x faster                                                 |
| genshi_text     | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                 |
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 48.0 ms: 1.37x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 157 us: 3.46x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 619 ms: 2.86x faster                                                  |
| generators               | 80.1 ms                                                | 28.2 ms: 2.84x faster                                                 |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.77x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 323 ms: 2.69x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 495 ms: 2.05x faster                                                  |
| go                       | 240 ms                                                 | 118 ms: 2.03x faster                                                  |
| pylint                   | 551 ms                                                 | 272 ms: 2.02x faster                                                  |
| chaos                    | 115 ms                                                 | 58.5 ms: 1.97x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 30.4 us: 1.92x faster                                                 |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                  |
| richards_super           | 94.7 ms                                                | 51.2 ms: 1.85x faster                                                 |
| deepcopy                 | 479 us                                                 | 260 us: 1.85x faster                                                  |
| spectral_norm            | 170 ms                                                 | 94.0 ms: 1.81x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 70.7 ms: 1.81x faster                                                 |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                                  |
| richards                 | 79.3 ms                                                | 44.4 ms: 1.79x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 67.4 ms: 1.75x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                                 |
| logging_silent           | 190 ns                                                 | 110 ns: 1.73x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.26 ms: 1.72x faster                                                 |
| pyflate                  | 716 ms                                                 | 424 ms: 1.69x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.26 ms: 1.66x faster                                                 |
| float                    | 117 ms                                                 | 71.1 ms: 1.65x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                                 |
| nbody                    | 154 ms                                                 | 94.4 ms: 1.63x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.59x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                                 |
| django_template          | 48.2 ms                                                | 31.7 ms: 1.52x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.48 us: 1.52x faster                                                 |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                  |
| logging_format           | 9.09 us                                                | 6.03 us: 1.51x faster                                                 |
| genshi_text              | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                 |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                                  |
| html5lib                 | 88.9 ms                                                | 60.2 ms: 1.48x faster                                                 |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.5 ms: 1.42x faster                                                 |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                 |
| thrift                   | 1.07 ms                                                | 759 us: 1.41x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.61 ms: 1.40x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 734 ms: 1.39x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 104 ms: 1.38x faster                                                  |
| 2to3                     | 348 ms                                                 | 253 ms: 1.38x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 48.0 ms: 1.37x faster                                                 |
| scimark_fft              | 466 ms                                                 | 339 ms: 1.37x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 58.4 ms: 1.35x faster                                                 |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.35x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.34x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 51.8 ms: 1.33x faster                                                 |
| nqueens                  | 106 ms                                                 | 80.3 ms: 1.32x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 64.1 ms: 1.32x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                                 |
| sympy_str                | 346 ms                                                 | 266 ms: 1.30x faster                                                  |
| pathlib                  | 20.5 ms                                                | 15.7 ms: 1.30x faster                                                 |
| fannkuch                 | 532 ms                                                 | 412 ms: 1.29x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                |
| sympy_expand             | 566 ms                                                 | 450 ms: 1.26x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                  |
| json_dumps               | 14.2 ms                                                | 12.0 ms: 1.19x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 97.4 ms: 1.18x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 83.9 ms: 1.18x faster                                                 |
| async_generators         | 444 ms                                                 | 384 ms: 1.16x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.48 sec: 1.15x faster                                                |
| bench_thread_pool        | 986 us                                                 | 860 us: 1.15x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                 |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.10x faster                                                 |
| json                     | 5.69 ms                                                | 5.23 ms: 1.09x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.34 ms: 1.09x faster                                                 |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                 |
| regex_dna                | 227 ms                                                 | 209 ms: 1.08x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                 |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                  |
| telco                    | 7.27 ms                                                | 7.91 ms: 1.09x slower                                                 |
| coverage                 | 79.4 ms                                                | 89.8 ms: 1.13x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 4.77 ms: 1.32x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                                 |
| bench_mp_pool            | 24.0 ms                                                | 81.3 ms: 3.39x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                          |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250131-3.14.0a4+-1895d69/bm-20250131-linux-x86_64-eendebakpt-binaryops_shift-3.14.0a4+-1895d69.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.453x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.26x