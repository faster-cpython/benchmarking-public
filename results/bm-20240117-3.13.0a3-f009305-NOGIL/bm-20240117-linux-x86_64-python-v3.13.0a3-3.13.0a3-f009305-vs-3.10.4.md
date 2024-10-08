# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.15x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 290 ms: 1.20x faster                                       |
| chameleon      | 9.68 ms                                                | 7.87 ms: 1.23x faster                                      |
| docutils       | 3.30 sec                                               | 2.95 sec: 1.12x faster                                     |
| html5lib       | 88.9 ms                                                | 70.5 ms: 1.26x faster                                      |
| tornado_http   | 136 ms                                                 | 102 ms: 1.34x faster                                       |
| Geometric mean | (ref)                                                  | 1.23x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 533 ms: 1.37x faster                                       |
| async_tree_memoization  | 870 ms                                                 | 704 ms: 1.24x faster                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 838 ms: 1.21x faster                                       |
| async_tree_io           | 1.77 sec                                               | 1.49 sec: 1.19x faster                                     |
| Geometric mean          | (ref)                                                  | 1.25x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 154 ms                                                 | 105 ms: 1.46x faster                                       |
| float          | 117 ms                                                 | 88.3 ms: 1.33x faster                                      |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                       |
| Geometric mean | (ref)                                                  | 1.26x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 139 ms: 1.36x faster                                       |
| regex_v8       | 27.8 ms                                                | 23.7 ms: 1.17x faster                                      |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                       |
| regex_effbot   | 3.63 ms                                                | 3.52 ms: 1.03x faster                                      |
| Geometric mean | (ref)                                                  | 1.14x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                       |
| unpickle_pure_python | 331 us                                                 | 234 us: 1.41x faster                                       |
| tomli_loads          | 3.14 sec                                               | 2.24 sec: 1.40x faster                                     |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.29x faster                                      |
| xml_etree_process    | 79.1 ms                                                | 65.4 ms: 1.21x faster                                      |
| json_loads           | 31.2 us                                                | 29.3 us: 1.06x faster                                      |
| xml_etree_generate   | 99.4 ms                                                | 94.2 ms: 1.06x faster                                      |
| pickle_list          | 5.08 us                                                | 4.87 us: 1.04x faster                                      |
| unpickle_list        | 5.20 us                                                | 4.99 us: 1.04x faster                                      |
| xml_etree_iterparse  | 115 ms                                                 | 114 ms: 1.02x faster                                       |
| pickle               | 10.7 us                                                | 10.6 us: 1.01x faster                                      |
| xml_etree_parse      | 168 ms                                                 | 172 ms: 1.02x slower                                       |
| unpickle             | 14.4 us                                                | 15.8 us: 1.10x slower                                      |
| pickle_dict          | 29.6 us                                                | 33.2 us: 1.12x slower                                      |
| Geometric mean       | (ref)                                                  | 1.12x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.1 ms: 1.21x faster                                      |
| python_startup_no_site | 5.93 ms                                                | 10.5 ms: 1.77x slower                                      |
| Geometric mean         | (ref)                                                  | 1.21x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 16.3 ms                                                | 12.0 ms: 1.36x faster                                      |
| genshi_text     | 31.8 ms                                                | 24.6 ms: 1.29x faster                                      |
| django_template | 48.2 ms                                                | 37.3 ms: 1.29x faster                                      |
| genshi_xml      | 66.0 ms                                                | 55.0 ms: 1.20x faster                                      |
| Geometric mean  | (ref)                                                  | 1.28x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 124 us: 4.40x faster                                       |
| generators               | 80.1 ms                                                | 32.3 ms: 2.48x faster                                      |
| deltablue                | 7.91 ms                                                | 3.56 ms: 2.23x faster                                      |
| asyncio_tcp              | 922 ms                                                 | 510 ms: 1.81x faster                                       |
| chaos                    | 115 ms                                                 | 65.2 ms: 1.77x faster                                      |
| raytrace                 | 507 ms                                                 | 291 ms: 1.74x faster                                       |
| crypto_pyaes             | 128 ms                                                 | 74.5 ms: 1.72x faster                                      |
| logging_silent           | 190 ns                                                 | 111 ns: 1.71x faster                                       |
| richards_super           | 94.7 ms                                                | 56.0 ms: 1.69x faster                                      |
| pylint                   | 551 ms                                                 | 335 ms: 1.64x faster                                       |
| scimark_sor              | 220 ms                                                 | 134 ms: 1.64x faster                                       |
| comprehensions           | 28.8 us                                                | 17.7 us: 1.63x faster                                      |
| go                       | 240 ms                                                 | 149 ms: 1.61x faster                                       |
| richards                 | 79.3 ms                                                | 49.6 ms: 1.60x faster                                      |
| scimark_monte_carlo      | 118 ms                                                 | 74.0 ms: 1.60x faster                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.36 ms: 1.59x faster                                      |
| hexiom                   | 10.4 ms                                                | 6.64 ms: 1.57x faster                                      |
| pyflate                  | 716 ms                                                 | 469 ms: 1.53x faster                                       |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.71 ms: 1.51x faster                                      |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.50x faster                                       |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.49x faster                                      |
| scimark_lu               | 176 ms                                                 | 120 ms: 1.47x faster                                       |
| nbody                    | 154 ms                                                 | 105 ms: 1.46x faster                                       |
| unpickle_pure_python     | 331 us                                                 | 234 us: 1.41x faster                                       |
| tomli_loads              | 3.14 sec                                               | 2.24 sec: 1.40x faster                                     |
| deepcopy_memo            | 58.5 us                                                | 42.4 us: 1.38x faster                                      |
| async_tree_none          | 728 ms                                                 | 533 ms: 1.37x faster                                       |
| mako                     | 16.3 ms                                                | 12.0 ms: 1.36x faster                                      |
| regex_compile            | 188 ms                                                 | 139 ms: 1.36x faster                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.90 sec: 1.35x faster                                     |
| tornado_http             | 136 ms                                                 | 102 ms: 1.34x faster                                       |
| logging_simple           | 8.30 us                                                | 6.26 us: 1.33x faster                                      |
| float                    | 117 ms                                                 | 88.3 ms: 1.33x faster                                      |
| logging_format           | 9.09 us                                                | 6.96 us: 1.31x faster                                      |
| deepcopy                 | 479 us                                                 | 368 us: 1.30x faster                                       |
| genshi_text              | 31.8 ms                                                | 24.6 ms: 1.29x faster                                      |
| django_template          | 48.2 ms                                                | 37.3 ms: 1.29x faster                                      |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.29x faster                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.26 ms: 1.29x faster                                      |
| pprint_pformat           | 2.10 sec                                               | 1.64 sec: 1.29x faster                                     |
| pprint_safe_repr         | 1.02 sec                                               | 796 ms: 1.28x faster                                       |
| deepcopy_reduce          | 4.17 us                                                | 3.27 us: 1.27x faster                                      |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                       |
| html5lib                 | 88.9 ms                                                | 70.5 ms: 1.26x faster                                      |
| nqueens                  | 106 ms                                                 | 85.2 ms: 1.24x faster                                      |
| async_tree_memoization   | 870 ms                                                 | 704 ms: 1.24x faster                                       |
| dulwich_log              | 84.3 ms                                                | 68.4 ms: 1.23x faster                                      |
| chameleon                | 9.68 ms                                                | 7.87 ms: 1.23x faster                                      |
| pycparser                | 1.58 sec                                               | 1.29 sec: 1.23x faster                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 838 ms: 1.21x faster                                       |
| xml_etree_process        | 79.1 ms                                                | 65.4 ms: 1.21x faster                                      |
| python_startup           | 14.6 ms                                                | 12.1 ms: 1.21x faster                                      |
| sqlglot_optimize         | 69.2 ms                                                | 57.3 ms: 1.21x faster                                      |
| 2to3                     | 348 ms                                                 | 290 ms: 1.20x faster                                       |
| genshi_xml               | 66.0 ms                                                | 55.0 ms: 1.20x faster                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.42 ms: 1.19x faster                                      |
| scimark_fft              | 466 ms                                                 | 391 ms: 1.19x faster                                       |
| async_tree_io            | 1.77 sec                                               | 1.49 sec: 1.19x faster                                     |
| regex_v8                 | 27.8 ms                                                | 23.7 ms: 1.17x faster                                      |
| aiohttp                  | 1.44 ms                                                | 1.23 ms: 1.17x faster                                      |
| gunicorn                 | 1.53 ms                                                | 1.33 ms: 1.15x faster                                      |
| sympy_integrate          | 25.8 ms                                                | 23.0 ms: 1.12x faster                                      |
| docutils                 | 3.30 sec                                               | 2.95 sec: 1.12x faster                                     |
| pathlib                  | 20.5 ms                                                | 18.9 ms: 1.08x faster                                      |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                      |
| json_loads               | 31.2 us                                                | 29.3 us: 1.06x faster                                      |
| xml_etree_generate       | 99.4 ms                                                | 94.2 ms: 1.06x faster                                      |
| pickle_list              | 5.08 us                                                | 4.87 us: 1.04x faster                                      |
| unpickle_list            | 5.20 us                                                | 4.99 us: 1.04x faster                                      |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                       |
| meteor_contest           | 120 ms                                                 | 115 ms: 1.04x faster                                       |
| regex_effbot             | 3.63 ms                                                | 3.52 ms: 1.03x faster                                      |
| gc_traversal             | 3.62 ms                                                | 3.52 ms: 1.03x faster                                      |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                       |
| bench_mp_pool            | 24.0 ms                                                | 23.5 ms: 1.02x faster                                      |
| xml_etree_iterparse      | 115 ms                                                 | 114 ms: 1.02x faster                                       |
| pickle                   | 10.7 us                                                | 10.6 us: 1.01x faster                                      |
| sympy_str                | 346 ms                                                 | 342 ms: 1.01x faster                                       |
| xml_etree_parse          | 168 ms                                                 | 172 ms: 1.02x slower                                       |
| mdp                      | 2.85 sec                                               | 2.93 sec: 1.03x slower                                     |
| sqlite_synth             | 3.02 us                                                | 3.15 us: 1.04x slower                                      |
| async_generators         | 444 ms                                                 | 476 ms: 1.07x slower                                       |
| unpickle                 | 14.4 us                                                | 15.8 us: 1.10x slower                                      |
| sympy_sum                | 196 ms                                                 | 216 ms: 1.10x slower                                       |
| pickle_dict              | 29.6 us                                                | 33.2 us: 1.12x slower                                      |
| sympy_expand             | 566 ms                                                 | 644 ms: 1.14x slower                                       |
| telco                    | 7.27 ms                                                | 9.10 ms: 1.25x slower                                      |
| mypy2                    | 894 ms                                                 | 1.18 sec: 1.32x slower                                     |
| flaskblogging            | 8.58 ms                                                | 12.6 ms: 1.47x slower                                      |
| python_startup_no_site   | 5.93 ms                                                | 10.5 ms: 1.77x slower                                      |
| bench_thread_pool        | 986 us                                                 | 2.54 ms: 2.57x slower                                      |
| thrift                   | 1.07 ms                                                | 9.30 ms: 8.68x slower                                      |
| coverage                 | 79.4 ms                                                | 690 ms: 8.68x slower                                       |
| fannkuch                 | 532 ms                                                 | 4.97 sec: 9.35x slower                                     |
| Geometric mean           | (ref)                                                  | 1.15x faster                                               |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, djangocms, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240117-3.13.0a3-f009305-NOGIL/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.19x