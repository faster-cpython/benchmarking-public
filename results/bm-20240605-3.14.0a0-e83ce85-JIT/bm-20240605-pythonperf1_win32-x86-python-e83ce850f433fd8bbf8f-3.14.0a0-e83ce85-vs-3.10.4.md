# Results vs. 3.10.4

- fork: python
- ref: e83ce850f433fd8bbf8f
- machine: windows-x86
- commit hash: e83ce85
- commit date: 2024-06-05
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                          | 242 ms: 1.10x faster                                                           |
| docutils       | 1.95 sec                                                        | 1.85 sec: 1.05x faster                                                         |
| html5lib       | 52.1 ms                                                         | 46.0 ms: 1.13x faster                                                          |
| tornado_http   | 118 ms                                                          | 96.4 ms: 1.22x faster                                                          |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 922 ms                                                          | 504 ms: 1.83x faster                                                           |
| async_tree_io           | 940 ms                                                          | 534 ms: 1.76x faster                                                           |
| async_tree_none         | 394 ms                                                          | 230 ms: 1.71x faster                                                           |
| async_tree_memoization  | 467 ms                                                          | 280 ms: 1.66x faster                                                           |
| Geometric mean          | (ref)                                                           | 1.74x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 502 ms                                                          | 198 ms: 2.54x faster                                                           |
| float          | 69.6 ms                                                         | 41.4 ms: 1.68x faster                                                          |
| nbody          | 79.1 ms                                                         | 52.9 ms: 1.50x faster                                                          |
| Geometric mean | (ref)                                                           | 1.85x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 117 ms                                                          | 96.7 ms: 1.21x faster                                                          |
| regex_dna      | 131 ms                                                          | 123 ms: 1.06x faster                                                           |
| regex_v8       | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                          |
| regex_effbot   | 1.66 ms                                                         | 1.98 ms: 1.19x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 9.82 ms                                                         | 6.51 ms: 1.51x faster                                                          |
| pickle_pure_python   | 280 us                                                          | 199 us: 1.41x faster                                                           |
| unpickle_pure_python | 189 us                                                          | 135 us: 1.40x faster                                                           |
| tomli_loads          | 1.91 sec                                                        | 1.43 sec: 1.34x faster                                                         |
| xml_etree_process    | 48.1 ms                                                         | 40.4 ms: 1.19x faster                                                          |
| xml_etree_parse      | 120 ms                                                          | 102 ms: 1.17x faster                                                           |
| xml_etree_iterparse  | 70.8 ms                                                         | 61.2 ms: 1.16x faster                                                          |
| xml_etree_generate   | 61.6 ms                                                         | 55.2 ms: 1.12x faster                                                          |
| json_loads           | 22.4 us                                                         | 20.7 us: 1.08x faster                                                          |
| unpickle_list        | 2.98 us                                                         | 2.90 us: 1.03x faster                                                          |
| pickle               | 7.83 us                                                         | 8.23 us: 1.05x slower                                                          |
| unpickle             | 9.82 us                                                         | 10.5 us: 1.07x slower                                                          |
| pickle_dict          | 18.2 us                                                         | 20.7 us: 1.14x slower                                                          |
| pickle_list          | 3.22 us                                                         | 3.72 us: 1.16x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.13x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.9 ms                                                         | 24.2 ms: 1.06x slower                                                          |
| python_startup_no_site | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.10 ms                                                         | 5.34 ms: 1.70x faster                                                          |
| django_template | 36.0 ms                                                         | 31.7 ms: 1.14x faster                                                          |
| genshi_xml      | 46.6 ms                                                         | 51.6 ms: 1.11x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.15x faster                                                                   |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120 | bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|--------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| typing_runtime_protocols | 396 us                                                          | 135 us: 2.92x faster                                                           |
| pidigits                 | 502 ms                                                          | 198 ms: 2.54x faster                                                           |
| async_tree_cpu_io_mixed  | 922 ms                                                          | 504 ms: 1.83x faster                                                           |
| logging_silent           | 97.9 ns                                                         | 53.9 ns: 1.82x faster                                                          |
| async_tree_io            | 940 ms                                                          | 534 ms: 1.76x faster                                                           |
| async_tree_none          | 394 ms                                                          | 230 ms: 1.71x faster                                                           |
| mako                     | 9.10 ms                                                         | 5.34 ms: 1.70x faster                                                          |
| crypto_pyaes             | 81.3 ms                                                         | 47.9 ms: 1.70x faster                                                          |
| spectral_norm            | 80.2 ms                                                         | 47.6 ms: 1.68x faster                                                          |
| float                    | 69.6 ms                                                         | 41.4 ms: 1.68x faster                                                          |
| async_tree_memoization   | 467 ms                                                          | 280 ms: 1.66x faster                                                           |
| pylint                   | 384 ms                                                          | 235 ms: 1.63x faster                                                           |
| comprehensions           | 17.7 us                                                         | 11.0 us: 1.61x faster                                                          |
| deltablue                | 4.04 ms                                                         | 2.54 ms: 1.59x faster                                                          |
| pyflate                  | 422 ms                                                          | 271 ms: 1.56x faster                                                           |
| scimark_monte_carlo      | 61.9 ms                                                         | 39.8 ms: 1.56x faster                                                          |
| json_dumps               | 9.82 ms                                                         | 6.51 ms: 1.51x faster                                                          |
| nbody                    | 79.1 ms                                                         | 52.9 ms: 1.50x faster                                                          |
| chaos                    | 74.4 ms                                                         | 50.1 ms: 1.48x faster                                                          |
| sqlglot_parse            | 1.33 ms                                                         | 900 us: 1.48x faster                                                           |
| raytrace                 | 303 ms                                                          | 205 ms: 1.47x faster                                                           |
| fannkuch                 | 317 ms                                                          | 219 ms: 1.45x faster                                                           |
| deepcopy_memo            | 29.6 us                                                         | 20.7 us: 1.43x faster                                                          |
| richards_super           | 49.9 ms                                                         | 35.1 ms: 1.42x faster                                                          |
| pickle_pure_python       | 280 us                                                          | 199 us: 1.41x faster                                                           |
| unpickle_pure_python     | 189 us                                                          | 135 us: 1.40x faster                                                           |
| scimark_sparse_mat_mult  | 3.24 ms                                                         | 2.34 ms: 1.38x faster                                                          |
| generators               | 31.6 ms                                                         | 23.0 ms: 1.37x faster                                                          |
| sqlglot_transpile        | 1.58 ms                                                         | 1.16 ms: 1.37x faster                                                          |
| hexiom                   | 6.13 ms                                                         | 4.53 ms: 1.35x faster                                                          |
| tomli_loads              | 1.91 sec                                                        | 1.43 sec: 1.34x faster                                                         |
| go                       | 146 ms                                                          | 109 ms: 1.33x faster                                                           |
| scimark_fft              | 216 ms                                                          | 164 ms: 1.31x faster                                                           |
| pycparser                | 1.04 sec                                                        | 798 ms: 1.30x faster                                                           |
| thrift                   | 902 us                                                          | 699 us: 1.29x faster                                                           |
| richards                 | 40.3 ms                                                         | 31.3 ms: 1.29x faster                                                          |
| scimark_sor              | 115 ms                                                          | 90.4 ms: 1.27x faster                                                          |
| scimark_lu               | 89.8 ms                                                         | 71.1 ms: 1.26x faster                                                          |
| asyncio_tcp              | 744 ms                                                          | 600 ms: 1.24x faster                                                           |
| nqueens                  | 87.1 ms                                                         | 70.2 ms: 1.24x faster                                                          |
| tornado_http             | 118 ms                                                          | 96.4 ms: 1.22x faster                                                          |
| sqlite_synth             | 2.29 us                                                         | 1.90 us: 1.21x faster                                                          |
| pprint_pformat           | 1.37 sec                                                        | 1.13 sec: 1.21x faster                                                         |
| regex_compile            | 117 ms                                                          | 96.7 ms: 1.21x faster                                                          |
| pprint_safe_repr         | 658 ms                                                          | 546 ms: 1.21x faster                                                           |
| xml_etree_process        | 48.1 ms                                                         | 40.4 ms: 1.19x faster                                                          |
| xml_etree_parse          | 120 ms                                                          | 102 ms: 1.17x faster                                                           |
| xml_etree_iterparse      | 70.8 ms                                                         | 61.2 ms: 1.16x faster                                                          |
| sympy_sum                | 122 ms                                                          | 106 ms: 1.15x faster                                                           |
| coroutines               | 17.9 ms                                                         | 15.7 ms: 1.14x faster                                                          |
| bench_thread_pool        | 1.12 ms                                                         | 984 us: 1.14x faster                                                           |
| django_template          | 36.0 ms                                                         | 31.7 ms: 1.14x faster                                                          |
| html5lib                 | 52.1 ms                                                         | 46.0 ms: 1.13x faster                                                          |
| json                     | 4.76 ms                                                         | 4.24 ms: 1.12x faster                                                          |
| mdp                      | 1.83 sec                                                        | 1.63 sec: 1.12x faster                                                         |
| xml_etree_generate       | 61.6 ms                                                         | 55.2 ms: 1.12x faster                                                          |
| meteor_contest           | 80.0 ms                                                         | 72.3 ms: 1.11x faster                                                          |
| sympy_str                | 229 ms                                                          | 208 ms: 1.10x faster                                                           |
| 2to3                     | 265 ms                                                          | 242 ms: 1.10x faster                                                           |
| sqlglot_optimize         | 44.7 ms                                                         | 41.3 ms: 1.08x faster                                                          |
| json_loads               | 22.4 us                                                         | 20.7 us: 1.08x faster                                                          |
| sympy_integrate          | 16.6 ms                                                         | 15.5 ms: 1.08x faster                                                          |
| regex_dna                | 131 ms                                                          | 123 ms: 1.06x faster                                                           |
| sqlglot_normalize        | 230 ms                                                          | 218 ms: 1.06x faster                                                           |
| sympy_expand             | 391 ms                                                          | 370 ms: 1.05x faster                                                           |
| docutils                 | 1.95 sec                                                        | 1.85 sec: 1.05x faster                                                         |
| deepcopy                 | 310 us                                                          | 300 us: 1.03x faster                                                           |
| unpickle_list            | 2.98 us                                                         | 2.90 us: 1.03x faster                                                          |
| asyncio_tcp_ssl          | 17.0 sec                                                        | 16.8 sec: 1.01x faster                                                         |
| regex_v8                 | 15.8 ms                                                         | 15.9 ms: 1.01x slower                                                          |
| pathlib                  | 81.2 ms                                                         | 82.4 ms: 1.01x slower                                                          |
| deepcopy_reduce          | 2.68 us                                                         | 2.74 us: 1.02x slower                                                          |
| pickle                   | 7.83 us                                                         | 8.23 us: 1.05x slower                                                          |
| python_startup           | 22.9 ms                                                         | 24.2 ms: 1.06x slower                                                          |
| unpickle                 | 9.82 us                                                         | 10.5 us: 1.07x slower                                                          |
| coverage                 | 46.6 ms                                                         | 50.6 ms: 1.09x slower                                                          |
| create_gc_cycles         | 694 us                                                          | 757 us: 1.09x slower                                                           |
| genshi_xml               | 46.6 ms                                                         | 51.6 ms: 1.11x slower                                                          |
| bench_mp_pool            | 66.4 ms                                                         | 74.1 ms: 1.12x slower                                                          |
| python_startup_no_site   | 18.1 ms                                                         | 20.2 ms: 1.12x slower                                                          |
| gc_traversal             | 1.28 ms                                                         | 1.44 ms: 1.12x slower                                                          |
| pickle_dict              | 18.2 us                                                         | 20.7 us: 1.14x slower                                                          |
| pickle_list              | 3.22 us                                                         | 3.72 us: 1.16x slower                                                          |
| telco                    | 4.83 ms                                                         | 5.64 ms: 1.17x slower                                                          |
| regex_effbot             | 1.66 ms                                                         | 1.98 ms: 1.19x slower                                                          |
| async_generators         | 241 ms                                                          | 305 ms: 1.27x slower                                                           |
| Geometric mean           | (ref)                                                           | 1.23x faster                                                                   |

Benchmark hidden because not significant (3): logging_simple, genshi_text, logging_format
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1_win32-x86-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240605-3.14.0a0-e83ce85-JIT/bm-20240605-pythonperf1_win32-x86-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown