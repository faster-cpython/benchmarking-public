# Results vs. 3.10.4

- fork: gvanrossum
- ref: backoff_counter_woes
- machine: linux-x86_64
- commit hash: 4c1049b
- commit date: 2024-05-04
- overall geometric mean: 1.32x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 272 ms: 1.28x faster                                                       |
| chameleon      | 9.68 ms                                                | 7.15 ms: 1.35x faster                                                      |
| docutils       | 3.30 sec                                               | 2.83 sec: 1.16x faster                                                     |
| html5lib       | 88.9 ms                                                | 68.8 ms: 1.29x faster                                                      |
| tornado_http   | 136 ms                                                 | 94.7 ms: 1.44x faster                                                      |
| Geometric mean | (ref)                                                  | 1.30x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 370 ms: 1.97x faster                                                       |
| async_tree_io           | 1.77 sec                                               | 941 ms: 1.88x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 466 ms: 1.87x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 628 ms: 1.62x faster                                                       |
| Geometric mean          | (ref)                                                  | 1.83x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 90.4 ms: 1.70x faster                                                      |
| float          | 117 ms                                                 | 78.5 ms: 1.49x faster                                                      |
| pidigits       | 191 ms                                                 | 191 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                  | 1.36x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 137 ms: 1.38x faster                                                       |
| regex_v8       | 27.8 ms                                                | 26.0 ms: 1.07x faster                                                      |
| regex_dna      | 227 ms                                                 | 232 ms: 1.02x slower                                                       |
| regex_effbot   | 3.63 ms                                                | 3.79 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 314 us: 1.55x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 225 us: 1.47x faster                                                       |
| tomli_loads          | 3.14 sec                                               | 2.18 sec: 1.44x faster                                                     |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 61.0 ms: 1.30x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 88.1 ms: 1.13x faster                                                      |
| json_loads           | 31.2 us                                                | 27.7 us: 1.12x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 107 ms: 1.07x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 158 ms: 1.06x faster                                                       |
| pickle_list          | 5.08 us                                                | 5.00 us: 1.02x faster                                                      |
| unpickle_list        | 5.20 us                                                | 5.44 us: 1.05x slower                                                      |
| unpickle             | 14.4 us                                                | 15.3 us: 1.07x slower                                                      |
| pickle               | 10.7 us                                                | 12.0 us: 1.13x slower                                                      |
| pickle_dict          | 29.6 us                                                | 36.4 us: 1.23x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.7 ms: 1.36x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 7.21 ms: 1.22x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.7 ms: 1.52x faster                                                      |
| genshi_text     | 31.8 ms                                                | 22.8 ms: 1.39x faster                                                      |
| django_template | 48.2 ms                                                | 35.1 ms: 1.37x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 52.2 ms: 1.27x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.24x faster                                                       |
| generators               | 80.1 ms                                                | 29.3 ms: 2.74x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.29 ms: 2.41x faster                                                      |
| async_tree_none          | 728 ms                                                 | 370 ms: 1.97x faster                                                       |
| chaos                    | 115 ms                                                 | 58.9 ms: 1.96x faster                                                      |
| raytrace                 | 507 ms                                                 | 265 ms: 1.91x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 941 ms: 1.88x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 466 ms: 1.87x faster                                                       |
| logging_silent           | 190 ns                                                 | 103 ns: 1.85x faster                                                       |
| asyncio_tcp              | 922 ms                                                 | 506 ms: 1.82x faster                                                       |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.71x faster                                                       |
| pylint                   | 551 ms                                                 | 322 ms: 1.71x faster                                                       |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                      |
| nbody                    | 154 ms                                                 | 90.4 ms: 1.70x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 69.6 ms: 1.70x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.18 ms: 1.68x faster                                                      |
| richards_super           | 94.7 ms                                                | 56.4 ms: 1.68x faster                                                      |
| go                       | 240 ms                                                 | 144 ms: 1.66x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 76.9 ms: 1.66x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.64x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 628 ms: 1.62x faster                                                       |
| richards                 | 79.3 ms                                                | 50.4 ms: 1.57x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 314 us: 1.55x faster                                                       |
| spectral_norm            | 170 ms                                                 | 110 ms: 1.54x faster                                                       |
| mako                     | 16.3 ms                                                | 10.7 ms: 1.52x faster                                                      |
| pyflate                  | 716 ms                                                 | 474 ms: 1.51x faster                                                       |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.50x faster                                                      |
| float                    | 117 ms                                                 | 78.5 ms: 1.49x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 225 us: 1.47x faster                                                       |
| scimark_lu               | 176 ms                                                 | 120 ms: 1.46x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 40.2 us: 1.45x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 2.18 sec: 1.44x faster                                                     |
| tornado_http             | 136 ms                                                 | 94.7 ms: 1.44x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.82 us: 1.43x faster                                                      |
| logging_format           | 9.09 us                                                | 6.46 us: 1.41x faster                                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.84 sec: 1.39x faster                                                     |
| genshi_text              | 31.8 ms                                                | 22.8 ms: 1.39x faster                                                      |
| regex_compile            | 188 ms                                                 | 137 ms: 1.38x faster                                                       |
| django_template          | 48.2 ms                                                | 35.1 ms: 1.37x faster                                                      |
| python_startup           | 14.6 ms                                                | 10.7 ms: 1.36x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.36x faster                                                     |
| chameleon                | 9.68 ms                                                | 7.15 ms: 1.35x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                     |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 755 ms: 1.35x faster                                                       |
| fannkuch                 | 532 ms                                                 | 401 ms: 1.33x faster                                                       |
| deepcopy                 | 479 us                                                 | 363 us: 1.32x faster                                                       |
| thrift                   | 1.07 ms                                                | 818 us: 1.31x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 61.0 ms: 1.30x faster                                                      |
| html5lib                 | 88.9 ms                                                | 68.8 ms: 1.29x faster                                                      |
| 2to3                     | 348 ms                                                 | 272 ms: 1.28x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 3.29 us: 1.27x faster                                                      |
| nqueens                  | 106 ms                                                 | 83.4 ms: 1.27x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 52.2 ms: 1.27x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 66.6 ms: 1.27x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 20.5 ms: 1.26x faster                                                      |
| sympy_sum                | 196 ms                                                 | 156 ms: 1.26x faster                                                       |
| scimark_fft              | 466 ms                                                 | 372 ms: 1.25x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 55.5 ms: 1.25x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.29 ms: 1.22x faster                                                      |
| sympy_str                | 346 ms                                                 | 283 ms: 1.22x faster                                                       |
| aiohttp                  | 1.44 ms                                                | 1.19 ms: 1.21x faster                                                      |
| djangocms                | 38.4 us                                                | 31.9 us: 1.20x faster                                                      |
| mypy2                    | 894 ms                                                 | 744 ms: 1.20x faster                                                       |
| dask                     | 441 ms                                                 | 370 ms: 1.19x faster                                                       |
| gunicorn                 | 1.53 ms                                                | 1.29 ms: 1.19x faster                                                      |
| sympy_expand             | 566 ms                                                 | 477 ms: 1.19x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 833 us: 1.18x faster                                                       |
| pathlib                  | 20.5 ms                                                | 17.5 ms: 1.17x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.83 sec: 1.16x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 88.1 ms: 1.13x faster                                                      |
| json_loads               | 31.2 us                                                | 27.7 us: 1.12x faster                                                      |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 107 ms: 1.07x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.65 sec: 1.07x faster                                                     |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 26.0 ms: 1.07x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 158 ms: 1.06x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.90 us: 1.04x faster                                                      |
| pickle_list              | 5.08 us                                                | 5.00 us: 1.02x faster                                                      |
| bench_mp_pool            | 24.0 ms                                                | 23.9 ms: 1.01x faster                                                      |
| pidigits                 | 191 ms                                                 | 191 ms: 1.00x slower                                                       |
| asyncio_websockets       | 559 ms                                                 | 566 ms: 1.01x slower                                                       |
| regex_dna                | 227 ms                                                 | 232 ms: 1.02x slower                                                       |
| regex_effbot             | 3.63 ms                                                | 3.79 ms: 1.04x slower                                                      |
| unpickle_list            | 5.20 us                                                | 5.44 us: 1.05x slower                                                      |
| flaskblogging            | 8.58 ms                                                | 9.02 ms: 1.05x slower                                                      |
| unpickle                 | 14.4 us                                                | 15.3 us: 1.07x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 3.99 ms: 1.10x slower                                                      |
| pickle                   | 10.7 us                                                | 12.0 us: 1.13x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.84 ms: 1.14x slower                                                      |
| telco                    | 7.27 ms                                                | 8.60 ms: 1.18x slower                                                      |
| coverage                 | 79.4 ms                                                | 94.7 ms: 1.19x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.21 ms: 1.22x slower                                                      |
| pickle_dict              | 29.6 us                                                | 36.4 us: 1.23x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.32x faster                                                               |

Benchmark hidden because not significant (1): async_generators
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240504-3.13.0a6+-4c1049b/bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.11x