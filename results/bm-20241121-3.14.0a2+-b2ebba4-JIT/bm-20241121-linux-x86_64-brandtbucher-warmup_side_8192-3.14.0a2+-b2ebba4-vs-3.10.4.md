# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmup_side_8192
- machine: linux-x86_64
- commit hash: b2ebba4
- commit date: 2024-11-21
- overall geometric mean: 1.416x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                     |
| docutils       | 3.30 sec                                               | 2.75 sec: 1.20x faster                                                   |
| html5lib       | 88.9 ms                                                | 66.1 ms: 1.34x faster                                                    |
| Geometric mean | (ref)                                                  | 1.29x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 324 ms: 2.25x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 410 ms: 2.12x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 909 ms: 1.95x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 560 ms: 1.81x faster                                                     |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.4 ms: 1.89x faster                                                    |
| float          | 117 ms                                                 | 78.4 ms: 1.49x faster                                                    |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.42x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.47x faster                                                     |
| regex_v8       | 27.8 ms                                                | 26.0 ms: 1.07x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.43 ms: 1.06x faster                                                    |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.14x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 192 us: 1.72x faster                                                     |
| tomli_loads          | 3.14 sec                                               | 2.00 sec: 1.57x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 328 us: 1.48x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 55.8 ms: 1.42x faster                                                    |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 79.1 ms: 1.26x faster                                                    |
| json_loads           | 31.2 us                                                | 26.2 us: 1.19x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.13x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.3 ms: 1.59x faster                                                    |
| django_template | 48.2 ms                                                | 33.6 ms: 1.43x faster                                                    |
| genshi_text     | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 60.4 ms: 1.09x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.18 ms: 2.49x faster                                                    |
| async_tree_none          | 728 ms                                                 | 324 ms: 2.25x faster                                                     |
| generators               | 80.1 ms                                                | 35.6 ms: 2.25x faster                                                    |
| richards_super           | 94.7 ms                                                | 44.5 ms: 2.13x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 410 ms: 2.12x faster                                                     |
| richards                 | 79.3 ms                                                | 38.6 ms: 2.05x faster                                                    |
| pylint                   | 551 ms                                                 | 273 ms: 2.02x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 1.99x faster                                                    |
| chaos                    | 115 ms                                                 | 59.0 ms: 1.96x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 909 ms: 1.95x faster                                                     |
| nbody                    | 154 ms                                                 | 81.4 ms: 1.89x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 68.2 ms: 1.87x faster                                                    |
| go                       | 240 ms                                                 | 128 ms: 1.87x faster                                                     |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                     |
| logging_silent           | 190 ns                                                 | 103 ns: 1.85x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 64.6 ms: 1.83x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 560 ms: 1.81x faster                                                     |
| raytrace                 | 507 ms                                                 | 286 ms: 1.77x faster                                                     |
| deepcopy                 | 479 us                                                 | 273 us: 1.76x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 192 us: 1.72x faster                                                     |
| djangocms                | 38.4 us                                                | 22.7 us: 1.69x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.65x faster                                                    |
| comprehensions           | 28.8 us                                                | 17.5 us: 1.64x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                    |
| mako                     | 16.3 ms                                                | 10.3 ms: 1.59x faster                                                    |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.59x faster                                                     |
| pyflate                  | 716 ms                                                 | 455 ms: 1.57x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 2.00 sec: 1.57x faster                                                   |
| spectral_norm            | 170 ms                                                 | 111 ms: 1.53x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                                    |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                    |
| logging_format           | 9.09 us                                                | 6.08 us: 1.50x faster                                                    |
| float                    | 117 ms                                                 | 78.4 ms: 1.49x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.96 ms: 1.49x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.59 us: 1.49x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 328 us: 1.48x faster                                                     |
| scimark_fft              | 466 ms                                                 | 316 ms: 1.47x faster                                                     |
| regex_compile            | 188 ms                                                 | 129 ms: 1.47x faster                                                     |
| django_template          | 48.2 ms                                                | 33.6 ms: 1.43x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 55.8 ms: 1.42x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.62 ms: 1.40x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 731 ms: 1.39x faster                                                     |
| thrift                   | 1.07 ms                                                | 776 us: 1.38x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.37x faster                                                    |
| fannkuch                 | 532 ms                                                 | 394 ms: 1.35x faster                                                     |
| html5lib                 | 88.9 ms                                                | 66.1 ms: 1.34x faster                                                    |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.33x faster                                                     |
| genshi_text              | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.28x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                    |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.26x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 67.1 ms: 1.26x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 79.1 ms: 1.26x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 20.7 ms: 1.25x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 55.5 ms: 1.25x faster                                                    |
| sympy_str                | 346 ms                                                 | 281 ms: 1.23x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.75 sec: 1.20x faster                                                   |
| json_loads               | 31.2 us                                                | 26.2 us: 1.19x faster                                                    |
| nqueens                  | 106 ms                                                 | 89.4 ms: 1.18x faster                                                    |
| sympy_expand             | 566 ms                                                 | 479 ms: 1.18x faster                                                     |
| json                     | 5.69 ms                                                | 4.93 ms: 1.15x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                     |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.13x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 871 us: 1.13x faster                                                     |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 60.4 ms: 1.09x faster                                                    |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 26.0 ms: 1.07x faster                                                    |
| regex_effbot             | 3.63 ms                                                | 3.43 ms: 1.06x faster                                                    |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.78 sec: 1.02x faster                                                   |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                     |
| async_generators         | 444 ms                                                 | 456 ms: 1.03x slower                                                     |
| telco                    | 7.27 ms                                                | 7.67 ms: 1.06x slower                                                    |
| coverage                 | 79.4 ms                                                | 84.3 ms: 1.06x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 4.35 ms: 1.20x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 2.64 ms: 1.63x slower                                                    |
| bench_mp_pool            | 24.0 ms                                                | 79.3 ms: 3.30x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                             |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241121-3.14.0a2+-b2ebba4-JIT/bm-20241121-linux-x86_64-brandtbucher-warmup_side_8192-3.14.0a2+-b2ebba4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.416x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.28x