# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmup_side_4096
- machine: linux-x86_64
- commit hash: bba66e4
- commit date: 2024-11-20
- overall geometric mean: 1.418x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.34x faster                                                     |
| docutils       | 3.30 sec                                               | 2.77 sec: 1.19x faster                                                   |
| html5lib       | 88.9 ms                                                | 66.3 ms: 1.34x faster                                                    |
| Geometric mean | (ref)                                                  | 1.29x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 325 ms: 2.24x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 411 ms: 2.12x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 903 ms: 1.96x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 562 ms: 1.81x faster                                                     |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 83.2 ms: 1.85x faster                                                    |
| float          | 117 ms                                                 | 79.0 ms: 1.48x faster                                                    |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.41x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.47x faster                                                     |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.42 ms: 1.06x faster                                                    |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.15x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 195 us: 1.69x faster                                                     |
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 317 us: 1.53x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 55.7 ms: 1.42x faster                                                    |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 79.0 ms: 1.26x faster                                                    |
| json_loads           | 31.2 us                                                | 26.1 us: 1.20x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.0 ms: 1.62x faster                                                    |
| django_template | 48.2 ms                                                | 33.3 ms: 1.45x faster                                                    |
| genshi_text     | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 58.5 ms: 1.13x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.23x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.18 ms: 2.48x faster                                                    |
| async_tree_none          | 728 ms                                                 | 325 ms: 2.24x faster                                                     |
| generators               | 80.1 ms                                                | 36.5 ms: 2.19x faster                                                    |
| richards_super           | 94.7 ms                                                | 44.7 ms: 2.12x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 411 ms: 2.12x faster                                                     |
| richards                 | 79.3 ms                                                | 38.7 ms: 2.05x faster                                                    |
| pylint                   | 551 ms                                                 | 271 ms: 2.04x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 29.2 us: 2.00x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 903 ms: 1.96x faster                                                     |
| chaos                    | 115 ms                                                 | 59.3 ms: 1.95x faster                                                    |
| logging_silent           | 190 ns                                                 | 98.5 ns: 1.93x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 67.2 ms: 1.90x faster                                                    |
| nbody                    | 154 ms                                                 | 83.2 ms: 1.85x faster                                                    |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 562 ms: 1.81x faster                                                     |
| deepcopy                 | 479 us                                                 | 266 us: 1.80x faster                                                     |
| go                       | 240 ms                                                 | 133 ms: 1.80x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 65.7 ms: 1.80x faster                                                    |
| raytrace                 | 507 ms                                                 | 285 ms: 1.78x faster                                                     |
| djangocms                | 38.4 us                                                | 22.3 us: 1.72x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 195 us: 1.69x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.65x faster                                                    |
| comprehensions           | 28.8 us                                                | 17.5 us: 1.65x faster                                                    |
| pyflate                  | 716 ms                                                 | 438 ms: 1.64x faster                                                     |
| mako                     | 16.3 ms                                                | 10.0 ms: 1.62x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                    |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.55x faster                                                     |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 317 us: 1.53x faster                                                     |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.50x faster                                                     |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.59 us: 1.48x faster                                                    |
| float                    | 117 ms                                                 | 79.0 ms: 1.48x faster                                                    |
| hexiom                   | 10.4 ms                                                | 7.02 ms: 1.48x faster                                                    |
| logging_format           | 9.09 us                                                | 6.20 us: 1.47x faster                                                    |
| regex_compile            | 188 ms                                                 | 129 ms: 1.47x faster                                                     |
| django_template          | 48.2 ms                                                | 33.3 ms: 1.45x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.52 ms: 1.43x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 716 ms: 1.42x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 55.7 ms: 1.42x faster                                                    |
| thrift                   | 1.07 ms                                                | 773 us: 1.39x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.37x faster                                                    |
| fannkuch                 | 532 ms                                                 | 390 ms: 1.36x faster                                                     |
| 2to3                     | 348 ms                                                 | 259 ms: 1.34x faster                                                     |
| html5lib                 | 88.9 ms                                                | 66.3 ms: 1.34x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.33x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.27x faster                                                    |
| genshi_text              | 31.8 ms                                                | 25.1 ms: 1.27x faster                                                    |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.27x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 79.0 ms: 1.26x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 67.1 ms: 1.26x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.25x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 20.7 ms: 1.25x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 55.6 ms: 1.24x faster                                                    |
| sympy_str                | 346 ms                                                 | 280 ms: 1.23x faster                                                     |
| nqueens                  | 106 ms                                                 | 88.5 ms: 1.20x faster                                                    |
| json_loads               | 31.2 us                                                | 26.1 us: 1.20x faster                                                    |
| json                     | 5.69 ms                                                | 4.77 ms: 1.19x faster                                                    |
| sympy_expand             | 566 ms                                                 | 475 ms: 1.19x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.77 sec: 1.19x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                     |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 872 us: 1.13x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 58.5 ms: 1.13x faster                                                    |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.59 sec: 1.10x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                    |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                    |
| regex_effbot             | 3.63 ms                                                | 3.42 ms: 1.06x faster                                                    |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                                     |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                     |
| async_generators         | 444 ms                                                 | 450 ms: 1.01x slower                                                     |
| telco                    | 7.27 ms                                                | 7.50 ms: 1.03x slower                                                    |
| coverage                 | 79.4 ms                                                | 83.1 ms: 1.05x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 4.54 ms: 1.25x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 2.65 ms: 1.64x slower                                                    |
| bench_mp_pool            | 24.0 ms                                                | 78.8 ms: 3.28x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                             |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241120-3.14.0a2+-bba66e4-JIT/bm-20241120-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-bba66e4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.418x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.28x