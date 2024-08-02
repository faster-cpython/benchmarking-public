# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_recompile
- machine: linux-x86_64
- commit hash: 0cc257c
- commit date: 2024-05-08
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 302 ms: 1.15x faster                                                    |
| chameleon      | 9.68 ms                                                | 7.11 ms: 1.36x faster                                                   |
| docutils       | 3.30 sec                                               | 3.83 sec: 1.16x slower                                                  |
| html5lib       | 88.9 ms                                                | 75.0 ms: 1.18x faster                                                   |
| tornado_http   | 136 ms                                                 | 99.4 ms: 1.37x faster                                                   |
| Geometric mean | (ref)                                                  | 1.17x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 1.18 sec: 1.50x faster                                                  |
| async_tree_none         | 728 ms                                                 | 489 ms: 1.49x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 618 ms: 1.41x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 754 ms: 1.35x faster                                                    |
| Geometric mean          | (ref)                                                  | 1.44x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.0 ms: 1.90x faster                                                   |
| float          | 117 ms                                                 | 89.8 ms: 1.30x faster                                                   |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.36x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 140 ms: 1.35x faster                                                    |
| regex_v8       | 27.8 ms                                                | 25.8 ms: 1.08x faster                                                   |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.85 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 307 us: 1.58x faster                                                    |
| tomli_loads          | 3.14 sec                                               | 2.02 sec: 1.56x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 224 us: 1.48x faster                                                    |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 66.2 ms: 1.20x faster                                                   |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 93.2 ms: 1.07x faster                                                   |
| unpickle_list        | 5.20 us                                                | 5.26 us: 1.01x slower                                                   |
| xml_etree_parse      | 168 ms                                                 | 174 ms: 1.04x slower                                                    |
| unpickle             | 14.4 us                                                | 15.2 us: 1.06x slower                                                   |
| pickle_list          | 5.08 us                                                | 5.46 us: 1.07x slower                                                   |
| pickle               | 10.7 us                                                | 12.0 us: 1.13x slower                                                   |
| pickle_dict          | 29.6 us                                                | 34.2 us: 1.15x slower                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 140 ms: 1.21x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.1 ms: 1.31x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.68 ms: 1.29x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.72 ms: 1.68x faster                                                   |
| django_template | 48.2 ms                                                | 36.4 ms: 1.32x faster                                                   |
| genshi_text     | 31.8 ms                                                | 25.2 ms: 1.26x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 61.3 ms: 1.08x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 175 us: 3.11x faster                                                    |
| generators               | 80.1 ms                                                | 29.9 ms: 2.68x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.99 ms: 1.98x faster                                                   |
| chaos                    | 115 ms                                                 | 58.8 ms: 1.96x faster                                                   |
| nbody                    | 154 ms                                                 | 81.0 ms: 1.90x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 67.6 ms: 1.89x faster                                                   |
| richards_super           | 94.7 ms                                                | 50.5 ms: 1.88x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 64.1 ms: 1.84x faster                                                   |
| raytrace                 | 507 ms                                                 | 280 ms: 1.81x faster                                                    |
| richards                 | 79.3 ms                                                | 44.0 ms: 1.80x faster                                                   |
| asyncio_tcp              | 922 ms                                                 | 515 ms: 1.79x faster                                                    |
| logging_silent           | 190 ns                                                 | 107 ns: 1.77x faster                                                    |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                   |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                                    |
| mako                     | 16.3 ms                                                | 9.72 ms: 1.68x faster                                                   |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.67x faster                                                    |
| pyflate                  | 716 ms                                                 | 444 ms: 1.61x faster                                                    |
| go                       | 240 ms                                                 | 151 ms: 1.59x faster                                                    |
| hexiom                   | 10.4 ms                                                | 6.58 ms: 1.58x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 307 us: 1.58x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 2.02 sec: 1.56x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.40 ms: 1.55x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 37.7 us: 1.55x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.52x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 1.18 sec: 1.50x faster                                                  |
| async_tree_none          | 728 ms                                                 | 489 ms: 1.49x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.74 ms: 1.48x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 224 us: 1.48x faster                                                    |
| scimark_fft              | 466 ms                                                 | 318 ms: 1.47x faster                                                    |
| fannkuch                 | 532 ms                                                 | 363 ms: 1.46x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.77 us: 1.44x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 714 ms: 1.43x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.54 ms: 1.43x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                  |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.41x faster                                                    |
| logging_format           | 9.09 us                                                | 6.45 us: 1.41x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 618 ms: 1.41x faster                                                    |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                                  |
| tornado_http             | 136 ms                                                 | 99.4 ms: 1.37x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                   |
| chameleon                | 9.68 ms                                                | 7.11 ms: 1.36x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 754 ms: 1.35x faster                                                    |
| regex_compile            | 188 ms                                                 | 140 ms: 1.35x faster                                                    |
| pylint                   | 551 ms                                                 | 415 ms: 1.33x faster                                                    |
| django_template          | 48.2 ms                                                | 36.4 ms: 1.32x faster                                                   |
| thrift                   | 1.07 ms                                                | 814 us: 1.32x faster                                                    |
| python_startup           | 14.6 ms                                                | 11.1 ms: 1.31x faster                                                   |
| float                    | 117 ms                                                 | 89.8 ms: 1.30x faster                                                   |
| deepcopy                 | 479 us                                                 | 374 us: 1.28x faster                                                    |
| genshi_text              | 31.8 ms                                                | 25.2 ms: 1.26x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.26 sec: 1.25x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 115 ms: 1.24x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 3.39 us: 1.23x faster                                                   |
| nqueens                  | 106 ms                                                 | 86.6 ms: 1.22x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 69.4 ms: 1.21x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 66.2 ms: 1.20x faster                                                   |
| html5lib                 | 88.9 ms                                                | 75.0 ms: 1.18x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 58.8 ms: 1.18x faster                                                   |
| 2to3                     | 348 ms                                                 | 302 ms: 1.15x faster                                                    |
| pathlib                  | 20.5 ms                                                | 17.9 ms: 1.14x faster                                                   |
| sympy_str                | 346 ms                                                 | 304 ms: 1.14x faster                                                    |
| sympy_sum                | 196 ms                                                 | 173 ms: 1.13x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 871 us: 1.13x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                                   |
| aiohttp                  | 1.44 ms                                                | 1.28 ms: 1.12x faster                                                   |
| gunicorn                 | 1.53 ms                                                | 1.38 ms: 1.11x faster                                                   |
| sympy_expand             | 566 ms                                                 | 513 ms: 1.10x faster                                                    |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.09x faster                                                    |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 61.3 ms: 1.08x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 25.8 ms: 1.08x faster                                                   |
| json                     | 5.69 ms                                                | 5.30 ms: 1.07x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 93.2 ms: 1.07x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.80 sec: 1.02x faster                                                  |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                    |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 564 ms: 1.01x slower                                                    |
| unpickle_list            | 5.20 us                                                | 5.26 us: 1.01x slower                                                   |
| dask                     | 441 ms                                                 | 449 ms: 1.02x slower                                                    |
| xml_etree_parse          | 168 ms                                                 | 174 ms: 1.04x slower                                                    |
| unpickle                 | 14.4 us                                                | 15.2 us: 1.06x slower                                                   |
| regex_effbot             | 3.63 ms                                                | 3.85 ms: 1.06x slower                                                   |
| pickle_list              | 5.08 us                                                | 5.46 us: 1.07x slower                                                   |
| async_generators         | 444 ms                                                 | 488 ms: 1.10x slower                                                    |
| pickle                   | 10.7 us                                                | 12.0 us: 1.13x slower                                                   |
| coverage                 | 79.4 ms                                                | 89.6 ms: 1.13x slower                                                   |
| pickle_dict              | 29.6 us                                                | 34.2 us: 1.15x slower                                                   |
| docutils                 | 3.30 sec                                               | 3.83 sec: 1.16x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.32 ms: 1.19x slower                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 140 ms: 1.21x slower                                                    |
| flaskblogging            | 8.58 ms                                                | 10.4 ms: 1.22x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.68 ms: 1.29x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 2.23 ms: 1.37x slower                                                   |
| telco                    | 7.27 ms                                                | 170 ms: 23.45x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.24x faster                                                            |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: djangocms, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240508-3.14.0a0-0cc257c-JIT/bm-20240508-linux-x86_64-brandtbucher-justin_recompile-3.14.0a0-0cc257c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.21x