# Results vs. 3.10.4

- fork: python
- ref: b5e142ba7c2063efe9bb
- machine: linux-x86_64
- commit hash: b5e142b
- commit date: 2024-08-06
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 275 ms: 1.27x faster                                                  |
| docutils       | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                |
| html5lib       | 88.9 ms                                                | 63.8 ms: 1.39x faster                                                 |
| tornado_http   | 136 ms                                                 | 92.6 ms: 1.47x faster                                                 |
| Geometric mean | (ref)                                                  | 1.31x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 327 ms: 2.23x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 422 ms: 2.06x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 910 ms: 1.94x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 570 ms: 1.78x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.00x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.1 ms: 1.94x faster                                                 |
| float          | 117 ms                                                 | 70.5 ms: 1.66x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.49x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.40x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                 |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.83 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                |
| pickle_pure_python   | 484 us                                                 | 300 us: 1.61x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 57.2 ms: 1.38x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 81.6 ms: 1.22x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 99.2 ms: 1.16x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                  |
| json_loads           | 31.2 us                                                | 27.7 us: 1.13x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.85 ms: 1.66x faster                                                 |
| django_template | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                 |
| genshi_text     | 31.8 ms                                                | 24.5 ms: 1.30x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 53.4 ms: 1.24x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.19x faster                                                  |
| generators               | 80.1 ms                                                | 32.9 ms: 2.44x faster                                                 |
| async_tree_none          | 728 ms                                                 | 327 ms: 2.23x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.58 ms: 2.21x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 422 ms: 2.06x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.1 us: 2.01x faster                                                 |
| richards_super           | 94.7 ms                                                | 47.5 ms: 1.99x faster                                                 |
| chaos                    | 115 ms                                                 | 58.1 ms: 1.99x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 60.7 ms: 1.95x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 910 ms: 1.94x faster                                                  |
| nbody                    | 154 ms                                                 | 79.1 ms: 1.94x faster                                                 |
| richards                 | 79.3 ms                                                | 41.2 ms: 1.93x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 66.8 ms: 1.91x faster                                                 |
| raytrace                 | 507 ms                                                 | 269 ms: 1.88x faster                                                  |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 498 ms: 1.85x faster                                                  |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 570 ms: 1.78x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.2 us: 1.77x faster                                                 |
| deepcopy                 | 479 us                                                 | 273 us: 1.75x faster                                                  |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.69x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                 |
| float                    | 117 ms                                                 | 70.5 ms: 1.66x faster                                                 |
| pyflate                  | 716 ms                                                 | 432 ms: 1.66x faster                                                  |
| mako                     | 16.3 ms                                                | 9.85 ms: 1.66x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                |
| go                       | 240 ms                                                 | 146 ms: 1.64x faster                                                  |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.62x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.61x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                 |
| pylint                   | 551 ms                                                 | 356 ms: 1.55x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.71 ms: 1.55x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                 |
| scimark_fft              | 466 ms                                                 | 307 ms: 1.52x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.78 us: 1.50x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.57 us: 1.49x faster                                                 |
| logging_format           | 9.09 us                                                | 6.17 us: 1.47x faster                                                 |
| tornado_http             | 136 ms                                                 | 92.6 ms: 1.47x faster                                                 |
| fannkuch                 | 532 ms                                                 | 371 ms: 1.43x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.55 ms: 1.42x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 722 ms: 1.41x faster                                                  |
| regex_compile            | 188 ms                                                 | 135 ms: 1.40x faster                                                  |
| html5lib                 | 88.9 ms                                                | 63.8 ms: 1.39x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 57.2 ms: 1.38x faster                                                 |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                 |
| thrift                   | 1.07 ms                                                | 797 us: 1.35x faster                                                  |
| django_template          | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.33x faster                                                |
| genshi_text              | 31.8 ms                                                | 24.5 ms: 1.30x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                                  |
| 2to3                     | 348 ms                                                 | 275 ms: 1.27x faster                                                  |
| nqueens                  | 106 ms                                                 | 84.0 ms: 1.26x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 55.9 ms: 1.24x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 53.4 ms: 1.24x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 81.6 ms: 1.22x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 822 us: 1.20x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 99.2 ms: 1.16x faster                                                 |
| sympy_str                | 346 ms                                                 | 298 ms: 1.16x faster                                                  |
| sympy_sum                | 196 ms                                                 | 170 ms: 1.15x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 22.6 ms: 1.14x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                 |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.13x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.92 sec: 1.13x faster                                                |
| json_loads               | 31.2 us                                                | 27.7 us: 1.13x faster                                                 |
| json                     | 5.69 ms                                                | 5.09 ms: 1.12x faster                                                 |
| sympy_expand             | 566 ms                                                 | 508 ms: 1.11x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                                |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                  |
| async_generators         | 444 ms                                                 | 453 ms: 1.02x slower                                                  |
| regex_effbot             | 3.63 ms                                                | 3.83 ms: 1.05x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 3.85 ms: 1.06x slower                                                 |
| telco                    | 7.27 ms                                                | 7.97 ms: 1.10x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                 |
| coverage                 | 79.4 ms                                                | 91.8 ms: 1.16x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240806-3.14.0a0-b5e142b-JIT/bm-20240806-linux-x86_64-python-b5e142ba7c2063efe9bb-3.14.0a0-b5e142b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.20x