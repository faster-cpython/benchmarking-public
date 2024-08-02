# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmer_side_exits
- machine: linux-x86_64
- commit hash: 080259b
- commit date: 2024-06-20
- overall geometric mean: 1.38x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 276 ms: 1.26x faster                                                     |
| docutils       | 3.30 sec                                               | 2.88 sec: 1.15x faster                                                   |
| html5lib       | 88.9 ms                                                | 65.5 ms: 1.36x faster                                                    |
| tornado_http   | 136 ms                                                 | 94.1 ms: 1.45x faster                                                    |
| Geometric mean | (ref)                                                  | 1.30x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 369 ms: 1.97x faster                                                     |
| async_tree_io           | 1.77 sec                                               | 911 ms: 1.94x faster                                                     |
| async_tree_memoization  | 870 ms                                                 | 452 ms: 1.92x faster                                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 596 ms: 1.71x faster                                                     |
| Geometric mean          | (ref)                                                  | 1.88x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 83.0 ms: 1.85x faster                                                    |
| float          | 117 ms                                                 | 70.6 ms: 1.66x faster                                                    |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.47x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.40x faster                                                     |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                    |
| regex_dna      | 227 ms                                                 | 228 ms: 1.00x slower                                                     |
| regex_effbot   | 3.63 ms                                                | 3.72 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                  | 1.12x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 294 us: 1.65x faster                                                     |
| unpickle_pure_python | 331 us                                                 | 204 us: 1.62x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 57.8 ms: 1.37x faster                                                    |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                    |
| xml_etree_generate   | 99.4 ms                                                | 80.6 ms: 1.23x faster                                                    |
| xml_etree_iterparse  | 115 ms                                                 | 99.3 ms: 1.16x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                     |
| json_loads           | 31.2 us                                                | 28.5 us: 1.10x faster                                                    |
| unpickle_list        | 5.20 us                                                | 5.13 us: 1.01x faster                                                    |
| pickle_list          | 5.08 us                                                | 5.19 us: 1.02x slower                                                    |
| unpickle             | 14.4 us                                                | 15.5 us: 1.08x slower                                                    |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                                    |
| pickle_dict          | 29.6 us                                                | 35.9 us: 1.21x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.8 ms: 1.35x faster                                                    |
| python_startup_no_site | 5.93 ms                                                | 7.39 ms: 1.25x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.58 ms: 1.70x faster                                                    |
| django_template | 48.2 ms                                                | 35.5 ms: 1.36x faster                                                    |
| genshi_text     | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                    |
| genshi_xml      | 66.0 ms                                                | 55.9 ms: 1.18x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.22x faster                                                     |
| generators               | 80.1 ms                                                | 29.7 ms: 2.69x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.84 ms: 2.06x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 29.1 us: 2.01x faster                                                    |
| richards_super           | 94.7 ms                                                | 47.6 ms: 1.99x faster                                                    |
| chaos                    | 115 ms                                                 | 58.3 ms: 1.98x faster                                                    |
| async_tree_none          | 728 ms                                                 | 369 ms: 1.97x faster                                                     |
| richards                 | 79.3 ms                                                | 40.5 ms: 1.95x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 911 ms: 1.94x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 452 ms: 1.92x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 66.8 ms: 1.91x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 61.9 ms: 1.91x faster                                                    |
| asyncio_tcp              | 922 ms                                                 | 491 ms: 1.88x faster                                                     |
| nbody                    | 154 ms                                                 | 83.0 ms: 1.85x faster                                                    |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                                     |
| logging_silent           | 190 ns                                                 | 106 ns: 1.80x faster                                                     |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                                    |
| deepcopy                 | 479 us                                                 | 279 us: 1.72x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 596 ms: 1.71x faster                                                     |
| mako                     | 16.3 ms                                                | 9.58 ms: 1.70x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                    |
| float                    | 117 ms                                                 | 70.6 ms: 1.66x faster                                                    |
| pyflate                  | 716 ms                                                 | 434 ms: 1.65x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.90 sec: 1.65x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 294 us: 1.65x faster                                                     |
| go                       | 240 ms                                                 | 147 ms: 1.63x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 204 us: 1.62x faster                                                     |
| spectral_norm            | 170 ms                                                 | 105 ms: 1.62x faster                                                     |
| scimark_sor              | 220 ms                                                 | 136 ms: 1.62x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.54 ms: 1.59x faster                                                    |
| pylint                   | 551 ms                                                 | 347 ms: 1.59x faster                                                     |
| fannkuch                 | 532 ms                                                 | 345 ms: 1.54x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.22 ms: 1.53x faster                                                    |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.46 us: 1.52x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.76 us: 1.51x faster                                                    |
| logging_format           | 9.09 us                                                | 6.03 us: 1.51x faster                                                    |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                     |
| tornado_http             | 136 ms                                                 | 94.1 ms: 1.45x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.43x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 712 ms: 1.43x faster                                                     |
| scimark_lu               | 176 ms                                                 | 124 ms: 1.42x faster                                                     |
| regex_compile            | 188 ms                                                 | 134 ms: 1.40x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 57.8 ms: 1.37x faster                                                    |
| django_template          | 48.2 ms                                                | 35.5 ms: 1.36x faster                                                    |
| html5lib                 | 88.9 ms                                                | 65.5 ms: 1.36x faster                                                    |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                    |
| python_startup           | 14.6 ms                                                | 10.8 ms: 1.35x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.33x faster                                                   |
| thrift                   | 1.07 ms                                                | 817 us: 1.31x faster                                                     |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.28x faster                                                    |
| genshi_text              | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                    |
| 2to3                     | 348 ms                                                 | 276 ms: 1.26x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                     |
| nqueens                  | 106 ms                                                 | 84.7 ms: 1.25x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 67.7 ms: 1.24x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 80.6 ms: 1.23x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 56.3 ms: 1.23x faster                                                    |
| dask                     | 441 ms                                                 | 366 ms: 1.21x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 827 us: 1.19x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 55.9 ms: 1.18x faster                                                    |
| sympy_sum                | 196 ms                                                 | 169 ms: 1.16x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 99.3 ms: 1.16x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 22.3 ms: 1.16x faster                                                    |
| sympy_str                | 346 ms                                                 | 300 ms: 1.15x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.88 sec: 1.15x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                     |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                                     |
| sympy_expand             | 566 ms                                                 | 505 ms: 1.12x faster                                                     |
| json_loads               | 31.2 us                                                | 28.5 us: 1.10x faster                                                    |
| json                     | 5.69 ms                                                | 5.28 ms: 1.08x faster                                                    |
| sqlite_synth             | 3.02 us                                                | 2.83 us: 1.07x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.75 sec: 1.04x faster                                                   |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                     |
| gc_traversal             | 3.62 ms                                                | 3.57 ms: 1.02x faster                                                    |
| unpickle_list            | 5.20 us                                                | 5.13 us: 1.01x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                     |
| regex_dna                | 227 ms                                                 | 228 ms: 1.00x slower                                                     |
| pickle_list              | 5.08 us                                                | 5.19 us: 1.02x slower                                                    |
| regex_effbot             | 3.63 ms                                                | 3.72 ms: 1.03x slower                                                    |
| async_generators         | 444 ms                                                 | 457 ms: 1.03x slower                                                     |
| unpickle                 | 14.4 us                                                | 15.5 us: 1.08x slower                                                    |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                    |
| telco                    | 7.27 ms                                                | 7.97 ms: 1.10x slower                                                    |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                                    |
| coverage                 | 79.4 ms                                                | 92.9 ms: 1.17x slower                                                    |
| pickle_dict              | 29.6 us                                                | 35.9 us: 1.21x slower                                                    |
| python_startup_no_site   | 5.93 ms                                                | 7.39 ms: 1.25x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                             |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240620-3.14.0a0-080259b-JIT/bm-20240620-linux-x86_64-brandtbucher-warmer_side_exits-3.14.0a0-080259b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.23x