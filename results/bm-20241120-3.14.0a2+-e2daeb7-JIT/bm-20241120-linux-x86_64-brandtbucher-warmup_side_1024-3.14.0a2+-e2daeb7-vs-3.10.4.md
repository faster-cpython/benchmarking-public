# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmup_side_1024
- machine: linux-x86_64
- commit hash: e2daeb7
- commit date: 2024-11-20
- overall geometric mean: 1.414x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.34x faster                                                     |
| docutils       | 3.30 sec                                               | 2.81 sec: 1.17x faster                                                   |
| html5lib       | 88.9 ms                                                | 67.2 ms: 1.32x faster                                                    |
| Geometric mean | (ref)                                                  | 1.27x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 328 ms: 2.22x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 410 ms: 2.12x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 914 ms: 1.93x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 561 ms: 1.81x faster                                                     |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 84.8 ms: 1.81x faster                                                    |
| float          | 117 ms                                                 | 78.2 ms: 1.50x faster                                                    |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.41x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                     |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.38 ms: 1.07x faster                                                    |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.15x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 191 us: 1.73x faster                                                     |
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 323 us: 1.50x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                    |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.28x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 79.5 ms: 1.25x faster                                                    |
| json_loads           | 31.2 us                                                | 26.4 us: 1.18x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                    |
| django_template | 48.2 ms                                                | 33.0 ms: 1.46x faster                                                    |
| genshi_text     | 31.8 ms                                                | 24.2 ms: 1.31x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 55.5 ms: 1.19x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.27x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.20 ms: 2.47x faster                                                    |
| generators               | 80.1 ms                                                | 35.6 ms: 2.25x faster                                                    |
| async_tree_none          | 728 ms                                                 | 328 ms: 2.22x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 410 ms: 2.12x faster                                                     |
| richards_super           | 94.7 ms                                                | 46.4 ms: 2.04x faster                                                    |
| pylint                   | 551 ms                                                 | 274 ms: 2.01x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 2.00x faster                                                    |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                                    |
| richards                 | 79.3 ms                                                | 40.6 ms: 1.95x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 914 ms: 1.93x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 67.7 ms: 1.89x faster                                                    |
| go                       | 240 ms                                                 | 129 ms: 1.86x faster                                                     |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                     |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 65.3 ms: 1.81x faster                                                    |
| nbody                    | 154 ms                                                 | 84.8 ms: 1.81x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 561 ms: 1.81x faster                                                     |
| deepcopy                 | 479 us                                                 | 268 us: 1.79x faster                                                     |
| raytrace                 | 507 ms                                                 | 287 ms: 1.76x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 191 us: 1.73x faster                                                     |
| djangocms                | 38.4 us                                                | 22.6 us: 1.70x faster                                                    |
| comprehensions           | 28.8 us                                                | 17.3 us: 1.66x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                   |
| mako                     | 16.3 ms                                                | 10.2 ms: 1.60x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                    |
| pyflate                  | 716 ms                                                 | 455 ms: 1.57x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.55x faster                                                    |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                    |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.49 us: 1.51x faster                                                    |
| spectral_norm            | 170 ms                                                 | 112 ms: 1.51x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 323 us: 1.50x faster                                                     |
| float                    | 117 ms                                                 | 78.2 ms: 1.50x faster                                                    |
| logging_format           | 9.09 us                                                | 6.10 us: 1.49x faster                                                    |
| scimark_fft              | 466 ms                                                 | 315 ms: 1.48x faster                                                     |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                     |
| django_template          | 48.2 ms                                                | 33.0 ms: 1.46x faster                                                    |
| hexiom                   | 10.4 ms                                                | 7.13 ms: 1.46x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 724 ms: 1.41x faster                                                     |
| fannkuch                 | 532 ms                                                 | 384 ms: 1.39x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                   |
| thrift                   | 1.07 ms                                                | 779 us: 1.38x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.74 ms: 1.36x faster                                                    |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.4 ms: 1.34x faster                                                    |
| 2to3                     | 348 ms                                                 | 261 ms: 1.34x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.33x faster                                                     |
| html5lib                 | 88.9 ms                                                | 67.2 ms: 1.32x faster                                                    |
| genshi_text              | 31.8 ms                                                | 24.2 ms: 1.31x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.28x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 67.2 ms: 1.25x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 79.5 ms: 1.25x faster                                                    |
| sympy_sum                | 196 ms                                                 | 158 ms: 1.25x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 55.5 ms: 1.25x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 20.8 ms: 1.24x faster                                                    |
| sympy_str                | 346 ms                                                 | 284 ms: 1.22x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 55.5 ms: 1.19x faster                                                    |
| json_loads               | 31.2 us                                                | 26.4 us: 1.18x faster                                                    |
| nqueens                  | 106 ms                                                 | 89.5 ms: 1.18x faster                                                    |
| sympy_expand             | 566 ms                                                 | 479 ms: 1.18x faster                                                     |
| json                     | 5.69 ms                                                | 4.82 ms: 1.18x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.81 sec: 1.17x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                     |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 872 us: 1.13x faster                                                     |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.09x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                    |
| regex_effbot             | 3.63 ms                                                | 3.38 ms: 1.07x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.71 sec: 1.05x faster                                                   |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                                     |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                     |
| async_generators         | 444 ms                                                 | 451 ms: 1.02x slower                                                     |
| telco                    | 7.27 ms                                                | 7.46 ms: 1.03x slower                                                    |
| coverage                 | 79.4 ms                                                | 84.8 ms: 1.07x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 4.45 ms: 1.23x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 2.66 ms: 1.64x slower                                                    |
| bench_mp_pool            | 24.0 ms                                                | 79.4 ms: 3.31x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                             |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241120-3.14.0a2+-e2daeb7-JIT/bm-20241120-linux-x86_64-brandtbucher-warmup_side_1024-3.14.0a2+-e2daeb7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.414x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.28x