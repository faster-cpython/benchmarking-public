# Results vs. 3.10.4

- fork: brandtbucher
- ref: exits
- machine: linux-x86_64
- commit hash: 345fc71
- commit date: 2024-05-04
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 279 ms: 1.25x faster                                          |
| chameleon      | 9.68 ms                                                | 7.16 ms: 1.35x faster                                         |
| html5lib       | 88.9 ms                                                | 69.7 ms: 1.28x faster                                         |
| tornado_http   | 136 ms                                                 | 97.4 ms: 1.40x faster                                         |
| Geometric mean | (ref)                                                  | 1.32x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 365 ms: 2.00x faster                                          |
| async_tree_io           | 1.77 sec                                               | 935 ms: 1.89x faster                                          |
| async_tree_memoization  | 870 ms                                                 | 480 ms: 1.81x faster                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 617 ms: 1.65x faster                                          |
| Geometric mean          | (ref)                                                  | 1.83x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.4 ms: 1.89x faster                                         |
| float          | 117 ms                                                 | 72.6 ms: 1.61x faster                                         |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                  | 1.45x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 140 ms: 1.35x faster                                          |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                         |
| regex_dna      | 227 ms                                                 | 226 ms: 1.00x faster                                          |
| regex_effbot   | 3.63 ms                                                | 3.77 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                  | 1.09x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                        |
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                          |
| unpickle_pure_python | 331 us                                                 | 221 us: 1.50x faster                                          |
| xml_etree_process    | 79.1 ms                                                | 58.7 ms: 1.35x faster                                         |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                         |
| xml_etree_generate   | 99.4 ms                                                | 84.4 ms: 1.18x faster                                         |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.14x faster                                          |
| json_loads           | 31.2 us                                                | 27.8 us: 1.12x faster                                         |
| xml_etree_parse      | 168 ms                                                 | 151 ms: 1.11x faster                                          |
| pickle               | 10.7 us                                                | 11.9 us: 1.12x slower                                         |
| unpickle             | 14.4 us                                                | 16.2 us: 1.13x slower                                         |
| pickle_dict          | 29.6 us                                                | 33.9 us: 1.15x slower                                         |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                  |

