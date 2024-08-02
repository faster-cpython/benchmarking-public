# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 270 ms: 1.29x faster                                       |
| chameleon      | 9.68 ms                                                | 6.87 ms: 1.41x faster                                      |
| docutils       | 3.30 sec                                               | 2.68 sec: 1.23x faster                                     |
| html5lib       | 88.9 ms                                                | 67.9 ms: 1.31x faster                                      |
| tornado_http   | 136 ms                                                 | 96.8 ms: 1.41x faster                                      |
| Geometric mean | (ref)                                                  | 1.33x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 446 ms: 1.63x faster                                       |
| async_tree_memoization  | 870 ms                                                 | 574 ms: 1.52x faster                                       |
| async_tree_io           | 1.77 sec                                               | 1.21 sec: 1.46x faster                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 724 ms: 1.40x faster                                       |
| Geometric mean          | (ref)                                                  | 1.50x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 154 ms                                                 | 89.5 ms: 1.72x faster                                      |
| float          | 117 ms                                                 | 82.0 ms: 1.43x faster                                      |
| pidigits       | 191 ms                                                 | 191 ms: 1.00x faster                                       |
| Geometric mean | (ref)                                                  | 1.35x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 131 ms: 1.44x faster                                       |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                      |
| regex_dna      | 227 ms                                                 | 230 ms: 1.02x slower                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                       |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                       |
| tomli_loads          | 3.14 sec                                               | 2.16 sec: 1.45x faster                                     |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.36x faster                                      |
| xml_etree_process    | 79.1 ms                                                | 59.9 ms: 1.32x faster                                      |
| xml_etree_generate   | 99.4 ms                                                | 87.4 ms: 1.14x faster                                      |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                      |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                       |
| xml_etree_parse      | 168 ms                                                 | 161 ms: 1.04x faster                                       |
| pickle_list          | 5.08 us                                                | 4.98 us: 1.02x faster                                      |
| pickle               | 10.7 us                                                | 11.5 us: 1.08x slower                                      |
| unpickle             | 14.4 us                                                | 15.9 us: 1.10x slower                                      |
| pickle_dict          | 29.6 us                                                | 33.8 us: 1.14x slower                                      |
| Geometric mean       | (ref)                                                  | 1.14x faster                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.4 ms: 1.41x faster                                      |
| python_startup_no_site | 5.93 ms                                                | 8.92 ms: 1.50x slower                                      |
| Geometric mean         | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                      |
| django_template | 48.2 ms                                                | 34.7 ms: 1.39x faster                                      |
| genshi_text     | 31.8 ms                                                | 23.2 ms: 1.37x faster                                      |
| genshi_xml      | 66.0 ms                                                | 52.1 ms: 1.27x faster                                      |
| Geometric mean  | (ref)                                                  | 1.37x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 110 us: 4.95x faster                                       |
| generators               | 80.1 ms                                                | 29.2 ms: 2.74x faster                                      |
| deltablue                | 7.91 ms                                                | 3.23 ms: 2.45x faster                                      |
| chaos                    | 115 ms                                                 | 59.9 ms: 1.93x faster                                      |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                       |
| asyncio_tcp              | 922 ms                                                 | 493 ms: 1.87x faster                                       |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                       |
| comprehensions           | 28.8 us                                                | 16.3 us: 1.77x faster                                      |
| crypto_pyaes             | 128 ms                                                 | 72.3 ms: 1.77x faster                                      |
| pylint                   | 551 ms                                                 | 313 ms: 1.76x faster                                       |
| scimark_monte_carlo      | 118 ms                                                 | 68.6 ms: 1.72x faster                                      |
| richards_super           | 94.7 ms                                                | 55.1 ms: 1.72x faster                                      |
| nbody                    | 154 ms                                                 | 89.5 ms: 1.72x faster                                      |
| go                       | 240 ms                                                 | 140 ms: 1.71x faster                                       |
| hexiom                   | 10.4 ms                                                | 6.10 ms: 1.70x faster                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                      |
| scimark_sor              | 220 ms                                                 | 131 ms: 1.68x faster                                       |
| async_tree_none          | 728 ms                                                 | 446 ms: 1.63x faster                                       |
| richards                 | 79.3 ms                                                | 48.9 ms: 1.62x faster                                      |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                      |
| coroutines               | 35.1 ms                                                | 22.3 ms: 1.57x faster                                      |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.55x faster                                       |
| spectral_norm            | 170 ms                                                 | 111 ms: 1.53x faster                                       |
| deepcopy_memo            | 58.5 us                                                | 38.4 us: 1.52x faster                                      |
| pyflate                  | 716 ms                                                 | 471 ms: 1.52x faster                                       |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                       |
| async_tree_memoization   | 870 ms                                                 | 574 ms: 1.52x faster                                       |
| async_tree_io            | 1.77 sec                                               | 1.21 sec: 1.46x faster                                     |
| tomli_loads              | 3.14 sec                                               | 2.16 sec: 1.45x faster                                     |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                      |
| regex_compile            | 188 ms                                                 | 131 ms: 1.44x faster                                       |
| float                    | 117 ms                                                 | 82.0 ms: 1.43x faster                                      |
| logging_simple           | 8.30 us                                                | 5.89 us: 1.41x faster                                      |
| chameleon                | 9.68 ms                                                | 6.87 ms: 1.41x faster                                      |
| tornado_http             | 136 ms                                                 | 96.8 ms: 1.41x faster                                      |
| python_startup           | 14.6 ms                                                | 10.4 ms: 1.41x faster                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.83 sec: 1.41x faster                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 724 ms: 1.40x faster                                       |
| logging_format           | 9.09 us                                                | 6.53 us: 1.39x faster                                      |
| django_template          | 48.2 ms                                                | 34.7 ms: 1.39x faster                                      |
| genshi_text              | 31.8 ms                                                | 23.2 ms: 1.37x faster                                      |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.37x faster                                     |
| deepcopy                 | 479 us                                                 | 350 us: 1.37x faster                                       |
| pprint_safe_repr         | 1.02 sec                                               | 745 ms: 1.37x faster                                       |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.36x faster                                      |
| thrift                   | 1.07 ms                                                | 796 us: 1.35x faster                                       |
| deepcopy_reduce          | 4.17 us                                                | 3.11 us: 1.34x faster                                      |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                     |
| fannkuch                 | 532 ms                                                 | 402 ms: 1.32x faster                                       |
| xml_etree_process        | 79.1 ms                                                | 59.9 ms: 1.32x faster                                      |
| nqueens                  | 106 ms                                                 | 80.7 ms: 1.31x faster                                      |
| html5lib                 | 88.9 ms                                                | 67.9 ms: 1.31x faster                                      |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                       |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.29x faster                                       |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                      |
| 2to3                     | 348 ms                                                 | 270 ms: 1.29x faster                                       |
| scimark_fft              | 466 ms                                                 | 366 ms: 1.27x faster                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.10 ms: 1.27x faster                                      |
| genshi_xml               | 66.0 ms                                                | 52.1 ms: 1.27x faster                                      |
| sqlglot_optimize         | 69.2 ms                                                | 54.8 ms: 1.26x faster                                      |
| dulwich_log              | 84.3 ms                                                | 66.8 ms: 1.26x faster                                      |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                       |
| docutils                 | 3.30 sec                                               | 2.68 sec: 1.23x faster                                     |
| aiohttp                  | 1.44 ms                                                | 1.17 ms: 1.23x faster                                      |
| sympy_expand             | 566 ms                                                 | 466 ms: 1.21x faster                                       |
| djangocms                | 38.4 us                                                | 31.7 us: 1.21x faster                                      |
| gunicorn                 | 1.53 ms                                                | 1.27 ms: 1.21x faster                                      |
| bench_thread_pool        | 986 us                                                 | 842 us: 1.17x faster                                       |
| xml_etree_generate       | 99.4 ms                                                | 87.4 ms: 1.14x faster                                      |
| pathlib                  | 20.5 ms                                                | 18.5 ms: 1.11x faster                                      |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.10x faster                                     |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                      |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                       |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                      |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.51 ms: 1.07x faster                                      |
| json                     | 5.69 ms                                                | 5.39 ms: 1.06x faster                                      |
| sqlite_synth             | 3.02 us                                                | 2.88 us: 1.05x faster                                      |
| xml_etree_parse          | 168 ms                                                 | 161 ms: 1.04x faster                                       |
| pickle_list              | 5.08 us                                                | 4.98 us: 1.02x faster                                      |
| bench_mp_pool            | 24.0 ms                                                | 23.8 ms: 1.01x faster                                      |
| pidigits                 | 191 ms                                                 | 191 ms: 1.00x faster                                       |
| asyncio_websockets       | 559 ms                                                 | 563 ms: 1.01x slower                                       |
| regex_dna                | 227 ms                                                 | 230 ms: 1.02x slower                                       |
| async_generators         | 444 ms                                                 | 454 ms: 1.02x slower                                       |
| flaskblogging            | 8.58 ms                                                | 8.79 ms: 1.02x slower                                      |
| gc_traversal             | 3.62 ms                                                | 3.78 ms: 1.04x slower                                      |
| pickle                   | 10.7 us                                                | 11.5 us: 1.08x slower                                      |
| unpickle                 | 14.4 us                                                | 15.9 us: 1.10x slower                                      |
| pickle_dict              | 29.6 us                                                | 33.8 us: 1.14x slower                                      |
| telco                    | 7.27 ms                                                | 8.55 ms: 1.18x slower                                      |
| coverage                 | 79.4 ms                                                | 95.8 ms: 1.21x slower                                      |
| python_startup_no_site   | 5.93 ms                                                | 8.92 ms: 1.50x slower                                      |
| Geometric mean           | (ref)                                                  | 1.33x faster                                               |

Benchmark hidden because not significant (3): mypy2, unpickle_list, regex_effbot
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240117-3.13.0a3-f009305/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.06x