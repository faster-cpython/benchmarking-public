# Results vs. 3.10.4

- fork: nohlson
- ref: enable_fortify_sourc
- machine: linux-x86_64
- commit hash: 7a595e7
- commit date: 2024-07-14
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 263 ms: 1.32x faster                                                   |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                 |
| html5lib       | 88.9 ms                                                | 64.9 ms: 1.37x faster                                                  |
| tornado_http   | 136 ms                                                 | 89.8 ms: 1.52x faster                                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.24x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 408 ms: 2.13x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 849 ms: 2.08x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 566 ms: 1.80x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.06x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 91.4 ms: 1.68x faster                                                  |
| float          | 117 ms                                                 | 78.1 ms: 1.50x faster                                                  |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 131 ms: 1.44x faster                                                   |
| regex_v8       | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                  |
| regex_dna      | 227 ms                                                 | 217 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.15x faster                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 303 us: 1.60x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 211 us: 1.56x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 2.12 sec: 1.48x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.34x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 85.9 ms: 1.16x faster                                                  |
| json_loads           | 31.2 us                                                | 27.4 us: 1.14x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 158 ms: 1.07x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                  |
| django_template | 48.2 ms                                                | 34.3 ms: 1.41x faster                                                  |
| genshi_text     | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 50.2 ms: 1.31x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                                   |
| generators               | 80.1 ms                                                | 29.3 ms: 2.73x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.29 ms: 2.40x faster                                                  |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.24x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 408 ms: 2.13x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 849 ms: 2.08x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 30.0 us: 1.95x faster                                                  |
| chaos                    | 115 ms                                                 | 59.9 ms: 1.93x faster                                                  |
| raytrace                 | 507 ms                                                 | 269 ms: 1.89x faster                                                   |
| asyncio_tcp              | 922 ms                                                 | 492 ms: 1.87x faster                                                   |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                   |
| pylint                   | 551 ms                                                 | 302 ms: 1.82x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 566 ms: 1.80x faster                                                   |
| richards_super           | 94.7 ms                                                | 53.1 ms: 1.78x faster                                                  |
| logging_silent           | 190 ns                                                 | 108 ns: 1.76x faster                                                   |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.76x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 72.9 ms: 1.75x faster                                                  |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.75x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 68.8 ms: 1.72x faster                                                  |
| go                       | 240 ms                                                 | 140 ms: 1.71x faster                                                   |
| nbody                    | 154 ms                                                 | 91.4 ms: 1.68x faster                                                  |
| richards                 | 79.3 ms                                                | 47.2 ms: 1.68x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.24 ms: 1.67x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 303 us: 1.60x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 211 us: 1.56x faster                                                   |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                   |
| pyflate                  | 716 ms                                                 | 467 ms: 1.53x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                                  |
| tornado_http             | 136 ms                                                 | 89.8 ms: 1.52x faster                                                  |
| spectral_norm            | 170 ms                                                 | 112 ms: 1.51x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.51 us: 1.51x faster                                                  |
| float                    | 117 ms                                                 | 78.1 ms: 1.50x faster                                                  |
| logging_format           | 9.09 us                                                | 6.09 us: 1.49x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.12 sec: 1.48x faster                                                 |
| regex_compile            | 188 ms                                                 | 131 ms: 1.44x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                 |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                  |
| django_template          | 48.2 ms                                                | 34.3 ms: 1.41x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                                 |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.38x faster                                                 |
| genshi_text              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.72 ms: 1.37x faster                                                  |
| html5lib                 | 88.9 ms                                                | 64.9 ms: 1.37x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 745 ms: 1.37x faster                                                   |
| nqueens                  | 106 ms                                                 | 78.5 ms: 1.35x faster                                                  |
| thrift                   | 1.07 ms                                                | 796 us: 1.35x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.34x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 63.7 ms: 1.32x faster                                                  |
| fannkuch                 | 532 ms                                                 | 401 ms: 1.32x faster                                                   |
| 2to3                     | 348 ms                                                 | 263 ms: 1.32x faster                                                   |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.31x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 50.2 ms: 1.31x faster                                                  |
| pathlib                  | 20.5 ms                                                | 15.6 ms: 1.31x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 53.5 ms: 1.29x faster                                                  |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                                   |
| scimark_fft              | 466 ms                                                 | 370 ms: 1.26x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 792 us: 1.25x faster                                                   |
| dask                     | 441 ms                                                 | 359 ms: 1.23x faster                                                   |
| sympy_expand             | 566 ms                                                 | 461 ms: 1.23x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.23x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 85.9 ms: 1.16x faster                                                  |
| json_loads               | 31.2 us                                                | 27.4 us: 1.14x faster                                                  |
| json                     | 5.69 ms                                                | 5.10 ms: 1.12x faster                                                  |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 158 ms: 1.07x faster                                                   |
| regex_dna                | 227 ms                                                 | 217 ms: 1.05x faster                                                   |
| async_generators         | 444 ms                                                 | 428 ms: 1.04x faster                                                   |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                   |
| gc_traversal             | 3.62 ms                                                | 3.69 ms: 1.02x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                  |
| telco                    | 7.27 ms                                                | 8.34 ms: 1.15x slower                                                  |
| coverage                 | 79.4 ms                                                | 93.1 ms: 1.17x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                           |

Benchmark hidden because not significant (3): asyncio_websockets, bench_mp_pool, regex_effbot
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240714-3.14.0a0-7a595e7/bm-20240714-linux-x86_64-nohlson-enable_fortify_sourc-3.14.0a0-7a595e7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.11x