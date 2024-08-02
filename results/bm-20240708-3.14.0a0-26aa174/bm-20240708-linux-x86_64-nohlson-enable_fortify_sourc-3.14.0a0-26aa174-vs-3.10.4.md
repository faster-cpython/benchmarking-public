# Results vs. 3.10.4

- fork: nohlson
- ref: enable_fortify_sourc
- machine: linux-x86_64
- commit hash: 26aa174
- commit date: 2024-07-08
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.33x faster                                                   |
| docutils       | 3.30 sec                                               | 2.71 sec: 1.22x faster                                                 |
| html5lib       | 88.9 ms                                                | 65.8 ms: 1.35x faster                                                  |
| tornado_http   | 136 ms                                                 | 90.4 ms: 1.51x faster                                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 321 ms: 2.27x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 408 ms: 2.13x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 850 ms: 2.08x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 560 ms: 1.81x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.07x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 85.0 ms: 1.81x faster                                                  |
| float          | 117 ms                                                 | 75.5 ms: 1.55x faster                                                  |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.42x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                   |
| regex_v8       | 27.8 ms                                                | 25.8 ms: 1.08x faster                                                  |
| regex_dna      | 227 ms                                                 | 229 ms: 1.01x slower                                                   |
| regex_effbot   | 3.63 ms                                                | 3.82 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 299 us: 1.62x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 208 us: 1.59x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 58.8 ms: 1.35x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 84.7 ms: 1.17x faster                                                  |
| json_loads           | 31.2 us                                                | 27.3 us: 1.14x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 157 ms: 1.07x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.0 ms: 1.48x faster                                                  |
| django_template | 48.2 ms                                                | 33.7 ms: 1.43x faster                                                  |
| genshi_text     | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 50.8 ms: 1.30x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.35x faster                                                   |
| generators               | 80.1 ms                                                | 28.9 ms: 2.77x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.14 ms: 2.52x faster                                                  |
| async_tree_none          | 728 ms                                                 | 321 ms: 2.27x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 408 ms: 2.13x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 850 ms: 2.08x faster                                                   |
| chaos                    | 115 ms                                                 | 57.8 ms: 2.00x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                                  |
| raytrace                 | 507 ms                                                 | 256 ms: 1.98x faster                                                   |
| logging_silent           | 190 ns                                                 | 97.1 ns: 1.95x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 485 ms: 1.90x faster                                                   |
| richards_super           | 94.7 ms                                                | 51.4 ms: 1.84x faster                                                  |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                                   |
| pylint                   | 551 ms                                                 | 301 ms: 1.83x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 560 ms: 1.81x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 70.5 ms: 1.81x faster                                                  |
| nbody                    | 154 ms                                                 | 85.0 ms: 1.81x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 66.7 ms: 1.77x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.3 us: 1.76x faster                                                  |
| scimark_sor              | 220 ms                                                 | 125 ms: 1.75x faster                                                   |
| go                       | 240 ms                                                 | 138 ms: 1.74x faster                                                   |
| richards                 | 79.3 ms                                                | 45.8 ms: 1.73x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.01 ms: 1.73x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.56 ms: 1.65x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 299 us: 1.62x faster                                                   |
| pyflate                  | 716 ms                                                 | 443 ms: 1.62x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 208 us: 1.59x faster                                                   |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.58x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                                  |
| float                    | 117 ms                                                 | 75.5 ms: 1.55x faster                                                  |
| spectral_norm            | 170 ms                                                 | 110 ms: 1.54x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.50 us: 1.51x faster                                                  |
| tornado_http             | 136 ms                                                 | 90.4 ms: 1.51x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                 |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.48x faster                                                  |
| logging_format           | 9.09 us                                                | 6.20 us: 1.47x faster                                                  |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.78 sec: 1.44x faster                                                 |
| django_template          | 48.2 ms                                                | 33.7 ms: 1.43x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.38x faster                                                 |
| genshi_text              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                  |
| fannkuch                 | 532 ms                                                 | 386 ms: 1.38x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 745 ms: 1.37x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                  |
| thrift                   | 1.07 ms                                                | 793 us: 1.35x faster                                                   |
| html5lib                 | 88.9 ms                                                | 65.8 ms: 1.35x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 58.8 ms: 1.35x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.81 ms: 1.35x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                                 |
| nqueens                  | 106 ms                                                 | 78.9 ms: 1.34x faster                                                  |
| 2to3                     | 348 ms                                                 | 261 ms: 1.33x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.33x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 64.1 ms: 1.31x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                                  |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 50.8 ms: 1.30x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 53.4 ms: 1.29x faster                                                  |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                  |
| scimark_fft              | 466 ms                                                 | 362 ms: 1.29x faster                                                   |
| sympy_str                | 346 ms                                                 | 274 ms: 1.26x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 791 us: 1.25x faster                                                   |
| dask                     | 441 ms                                                 | 357 ms: 1.23x faster                                                   |
| sympy_expand             | 566 ms                                                 | 463 ms: 1.22x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.71 sec: 1.22x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 84.7 ms: 1.17x faster                                                  |
| json_loads               | 31.2 us                                                | 27.3 us: 1.14x faster                                                  |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                   |
| json                     | 5.69 ms                                                | 5.11 ms: 1.11x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 25.8 ms: 1.08x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 157 ms: 1.07x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.66 sec: 1.07x faster                                                 |
| async_generators         | 444 ms                                                 | 427 ms: 1.04x faster                                                   |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                   |
| regex_dna                | 227 ms                                                 | 229 ms: 1.01x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 3.76 ms: 1.04x slower                                                  |
| regex_effbot             | 3.63 ms                                                | 3.82 ms: 1.05x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                  |
| telco                    | 7.27 ms                                                | 8.26 ms: 1.14x slower                                                  |
| coverage                 | 79.4 ms                                                | 92.4 ms: 1.16x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240708-3.14.0a0-26aa174/bm-20240708-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-26aa174.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.11x