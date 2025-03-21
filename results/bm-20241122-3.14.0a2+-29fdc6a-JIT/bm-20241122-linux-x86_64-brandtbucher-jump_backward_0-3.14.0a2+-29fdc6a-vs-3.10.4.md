# Results vs. 3.10.4

- fork: brandtbucher
- ref: jump_backward_0
- machine: linux-x86_64
- commit hash: 29fdc6a
- commit date: 2024-11-22
- overall geometric mean: 1.360x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 268 ms: 1.30x faster                                                    |
| docutils       | 3.30 sec                                               | 3.02 sec: 1.09x faster                                                  |
| html5lib       | 88.9 ms                                                | 67.2 ms: 1.32x faster                                                   |
| Geometric mean | (ref)                                                  | 1.23x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 338 ms: 2.15x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 423 ms: 2.06x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 939 ms: 1.88x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 582 ms: 1.75x faster                                                    |
| Geometric mean          | (ref)                                                  | 1.95x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.8 ms: 1.85x faster                                                   |
| float          | 117 ms                                                 | 77.4 ms: 1.51x faster                                                   |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.42x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 137 ms: 1.38x faster                                                    |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.45 ms: 1.05x faster                                                   |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.12x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.60x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 324 us: 1.49x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                   |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                   |
| json_loads           | 31.2 us                                                | 26.0 us: 1.20x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 83.8 ms: 1.19x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                    |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.6 ms: 1.54x faster                                                   |
| django_template | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                   |
| genshi_text     | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 58.2 ms: 1.14x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.18x faster                                                    |
| generators               | 80.1 ms                                                | 36.9 ms: 2.17x faster                                                   |
| async_tree_none          | 728 ms                                                 | 338 ms: 2.15x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 423 ms: 2.06x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.93 ms: 2.01x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 29.6 us: 1.97x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 62.4 ms: 1.89x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 939 ms: 1.88x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 68.1 ms: 1.88x faster                                                   |
| chaos                    | 115 ms                                                 | 61.8 ms: 1.87x faster                                                   |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                                    |
| go                       | 240 ms                                                 | 129 ms: 1.86x faster                                                    |
| nbody                    | 154 ms                                                 | 82.8 ms: 1.85x faster                                                   |
| pylint                   | 551 ms                                                 | 305 ms: 1.81x faster                                                    |
| richards_super           | 94.7 ms                                                | 52.7 ms: 1.80x faster                                                   |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.79x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 582 ms: 1.75x faster                                                    |
| deepcopy                 | 479 us                                                 | 277 us: 1.73x faster                                                    |
| raytrace                 | 507 ms                                                 | 294 ms: 1.72x faster                                                    |
| richards                 | 79.3 ms                                                | 46.7 ms: 1.70x faster                                                   |
| comprehensions           | 28.8 us                                                | 17.7 us: 1.63x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.60x faster                                                  |
| djangocms                | 38.4 us                                                | 24.3 us: 1.58x faster                                                   |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                                    |
| mako                     | 16.3 ms                                                | 10.6 ms: 1.54x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                    |
| pyflate                  | 716 ms                                                 | 468 ms: 1.53x faster                                                    |
| float                    | 117 ms                                                 | 77.4 ms: 1.51x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.43 ms: 1.51x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 324 us: 1.49x faster                                                    |
| scimark_fft              | 466 ms                                                 | 316 ms: 1.47x faster                                                    |
| spectral_norm            | 170 ms                                                 | 118 ms: 1.44x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.90 us: 1.44x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.80 ms: 1.43x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.58 ms: 1.41x faster                                                   |
| hexiom                   | 10.4 ms                                                | 7.40 ms: 1.40x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.39x faster                                                  |
| regex_compile            | 188 ms                                                 | 137 ms: 1.38x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 744 ms: 1.37x faster                                                    |
| fannkuch                 | 532 ms                                                 | 389 ms: 1.37x faster                                                    |
| django_template          | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                   |
| html5lib                 | 88.9 ms                                                | 67.2 ms: 1.32x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                                  |
| genshi_text              | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                   |
| 2to3                     | 348 ms                                                 | 268 ms: 1.30x faster                                                    |
| thrift                   | 1.07 ms                                                | 825 us: 1.30x faster                                                    |
| coroutines               | 35.1 ms                                                | 27.1 ms: 1.30x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.29x faster                                                    |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.26x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 117 ms: 1.22x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 69.0 ms: 1.22x faster                                                   |
| logging_format           | 9.09 us                                                | 7.46 us: 1.22x faster                                                   |
| logging_simple           | 8.30 us                                                | 6.84 us: 1.21x faster                                                   |
| json_loads               | 31.2 us                                                | 26.0 us: 1.20x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 83.8 ms: 1.19x faster                                                   |
| json                     | 5.69 ms                                                | 4.84 ms: 1.18x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 59.4 ms: 1.17x faster                                                   |
| nqueens                  | 106 ms                                                 | 90.8 ms: 1.17x faster                                                   |
| sympy_str                | 346 ms                                                 | 297 ms: 1.16x faster                                                    |
| sqlalchemy_imperative    | 23.3 ms                                                | 20.2 ms: 1.15x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 22.4 ms: 1.15x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                    |
| genshi_xml               | 66.0 ms                                                | 58.2 ms: 1.14x faster                                                   |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                    |
| sympy_expand             | 566 ms                                                 | 501 ms: 1.13x faster                                                    |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                    |
| sympy_sum                | 196 ms                                                 | 178 ms: 1.10x faster                                                    |
| docutils                 | 3.30 sec                                               | 3.02 sec: 1.09x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.09x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.64 sec: 1.08x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 923 us: 1.07x faster                                                    |
| regex_effbot             | 3.63 ms                                                | 3.45 ms: 1.05x faster                                                   |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                    |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                                    |
| telco                    | 7.27 ms                                                | 7.46 ms: 1.03x slower                                                   |
| async_generators         | 444 ms                                                 | 457 ms: 1.03x slower                                                    |
| coverage                 | 79.4 ms                                                | 87.9 ms: 1.11x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 4.52 ms: 1.25x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 2.66 ms: 1.64x slower                                                   |
| bench_mp_pool            | 24.0 ms                                                | 79.4 ms: 3.31x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                            |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241122-3.14.0a2+-29fdc6a-JIT/bm-20241122-linux-x86_64-brandtbucher-jump_backward_0-3.14.0a2+-29fdc6a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.360x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.29x