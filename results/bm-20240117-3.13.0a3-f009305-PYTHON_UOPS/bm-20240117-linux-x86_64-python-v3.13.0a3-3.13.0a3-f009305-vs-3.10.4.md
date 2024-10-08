
# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 282 ms: 1.24x faster                                       |
| chameleon      | 9.68 ms                                                | 7.24 ms: 1.34x faster                                      |
| docutils       | 3.30 sec                                               | 2.71 sec: 1.22x faster                                     |
| tornado_http   | 136 ms                                                 | 97.8 ms: 1.39x faster                                      |
| Geometric mean | (ref)                                                  | 1.29x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 448 ms: 1.63x faster                                       |
| async_tree_memoization  | 870 ms                                                 | 574 ms: 1.51x faster                                       |
| async_tree_io           | 1.77 sec                                               | 1.20 sec: 1.47x faster                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 718 ms: 1.42x faster                                       |
| Geometric mean          | (ref)                                                  | 1.50x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 154 ms                                                 | 119 ms: 1.29x faster                                       |
| float          | 117 ms                                                 | 94.1 ms: 1.24x faster                                      |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                  | 1.17x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 153 ms: 1.23x faster                                       |
| regex_v8       | 27.8 ms                                                | 24.6 ms: 1.13x faster                                      |
| regex_dna      | 227 ms                                                 | 228 ms: 1.01x slower                                       |
| regex_effbot   | 3.63 ms                                                | 3.74 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 301 us: 1.61x faster                                       |
| unpickle_pure_python | 331 us                                                 | 234 us: 1.41x faster                                       |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                      |
| xml_etree_process    | 79.1 ms                                                | 61.1 ms: 1.30x faster                                      |
| tomli_loads          | 3.14 sec                                               | 2.61 sec: 1.20x faster                                     |
| xml_etree_generate   | 99.4 ms                                                | 89.5 ms: 1.11x faster                                      |
| json_loads           | 31.2 us                                                | 28.2 us: 1.11x faster                                      |
| xml_etree_parse      | 168 ms                                                 | 159 ms: 1.06x faster                                       |
| xml_etree_iterparse  | 115 ms                                                 | 112 ms: 1.03x faster                                       |
| unpickle_list        | 5.20 us                                                | 5.14 us: 1.01x faster                                      |
| pickle_list          | 5.08 us                                                | 5.24 us: 1.03x slower                                      |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                      |
| unpickle             | 14.4 us                                                | 16.1 us: 1.12x slower                                      |
| pickle_dict          | 29.6 us                                                | 35.0 us: 1.18x slower                                      |
| Geometric mean       | (ref)                                                  | 1.11x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.1 ms: 1.45x faster                                      |
| python_startup_no_site | 5.93 ms                                                | 8.72 ms: 1.47x slower                                      |
| Geometric mean         | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 16.3 ms                                                | 14.2 ms: 1.15x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 117 us: 4.67x faster                                       |
| generators               | 80.1 ms                                                | 29.3 ms: 2.73x faster                                      |
| asyncio_tcp              | 922 ms                                                 | 492 ms: 1.87x faster                                       |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                       |
| richards_super           | 94.7 ms                                                | 54.7 ms: 1.73x faster                                      |
| raytrace                 | 507 ms                                                 | 302 ms: 1.68x faster                                       |
| scimark_sor              | 220 ms                                                 | 134 ms: 1.64x faster                                       |
| richards                 | 79.3 ms                                                | 48.3 ms: 1.64x faster                                      |
| deltablue                | 7.91 ms                                                | 4.85 ms: 1.63x faster                                      |
| async_tree_none          | 728 ms                                                 | 448 ms: 1.63x faster                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.62x faster                                      |
| pickle_pure_python       | 484 us                                                 | 301 us: 1.61x faster                                       |
| chaos                    | 115 ms                                                 | 73.6 ms: 1.57x faster                                      |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                      |
| go                       | 240 ms                                                 | 156 ms: 1.54x faster                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.67 ms: 1.54x faster                                      |
| async_tree_memoization   | 870 ms                                                 | 574 ms: 1.51x faster                                       |
| crypto_pyaes             | 128 ms                                                 | 85.0 ms: 1.50x faster                                      |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.47x faster                                       |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.47x faster                                     |
| scimark_monte_carlo      | 118 ms                                                 | 81.4 ms: 1.45x faster                                      |
| python_startup           | 14.6 ms                                                | 10.1 ms: 1.45x faster                                      |
| deepcopy_memo            | 58.5 us                                                | 40.8 us: 1.43x faster                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                     |
| unpack_sequence          | 60.0 ns                                                | 42.4 ns: 1.42x faster                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 718 ms: 1.42x faster                                       |
| unpickle_pure_python     | 331 us                                                 | 234 us: 1.41x faster                                       |
| tornado_http             | 136 ms                                                 | 97.8 ms: 1.39x faster                                      |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                      |
| logging_simple           | 8.30 us                                                | 6.20 us: 1.34x faster                                      |
| chameleon                | 9.68 ms                                                | 7.24 ms: 1.34x faster                                      |
| pyflate                  | 716 ms                                                 | 536 ms: 1.34x faster                                       |
| deepcopy                 | 479 us                                                 | 359 us: 1.33x faster                                       |
| comprehensions           | 28.8 us                                                | 21.6 us: 1.33x faster                                      |
| deepcopy_reduce          | 4.17 us                                                | 3.15 us: 1.32x faster                                      |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                     |
| xml_etree_process        | 79.1 ms                                                | 61.1 ms: 1.30x faster                                      |
| nbody                    | 154 ms                                                 | 119 ms: 1.29x faster                                       |
| logging_format           | 9.09 us                                                | 7.07 us: 1.29x faster                                      |
| pprint_safe_repr         | 1.02 sec                                               | 816 ms: 1.25x faster                                       |
| float                    | 117 ms                                                 | 94.1 ms: 1.24x faster                                      |
| pprint_pformat           | 2.10 sec                                               | 1.70 sec: 1.24x faster                                     |
| 2to3                     | 348 ms                                                 | 282 ms: 1.24x faster                                       |
| regex_compile            | 188 ms                                                 | 153 ms: 1.23x faster                                       |
| sqlglot_normalize        | 143 ms                                                 | 116 ms: 1.23x faster                                       |
| dulwich_log              | 84.3 ms                                                | 69.0 ms: 1.22x faster                                      |
| sympy_integrate          | 25.8 ms                                                | 21.1 ms: 1.22x faster                                      |
| sympy_sum                | 196 ms                                                 | 161 ms: 1.22x faster                                       |
| docutils                 | 3.30 sec                                               | 2.71 sec: 1.22x faster                                     |
| hexiom                   | 10.4 ms                                                | 8.65 ms: 1.20x faster                                      |
| tomli_loads              | 3.14 sec                                               | 2.61 sec: 1.20x faster                                     |
| dask                     | 441 ms                                                 | 369 ms: 1.19x faster                                       |
| sqlglot_optimize         | 69.2 ms                                                | 58.4 ms: 1.18x faster                                      |
| fannkuch                 | 532 ms                                                 | 454 ms: 1.17x faster                                       |
| bench_thread_pool        | 986 us                                                 | 848 us: 1.16x faster                                       |
| mako                     | 16.3 ms                                                | 14.2 ms: 1.15x faster                                      |
| sympy_str                | 346 ms                                                 | 302 ms: 1.15x faster                                       |
| sympy_expand             | 566 ms                                                 | 495 ms: 1.14x faster                                       |
| regex_v8                 | 27.8 ms                                                | 24.6 ms: 1.13x faster                                      |
| pathlib                  | 20.5 ms                                                | 18.3 ms: 1.12x faster                                      |
| xml_etree_generate       | 99.4 ms                                                | 89.5 ms: 1.11x faster                                      |
| nqueens                  | 106 ms                                                 | 95.4 ms: 1.11x faster                                      |
| json_loads               | 31.2 us                                                | 28.2 us: 1.11x faster                                      |
| spectral_norm            | 170 ms                                                 | 154 ms: 1.10x faster                                       |
| json                     | 5.69 ms                                                | 5.19 ms: 1.10x faster                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.49 ms: 1.09x faster                                      |
| mdp                      | 2.85 sec                                               | 2.67 sec: 1.07x faster                                     |
| xml_etree_parse          | 168 ms                                                 | 159 ms: 1.06x faster                                       |
| meteor_contest           | 120 ms                                                 | 114 ms: 1.05x faster                                       |
| sqlite_synth             | 3.02 us                                                | 2.91 us: 1.04x faster                                      |
| xml_etree_iterparse      | 115 ms                                                 | 112 ms: 1.03x faster                                       |
| scimark_fft              | 466 ms                                                 | 457 ms: 1.02x faster                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.38 ms: 1.01x faster                                      |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                       |
| unpickle_list            | 5.20 us                                                | 5.14 us: 1.01x faster                                      |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                       |
| regex_dna                | 227 ms                                                 | 228 ms: 1.01x slower                                       |
| gc_traversal             | 3.62 ms                                                | 3.69 ms: 1.02x slower                                      |
| regex_effbot             | 3.63 ms                                                | 3.74 ms: 1.03x slower                                      |
| pickle_list              | 5.08 us                                                | 5.24 us: 1.03x slower                                      |
| async_generators         | 444 ms                                                 | 461 ms: 1.04x slower                                       |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                      |
| unpickle                 | 14.4 us                                                | 16.1 us: 1.12x slower                                      |
| pickle_dict              | 29.6 us                                                | 35.0 us: 1.18x slower                                      |
| telco                    | 7.27 ms                                                | 8.62 ms: 1.19x slower                                      |
| coverage                 | 79.4 ms                                                | 95.0 ms: 1.20x slower                                      |
| python_startup_no_site   | 5.93 ms                                                | 8.72 ms: 1.47x slower                                      |
| Geometric mean           | (ref)                                                  | 1.26x faster                                               |

Benchmark hidden because not significant (2): mypy2, bench_mp_pool
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (4) of results/bm-20240117-3.13.0a3-f009305-PYTHON_UOPS/bm-20240117-linux-x86_64-python-v3.13.0a3-3.13.0a3-f009305.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x


# Memory

- memory change: 1.06x