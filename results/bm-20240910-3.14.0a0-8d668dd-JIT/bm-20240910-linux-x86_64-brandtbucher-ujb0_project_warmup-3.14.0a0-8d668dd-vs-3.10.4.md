# Results vs. 3.10.4

- fork: brandtbucher
- ref: ujb0_project_warmup
- machine: linux-x86_64
- commit hash: 8d668dd
- commit date: 2024-09-10
- overall geometric mean: 1.32x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 289 ms: 1.21x faster                                                       |
| docutils       | 3.30 sec                                               | 3.48 sec: 1.06x slower                                                     |
| html5lib       | 88.9 ms                                                | 74.4 ms: 1.19x faster                                                      |
| tornado_http   | 136 ms                                                 | 114 ms: 1.20x faster                                                       |
| Geometric mean | (ref)                                                  | 1.13x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 338 ms: 2.15x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 423 ms: 2.06x faster                                                       |
| async_tree_io           | 1.77 sec                                               | 953 ms: 1.85x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 571 ms: 1.78x faster                                                       |
| Geometric mean          | (ref)                                                  | 1.96x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.8 ms: 1.92x faster                                                      |
| float          | 117 ms                                                 | 68.4 ms: 1.71x faster                                                      |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.50x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 151 ms: 1.25x faster                                                       |
| regex_v8       | 27.8 ms                                                | 25.8 ms: 1.08x faster                                                      |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                                       |
| regex_effbot   | 3.63 ms                                                | 3.72 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 196 us: 1.68x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                       |
| tomli_loads          | 3.14 sec                                               | 2.13 sec: 1.48x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 54.4 ms: 1.45x faster                                                      |
| json_dumps           | 14.2 ms                                                | 9.95 ms: 1.42x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 78.7 ms: 1.26x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 98.0 ms: 1.18x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                       |
| json_loads           | 31.2 us                                                | 29.7 us: 1.05x faster                                                      |
| pickle_list          | 5.08 us                                                | 5.17 us: 1.02x slower                                                      |
| unpickle             | 14.4 us                                                | 14.9 us: 1.04x slower                                                      |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                                      |
| pickle_dict          | 29.6 us                                                | 34.2 us: 1.15x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                               |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.7 ms: 1.36x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 7.15 ms: 1.20x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.86 ms: 1.66x faster                                                      |
| genshi_text     | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                      |
| django_template | 48.2 ms                                                | 40.4 ms: 1.19x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 62.3 ms: 1.06x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.30x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.38x faster                                                       |
| generators               | 80.1 ms                                                | 34.7 ms: 2.30x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.59 ms: 2.21x faster                                                      |
| async_tree_none          | 728 ms                                                 | 338 ms: 2.15x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 27.3 us: 2.15x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 423 ms: 2.06x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 58.8 ms: 2.01x faster                                                      |
| chaos                    | 115 ms                                                 | 59.9 ms: 1.93x faster                                                      |
| nbody                    | 154 ms                                                 | 79.8 ms: 1.92x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 67.2 ms: 1.90x faster                                                      |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 953 ms: 1.85x faster                                                       |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                       |
| raytrace                 | 507 ms                                                 | 281 ms: 1.80x faster                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 571 ms: 1.78x faster                                                       |
| asyncio_tcp              | 922 ms                                                 | 525 ms: 1.76x faster                                                       |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                      |
| float                    | 117 ms                                                 | 68.4 ms: 1.71x faster                                                      |
| deepcopy                 | 479 us                                                 | 280 us: 1.71x faster                                                       |
| richards_super           | 94.7 ms                                                | 55.8 ms: 1.70x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 196 us: 1.68x faster                                                       |
| mako                     | 16.3 ms                                                | 9.86 ms: 1.66x faster                                                      |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                       |
| pyflate                  | 716 ms                                                 | 436 ms: 1.64x faster                                                       |
| richards                 | 79.3 ms                                                | 48.3 ms: 1.64x faster                                                      |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.60x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.27 ms: 1.52x faster                                                      |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                                       |
| tomli_loads              | 3.14 sec                                               | 2.13 sec: 1.48x faster                                                     |
| coroutines               | 35.1 ms                                                | 24.1 ms: 1.45x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 54.4 ms: 1.45x faster                                                      |
| json_dumps               | 14.2 ms                                                | 9.95 ms: 1.42x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.83 us: 1.42x faster                                                      |
| fannkuch                 | 532 ms                                                 | 376 ms: 1.41x faster                                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.82 sec: 1.41x faster                                                     |
| logging_format           | 9.09 us                                                | 6.53 us: 1.39x faster                                                      |
| hexiom                   | 10.4 ms                                                | 7.49 ms: 1.39x faster                                                      |
| genshi_text              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                      |
| go                       | 240 ms                                                 | 176 ms: 1.36x faster                                                       |
| python_startup           | 14.6 ms                                                | 10.7 ms: 1.36x faster                                                      |
| thrift                   | 1.07 ms                                                | 809 us: 1.32x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 776 ms: 1.31x faster                                                       |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.29x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.68 ms: 1.29x faster                                                      |
| nqueens                  | 106 ms                                                 | 83.3 ms: 1.27x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.66 sec: 1.26x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 78.7 ms: 1.26x faster                                                      |
| regex_compile            | 188 ms                                                 | 151 ms: 1.25x faster                                                       |
| sqlglot_transpile        | 2.57 ms                                                | 2.08 ms: 1.23x faster                                                      |
| pylint                   | 551 ms                                                 | 454 ms: 1.21x faster                                                       |
| 2to3                     | 348 ms                                                 | 289 ms: 1.21x faster                                                       |
| tornado_http             | 136 ms                                                 | 114 ms: 1.20x faster                                                       |
| html5lib                 | 88.9 ms                                                | 74.4 ms: 1.19x faster                                                      |
| django_template          | 48.2 ms                                                | 40.4 ms: 1.19x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 98.0 ms: 1.18x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.35 sec: 1.17x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 126 ms: 1.13x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 892 us: 1.11x faster                                                       |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                                      |
| json                     | 5.69 ms                                                | 5.25 ms: 1.08x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 64.0 ms: 1.08x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 25.8 ms: 1.08x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 62.3 ms: 1.06x faster                                                      |
| json_loads               | 31.2 us                                                | 29.7 us: 1.05x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.72 sec: 1.05x faster                                                     |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                                       |
| sympy_str                | 346 ms                                                 | 336 ms: 1.03x faster                                                       |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| sympy_expand             | 566 ms                                                 | 554 ms: 1.02x faster                                                       |
| gc_traversal             | 3.62 ms                                                | 3.55 ms: 1.02x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 25.3 ms: 1.02x faster                                                      |
| bench_mp_pool            | 24.0 ms                                                | 24.4 ms: 1.02x slower                                                      |
| pickle_list              | 5.08 us                                                | 5.17 us: 1.02x slower                                                      |
| regex_effbot             | 3.63 ms                                                | 3.72 ms: 1.03x slower                                                      |
| async_generators         | 444 ms                                                 | 457 ms: 1.03x slower                                                       |
| unpickle                 | 14.4 us                                                | 14.9 us: 1.04x slower                                                      |
| telco                    | 7.27 ms                                                | 7.62 ms: 1.05x slower                                                      |
| docutils                 | 3.30 sec                                               | 3.48 sec: 1.06x slower                                                     |
| sympy_sum                | 196 ms                                                 | 209 ms: 1.06x slower                                                       |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                                      |
| coverage                 | 79.4 ms                                                | 86.8 ms: 1.09x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                      |
| pickle_dict              | 29.6 us                                                | 34.2 us: 1.15x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.15 ms: 1.20x slower                                                      |
| unpack_sequence          | 60.0 ns                                                | 105 ns: 1.75x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.32x faster                                                               |

Benchmark hidden because not significant (2): asyncio_websockets, unpickle_list
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240910-3.14.0a0-8d668dd-JIT/bm-20240910-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-8d668dd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.31x