# Results vs. 3.10.4

- fork: nohlson
- ref: enable_no_strict_ali
- machine: linux-x86_64
- commit hash: 9134938
- commit date: 2024-06-25
- overall geometric mean: 1.38x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 264 ms: 1.32x faster                                                   |
| docutils       | 3.30 sec                                               | 2.72 sec: 1.21x faster                                                 |
| html5lib       | 88.9 ms                                                | 65.9 ms: 1.35x faster                                                  |
| tornado_http   | 136 ms                                                 | 90.0 ms: 1.51x faster                                                  |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 327 ms: 2.23x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 411 ms: 2.12x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 859 ms: 2.06x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 571 ms: 1.78x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.04x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 92.0 ms: 1.67x faster                                                  |
| float          | 117 ms                                                 | 78.5 ms: 1.49x faster                                                  |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 133 ms: 1.42x faster                                                   |
| regex_v8       | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                  |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.70 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 60.3 ms: 1.31x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 86.4 ms: 1.15x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                                   |
| json_loads           | 31.2 us                                                | 28.2 us: 1.11x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 157 ms: 1.07x faster                                                   |
| unpickle_list        | 5.20 us                                                | 5.28 us: 1.02x slower                                                  |
| pickle_list          | 5.08 us                                                | 5.19 us: 1.02x slower                                                  |
| unpickle             | 14.4 us                                                | 15.1 us: 1.05x slower                                                  |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                                  |
| pickle_dict          | 29.6 us                                                | 35.3 us: 1.19x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                  |
| django_template | 48.2 ms                                                | 33.9 ms: 1.42x faster                                                  |
| genshi_text     | 31.8 ms                                                | 23.6 ms: 1.35x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 51.4 ms: 1.29x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                                   |
| generators               | 80.1 ms                                                | 29.4 ms: 2.72x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                                  |
| async_tree_none          | 728 ms                                                 | 327 ms: 2.23x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 411 ms: 2.12x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 859 ms: 2.06x faster                                                   |
| chaos                    | 115 ms                                                 | 59.0 ms: 1.96x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 475 ms: 1.94x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 30.5 us: 1.92x faster                                                  |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                   |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                                   |
| deepcopy                 | 479 us                                                 | 265 us: 1.81x faster                                                   |
| pylint                   | 551 ms                                                 | 309 ms: 1.79x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 571 ms: 1.78x faster                                                   |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.78x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 67.1 ms: 1.76x faster                                                  |
| richards_super           | 94.7 ms                                                | 53.9 ms: 1.76x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 73.3 ms: 1.74x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                  |
| go                       | 240 ms                                                 | 143 ms: 1.68x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                  |
| nbody                    | 154 ms                                                 | 92.0 ms: 1.67x faster                                                  |
| richards                 | 79.3 ms                                                | 47.7 ms: 1.66x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.26 ms: 1.66x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                   |
| pyflate                  | 716 ms                                                 | 465 ms: 1.54x faster                                                   |
| spectral_norm            | 170 ms                                                 | 111 ms: 1.53x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                                  |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                   |
| tornado_http             | 136 ms                                                 | 90.0 ms: 1.51x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                  |
| logging_format           | 9.09 us                                                | 6.02 us: 1.51x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.50 us: 1.51x faster                                                  |
| float                    | 117 ms                                                 | 78.5 ms: 1.49x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.78 sec: 1.44x faster                                                 |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                  |
| django_template          | 48.2 ms                                                | 33.9 ms: 1.42x faster                                                  |
| regex_compile            | 188 ms                                                 | 133 ms: 1.42x faster                                                   |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                  |
| thrift                   | 1.07 ms                                                | 791 us: 1.36x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                                 |
| html5lib                 | 88.9 ms                                                | 65.9 ms: 1.35x faster                                                  |
| genshi_text              | 31.8 ms                                                | 23.6 ms: 1.35x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 761 ms: 1.34x faster                                                   |
| fannkuch                 | 532 ms                                                 | 398 ms: 1.34x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                 |
| nqueens                  | 106 ms                                                 | 79.4 ms: 1.33x faster                                                  |
| 2to3                     | 348 ms                                                 | 264 ms: 1.32x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 60.3 ms: 1.31x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 64.4 ms: 1.31x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.96 ms: 1.30x faster                                                  |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.29x faster                                                   |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.29x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 51.4 ms: 1.29x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 54.5 ms: 1.27x faster                                                  |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 788 us: 1.25x faster                                                   |
| scimark_fft              | 466 ms                                                 | 374 ms: 1.25x faster                                                   |
| dask                     | 441 ms                                                 | 356 ms: 1.24x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.72 sec: 1.21x faster                                                 |
| sympy_expand             | 566 ms                                                 | 471 ms: 1.20x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 86.4 ms: 1.15x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.14x faster                                                 |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                                   |
| json_loads               | 31.2 us                                                | 28.2 us: 1.11x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                  |
| json                     | 5.69 ms                                                | 5.25 ms: 1.08x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 157 ms: 1.07x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.91 us: 1.04x faster                                                  |
| async_generators         | 444 ms                                                 | 429 ms: 1.03x faster                                                   |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                                   |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                   |
| unpickle_list            | 5.20 us                                                | 5.28 us: 1.02x slower                                                  |
| regex_effbot             | 3.63 ms                                                | 3.70 ms: 1.02x slower                                                  |
| pickle_list              | 5.08 us                                                | 5.19 us: 1.02x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 3.72 ms: 1.03x slower                                                  |
| unpickle                 | 14.4 us                                                | 15.1 us: 1.05x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                                  |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                                  |
| telco                    | 7.27 ms                                                | 8.33 ms: 1.15x slower                                                  |
| coverage                 | 79.4 ms                                                | 93.0 ms: 1.17x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                  |
| pickle_dict              | 29.6 us                                                | 35.3 us: 1.19x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240625-3.14.0a0-9134938/bm-20240625-linux-x86_64-nohlson-enable_no_strict_ali-3.14.0a0-9134938.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.11x