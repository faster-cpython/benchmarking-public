# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: partial_evaluator_un
- machine: linux-x86_64
- commit hash: aaab6a6
- commit date: 2024-09-20
- overall geometric mean: 1.38x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.84x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 276 ms: 1.26x faster                                                            |
| docutils       | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                          |
| html5lib       | 88.9 ms                                                | 65.1 ms: 1.36x faster                                                           |
| tornado_http   | 136 ms                                                 | 95.1 ms: 1.43x faster                                                           |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 320 ms: 2.28x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 403 ms: 2.16x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 862 ms: 2.05x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 569 ms: 1.79x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.06x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.1 ms: 1.89x faster                                                           |
| float          | 117 ms                                                 | 69.4 ms: 1.69x faster                                                           |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.48x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 142 ms: 1.33x faster                                                            |
| regex_v8       | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                           |
| regex_dna      | 227 ms                                                 | 226 ms: 1.00x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.92 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                          |
| pickle_pure_python   | 484 us                                                 | 309 us: 1.57x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 53.7 ms: 1.47x faster                                                           |
| json_dumps           | 14.2 ms                                                | 10.1 ms: 1.40x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 76.7 ms: 1.30x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 98.1 ms: 1.18x faster                                                           |
| json_loads           | 31.2 us                                                | 26.6 us: 1.17x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                            |
| unpickle_list        | 5.20 us                                                | 5.29 us: 1.02x slower                                                           |
| pickle_list          | 5.08 us                                                | 5.17 us: 1.02x slower                                                           |
| pickle               | 10.7 us                                                | 11.6 us: 1.08x slower                                                           |
| pickle_dict          | 29.6 us                                                | 34.4 us: 1.16x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                                    |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.92 ms: 1.65x faster                                                           |
| django_template | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                           |
| genshi_text     | 31.8 ms                                                | 24.6 ms: 1.29x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 58.1 ms: 1.14x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.31x faster                                                            |
| deltablue                | 7.91 ms                                                | 3.23 ms: 2.45x faster                                                           |
| generators               | 80.1 ms                                                | 33.0 ms: 2.43x faster                                                           |
| async_tree_none          | 728 ms                                                 | 320 ms: 2.28x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 26.9 us: 2.18x faster                                                           |
| async_tree_memoization   | 870 ms                                                 | 403 ms: 2.16x faster                                                            |
| richards_super           | 94.7 ms                                                | 45.7 ms: 2.07x faster                                                           |
| async_tree_io            | 1.77 sec                                               | 862 ms: 2.05x faster                                                            |
| richards                 | 79.3 ms                                                | 39.6 ms: 2.00x faster                                                           |
| chaos                    | 115 ms                                                 | 58.4 ms: 1.98x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 66.4 ms: 1.92x faster                                                           |
| nbody                    | 154 ms                                                 | 81.1 ms: 1.89x faster                                                           |
| asyncio_tcp              | 922 ms                                                 | 497 ms: 1.85x faster                                                            |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                            |
| logging_silent           | 190 ns                                                 | 103 ns: 1.85x faster                                                            |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                            |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 64.2 ms: 1.84x faster                                                           |
| go                       | 240 ms                                                 | 132 ms: 1.82x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 569 ms: 1.79x faster                                                            |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                           |
| float                    | 117 ms                                                 | 69.4 ms: 1.69x faster                                                           |
| mako                     | 16.3 ms                                                | 9.92 ms: 1.65x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                          |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.60x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.35 ms: 1.60x faster                                                           |
| spectral_norm            | 170 ms                                                 | 107 ms: 1.59x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.63 us: 1.58x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 309 us: 1.57x faster                                                            |
| coroutines               | 35.1 ms                                                | 22.5 ms: 1.56x faster                                                           |
| pyflate                  | 716 ms                                                 | 464 ms: 1.54x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.86 ms: 1.52x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.71 ms: 1.51x faster                                                           |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.37 ms: 1.48x faster                                                           |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                                           |
| pylint                   | 551 ms                                                 | 373 ms: 1.48x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 53.7 ms: 1.47x faster                                                           |
| scimark_fft              | 466 ms                                                 | 320 ms: 1.46x faster                                                            |
| tornado_http             | 136 ms                                                 | 95.1 ms: 1.43x faster                                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                          |
| fannkuch                 | 532 ms                                                 | 375 ms: 1.42x faster                                                            |
| json_dumps               | 14.2 ms                                                | 10.1 ms: 1.40x faster                                                           |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.37x faster                                                          |
| html5lib                 | 88.9 ms                                                | 65.1 ms: 1.36x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                          |
| thrift                   | 1.07 ms                                                | 792 us: 1.35x faster                                                            |
| pprint_safe_repr         | 1.02 sec                                               | 754 ms: 1.35x faster                                                            |
| django_template          | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                           |
| regex_compile            | 188 ms                                                 | 142 ms: 1.33x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 76.7 ms: 1.30x faster                                                           |
| genshi_text              | 31.8 ms                                                | 24.6 ms: 1.29x faster                                                           |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.29x faster                                                           |
| 2to3                     | 348 ms                                                 | 276 ms: 1.26x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                            |
| dulwich_log              | 84.3 ms                                                | 67.2 ms: 1.25x faster                                                           |
| nqueens                  | 106 ms                                                 | 85.7 ms: 1.23x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 58.4 ms: 1.19x faster                                                           |
| bench_thread_pool        | 986 us                                                 | 835 us: 1.18x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 98.1 ms: 1.18x faster                                                           |
| json_loads               | 31.2 us                                                | 26.6 us: 1.17x faster                                                           |
| sympy_str                | 346 ms                                                 | 298 ms: 1.16x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                            |
| json                     | 5.69 ms                                                | 4.97 ms: 1.14x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                           |
| sympy_sum                | 196 ms                                                 | 173 ms: 1.14x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 58.1 ms: 1.14x faster                                                           |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                                           |
| sympy_expand             | 566 ms                                                 | 505 ms: 1.12x faster                                                            |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                          |
| docutils                 | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                          |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                                           |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                            |
| regex_dna                | 227 ms                                                 | 226 ms: 1.00x faster                                                            |
| unpickle_list            | 5.20 us                                                | 5.29 us: 1.02x slower                                                           |
| pickle_list              | 5.08 us                                                | 5.17 us: 1.02x slower                                                           |
| async_generators         | 444 ms                                                 | 456 ms: 1.03x slower                                                            |
| coverage                 | 79.4 ms                                                | 84.2 ms: 1.06x slower                                                           |
| regex_effbot             | 3.63 ms                                                | 3.92 ms: 1.08x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 3.91 ms: 1.08x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                           |
| telco                    | 7.27 ms                                                | 7.88 ms: 1.08x slower                                                           |
| pickle                   | 10.7 us                                                | 11.6 us: 1.08x slower                                                           |
| pickle_dict              | 29.6 us                                                | 34.4 us: 1.16x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                           |
| unpack_sequence          | 60.0 ns                                                | 111 ns: 1.85x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                                    |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240920-3.14.0a0-aaab6a6-JIT/bm-20240920-linux-x86_64-Fidget%2dSpinner-partial_evaluator_un-3.14.0a0-aaab6a6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.84x