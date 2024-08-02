# Results vs. 3.10.4

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: windows-x86
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 255 ms: 1.04x faster                                                           |
| chameleon      | 6.42 ms                                                         | 6.18 ms: 1.04x faster                                                          |
| docutils       | 1.95 sec                                                        | 2.01 sec: 1.03x slower                                                         |
| html5lib       | 52.1 ms                                                         | 50.5 ms: 1.03x faster                                                          |
| tornado_http   | 118 ms                                                          | 99.3 ms: 1.18x faster                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 472 ms: 1.95x faster                                                           |
| async_tree_io           | 940 ms                                                          | 542 ms: 1.74x faster                                                           |
| async_tree_none         | 394 ms                                                          | 234 ms: 1.68x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 283 ms: 1.65x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.75x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 198 ms: 2.53x faster                                                           |
| float          | 69.6 ms                                                         | 51.9 ms: 1.34x faster                                                          |
| nbody          | 79.1 ms                                                         | 75.9 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                           | 1.52x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 131 ms                                                          | 120 ms: 1.09x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                          |
| regex_compile  | 117 ms                                                          | 123 ms: 1.06x slower                                                           |
| regex_effbot   | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.92 ms: 1.42x faster                                                          |
| tomli_loads          | 1.91 sec                                                        | 1.61 sec: 1.19x faster                                                         |
| xml_etree_parse      | 120 ms                                                          | 104 ms: 1.15x faster                                                           |
| pickle_pure_python   | 280 us                                                          | 243 us: 1.15x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 168 us: 1.13x faster                                                           |
| xml_etree_process    | 48.1 ms                                                         | 43.2 ms: 1.11x faster                                                          |
| xml_etree_iterparse  | 70.8 ms                                                         | 64.7 ms: 1.09x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.7 us: 1.08x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 60.3 ms: 1.02x faster                                                          |
| unpickle_list        | 2.98 us                                                         | 3.02 us: 1.01x slower                                                          |
| pickle               | 7.83 us                                                         | 8.17 us: 1.04x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.3 us: 1.05x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.58 us: 1.11x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.7 us: 1.14x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.1 ms                                                         | 19.1 ms: 1.06x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                                   |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 7.08 ms: 1.29x faster                                                          |
| django_template | 36.0 ms                                                         | 32.2 ms: 1.12x faster                                                          |
| genshi_text     | 21.0 ms                                                         | 21.2 ms: 1.01x slower                                                          |
| genshi_xml      | 46.6 ms                                                         | 47.7 ms: 1.02x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.09x faster                                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 149 us: 2.66x faster                                                           |
| pidigits                 | 502 ms                                                          | 198 ms: 2.53x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 472 ms: 1.95x faster                                                           |
| async_tree_io            | 940 ms                                                          | 542 ms: 1.74x faster                                                           |
| async_tree_none          | 394 ms                                                          | 234 ms: 1.68x faster                                                           |
| async_tree_memoization   | 467 ms                                                          | 283 ms: 1.65x faster                                                           |
| pylint                   | 384 ms                                                          | 244 ms: 1.58x faster                                                           |
| raytrace                 | 303 ms                                                          | 209 ms: 1.45x faster                                                           |
| deltablue                | 4.04 ms                                                         | 2.84 ms: 1.42x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 6.92 ms: 1.42x faster                                                          |
| richards_super           | 49.9 ms                                                         | 35.5 ms: 1.40x faster                                                          |
| chaos                    | 74.4 ms                                                         | 53.4 ms: 1.39x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 58.5 ms: 1.39x faster                                                          |
| generators               | 31.6 ms                                                         | 23.2 ms: 1.36x faster                                                          |
| float                    | 69.6 ms                                                         | 51.9 ms: 1.34x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 997 us: 1.33x faster                                                           |
| comprehensions           | 17.7 us                                                         | 13.3 us: 1.33x faster                                                          |
| logging_silent           | 97.9 ns                                                         | 74.1 ns: 1.32x faster                                                          |
| richards                 | 40.3 ms                                                         | 31.0 ms: 1.30x faster                                                          |
| go                       | 146 ms                                                          | 113 ms: 1.29x faster                                                           |
| mako                     | 9.10 ms                                                         | 7.08 ms: 1.29x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.24 ms: 1.27x faster                                                          |
| thrift                   | 902 us                                                          | 723 us: 1.25x faster                                                           |
| scimark_sor              | 115 ms                                                          | 93.5 ms: 1.23x faster                                                          |
| scimark_monte_carlo      | 61.9 ms                                                         | 50.8 ms: 1.22x faster                                                          |
| pycparser                | 1.04 sec                                                        | 854 ms: 1.22x faster                                                           |
| sqlite_synth             | 2.29 us                                                         | 1.92 us: 1.19x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.61 sec: 1.19x faster                                                         |
| tornado_http             | 118 ms                                                          | 99.3 ms: 1.18x faster                                                          |
| pyflate                  | 422 ms                                                          | 360 ms: 1.17x faster                                                           |
| scimark_lu               | 89.8 ms                                                         | 77.3 ms: 1.16x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 104 ms: 1.15x faster                                                           |
| pickle_pure_python       | 280 us                                                          | 243 us: 1.15x faster                                                           |
| fannkuch                 | 317 ms                                                          | 276 ms: 1.15x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 168 us: 1.13x faster                                                           |
| json                     | 4.76 ms                                                         | 4.23 ms: 1.13x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.62 sec: 1.12x faster                                                         |
| django_template          | 36.0 ms                                                         | 32.2 ms: 1.12x faster                                                          |
| xml_etree_process        | 48.1 ms                                                         | 43.2 ms: 1.11x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 72.3 ms: 1.11x faster                                                          |
| nqueens                  | 87.1 ms                                                         | 79.0 ms: 1.10x faster                                                          |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.94 ms: 1.10x faster                                                          |
| coroutines               | 17.9 ms                                                         | 16.4 ms: 1.10x faster                                                          |
| xml_etree_iterparse      | 70.8 ms                                                         | 64.7 ms: 1.09x faster                                                          |
| regex_dna                | 131 ms                                                          | 120 ms: 1.09x faster                                                           |
| json_loads               | 22.4 us                                                         | 20.7 us: 1.08x faster                                                          |
| deepcopy_memo            | 29.6 us                                                         | 27.6 us: 1.07x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 5.72 ms: 1.07x faster                                                          |
| scimark_fft              | 216 ms                                                          | 202 ms: 1.07x faster                                                           |
| bench_thread_pool        | 1.12 ms                                                         | 1.05 ms: 1.07x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.29 sec: 1.06x faster                                                         |
| asyncio_tcp              | 744 ms                                                          | 711 ms: 1.05x faster                                                           |
| pprint_safe_repr         | 658 ms                                                          | 630 ms: 1.05x faster                                                           |
| nbody                    | 79.1 ms                                                         | 75.9 ms: 1.04x faster                                                          |
| 2to3                     | 265 ms                                                          | 255 ms: 1.04x faster                                                           |
| sympy_sum                | 122 ms                                                          | 118 ms: 1.04x faster                                                           |
| chameleon                | 6.42 ms                                                         | 6.18 ms: 1.04x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 50.5 ms: 1.03x faster                                                          |
| deepcopy                 | 310 us                                                          | 301 us: 1.03x faster                                                           |
| meteor_contest           | 80.0 ms                                                         | 77.7 ms: 1.03x faster                                                          |
| sqlglot_optimize         | 44.7 ms                                                         | 43.6 ms: 1.03x faster                                                          |
| xml_etree_generate       | 61.6 ms                                                         | 60.3 ms: 1.02x faster                                                          |
| sqlglot_normalize        | 230 ms                                                          | 226 ms: 1.02x faster                                                           |
| sympy_integrate          | 16.6 ms                                                         | 16.5 ms: 1.01x faster                                                          |
| flaskblogging            | 2.03 sec                                                        | 2.03 sec: 1.00x slower                                                         |
| genshi_text              | 21.0 ms                                                         | 21.2 ms: 1.01x slower                                                          |
| unpickle_list            | 2.98 us                                                         | 3.02 us: 1.01x slower                                                          |
| regex_v8                 | 15.8 ms                                                         | 16.1 ms: 1.02x slower                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.73 us: 1.02x slower                                                          |
| genshi_xml               | 46.6 ms                                                         | 47.7 ms: 1.02x slower                                                          |
| docutils                 | 1.95 sec                                                        | 2.01 sec: 1.03x slower                                                         |
| sympy_str                | 229 ms                                                          | 238 ms: 1.04x slower                                                           |
| pickle                   | 7.83 us                                                         | 8.17 us: 1.04x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.3 us: 1.05x slower                                                          |
| logging_format           | 7.91 us                                                         | 8.32 us: 1.05x slower                                                          |
| logging_simple           | 7.29 us                                                         | 7.70 us: 1.06x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 19.1 ms: 1.06x slower                                                          |
| regex_compile            | 117 ms                                                          | 123 ms: 1.06x slower                                                           |
| coverage                 | 46.6 ms                                                         | 49.7 ms: 1.07x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 87.3 ms: 1.07x slower                                                          |
| sympy_expand             | 391 ms                                                          | 423 ms: 1.08x slower                                                           |
| create_gc_cycles         | 694 us                                                          | 758 us: 1.09x slower                                                           |
| bench_mp_pool            | 66.4 ms                                                         | 72.7 ms: 1.09x slower                                                          |
| pickle_list              | 3.22 us                                                         | 3.58 us: 1.11x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.12x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 20.7 us: 1.14x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.91 ms: 1.15x slower                                                          |
| async_generators         | 241 ms                                                          | 295 ms: 1.22x slower                                                           |
| telco                    | 4.83 ms                                                         | 6.08 ms: 1.26x slower                                                          |
| Geometric mean           | (ref)                                                           | 1.13x faster                                                                   |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, python_startup
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240511-3.14.0a0-5b941e5-PYTHON_UOPS/bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown