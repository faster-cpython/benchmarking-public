# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_plt
- machine: linux-x86_64
- commit hash: 9242976
- commit date: 2024-03-15
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 285 ms: 1.22x faster                                               |
| chameleon      | 9.68 ms                                                | 6.86 ms: 1.41x faster                                              |
| docutils       | 3.30 sec                                               | 2.79 sec: 1.18x faster                                             |
| html5lib       | 88.9 ms                                                | 66.0 ms: 1.35x faster                                              |
| tornado_http   | 136 ms                                                 | 99.3 ms: 1.37x faster                                              |
| Geometric mean | (ref)                                                  | 1.30x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 450 ms: 1.62x faster                                               |
| async_tree_memoization  | 870 ms                                                 | 580 ms: 1.50x faster                                               |
| async_tree_io           | 1.77 sec                                               | 1.22 sec: 1.45x faster                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 724 ms: 1.40x faster                                               |
| Geometric mean          | (ref)                                                  | 1.49x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 97.9 ms: 1.57x faster                                              |
| float          | 117 ms                                                 | 81.5 ms: 1.44x faster                                              |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.31x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 155 ms: 1.22x faster                                               |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                              |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.92 ms: 1.08x slower                                              |
| Geometric mean | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 300 us: 1.62x faster                                               |
| tomli_loads          | 3.14 sec                                               | 2.17 sec: 1.45x faster                                             |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                              |
| unpickle_pure_python | 331 us                                                 | 246 us: 1.34x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 60.1 ms: 1.32x faster                                              |
| xml_etree_generate   | 99.4 ms                                                | 88.4 ms: 1.12x faster                                              |
| json_loads           | 31.2 us                                                | 28.1 us: 1.11x faster                                              |
| xml_etree_iterparse  | 115 ms                                                 | 109 ms: 1.06x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 160 ms: 1.05x faster                                               |
| unpickle_list        | 5.20 us                                                | 5.09 us: 1.02x faster                                              |
| pickle_list          | 5.08 us                                                | 5.19 us: 1.02x slower                                              |
| unpickle             | 14.4 us                                                | 14.8 us: 1.03x slower                                              |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                              |
| pickle_dict          | 29.6 us                                                | 34.5 us: 1.17x slower                                              |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.5 ms: 1.27x faster                                              |
| python_startup_no_site | 5.93 ms                                                | 10.1 ms: 1.70x slower                                              |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                              |
| django_template | 48.2 ms                                                | 34.6 ms: 1.39x faster                                              |
| genshi_text     | 31.8 ms                                                | 24.6 ms: 1.29x faster                                              |
| genshi_xml      | 66.0 ms                                                | 55.9 ms: 1.18x faster                                              |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 109 us: 4.97x faster                                               |
| generators               | 80.1 ms                                                | 29.8 ms: 2.69x faster                                              |
| deltablue                | 7.91 ms                                                | 3.48 ms: 2.28x faster                                              |
| logging_silent           | 190 ns                                                 | 100 ns: 1.89x faster                                               |
| asyncio_tcp              | 922 ms                                                 | 501 ms: 1.84x faster                                               |
| richards_super           | 94.7 ms                                                | 53.3 ms: 1.78x faster                                              |
| chaos                    | 115 ms                                                 | 66.9 ms: 1.72x faster                                              |
| pylint                   | 551 ms                                                 | 325 ms: 1.70x faster                                               |
| scimark_sor              | 220 ms                                                 | 130 ms: 1.68x faster                                               |
| raytrace                 | 507 ms                                                 | 303 ms: 1.67x faster                                               |
| richards                 | 79.3 ms                                                | 47.5 ms: 1.67x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 77.9 ms: 1.64x faster                                              |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                              |
| async_tree_none          | 728 ms                                                 | 450 ms: 1.62x faster                                               |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.62x faster                                               |
| comprehensions           | 28.8 us                                                | 18.3 us: 1.57x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 75.1 ms: 1.57x faster                                              |
| nbody                    | 154 ms                                                 | 97.9 ms: 1.57x faster                                              |
| sqlglot_transpile        | 2.57 ms                                                | 1.68 ms: 1.53x faster                                              |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                              |
| go                       | 240 ms                                                 | 159 ms: 1.51x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 38.9 us: 1.50x faster                                              |
| async_tree_memoization   | 870 ms                                                 | 580 ms: 1.50x faster                                               |
| async_tree_io            | 1.77 sec                                               | 1.22 sec: 1.45x faster                                             |
| tomli_loads              | 3.14 sec                                               | 2.17 sec: 1.45x faster                                             |
| float                    | 117 ms                                                 | 81.5 ms: 1.44x faster                                              |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                              |
| logging_simple           | 8.30 us                                                | 5.83 us: 1.42x faster                                              |
| chameleon                | 9.68 ms                                                | 6.86 ms: 1.41x faster                                              |
| logging_format           | 9.09 us                                                | 6.46 us: 1.41x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 724 ms: 1.40x faster                                               |
| pyflate                  | 716 ms                                                 | 513 ms: 1.39x faster                                               |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                             |
| django_template          | 48.2 ms                                                | 34.6 ms: 1.39x faster                                              |
| tornado_http             | 136 ms                                                 | 99.3 ms: 1.37x faster                                              |
| hexiom                   | 10.4 ms                                                | 7.60 ms: 1.37x faster                                              |
| deepcopy                 | 479 us                                                 | 351 us: 1.36x faster                                               |
| spectral_norm            | 170 ms                                                 | 125 ms: 1.36x faster                                               |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 3.08 us: 1.35x faster                                              |
| html5lib                 | 88.9 ms                                                | 66.0 ms: 1.35x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 246 us: 1.34x faster                                               |
| thrift                   | 1.07 ms                                                | 801 us: 1.34x faster                                               |
| scimark_lu               | 176 ms                                                 | 133 ms: 1.32x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 60.1 ms: 1.32x faster                                              |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.32x faster                                               |
| genshi_text              | 31.8 ms                                                | 24.6 ms: 1.29x faster                                              |
| scimark_fft              | 466 ms                                                 | 363 ms: 1.28x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 792 ms: 1.28x faster                                               |
| pycparser                | 1.58 sec                                               | 1.23 sec: 1.28x faster                                             |
| python_startup           | 14.6 ms                                                | 11.5 ms: 1.27x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.16 ms: 1.26x faster                                              |
| pprint_pformat           | 2.10 sec                                               | 1.69 sec: 1.25x faster                                             |
| fannkuch                 | 532 ms                                                 | 429 ms: 1.24x faster                                               |
| 2to3                     | 348 ms                                                 | 285 ms: 1.22x faster                                               |
| regex_compile            | 188 ms                                                 | 155 ms: 1.22x faster                                               |
| djangocms                | 38.4 us                                                | 31.8 us: 1.21x faster                                              |
| sympy_integrate          | 25.8 ms                                                | 21.4 ms: 1.21x faster                                              |
| sympy_sum                | 196 ms                                                 | 163 ms: 1.21x faster                                               |
| sqlglot_optimize         | 69.2 ms                                                | 57.6 ms: 1.20x faster                                              |
| aiohttp                  | 1.44 ms                                                | 1.21 ms: 1.19x faster                                              |
| sympy_str                | 346 ms                                                 | 290 ms: 1.19x faster                                               |
| docutils                 | 3.30 sec                                               | 2.79 sec: 1.18x faster                                             |
| dask                     | 441 ms                                                 | 373 ms: 1.18x faster                                               |
| genshi_xml               | 66.0 ms                                                | 55.9 ms: 1.18x faster                                              |
| gunicorn                 | 1.53 ms                                                | 1.30 ms: 1.18x faster                                              |
| dulwich_log              | 84.3 ms                                                | 71.8 ms: 1.17x faster                                              |
| sympy_expand             | 566 ms                                                 | 492 ms: 1.15x faster                                               |
| bench_thread_pool        | 986 us                                                 | 862 us: 1.14x faster                                               |
| nqueens                  | 106 ms                                                 | 93.2 ms: 1.14x faster                                              |
| xml_etree_generate       | 99.4 ms                                                | 88.4 ms: 1.12x faster                                              |
| json_loads               | 31.2 us                                                | 28.1 us: 1.11x faster                                              |
| pathlib                  | 20.5 ms                                                | 18.8 ms: 1.09x faster                                              |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                              |
| create_gc_cycles         | 1.62 ms                                                | 1.51 ms: 1.07x faster                                              |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                              |
| meteor_contest           | 120 ms                                                 | 112 ms: 1.07x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 109 ms: 1.06x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 160 ms: 1.05x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.89 us: 1.05x faster                                              |
| mdp                      | 2.85 sec                                               | 2.77 sec: 1.03x faster                                             |
| unpickle_list            | 5.20 us                                                | 5.09 us: 1.02x faster                                              |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                               |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 564 ms: 1.01x slower                                               |
| pickle_list              | 5.08 us                                                | 5.19 us: 1.02x slower                                              |
| unpickle                 | 14.4 us                                                | 14.8 us: 1.03x slower                                              |
| async_generators         | 444 ms                                                 | 469 ms: 1.06x slower                                               |
| regex_effbot             | 3.63 ms                                                | 3.92 ms: 1.08x slower                                              |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                              |
| gc_traversal             | 3.62 ms                                                | 4.09 ms: 1.13x slower                                              |
| pickle_dict              | 29.6 us                                                | 34.5 us: 1.17x slower                                              |
| telco                    | 7.27 ms                                                | 8.55 ms: 1.18x slower                                              |
| coverage                 | 79.4 ms                                                | 98.8 ms: 1.24x slower                                              |
| python_startup_no_site   | 5.93 ms                                                | 10.1 ms: 1.70x slower                                              |
| unpack_sequence          | 60.0 ns                                                | 122 ns: 2.03x slower                                               |
| Geometric mean           | (ref)                                                  | 1.28x faster                                                       |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240315-3.13.0a5+-9242976-JIT/bm-20240315-linux-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x


# Memory

- memory change: 1.22x