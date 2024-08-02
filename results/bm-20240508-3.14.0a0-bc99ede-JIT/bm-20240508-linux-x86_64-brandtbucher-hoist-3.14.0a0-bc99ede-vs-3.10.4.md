# Results vs. 3.10.4

- fork: brandtbucher
- ref: hoist
- machine: linux-x86_64
- commit hash: bc99ede
- commit date: 2024-05-08
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 279 ms: 1.25x faster                                         |
| chameleon      | 9.68 ms                                                | 7.07 ms: 1.37x faster                                        |
| docutils       | 3.30 sec                                               | 2.96 sec: 1.11x faster                                       |
| html5lib       | 88.9 ms                                                | 69.7 ms: 1.28x faster                                        |
| tornado_http   | 136 ms                                                 | 97.4 ms: 1.40x faster                                        |
| Geometric mean | (ref)                                                  | 1.28x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 364 ms: 2.00x faster                                         |
| async_tree_io           | 1.77 sec                                               | 932 ms: 1.90x faster                                         |
| async_tree_memoization  | 870 ms                                                 | 478 ms: 1.82x faster                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 617 ms: 1.65x faster                                         |
| Geometric mean          | (ref)                                                  | 1.84x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.0 ms: 1.79x faster                                        |
| float          | 117 ms                                                 | 70.8 ms: 1.65x faster                                        |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                  | 1.44x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 140 ms: 1.34x faster                                         |
| regex_v8       | 27.8 ms                                                | 24.6 ms: 1.13x faster                                        |
| regex_dna      | 227 ms                                                 | 221 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                  | 1.11x faster                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.99 sec: 1.58x faster                                       |
| pickle_pure_python   | 484 us                                                 | 308 us: 1.57x faster                                         |
| unpickle_pure_python | 331 us                                                 | 221 us: 1.50x faster                                         |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                        |
| xml_etree_process    | 79.1 ms                                                | 57.9 ms: 1.37x faster                                        |
| xml_etree_generate   | 99.4 ms                                                | 82.5 ms: 1.20x faster                                        |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.13x faster                                         |
| xml_etree_parse      | 168 ms                                                 | 153 ms: 1.10x faster                                         |
| json_loads           | 31.2 us                                                | 29.0 us: 1.08x faster                                        |
| pickle_list          | 5.08 us                                                | 5.14 us: 1.01x slower                                        |
| unpickle_list        | 5.20 us                                                | 5.40 us: 1.04x slower                                        |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                        |
| unpickle             | 14.4 us                                                | 16.2 us: 1.13x slower                                        |
| pickle_dict          | 29.6 us                                                | 33.9 us: 1.15x slower                                        |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.1 ms: 1.31x faster                                        |
| python_startup_no_site | 5.93 ms                                                | 7.67 ms: 1.29x slower                                        |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.52 ms: 1.72x faster                                        |
| django_template | 48.2 ms                                                | 36.0 ms: 1.34x faster                                        |
| genshi_text     | 31.8 ms                                                | 24.7 ms: 1.29x faster                                        |
| genshi_xml      | 66.0 ms                                                | 58.5 ms: 1.13x faster                                        |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 177 us: 3.07x faster                                         |
| generators               | 80.1 ms                                                | 29.7 ms: 2.69x faster                                        |
| deltablue                | 7.91 ms                                                | 3.73 ms: 2.12x faster                                        |
| async_tree_none          | 728 ms                                                 | 364 ms: 2.00x faster                                         |
| chaos                    | 115 ms                                                 | 59.0 ms: 1.96x faster                                        |
| richards_super           | 94.7 ms                                                | 48.8 ms: 1.94x faster                                        |
| async_tree_io            | 1.77 sec                                               | 932 ms: 1.90x faster                                         |
| richards                 | 79.3 ms                                                | 42.7 ms: 1.86x faster                                        |
| crypto_pyaes             | 128 ms                                                 | 69.1 ms: 1.85x faster                                        |
| scimark_monte_carlo      | 118 ms                                                 | 64.1 ms: 1.84x faster                                        |
| async_tree_memoization   | 870 ms                                                 | 478 ms: 1.82x faster                                         |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                         |
| asyncio_tcp              | 922 ms                                                 | 515 ms: 1.79x faster                                         |
| raytrace                 | 507 ms                                                 | 283 ms: 1.79x faster                                         |
| nbody                    | 154 ms                                                 | 86.0 ms: 1.79x faster                                        |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.74x faster                                        |
| spectral_norm            | 170 ms                                                 | 99.0 ms: 1.72x faster                                        |
| mako                     | 16.3 ms                                                | 9.52 ms: 1.72x faster                                        |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                         |
| float                    | 117 ms                                                 | 70.8 ms: 1.65x faster                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.65x faster                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 617 ms: 1.65x faster                                         |
| go                       | 240 ms                                                 | 147 ms: 1.63x faster                                         |
| pyflate                  | 716 ms                                                 | 449 ms: 1.60x faster                                         |
| tomli_loads              | 3.14 sec                                               | 1.99 sec: 1.58x faster                                       |
| pickle_pure_python       | 484 us                                                 | 308 us: 1.57x faster                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                        |
| deepcopy_memo            | 58.5 us                                                | 37.7 us: 1.55x faster                                        |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                        |
| hexiom                   | 10.4 ms                                                | 6.73 ms: 1.54x faster                                        |
| pylint                   | 551 ms                                                 | 357 ms: 1.54x faster                                         |
| unpickle_pure_python     | 331 us                                                 | 221 us: 1.50x faster                                         |
| scimark_fft              | 466 ms                                                 | 321 ms: 1.45x faster                                         |
| logging_simple           | 8.30 us                                                | 5.72 us: 1.45x faster                                        |
| fannkuch                 | 532 ms                                                 | 368 ms: 1.45x faster                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.55 ms: 1.42x faster                                        |
| logging_format           | 9.09 us                                                | 6.41 us: 1.42x faster                                        |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.40x faster                                         |
| tornado_http             | 136 ms                                                 | 97.4 ms: 1.40x faster                                        |
| pprint_safe_repr         | 1.02 sec                                               | 727 ms: 1.40x faster                                         |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                       |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                       |
| chameleon                | 9.68 ms                                                | 7.07 ms: 1.37x faster                                        |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                        |
| xml_etree_process        | 79.1 ms                                                | 57.9 ms: 1.37x faster                                        |
| regex_compile            | 188 ms                                                 | 140 ms: 1.34x faster                                         |
| django_template          | 48.2 ms                                                | 36.0 ms: 1.34x faster                                        |
| thrift                   | 1.07 ms                                                | 809 us: 1.32x faster                                         |
| python_startup           | 14.6 ms                                                | 11.1 ms: 1.31x faster                                        |
| genshi_text              | 31.8 ms                                                | 24.7 ms: 1.29x faster                                        |
| html5lib                 | 88.9 ms                                                | 69.7 ms: 1.28x faster                                        |
| deepcopy                 | 479 us                                                 | 378 us: 1.27x faster                                         |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                         |
| deepcopy_reduce          | 4.17 us                                                | 3.31 us: 1.26x faster                                        |
| 2to3                     | 348 ms                                                 | 279 ms: 1.25x faster                                         |
| sqlglot_optimize         | 69.2 ms                                                | 57.1 ms: 1.21x faster                                        |
| nqueens                  | 106 ms                                                 | 87.8 ms: 1.21x faster                                        |
| xml_etree_generate       | 99.4 ms                                                | 82.5 ms: 1.20x faster                                        |
| dulwich_log              | 84.3 ms                                                | 70.1 ms: 1.20x faster                                        |
| dask                     | 441 ms                                                 | 379 ms: 1.16x faster                                         |
| pathlib                  | 20.5 ms                                                | 17.8 ms: 1.15x faster                                        |
| aiohttp                  | 1.44 ms                                                | 1.26 ms: 1.14x faster                                        |
| sympy_str                | 346 ms                                                 | 304 ms: 1.14x faster                                         |
| bench_thread_pool        | 986 us                                                 | 868 us: 1.14x faster                                         |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                        |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.13x faster                                         |
| gunicorn                 | 1.53 ms                                                | 1.35 ms: 1.13x faster                                        |
| genshi_xml               | 66.0 ms                                                | 58.5 ms: 1.13x faster                                        |
| sympy_sum                | 196 ms                                                 | 174 ms: 1.13x faster                                         |
| regex_v8                 | 27.8 ms                                                | 24.6 ms: 1.13x faster                                        |
| docutils                 | 3.30 sec                                               | 2.96 sec: 1.11x faster                                       |
| sympy_expand             | 566 ms                                                 | 511 ms: 1.11x faster                                         |
| xml_etree_parse          | 168 ms                                                 | 153 ms: 1.10x faster                                         |
| mdp                      | 2.85 sec                                               | 2.61 sec: 1.09x faster                                       |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                         |
| json_loads               | 31.2 us                                                | 29.0 us: 1.08x faster                                        |
| json                     | 5.69 ms                                                | 5.34 ms: 1.07x faster                                        |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.06x faster                                        |
| regex_dna                | 227 ms                                                 | 221 ms: 1.02x faster                                         |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                         |
| pickle_list              | 5.08 us                                                | 5.14 us: 1.01x slower                                        |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.02x slower                                         |
| unpickle_list            | 5.20 us                                                | 5.40 us: 1.04x slower                                        |
| async_generators         | 444 ms                                                 | 465 ms: 1.05x slower                                         |
| gc_traversal             | 3.62 ms                                                | 3.84 ms: 1.06x slower                                        |
| flaskblogging            | 8.58 ms                                                | 9.23 ms: 1.08x slower                                        |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                        |
| create_gc_cycles         | 1.62 ms                                                | 1.81 ms: 1.12x slower                                        |
| coverage                 | 79.4 ms                                                | 88.7 ms: 1.12x slower                                        |
| unpickle                 | 14.4 us                                                | 16.2 us: 1.13x slower                                        |
| pickle_dict              | 29.6 us                                                | 33.9 us: 1.15x slower                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.67 ms: 1.29x slower                                        |
| telco                    | 7.27 ms                                                | 171 ms: 23.59x slower                                        |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                 |

Benchmark hidden because not significant (2): bench_mp_pool, regex_effbot
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: djangocms, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240508-3.14.0a0-bc99ede-JIT/bm-20240508-linux-x86_64-brandtbucher-hoist-3.14.0a0-bc99ede.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.21x