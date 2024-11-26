# Results vs. 3.10.4

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: linux-x86_64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.440x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                  |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                |
| html5lib       | 88.9 ms                                                | 64.5 ms: 1.38x faster                                                 |
| tornado_http   | 136 ms                                                 | 90.2 ms: 1.51x faster                                                 |
| Geometric mean | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 322 ms: 2.26x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 397 ms: 2.19x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 901 ms: 1.96x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 556 ms: 1.83x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 84.7 ms: 1.81x faster                                                 |
| float          | 117 ms                                                 | 77.9 ms: 1.50x faster                                                 |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.41x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                  |
| regex_v8       | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                 |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 298 us: 1.62x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 209 us: 1.58x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.06 sec: 1.52x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 59.1 ms: 1.34x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 86.3 ms: 1.15x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                                  |
| json_loads           | 31.2 us                                                | 28.5 us: 1.09x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 157 ms: 1.07x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.1 ms: 1.48x faster                                                 |
| django_template | 48.2 ms                                                | 33.8 ms: 1.42x faster                                                 |
| genshi_text     | 31.8 ms                                                | 22.5 ms: 1.41x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 50.0 ms: 1.32x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                                  |
| generators               | 80.1 ms                                                | 27.7 ms: 2.89x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.17 ms: 2.50x faster                                                 |
| async_tree_none          | 728 ms                                                 | 322 ms: 2.26x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 397 ms: 2.19x faster                                                  |
| raytrace                 | 507 ms                                                 | 253 ms: 2.01x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.1 us: 2.01x faster                                                 |
| chaos                    | 115 ms                                                 | 58.3 ms: 1.98x faster                                                 |
| logging_silent           | 190 ns                                                 | 96.5 ns: 1.97x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 901 ms: 1.96x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 487 ms: 1.89x faster                                                  |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                                  |
| richards_super           | 94.7 ms                                                | 51.2 ms: 1.85x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 556 ms: 1.83x faster                                                  |
| nbody                    | 154 ms                                                 | 84.7 ms: 1.81x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 66.2 ms: 1.78x faster                                                 |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.77x faster                                                  |
| richards                 | 79.3 ms                                                | 45.1 ms: 1.76x faster                                                 |
| pylint                   | 551 ms                                                 | 317 ms: 1.74x faster                                                  |
| go                       | 240 ms                                                 | 138 ms: 1.74x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 74.4 ms: 1.72x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.17 ms: 1.68x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 298 us: 1.62x faster                                                  |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.58x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 209 us: 1.58x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                 |
| pyflate                  | 716 ms                                                 | 466 ms: 1.54x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.46 us: 1.52x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 2.06 sec: 1.52x faster                                                |
| tornado_http             | 136 ms                                                 | 90.2 ms: 1.51x faster                                                 |
| logging_format           | 9.09 us                                                | 6.03 us: 1.51x faster                                                 |
| float                    | 117 ms                                                 | 77.9 ms: 1.50x faster                                                 |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                                  |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.48x faster                                                 |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.52 ms: 1.43x faster                                                 |
| django_template          | 48.2 ms                                                | 33.8 ms: 1.42x faster                                                 |
| genshi_text              | 31.8 ms                                                | 22.5 ms: 1.41x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 736 ms: 1.38x faster                                                  |
| html5lib                 | 88.9 ms                                                | 64.5 ms: 1.38x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                 |
| thrift                   | 1.07 ms                                                | 784 us: 1.37x faster                                                  |
| nqueens                  | 106 ms                                                 | 78.7 ms: 1.34x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 59.1 ms: 1.34x faster                                                 |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 50.0 ms: 1.32x faster                                                 |
| fannkuch                 | 532 ms                                                 | 405 ms: 1.31x faster                                                  |
| scimark_fft              | 466 ms                                                 | 356 ms: 1.31x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 53.1 ms: 1.30x faster                                                 |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                  |
| sympy_str                | 346 ms                                                 | 271 ms: 1.27x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 787 us: 1.25x faster                                                  |
| sympy_expand             | 566 ms                                                 | 460 ms: 1.23x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                |
| regex_v8                 | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 86.3 ms: 1.15x faster                                                 |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                                  |
| json_loads               | 31.2 us                                                | 28.5 us: 1.09x faster                                                 |
| json                     | 5.69 ms                                                | 5.28 ms: 1.08x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 157 ms: 1.07x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.71 sec: 1.05x faster                                                |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                                  |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| async_generators         | 444 ms                                                 | 436 ms: 1.02x faster                                                  |
| gc_traversal             | 3.62 ms                                                | 3.57 ms: 1.01x faster                                                 |
| coverage                 | 79.4 ms                                                | 83.9 ms: 1.06x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                                 |
| telco                    | 7.27 ms                                                | 8.15 ms: 1.12x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                          |

Benchmark hidden because not significant (3): regex_effbot, asyncio_websockets, bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-linux-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.440x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.12x