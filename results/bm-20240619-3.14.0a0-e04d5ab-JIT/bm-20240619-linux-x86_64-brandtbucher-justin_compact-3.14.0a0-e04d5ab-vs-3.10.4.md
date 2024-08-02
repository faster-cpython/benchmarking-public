# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_compact
- machine: linux-x86_64
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 281 ms: 1.24x faster                                                  |
| docutils       | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                |
| html5lib       | 88.9 ms                                                | 67.2 ms: 1.32x faster                                                 |
| tornado_http   | 136 ms                                                 | 96.3 ms: 1.42x faster                                                 |
| Geometric mean | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 374 ms: 1.95x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 957 ms: 1.85x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 493 ms: 1.76x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 626 ms: 1.62x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.79x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.8 ms: 1.90x faster                                                 |
| float          | 117 ms                                                 | 71.8 ms: 1.63x faster                                                 |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.47x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 136 ms: 1.38x faster                                                  |
| regex_v8       | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                 |
| regex_dna      | 227 ms                                                 | 230 ms: 1.01x slower                                                  |
| regex_effbot   | 3.63 ms                                                | 3.71 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 301 us: 1.61x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.59x faster                                                |
| unpickle_pure_python | 331 us                                                 | 224 us: 1.47x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 58.3 ms: 1.36x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 82.3 ms: 1.21x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.13x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                  |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                                 |
| pickle_list          | 5.08 us                                                | 5.12 us: 1.01x slower                                                 |
| unpickle_list        | 5.20 us                                                | 5.37 us: 1.03x slower                                                 |
| unpickle             | 14.4 us                                                | 15.0 us: 1.04x slower                                                 |
| pickle               | 10.7 us                                                | 12.2 us: 1.15x slower                                                 |
| pickle_dict          | 29.6 us                                                | 35.6 us: 1.20x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.1 ms: 1.31x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.63 ms: 1.29x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                 |
| django_template | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                 |
| genshi_text     | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 56.3 ms: 1.17x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.18x faster                                                  |
| generators               | 80.1 ms                                                | 30.0 ms: 2.67x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.69 ms: 2.14x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 28.8 us: 2.03x faster                                                 |
| async_tree_none          | 728 ms                                                 | 374 ms: 1.95x faster                                                  |
| chaos                    | 115 ms                                                 | 59.4 ms: 1.94x faster                                                 |
| richards_super           | 94.7 ms                                                | 49.4 ms: 1.92x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 67.1 ms: 1.91x faster                                                 |
| nbody                    | 154 ms                                                 | 80.8 ms: 1.90x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 62.3 ms: 1.90x faster                                                 |
| richards                 | 79.3 ms                                                | 42.8 ms: 1.85x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 957 ms: 1.85x faster                                                  |
| raytrace                 | 507 ms                                                 | 279 ms: 1.82x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 516 ms: 1.79x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 493 ms: 1.76x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                 |
| deepcopy                 | 479 us                                                 | 277 us: 1.73x faster                                                  |
| logging_silent           | 190 ns                                                 | 110 ns: 1.72x faster                                                  |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                                  |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.67x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.65x faster                                                 |
| float                    | 117 ms                                                 | 71.8 ms: 1.63x faster                                                 |
| mako                     | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 626 ms: 1.62x faster                                                  |
| go                       | 240 ms                                                 | 149 ms: 1.61x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 301 us: 1.61x faster                                                  |
| pyflate                  | 716 ms                                                 | 445 ms: 1.61x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.59x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                                 |
| pylint                   | 551 ms                                                 | 353 ms: 1.56x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.68 ms: 1.56x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.77 us: 1.50x faster                                                 |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                                  |
| fannkuch                 | 532 ms                                                 | 356 ms: 1.50x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.57 us: 1.49x faster                                                 |
| logging_format           | 9.09 us                                                | 6.17 us: 1.47x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 224 us: 1.47x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.43 ms: 1.46x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                |
| tornado_http             | 136 ms                                                 | 96.3 ms: 1.42x faster                                                 |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.41x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 722 ms: 1.41x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.39x faster                                                |
| regex_compile            | 188 ms                                                 | 136 ms: 1.38x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 58.3 ms: 1.36x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                 |
| django_template          | 48.2 ms                                                | 36.2 ms: 1.33x faster                                                 |
| html5lib                 | 88.9 ms                                                | 67.2 ms: 1.32x faster                                                 |
| python_startup           | 14.6 ms                                                | 11.1 ms: 1.31x faster                                                 |
| thrift                   | 1.07 ms                                                | 833 us: 1.29x faster                                                  |
| genshi_text              | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.25x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 115 ms: 1.25x faster                                                  |
| 2to3                     | 348 ms                                                 | 281 ms: 1.24x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 69.1 ms: 1.22x faster                                                 |
| nqueens                  | 106 ms                                                 | 86.8 ms: 1.22x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 57.2 ms: 1.21x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 82.3 ms: 1.21x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 56.3 ms: 1.17x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 23.8 ms: 1.17x faster                                                 |
| dask                     | 441 ms                                                 | 379 ms: 1.16x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 854 us: 1.15x faster                                                  |
| sympy_str                | 346 ms                                                 | 301 ms: 1.15x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 22.6 ms: 1.14x faster                                                 |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.14x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.13x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                |
| sympy_expand             | 566 ms                                                 | 508 ms: 1.11x faster                                                  |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                  |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                                 |
| json                     | 5.69 ms                                                | 5.40 ms: 1.05x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.89 us: 1.05x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.77 sec: 1.03x faster                                                |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                  |
| pickle_list              | 5.08 us                                                | 5.12 us: 1.01x slower                                                 |
| regex_dna                | 227 ms                                                 | 230 ms: 1.01x slower                                                  |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.01x slower                                                  |
| regex_effbot             | 3.63 ms                                                | 3.71 ms: 1.02x slower                                                 |
| unpickle_list            | 5.20 us                                                | 5.37 us: 1.03x slower                                                 |
| unpickle                 | 14.4 us                                                | 15.0 us: 1.04x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 3.82 ms: 1.05x slower                                                 |
| async_generators         | 444 ms                                                 | 471 ms: 1.06x slower                                                  |
| telco                    | 7.27 ms                                                | 8.03 ms: 1.11x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.80 ms: 1.11x slower                                                 |
| pickle                   | 10.7 us                                                | 12.2 us: 1.15x slower                                                 |
| coverage                 | 79.4 ms                                                | 95.3 ms: 1.20x slower                                                 |
| pickle_dict              | 29.6 us                                                | 35.6 us: 1.20x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.63 ms: 1.29x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240619-3.14.0a0-e04d5ab-JIT/bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.21x