# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_compact
- machine: linux-x86_64
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.38x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 273 ms: 1.27x faster                                                  |
| docutils       | 3.30 sec                                               | 2.87 sec: 1.15x faster                                                |
| html5lib       | 88.9 ms                                                | 66.8 ms: 1.33x faster                                                 |
| tornado_http   | 136 ms                                                 | 94.0 ms: 1.45x faster                                                 |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 364 ms: 2.00x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 934 ms: 1.89x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 483 ms: 1.80x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 608 ms: 1.67x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.84x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.3 ms: 1.91x faster                                                 |
| float          | 117 ms                                                 | 69.8 ms: 1.68x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.49x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.40x faster                                                  |
| regex_v8       | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                 |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 297 us: 1.63x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.61x faster                                                |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                  |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 57.2 ms: 1.38x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 80.4 ms: 1.24x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 99.9 ms: 1.16x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                  |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                                 |
| pickle_list          | 5.08 us                                                | 4.99 us: 1.02x faster                                                 |
| unpickle_list        | 5.20 us                                                | 5.12 us: 1.01x faster                                                 |
| unpickle             | 14.4 us                                                | 15.0 us: 1.04x slower                                                 |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                                 |
| pickle_dict          | 29.6 us                                                | 35.2 us: 1.19x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.9 ms: 1.34x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.43 ms: 1.25x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.70 ms: 1.68x faster                                                 |
| django_template | 48.2 ms                                                | 36.3 ms: 1.33x faster                                                 |
| genshi_text     | 31.8 ms                                                | 24.9 ms: 1.28x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 57.4 ms: 1.15x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.21x faster                                                  |
| generators               | 80.1 ms                                                | 29.6 ms: 2.71x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.55 ms: 2.23x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 28.8 us: 2.03x faster                                                 |
| async_tree_none          | 728 ms                                                 | 364 ms: 2.00x faster                                                  |
| richards_super           | 94.7 ms                                                | 47.7 ms: 1.98x faster                                                 |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                                 |
| nbody                    | 154 ms                                                 | 80.3 ms: 1.91x faster                                                 |
| richards                 | 79.3 ms                                                | 41.5 ms: 1.91x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 67.4 ms: 1.90x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 934 ms: 1.89x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 493 ms: 1.87x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 63.2 ms: 1.87x faster                                                 |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 483 ms: 1.80x faster                                                  |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.75x faster                                                 |
| deepcopy                 | 479 us                                                 | 278 us: 1.73x faster                                                  |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.71x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                                 |
| mako                     | 16.3 ms                                                | 9.70 ms: 1.68x faster                                                 |
| float                    | 117 ms                                                 | 69.8 ms: 1.68x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 608 ms: 1.67x faster                                                  |
| go                       | 240 ms                                                 | 145 ms: 1.66x faster                                                  |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                  |
| pyflate                  | 716 ms                                                 | 438 ms: 1.63x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 297 us: 1.63x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.61x faster                                                |
| pylint                   | 551 ms                                                 | 343 ms: 1.61x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.60x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.52 ms: 1.59x faster                                                 |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                                 |
| fannkuch                 | 532 ms                                                 | 348 ms: 1.53x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.54 us: 1.50x faster                                                 |
| logging_format           | 9.09 us                                                | 6.08 us: 1.50x faster                                                 |
| scimark_fft              | 466 ms                                                 | 318 ms: 1.47x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.44 sec: 1.46x faster                                                |
| tornado_http             | 136 ms                                                 | 94.0 ms: 1.45x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 707 ms: 1.44x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.41x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.61 ms: 1.40x faster                                                 |
| regex_compile            | 188 ms                                                 | 135 ms: 1.40x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                                |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 57.2 ms: 1.38x faster                                                 |
| python_startup           | 14.6 ms                                                | 10.9 ms: 1.34x faster                                                 |
| html5lib                 | 88.9 ms                                                | 66.8 ms: 1.33x faster                                                 |
| django_template          | 48.2 ms                                                | 36.3 ms: 1.33x faster                                                 |
| thrift                   | 1.07 ms                                                | 811 us: 1.32x faster                                                  |
| genshi_text              | 31.8 ms                                                | 24.9 ms: 1.28x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                 |
| 2to3                     | 348 ms                                                 | 273 ms: 1.27x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 68.0 ms: 1.24x faster                                                 |
| nqueens                  | 106 ms                                                 | 85.5 ms: 1.24x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 80.4 ms: 1.24x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 56.1 ms: 1.23x faster                                                 |
| dask                     | 441 ms                                                 | 367 ms: 1.20x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 831 us: 1.19x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 22.0 ms: 1.17x faster                                                 |
| sympy_sum                | 196 ms                                                 | 167 ms: 1.17x faster                                                  |
| sympy_str                | 346 ms                                                 | 296 ms: 1.17x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 99.9 ms: 1.16x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 57.4 ms: 1.15x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.87 sec: 1.15x faster                                                |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                  |
| sympy_expand             | 566 ms                                                 | 500 ms: 1.13x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                                |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                                 |
| json                     | 5.69 ms                                                | 5.30 ms: 1.07x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.82 us: 1.07x faster                                                 |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                                  |
| pickle_list              | 5.08 us                                                | 4.99 us: 1.02x faster                                                 |
| unpickle_list            | 5.20 us                                                | 5.12 us: 1.01x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                  |
| gc_traversal             | 3.62 ms                                                | 3.73 ms: 1.03x slower                                                 |
| async_generators         | 444 ms                                                 | 458 ms: 1.03x slower                                                  |
| unpickle                 | 14.4 us                                                | 15.0 us: 1.04x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.08x slower                                                 |
| telco                    | 7.27 ms                                                | 7.89 ms: 1.09x slower                                                 |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                                 |
| coverage                 | 79.4 ms                                                | 93.5 ms: 1.18x slower                                                 |
| pickle_dict              | 29.6 us                                                | 35.2 us: 1.19x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.43 ms: 1.25x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                          |

Benchmark hidden because not significant (2): bench_mp_pool, regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240620-3.14.0a0-34e6994-JIT/bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.21x