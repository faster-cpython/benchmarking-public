# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmup_side_4096
- machine: linux-x86_64
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.415x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                     |
| docutils       | 3.30 sec                                               | 2.77 sec: 1.19x faster                                                   |
| html5lib       | 88.9 ms                                                | 67.1 ms: 1.32x faster                                                    |
| Geometric mean | (ref)                                                  | 1.28x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 325 ms: 2.24x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 411 ms: 2.12x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 914 ms: 1.94x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 563 ms: 1.81x faster                                                     |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.9 ms: 1.85x faster                                                    |
| float          | 117 ms                                                 | 78.0 ms: 1.50x faster                                                    |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.41x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                     |
| regex_effbot   | 3.63 ms                                                | 3.36 ms: 1.08x faster                                                    |
| regex_v8       | 27.8 ms                                                | 25.9 ms: 1.07x faster                                                    |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                  | 1.15x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 195 us: 1.69x faster                                                     |
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.51x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 55.4 ms: 1.43x faster                                                    |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 78.5 ms: 1.27x faster                                                    |
| json_loads           | 31.2 us                                                | 26.2 us: 1.19x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.13x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.96 ms: 1.64x faster                                                    |
| django_template | 48.2 ms                                                | 33.5 ms: 1.44x faster                                                    |
| genshi_text     | 31.8 ms                                                | 25.4 ms: 1.25x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 59.6 ms: 1.11x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.24x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                                    |
| async_tree_none          | 728 ms                                                 | 325 ms: 2.24x faster                                                     |
| generators               | 80.1 ms                                                | 36.5 ms: 2.19x faster                                                    |
| richards_super           | 94.7 ms                                                | 44.5 ms: 2.13x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 411 ms: 2.12x faster                                                     |
| richards                 | 79.3 ms                                                | 38.5 ms: 2.06x faster                                                    |
| pylint                   | 551 ms                                                 | 272 ms: 2.03x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 29.2 us: 2.00x faster                                                    |
| chaos                    | 115 ms                                                 | 59.6 ms: 1.94x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 914 ms: 1.94x faster                                                     |
| logging_silent           | 190 ns                                                 | 101 ns: 1.87x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 68.5 ms: 1.87x faster                                                    |
| nbody                    | 154 ms                                                 | 82.9 ms: 1.85x faster                                                    |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.84x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 64.6 ms: 1.83x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 563 ms: 1.81x faster                                                     |
| go                       | 240 ms                                                 | 133 ms: 1.80x faster                                                     |
| deepcopy                 | 479 us                                                 | 267 us: 1.79x faster                                                     |
| raytrace                 | 507 ms                                                 | 284 ms: 1.78x faster                                                     |
| djangocms                | 38.4 us                                                | 22.4 us: 1.71x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 195 us: 1.69x faster                                                     |
| comprehensions           | 28.8 us                                                | 17.2 us: 1.67x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                    |
| mako                     | 16.3 ms                                                | 9.96 ms: 1.64x faster                                                    |
| pyflate                  | 716 ms                                                 | 442 ms: 1.62x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                    |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.58x faster                                                     |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.54x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.51x faster                                                     |
| float                    | 117 ms                                                 | 78.0 ms: 1.50x faster                                                    |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.49x faster                                                     |
| hexiom                   | 10.4 ms                                                | 7.04 ms: 1.48x faster                                                    |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                     |
| scimark_fft              | 466 ms                                                 | 318 ms: 1.46x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.70 us: 1.46x faster                                                    |
| logging_format           | 9.09 us                                                | 6.28 us: 1.45x faster                                                    |
| django_template          | 48.2 ms                                                | 33.5 ms: 1.44x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 55.4 ms: 1.43x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 715 ms: 1.42x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.57 ms: 1.42x faster                                                    |
| thrift                   | 1.07 ms                                                | 772 us: 1.39x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                   |
| fannkuch                 | 532 ms                                                 | 386 ms: 1.38x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.3 ms: 1.35x faster                                                    |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.33x faster                                                     |
| html5lib                 | 88.9 ms                                                | 67.1 ms: 1.32x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.29x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 78.5 ms: 1.27x faster                                                    |
| sympy_sum                | 196 ms                                                 | 156 ms: 1.26x faster                                                     |
| genshi_text              | 31.8 ms                                                | 25.4 ms: 1.25x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 67.4 ms: 1.25x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 20.7 ms: 1.25x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 55.7 ms: 1.24x faster                                                    |
| sympy_str                | 346 ms                                                 | 281 ms: 1.23x faster                                                     |
| nqueens                  | 106 ms                                                 | 88.1 ms: 1.20x faster                                                    |
| json_loads               | 31.2 us                                                | 26.2 us: 1.19x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.77 sec: 1.19x faster                                                   |
| json                     | 5.69 ms                                                | 4.78 ms: 1.19x faster                                                    |
| sympy_expand             | 566 ms                                                 | 477 ms: 1.19x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.13x faster                                                     |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 874 us: 1.13x faster                                                     |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 59.6 ms: 1.11x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.59 sec: 1.10x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.36 ms: 1.08x faster                                                    |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 25.9 ms: 1.07x faster                                                    |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                                     |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                     |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                     |
| async_generators         | 444 ms                                                 | 461 ms: 1.04x slower                                                     |
| telco                    | 7.27 ms                                                | 7.57 ms: 1.04x slower                                                    |
| coverage                 | 79.4 ms                                                | 84.2 ms: 1.06x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 4.68 ms: 1.29x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 2.67 ms: 1.65x slower                                                    |
| bench_mp_pool            | 24.0 ms                                                | 79.3 ms: 3.30x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                             |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241122-3.14.0a2+-a8a4ed3-JIT/bm-20241122-linux-x86_64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.415x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.28x