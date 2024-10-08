# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 296 ms: 1.18x faster                                       |
| chameleon      | 9.68 ms                                                | 8.24 ms: 1.17x faster                                      |
| docutils       | 3.30 sec                                               | 3.07 sec: 1.07x faster                                     |
| html5lib       | 88.9 ms                                                | 67.9 ms: 1.31x faster                                      |
| tornado_http   | 136 ms                                                 | 98.6 ms: 1.38x faster                                      |
| Geometric mean | (ref)                                                  | 1.22x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 796 ms: 2.22x faster                                       |
| async_tree_none         | 728 ms                                                 | 377 ms: 1.93x faster                                       |
| async_tree_memoization  | 870 ms                                                 | 476 ms: 1.83x faster                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 646 ms: 1.57x faster                                       |
| Geometric mean          | (ref)                                                  | 1.87x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 117 ms                                                 | 74.2 ms: 1.58x faster                                      |
| nbody          | 154 ms                                                 | 104 ms: 1.47x faster                                       |
| pidigits       | 191 ms                                                 | 194 ms: 1.02x slower                                       |
| Geometric mean | (ref)                                                  | 1.32x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 141 ms: 1.34x faster                                       |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                      |
| regex_dna      | 227 ms                                                 | 232 ms: 1.02x slower                                       |
| Geometric mean | (ref)                                                  | 1.10x faster                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 333 us: 1.46x faster                                       |
| tomli_loads          | 3.14 sec                                               | 2.23 sec: 1.41x faster                                     |
| unpickle_pure_python | 331 us                                                 | 237 us: 1.40x faster                                       |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                      |
| xml_etree_process    | 79.1 ms                                                | 71.1 ms: 1.11x faster                                      |
| xml_etree_parse      | 168 ms                                                 | 151 ms: 1.11x faster                                       |
| xml_etree_generate   | 99.4 ms                                                | 90.5 ms: 1.10x faster                                      |
| pickle_list          | 5.08 us                                                | 4.88 us: 1.04x faster                                      |
| json_loads           | 31.2 us                                                | 32.2 us: 1.03x slower                                      |
| pickle               | 10.7 us                                                | 12.0 us: 1.13x slower                                      |
| unpickle             | 14.4 us                                                | 18.0 us: 1.25x slower                                      |
| pickle_dict          | 29.6 us                                                | 41.2 us: 1.39x slower                                      |
| xml_etree_iterparse  | 115 ms                                                 | 166 ms: 1.44x slower                                       |
| Geometric mean       | (ref)                                                  | 1.04x faster                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.0 ms: 1.21x faster                                      |
| python_startup_no_site | 5.93 ms                                                | 10.0 ms: 1.69x slower                                      |
| Geometric mean         | (ref)                                                  | 1.18x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 48.2 ms                                                | 39.1 ms: 1.23x faster                                      |
| genshi_text     | 31.8 ms                                                | 26.1 ms: 1.22x faster                                      |
| genshi_xml      | 66.0 ms                                                | 54.7 ms: 1.21x faster                                      |
| Geometric mean  | (ref)                                                  | 1.16x faster                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 122 us: 4.46x faster                                       |
| generators               | 80.1 ms                                                | 31.2 ms: 2.57x faster                                      |
| async_tree_io            | 1.77 sec                                               | 796 ms: 2.22x faster                                       |
| async_tree_none          | 728 ms                                                 | 377 ms: 1.93x faster                                       |
| deltablue                | 7.91 ms                                                | 4.16 ms: 1.90x faster                                      |
| pylint                   | 551 ms                                                 | 296 ms: 1.86x faster                                       |
| async_tree_memoization   | 870 ms                                                 | 476 ms: 1.83x faster                                       |
| asyncio_tcp              | 922 ms                                                 | 508 ms: 1.81x faster                                       |
| chaos                    | 115 ms                                                 | 66.2 ms: 1.74x faster                                      |
| raytrace                 | 507 ms                                                 | 298 ms: 1.70x faster                                       |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                       |
| crypto_pyaes             | 128 ms                                                 | 75.5 ms: 1.69x faster                                      |
| richards_super           | 94.7 ms                                                | 56.3 ms: 1.68x faster                                      |
| logging_silent           | 190 ns                                                 | 114 ns: 1.66x faster                                       |
| richards                 | 79.3 ms                                                | 49.2 ms: 1.61x faster                                      |
| scimark_monte_carlo      | 118 ms                                                 | 74.0 ms: 1.60x faster                                      |
| float                    | 117 ms                                                 | 74.2 ms: 1.58x faster                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.03 ms: 1.58x faster                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 646 ms: 1.57x faster                                       |
| hexiom                   | 10.4 ms                                                | 6.62 ms: 1.57x faster                                      |
| go                       | 240 ms                                                 | 154 ms: 1.56x faster                                       |
| comprehensions           | 28.8 us                                                | 18.5 us: 1.55x faster                                      |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                      |
| pyflate                  | 716 ms                                                 | 474 ms: 1.51x faster                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.44 ms: 1.50x faster                                      |
| nbody                    | 154 ms                                                 | 104 ms: 1.47x faster                                       |
| scimark_lu               | 176 ms                                                 | 121 ms: 1.46x faster                                       |
| pickle_pure_python       | 484 us                                                 | 333 us: 1.46x faster                                       |
| spectral_norm            | 170 ms                                                 | 118 ms: 1.44x faster                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.78 ms: 1.44x faster                                      |
| gc_traversal             | 3.62 ms                                                | 2.57 ms: 1.41x faster                                      |
| tomli_loads              | 3.14 sec                                               | 2.23 sec: 1.41x faster                                     |
| unpickle_pure_python     | 331 us                                                 | 237 us: 1.40x faster                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                     |
| tornado_http             | 136 ms                                                 | 98.6 ms: 1.38x faster                                      |
| regex_compile            | 188 ms                                                 | 141 ms: 1.34x faster                                       |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                     |
| html5lib                 | 88.9 ms                                                | 67.9 ms: 1.31x faster                                      |
| logging_simple           | 8.30 us                                                | 6.43 us: 1.29x faster                                      |
| mypy2                    | 894 ms                                                 | 696 ms: 1.28x faster                                       |
| deepcopy_memo            | 58.5 us                                                | 45.6 us: 1.28x faster                                      |
| pprint_pformat           | 2.10 sec                                               | 1.64 sec: 1.28x faster                                     |
| pprint_safe_repr         | 1.02 sec                                               | 797 ms: 1.28x faster                                       |
| logging_format           | 9.09 us                                                | 7.18 us: 1.27x faster                                      |
| nqueens                  | 106 ms                                                 | 84.7 ms: 1.25x faster                                      |
| fannkuch                 | 532 ms                                                 | 428 ms: 1.24x faster                                       |
| sqlglot_normalize        | 143 ms                                                 | 116 ms: 1.23x faster                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.25 ms: 1.23x faster                                      |
| django_template          | 48.2 ms                                                | 39.1 ms: 1.23x faster                                      |
| deepcopy                 | 479 us                                                 | 390 us: 1.23x faster                                       |
| scimark_fft              | 466 ms                                                 | 380 ms: 1.23x faster                                       |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                      |
| dulwich_log              | 84.3 ms                                                | 69.0 ms: 1.22x faster                                      |
| genshi_text              | 31.8 ms                                                | 26.1 ms: 1.22x faster                                      |
| python_startup           | 14.6 ms                                                | 12.0 ms: 1.21x faster                                      |
| genshi_xml               | 66.0 ms                                                | 54.7 ms: 1.21x faster                                      |
| deepcopy_reduce          | 4.17 us                                                | 3.46 us: 1.21x faster                                      |
| 2to3                     | 348 ms                                                 | 296 ms: 1.18x faster                                       |
| chameleon                | 9.68 ms                                                | 8.24 ms: 1.17x faster                                      |
| sqlglot_optimize         | 69.2 ms                                                | 59.3 ms: 1.17x faster                                      |
| aiohttp                  | 1.44 ms                                                | 1.27 ms: 1.13x faster                                      |
| gunicorn                 | 1.53 ms                                                | 1.37 ms: 1.11x faster                                      |
| xml_etree_process        | 79.1 ms                                                | 71.1 ms: 1.11x faster                                      |
| xml_etree_parse          | 168 ms                                                 | 151 ms: 1.11x faster                                       |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                      |
| xml_etree_generate       | 99.4 ms                                                | 90.5 ms: 1.10x faster                                      |
| sympy_integrate          | 25.8 ms                                                | 23.8 ms: 1.08x faster                                      |
| pathlib                  | 20.5 ms                                                | 19.0 ms: 1.08x faster                                      |
| docutils                 | 3.30 sec                                               | 3.07 sec: 1.07x faster                                     |
| pickle_list              | 5.08 us                                                | 4.88 us: 1.04x faster                                      |
| meteor_contest           | 120 ms                                                 | 115 ms: 1.04x faster                                       |
| bench_mp_pool            | 24.0 ms                                                | 23.4 ms: 1.03x faster                                      |
| pidigits                 | 191 ms                                                 | 194 ms: 1.02x slower                                       |
| json                     | 5.69 ms                                                | 5.81 ms: 1.02x slower                                      |
| regex_dna                | 227 ms                                                 | 232 ms: 1.02x slower                                       |
| sympy_str                | 346 ms                                                 | 354 ms: 1.02x slower                                       |
| json_loads               | 31.2 us                                                | 32.2 us: 1.03x slower                                      |
| async_generators         | 444 ms                                                 | 463 ms: 1.04x slower                                       |
| sqlite_synth             | 3.02 us                                                | 3.17 us: 1.05x slower                                      |
| sympy_sum                | 196 ms                                                 | 211 ms: 1.08x slower                                       |
| sympy_expand             | 566 ms                                                 | 623 ms: 1.10x slower                                       |
| pickle                   | 10.7 us                                                | 12.0 us: 1.13x slower                                      |
| unpickle                 | 14.4 us                                                | 18.0 us: 1.25x slower                                      |
| telco                    | 7.27 ms                                                | 9.09 ms: 1.25x slower                                      |
| mdp                      | 2.85 sec                                               | 3.64 sec: 1.28x slower                                     |
| pickle_dict              | 29.6 us                                                | 41.2 us: 1.39x slower                                      |
| xml_etree_iterparse      | 115 ms                                                 | 166 ms: 1.44x slower                                       |
| python_startup_no_site   | 5.93 ms                                                | 10.0 ms: 1.69x slower                                      |
| flaskblogging            | 8.58 ms                                                | 18.7 ms: 2.18x slower                                      |
| bench_thread_pool        | 986 us                                                 | 2.42 ms: 2.46x slower                                      |
| thrift                   | 1.07 ms                                                | 9.43 ms: 8.80x slower                                      |
| coverage                 | 79.4 ms                                                | 712 ms: 8.96x slower                                       |
| Geometric mean           | (ref)                                                  | 1.18x faster                                               |

Benchmark hidden because not significant (4): regex_effbot, asyncio_websockets, mako, unpickle_list
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, djangocms, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240215-3.13.0a4-9d34f60-NOGIL/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.19x