Benchmark hidden because not significant (2): unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.2 ms: 1.30x faster                                         |
| python_startup_no_site | 5.93 ms                                                | 7.69 ms: 1.30x slower                                         |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.45 ms: 1.73x faster                                         |
| genshi_text     | 31.8 ms                                                | 24.1 ms: 1.32x faster                                         |
| django_template | 48.2 ms                                                | 36.7 ms: 1.31x faster                                         |
| genshi_xml      | 66.0 ms                                                | 59.4 ms: 1.11x faster                                         |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 178 us: 3.06x faster                                          |
| generators               | 80.1 ms                                                | 29.9 ms: 2.68x faster                                         |
| deltablue                | 7.91 ms                                                | 3.75 ms: 2.11x faster                                         |
| chaos                    | 115 ms                                                 | 57.4 ms: 2.01x faster                                         |
| async_tree_none          | 728 ms                                                 | 365 ms: 2.00x faster                                          |
| richards_super           | 94.7 ms                                                | 49.0 ms: 1.94x faster                                         |
| async_tree_io            | 1.77 sec                                               | 935 ms: 1.89x faster                                          |
| nbody                    | 154 ms                                                 | 81.4 ms: 1.89x faster                                         |
| raytrace                 | 507 ms                                                 | 272 ms: 1.86x faster                                          |
| richards                 | 79.3 ms                                                | 42.9 ms: 1.85x faster                                         |
| scimark_monte_carlo      | 118 ms                                                 | 64.0 ms: 1.85x faster                                         |
| crypto_pyaes             | 128 ms                                                 | 70.3 ms: 1.82x faster                                         |
| async_tree_memoization   | 870 ms                                                 | 480 ms: 1.81x faster                                          |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                          |
| asyncio_tcp              | 922 ms                                                 | 523 ms: 1.76x faster                                          |
| spectral_norm            | 170 ms                                                 | 97.4 ms: 1.74x faster                                         |
| mako                     | 16.3 ms                                                | 9.45 ms: 1.73x faster                                         |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                         |
| scimark_sor              | 220 ms                                                 | 132 ms: 1.67x faster                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 617 ms: 1.65x faster                                          |
| go                       | 240 ms                                                 | 147 ms: 1.63x faster                                          |
| float                    | 117 ms                                                 | 72.6 ms: 1.61x faster                                         |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                        |
| pyflate                  | 716 ms                                                 | 445 ms: 1.61x faster                                          |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                          |
| hexiom                   | 10.4 ms                                                | 6.57 ms: 1.58x faster                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                         |
| deepcopy_memo            | 58.5 us                                                | 37.6 us: 1.56x faster                                         |
| pylint                   | 551 ms                                                 | 355 ms: 1.55x faster                                          |
| unpickle_pure_python     | 331 us                                                 | 221 us: 1.50x faster                                          |
| fannkuch                 | 532 ms                                                 | 357 ms: 1.49x faster                                          |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.47x faster                                         |
| scimark_fft              | 466 ms                                                 | 318 ms: 1.47x faster                                          |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                        |
| scimark_lu               | 176 ms                                                 | 124 ms: 1.42x faster                                          |
| pprint_safe_repr         | 1.02 sec                                               | 721 ms: 1.41x faster                                          |
| tornado_http             | 136 ms                                                 | 97.4 ms: 1.40x faster                                         |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.69 ms: 1.38x faster                                         |
| logging_simple           | 8.30 us                                                | 6.06 us: 1.37x faster                                         |
| logging_format           | 9.09 us                                                | 6.70 us: 1.36x faster                                         |
| chameleon                | 9.68 ms                                                | 7.16 ms: 1.35x faster                                         |
| xml_etree_process        | 79.1 ms                                                | 58.7 ms: 1.35x faster                                         |
| regex_compile            | 188 ms                                                 | 140 ms: 1.35x faster                                          |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                         |
| genshi_text              | 31.8 ms                                                | 24.1 ms: 1.32x faster                                         |
| thrift                   | 1.07 ms                                                | 816 us: 1.31x faster                                          |
| django_template          | 48.2 ms                                                | 36.7 ms: 1.31x faster                                         |
| python_startup           | 14.6 ms                                                | 11.2 ms: 1.30x faster                                         |
| pycparser                | 1.58 sec                                               | 1.22 sec: 1.29x faster                                        |
| deepcopy                 | 479 us                                                 | 372 us: 1.29x faster                                          |
| html5lib                 | 88.9 ms                                                | 69.7 ms: 1.28x faster                                         |
| 2to3                     | 348 ms                                                 | 279 ms: 1.25x faster                                          |
| sqlglot_normalize        | 143 ms                                                 | 115 ms: 1.25x faster                                          |
| deepcopy_reduce          | 4.17 us                                                | 3.37 us: 1.24x faster                                         |
| nqueens                  | 106 ms                                                 | 86.3 ms: 1.23x faster                                         |
| sqlglot_optimize         | 69.2 ms                                                | 56.9 ms: 1.22x faster                                         |
| dulwich_log              | 84.3 ms                                                | 70.2 ms: 1.20x faster                                         |
| djangocms                | 38.4 us                                                | 32.2 us: 1.19x faster                                         |
| xml_etree_generate       | 99.4 ms                                                | 84.4 ms: 1.18x faster                                         |
| dask                     | 441 ms                                                 | 378 ms: 1.16x faster                                          |
| sympy_str                | 346 ms                                                 | 301 ms: 1.15x faster                                          |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                          |
| pathlib                  | 20.5 ms                                                | 17.8 ms: 1.15x faster                                         |
| sympy_integrate          | 25.8 ms                                                | 22.6 ms: 1.14x faster                                         |
| aiohttp                  | 1.44 ms                                                | 1.26 ms: 1.14x faster                                         |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.14x faster                                          |
| gunicorn                 | 1.53 ms                                                | 1.36 ms: 1.13x faster                                         |
| json_loads               | 31.2 us                                                | 27.8 us: 1.12x faster                                         |
| json                     | 5.69 ms                                                | 5.07 ms: 1.12x faster                                         |
| bench_thread_pool        | 986 us                                                 | 880 us: 1.12x faster                                          |
| sympy_expand             | 566 ms                                                 | 506 ms: 1.12x faster                                          |
| xml_etree_parse          | 168 ms                                                 | 151 ms: 1.11x faster                                          |
| genshi_xml               | 66.0 ms                                                | 59.4 ms: 1.11x faster                                         |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                          |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                         |
| mypy2                    | 894 ms                                                 | 822 ms: 1.09x faster                                          |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.07x faster                                         |
| mdp                      | 2.85 sec                                               | 2.82 sec: 1.01x faster                                        |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                          |
| regex_dna                | 227 ms                                                 | 226 ms: 1.00x faster                                          |
| gc_traversal             | 3.62 ms                                                | 3.65 ms: 1.01x slower                                         |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.01x slower                                          |
| regex_effbot             | 3.63 ms                                                | 3.77 ms: 1.04x slower                                         |
| async_generators         | 444 ms                                                 | 470 ms: 1.06x slower                                          |
| flaskblogging            | 8.58 ms                                                | 9.37 ms: 1.09x slower                                         |
| coverage                 | 79.4 ms                                                | 88.0 ms: 1.11x slower                                         |
| pickle                   | 10.7 us                                                | 11.9 us: 1.12x slower                                         |
| telco                    | 7.27 ms                                                | 8.18 ms: 1.13x slower                                         |
| unpickle                 | 14.4 us                                                | 16.2 us: 1.13x slower                                         |
| create_gc_cycles         | 1.62 ms                                                | 1.85 ms: 1.14x slower                                         |
| pickle_dict              | 29.6 us                                                | 33.9 us: 1.15x slower                                         |
| python_startup_no_site   | 5.93 ms                                                | 7.69 ms: 1.30x slower                                         |
| Geometric mean           | (ref)                                                  | 1.33x faster                                                  |

Benchmark hidden because not significant (3): unpickle_list, pickle_list, bench_mp_pool
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240504-3.13.0a6+-345fc71-JIT/bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.21x