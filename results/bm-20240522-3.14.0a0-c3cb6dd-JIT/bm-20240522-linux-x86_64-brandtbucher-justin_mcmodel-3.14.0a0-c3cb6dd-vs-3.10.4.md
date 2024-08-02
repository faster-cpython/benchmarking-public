# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-x86_64
- commit hash: c3cb6dd
- commit date: 2024-05-22
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 275 ms: 1.27x faster                                                  |
| chameleon      | 9.68 ms                                                | 7.14 ms: 1.36x faster                                                 |
| docutils       | 3.30 sec                                               | 2.90 sec: 1.14x faster                                                |
| html5lib       | 88.9 ms                                                | 66.3 ms: 1.34x faster                                                 |
| tornado_http   | 136 ms                                                 | 96.7 ms: 1.41x faster                                                 |
| Geometric mean | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 377 ms: 1.93x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 459 ms: 1.89x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 934 ms: 1.89x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 613 ms: 1.66x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.84x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.3 ms: 1.94x faster                                                 |
| float          | 117 ms                                                 | 72.2 ms: 1.62x faster                                                 |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.47x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.40x faster                                                  |
| regex_v8       | 27.8 ms                                                | 23.7 ms: 1.17x faster                                                 |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 300 us: 1.61x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.01 sec: 1.56x faster                                                |
| unpickle_pure_python | 331 us                                                 | 227 us: 1.46x faster                                                  |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 58.3 ms: 1.36x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 82.5 ms: 1.20x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.15x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 151 ms: 1.11x faster                                                  |
| json_loads           | 31.2 us                                                | 28.5 us: 1.09x faster                                                 |
| unpickle_list        | 5.20 us                                                | 5.10 us: 1.02x faster                                                 |
| pickle_list          | 5.08 us                                                | 5.10 us: 1.00x slower                                                 |
| unpickle             | 14.4 us                                                | 15.0 us: 1.05x slower                                                 |
| pickle               | 10.7 us                                                | 12.2 us: 1.14x slower                                                 |
| pickle_dict          | 29.6 us                                                | 34.8 us: 1.18x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.9 ms: 1.34x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.58 ms: 1.28x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                 |
| django_template | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                 |
| genshi_text     | 31.8 ms                                                | 24.0 ms: 1.33x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 54.3 ms: 1.22x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                                  |
| generators               | 80.1 ms                                                | 30.2 ms: 2.65x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.77 ms: 2.10x faster                                                 |
| richards_super           | 94.7 ms                                                | 46.8 ms: 2.02x faster                                                 |
| richards                 | 79.3 ms                                                | 40.2 ms: 1.97x faster                                                 |
| chaos                    | 115 ms                                                 | 59.4 ms: 1.94x faster                                                 |
| nbody                    | 154 ms                                                 | 79.3 ms: 1.94x faster                                                 |
| async_tree_none          | 728 ms                                                 | 377 ms: 1.93x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 459 ms: 1.89x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 934 ms: 1.89x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 68.2 ms: 1.87x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 63.1 ms: 1.87x faster                                                 |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 519 ms: 1.78x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.76x faster                                                 |
| logging_silent           | 190 ns                                                 | 109 ns: 1.74x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 613 ms: 1.66x faster                                                  |
| go                       | 240 ms                                                 | 145 ms: 1.66x faster                                                  |
| pyflate                  | 716 ms                                                 | 439 ms: 1.63x faster                                                  |
| float                    | 117 ms                                                 | 72.2 ms: 1.62x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                 |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.61x faster                                                  |
| spectral_norm            | 170 ms                                                 | 105 ms: 1.61x faster                                                  |
| scimark_sor              | 220 ms                                                 | 136 ms: 1.61x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.52 ms: 1.60x faster                                                 |
| pylint                   | 551 ms                                                 | 351 ms: 1.57x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.01 sec: 1.56x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 37.5 us: 1.56x faster                                                 |
| fannkuch                 | 532 ms                                                 | 363 ms: 1.47x faster                                                  |
| coroutines               | 35.1 ms                                                | 24.0 ms: 1.46x faster                                                 |
| scimark_fft              | 466 ms                                                 | 319 ms: 1.46x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 227 us: 1.46x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.44 sec: 1.46x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 703 ms: 1.45x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.74 us: 1.45x faster                                                 |
| tornado_http             | 136 ms                                                 | 96.7 ms: 1.41x faster                                                 |
| logging_format           | 9.09 us                                                | 6.47 us: 1.41x faster                                                 |
| regex_compile            | 188 ms                                                 | 135 ms: 1.40x faster                                                  |
| scimark_lu               | 176 ms                                                 | 127 ms: 1.39x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.66 ms: 1.39x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                |
| chameleon                | 9.68 ms                                                | 7.14 ms: 1.36x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 58.3 ms: 1.36x faster                                                 |
| python_startup           | 14.6 ms                                                | 10.9 ms: 1.34x faster                                                 |
| html5lib                 | 88.9 ms                                                | 66.3 ms: 1.34x faster                                                 |
| django_template          | 48.2 ms                                                | 36.0 ms: 1.34x faster                                                 |
| genshi_text              | 31.8 ms                                                | 24.0 ms: 1.33x faster                                                 |
| thrift                   | 1.07 ms                                                | 808 us: 1.33x faster                                                  |
| deepcopy                 | 479 us                                                 | 366 us: 1.31x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 3.29 us: 1.27x faster                                                 |
| 2to3                     | 348 ms                                                 | 275 ms: 1.27x faster                                                  |
| nqueens                  | 106 ms                                                 | 85.1 ms: 1.24x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 55.8 ms: 1.24x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 68.9 ms: 1.22x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 54.3 ms: 1.22x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 82.5 ms: 1.20x faster                                                 |
| dask                     | 441 ms                                                 | 375 ms: 1.18x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 23.7 ms: 1.17x faster                                                 |
| sympy_sum                | 196 ms                                                 | 168 ms: 1.17x faster                                                  |
| sympy_str                | 346 ms                                                 | 297 ms: 1.16x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 22.2 ms: 1.16x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 859 us: 1.15x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.15x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.90 sec: 1.14x faster                                                |
| sympy_expand             | 566 ms                                                 | 503 ms: 1.12x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 151 ms: 1.11x faster                                                  |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                  |
| json                     | 5.69 ms                                                | 5.16 ms: 1.10x faster                                                 |
| json_loads               | 31.2 us                                                | 28.5 us: 1.09x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.89 us: 1.05x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.76 sec: 1.03x faster                                                |
| unpickle_list            | 5.20 us                                                | 5.10 us: 1.02x faster                                                 |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                  |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                                  |
| pickle_list              | 5.08 us                                                | 5.10 us: 1.00x slower                                                 |
| asyncio_websockets       | 559 ms                                                 | 566 ms: 1.01x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 3.75 ms: 1.04x slower                                                 |
| unpickle                 | 14.4 us                                                | 15.0 us: 1.05x slower                                                 |
| async_generators         | 444 ms                                                 | 471 ms: 1.06x slower                                                  |
| flaskblogging            | 8.58 ms                                                | 9.24 ms: 1.08x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.79 ms: 1.11x slower                                                 |
| telco                    | 7.27 ms                                                | 8.13 ms: 1.12x slower                                                 |
| pickle                   | 10.7 us                                                | 12.2 us: 1.14x slower                                                 |
| coverage                 | 79.4 ms                                                | 93.3 ms: 1.17x slower                                                 |
| pickle_dict              | 29.6 us                                                | 34.8 us: 1.18x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.58 ms: 1.28x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                          |

Benchmark hidden because not significant (2): bench_mp_pool, regex_effbot
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240522-3.14.0a0-c3cb6dd-JIT/bm-20240522-linux-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-c3cb6dd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.20x