# Results vs. 3.10.4

- fork: brandtbucher
- ref: hoist_partial
- machine: linux-x86_64
- commit hash: 1ce3b25
- commit date: 2024-05-09
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 280 ms: 1.24x faster                                                 |
| chameleon      | 9.68 ms                                                | 7.17 ms: 1.35x faster                                                |
| docutils       | 3.30 sec                                               | 2.98 sec: 1.11x faster                                               |
| html5lib       | 88.9 ms                                                | 69.1 ms: 1.29x faster                                                |
| tornado_http   | 136 ms                                                 | 98.1 ms: 1.39x faster                                                |
| Geometric mean | (ref)                                                  | 1.27x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 363 ms: 2.00x faster                                                 |
| async_tree_io           | 1.77 sec                                               | 933 ms: 1.90x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 477 ms: 1.82x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 618 ms: 1.64x faster                                                 |
| Geometric mean          | (ref)                                                  | 1.84x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.1 ms: 1.78x faster                                                |
| float          | 117 ms                                                 | 70.6 ms: 1.66x faster                                                |
| pidigits       | 191 ms                                                 | 197 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.42x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 139 ms: 1.35x faster                                                 |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                |
| Geometric mean | (ref)                                                  | 1.11x faster                                                         |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                               |
| pickle_pure_python   | 484 us                                                 | 304 us: 1.59x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 58.2 ms: 1.36x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 83.6 ms: 1.19x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.13x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 152 ms: 1.11x faster                                                 |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                                |
| unpickle_list        | 5.20 us                                                | 5.27 us: 1.01x slower                                                |
| pickle_list          | 5.08 us                                                | 5.29 us: 1.04x slower                                                |
| unpickle             | 14.4 us                                                | 15.9 us: 1.11x slower                                                |
| pickle_dict          | 29.6 us                                                | 33.1 us: 1.12x slower                                                |
| pickle               | 10.7 us                                                | 12.0 us: 1.13x slower                                                |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.1 ms: 1.31x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 7.70 ms: 1.30x slower                                                |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.62 ms: 1.70x faster                                                |
| django_template | 48.2 ms                                                | 36.5 ms: 1.32x faster                                                |
| genshi_text     | 31.8 ms                                                | 25.3 ms: 1.26x faster                                                |
| genshi_xml      | 66.0 ms                                                | 58.7 ms: 1.13x faster                                                |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 176 us: 3.09x faster                                                 |
| generators               | 80.1 ms                                                | 30.2 ms: 2.65x faster                                                |
| deltablue                | 7.91 ms                                                | 3.75 ms: 2.11x faster                                                |
| async_tree_none          | 728 ms                                                 | 363 ms: 2.00x faster                                                 |
| chaos                    | 115 ms                                                 | 58.8 ms: 1.96x faster                                                |
| richards_super           | 94.7 ms                                                | 49.1 ms: 1.93x faster                                                |
| async_tree_io            | 1.77 sec                                               | 933 ms: 1.90x faster                                                 |
| richards                 | 79.3 ms                                                | 42.7 ms: 1.86x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 64.1 ms: 1.84x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 69.6 ms: 1.84x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 477 ms: 1.82x faster                                                 |
| raytrace                 | 507 ms                                                 | 284 ms: 1.79x faster                                                 |
| nbody                    | 154 ms                                                 | 86.1 ms: 1.78x faster                                                |
| asyncio_tcp              | 922 ms                                                 | 519 ms: 1.78x faster                                                 |
| logging_silent           | 190 ns                                                 | 107 ns: 1.77x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                                |
| mako                     | 16.3 ms                                                | 9.62 ms: 1.70x faster                                                |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                 |
| scimark_sor              | 220 ms                                                 | 132 ms: 1.67x faster                                                 |
| float                    | 117 ms                                                 | 70.6 ms: 1.66x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.65x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 618 ms: 1.64x faster                                                 |
| go                       | 240 ms                                                 | 148 ms: 1.63x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                               |
| pyflate                  | 716 ms                                                 | 449 ms: 1.60x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.59x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 37.5 us: 1.56x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.69 ms: 1.55x faster                                                |
| pylint                   | 551 ms                                                 | 357 ms: 1.54x faster                                                 |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                 |
| scimark_fft              | 466 ms                                                 | 321 ms: 1.45x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.47 ms: 1.45x faster                                                |
| fannkuch                 | 532 ms                                                 | 368 ms: 1.45x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.77 us: 1.44x faster                                                |
| logging_format           | 9.09 us                                                | 6.40 us: 1.42x faster                                                |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.41x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 724 ms: 1.41x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.41x faster                                               |
| tornado_http             | 136 ms                                                 | 98.1 ms: 1.39x faster                                                |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                               |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 58.2 ms: 1.36x faster                                                |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.35x faster                                               |
| regex_compile            | 188 ms                                                 | 139 ms: 1.35x faster                                                 |
| chameleon                | 9.68 ms                                                | 7.17 ms: 1.35x faster                                                |
| thrift                   | 1.07 ms                                                | 810 us: 1.32x faster                                                 |
| django_template          | 48.2 ms                                                | 36.5 ms: 1.32x faster                                                |
| python_startup           | 14.6 ms                                                | 11.1 ms: 1.31x faster                                                |
| html5lib                 | 88.9 ms                                                | 69.1 ms: 1.29x faster                                                |
| genshi_text              | 31.8 ms                                                | 25.3 ms: 1.26x faster                                                |
| deepcopy                 | 479 us                                                 | 383 us: 1.25x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 3.34 us: 1.25x faster                                                |
| 2to3                     | 348 ms                                                 | 280 ms: 1.24x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 57.1 ms: 1.21x faster                                                |
| nqueens                  | 106 ms                                                 | 87.7 ms: 1.21x faster                                                |
| dulwich_log              | 84.3 ms                                                | 70.4 ms: 1.20x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 83.6 ms: 1.19x faster                                                |
| dask                     | 441 ms                                                 | 379 ms: 1.16x faster                                                 |
| sympy_str                | 346 ms                                                 | 302 ms: 1.14x faster                                                 |
| pathlib                  | 20.5 ms                                                | 17.9 ms: 1.14x faster                                                |
| aiohttp                  | 1.44 ms                                                | 1.26 ms: 1.14x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.13x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                                |
| bench_thread_pool        | 986 us                                                 | 871 us: 1.13x faster                                                 |
| gunicorn                 | 1.53 ms                                                | 1.35 ms: 1.13x faster                                                |
| sympy_sum                | 196 ms                                                 | 174 ms: 1.13x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 58.7 ms: 1.13x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 152 ms: 1.11x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                |
| sympy_expand             | 566 ms                                                 | 512 ms: 1.11x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.98 sec: 1.11x faster                                               |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                                 |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                                |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                                |
| mdp                      | 2.85 sec                                               | 2.73 sec: 1.04x faster                                               |
| unpickle_list            | 5.20 us                                                | 5.27 us: 1.01x slower                                                |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.01x slower                                                 |
| pidigits                 | 191 ms                                                 | 197 ms: 1.03x slower                                                 |
| pickle_list              | 5.08 us                                                | 5.29 us: 1.04x slower                                                |
| async_generators         | 444 ms                                                 | 468 ms: 1.05x slower                                                 |
| flaskblogging            | 8.58 ms                                                | 9.37 ms: 1.09x slower                                                |
| unpickle                 | 14.4 us                                                | 15.9 us: 1.11x slower                                                |
| coverage                 | 79.4 ms                                                | 88.2 ms: 1.11x slower                                                |
| pickle_dict              | 29.6 us                                                | 33.1 us: 1.12x slower                                                |
| pickle                   | 10.7 us                                                | 12.0 us: 1.13x slower                                                |
| gc_traversal             | 3.62 ms                                                | 4.11 ms: 1.13x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 1.84 ms: 1.14x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 7.70 ms: 1.30x slower                                                |
| telco                    | 7.27 ms                                                | 172 ms: 23.65x slower                                                |
| Geometric mean           | (ref)                                                  | 1.28x faster                                                         |

Benchmark hidden because not significant (3): regex_effbot, regex_dna, bench_mp_pool
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: djangocms, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240509-3.14.0a0-1ce3b25-JIT/bm-20240509-linux-x86_64-brandtbucher-hoist_partial-3.14.0a0-1ce3b25.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.21x