# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: fewer_set_ip
- machine: linux-x86_64
- commit hash: 3d98d27
- commit date: 2024-09-17
- overall geometric mean: 1.431x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 275 ms: 1.27x faster                                                    |
| docutils       | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                  |
| html5lib       | 88.9 ms                                                | 65.6 ms: 1.36x faster                                                   |
| tornado_http   | 136 ms                                                 | 94.8 ms: 1.44x faster                                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 317 ms: 2.30x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 398 ms: 2.19x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 863 ms: 2.05x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 566 ms: 1.80x faster                                                    |
| Geometric mean          | (ref)                                                  | 2.07x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.1 ms: 1.87x faster                                                   |
| float          | 117 ms                                                 | 69.1 ms: 1.70x faster                                                   |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.48x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 141 ms: 1.34x faster                                                    |
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                   |
| regex_dna      | 227 ms                                                 | 228 ms: 1.01x slower                                                    |
| regex_effbot   | 3.63 ms                                                | 4.01 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.90 sec: 1.66x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 307 us: 1.58x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 53.9 ms: 1.47x faster                                                   |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 77.5 ms: 1.28x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 97.8 ms: 1.18x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 144 ms: 1.17x faster                                                    |
| json_loads           | 31.2 us                                                | 27.0 us: 1.16x faster                                                   |
| pickle_list          | 5.08 us                                                | 5.02 us: 1.01x faster                                                   |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                                   |
| pickle_dict          | 29.6 us                                                | 33.0 us: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.21x faster                                                            |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.80 ms: 1.67x faster                                                   |
| django_template | 48.2 ms                                                | 35.2 ms: 1.37x faster                                                   |
| genshi_text     | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 57.3 ms: 1.15x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.39x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.21 ms: 2.47x faster                                                   |
| generators               | 80.1 ms                                                | 33.3 ms: 2.41x faster                                                   |
| async_tree_none          | 728 ms                                                 | 317 ms: 2.30x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 26.7 us: 2.19x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 398 ms: 2.19x faster                                                    |
| richards_super           | 94.7 ms                                                | 45.0 ms: 2.11x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 863 ms: 2.05x faster                                                    |
| richards                 | 79.3 ms                                                | 39.5 ms: 2.01x faster                                                   |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 65.4 ms: 1.96x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 61.9 ms: 1.91x faster                                                   |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                    |
| nbody                    | 154 ms                                                 | 82.1 ms: 1.87x faster                                                   |
| logging_silent           | 190 ns                                                 | 101 ns: 1.87x faster                                                    |
| asyncio_tcp              | 922 ms                                                 | 500 ms: 1.84x faster                                                    |
| go                       | 240 ms                                                 | 131 ms: 1.83x faster                                                    |
| raytrace                 | 507 ms                                                 | 277 ms: 1.83x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 566 ms: 1.80x faster                                                    |
| deepcopy                 | 479 us                                                 | 267 us: 1.80x faster                                                    |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.75x faster                                                   |
| float                    | 117 ms                                                 | 69.1 ms: 1.70x faster                                                   |
| mako                     | 16.3 ms                                                | 9.80 ms: 1.67x faster                                                   |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 1.90 sec: 1.66x faster                                                  |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.62x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.35 ms: 1.61x faster                                                   |
| pyflate                  | 716 ms                                                 | 448 ms: 1.60x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.63 us: 1.59x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 307 us: 1.58x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.14 ms: 1.56x faster                                                   |
| scimark_fft              | 466 ms                                                 | 301 ms: 1.55x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.52x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.84 ms: 1.52x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.50x faster                                                   |
| logging_format           | 9.09 us                                                | 6.05 us: 1.50x faster                                                   |
| pylint                   | 551 ms                                                 | 371 ms: 1.49x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 53.9 ms: 1.47x faster                                                   |
| fannkuch                 | 532 ms                                                 | 369 ms: 1.44x faster                                                    |
| tornado_http             | 136 ms                                                 | 94.8 ms: 1.44x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 743 ms: 1.37x faster                                                    |
| django_template          | 48.2 ms                                                | 35.2 ms: 1.37x faster                                                   |
| thrift                   | 1.07 ms                                                | 783 us: 1.37x faster                                                    |
| html5lib                 | 88.9 ms                                                | 65.6 ms: 1.36x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                                  |
| regex_compile            | 188 ms                                                 | 141 ms: 1.34x faster                                                    |
| genshi_text              | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                   |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 77.5 ms: 1.28x faster                                                   |
| 2to3                     | 348 ms                                                 | 275 ms: 1.27x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                                    |
| nqueens                  | 106 ms                                                 | 85.0 ms: 1.24x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 67.8 ms: 1.24x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 57.9 ms: 1.19x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 97.8 ms: 1.18x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 836 us: 1.18x faster                                                    |
| sympy_str                | 346 ms                                                 | 295 ms: 1.17x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 144 ms: 1.17x faster                                                    |
| json_loads               | 31.2 us                                                | 27.0 us: 1.16x faster                                                   |
| sympy_sum                | 196 ms                                                 | 170 ms: 1.15x faster                                                    |
| genshi_xml               | 66.0 ms                                                | 57.3 ms: 1.15x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 22.6 ms: 1.14x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.13x faster                                                   |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.13x faster                                                    |
| sympy_expand             | 566 ms                                                 | 499 ms: 1.13x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                  |
| json                     | 5.69 ms                                                | 5.12 ms: 1.11x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.07x faster                                                   |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                    |
| pickle_list              | 5.08 us                                                | 5.02 us: 1.01x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                    |
| regex_dna                | 227 ms                                                 | 228 ms: 1.01x slower                                                    |
| async_generators         | 444 ms                                                 | 453 ms: 1.02x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 3.74 ms: 1.03x slower                                                   |
| coverage                 | 79.4 ms                                                | 85.0 ms: 1.07x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                   |
| telco                    | 7.27 ms                                                | 7.91 ms: 1.09x slower                                                   |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                                   |
| regex_effbot             | 3.63 ms                                                | 4.01 ms: 1.10x slower                                                   |
| pickle_dict              | 29.6 us                                                | 33.0 us: 1.12x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                   |
| unpack_sequence          | 60.0 ns                                                | 113 ns: 1.88x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                            |

Benchmark hidden because not significant (3): unpickle_list, bench_mp_pool, unpickle
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240917-3.14.0a0-3d98d27-JIT/bm-20240917-linux-x86_64-Fidget%2dSpinner-fewer_set_ip-3.14.0a0-3d98d27.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.431x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.21x