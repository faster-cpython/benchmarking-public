# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_compact
- machine: windows-x86
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 258 ms: 1.03x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.92 sec: 1.02x faster                                                         |
| html5lib       | 52.1 ms                                                         | 48.0 ms: 1.09x faster                                                          |
| tornado_http   | 118 ms                                                          | 97.9 ms: 1.20x faster                                                          |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 486 ms: 1.90x faster                                                           |
| async_tree_io           | 940 ms                                                          | 552 ms: 1.70x faster                                                           |
| async_tree_none         | 394 ms                                                          | 238 ms: 1.66x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 292 ms: 1.60x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.71x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 197 ms: 2.55x faster                                                           |
| float          | 69.6 ms                                                         | 42.5 ms: 1.64x faster                                                          |
| nbody          | 79.1 ms                                                         | 52.4 ms: 1.51x faster                                                          |
| Geometric mean | (ref)                                                           | 1.85x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 94.3 ms: 1.24x faster                                                          |
| regex_dna      | 131 ms                                                          | 118 ms: 1.10x faster                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.99 ms: 1.20x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.97 ms: 1.41x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 209 us: 1.34x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.46 sec: 1.31x faster                                                         |
| unpickle_pure_python | 189 us                                                          | 147 us: 1.29x faster                                                           |
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.16x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 62.0 ms: 1.14x faster                                                          |
| xml_etree_process    | 48.1 ms                                                         | 43.2 ms: 1.11x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 58.4 ms: 1.06x faster                                                          |
| json_loads           | 22.4 us                                                         | 21.4 us: 1.05x faster                                                          |
| unpickle_list        | 2.98 us                                                         | 2.86 us: 1.04x faster                                                          |
| pickle               | 7.83 us                                                         | 8.14 us: 1.04x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.8 us: 1.10x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.5 us: 1.12x slower                                                          |
| pickle_list          | 3.22 us                                                         | 4.05 us: 1.26x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.8 ms: 1.08x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 20.7 ms: 1.14x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.34 ms: 1.71x faster                                                          |
| django_template | 36.0 ms                                                         | 32.8 ms: 1.10x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 21.2 ms: 1.01x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 48.5 ms: 1.04x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 146 us: 2.72x faster                                                           |
| pidigits                 | 502 ms                                                          | 197 ms: 2.55x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 15.5 us: 1.91x faster                                                          |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 486 ms: 1.90x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 57.3 ns: 1.71x faster                                                          |
| mako                     | 9.10 ms                                                         | 5.34 ms: 1.71x faster                                                          |
| async_tree_io            | 940 ms                                                          | 552 ms: 1.70x faster                                                           |
| crypto_pyaes             | 81.3 ms                                                         | 48.0 ms: 1.69x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 48.2 ms: 1.66x faster                                                          |
| async_tree_none          | 394 ms                                                          | 238 ms: 1.66x faster                                                           |
| float                    | 69.6 ms                                                         | 42.5 ms: 1.64x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 292 ms: 1.60x faster                                                           |
| comprehensions           | 17.7 us                                                         | 11.2 us: 1.59x faster                                                          |
| pylint                   | 384 ms                                                          | 244 ms: 1.57x faster                                                           |
| nbody                    | 79.1 ms                                                         | 52.4 ms: 1.51x faster                                                          |
| pyflate                  | 422 ms                                                          | 279 ms: 1.51x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.73 ms: 1.48x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 921 us: 1.44x faster                                                           |
| hexiom                   | 6.13 ms                                                         | 4.28 ms: 1.43x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 43.6 ms: 1.42x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 6.97 ms: 1.41x faster                                                          |
| fannkuch                 | 317 ms                                                          | 228 ms: 1.39x faster                                                           |
| chaos                    | 74.4 ms                                                         | 54.2 ms: 1.37x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 209 us: 1.34x faster                                                           |
| sqlglot_transpile        | 1.58 ms                                                         | 1.18 ms: 1.34x faster                                                          |
| deepcopy                 | 310 us                                                          | 234 us: 1.32x faster                                                           |
| go                       | 146 ms                                                          | 111 ms: 1.32x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.48 ms: 1.31x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.46 sec: 1.31x faster                                                         |
| richards_super           | 49.9 ms                                                         | 38.2 ms: 1.31x faster                                                          |
| raytrace                 | 303 ms                                                          | 232 ms: 1.30x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 147 us: 1.29x faster                                                           |
| pycparser                | 1.04 sec                                                        | 823 ms: 1.27x faster                                                           |
| scimark_fft              | 216 ms                                                          | 172 ms: 1.25x faster                                                           |
| regex_compile            | 117 ms                                                          | 94.3 ms: 1.24x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 608 ms: 1.22x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 71.2 ms: 1.22x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.90 us: 1.21x faster                                                          |
| tornado_http             | 118 ms                                                          | 97.9 ms: 1.20x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 75.2 ms: 1.19x faster                                                          |
| richards                 | 40.3 ms                                                         | 33.7 ms: 1.19x faster                                                          |
| thrift                   | 902 us                                                          | 757 us: 1.19x faster                                                           |
| scimark_sor              | 115 ms                                                          | 96.9 ms: 1.19x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 964 us: 1.16x faster                                                           |
| pprint_pformat           | 1.37 sec                                                        | 1.18 sec: 1.16x faster                                                         |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.16x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 572 ms: 1.15x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 62.0 ms: 1.14x faster                                                          |
| generators               | 31.6 ms                                                         | 27.6 ms: 1.14x faster                                                          |
| sympy_sum                | 122 ms                                                          | 110 ms: 1.12x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 43.2 ms: 1.11x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.64 sec: 1.11x faster                                                         |
| regex_dna                | 131 ms                                                          | 118 ms: 1.10x faster                                                           |
| django_template          | 36.0 ms                                                         | 32.8 ms: 1.10x faster                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.47 us: 1.09x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 48.0 ms: 1.09x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 74.2 ms: 1.08x faster                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 58.4 ms: 1.06x faster                                                          |
| json_loads               | 22.4 us                                                         | 21.4 us: 1.05x faster                                                          |
| sympy_str                | 229 ms                                                          | 219 ms: 1.05x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.86 us: 1.04x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 43.0 ms: 1.04x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 16.1 ms: 1.04x faster                                                          |
| 2to3                     | 265 ms                                                          | 258 ms: 1.03x faster                                                           |
| coroutines               | 17.9 ms                                                         | 17.6 ms: 1.02x faster                                                          |
| docutils                 | 1.95 sec                                                        | 1.92 sec: 1.02x faster                                                         |
| sqlglot_normalize        | 230 ms                                                          | 233 ms: 1.01x slower                                                           |
| genshi_text              | 21.0 ms                                                         | 21.2 ms: 1.01x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.39 us: 1.01x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.05 us: 1.02x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 83.4 ms: 1.03x slower                                                          |
| pickle                   | 7.83 us                                                         | 8.14 us: 1.04x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 48.5 ms: 1.04x slower                                                          |
| python_startup           | 22.9 ms                                                         | 24.8 ms: 1.08x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 755 us: 1.09x slower                                                           |
| unpickle                 | 9.82 us                                                         | 10.8 us: 1.10x slower                                                          |
| coverage                 | 46.6 ms                                                         | 51.2 ms: 1.10x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.43 ms: 1.12x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 20.5 us: 1.12x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 75.9 ms: 1.14x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 20.7 ms: 1.14x slower                                                          |
| telco                    | 4.83 ms                                                         | 5.66 ms: 1.17x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.99 ms: 1.20x slower                                                          |
| async_generators         | 241 ms                                                          | 298 ms: 1.24x slower                                                           |
| pickle_list              | 3.22 us                                                         | 4.05 us: 1.26x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.20x faster                                                                   |

Benchmark hidden because not significant (4): asyncio_tcp_ssl, regex_v8, sympy_expand, json
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240619-3.14.0a0-e04d5ab-JIT/bm-20240619-pythonperf1_win32-x86-brandtbucher-justin_compact-3.14.0a0-e04d5ab.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown