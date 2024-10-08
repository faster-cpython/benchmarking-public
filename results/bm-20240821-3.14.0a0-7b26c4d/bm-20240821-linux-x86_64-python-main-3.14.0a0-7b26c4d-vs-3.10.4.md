# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 7b26c4d
- commit date: 2024-08-21
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 348 ms                                                 | 262 ms: 1.33x faster                                  |
| docutils       | 3.30 sec                                               | 2.72 sec: 1.21x faster                                |
| html5lib       | 88.9 ms                                                | 63.5 ms: 1.40x faster                                 |
| tornado_http   | 136 ms                                                 | 90.2 ms: 1.51x faster                                 |
| Geometric mean | (ref)                                                  | 1.36x faster                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 323 ms: 2.26x faster                                  |
| async_tree_memoization  | 870 ms                                                 | 413 ms: 2.10x faster                                  |
| async_tree_io           | 1.77 sec                                               | 903 ms: 1.96x faster                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 560 ms: 1.82x faster                                  |
| Geometric mean          | (ref)                                                  | 2.03x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 154 ms                                                 | 87.7 ms: 1.75x faster                                 |
| float          | 117 ms                                                 | 78.3 ms: 1.50x faster                                 |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                  |
| regex_v8       | 27.8 ms                                                | 24.9 ms: 1.12x faster                                 |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 303 us: 1.60x faster                                  |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                  |
| tomli_loads          | 3.14 sec                                               | 2.07 sec: 1.52x faster                                |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                 |
| xml_etree_process    | 79.1 ms                                                | 59.6 ms: 1.33x faster                                 |
| xml_etree_generate   | 99.4 ms                                                | 86.1 ms: 1.16x faster                                 |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                  |
| json_loads           | 31.2 us                                                | 28.4 us: 1.10x faster                                 |
| xml_etree_parse      | 168 ms                                                 | 153 ms: 1.10x faster                                  |
| Geometric mean       | (ref)                                                  | 1.29x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                 |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.20x slower                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                 |
| django_template | 48.2 ms                                                | 33.8 ms: 1.42x faster                                 |
| genshi_text     | 31.8 ms                                                | 23.5 ms: 1.35x faster                                 |
| genshi_xml      | 66.0 ms                                                | 51.3 ms: 1.29x faster                                 |
| Geometric mean  | (ref)                                                  | 1.38x faster                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.30x faster                                  |
| generators               | 80.1 ms                                                | 27.9 ms: 2.87x faster                                 |
| deltablue                | 7.91 ms                                                | 3.16 ms: 2.51x faster                                 |
| async_tree_none          | 728 ms                                                 | 323 ms: 2.26x faster                                  |
| async_tree_memoization   | 870 ms                                                 | 413 ms: 2.10x faster                                  |
| async_tree_io            | 1.77 sec                                               | 903 ms: 1.96x faster                                  |
| chaos                    | 115 ms                                                 | 59.3 ms: 1.95x faster                                 |
| deepcopy_memo            | 58.5 us                                                | 30.2 us: 1.93x faster                                 |
| raytrace                 | 507 ms                                                 | 263 ms: 1.92x faster                                  |
| asyncio_tcp              | 922 ms                                                 | 480 ms: 1.92x faster                                  |
| logging_silent           | 190 ns                                                 | 100 ns: 1.89x faster                                  |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 560 ms: 1.82x faster                                  |
| richards_super           | 94.7 ms                                                | 52.8 ms: 1.79x faster                                 |
| crypto_pyaes             | 128 ms                                                 | 71.9 ms: 1.78x faster                                 |
| comprehensions           | 28.8 us                                                | 16.3 us: 1.76x faster                                 |
| scimark_sor              | 220 ms                                                 | 125 ms: 1.75x faster                                  |
| nbody                    | 154 ms                                                 | 87.7 ms: 1.75x faster                                 |
| pylint                   | 551 ms                                                 | 317 ms: 1.74x faster                                  |
| scimark_monte_carlo      | 118 ms                                                 | 68.3 ms: 1.73x faster                                 |
| richards                 | 79.3 ms                                                | 46.6 ms: 1.70x faster                                 |
| hexiom                   | 10.4 ms                                                | 6.13 ms: 1.70x faster                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                 |
| go                       | 240 ms                                                 | 146 ms: 1.65x faster                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                 |
| pickle_pure_python       | 484 us                                                 | 303 us: 1.60x faster                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                 |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                  |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                  |
| spectral_norm            | 170 ms                                                 | 111 ms: 1.53x faster                                  |
| logging_simple           | 8.30 us                                                | 5.45 us: 1.52x faster                                 |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                 |
| pyflate                  | 716 ms                                                 | 472 ms: 1.52x faster                                  |
| tomli_loads              | 3.14 sec                                               | 2.07 sec: 1.52x faster                                |
| tornado_http             | 136 ms                                                 | 90.2 ms: 1.51x faster                                 |
| logging_format           | 9.09 us                                                | 6.06 us: 1.50x faster                                 |
| float                    | 117 ms                                                 | 78.3 ms: 1.50x faster                                 |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                  |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.78 sec: 1.44x faster                                |
| django_template          | 48.2 ms                                                | 33.8 ms: 1.42x faster                                 |
| thrift                   | 1.07 ms                                                | 754 us: 1.42x faster                                  |
| html5lib                 | 88.9 ms                                                | 63.5 ms: 1.40x faster                                 |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.39x faster                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.67 ms: 1.39x faster                                 |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                 |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.38x faster                                |
| pprint_safe_repr         | 1.02 sec                                               | 740 ms: 1.38x faster                                  |
| genshi_text              | 31.8 ms                                                | 23.5 ms: 1.35x faster                                 |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                 |
| 2to3                     | 348 ms                                                 | 262 ms: 1.33x faster                                  |
| xml_etree_process        | 79.1 ms                                                | 59.6 ms: 1.33x faster                                 |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.33x faster                                  |
| nqueens                  | 106 ms                                                 | 80.1 ms: 1.32x faster                                 |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                  |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                  |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                 |
| scimark_fft              | 466 ms                                                 | 361 ms: 1.29x faster                                  |
| sqlglot_optimize         | 69.2 ms                                                | 53.7 ms: 1.29x faster                                 |
| genshi_xml               | 66.0 ms                                                | 51.3 ms: 1.29x faster                                 |
| sympy_str                | 346 ms                                                 | 271 ms: 1.28x faster                                  |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                 |
| bench_thread_pool        | 986 us                                                 | 785 us: 1.26x faster                                  |
| sympy_expand             | 566 ms                                                 | 458 ms: 1.23x faster                                  |
| docutils                 | 3.30 sec                                               | 2.72 sec: 1.21x faster                                |
| xml_etree_generate       | 99.4 ms                                                | 86.1 ms: 1.16x faster                                 |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                  |
| regex_v8                 | 27.8 ms                                                | 24.9 ms: 1.12x faster                                 |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                  |
| json_loads               | 31.2 us                                                | 28.4 us: 1.10x faster                                 |
| xml_etree_parse          | 168 ms                                                 | 153 ms: 1.10x faster                                  |
| mdp                      | 2.85 sec                                               | 2.60 sec: 1.09x faster                                |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                 |
| async_generators         | 444 ms                                                 | 433 ms: 1.02x faster                                  |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                  |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                  |
| coverage                 | 79.4 ms                                                | 83.8 ms: 1.05x slower                                 |
| gc_traversal             | 3.62 ms                                                | 3.85 ms: 1.06x slower                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.08x slower                                 |
| telco                    | 7.27 ms                                                | 8.18 ms: 1.13x slower                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.20x slower                                 |
| Geometric mean           | (ref)                                                  | 1.43x faster                                          |

Benchmark hidden because not significant (3): regex_effbot, bench_mp_pool, asyncio_websockets
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240821-3.14.0a0-7b26c4d/bm-20240821-linux-x86_64-python-main-3.14.0a0-7b26c4d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.12x