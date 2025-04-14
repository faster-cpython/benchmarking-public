# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.335x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 277 ms: 1.26x faster                                       |
| chameleon      | 9.68 ms                                                | 6.93 ms: 1.40x faster                                      |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                     |
| html5lib       | 88.9 ms                                                | 67.3 ms: 1.32x faster                                      |
| tornado_http   | 136 ms                                                 | 96.9 ms: 1.41x faster                                      |
| Geometric mean | (ref)                                                  | 1.32x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 438 ms: 1.66x faster                                       |
| async_tree_memoization  | 870 ms                                                 | 565 ms: 1.54x faster                                       |
| async_tree_io           | 1.77 sec                                               | 1.18 sec: 1.50x faster                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 710 ms: 1.43x faster                                       |
| Geometric mean          | (ref)                                                  | 1.53x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 154 ms                                                 | 103 ms: 1.49x faster                                       |
| float          | 117 ms                                                 | 85.3 ms: 1.37x faster                                      |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                       |
| Geometric mean | (ref)                                                  | 1.27x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.37x faster                                       |
| regex_v8       | 27.8 ms                                                | 25.2 ms: 1.10x faster                                      |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                       |
| Geometric mean | (ref)                                                  | 1.12x faster                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 298 us: 1.62x faster                                       |
| unpickle_pure_python | 331 us                                                 | 230 us: 1.44x faster                                       |
| tomli_loads          | 3.14 sec                                               | 2.21 sec: 1.42x faster                                     |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                      |
| xml_etree_process    | 79.1 ms                                                | 58.4 ms: 1.35x faster                                      |
| xml_etree_generate   | 99.4 ms                                                | 86.0 ms: 1.16x faster                                      |
| json_loads           | 31.2 us                                                | 27.5 us: 1.14x faster                                      |
| xml_etree_iterparse  | 115 ms                                                 | 107 ms: 1.08x faster                                       |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                       |
| unpickle_list        | 5.20 us                                                | 4.96 us: 1.05x faster                                      |
| pickle_list          | 5.08 us                                                | 5.00 us: 1.02x faster                                      |
| unpickle             | 14.4 us                                                | 15.3 us: 1.06x slower                                      |
| pickle               | 10.7 us                                                | 11.4 us: 1.07x slower                                      |
| pickle_dict          | 29.6 us                                                | 34.2 us: 1.16x slower                                      |
| Geometric mean       | (ref)                                                  | 1.16x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.2 ms: 1.43x faster                                      |
| python_startup_no_site | 5.93 ms                                                | 8.84 ms: 1.49x slower                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 48.2 ms                                                | 34.2 ms: 1.41x faster                                      |
| genshi_text     | 31.8 ms                                                | 23.4 ms: 1.36x faster                                      |
| mako            | 16.3 ms                                                | 12.1 ms: 1.35x faster                                      |
| genshi_xml      | 66.0 ms                                                | 52.7 ms: 1.25x faster                                      |
| Geometric mean  | (ref)                                                  | 1.34x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 111 us: 4.90x faster                                       |
| generators               | 80.1 ms                                                | 29.2 ms: 2.74x faster                                      |
| deltablue                | 7.91 ms                                                | 3.37 ms: 2.35x faster                                      |
| asyncio_tcp              | 922 ms                                                 | 478 ms: 1.93x faster                                       |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                       |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                       |
| richards_super           | 94.7 ms                                                | 51.7 ms: 1.83x faster                                      |
| raytrace                 | 507 ms                                                 | 279 ms: 1.82x faster                                       |
| pylint                   | 551 ms                                                 | 311 ms: 1.77x faster                                       |
| richards                 | 79.3 ms                                                | 45.3 ms: 1.75x faster                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                      |
| chaos                    | 115 ms                                                 | 69.5 ms: 1.66x faster                                      |
| async_tree_none          | 728 ms                                                 | 438 ms: 1.66x faster                                       |
| crypto_pyaes             | 128 ms                                                 | 78.6 ms: 1.63x faster                                      |
| pickle_pure_python       | 484 us                                                 | 298 us: 1.62x faster                                       |
| go                       | 240 ms                                                 | 148 ms: 1.62x faster                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                      |
| scimark_monte_carlo      | 118 ms                                                 | 74.5 ms: 1.59x faster                                      |
| comprehensions           | 28.8 us                                                | 18.3 us: 1.57x faster                                      |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                      |
| async_tree_memoization   | 870 ms                                                 | 565 ms: 1.54x faster                                       |
| deepcopy_memo            | 58.5 us                                                | 38.5 us: 1.52x faster                                      |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                       |
| async_tree_io            | 1.77 sec                                               | 1.18 sec: 1.50x faster                                     |
| nbody                    | 154 ms                                                 | 103 ms: 1.49x faster                                       |
| unpickle_pure_python     | 331 us                                                 | 230 us: 1.44x faster                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 710 ms: 1.43x faster                                       |
| logging_simple           | 8.30 us                                                | 5.81 us: 1.43x faster                                      |
| python_startup           | 14.6 ms                                                | 10.2 ms: 1.43x faster                                      |
| tomli_loads              | 3.14 sec                                               | 2.21 sec: 1.42x faster                                     |
| pyflate                  | 716 ms                                                 | 507 ms: 1.41x faster                                       |
| django_template          | 48.2 ms                                                | 34.2 ms: 1.41x faster                                      |
| tornado_http             | 136 ms                                                 | 96.9 ms: 1.41x faster                                      |
| logging_format           | 9.09 us                                                | 6.47 us: 1.40x faster                                      |
| chameleon                | 9.68 ms                                                | 6.93 ms: 1.40x faster                                      |
| deepcopy_reduce          | 4.17 us                                                | 3.03 us: 1.38x faster                                      |
| float                    | 117 ms                                                 | 85.3 ms: 1.37x faster                                      |
| deepcopy                 | 479 us                                                 | 350 us: 1.37x faster                                       |
| regex_compile            | 188 ms                                                 | 138 ms: 1.37x faster                                       |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                      |
| genshi_text              | 31.8 ms                                                | 23.4 ms: 1.36x faster                                      |
| thrift                   | 1.07 ms                                                | 789 us: 1.36x faster                                       |
| xml_etree_process        | 79.1 ms                                                | 58.4 ms: 1.35x faster                                      |
| mako                     | 16.3 ms                                                | 12.1 ms: 1.35x faster                                      |
| hexiom                   | 10.4 ms                                                | 7.76 ms: 1.34x faster                                      |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                     |
| pprint_safe_repr         | 1.02 sec                                               | 770 ms: 1.32x faster                                       |
| html5lib                 | 88.9 ms                                                | 67.3 ms: 1.32x faster                                      |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.32x faster                                       |
| spectral_norm            | 170 ms                                                 | 132 ms: 1.29x faster                                       |
| pprint_pformat           | 2.10 sec                                               | 1.63 sec: 1.29x faster                                     |
| fannkuch                 | 532 ms                                                 | 420 ms: 1.26x faster                                       |
| scimark_fft              | 466 ms                                                 | 369 ms: 1.26x faster                                       |
| 2to3                     | 348 ms                                                 | 277 ms: 1.26x faster                                       |
| sympy_integrate          | 25.8 ms                                                | 20.6 ms: 1.25x faster                                      |
| genshi_xml               | 66.0 ms                                                | 52.7 ms: 1.25x faster                                      |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                     |
| sqlglot_optimize         | 69.2 ms                                                | 55.7 ms: 1.24x faster                                      |
| sympy_sum                | 196 ms                                                 | 159 ms: 1.24x faster                                       |
| dulwich_log              | 84.3 ms                                                | 68.7 ms: 1.23x faster                                      |
| sympy_str                | 346 ms                                                 | 283 ms: 1.22x faster                                       |
| aiohttp                  | 1.44 ms                                                | 1.18 ms: 1.22x faster                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.30 ms: 1.22x faster                                      |
| gunicorn                 | 1.53 ms                                                | 1.27 ms: 1.21x faster                                      |
| bench_thread_pool        | 986 us                                                 | 839 us: 1.18x faster                                       |
| djangocms                | 38.4 us                                                | 32.8 us: 1.17x faster                                      |
| sympy_expand             | 566 ms                                                 | 484 ms: 1.17x faster                                       |
| nqueens                  | 106 ms                                                 | 91.0 ms: 1.16x faster                                      |
| xml_etree_generate       | 99.4 ms                                                | 86.0 ms: 1.16x faster                                      |
| unpack_sequence          | 60.0 ns                                                | 52.6 ns: 1.14x faster                                      |
| json_loads               | 31.2 us                                                | 27.5 us: 1.14x faster                                      |
| json                     | 5.69 ms                                                | 5.07 ms: 1.12x faster                                      |
| pathlib                  | 20.5 ms                                                | 18.4 ms: 1.11x faster                                      |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                       |
| regex_v8                 | 27.8 ms                                                | 25.2 ms: 1.10x faster                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.48 ms: 1.10x faster                                      |
| xml_etree_iterparse      | 115 ms                                                 | 107 ms: 1.08x faster                                       |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                       |
| sqlite_synth             | 3.02 us                                                | 2.83 us: 1.07x faster                                      |
| mdp                      | 2.85 sec                                               | 2.71 sec: 1.05x faster                                     |
| unpickle_list            | 5.20 us                                                | 4.96 us: 1.05x faster                                      |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                       |
| pickle_list              | 5.08 us                                                | 5.00 us: 1.02x faster                                      |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                       |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                       |
| async_generators         | 444 ms                                                 | 455 ms: 1.02x slower                                       |
| gc_traversal             | 3.62 ms                                                | 3.72 ms: 1.03x slower                                      |
| unpickle                 | 14.4 us                                                | 15.3 us: 1.06x slower                                      |
| pickle                   | 10.7 us                                                | 11.4 us: 1.07x slower                                      |
| flaskblogging            | 8.58 ms                                                | 9.37 ms: 1.09x slower                                      |
| pickle_dict              | 29.6 us                                                | 34.2 us: 1.16x slower                                      |
| telco                    | 7.27 ms                                                | 8.42 ms: 1.16x slower                                      |
| coverage                 | 79.4 ms                                                | 94.7 ms: 1.19x slower                                      |
| python_startup_no_site   | 5.93 ms                                                | 8.84 ms: 1.49x slower                                      |
| Geometric mean           | (ref)                                                  | 1.31x faster                                               |

Benchmark hidden because not significant (3): mypy2, regex_effbot, bench_mp_pool
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240215-3.13.0a4-9d34f60-PYTHON_UOPS/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.335x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.11x