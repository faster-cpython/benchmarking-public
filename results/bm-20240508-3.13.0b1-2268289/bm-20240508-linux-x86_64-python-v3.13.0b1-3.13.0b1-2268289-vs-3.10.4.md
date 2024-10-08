# Results vs. 3.10.4

- fork: python
- ref: v3.13.0b1
- machine: linux-x86_64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 272 ms: 1.28x faster                                       |
| chameleon      | 9.68 ms                                                | 7.11 ms: 1.36x faster                                      |
| docutils       | 3.30 sec                                               | 2.86 sec: 1.15x faster                                     |
| html5lib       | 88.9 ms                                                | 68.4 ms: 1.30x faster                                      |
| tornado_http   | 136 ms                                                 | 95.8 ms: 1.42x faster                                      |
| Geometric mean | (ref)                                                  | 1.30x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 363 ms: 2.00x faster                                       |
| async_tree_io           | 1.77 sec                                               | 936 ms: 1.89x faster                                       |
| async_tree_memoization  | 870 ms                                                 | 477 ms: 1.83x faster                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 619 ms: 1.64x faster                                       |
| Geometric mean          | (ref)                                                  | 1.84x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 154 ms                                                 | 87.8 ms: 1.75x faster                                      |
| float          | 117 ms                                                 | 78.5 ms: 1.49x faster                                      |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                  | 1.38x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.40x faster                                       |
| regex_v8       | 27.8 ms                                                | 26.2 ms: 1.06x faster                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                               |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 311 us: 1.56x faster                                       |
| unpickle_pure_python | 331 us                                                 | 223 us: 1.48x faster                                       |
| tomli_loads          | 3.14 sec                                               | 2.22 sec: 1.42x faster                                     |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.36x faster                                      |
| xml_etree_process    | 79.1 ms                                                | 60.3 ms: 1.31x faster                                      |
| xml_etree_generate   | 99.4 ms                                                | 87.7 ms: 1.13x faster                                      |
| json_loads           | 31.2 us                                                | 28.9 us: 1.08x faster                                      |
| xml_etree_iterparse  | 115 ms                                                 | 108 ms: 1.07x faster                                       |
| xml_etree_parse      | 168 ms                                                 | 159 ms: 1.06x faster                                       |
| unpickle_list        | 5.20 us                                                | 5.38 us: 1.04x slower                                      |
| pickle_list          | 5.08 us                                                | 5.30 us: 1.04x slower                                      |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                      |
| pickle_dict          | 29.6 us                                                | 33.8 us: 1.14x slower                                      |
| unpickle             | 14.4 us                                                | 17.0 us: 1.18x slower                                      |
| Geometric mean       | (ref)                                                  | 1.12x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.7 ms: 1.36x faster                                      |
| python_startup_no_site | 5.93 ms                                                | 7.19 ms: 1.21x slower                                      |
| Geometric mean         | (ref)                                                  | 1.06x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.9 ms: 1.50x faster                                      |
| genshi_text     | 31.8 ms                                                | 23.1 ms: 1.38x faster                                      |
| django_template | 48.2 ms                                                | 35.1 ms: 1.37x faster                                      |
| genshi_xml      | 66.0 ms                                                | 52.1 ms: 1.27x faster                                      |
| Geometric mean  | (ref)                                                  | 1.38x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.21x faster                                       |
| generators               | 80.1 ms                                                | 29.3 ms: 2.74x faster                                      |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                      |
| async_tree_none          | 728 ms                                                 | 363 ms: 2.00x faster                                       |
| chaos                    | 115 ms                                                 | 58.8 ms: 1.96x faster                                      |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                       |
| async_tree_io            | 1.77 sec                                               | 936 ms: 1.89x faster                                       |
| async_tree_memoization   | 870 ms                                                 | 477 ms: 1.83x faster                                       |
| asyncio_tcp              | 922 ms                                                 | 510 ms: 1.81x faster                                       |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                       |
| nbody                    | 154 ms                                                 | 87.8 ms: 1.75x faster                                      |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.72x faster                                       |
| pylint                   | 551 ms                                                 | 321 ms: 1.72x faster                                       |
| comprehensions           | 28.8 us                                                | 17.0 us: 1.70x faster                                      |
| hexiom                   | 10.4 ms                                                | 6.15 ms: 1.69x faster                                      |
| scimark_monte_carlo      | 118 ms                                                 | 69.9 ms: 1.69x faster                                      |
| crypto_pyaes             | 128 ms                                                 | 76.2 ms: 1.68x faster                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                      |
| richards_super           | 94.7 ms                                                | 57.4 ms: 1.65x faster                                      |
| go                       | 240 ms                                                 | 146 ms: 1.64x faster                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 619 ms: 1.64x faster                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.58x faster                                      |
| richards                 | 79.3 ms                                                | 50.5 ms: 1.57x faster                                      |
| pickle_pure_python       | 484 us                                                 | 311 us: 1.56x faster                                       |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                      |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                       |
| pyflate                  | 716 ms                                                 | 473 ms: 1.52x faster                                       |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.50x faster                                       |
| mako                     | 16.3 ms                                                | 10.9 ms: 1.50x faster                                      |
| float                    | 117 ms                                                 | 78.5 ms: 1.49x faster                                      |
| deepcopy_memo            | 58.5 us                                                | 39.4 us: 1.48x faster                                      |
| unpickle_pure_python     | 331 us                                                 | 223 us: 1.48x faster                                       |
| tornado_http             | 136 ms                                                 | 95.8 ms: 1.42x faster                                      |
| tomli_loads              | 3.14 sec                                               | 2.22 sec: 1.42x faster                                     |
| logging_simple           | 8.30 us                                                | 5.91 us: 1.41x faster                                      |
| regex_compile            | 188 ms                                                 | 135 ms: 1.40x faster                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.84 sec: 1.40x faster                                     |
| logging_format           | 9.09 us                                                | 6.54 us: 1.39x faster                                      |
| genshi_text              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                      |
| django_template          | 48.2 ms                                                | 35.1 ms: 1.37x faster                                      |
| python_startup           | 14.6 ms                                                | 10.7 ms: 1.36x faster                                      |
| chameleon                | 9.68 ms                                                | 7.11 ms: 1.36x faster                                      |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.36x faster                                      |
| fannkuch                 | 532 ms                                                 | 393 ms: 1.35x faster                                       |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                     |
| thrift                   | 1.07 ms                                                | 801 us: 1.34x faster                                       |
| pprint_safe_repr         | 1.02 sec                                               | 767 ms: 1.33x faster                                       |
| xml_etree_process        | 79.1 ms                                                | 60.3 ms: 1.31x faster                                      |
| deepcopy                 | 479 us                                                 | 366 us: 1.31x faster                                       |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.30x faster                                     |
| nqueens                  | 106 ms                                                 | 81.4 ms: 1.30x faster                                      |
| html5lib                 | 88.9 ms                                                | 68.4 ms: 1.30x faster                                      |
| 2to3                     | 348 ms                                                 | 272 ms: 1.28x faster                                       |
| deepcopy_reduce          | 4.17 us                                                | 3.26 us: 1.28x faster                                      |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                       |
| genshi_xml               | 66.0 ms                                                | 52.1 ms: 1.27x faster                                      |
| dulwich_log              | 84.3 ms                                                | 67.0 ms: 1.26x faster                                      |
| sympy_integrate          | 25.8 ms                                                | 20.5 ms: 1.26x faster                                      |
| scimark_fft              | 466 ms                                                 | 373 ms: 1.25x faster                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.18 ms: 1.25x faster                                      |
| sympy_sum                | 196 ms                                                 | 157 ms: 1.25x faster                                       |
| sqlglot_optimize         | 69.2 ms                                                | 55.8 ms: 1.24x faster                                      |
| sympy_str                | 346 ms                                                 | 284 ms: 1.22x faster                                       |
| djangocms                | 38.4 us                                                | 31.7 us: 1.21x faster                                      |
| mypy2                    | 894 ms                                                 | 743 ms: 1.20x faster                                       |
| aiohttp                  | 1.44 ms                                                | 1.20 ms: 1.20x faster                                      |
| gunicorn                 | 1.53 ms                                                | 1.29 ms: 1.19x faster                                      |
| sympy_expand             | 566 ms                                                 | 477 ms: 1.19x faster                                       |
| dask                     | 441 ms                                                 | 372 ms: 1.18x faster                                       |
| bench_thread_pool        | 986 us                                                 | 839 us: 1.18x faster                                       |
| docutils                 | 3.30 sec                                               | 2.86 sec: 1.15x faster                                     |
| pathlib                  | 20.5 ms                                                | 17.9 ms: 1.15x faster                                      |
| xml_etree_generate       | 99.4 ms                                                | 87.7 ms: 1.13x faster                                      |
| mdp                      | 2.85 sec                                               | 2.60 sec: 1.09x faster                                     |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.08x faster                                       |
| json_loads               | 31.2 us                                                | 28.9 us: 1.08x faster                                      |
| xml_etree_iterparse      | 115 ms                                                 | 108 ms: 1.07x faster                                       |
| regex_v8                 | 27.8 ms                                                | 26.2 ms: 1.06x faster                                      |
| xml_etree_parse          | 168 ms                                                 | 159 ms: 1.06x faster                                       |
| json                     | 5.69 ms                                                | 5.41 ms: 1.05x faster                                      |
| sqlite_synth             | 3.02 us                                                | 2.96 us: 1.02x faster                                      |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                       |
| bench_mp_pool            | 24.0 ms                                                | 23.9 ms: 1.01x faster                                      |
| asyncio_websockets       | 559 ms                                                 | 564 ms: 1.01x slower                                       |
| async_generators         | 444 ms                                                 | 452 ms: 1.02x slower                                       |
| unpickle_list            | 5.20 us                                                | 5.38 us: 1.04x slower                                      |
| pickle_list              | 5.08 us                                                | 5.30 us: 1.04x slower                                      |
| flaskblogging            | 8.58 ms                                                | 9.05 ms: 1.06x slower                                      |
| gc_traversal             | 3.62 ms                                                | 3.85 ms: 1.06x slower                                      |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.80 ms: 1.11x slower                                      |
| pickle_dict              | 29.6 us                                                | 33.8 us: 1.14x slower                                      |
| coverage                 | 79.4 ms                                                | 92.4 ms: 1.16x slower                                      |
| unpickle                 | 14.4 us                                                | 17.0 us: 1.18x slower                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.19 ms: 1.21x slower                                      |
| telco                    | 7.27 ms                                                | 173 ms: 23.75x slower                                      |
| Geometric mean           | (ref)                                                  | 1.28x faster                                               |

Benchmark hidden because not significant (2): regex_dna, regex_effbot
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240508-3.13.0b1-2268289/bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.12x