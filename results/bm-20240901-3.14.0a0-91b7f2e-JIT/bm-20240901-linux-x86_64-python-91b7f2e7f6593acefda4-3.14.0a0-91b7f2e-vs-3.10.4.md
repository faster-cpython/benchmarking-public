# Results vs. 3.10.4

- fork: python
- ref: 91b7f2e7f6593acefda4
- machine: linux-x86_64
- commit hash: 91b7f2e
- commit date: 2024-09-01
- overall geometric mean: 1.432x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 276 ms: 1.26x faster                                                  |
| docutils       | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                |
| html5lib       | 88.9 ms                                                | 64.7 ms: 1.37x faster                                                 |
| tornado_http   | 136 ms                                                 | 94.4 ms: 1.44x faster                                                 |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.24x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 401 ms: 2.17x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 933 ms: 1.90x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 554 ms: 1.83x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.8 ms: 1.92x faster                                                 |
| float          | 117 ms                                                 | 70.1 ms: 1.67x faster                                                 |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.49x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 141 ms: 1.33x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                 |
| regex_dna      | 227 ms                                                 | 217 ms: 1.05x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.52 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                |
| pickle_pure_python   | 484 us                                                 | 304 us: 1.59x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 55.1 ms: 1.44x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 77.6 ms: 1.28x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 98.3 ms: 1.17x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                                  |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.15 ms: 1.20x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.97 ms: 1.64x faster                                                 |
| django_template | 48.2 ms                                                | 36.3 ms: 1.33x faster                                                 |
| genshi_text     | 31.8 ms                                                | 24.9 ms: 1.28x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 58.3 ms: 1.13x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.31x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                                 |
| generators               | 80.1 ms                                                | 33.1 ms: 2.42x faster                                                 |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.24x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 26.7 us: 2.19x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 401 ms: 2.17x faster                                                  |
| richards_super           | 94.7 ms                                                | 45.4 ms: 2.09x faster                                                 |
| richards                 | 79.3 ms                                                | 39.3 ms: 2.02x faster                                                 |
| chaos                    | 115 ms                                                 | 58.5 ms: 1.97x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 65.7 ms: 1.95x faster                                                 |
| nbody                    | 154 ms                                                 | 79.8 ms: 1.92x faster                                                 |
| scimark_sor              | 220 ms                                                 | 116 ms: 1.90x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 933 ms: 1.90x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 62.9 ms: 1.88x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 495 ms: 1.86x faster                                                  |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                                  |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 554 ms: 1.83x faster                                                  |
| go                       | 240 ms                                                 | 131 ms: 1.83x faster                                                  |
| deepcopy                 | 479 us                                                 | 267 us: 1.79x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                 |
| spectral_norm            | 170 ms                                                 | 99.9 ms: 1.70x faster                                                 |
| float                    | 117 ms                                                 | 70.1 ms: 1.67x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                |
| mako                     | 16.3 ms                                                | 9.97 ms: 1.64x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.62x faster                                                 |
| pyflate                  | 716 ms                                                 | 449 ms: 1.59x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.59x faster                                                  |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.58x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                                 |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.54x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.52x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.86 ms: 1.52x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.51 us: 1.51x faster                                                 |
| scimark_fft              | 466 ms                                                 | 309 ms: 1.51x faster                                                  |
| logging_format           | 9.09 us                                                | 6.07 us: 1.50x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.34 ms: 1.49x faster                                                 |
| pylint                   | 551 ms                                                 | 372 ms: 1.48x faster                                                  |
| tornado_http             | 136 ms                                                 | 94.4 ms: 1.44x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 55.1 ms: 1.44x faster                                                 |
| fannkuch                 | 532 ms                                                 | 372 ms: 1.43x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 718 ms: 1.42x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                 |
| html5lib                 | 88.9 ms                                                | 64.7 ms: 1.37x faster                                                 |
| thrift                   | 1.07 ms                                                | 786 us: 1.36x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                |
| regex_compile            | 188 ms                                                 | 141 ms: 1.33x faster                                                  |
| django_template          | 48.2 ms                                                | 36.3 ms: 1.33x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 77.6 ms: 1.28x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                 |
| genshi_text              | 31.8 ms                                                | 24.9 ms: 1.28x faster                                                 |
| 2to3                     | 348 ms                                                 | 276 ms: 1.26x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                  |
| nqueens                  | 106 ms                                                 | 85.1 ms: 1.24x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 68.2 ms: 1.24x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 833 us: 1.18x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 58.4 ms: 1.18x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 98.3 ms: 1.17x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                                  |
| sympy_str                | 346 ms                                                 | 301 ms: 1.15x faster                                                  |
| sympy_sum                | 196 ms                                                 | 173 ms: 1.14x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 58.3 ms: 1.13x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                                 |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                                |
| sympy_expand             | 566 ms                                                 | 507 ms: 1.12x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                 |
| json                     | 5.69 ms                                                | 5.36 ms: 1.06x faster                                                 |
| regex_dna                | 227 ms                                                 | 217 ms: 1.05x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.52 ms: 1.03x faster                                                 |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                  |
| gc_traversal             | 3.62 ms                                                | 3.56 ms: 1.02x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                  |
| async_generators         | 444 ms                                                 | 455 ms: 1.03x slower                                                  |
| coverage                 | 79.4 ms                                                | 85.4 ms: 1.07x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                 |
| telco                    | 7.27 ms                                                | 7.93 ms: 1.09x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.15 ms: 1.20x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240901-3.14.0a0-91b7f2e-JIT/bm-20240901-linux-x86_64-python-91b7f2e7f6593acefda4-3.14.0a0-91b7f2e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.432x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.22x