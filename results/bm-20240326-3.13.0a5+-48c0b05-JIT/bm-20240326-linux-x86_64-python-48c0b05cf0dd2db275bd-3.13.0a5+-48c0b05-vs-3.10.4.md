# Results vs. 3.10.4

- fork: python
- ref: 48c0b05cf0dd2db275bd
- machine: linux-x86_64
- commit hash: 48c0b05
- commit date: 2024-03-26
- overall geometric mean: 1.31x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 276 ms: 1.26x faster                                                   |
| chameleon      | 9.68 ms                                                | 6.88 ms: 1.41x faster                                                  |
| docutils       | 3.30 sec                                               | 2.90 sec: 1.14x faster                                                 |
| html5lib       | 88.9 ms                                                | 67.8 ms: 1.31x faster                                                  |
| tornado_http   | 136 ms                                                 | 96.8 ms: 1.41x faster                                                  |
| Geometric mean | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 354 ms: 2.06x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 452 ms: 1.93x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 927 ms: 1.91x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 615 ms: 1.65x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.88x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 92.7 ms: 1.66x faster                                                  |
| float          | 117 ms                                                 | 76.7 ms: 1.53x faster                                                  |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 147 ms: 1.28x faster                                                   |
| regex_v8       | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                  |
| regex_dna      | 227 ms                                                 | 217 ms: 1.04x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 306 us: 1.58x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 241 us: 1.37x faster                                                   |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.36x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 87.0 ms: 1.14x faster                                                  |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 107 ms: 1.08x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 161 ms: 1.04x faster                                                   |
| pickle_list          | 5.08 us                                                | 4.94 us: 1.03x faster                                                  |
| unpickle_list        | 5.20 us                                                | 5.29 us: 1.02x slower                                                  |
| unpickle             | 14.4 us                                                | 15.2 us: 1.05x slower                                                  |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                                  |
| pickle_dict          | 29.6 us                                                | 34.3 us: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.0 ms: 1.32x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 9.48 ms: 1.60x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.8 ms: 1.51x faster                                                  |
| django_template | 48.2 ms                                                | 36.1 ms: 1.34x faster                                                  |
| genshi_text     | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 54.3 ms: 1.22x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 111 us: 4.90x faster                                                   |
| generators               | 80.1 ms                                                | 29.5 ms: 2.72x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.44 ms: 2.30x faster                                                  |
| async_tree_none          | 728 ms                                                 | 354 ms: 2.06x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 452 ms: 1.93x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 927 ms: 1.91x faster                                                   |
| logging_silent           | 190 ns                                                 | 104 ns: 1.83x faster                                                   |
| chaos                    | 115 ms                                                 | 63.1 ms: 1.83x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 510 ms: 1.81x faster                                                   |
| richards_super           | 94.7 ms                                                | 52.6 ms: 1.80x faster                                                  |
| raytrace                 | 507 ms                                                 | 289 ms: 1.75x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 75.0 ms: 1.70x faster                                                  |
| richards                 | 79.3 ms                                                | 46.7 ms: 1.70x faster                                                  |
| scimark_sor              | 220 ms                                                 | 131 ms: 1.68x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 71.0 ms: 1.67x faster                                                  |
| nbody                    | 154 ms                                                 | 92.7 ms: 1.66x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 615 ms: 1.65x faster                                                   |
| pylint                   | 551 ms                                                 | 335 ms: 1.65x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 306 us: 1.58x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                                  |
| comprehensions           | 28.8 us                                                | 18.4 us: 1.56x faster                                                  |
| go                       | 240 ms                                                 | 155 ms: 1.54x faster                                                   |
| float                    | 117 ms                                                 | 76.7 ms: 1.53x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                                  |
| mako                     | 16.3 ms                                                | 10.8 ms: 1.51x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                 |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.50x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 39.5 us: 1.48x faster                                                  |
| pyflate                  | 716 ms                                                 | 493 ms: 1.45x faster                                                   |
| hexiom                   | 10.4 ms                                                | 7.23 ms: 1.44x faster                                                  |
| chameleon                | 9.68 ms                                                | 6.88 ms: 1.41x faster                                                  |
| tornado_http             | 136 ms                                                 | 96.8 ms: 1.41x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.96 us: 1.39x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                 |
| logging_format           | 9.09 us                                                | 6.57 us: 1.38x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 241 us: 1.37x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.36x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 753 ms: 1.35x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                                 |
| fannkuch                 | 532 ms                                                 | 396 ms: 1.34x faster                                                   |
| django_template          | 48.2 ms                                                | 36.1 ms: 1.34x faster                                                  |
| deepcopy                 | 479 us                                                 | 360 us: 1.33x faster                                                   |
| scimark_fft              | 466 ms                                                 | 351 ms: 1.33x faster                                                   |
| thrift                   | 1.07 ms                                                | 810 us: 1.32x faster                                                   |
| python_startup           | 14.6 ms                                                | 11.0 ms: 1.32x faster                                                  |
| scimark_lu               | 176 ms                                                 | 134 ms: 1.32x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 3.17 us: 1.32x faster                                                  |
| genshi_text              | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                  |
| html5lib                 | 88.9 ms                                                | 67.8 ms: 1.31x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.02 ms: 1.29x faster                                                  |
| regex_compile            | 188 ms                                                 | 147 ms: 1.28x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                   |
| 2to3                     | 348 ms                                                 | 276 ms: 1.26x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 54.3 ms: 1.22x faster                                                  |
| sympy_sum                | 196 ms                                                 | 165 ms: 1.19x faster                                                   |
| aiohttp                  | 1.44 ms                                                | 1.21 ms: 1.19x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 58.1 ms: 1.19x faster                                                  |
| sympy_str                | 346 ms                                                 | 291 ms: 1.19x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 70.9 ms: 1.19x faster                                                  |
| djangocms                | 38.4 us                                                | 32.4 us: 1.19x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 21.8 ms: 1.19x faster                                                  |
| nqueens                  | 106 ms                                                 | 90.1 ms: 1.17x faster                                                  |
| dask                     | 441 ms                                                 | 377 ms: 1.17x faster                                                   |
| gunicorn                 | 1.53 ms                                                | 1.31 ms: 1.17x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 852 us: 1.16x faster                                                   |
| sympy_expand             | 566 ms                                                 | 491 ms: 1.15x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 87.0 ms: 1.14x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.90 sec: 1.14x faster                                                 |
| mypy2                    | 894 ms                                                 | 789 ms: 1.13x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                  |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                  |
| pathlib                  | 20.5 ms                                                | 19.0 ms: 1.08x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 107 ms: 1.08x faster                                                   |
| meteor_contest           | 120 ms                                                 | 111 ms: 1.07x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.65 sec: 1.07x faster                                                 |
| json                     | 5.69 ms                                                | 5.37 ms: 1.06x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.88 us: 1.05x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 161 ms: 1.04x faster                                                   |
| regex_dna                | 227 ms                                                 | 217 ms: 1.04x faster                                                   |
| pickle_list              | 5.08 us                                                | 4.94 us: 1.03x faster                                                  |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                   |
| unpickle_list            | 5.20 us                                                | 5.29 us: 1.02x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 3.69 ms: 1.02x slower                                                  |
| asyncio_websockets       | 559 ms                                                 | 569 ms: 1.02x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 1.67 ms: 1.03x slower                                                  |
| regex_effbot             | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                  |
| async_generators         | 444 ms                                                 | 463 ms: 1.04x slower                                                   |
| unpickle                 | 14.4 us                                                | 15.2 us: 1.05x slower                                                  |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                                  |
| pickle_dict              | 29.6 us                                                | 34.3 us: 1.16x slower                                                  |
| telco                    | 7.27 ms                                                | 8.69 ms: 1.20x slower                                                  |
| coverage                 | 79.4 ms                                                | 96.4 ms: 1.21x slower                                                  |
| unpack_sequence          | 60.0 ns                                                | 86.5 ns: 1.44x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 9.48 ms: 1.60x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.31x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240326-3.13.0a5+-48c0b05-JIT/bm-20240326-linux-x86_64-python-48c0b05cf0dd2db275bd-3.13.0a5+-48c0b05.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x


# Memory

- memory change: 1.18x