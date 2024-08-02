# Results vs. 3.10.4

- fork: python
- ref: ec9d12be9648ee60a2eb
- machine: linux-x86_64
- commit hash: ec9d12b
- commit date: 2024-05-10
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 269 ms: 1.29x faster                                                  |
| chameleon      | 9.68 ms                                                | 7.08 ms: 1.37x faster                                                 |
| docutils       | 3.30 sec                                               | 2.81 sec: 1.17x faster                                                |
| html5lib       | 88.9 ms                                                | 68.3 ms: 1.30x faster                                                 |
| tornado_http   | 136 ms                                                 | 93.9 ms: 1.45x faster                                                 |
| Geometric mean | (ref)                                                  | 1.31x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 363 ms: 2.01x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 955 ms: 1.85x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 479 ms: 1.82x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 617 ms: 1.65x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.83x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.0 ms: 1.75x faster                                                 |
| float          | 117 ms                                                 | 78.6 ms: 1.49x faster                                                 |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.38x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.39x faster                                                  |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.10x faster                                                 |
| regex_dna      | 227 ms                                                 | 215 ms: 1.05x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.78 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 310 us: 1.56x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 220 us: 1.50x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.10 sec: 1.50x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.7 ms: 1.32x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 61.5 ms: 1.29x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 89.0 ms: 1.12x faster                                                 |
| json_loads           | 31.2 us                                                | 29.0 us: 1.08x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 108 ms: 1.07x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 163 ms: 1.03x faster                                                  |
| unpickle_list        | 5.20 us                                                | 5.34 us: 1.03x slower                                                 |
| pickle_list          | 5.08 us                                                | 5.29 us: 1.04x slower                                                 |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                                 |
| unpickle             | 14.4 us                                                | 16.1 us: 1.12x slower                                                 |
| pickle_dict          | 29.6 us                                                | 35.1 us: 1.19x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.3 ms: 1.41x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                 |
| django_template | 48.2 ms                                                | 35.1 ms: 1.37x faster                                                 |
| genshi_text     | 31.8 ms                                                | 23.7 ms: 1.34x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 51.7 ms: 1.28x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                  |
| generators               | 80.1 ms                                                | 29.3 ms: 2.73x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                                 |
| async_tree_none          | 728 ms                                                 | 363 ms: 2.01x faster                                                  |
| chaos                    | 115 ms                                                 | 60.3 ms: 1.92x faster                                                 |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 955 ms: 1.85x faster                                                  |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 479 ms: 1.82x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 510 ms: 1.81x faster                                                  |
| nbody                    | 154 ms                                                 | 88.0 ms: 1.75x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 67.9 ms: 1.74x faster                                                 |
| richards_super           | 94.7 ms                                                | 54.5 ms: 1.74x faster                                                 |
| pylint                   | 551 ms                                                 | 319 ms: 1.73x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 74.5 ms: 1.72x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                 |
| scimark_sor              | 220 ms                                                 | 130 ms: 1.69x faster                                                  |
| go                       | 240 ms                                                 | 144 ms: 1.67x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.28 ms: 1.66x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                 |
| richards                 | 79.3 ms                                                | 48.0 ms: 1.65x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 617 ms: 1.65x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 310 us: 1.56x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                 |
| pyflate                  | 716 ms                                                 | 474 ms: 1.51x faster                                                  |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 220 us: 1.50x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.10 sec: 1.50x faster                                                |
| float                    | 117 ms                                                 | 78.6 ms: 1.49x faster                                                 |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                                  |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                 |
| tornado_http             | 136 ms                                                 | 93.9 ms: 1.45x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 40.3 us: 1.45x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.77 us: 1.44x faster                                                 |
| logging_format           | 9.09 us                                                | 6.42 us: 1.42x faster                                                 |
| python_startup           | 14.6 ms                                                | 10.3 ms: 1.41x faster                                                 |
| regex_compile            | 188 ms                                                 | 135 ms: 1.39x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                |
| django_template          | 48.2 ms                                                | 35.1 ms: 1.37x faster                                                 |
| chameleon                | 9.68 ms                                                | 7.08 ms: 1.37x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.35x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                                |
| genshi_text              | 31.8 ms                                                | 23.7 ms: 1.34x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 764 ms: 1.33x faster                                                  |
| fannkuch                 | 532 ms                                                 | 400 ms: 1.33x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.7 ms: 1.32x faster                                                 |
| nqueens                  | 106 ms                                                 | 80.3 ms: 1.32x faster                                                 |
| deepcopy                 | 479 us                                                 | 366 us: 1.31x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                  |
| thrift                   | 1.07 ms                                                | 820 us: 1.31x faster                                                  |
| html5lib                 | 88.9 ms                                                | 68.3 ms: 1.30x faster                                                 |
| 2to3                     | 348 ms                                                 | 269 ms: 1.29x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 61.5 ms: 1.29x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 65.8 ms: 1.28x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 51.7 ms: 1.28x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 3.27 us: 1.28x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.10 ms: 1.27x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 20.5 ms: 1.26x faster                                                 |
| sympy_sum                | 196 ms                                                 | 157 ms: 1.25x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 55.2 ms: 1.25x faster                                                 |
| sympy_str                | 346 ms                                                 | 279 ms: 1.24x faster                                                  |
| scimark_fft              | 466 ms                                                 | 382 ms: 1.22x faster                                                  |
| sympy_expand             | 566 ms                                                 | 469 ms: 1.21x faster                                                  |
| dask                     | 441 ms                                                 | 371 ms: 1.19x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 833 us: 1.18x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.81 sec: 1.17x faster                                                |
| pathlib                  | 20.5 ms                                                | 17.6 ms: 1.16x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 89.0 ms: 1.12x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                                |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.10x faster                                                 |
| meteor_contest           | 120 ms                                                 | 111 ms: 1.08x faster                                                  |
| json_loads               | 31.2 us                                                | 29.0 us: 1.08x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 108 ms: 1.07x faster                                                  |
| regex_dna                | 227 ms                                                 | 215 ms: 1.05x faster                                                  |
| json                     | 5.69 ms                                                | 5.44 ms: 1.05x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 163 ms: 1.03x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.94 us: 1.03x faster                                                 |
| bench_mp_pool            | 24.0 ms                                                | 23.8 ms: 1.01x faster                                                 |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                  |
| async_generators         | 444 ms                                                 | 446 ms: 1.00x slower                                                  |
| asyncio_websockets       | 559 ms                                                 | 563 ms: 1.01x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 3.67 ms: 1.01x slower                                                 |
| unpickle_list            | 5.20 us                                                | 5.34 us: 1.03x slower                                                 |
| regex_effbot             | 3.63 ms                                                | 3.78 ms: 1.04x slower                                                 |
| pickle_list              | 5.08 us                                                | 5.29 us: 1.04x slower                                                 |
| flaskblogging            | 8.58 ms                                                | 8.94 ms: 1.04x slower                                                 |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.80 ms: 1.11x slower                                                 |
| unpickle                 | 14.4 us                                                | 16.1 us: 1.12x slower                                                 |
| coverage                 | 79.4 ms                                                | 93.8 ms: 1.18x slower                                                 |
| pickle_dict              | 29.6 us                                                | 35.1 us: 1.19x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                 |
| telco                    | 7.27 ms                                                | 173 ms: 23.85x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                          |
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240510-3.14.0a0-ec9d12b/bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.11x