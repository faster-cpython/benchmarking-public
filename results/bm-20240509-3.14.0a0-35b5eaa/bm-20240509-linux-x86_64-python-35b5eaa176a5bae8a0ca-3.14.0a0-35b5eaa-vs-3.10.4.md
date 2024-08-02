# Results vs. 3.10.4

- fork: python
- ref: 35b5eaa176a5bae8a0ca
- machine: linux-x86_64
- commit hash: 35b5eaa
- commit date: 2024-05-09
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 270 ms: 1.29x faster                                                  |
| chameleon      | 9.68 ms                                                | 6.87 ms: 1.41x faster                                                 |
| docutils       | 3.30 sec                                               | 2.80 sec: 1.18x faster                                                |
| html5lib       | 88.9 ms                                                | 67.0 ms: 1.33x faster                                                 |
| tornado_http   | 136 ms                                                 | 93.7 ms: 1.46x faster                                                 |
| Geometric mean | (ref)                                                  | 1.33x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 361 ms: 2.02x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 931 ms: 1.90x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 474 ms: 1.83x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 618 ms: 1.65x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.84x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.6 ms: 1.73x faster                                                 |
| float          | 117 ms                                                 | 77.1 ms: 1.52x faster                                                 |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.40x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                 |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.06 sec: 1.52x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.33x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 60.6 ms: 1.30x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 87.4 ms: 1.14x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.08x faster                                                  |
| json_loads           | 31.2 us                                                | 28.9 us: 1.08x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 161 ms: 1.04x faster                                                  |
| pickle_list          | 5.08 us                                                | 5.20 us: 1.02x slower                                                 |
| unpickle_list        | 5.20 us                                                | 5.47 us: 1.05x slower                                                 |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                                 |
| unpickle             | 14.4 us                                                | 15.9 us: 1.10x slower                                                 |
| pickle_dict          | 29.6 us                                                | 33.9 us: 1.15x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.4 ms: 1.41x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.6 ms: 1.54x faster                                                 |
| django_template | 48.2 ms                                                | 33.8 ms: 1.43x faster                                                 |
| genshi_text     | 31.8 ms                                                | 23.4 ms: 1.36x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 50.9 ms: 1.30x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.29x faster                                                  |
| generators               | 80.1 ms                                                | 29.4 ms: 2.72x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.24 ms: 2.44x faster                                                 |
| async_tree_none          | 728 ms                                                 | 361 ms: 2.02x faster                                                  |
| chaos                    | 115 ms                                                 | 60.0 ms: 1.92x faster                                                 |
| raytrace                 | 507 ms                                                 | 265 ms: 1.91x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 931 ms: 1.90x faster                                                  |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 474 ms: 1.83x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 505 ms: 1.83x faster                                                  |
| richards_super           | 94.7 ms                                                | 53.8 ms: 1.76x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                 |
| pylint                   | 551 ms                                                 | 317 ms: 1.74x faster                                                  |
| nbody                    | 154 ms                                                 | 88.6 ms: 1.73x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 68.3 ms: 1.73x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 73.9 ms: 1.73x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.11 ms: 1.70x faster                                                 |
| scimark_sor              | 220 ms                                                 | 131 ms: 1.68x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                 |
| go                       | 240 ms                                                 | 143 ms: 1.68x faster                                                  |
| richards                 | 79.3 ms                                                | 47.9 ms: 1.66x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 618 ms: 1.65x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                                  |
| mako                     | 16.3 ms                                                | 10.6 ms: 1.54x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.06 sec: 1.52x faster                                                |
| float                    | 117 ms                                                 | 77.1 ms: 1.52x faster                                                 |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                  |
| pyflate                  | 716 ms                                                 | 474 ms: 1.51x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 39.3 us: 1.49x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.49x faster                                                 |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.48x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.68 us: 1.46x faster                                                 |
| tornado_http             | 136 ms                                                 | 93.7 ms: 1.46x faster                                                 |
| logging_format           | 9.09 us                                                | 6.30 us: 1.44x faster                                                 |
| django_template          | 48.2 ms                                                | 33.8 ms: 1.43x faster                                                 |
| chameleon                | 9.68 ms                                                | 6.87 ms: 1.41x faster                                                 |
| python_startup           | 14.6 ms                                                | 10.4 ms: 1.41x faster                                                 |
| regex_compile            | 188 ms                                                 | 134 ms: 1.40x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                |
| genshi_text              | 31.8 ms                                                | 23.4 ms: 1.36x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                                |
| fannkuch                 | 532 ms                                                 | 398 ms: 1.34x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.33x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 766 ms: 1.33x faster                                                  |
| html5lib                 | 88.9 ms                                                | 67.0 ms: 1.33x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.32x faster                                                |
| deepcopy                 | 479 us                                                 | 366 us: 1.31x faster                                                  |
| thrift                   | 1.07 ms                                                | 819 us: 1.31x faster                                                  |
| nqueens                  | 106 ms                                                 | 81.0 ms: 1.31x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 60.6 ms: 1.30x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 50.9 ms: 1.30x faster                                                 |
| 2to3                     | 348 ms                                                 | 270 ms: 1.29x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 65.6 ms: 1.29x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 54.8 ms: 1.26x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 20.4 ms: 1.26x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 3.31 us: 1.26x faster                                                 |
| sympy_sum                | 196 ms                                                 | 156 ms: 1.26x faster                                                  |
| scimark_fft              | 466 ms                                                 | 372 ms: 1.25x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.17 ms: 1.25x faster                                                 |
| sympy_str                | 346 ms                                                 | 282 ms: 1.23x faster                                                  |
| sympy_expand             | 566 ms                                                 | 471 ms: 1.20x faster                                                  |
| dask                     | 441 ms                                                 | 370 ms: 1.19x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 832 us: 1.19x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.80 sec: 1.18x faster                                                |
| pathlib                  | 20.5 ms                                                | 17.6 ms: 1.16x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 87.4 ms: 1.14x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                 |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.08x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.63 sec: 1.08x faster                                                |
| json_loads               | 31.2 us                                                | 28.9 us: 1.08x faster                                                 |
| json                     | 5.69 ms                                                | 5.44 ms: 1.05x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 161 ms: 1.04x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.95 us: 1.03x faster                                                 |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                                  |
| bench_mp_pool            | 24.0 ms                                                | 23.7 ms: 1.01x faster                                                 |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 563 ms: 1.01x slower                                                  |
| async_generators         | 444 ms                                                 | 448 ms: 1.01x slower                                                  |
| pickle_list              | 5.08 us                                                | 5.20 us: 1.02x slower                                                 |
| flaskblogging            | 8.58 ms                                                | 8.92 ms: 1.04x slower                                                 |
| unpickle_list            | 5.20 us                                                | 5.47 us: 1.05x slower                                                 |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                                 |
| unpickle                 | 14.4 us                                                | 15.9 us: 1.10x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.80 ms: 1.11x slower                                                 |
| pickle_dict              | 29.6 us                                                | 33.9 us: 1.15x slower                                                 |
| coverage                 | 79.4 ms                                                | 93.4 ms: 1.18x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                 |
| telco                    | 7.27 ms                                                | 176 ms: 24.25x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (2): gc_traversal, regex_effbot
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240509-3.14.0a0-35b5eaa/bm-20240509-linux-x86_64-python-35b5eaa176a5bae8a0ca-3.14.0a0-35b5eaa.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.10x