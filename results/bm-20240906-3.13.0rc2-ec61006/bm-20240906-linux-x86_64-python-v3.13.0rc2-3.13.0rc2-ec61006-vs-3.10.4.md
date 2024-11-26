# Results vs. 3.10.4

- fork: python
- ref: v3.13.0rc2
- machine: linux-x86_64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.383x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 263 ms: 1.32x faster                                         |
| chameleon      | 9.68 ms                                                | 6.97 ms: 1.39x faster                                        |
| docutils       | 3.30 sec                                               | 2.74 sec: 1.20x faster                                       |
| html5lib       | 88.9 ms                                                | 64.9 ms: 1.37x faster                                        |
| tornado_http   | 136 ms                                                 | 91.4 ms: 1.49x faster                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 362 ms: 2.01x faster                                         |
| async_tree_io           | 1.77 sec                                               | 889 ms: 1.99x faster                                         |
| async_tree_memoization  | 870 ms                                                 | 455 ms: 1.91x faster                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 588 ms: 1.73x faster                                         |
| Geometric mean          | (ref)                                                  | 1.91x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.0 ms: 1.74x faster                                        |
| float          | 117 ms                                                 | 77.4 ms: 1.51x faster                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                  | 1.39x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 133 ms: 1.41x faster                                         |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                        |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                         |
| regex_effbot   | 3.63 ms                                                | 3.49 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                  | 1.15x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                         |
| tomli_loads          | 3.14 sec                                               | 2.07 sec: 1.52x faster                                       |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.51x faster                                         |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                        |
| xml_etree_process    | 79.1 ms                                                | 60.8 ms: 1.30x faster                                        |
| json_loads           | 31.2 us                                                | 27.1 us: 1.15x faster                                        |
| xml_etree_generate   | 99.4 ms                                                | 87.5 ms: 1.14x faster                                        |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                         |
| xml_etree_iterparse  | 115 ms                                                 | 107 ms: 1.08x faster                                         |
| unpickle_list        | 5.20 us                                                | 5.06 us: 1.03x faster                                        |
| pickle_list          | 5.08 us                                                | 5.25 us: 1.03x slower                                        |
| unpickle             | 14.4 us                                                | 14.9 us: 1.04x slower                                        |
| pickle               | 10.7 us                                                | 11.4 us: 1.07x slower                                        |
| pickle_dict          | 29.6 us                                                | 34.5 us: 1.16x slower                                        |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                        |
| python_startup_no_site | 5.93 ms                                                | 6.96 ms: 1.17x slower                                        |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                        |
| django_template | 48.2 ms                                                | 33.9 ms: 1.42x faster                                        |
| genshi_text     | 31.8 ms                                                | 23.4 ms: 1.36x faster                                        |
| genshi_xml      | 66.0 ms                                                | 50.9 ms: 1.30x faster                                        |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                         |
| generators               | 80.1 ms                                                | 29.1 ms: 2.75x faster                                        |
| deltablue                | 7.91 ms                                                | 3.25 ms: 2.44x faster                                        |
| async_tree_none          | 728 ms                                                 | 362 ms: 2.01x faster                                         |
| async_tree_io            | 1.77 sec                                               | 889 ms: 1.99x faster                                         |
| chaos                    | 115 ms                                                 | 59.6 ms: 1.94x faster                                        |
| asyncio_tcp              | 922 ms                                                 | 480 ms: 1.92x faster                                         |
| async_tree_memoization   | 870 ms                                                 | 455 ms: 1.91x faster                                         |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                         |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                         |
| richards_super           | 94.7 ms                                                | 53.2 ms: 1.78x faster                                        |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                        |
| nbody                    | 154 ms                                                 | 88.0 ms: 1.74x faster                                        |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                         |
| scimark_monte_carlo      | 118 ms                                                 | 68.2 ms: 1.73x faster                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 588 ms: 1.73x faster                                         |
| pylint                   | 551 ms                                                 | 323 ms: 1.71x faster                                         |
| go                       | 240 ms                                                 | 141 ms: 1.71x faster                                         |
| crypto_pyaes             | 128 ms                                                 | 75.3 ms: 1.70x faster                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                        |
| richards                 | 79.3 ms                                                | 47.3 ms: 1.68x faster                                        |
| hexiom                   | 10.4 ms                                                | 6.29 ms: 1.65x faster                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                        |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                         |
| coroutines               | 35.1 ms                                                | 22.1 ms: 1.59x faster                                        |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                         |
| pyflate                  | 716 ms                                                 | 467 ms: 1.53x faster                                         |
| tomli_loads              | 3.14 sec                                               | 2.07 sec: 1.52x faster                                       |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.51x faster                                         |
| float                    | 117 ms                                                 | 77.4 ms: 1.51x faster                                        |
| tornado_http             | 136 ms                                                 | 91.4 ms: 1.49x faster                                        |
| deepcopy_memo            | 58.5 us                                                | 39.5 us: 1.48x faster                                        |
| logging_simple           | 8.30 us                                                | 5.70 us: 1.46x faster                                        |
| spectral_norm            | 170 ms                                                 | 117 ms: 1.46x faster                                         |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.78 sec: 1.44x faster                                       |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                        |
| logging_format           | 9.09 us                                                | 6.39 us: 1.42x faster                                        |
| django_template          | 48.2 ms                                                | 33.9 ms: 1.42x faster                                        |
| regex_compile            | 188 ms                                                 | 133 ms: 1.41x faster                                         |
| chameleon                | 9.68 ms                                                | 6.97 ms: 1.39x faster                                        |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.38x faster                                       |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                        |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                       |
| pprint_safe_repr         | 1.02 sec                                               | 744 ms: 1.37x faster                                         |
| html5lib                 | 88.9 ms                                                | 64.9 ms: 1.37x faster                                        |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                        |
| genshi_text              | 31.8 ms                                                | 23.4 ms: 1.36x faster                                        |
| nqueens                  | 106 ms                                                 | 78.9 ms: 1.34x faster                                        |
| fannkuch                 | 532 ms                                                 | 398 ms: 1.34x faster                                         |
| deepcopy                 | 479 us                                                 | 359 us: 1.34x faster                                         |
| thrift                   | 1.07 ms                                                | 806 us: 1.33x faster                                         |
| dulwich_log              | 84.3 ms                                                | 63.7 ms: 1.32x faster                                        |
| 2to3                     | 348 ms                                                 | 263 ms: 1.32x faster                                         |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.32x faster                                         |
| xml_etree_process        | 79.1 ms                                                | 60.8 ms: 1.30x faster                                        |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                         |
| genshi_xml               | 66.0 ms                                                | 50.9 ms: 1.30x faster                                        |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.29x faster                                        |
| deepcopy_reduce          | 4.17 us                                                | 3.22 us: 1.29x faster                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.01 ms: 1.29x faster                                        |
| sqlglot_optimize         | 69.2 ms                                                | 53.9 ms: 1.28x faster                                        |
| scimark_fft              | 466 ms                                                 | 365 ms: 1.28x faster                                         |
| aiohttp                  | 1.44 ms                                                | 1.14 ms: 1.26x faster                                        |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                         |
| unpack_sequence          | 60.0 ns                                                | 47.9 ns: 1.25x faster                                        |
| mypy2                    | 894 ms                                                 | 717 ms: 1.25x faster                                         |
| gunicorn                 | 1.53 ms                                                | 1.24 ms: 1.24x faster                                        |
| dask                     | 441 ms                                                 | 358 ms: 1.23x faster                                         |
| sympy_expand             | 566 ms                                                 | 464 ms: 1.22x faster                                         |
| bench_thread_pool        | 986 us                                                 | 818 us: 1.21x faster                                         |
| docutils                 | 3.30 sec                                               | 2.74 sec: 1.20x faster                                       |
| pathlib                  | 20.5 ms                                                | 17.2 ms: 1.19x faster                                        |
| djangocms                | 38.4 us                                                | 32.5 us: 1.18x faster                                        |
| json_loads               | 31.2 us                                                | 27.1 us: 1.15x faster                                        |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                        |
| xml_etree_generate       | 99.4 ms                                                | 87.5 ms: 1.14x faster                                        |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                         |
| json                     | 5.69 ms                                                | 5.24 ms: 1.09x faster                                        |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                         |
| xml_etree_iterparse      | 115 ms                                                 | 107 ms: 1.08x faster                                         |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                        |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                         |
| regex_effbot             | 3.63 ms                                                | 3.49 ms: 1.04x faster                                        |
| mdp                      | 2.85 sec                                               | 2.75 sec: 1.03x faster                                       |
| unpickle_list            | 5.20 us                                                | 5.06 us: 1.03x faster                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                         |
| async_generators         | 444 ms                                                 | 435 ms: 1.02x faster                                         |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                         |
| gc_traversal             | 3.62 ms                                                | 3.73 ms: 1.03x slower                                        |
| pickle_list              | 5.08 us                                                | 5.25 us: 1.03x slower                                        |
| unpickle                 | 14.4 us                                                | 14.9 us: 1.04x slower                                        |
| coverage                 | 79.4 ms                                                | 84.1 ms: 1.06x slower                                        |
| flaskblogging            | 8.58 ms                                                | 9.16 ms: 1.07x slower                                        |
| pickle                   | 10.7 us                                                | 11.4 us: 1.07x slower                                        |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.08x slower                                        |
| pickle_dict              | 29.6 us                                                | 34.5 us: 1.16x slower                                        |
| python_startup_no_site   | 5.93 ms                                                | 6.96 ms: 1.17x slower                                        |
| telco                    | 7.27 ms                                                | 8.63 ms: 1.19x slower                                        |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.383x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.13x