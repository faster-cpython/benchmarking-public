# Results vs. base

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: 144a6fa
- commit date: 2024-05-11
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 269 ms                                                                | 283 ms: 1.05x slower                                                    |
| chameleon      | 7.08 ms                                                               | 7.80 ms: 1.10x slower                                                   |
| docutils       | 2.81 sec                                                              | 2.89 sec: 1.03x slower                                                  |
| html5lib       | 68.3 ms                                                               | 69.6 ms: 1.02x slower                                                   |
| tornado_http   | 93.9 ms                                                               | 97.8 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg        | 981 ms                                                                | 1.01 sec: 1.03x slower                                                  |
| async_tree_cpu_io_mixed | 617 ms                                                                | 636 ms: 1.03x slower                                                    |
| async_tree_none_tg      | 349 ms                                                                | 362 ms: 1.04x slower                                                    |
| async_tree_memoization  | 479 ms                                                                | 499 ms: 1.04x slower                                                    |
| async_tree_none         | 363 ms                                                                | 382 ms: 1.05x slower                                                    |
| Geometric mean          | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (3): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                | 190 ms: 1.00x slower                                                    |
| float          | 78.6 ms                                                               | 86.7 ms: 1.10x slower                                                   |
| nbody          | 88.0 ms                                                               | 105 ms: 1.19x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.78 ms                                                               | 3.60 ms: 1.05x faster                                                   |
| regex_v8       | 25.1 ms                                                               | 24.4 ms: 1.03x faster                                                   |
| regex_dna      | 215 ms                                                                | 217 ms: 1.01x slower                                                    |
| regex_compile  | 135 ms                                                                | 144 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle             | 16.1 us                                                               | 15.2 us: 1.06x faster                                                   |
| pickle_dict          | 35.1 us                                                               | 33.9 us: 1.03x faster                                                   |
| json_loads           | 29.0 us                                                               | 29.1 us: 1.00x slower                                                   |
| json_dumps           | 10.7 ms                                                               | 10.8 ms: 1.01x slower                                                   |
| pickle_list          | 5.29 us                                                               | 5.41 us: 1.02x slower                                                   |
| xml_etree_iterparse  | 108 ms                                                                | 112 ms: 1.04x slower                                                    |
| unpickle_list        | 5.34 us                                                               | 5.55 us: 1.04x slower                                                   |
| xml_etree_generate   | 89.0 ms                                                               | 93.4 ms: 1.05x slower                                                   |
| xml_etree_process    | 61.5 ms                                                               | 65.1 ms: 1.06x slower                                                   |
| pickle_pure_python   | 310 us                                                                | 335 us: 1.08x slower                                                    |
| unpickle_pure_python | 220 us                                                                | 243 us: 1.10x slower                                                    |
| tomli_loads          | 2.10 sec                                                              | 2.34 sec: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                            |

