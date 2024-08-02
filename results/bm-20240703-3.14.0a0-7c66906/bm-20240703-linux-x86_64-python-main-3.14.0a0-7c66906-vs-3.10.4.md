# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 7c66906
- commit date: 2024-07-03
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 348 ms                                                 | 262 ms: 1.33x faster                                  |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.23x faster                                |
| html5lib       | 88.9 ms                                                | 64.2 ms: 1.38x faster                                 |
| tornado_http   | 136 ms                                                 | 90.2 ms: 1.51x faster                                 |
| Geometric mean | (ref)                                                  | 1.36x faster                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 321 ms: 2.27x faster                                  |
| async_tree_memoization  | 870 ms                                                 | 405 ms: 2.15x faster                                  |
| async_tree_io           | 1.77 sec                                               | 827 ms: 2.14x faster                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 566 ms: 1.80x faster                                  |
| Geometric mean          | (ref)                                                  | 2.08x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.5 ms: 1.77x faster                                 |
| float          | 117 ms                                                 | 76.4 ms: 1.53x faster                                 |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                  | 1.41x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                  |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                 |
| regex_dna      | 227 ms                                                 | 231 ms: 1.02x slower                                  |
| regex_effbot   | 3.63 ms                                                | 3.79 ms: 1.05x slower                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 300 us: 1.61x faster                                  |
| unpickle_pure_python | 331 us                                                 | 211 us: 1.57x faster                                  |
| tomli_loads          | 3.14 sec                                               | 2.12 sec: 1.48x faster                                |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.34x faster                                 |
| xml_etree_process    | 79.1 ms                                                | 59.2 ms: 1.34x faster                                 |
| xml_etree_generate   | 99.4 ms                                                | 85.2 ms: 1.17x faster                                 |
| json_loads           | 31.2 us                                                | 27.8 us: 1.12x faster                                 |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                  |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                  |
| Geometric mean       | (ref)                                                  | 1.30x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                 |
| python_startup_no_site | 5.93 ms                                                | 7.03 ms: 1.19x slower                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.9 ms: 1.50x faster                                 |
| django_template | 48.2 ms                                                | 33.7 ms: 1.43x faster                                 |
| genshi_text     | 31.8 ms                                                | 22.9 ms: 1.39x faster                                 |
| genshi_xml      | 66.0 ms                                                | 49.2 ms: 1.34x faster                                 |
| Geometric mean  | (ref)                                                  | 1.41x faster                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.35x faster                                  |
| generators               | 80.1 ms                                                | 28.7 ms: 2.79x faster                                 |
| deltablue                | 7.91 ms                                                | 3.17 ms: 2.49x faster                                 |
| async_tree_none          | 728 ms                                                 | 321 ms: 2.27x faster                                  |
| async_tree_memoization   | 870 ms                                                 | 405 ms: 2.15x faster                                  |
| async_tree_io            | 1.77 sec                                               | 827 ms: 2.14x faster                                  |
| deepcopy_memo            | 58.5 us                                                | 29.0 us: 2.02x faster                                 |
| raytrace                 | 507 ms                                                 | 254 ms: 1.99x faster                                  |
| chaos                    | 115 ms                                                 | 57.9 ms: 1.99x faster                                 |
| asyncio_tcp              | 922 ms                                                 | 487 ms: 1.89x faster                                  |
| logging_silent           | 190 ns                                                 | 102 ns: 1.87x faster                                  |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                  |
| richards_super           | 94.7 ms                                                | 52.0 ms: 1.82x faster                                 |
| pylint                   | 551 ms                                                 | 307 ms: 1.80x faster                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 566 ms: 1.80x faster                                  |
| scimark_monte_carlo      | 118 ms                                                 | 66.4 ms: 1.78x faster                                 |
| nbody                    | 154 ms                                                 | 86.5 ms: 1.77x faster                                 |
| scimark_sor              | 220 ms                                                 | 125 ms: 1.76x faster                                  |
| crypto_pyaes             | 128 ms                                                 | 72.7 ms: 1.76x faster                                 |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                 |
| richards                 | 79.3 ms                                                | 45.9 ms: 1.73x faster                                 |
| go                       | 240 ms                                                 | 140 ms: 1.72x faster                                  |
| hexiom                   | 10.4 ms                                                | 6.08 ms: 1.71x faster                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                 |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.61x faster                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.62 us: 1.59x faster                                 |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.59x faster                                  |
| spectral_norm            | 170 ms                                                 | 108 ms: 1.58x faster                                  |
| unpickle_pure_python     | 331 us                                                 | 211 us: 1.57x faster                                  |
| pyflate                  | 716 ms                                                 | 467 ms: 1.53x faster                                  |
| float                    | 117 ms                                                 | 76.4 ms: 1.53x faster                                 |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.52x faster                                 |
| tornado_http             | 136 ms                                                 | 90.2 ms: 1.51x faster                                 |
| mako                     | 16.3 ms                                                | 10.9 ms: 1.50x faster                                 |
| logging_simple           | 8.30 us                                                | 5.57 us: 1.49x faster                                 |
| tomli_loads              | 3.14 sec                                               | 2.12 sec: 1.48x faster                                |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                  |
| logging_format           | 9.09 us                                                | 6.24 us: 1.46x faster                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.78 sec: 1.45x faster                                |
| django_template          | 48.2 ms                                                | 33.7 ms: 1.43x faster                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.58 ms: 1.41x faster                                 |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                 |
| genshi_text              | 31.8 ms                                                | 22.9 ms: 1.39x faster                                 |
| html5lib                 | 88.9 ms                                                | 64.2 ms: 1.38x faster                                 |
| pprint_safe_repr         | 1.02 sec                                               | 739 ms: 1.38x faster                                  |
| thrift                   | 1.07 ms                                                | 791 us: 1.36x faster                                  |
| nqueens                  | 106 ms                                                 | 78.1 ms: 1.35x faster                                 |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.34x faster                                 |
| genshi_xml               | 66.0 ms                                                | 49.2 ms: 1.34x faster                                 |
| fannkuch                 | 532 ms                                                 | 397 ms: 1.34x faster                                  |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                |
| xml_etree_process        | 79.1 ms                                                | 59.2 ms: 1.34x faster                                 |
| scimark_fft              | 466 ms                                                 | 350 ms: 1.33x faster                                  |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.33x faster                                  |
| 2to3                     | 348 ms                                                 | 262 ms: 1.33x faster                                  |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.32x faster                                 |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                  |
| dulwich_log              | 84.3 ms                                                | 64.3 ms: 1.31x faster                                 |
| sqlglot_optimize         | 69.2 ms                                                | 53.4 ms: 1.30x faster                                 |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.28x faster                                 |
| sympy_str                | 346 ms                                                 | 269 ms: 1.28x faster                                  |
| bench_thread_pool        | 986 us                                                 | 791 us: 1.25x faster                                  |
| sympy_expand             | 566 ms                                                 | 458 ms: 1.24x faster                                  |
| dask                     | 441 ms                                                 | 357 ms: 1.24x faster                                  |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.23x faster                                |
| xml_etree_generate       | 99.4 ms                                                | 85.2 ms: 1.17x faster                                 |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                  |
| json_loads               | 31.2 us                                                | 27.8 us: 1.12x faster                                 |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                  |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                 |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                 |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                  |
| mdp                      | 2.85 sec                                               | 2.74 sec: 1.04x faster                                |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                  |
| async_generators         | 444 ms                                                 | 437 ms: 1.01x faster                                  |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                  |
| gc_traversal             | 3.62 ms                                                | 3.68 ms: 1.02x slower                                 |
| regex_dna                | 227 ms                                                 | 231 ms: 1.02x slower                                  |
| regex_effbot             | 3.63 ms                                                | 3.79 ms: 1.05x slower                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.73 ms: 1.07x slower                                 |
| telco                    | 7.27 ms                                                | 8.22 ms: 1.13x slower                                 |
| coverage                 | 79.4 ms                                                | 92.7 ms: 1.17x slower                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.03 ms: 1.19x slower                                 |
| Geometric mean           | (ref)                                                  | 1.43x faster                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240703-3.14.0a0-7c66906/bm-20240703-linux-x86_64-python-main-3.14.0a0-7c66906.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.11x