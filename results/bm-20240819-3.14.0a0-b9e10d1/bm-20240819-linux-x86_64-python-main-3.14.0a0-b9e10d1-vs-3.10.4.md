# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: b9e10d1
- commit date: 2024-08-19
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                  |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                |
| html5lib       | 88.9 ms                                                | 65.0 ms: 1.37x faster                                 |
| tornado_http   | 136 ms                                                 | 90.2 ms: 1.51x faster                                 |
| Geometric mean | (ref)                                                  | 1.36x faster                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 323 ms: 2.25x faster                                  |
| async_tree_memoization  | 870 ms                                                 | 423 ms: 2.05x faster                                  |
| async_tree_io           | 1.77 sec                                               | 901 ms: 1.96x faster                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 566 ms: 1.80x faster                                  |
| Geometric mean          | (ref)                                                  | 2.01x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.9 ms: 1.77x faster                                 |
| float          | 117 ms                                                 | 78.6 ms: 1.49x faster                                 |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                  |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.13x faster                                 |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                  |
| Geometric mean | (ref)                                                  | 1.15x faster                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 304 us: 1.59x faster                                  |
| unpickle_pure_python | 331 us                                                 | 212 us: 1.56x faster                                  |
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                 |
| xml_etree_process    | 79.1 ms                                                | 58.6 ms: 1.35x faster                                 |
| xml_etree_generate   | 99.4 ms                                                | 84.8 ms: 1.17x faster                                 |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                  |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                 |
| xml_etree_parse      | 168 ms                                                 | 158 ms: 1.07x faster                                  |
| Geometric mean       | (ref)                                                  | 1.29x faster                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                 |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                 |
| django_template | 48.2 ms                                                | 34.0 ms: 1.42x faster                                 |
| genshi_text     | 31.8 ms                                                | 22.8 ms: 1.40x faster                                 |
| genshi_xml      | 66.0 ms                                                | 50.0 ms: 1.32x faster                                 |
| Geometric mean  | (ref)                                                  | 1.40x faster                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.33x faster                                  |
| generators               | 80.1 ms                                                | 27.8 ms: 2.88x faster                                 |
| deltablue                | 7.91 ms                                                | 3.12 ms: 2.53x faster                                 |
| async_tree_none          | 728 ms                                                 | 323 ms: 2.25x faster                                  |
| async_tree_memoization   | 870 ms                                                 | 423 ms: 2.05x faster                                  |
| raytrace                 | 507 ms                                                 | 255 ms: 1.99x faster                                  |
| async_tree_io            | 1.77 sec                                               | 901 ms: 1.96x faster                                  |
| chaos                    | 115 ms                                                 | 58.9 ms: 1.96x faster                                 |
| deepcopy_memo            | 58.5 us                                                | 29.9 us: 1.95x faster                                 |
| asyncio_tcp              | 922 ms                                                 | 483 ms: 1.91x faster                                  |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                  |
| deepcopy                 | 479 us                                                 | 260 us: 1.85x faster                                  |
| richards_super           | 94.7 ms                                                | 51.7 ms: 1.83x faster                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 566 ms: 1.80x faster                                  |
| nbody                    | 154 ms                                                 | 86.9 ms: 1.77x faster                                 |
| scimark_monte_carlo      | 118 ms                                                 | 67.8 ms: 1.74x faster                                 |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                  |
| richards                 | 79.3 ms                                                | 45.6 ms: 1.74x faster                                 |
| pylint                   | 551 ms                                                 | 318 ms: 1.73x faster                                  |
| crypto_pyaes             | 128 ms                                                 | 74.0 ms: 1.73x faster                                 |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                 |
| go                       | 240 ms                                                 | 141 ms: 1.70x faster                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                 |
| hexiom                   | 10.4 ms                                                | 6.23 ms: 1.67x faster                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                 |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.59x faster                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.58x faster                                 |
| unpickle_pure_python     | 331 us                                                 | 212 us: 1.56x faster                                  |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                  |
| logging_simple           | 8.30 us                                                | 5.42 us: 1.53x faster                                 |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                |
| tornado_http             | 136 ms                                                 | 90.2 ms: 1.51x faster                                 |
| logging_format           | 9.09 us                                                | 6.03 us: 1.51x faster                                 |
| pyflate                  | 716 ms                                                 | 477 ms: 1.50x faster                                  |
| float                    | 117 ms                                                 | 78.6 ms: 1.49x faster                                 |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.48x faster                                  |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                  |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.78 sec: 1.44x faster                                |
| coroutines               | 35.1 ms                                                | 24.7 ms: 1.42x faster                                 |
| django_template          | 48.2 ms                                                | 34.0 ms: 1.42x faster                                 |
| genshi_text              | 31.8 ms                                                | 22.8 ms: 1.40x faster                                 |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                 |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.38x faster                                |
| thrift                   | 1.07 ms                                                | 778 us: 1.38x faster                                  |
| pprint_safe_repr         | 1.02 sec                                               | 739 ms: 1.38x faster                                  |
| html5lib                 | 88.9 ms                                                | 65.0 ms: 1.37x faster                                 |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                 |
| xml_etree_process        | 79.1 ms                                                | 58.6 ms: 1.35x faster                                 |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                  |
| nqueens                  | 106 ms                                                 | 79.9 ms: 1.32x faster                                 |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.32x faster                                  |
| genshi_xml               | 66.0 ms                                                | 50.0 ms: 1.32x faster                                 |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                 |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.29x faster                                  |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.29x faster                                 |
| sqlglot_optimize         | 69.2 ms                                                | 53.6 ms: 1.29x faster                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.03 ms: 1.29x faster                                 |
| scimark_fft              | 466 ms                                                 | 365 ms: 1.28x faster                                  |
| fannkuch                 | 532 ms                                                 | 420 ms: 1.27x faster                                  |
| sympy_str                | 346 ms                                                 | 274 ms: 1.26x faster                                  |
| bench_thread_pool        | 986 us                                                 | 784 us: 1.26x faster                                  |
| sympy_expand             | 566 ms                                                 | 461 ms: 1.23x faster                                  |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                |
| xml_etree_generate       | 99.4 ms                                                | 84.8 ms: 1.17x faster                                 |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.13x faster                                 |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                  |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                  |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                 |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                 |
| xml_etree_parse          | 168 ms                                                 | 158 ms: 1.07x faster                                  |
| mdp                      | 2.85 sec                                               | 2.74 sec: 1.04x faster                                |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                  |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                  |
| async_generators         | 444 ms                                                 | 437 ms: 1.02x faster                                  |
| gc_traversal             | 3.62 ms                                                | 3.72 ms: 1.03x slower                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                 |
| coverage                 | 79.4 ms                                                | 85.2 ms: 1.07x slower                                 |
| telco                    | 7.27 ms                                                | 8.05 ms: 1.11x slower                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                 |
| Geometric mean           | (ref)                                                  | 1.43x faster                                          |

Benchmark hidden because not significant (3): regex_effbot, asyncio_websockets, bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240819-3.14.0a0-b9e10d1/bm-20240819-linux-x86_64-python-main-3.14.0a0-b9e10d1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.12x