Benchmark hidden because not significant (2): pickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 7.08 ms                                                               | 7.16 ms: 1.01x slower                                                   |
| python_startup         | 10.3 ms                                                               | 10.5 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                               | 24.8 ms: 1.05x slower                                                   |
| genshi_xml      | 51.7 ms                                                               | 55.7 ms: 1.08x slower                                                   |
| django_template | 35.1 ms                                                               | 38.2 ms: 1.09x slower                                                   |
| mako            | 11.1 ms                                                               | 12.7 ms: 1.14x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.09x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20240510-linux-x86_64-python-ec9d12be9648ee60a2eb-3.14.0a0-ec9d12b | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle                 | 16.1 us                                                               | 15.2 us: 1.06x faster                                                   |
| regex_effbot             | 3.78 ms                                                               | 3.60 ms: 1.05x faster                                                   |
| pickle_dict              | 35.1 us                                                               | 33.9 us: 1.03x faster                                                   |
| regex_v8                 | 25.1 ms                                                               | 24.4 ms: 1.03x faster                                                   |
| coverage                 | 93.8 ms                                                               | 92.7 ms: 1.01x faster                                                   |
| asyncio_tcp_ssl          | 1.85 sec                                                              | 1.85 sec: 1.00x slower                                                  |
| pidigits                 | 189 ms                                                                | 190 ms: 1.00x slower                                                    |
| create_gc_cycles         | 1.80 ms                                                               | 1.80 ms: 1.00x slower                                                   |
| json_loads               | 29.0 us                                                               | 29.1 us: 1.00x slower                                                   |
| json_dumps               | 10.7 ms                                                               | 10.8 ms: 1.01x slower                                                   |
| asyncio_websockets       | 563 ms                                                                | 567 ms: 1.01x slower                                                    |
| bench_mp_pool            | 23.8 ms                                                               | 24.0 ms: 1.01x slower                                                   |
| sqlite_synth             | 2.94 us                                                               | 2.97 us: 1.01x slower                                                   |
| regex_dna                | 215 ms                                                                | 217 ms: 1.01x slower                                                    |
| asyncio_tcp              | 510 ms                                                                | 516 ms: 1.01x slower                                                    |
| python_startup_no_site   | 7.08 ms                                                               | 7.16 ms: 1.01x slower                                                   |
| pathlib                  | 17.6 ms                                                               | 17.9 ms: 1.02x slower                                                   |
| python_startup           | 10.3 ms                                                               | 10.5 ms: 1.02x slower                                                   |
| html5lib                 | 68.3 ms                                                               | 69.6 ms: 1.02x slower                                                   |
| pickle_list              | 5.29 us                                                               | 5.41 us: 1.02x slower                                                   |
| dask                     | 371 ms                                                                | 380 ms: 1.02x slower                                                    |
| json                     | 5.44 ms                                                               | 5.57 ms: 1.02x slower                                                   |
| async_generators         | 446 ms                                                                | 458 ms: 1.03x slower                                                    |
| docutils                 | 2.81 sec                                                              | 2.89 sec: 1.03x slower                                                  |
| sympy_sum                | 157 ms                                                                | 161 ms: 1.03x slower                                                    |
| async_tree_io_tg         | 981 ms                                                                | 1.01 sec: 1.03x slower                                                  |
| async_tree_cpu_io_mixed  | 617 ms                                                                | 636 ms: 1.03x slower                                                    |
| flaskblogging            | 8.94 ms                                                               | 9.25 ms: 1.03x slower                                                   |
| mdp                      | 2.57 sec                                                              | 2.66 sec: 1.04x slower                                                  |
| xml_etree_iterparse      | 108 ms                                                                | 112 ms: 1.04x slower                                                    |
| sympy_integrate          | 20.5 ms                                                               | 21.2 ms: 1.04x slower                                                   |
| dulwich_log              | 65.8 ms                                                               | 68.3 ms: 1.04x slower                                                   |
| gc_traversal             | 3.67 ms                                                               | 3.81 ms: 1.04x slower                                                   |
| async_tree_none_tg       | 349 ms                                                                | 362 ms: 1.04x slower                                                    |
| unpickle_list            | 5.34 us                                                               | 5.55 us: 1.04x slower                                                   |
| bench_thread_pool        | 833 us                                                                | 865 us: 1.04x slower                                                    |
| meteor_contest           | 111 ms                                                                | 115 ms: 1.04x slower                                                    |
| async_tree_memoization   | 479 ms                                                                | 499 ms: 1.04x slower                                                    |
| tornado_http             | 93.9 ms                                                               | 97.8 ms: 1.04x slower                                                   |
| sympy_str                | 279 ms                                                                | 291 ms: 1.04x slower                                                    |
| thrift                   | 820 us                                                                | 856 us: 1.04x slower                                                    |
| sympy_expand             | 469 ms                                                                | 491 ms: 1.05x slower                                                    |
| genshi_text              | 23.7 ms                                                               | 24.8 ms: 1.05x slower                                                   |
| logging_format           | 6.42 us                                                               | 6.72 us: 1.05x slower                                                   |
| crypto_pyaes             | 74.5 ms                                                               | 78.1 ms: 1.05x slower                                                   |
| xml_etree_generate       | 89.0 ms                                                               | 93.4 ms: 1.05x slower                                                   |
| logging_simple           | 5.77 us                                                               | 6.06 us: 1.05x slower                                                   |
| 2to3                     | 269 ms                                                                | 283 ms: 1.05x slower                                                    |
| sqlglot_optimize         | 55.2 ms                                                               | 58.1 ms: 1.05x slower                                                   |
| async_tree_none          | 363 ms                                                                | 382 ms: 1.05x slower                                                    |
| spectral_norm            | 115 ms                                                                | 121 ms: 1.05x slower                                                    |
| xml_etree_process        | 61.5 ms                                                               | 65.1 ms: 1.06x slower                                                   |
| sqlglot_normalize        | 109 ms                                                                | 116 ms: 1.06x slower                                                    |
| regex_compile            | 135 ms                                                                | 144 ms: 1.07x slower                                                    |
| telco                    | 173 ms                                                                | 185 ms: 1.07x slower                                                    |
| scimark_lu               | 117 ms                                                                | 125 ms: 1.07x slower                                                    |
| richards                 | 48.0 ms                                                               | 51.2 ms: 1.07x slower                                                   |
| typing_runtime_protocols | 167 us                                                                | 178 us: 1.07x slower                                                    |
| generators               | 29.3 ms                                                               | 31.3 ms: 1.07x slower                                                   |
| richards_super           | 54.5 ms                                                               | 58.5 ms: 1.07x slower                                                   |
| genshi_xml               | 51.7 ms                                                               | 55.7 ms: 1.08x slower                                                   |
| logging_silent           | 104 ns                                                                | 112 ns: 1.08x slower                                                    |
| pycparser                | 1.16 sec                                                              | 1.26 sec: 1.08x slower                                                  |
| pyflate                  | 474 ms                                                                | 512 ms: 1.08x slower                                                    |
| raytrace                 | 267 ms                                                                | 289 ms: 1.08x slower                                                    |
| scimark_sor              | 130 ms                                                                | 141 ms: 1.08x slower                                                    |
| pickle_pure_python       | 310 us                                                                | 335 us: 1.08x slower                                                    |
| scimark_fft              | 382 ms                                                                | 414 ms: 1.08x slower                                                    |
| hexiom                   | 6.28 ms                                                               | 6.82 ms: 1.09x slower                                                   |
| sqlglot_transpile        | 1.62 ms                                                               | 1.76 ms: 1.09x slower                                                   |
| django_template          | 35.1 ms                                                               | 38.2 ms: 1.09x slower                                                   |
| sqlglot_parse            | 1.31 ms                                                               | 1.43 ms: 1.09x slower                                                   |
| go                       | 144 ms                                                                | 158 ms: 1.10x slower                                                    |
| deepcopy                 | 366 us                                                                | 401 us: 1.10x slower                                                    |
| deltablue                | 3.27 ms                                                               | 3.60 ms: 1.10x slower                                                   |
| deepcopy_reduce          | 3.27 us                                                               | 3.60 us: 1.10x slower                                                   |
| chameleon                | 7.08 ms                                                               | 7.80 ms: 1.10x slower                                                   |
| unpickle_pure_python     | 220 us                                                                | 243 us: 1.10x slower                                                    |
| float                    | 78.6 ms                                                               | 86.7 ms: 1.10x slower                                                   |
| chaos                    | 60.3 ms                                                               | 66.8 ms: 1.11x slower                                                   |
| nqueens                  | 80.3 ms                                                               | 89.1 ms: 1.11x slower                                                   |
| tomli_loads              | 2.10 sec                                                              | 2.34 sec: 1.11x slower                                                  |
| pprint_pformat           | 1.56 sec                                                              | 1.74 sec: 1.11x slower                                                  |
| pprint_safe_repr         | 764 ms                                                                | 853 ms: 1.12x slower                                                    |
| coroutines               | 22.8 ms                                                               | 25.5 ms: 1.12x slower                                                   |
| deepcopy_memo            | 40.3 us                                                               | 45.1 us: 1.12x slower                                                   |
| fannkuch                 | 400 ms                                                                | 449 ms: 1.12x slower                                                    |
| scimark_sparse_mat_mult  | 5.10 ms                                                               | 5.72 ms: 1.12x slower                                                   |
| comprehensions           | 16.8 us                                                               | 19.0 us: 1.13x slower                                                   |
| scimark_monte_carlo      | 67.9 ms                                                               | 76.7 ms: 1.13x slower                                                   |
| mako                     | 11.1 ms                                                               | 12.7 ms: 1.14x slower                                                   |
| nbody                    | 88.0 ms                                                               | 105 ms: 1.19x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.05x slower                                                            |

Benchmark hidden because not significant (6): pickle, xml_etree_parse, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, pylint

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.00x